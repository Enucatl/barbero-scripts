-- Podcast Assembler -- standard REAPER 7.46+; no SWS or external dependencies.
-- Load this file with Actions > New action > Load ReaScript, then run it.
-- The first run prepares VOICE. Later runs rebuild from CURRENT voice edits.
-- Music keeps its prepared duration unless another cue requires a shorter intro.

local SCRIPT_VERSION = "1.0"
local NAMESPACE = "PODCAST_ASSEMBLER"
local ASSET_FILES = {
    intro = "intro.wav",
    outro = "outro.wav",
    jingle_a = "jingle_a.wav",
    jingle_b = "jingle_b.wav",
    room_tone = "room_tone.wav",
}
local JINGLE_ORDER = {"jingle_b", "jingle_a"}

-- All user-adjustable settings are here. Times are timeline seconds.
local CONFIG = {
    DIAGNOSTICS = true, -- Detailed REAPER console trace; warnings/errors always print.
    START_TRIM = 0.100,
    END_TRIM = 0.100,
    EDGE_FADE = 0.008,
    SHORT_GAP_THRESHOLD = 2.000,
    ROOM_TONE_BEFORE = 1.0,
    ROOM_TONE_AFTER = 1.0,
    ROOM_TONE_FADE = 0.5,
    MUSIC_TRACK_DB = -20.0,
    MUSIC_FULL_DB = -3.0,
    MUSIC_DUCKED_DB = -18.0,
    INTRO_PRE_ROLL = 16.0,
    INTRO_DUCK_TIME = 4.0, -- Gradual duck centered on the voice entrance.
    OUTRO_UNDER_VOICE_TIME = 22.0,
    OUTRO_UNDER_VOICE_DB = -10.0,
    OUTRO_FINAL_RISE_TIME = 1.5,
    OUTRO_FADEOUT_TIME = 3.0,
    -- Minimum post-roll, limited by the WAV. The complete outro is preserved;
    -- a longer prepared outro therefore continues beyond this minimum.
    OUTRO_POST_ROLL = 3.0,
    JINGLE_FADE_TIME = 0.5,
    JINGLE_OVERLAP_BEFORE = 9.0, -- Quiet lead-in under outgoing speech.
    JINGLE_OVERLAP_AFTER = 2.0, -- Tail under incoming speech.
    AUTOMATION_TAIL = 0.050, -- Keep REAPER's automation edge blend beyond the audio.
    POSITION_EPSILON = 0.0001,
}

local r = reaper
local ITEM_MARKER = "P_EXT:" .. NAMESPACE
local VOICE_STATE = "P_EXT:" .. NAMESPACE .. "_VOICE_PREPARED"
local POOL_MARKER = "P_POOL_EXT:" .. NAMESPACE
local MUSIC_MARKER = NAMESPACE .. ":MUSIC"
local KINDS = {INTRO = true, OUTRO = true, JINGLE = true, ROOM_TONE = true}
local warnings, loose_sources = {}, {}
local current_stage = "startup"

local function diagnostic(format, ...)
    if CONFIG.DIAGNOSTICS then
        r.ShowConsoleMsg("[Podcast Assembler] " .. string.format(format, ...) .. "\n")
    end
end

local function stage(name)
    current_stage = name
    diagnostic("STAGE: %s", name)
end

local function fail(message)
    error(message, 0)
end

local function warn(message)
    warnings[#warnings + 1] = message
    r.ShowConsoleMsg("[Podcast Assembler] WARNING: " .. message .. "\n")
end

local function finite(value)
    return type(value) == "number" and value == value
        and value ~= math.huge and value ~= -math.huge
end

local function db_to_amp(db)
    return 10 ^ (db / 20)
end

local FULL = db_to_amp(CONFIG.MUSIC_FULL_DB)
local DUCKED = db_to_amp(CONFIG.MUSIC_DUCKED_DB)

local function item_value(item, key)
    return r.GetMediaItemInfo_Value(item, key)
end

local function owned_item(item)
    local _, marker = r.GetSetMediaItemInfo_String(item, ITEM_MARKER, "", false)
    return KINDS[marker:match("^" .. NAMESPACE .. ":(.+)$")] == true
end

local function release_sources()
    local count = 0
    for source in pairs(loose_sources) do
        r.PCM_Source_Destroy(source)
        loose_sources[source] = nil
        count = count + 1
    end
    diagnostic("Source cleanup: destroyed %d unattached source(s)", count)
end

local function open_source(path, label)
    diagnostic("Open source: %s; path=%s", label, path)
    if not r.file_exists(path) then
        fail("Missing " .. label .. " asset.\nAttempted path: " .. path)
    end
    local source = r.PCM_Source_CreateFromFile(path)
    if not source then
        fail("Unable to load " .. label .. " asset.\nAttempted path: " .. path)
    end
    loose_sources[source] = true
    local length, is_qn = r.GetMediaSourceLength(source)
    if is_qn or not finite(length) or length <= CONFIG.POSITION_EPSILON then
        fail("Invalid or empty " .. label .. " audio source.\nAttempted path: " .. path)
    end
    diagnostic("Source validated: %s; length=%.6fs", label, length)
    return source, length
end

local function validate_config()
    stage("validate configuration")
    local version = tonumber(r.GetAppVersion():match("^(%d+%.%d+)"))
    if not version or version < 7.46 then
        fail("Podcast Assembler requires standard REAPER 7.46 or newer.")
    end
    for key, value in pairs(CONFIG) do
        if key ~= "DIAGNOSTICS" then
            if not finite(value) or (not key:match("_DB$") and value < 0) then
                fail("Invalid configuration: " .. key)
            end
        elseif type(value) ~= "boolean" then
            fail(key .. " must be true or false.")
        end
    end
    for _, key in ipairs({"POSITION_EPSILON", "SHORT_GAP_THRESHOLD",
            "OUTRO_FADEOUT_TIME", "JINGLE_FADE_TIME", "AUTOMATION_TAIL"}) do
        if CONFIG[key] <= 0 then fail(key .. " must be greater than zero.") end
    end
    if CONFIG.POSITION_EPSILON >= CONFIG.SHORT_GAP_THRESHOLD
            or CONFIG.MUSIC_DUCKED_DB > CONFIG.MUSIC_FULL_DB
            or CONFIG.OUTRO_UNDER_VOICE_DB > CONFIG.MUSIC_FULL_DB
            or not finite(FULL) or not finite(DUCKED) then
        fail("Invalid threshold, tolerance, or music levels in CONFIG.")
    end
    local keys = {}
    for key in pairs(CONFIG) do keys[#keys + 1] = key end
    table.sort(keys)
    for _, key in ipairs(keys) do diagnostic("CONFIG %s=%s", key, tostring(CONFIG[key])) end
    diagnostic("Music amplitudes: full=%.9f; ducked=%.9f; silence=0", FULL, DUCKED)
end

local function load_assets()
    stage("validate assets")
    local _, script_path = r.get_action_context()
    script_path = script_path:gsub("\\", "/")
    -- Podcast_Assembler.lua -> barbero_scripts -> src -> repository root.
    local root = script_path:match("^(.*)/[^/]+/[^/]+/[^/]+$")
    if not root then fail("Cannot resolve repository root from script: " .. script_path) end
    diagnostic("Script path: %s; repository root: %s", script_path, root)
    local assets = {}
    for _, key in ipairs({"intro", "outro", "jingle_a", "jingle_b", "room_tone"}) do
        local path = root .. "/assets/audio/" .. ASSET_FILES[key]
        local source, length = open_source(path, key)
        assets[key] = {path = path, length = length}
        r.PCM_Source_Destroy(source)
        loose_sources[source] = nil
    end
    return assets
end

local function find_tracks()
    stage("identify tracks and processing state")
    local named, candidates, selected = {}, {}, {}
    local flat = true
    for i = 0, r.CountTracks(0) - 1 do
        local track = r.GetTrack(0, i)
        local _, name = r.GetTrackName(track)
        diagnostic("Track %d: name=%q; GUID=%s; items=%d; folder-depth=%d",
            i + 1, name, r.GetTrackGUID(track), r.CountTrackMediaItems(track),
            r.GetMediaTrackInfo_Value(track, "I_FOLDERDEPTH"))
        if name == "MUSIC" or name == "VOICE" or name == "ROOM TONE" then
            if named[name] then fail("Ambiguous project: multiple tracks named " .. name .. ".") end
            named[name] = track
        end
        if name ~= "MUSIC" and name ~= "ROOM TONE" then
            candidates[#candidates + 1] = track
        end
        selected[track] = r.IsTrackSelected(track)
        flat = flat and r.GetMediaTrackInfo_Value(track, "I_FOLDERDEPTH") == 0
    end
    if not named.VOICE then
        if #candidates ~= 1 then
            fail("Cannot identify VOICE: name the spoken-word source track VOICE, "
                .. "or start with one source track. No tracks were changed.")
        end
        named.VOICE = candidates[1]
    end
    -- Track P_EXT participates in Undo/save/copy. Project extstate alone does
    -- not participate in REAPER Undo, so it is only a version mirror below.
    local _, prepared = r.GetSetMediaTrackInfo_String(named.VOICE, VOICE_STATE, "", false)
    if prepared ~= "" and prepared ~= SCRIPT_VERSION then
        fail("This project was prepared by Podcast Assembler " .. prepared
            .. ". This version cannot migrate that state safely.")
    end
    diagnostic("VOICE authority: GUID=%s; preparation marker=%q; mode=%s",
        r.GetTrackGUID(named.VOICE), prepared, prepared ~= "" and "rebuild current edits" or "first preparation")
    diagnostic("Tracks: MUSIC=%s; ROOM TONE=%s; safe to reorder=%s",
        named.MUSIC and "reuse" or "create", named["ROOM TONE"] and "reuse" or "create", tostring(flat))
    return {voice = named.VOICE, music = named.MUSIC, room = named["ROOM TONE"],
        prepared = prepared ~= "", selected = selected, flat = flat}
end

local function sort_voice(voice)
    table.sort(voice, function(a, b)
        if a.position == b.position then return a.index < b.index end
        return a.position < b.position
    end)
end

local function plan_voice(tracks, assets)
    stage("plan voice preparation")
    local voice = {}
    for i = 0, r.CountTrackMediaItems(tracks.voice) - 1 do
        local item = r.GetTrackMediaItem(tracks.voice, i)
        if not owned_item(item) then
            local position, length = item_value(item, "D_POSITION"), item_value(item, "D_LENGTH")
            local label = "VOICE item " .. (i + 1)
            diagnostic("%s input: position=%.6f; length=%.6f; takes=%d; locked=%s",
                label, position, length, r.CountTakes(item), tostring(item_value(item, "C_LOCK") ~= 0))
            if not finite(position) or position < 0 or not finite(length)
                    or length <= CONFIG.POSITION_EPSILON then
                warn(label .. " has an invalid position or length; skipped.")
            else
                local entry = {item = item, position = position, length = length,
                    original_position = position, original_length = length,
                    index = i, label = label, takes = {}}
                local safe = length > CONFIG.START_TRIM + CONFIG.END_TRIM + CONFIG.POSITION_EPSILON
                local active = r.GetActiveTake(item)
                if not active or r.TakeIsMIDI(active) then
                    fail(label .. " has no active audio take; cannot identify spoken audio safely.")
                end
                diagnostic("%s active take: rate=%.6f; source-offset=%.6f",
                    label, r.GetMediaItemTakeInfo_Value(active, "D_PLAYRATE"),
                    r.GetMediaItemTakeInfo_Value(active, "D_STARTOFFS"))
                if not tracks.prepared then
                    for t = 0, r.CountTakes(item) - 1 do
                        local take = r.GetTake(item, t)
                        if not take then
                            -- REAPER's empty comp takes count toward CountTakes.
                            safe = false
                        else
                            local rate = r.GetMediaItemTakeInfo_Value(take, "D_PLAYRATE")
                            local offset = r.GetMediaItemTakeInfo_Value(take, "D_STARTOFFS")
                            diagnostic("%s take %d: rate=%.6f; source-offset=%.6f -> %.6f; stretch-markers=%d; envelopes=%d",
                                label, t + 1, rate, offset, offset + CONFIG.START_TRIM * rate,
                                r.GetTakeNumStretchMarkers(take), r.CountTakeEnvelopes(take))
                            -- Moving take envelopes/stretch markers needs a different trim map.
                            -- Preserve such edited recordings rather than changing their sound.
                            if r.TakeIsMIDI(take) or not finite(rate) or rate <= 0
                                    or not finite(offset) or offset < 0
                                    or r.GetTakeNumStretchMarkers(take) > 0
                                    or r.CountTakeEnvelopes(take) > 0
                                    or item_value(item, "C_LOCK") ~= 0 then
                                safe = false
                            end
                            entry.takes[#entry.takes + 1] = {take = take,
                                offset = offset + CONFIG.START_TRIM * rate}
                        end
                    end
                    if safe then
                        entry.position = position + CONFIG.START_TRIM
                        entry.length = length - CONFIG.START_TRIM - CONFIG.END_TRIM
                        entry.trim = true
                    else
                        warn(label .. " is too short, locked, or has unsupported take edits; "
                            .. "edge trimming skipped.")
                    end
                end
                voice[#voice + 1] = entry
            end
        else
            diagnostic("VOICE item %d: generated content excluded", i + 1)
        end
    end
    if #voice == 0 then fail("VOICE contains no usable audio items.") end
    sort_voice(voice)
    if not tracks.prepared then
        local removed = 0
        for i = 2, #voice do
            local previous, current = voice[i - 1], voice[i]
            current.position = current.position - removed
            local previous_end = previous.position + previous.length
            local gap = current.position - previous_end
            -- Classify before trims; ripple removed time through all later clips.
            local recorded_gap = current.original_position
                - previous.original_position - previous.original_length
            diagnostic("Gap before %s: %.6fs; threshold=%.6fs; decision=%s",
                current.label, recorded_gap, CONFIG.SHORT_GAP_THRESHOLD,
                recorded_gap < CONFIG.SHORT_GAP_THRESHOLD - CONFIG.POSITION_EPSILON and "collapse to previous end" or "preserve")
            -- Gaps within tolerance of the threshold are treated as equal.
            if recorded_gap < CONFIG.SHORT_GAP_THRESHOLD - CONFIG.POSITION_EPSILON then
                if gap < -CONFIG.POSITION_EPSILON then
                    warn(current.label .. " overlapped the previous clip; moved to its end.")
                end
                removed = removed + gap
                current.position = previous_end
            end
        end
        local desired_pre = math.min(CONFIG.INTRO_PRE_ROLL, assets.intro.length / 2)
        local shift = math.max(0, desired_pre - voice[1].position)
        diagnostic("Intro pre-roll: desired=%.6fs; uniform VOICE shift=%.6fs", desired_pre, shift)
        if shift > 0 then
            for _, entry in ipairs(voice) do
                entry.position = entry.position + shift
            end
        end
        for _, entry in ipairs(voice) do
            if item_value(entry.item, "C_LOCK") ~= 0
                    and math.abs(entry.position - entry.original_position) > CONFIG.POSITION_EPSILON then
                fail(entry.label .. " is locked and would need moving for gap removal or intro pre-roll.")
            end
        end
    else
        diagnostic("VOICE already prepared: preserve source edits; fit jingle breaks to speech overlaps")
    end
    for index, entry in ipairs(voice) do
        diagnostic("VOICE final plan %d (%s): position=%.6f; length=%.6f; end=%.6f; trim=%s",
            index, entry.label, entry.position, entry.length, entry.position + entry.length, tostring(entry.trim == true))
    end
    return voice
end

local function find_breaks(voice)
    stage("detect final voice breaks and seams")
    local breaks, seams = {}, {}
    local frontier = voice[1].position + voice[1].length
    for i = 2, #voice do
        local entry = voice[i]
        local gap = entry.position - frontier
        diagnostic("Final gap before %s: [%.6f, %.6f]; duration=%.6fs; kind=%s",
            entry.label, frontier, entry.position, gap,
            gap >= CONFIG.SHORT_GAP_THRESHOLD - CONFIG.POSITION_EPSILON and "long break"
                or (math.abs(gap) <= CONFIG.POSITION_EPSILON and "edit seam" or "preserved manual gap/overlap"))
        if gap >= CONFIG.SHORT_GAP_THRESHOLD - CONFIG.POSITION_EPSILON then
            breaks[#breaks + 1] = {start = frontier, finish = entry.position}
        elseif math.abs(gap) <= CONFIG.POSITION_EPSILON then
            seams[#seams + 1] = frontier
        end
        -- Existing manual overlaps are preserved on rebuilds; contained clips
        -- cannot manufacture a false break inside another clip's speech.
        if entry.position + entry.length > frontier then
            frontier = entry.position + entry.length
        end
    end
    diagnostic("Detected %d long break(s), %d seam(s); VOICE end=%.6f", #breaks, #seams, frontier)
    return breaks, seams, frontier
end

local function point(cue, time, value)
    local last = cue.points[#cue.points]
    if last and math.abs(time - last.time) < CONFIG.POSITION_EPSILON then
        last.value = value
    else
        assert(not last or time > last.time, "Backwards music automation timing")
        cue.points[#cue.points + 1] = {time = time, value = value}
    end
end

local function space_jingles(voice, assets)
    stage("fit jingle breaks")
    local shift, index = 0, 0
    local frontier = voice[1].position + voice[1].length
    for i = 2, #voice do
        local entry = voice[i]
        entry.position = entry.position + shift
        local gap = entry.position - frontier
        if gap >= CONFIG.SHORT_GAP_THRESHOLD - CONFIG.POSITION_EPSILON then
            index = index + 1
            local key = JINGLE_ORDER[(index - 1) % #JINGLE_ORDER + 1]
            local extra = math.max(CONFIG.SHORT_GAP_THRESHOLD, assets[key].length
                - CONFIG.JINGLE_OVERLAP_BEFORE - CONFIG.JINGLE_OVERLAP_AFTER) - gap
            shift = shift + extra
            entry.position = entry.position + extra
            diagnostic("JINGLE spacing %d (%s): gap=%.6f -> %.6f; ripple=%.6f",
                index, key, gap, gap + extra, shift)
        end
        if item_value(entry.item, "C_LOCK") ~= 0
                and math.abs(entry.position - item_value(entry.item, "D_POSITION")) > CONFIG.POSITION_EPSILON then
            fail(entry.label .. " is locked and would need moving for jingle spacing.")
        end
        frontier = math.max(frontier, entry.position + entry.length)
    end
end

local function jingle_start(gap, length)
    local overlap = CONFIG.JINGLE_OVERLAP_BEFORE + CONFIG.JINGLE_OVERLAP_AFTER
    local available = length - (gap.finish - gap.start)
    if available <= 0 or overlap == 0 then
        return (gap.start + gap.finish - length) / 2
    end
    return gap.start - available * CONFIG.JINGLE_OVERLAP_BEFORE / overlap
end

local function plan_assembly(voice, assets)
    local breaks, seams, voice_end = find_breaks(voice)
    stage("plan music and room tone")
    local music, room = {}, {}
    local last = voice[#voice]
    -- Restrict overlap to the final spoken section, and reserve post-roll.
    local under = math.min(CONFIG.OUTRO_UNDER_VOICE_TIME, last.length,
        math.max(0, assets.outro.length - CONFIG.OUTRO_POST_ROLL))
    local outro_start = voice_end - under
    local outro = {asset = "outro", kind = "OUTRO", position = outro_start,
        length = assets.outro.length, points = {}}
    -- Rise throughout the overlap, reaching full volume when speech ends.
    point(outro, outro_start, 0)
    if under > CONFIG.POSITION_EPSILON then
        point(outro, voice_end - math.min(CONFIG.OUTRO_FINAL_RISE_TIME, under / 2),
            db_to_amp(CONFIG.OUTRO_UNDER_VOICE_DB))
    end
    local full_start = under > 0 and voice_end
        or outro_start + math.min(CONFIG.JINGLE_FADE_TIME, outro.length / 2)
    point(outro, full_start, FULL)
    local outro_end = outro_start + outro.length
    local outro_fade = math.min(CONFIG.OUTRO_FADEOUT_TIME, (outro_end - voice_end) / 2)
    point(outro, outro_end - outro_fade, FULL)
    point(outro, outro_end, 0)
    diagnostic("OUTRO: start=%.6f; end=%.6f; under-voice=%.6fs; post-roll=%.6fs",
        outro_start, outro_end, under, outro_end - voice_end)

    local voice_start = voice[1].position
    local intro_end = math.min(assets.intro.length, outro_start)
    if breaks[1] then
        local first_jingle = jingle_start(breaks[1], assets[JINGLE_ORDER[1]].length)
        intro_end = math.min(intro_end, math.max(voice_start, first_jingle))
    end
    if intro_end > CONFIG.POSITION_EPSILON then
        -- The green track envelope controls the whole intro. End the media at
        -- its fade endpoint so later cues cannot revive an inaudible tail.
        local intro = {asset = "intro", kind = "INTRO", position = 0,
            length = intro_end, points = {}}
        local duck_start = math.max(0, math.min(voice_start, intro_end) - CONFIG.INTRO_DUCK_TIME / 2)
        local duck_end = math.min(intro_end, voice_start + CONFIG.INTRO_DUCK_TIME / 2)
        point(intro, 0, FULL)
        point(intro, duck_start, FULL)
        if voice_start < intro_end then point(intro, duck_end, DUCKED) end
        point(intro, intro_end, 0)
        music[#music + 1] = intro
        diagnostic("INTRO: start=0; voice-entry=%.6f; duck-start=%.6f; duck-end=%.6f; fade-end=%.6f; under-voice=%.6fs",
            voice_start, duck_start, duck_end, intro_end, math.max(0, intro_end - voice_start))
        if intro_end < assets.intro.length then warn("Intro shortened to avoid the next music cue.") end
    else
        warn("No usable time before outro; intro skipped.")
    end

    for index, gap in ipairs(breaks) do
        local key = JINGLE_ORDER[(index - 1) % #JINGLE_ORDER + 1]
        local length = assets[key].length
        -- Bias the complete WAV toward outgoing speech for a quiet lead-in.
        local earliest = music[#music] and music[#music].position + music[#music].length or 0
        local latest = outro_start
        local start = jingle_start(gap, length)
        start = math.max(earliest, math.min(start, latest - length))
        local finish = start + length
        diagnostic("JINGLE break %d: asset=%s; source=%.6fs; break=[%.6f, %.6f]; allowed=[%.6f, %.6f]; proposed=[%.6f, %.6f]",
            index, ASSET_FILES[key], length, gap.start, gap.finish, earliest, latest, start, finish)
        if length > latest - earliest + CONFIG.POSITION_EPSILON
                or finish <= gap.start or start >= gap.finish then
            warn(string.format("Long break %d (%.3fs): %s (%.3fs) conflicts with another music cue; skipped.",
                index, gap.finish - gap.start, ASSET_FILES[key], length))
        else
            local cue = {asset = key, kind = "JINGLE", position = start, length = length, points = {}}
            local clear_start, clear_end = math.max(start, gap.start), math.min(finish, gap.finish)
            -- Proportions preserve the musical shape for both prepared WAVs:
            -- quiet opening, gradual rise, short peak, longer fade to silence.
            point(cue, start, 0)
            point(cue, start + length * 0.025, DUCKED)
            point(cue, start + length * 0.37, DUCKED)
            point(cue, start + length * 0.56, FULL)
            point(cue, start + length * 0.75, FULL)
            point(cue, finish, 0)
            music[#music + 1] = cue
            diagnostic("JINGLE accepted: clear=[%.6f, %.6f]; left-overlap=%.6fs; right-overlap=%.6fs",
                clear_start, clear_end, math.max(0, gap.start - start), math.max(0, finish - gap.finish))
        end
    end
    music[#music + 1] = outro

    local desired = CONFIG.ROOM_TONE_BEFORE + CONFIG.ROOM_TONE_AFTER
    local patch_length = math.min(desired, assets.room_tone.length)
    if patch_length < desired then warn("Room-tone source is short; seam patches reduced to source length.") end
    if patch_length > CONFIG.POSITION_EPSILON then
        for index, seam in ipairs(seams) do
            local before = patch_length * CONFIG.ROOM_TONE_BEFORE / desired
            local start = math.max(0, seam - before)
            local length = math.min(patch_length, seam + patch_length - before - start)
            -- Reproducible offsets covering the source without repetition or stretch.
            local fraction = (index * 0.618033988749895) % 1
            room[#room + 1] = {asset = "room_tone", kind = "ROOM_TONE",
                position = start, length = length,
                offset = fraction * math.max(0, assets.room_tone.length - length)}
            diagnostic("ROOM_TONE seam %d: seam=%.6f; position=%.6f; length=%.6f; source-offset=%.6f",
                index, seam, start, length, room[#room].offset)
        end
    end
    diagnostic("Assembly plan: %d music item(s); %d room-tone patch(es)", #music, #room)
    return music, room
end

local function volume_envelope(track)
    return track and r.GetTrackEnvelopeByChunkName(track, "<VOLENV2")
end

local function inspect_automation(tracks, music)
    stage("validate automation ownership")
    local env = volume_envelope(tracks.music)
    local owned, used_pools, instances = nil, {}, {}
    -- Pool IDs are project-wide, including take and master-track envelopes.
    local function inspect(env_to_check)
        for i = 0, r.CountAutomationItems(env_to_check) - 1 do
            local pool = r.GetSetAutomationItemInfo(env_to_check, i, "D_POOL_ID", 0, false)
            used_pools[pool] = true
            instances[pool] = (instances[pool] or 0) + 1
            local _, marker = r.GetSetAutomationItemInfo_String(env_to_check, i, POOL_MARKER, "", false)
            diagnostic("Automation item: index=%d; pool=%d; marker=%q; on-MUSIC-volume=%s",
                i, pool, marker, tostring(env_to_check == env))
            if marker == MUSIC_MARKER then
                if env_to_check ~= env or owned then
                    fail("Generated music automation was copied or moved. Remove extra copies "
                        .. "or restore its original MUSIC Volume envelope before rebuilding.")
                end
                owned = {index = i, pool = pool}
            elseif env_to_check == env then
                local start = r.GetSetAutomationItemInfo(env, i, "D_POSITION", 0, false)
                local length = r.GetSetAutomationItemInfo(env, i, "D_LENGTH", 0, false)
                local first = music[1].position
                local last = music[#music].position + music[#music].length + CONFIG.AUTOMATION_TAIL
                if start < last and start + length > first then
                    fail("A user automation item overlaps the generated music range. "
                        .. "Move it outside that range before rebuilding; it will not be overwritten.")
                end
            end
        end
    end
    for t = -1, r.CountTracks(0) - 1 do
        local track = t == -1 and r.GetMasterTrack(0) or r.GetTrack(0, t)
        for e = 0, r.CountTrackEnvelopes(track) - 1 do inspect(r.GetTrackEnvelope(track, e)) end
        for i = 0, r.CountTrackMediaItems(track) - 1 do
            local item = r.GetTrackMediaItem(track, i)
            for take_index = 0, r.CountTakes(item) - 1 do
                local take = r.GetTake(item, take_index)
                if take then
                    for e = 0, r.CountTakeEnvelopes(take) - 1 do inspect(r.GetTakeEnvelope(take, e)) end
                end
            end
        end
    end
    if owned and instances[owned.pool] ~= 1 then fail("Generated music automation has pooled copies; unpool them first.") end
    local pool = 0
    for id in pairs(used_pools) do pool = math.max(pool, id + 1) end
    diagnostic("MUSIC Volume: envelope=%s; generated automation=%s; target pool=%d",
        env and "reuse" or "create", owned and "reuse" or "create", owned and owned.pool or pool)
    return env, owned, pool
end

local function append_chunk_block(chunk, block)
    local body = chunk:match("^(.*)\n%s*>%s*$")
    if not body then fail("Unexpected REAPER state chunk; no envelope could be created.") end
    return body .. "\n" .. block .. ">\n"
end

local function establish_tracks(tracks)
    stage("establish MUSIC / VOICE / ROOM TONE")
    local function create(name)
        local index = r.CountTracks(0)
        r.InsertTrackAtIndex(index, true)
        local track = r.GetTrack(0, index)
        assert(track, "Unable to create " .. name .. " track")
        assert(r.GetSetMediaTrackInfo_String(track, "P_NAME", name, true), "Unable to name track")
        diagnostic("Created track: %s; GUID=%s", name, r.GetTrackGUID(track))
        return track
    end
    assert(r.GetSetMediaTrackInfo_String(tracks.voice, "P_NAME", "VOICE", true), "Unable to name VOICE")
    tracks.music = tracks.music or create("MUSIC")
    tracks.room = tracks.room or create("ROOM TONE")
    assert(r.SetMediaTrackInfo_Value(tracks.music, "D_VOL", db_to_amp(CONFIG.MUSIC_TRACK_DB)),
        "Unable to set MUSIC track fader")
    if tracks.flat then
        diagnostic("Reorder podcast tracks to MUSIC, VOICE, ROOM TONE; restore original track selection")
        -- Move only our three tracks. Unrelated tracks retain their relative order.
        for target, track in ipairs({tracks.music, tracks.voice, tracks.room}) do
            for i = 0, r.CountTracks(0) - 1 do r.SetTrackSelected(r.GetTrack(0, i), false) end
            r.SetTrackSelected(track, true)
            assert(r.ReorderSelectedTracks(target - 1, 0), "Unable to reorder podcast tracks")
        end
        for i = 0, r.CountTracks(0) - 1 do
            local track = r.GetTrack(0, i)
            r.SetTrackSelected(track, tracks.selected[track] == true)
        end
    else
        warn("Track folders detected; track order preserved to protect folder routing.")
    end
end

local function set_fades(item, length, requested, label)
    local fade = math.min(requested, length / 2)
    if fade < requested then warn(label .. ": edge fades reduced for short item.") end
    r.SetMediaItemInfo_Value(item, "D_FADEINLEN", fade)
    r.SetMediaItemInfo_Value(item, "D_FADEOUTLEN", fade)
    r.SetMediaItemInfo_Value(item, "D_FADEINLEN_AUTO", -1)
    r.SetMediaItemInfo_Value(item, "D_FADEOUTLEN_AUTO", -1)
    diagnostic("%s fades: requested=%.6fs; applied=%.6fs at each edge", label, requested, fade)
end

local function prepare_voice(voice)
    stage("apply voice timing and one-time trims")
    for _, entry in ipairs(voice) do
        diagnostic("Apply %s: position %.6f -> %.6f; length %.6f -> %.6f; trim=%s",
            entry.label, item_value(entry.item, "D_POSITION"), entry.position,
            item_value(entry.item, "D_LENGTH"), entry.length, tostring(entry.trim == true))
        if entry.trim then
            for _, take in ipairs(entry.takes) do
                assert(r.SetMediaItemTakeInfo_Value(take.take, "D_STARTOFFS", take.offset), "Unable to trim take")
            end
            assert(r.SetMediaItemInfo_Value(entry.item, "D_LENGTH", entry.length), "Unable to trim voice end")
            set_fades(entry.item, entry.length, CONFIG.EDGE_FADE, entry.label)
        end
        assert(r.SetMediaItemInfo_Value(entry.item, "D_POSITION", entry.position), "Unable to position voice")
    end
end

local function delete_generated_items()
    stage("remove previously generated media")
    local removed = 0
    for t = 0, r.CountTracks(0) - 1 do
        local track = r.GetTrack(0, t)
        for i = r.CountTrackMediaItems(track) - 1, 0, -1 do
            local item = r.GetTrackMediaItem(track, i)
            if owned_item(item) then
                local _, marker = r.GetSetMediaItemInfo_String(item, ITEM_MARKER, "", false)
                diagnostic("Remove owned item: %s; track=%d; position=%.6f; length=%.6f",
                    marker, t + 1, item_value(item, "D_POSITION"), item_value(item, "D_LENGTH"))
                assert(r.DeleteTrackMediaItem(track, item), "Unable to remove generated item")
                removed = removed + 1
            end
        end
    end
    diagnostic("Removed %d generated item(s); retained all unmarked items", removed)
end

local function insert_item(track, cue)
    diagnostic("Insert %s: file=%s; position=%.6f; length=%.6f; source-offset=%.6f; rate=1",
        cue.kind, ASSET_FILES[cue.asset], cue.position, cue.length, cue.offset or 0)
    local item = assert(r.AddMediaItemToTrack(track), "Unable to insert " .. cue.kind)
    local take = assert(r.AddTakeToMediaItem(item), "Unable to create media take")
    assert(r.SetMediaItemTake_Source(take, cue.source), "Unable to attach " .. cue.kind .. " source")
    -- Ownership now belongs to the take. Only unattached preflight sources
    -- are destroyed by our cleanup; each generated take has its own source.
    loose_sources[cue.source] = nil
    r.SetMediaItemInfo_Value(item, "D_POSITION", cue.position)
    r.SetMediaItemInfo_Value(item, "D_LENGTH", cue.length)
    r.SetMediaItemInfo_Value(item, "B_LOOPSRC", 0)
    r.SetMediaItemInfo_Value(item, "C_BEATATTACHMODE", 0)
    r.SetMediaItemTakeInfo_Value(take, "D_STARTOFFS", cue.offset or 0)
    r.SetMediaItemTakeInfo_Value(take, "D_PLAYRATE", 1)
    assert(r.GetSetMediaItemInfo_String(item, ITEM_MARKER, NAMESPACE .. ":" .. cue.kind, true), "Unable to mark item")
    r.GetSetMediaItemTakeInfo_String(take, "P_NAME", NAMESPACE .. ":" .. cue.kind .. " / " .. ASSET_FILES[cue.asset], true)
    if cue.kind == "ROOM_TONE" then
        set_fades(item, cue.length, CONFIG.ROOM_TONE_FADE, "Room-tone patch")
    else
        -- The mix is on the track envelope, never default item fade handles.
        set_fades(item, cue.length, 0, cue.kind)
    end
end

local function write_automation(tracks, music, env, owned, fresh_pool)
    stage("write editable MUSIC Volume automation")
    if not env then
        -- REAPER has no direct create-track-envelope API. Append ONLY the
        -- missing post-fader Volume block to the existing complete track chunk.
        local ok, chunk = r.GetTrackStateChunk(tracks.music, "", false)
        assert(ok, "Unable to read MUSIC track")
        local block = "<VOLENV2\nACT 1 -1\nVIS 1 1 1\nARM 0\nDEFSHAPE 0 -1 -1\nPT 0 1 0\n>\n"
        assert(r.SetTrackStateChunk(tracks.music, append_chunk_block(chunk, block), false), "Unable to create MUSIC Volume")
        env = assert(volume_envelope(tracks.music), "Unable to obtain MUSIC Volume envelope")
    end
    for _, attribute in ipairs({"ACTIVE", "VISIBLE", "SHOWLANE"}) do
        assert(r.GetSetEnvelopeInfo_String(env, attribute, "1", true), "Unable to show MUSIC Volume")
    end
    r.GetSetEnvelopeInfo_String(env, "ARM", "0", true)
    -- Trim/Read is required for playback without writing over generated/manual
    -- automation; pan, FX and routing are otherwise left alone.
    r.SetTrackAutomationMode(tracks.music, 0)
    local start = music[1].position
    -- REAPER blends back to the underlying envelope near the AI's right edge.
    -- Keep that blend after the audio, with its final silence point inside.
    local finish = music[#music].position + music[#music].length + CONFIG.AUTOMATION_TAIL
    local index = owned and owned.index
    if not index then
        -- A negative pool ID would absorb underlying manual points. Allocate
        -- a fresh project-wide nonnegative ID so those points stay untouched.
        index = r.InsertAutomationItem(env, fresh_pool, start, finish - start)
        assert(index >= 0, "Unable to create generated music automation")
    end
    -- Reuse one positively marked AI: no action IDs or AI-chunk deletion.
    -- Full-loop indexing also clears points outside a manually trimmed AI.
    -- Clear a newly allocated pool too, in case REAPER retained an orphaned
    -- pool with that ID after its last (now absent) instance was deleted.
    local full_index = index + 0x10000000
    local old_points = r.CountEnvelopePointsEx(env, full_index)
    diagnostic("Automation %s: index=%d; pool=%d; range=[%.6f, %.6f]; remove %d owned point(s)",
        owned and "reuse" or "create", index, owned and owned.pool or fresh_pool, start, finish, old_points)
    for p = old_points - 1, 0, -1 do
        assert(r.DeleteEnvelopePointEx(env, full_index, p), "Unable to clear generated automation")
    end
    for key, value in pairs({D_POSITION = start, D_LENGTH = finish - start,
            D_STARTOFFS = 0, D_PLAYRATE = 1, D_BASELINE = 0,
            D_AMPLITUDE = 1, D_LOOPSRC = 0, D_MUTE = 0, D_UISEL = 0}) do
        r.GetSetAutomationItemInfo(env, index, key, value, true)
    end
    assert(r.GetSetAutomationItemInfo_String(env, index, POOL_MARKER, MUSIC_MARKER, true), "Unable to mark music automation")
    r.GetSetAutomationItemInfo_String(env, index, "P_POOL_NAME", MUSIC_MARKER, true)
    local scaling = r.GetEnvelopeScalingMode(env)
    diagnostic("MUSIC Volume envelope scaling mode=%d; baseline=0; amplitude=1; source looping=off", scaling)
    local inserted = 0
    for _, cue in ipairs(music) do
        for _, pt in ipairs(cue.points) do
            local scaled_value = r.ScaleToEnvelopeMode(scaling, pt.value)
            assert(r.InsertEnvelopePointEx(env, index, pt.time,
                scaled_value, 0, 0, false, true), "Unable to insert music automation point")
            inserted = inserted + 1
            diagnostic("Envelope point %d: cue=%s; time=%.6f; amp=%.9f; scaled=%.9f; shape=linear",
                inserted, cue.kind, pt.time, pt.value, scaled_value)
        end
    end
    r.Envelope_SortPointsEx(env, index)
    diagnostic("Sorted %d generated envelope point(s); underlying manual points retained", inserted)
    -- Ordinary user points and other automation pools are never deleted.
    -- This one AI controls the assembled range (silence between cues); the
    -- underlying manual envelope remains editable and resumes outside it.
end

local function preflight()
    validate_config()
    local assets = load_assets()
    local tracks = find_tracks()
    local voice = plan_voice(tracks, assets)
    space_jingles(voice, assets)
    local music, room = plan_assembly(voice, assets)
    local env, owned, pool = inspect_automation(tracks, music)
    stage("preload generated media sources before mutation")
    -- Load EVERY required generated source before opening the undo block.
    -- A predictable source-open failure must not leave a partly edited project.
    for _, cues in ipairs({music, room}) do
        for _, cue in ipairs(cues) do cue.source = open_source(assets[cue.asset].path, cue.asset) end
    end
    diagnostic("Validation complete: project changes may begin")
    return {tracks = tracks, voice = voice, music = music, room = room,
        env = env, owned = owned, pool = pool}
end

local function assemble(plan)
    establish_tracks(plan.tracks)
    prepare_voice(plan.voice)
    delete_generated_items()
    -- Create the track envelope before inserting media: track chunks can
    -- replace item/take pointers, so no generated pointers are retained here.
    write_automation(plan.tracks, plan.music, plan.env, plan.owned, plan.pool)
    stage("insert prepared MUSIC assets")
    for _, cue in ipairs(plan.music) do insert_item(plan.tracks.music, cue) end
    stage("insert room-tone seam patches")
    for _, cue in ipairs(plan.room) do insert_item(plan.tracks.room, cue) end
    if not plan.tracks.prepared then
        assert(r.GetSetMediaTrackInfo_String(plan.tracks.voice, VOICE_STATE, SCRIPT_VERSION, true), "Unable to save voice preparation state")
        r.SetProjExtState(0, NAMESPACE, "voice_guid", r.GetTrackGUID(plan.tracks.voice))
        r.SetProjExtState(0, NAMESPACE, "voice_prepared", SCRIPT_VERSION)
    end
    r.SetProjExtState(0, NAMESPACE, "script_version", SCRIPT_VERSION)
    diagnostic("Processing state saved: version=%s; authoritative VOICE marker=%s",
        SCRIPT_VERSION, VOICE_STATE)
end

local function main()
    diagnostic("=== RUN Podcast Assembler %s; REAPER %s ===", SCRIPT_VERSION, r.GetAppVersion())
    local valid, plan = xpcall(preflight, debug.traceback)
    if not valid then
        release_sources()
        r.ShowConsoleMsg("[Podcast Assembler] ERROR during " .. current_stage
            .. "; no project changes made:\n" .. plan .. "\n")
        r.ShowMessageBox(plan, "Podcast Assembler: validation failed", 0)
        return false
    end
    r.Undo_BeginBlock()
    r.PreventUIRefresh(1)
    local ok, message = xpcall(function() assemble(plan) end, debug.traceback)
    -- Always balance refresh, even when media insertion/automation raises.
    r.PreventUIRefresh(-1)
    release_sources()
    r.Undo_EndBlock("Podcast Assembler " .. SCRIPT_VERSION, -1)
    if not ok then
        r.Undo_DoUndo2(0)
        r.ShowConsoleMsg("[Podcast Assembler] ERROR during " .. current_stage
            .. "; project changes undone; UI refresh restored:\n" .. message .. "\n")
        r.ShowMessageBox("Assembly failed; project changes were undone.\n\n" .. message,
            "Podcast Assembler", 0)
    else
        diagnostic("SUCCESS: VOICE=%d item(s); MUSIC=%d generated item(s); ROOM TONE=%d patch(es); warnings=%d; one Undo; UI refresh restored",
            #plan.voice, #plan.music, #plan.room, #warnings)
    end
    r.TrackList_AdjustWindows(false)
    r.UpdateArrange()
    return ok
end

-- A sibling native test harness can assert the result; REAPER ignores it when
-- this script is run directly as an action. No test-specific behavior is used.
return main()
