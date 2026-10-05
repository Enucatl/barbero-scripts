-- Native REAPER test/debug harness. Load as a ReaScript alongside the assembler.
-- Run in an EMPTY project with the assembler's default CONFIG. Leaves the
-- assembled fixture editable for inspection; no rendering or extra WAVs needed.
-- Room tone stands in for recorded speech. Main diagnostics print to console.

local r = reaper
local _, script_path = r.get_action_context()
local directory = script_path:gsub("\\", "/"):match("^(.*)/[^/]+$")
local assembler = directory and directory .. "/Podcast_Assembler.lua"
local root = directory and directory:match("^(.*)/[^/]+/[^/]+$")
local pending_sources = {}

local function log(message)
    r.ShowConsoleMsg("[Podcast Assembler Debug] " .. message .. "\n")
end

local function near(actual, expected, label)
    assert(math.abs(actual - expected) < 0.00001,
        string.format("%s: expected %.6f, got %.6f", label, expected, actual))
end

local function generated(track, kind)
    local result = {}
    for i = 0, r.CountTrackMediaItems(track) - 1 do
        local item = r.GetTrackMediaItem(track, i)
        local _, marker = r.GetSetMediaItemInfo_String(item, "P_EXT:PODCAST_ASSEMBLER", "", false)
        if marker == "PODCAST_ASSEMBLER:" .. kind then result[#result + 1] = item end
    end
    table.sort(result, function(a, b)
        return r.GetMediaItemInfo_Value(a, "D_POSITION") < r.GetMediaItemInfo_Value(b, "D_POSITION")
    end)
    return result
end

local function snapshot_voice(voice)
    local result = {}
    for i = 0, r.CountTrackMediaItems(voice) - 1 do
        local item = r.GetTrackMediaItem(voice, i)
        result[#result + 1] = {position = r.GetMediaItemInfo_Value(item, "D_POSITION"),
            length = r.GetMediaItemInfo_Value(item, "D_LENGTH"),
            offset = r.GetMediaItemTakeInfo_Value(r.GetActiveTake(item), "D_STARTOFFS")}
    end
    return result
end

local function run_checks()
    assert(r.CountTracks(0) == 0, "Open an empty REAPER project before running this harness.")
    assert(assembler and root and r.file_exists(assembler), "Cannot locate sibling Podcast_Assembler.lua.")
    -- Two mini gaps followed by four- and five-second breaks. Widen the long
    -- breaks for complete B/A jingles with nine seconds before and two seconds after the break.
    local fixture = {{0, 8, 1, 1}, {8.5, 8, 2, 1.5}, {17, 20, 3, 0.8},
        {41, 20, 2, 1}, {66, 40, 4, 0.5}}
    local expected_positions = {16, 23.8, 31.6}
    for i, filename in ipairs({"jingle_b.wav", "jingle_a.wav"}) do
        local source = assert(r.PCM_Source_CreateFromFile(root .. "/assets/audio/" .. filename),
            "Cannot load jingle fixture: " .. filename)
        local length = r.GetMediaSourceLength(source)
        r.PCM_Source_Destroy(source)
        expected_positions[i + 3] = expected_positions[i + 2] + fixture[i + 2][2] - 0.2 + length - 11
    end
    local path = root .. "/assets/audio/room_tone.wav"
    -- Open fixture sources before creating anything. Each take owns its own
    -- source after attachment; only unattached sources belong to our cleanup.
    for _, spec in ipairs(fixture) do
        local source = assert(r.PCM_Source_CreateFromFile(path), "Cannot load fixture: " .. path)
        pending_sources[source] = true
        local length, is_qn = r.GetMediaSourceLength(source)
        assert(not is_qn and spec[3] + spec[2] * spec[4] <= length, "Room-tone source is too short for fixture.")
        spec.source = source
    end
    log("BEGIN: default configuration, real REAPER APIs, five synthetic voice clips")
    r.Undo_BeginBlock()
    local created, creation_error = xpcall(function()
        r.InsertTrackAtIndex(0, true)
        local voice = assert(r.GetTrack(0, 0), "Cannot create fixture voice track")
        -- Leave the source track unnamed, matching the normal starting project.
        for _, spec in ipairs(fixture) do
            local item = assert(r.AddMediaItemToTrack(voice), "Cannot create fixture item")
            local take = assert(r.AddTakeToMediaItem(item), "Cannot create fixture take")
            assert(r.SetMediaItemTake_Source(take, spec.source), "Cannot attach fixture source")
            pending_sources[spec.source] = nil
            r.SetMediaItemInfo_Value(item, "D_POSITION", spec[1])
            r.SetMediaItemInfo_Value(item, "D_LENGTH", spec[2])
            r.SetMediaItemInfo_Value(item, "B_LOOPSRC", 0)
            r.SetMediaItemTakeInfo_Value(take, "D_STARTOFFS", spec[3])
            r.SetMediaItemTakeInfo_Value(take, "D_PLAYRATE", spec[4])
        end
    end, debug.traceback)
    r.Undo_EndBlock("Podcast Assembler Debug: create fixture", -1)
    if not created then r.Undo_DoUndo2(0); error(creation_error, 0) end

    assert(dofile(assembler), "Assembler first run failed; see its console diagnostics.")
    assert(r.CountTracks(0) == 3, "Expected exactly three podcast tracks")
    for index, name in ipairs({"MUSIC", "VOICE", "ROOM TONE"}) do
        local _, actual = r.GetTrackName(r.GetTrack(0, index - 1))
        assert(actual == name, "Unexpected track order: " .. actual)
    end
    local music, voice, room = r.GetTrack(0, 0), r.GetTrack(0, 1), r.GetTrack(0, 2)
    local snapshot = snapshot_voice(voice)
    assert(#snapshot == #fixture, "Voice item count changed")
    for i, spec in ipairs(fixture) do
        near(snapshot[i].position, expected_positions[i], "VOICE position " .. i)
        near(snapshot[i].length, spec[2] - 0.2, "VOICE length " .. i)
        near(snapshot[i].offset, spec[3] + 0.1 * spec[4], "VOICE source offset " .. i)
    end
    local intro, outro = generated(music, "INTRO"), generated(music, "OUTRO")
    local jingles, patches = generated(music, "JINGLE"), generated(room, "ROOM_TONE")
    assert(#intro == 1 and #outro == 1 and #jingles == 2 and #patches == 2, "Unexpected generated item counts")
    near(r.GetMediaItemInfo_Value(intro[1], "D_POSITION"), 0, "Intro starts at zero")
    for i, item in ipairs({intro[1], jingles[1], jingles[2], outro[1]}) do
        local take = r.GetActiveTake(item)
        local source = r.GetMediaItemTake_Source(take)
        local source_length = r.GetMediaSourceLength(source)
        near(r.GetMediaItemInfo_Value(item, "D_LENGTH"), source_length, "Complete music asset " .. i)
        near(r.GetMediaItemTakeInfo_Value(take, "D_STARTOFFS"), 0, "Music source offset " .. i)
        near(r.GetMediaItemTakeInfo_Value(take, "D_PLAYRATE"), 1, "Music playback rate " .. i)
        assert(r.CountTakeEnvelopes(take) == 0, "Music unexpectedly has a take envelope")
    end
    for i, filename in ipairs({"jingle_b.wav", "jingle_a.wav"}) do
        local source = r.GetMediaItemTake_Source(r.GetActiveTake(jingles[i]))
        assert(r.GetMediaSourceFileName(source, ""):sub(-#filename) == filename, "Wrong alternating jingle")
        local start = r.GetMediaItemInfo_Value(jingles[i], "D_POSITION")
        local finish = start + r.GetMediaItemInfo_Value(jingles[i], "D_LENGTH")
        local left, right = snapshot[i + 2], snapshot[i + 3]
        near(left.position + left.length - start, 9, "Jingle left overlap " .. i)
        near(finish - right.position, 2, "Jingle right overlap " .. i)
        near(right.position - left.position - left.length, finish - start - 11,
            "Widened jingle break " .. i)
    end
    local offsets = {}
    for i, item in ipairs(patches) do
        local take = r.GetActiveTake(item)
        offsets[i] = r.GetMediaItemTakeInfo_Value(take, "D_STARTOFFS")
        local length = r.GetMediaItemInfo_Value(item, "D_LENGTH")
        local source_length = r.GetMediaSourceLength(r.GetMediaItemTake_Source(take))
        assert(offsets[i] >= 0 and offsets[i] + length <= source_length, "Room tone reads beyond its source")
        near(length, 2, "Room-tone patch length")
        near(r.GetMediaItemInfo_Value(item, "D_FADEINLEN"), 0.5, "Room-tone fade-in")
        near(r.GetMediaItemInfo_Value(item, "D_FADEOUTLEN"), 0.5, "Room-tone fade-out")
        near(r.GetMediaItemTakeInfo_Value(take, "D_PLAYRATE"), 1, "Room-tone playback rate")
    end
    assert(offsets[1] ~= offsets[2], "Room-tone offsets repeat")
    local env = assert(r.GetTrackEnvelopeByChunkName(music, "<VOLENV2"), "Missing MUSIC Volume")
    assert(r.CountAutomationItems(env) == 1, "Expected one generated automation item")
    near(r.GetMediaTrackInfo_Value(music, "D_VOL"), 10 ^ (-20 / 20), "MUSIC track fader")
    local full, ducked = 10 ^ (-3 / 20), 10 ^ (-18 / 20)
    local intro_end = r.GetMediaItemInfo_Value(intro[1], "D_LENGTH")
    local outro_start = r.GetMediaItemInfo_Value(outro[1], "D_POSITION")
    local outro_end = outro_start + r.GetMediaItemInfo_Value(outro[1], "D_LENGTH")
    local voice_end = snapshot[#snapshot].position + snapshot[#snapshot].length
    local outro_knee = voice_end - 1.5
    local outro_under = 10 ^ (-10 / 20)
    local outro_peak = outro_end - math.min(3, (outro_end - voice_end) / 2)
    near(voice_end - outro_start, 22, "Outro overlap")
    -- Probe inside the AI; native evaluation at its exact left edge blends
    -- with the underlying envelope for the boundary sample.
    local duck_start, duck_end = snapshot[1].position - 2, snapshot[1].position + 2
    for _, probe in ipairs({{0.5, full}, {duck_start / 2, full}, {duck_start, full},
            {snapshot[1].position, (full + ducked) / 2}, {duck_end, ducked}, {intro_end, 0}, {35, 0},
            {outro_start, 0}, {(outro_start + outro_knee) / 2, outro_under / 2},
            {outro_knee, outro_under},
            {voice_end, full}, {(voice_end + outro_peak) / 2, full},
            {outro_peak, full}, {outro_end, 0}}) do
        local _, value = r.Envelope_Evaluate(env, probe[1], 48000, 1)
        near(value, probe[2], "MUSIC volume at " .. probe[1])
    end
    local ramps = {{duck_start, intro_end, -1}, {outro_start, voice_end, 1}, {outro_peak, outro_end, -1}}
    for i, item in ipairs(jingles) do
        local start = r.GetMediaItemInfo_Value(item, "D_POSITION")
        local finish = start + r.GetMediaItemInfo_Value(item, "D_LENGTH")
        local length = finish - start
        local quiet_start, rise_start = start + length * 0.025, start + length * 0.37
        local full_start = start + length * 0.56
        local full_end = start + length * 0.75
        for _, probe in ipairs({{start, 0}, {(start + quiet_start) / 2, ducked / 2}, {quiet_start, ducked},
                {(quiet_start + rise_start) / 2, ducked}, {rise_start, ducked},
                {(rise_start + full_start) / 2, (ducked + full) / 2},
                {full_start, full}, {(full_start + full_end) / 2, full}, {full_end, full},
                {(full_end + finish) / 2, full / 2}, {finish, 0}}) do
            local _, value = r.Envelope_Evaluate(env, probe[1], 48000, 1)
            near(value, probe[2], "Jingle " .. i .. " volume at " .. probe[1])
        end
        ramps[#ramps + 1] = {start, quiet_start, 1}
        ramps[#ramps + 1] = {rise_start, full_start, 1}
        ramps[#ramps + 1] = {full_end, finish, -1}
    end
    for _, ramp in ipairs(ramps) do
        local _, previous = r.Envelope_Evaluate(env, ramp[1], 48000, 1)
        for step = 1, 64 do
            local time = ramp[1] + (ramp[2] - ramp[1]) * step / 64
            local _, value = r.Envelope_Evaluate(env, time, 48000, 1)
            assert((value - previous) * ramp[3] > 0,
                "Music ramp has a level hold or reversed slope at " .. time)
            previous = value
        end
    end
    log("PASS: tracks, rate-aware trims, cumulative gap removal, widened B/A breaks with 9/2-second overlaps, quiet jingle lead-ins and asymmetric ramps and full-level holds, complete assets, two-second room patches with half-second fades, zero-start intro hold and gradual ducking, 22-second outro rise to speech end, full post-roll and final fade")

    -- Create a manual voice edit and ordinary MUSIC automation point. Keep the
    -- edit in its own Undo block; do not nest around the assembler's block.
    r.Undo_BeginBlock()
    local first = r.GetTrackMediaItem(voice, 0)
    r.SetMediaItemInfo_Value(first, "D_LENGTH", snapshot[1].length - 0.4)
    snapshot = snapshot_voice(voice)
    local manual_time, manual_amp = 200, 0.42
    local point_added = r.InsertEnvelopePoint(env, manual_time,
        r.ScaleToEnvelopeMode(r.GetEnvelopeScalingMode(env), manual_amp), 0, 0, false, false)
    r.Undo_EndBlock("Podcast Assembler Debug: manual edits", -1)
    assert(point_added, "Cannot add manual envelope point")
    local manual_points = r.CountEnvelopePointsEx(env, -1)
    assert(dofile(assembler), "Assembler rebuild failed; see its console diagnostics.")
    music, voice, room = r.GetTrack(0, 0), r.GetTrack(0, 1), r.GetTrack(0, 2)
    local rebuilt = snapshot_voice(voice)
    assert(#rebuilt == #snapshot and r.CountTracks(0) == 3, "Rebuild duplicated tracks or voice clips")
    for i, before in ipairs(snapshot) do
        for _, key in ipairs({"position", "length", "offset"}) do near(rebuilt[i][key], before[key], "Rerun VOICE " .. key) end
    end
    assert(#generated(music, "INTRO") == 1 and #generated(music, "OUTRO") == 1
        and #generated(music, "JINGLE") == 2 and #generated(room, "ROOM_TONE") == 1, "Rebuild generated duplicates or stale seams")
    env = r.GetTrackEnvelopeByChunkName(music, "<VOLENV2")
    assert(r.CountAutomationItems(env) == 1 and r.CountEnvelopePointsEx(env, -1) == manual_points,
        "Rebuild duplicated automation or deleted manual points")
    local _, value = r.Envelope_Evaluate(env, manual_time, 48000, 1)
    near(value, manual_amp, "Preserved manual automation")
    log("PASS: rerun preserves current voice edits and manual automation; no duplicates; seams recalculated")
    log("SUCCESS: inspect the editable fixture and assembler diagnostics in the REAPER console")
end

local ok, message = xpcall(run_checks, debug.traceback)
for source in pairs(pending_sources) do r.PCM_Source_Destroy(source) end
r.TrackList_AdjustWindows(false)
r.UpdateArrange()
if not ok then
    log("FAIL: " .. message)
    r.ShowMessageBox(message, "Podcast Assembler Debug", 0)
end
return ok
