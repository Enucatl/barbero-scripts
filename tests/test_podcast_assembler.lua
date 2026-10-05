-- Run from the repository root: lua tests/test_podcast_assembler.lua
-- Mocked control-flow checks; native REAPER integration is a separate check.
local SCRIPT = "src/barbero_scripts/Podcast_Assembler.lua"
local MARKER = "P_EXT:PODCAST_ASSEMBLER"
local function close(actual, expected)
    assert(math.abs(actual - expected) < 1e-8,
        string.format("expected %.12g, got %.12g", expected, actual))
end
local function copy(value, seen)
    if type(value) ~= "table" then return value end
    seen = seen or {}
    if seen[value] then return seen[value] end
    local result = {}
    seen[value] = result
    for key, child in pairs(value) do result[copy(key, seen)] = copy(child, seen) end
    return result
end
local function take(rate, offset)
    return {D_PLAYRATE = rate or 1, D_STARTOFFS = offset or 0, envelopes = {}}
end
local function item(position, length, rate, offset)
    return {D_POSITION = position, D_LENGTH = length, C_LOCK = 0,
        takes = {take(rate, offset)}, strings = {}}
end
local function track(name, items)
    return {name = name, items = items or {}, strings = {}, envelopes = {}, I_FOLDERDEPTH = 0}
end
local function envelope()
    return {points = {{time = 0, value = 0.83}}, ais = {}, strings = {}}
end
local function project(tracks)
    return {tracks = tracks, master = track("MASTER"), extstate = {}}
end
local function mock(initial, options)
    options = options or {}
    local state = {project = initial, mutations = 0, refresh = 0, errors = {}, warnings = {},
        begin_count = 0, end_count = 0, undo_count = 0, scaling_calls = 0,
        opened = {}, destroyed = {}}
    local assets = {intro = 12, outro = 8, jingle_a = 5, jingle_b = 4, room_tone = 10}
    for key, value in pairs(options.lengths or {}) do assets[key] = value end
    local r = {}
    local function mutate()
        state.mutations = state.mutations + 1
    end
    local function strings(object, key, value, set)
        if set then mutate(); object.strings[key] = value end
        return true, object.strings[key] or ""
    end
    local function ai(env, index)
        return assert(env.ais[(index % 0x10000000) + 1], "unknown automation item")
    end
    r.GetAppVersion = function() return "7.46/linux-x86_64" end
    r.get_action_context = function() return false, "/repo/src/barbero_scripts/Podcast_Assembler.lua" end
    r.file_exists = function(path)
        assert(path:match("^/repo/assets/audio/[^/]+%.wav$"), "incorrect asset path")
        return not options.missing or not path:find(options.missing, 1, true)
    end
    r.PCM_Source_CreateFromFile = function(path)
        local key = path:match("([^/]+)%.wav$")
        if options.source_fail == key then return nil end
        local source = {path = path, length = assert(assets[key])}
        state.opened[#state.opened + 1] = source
        return source
    end
    r.PCM_Source_Destroy = function(source)
        assert(not source.attached, "destroyed a take-owned source")
        assert(not state.destroyed[source], "double source destruction")
        state.destroyed[source] = true
    end
    r.GetMediaSourceLength = function(source) return source.length, false end
    r.CountTracks = function() return #state.project.tracks end
    r.GetTrack = function(_, index) return state.project.tracks[index + 1] end
    r.GetMasterTrack = function() return state.project.master end
    r.GetTrackName = function(t) return true, t.name end
    r.GetTrackGUID = function(t) return t.name .. ":guid" end
    r.IsTrackSelected = function(t) return t.selected == true end
    r.SetTrackSelected = function(t, selected) mutate(); t.selected = selected end
    r.GetMediaTrackInfo_Value = function(t, key) return t[key] or 0 end
    r.SetMediaTrackInfo_Value = function(t, key, value) mutate(); t[key] = value; return true end
    r.GetSetMediaTrackInfo_String = function(t, key, value, set)
        if key == "P_NAME" then
            if set then mutate(); t.name = value end
            return true, t.name
        end
        return strings(t, key, value, set)
    end
    r.InsertTrackAtIndex = function(index) mutate(); table.insert(state.project.tracks, index + 1, track("")) end
    r.ReorderSelectedTracks = function(index)
        mutate()
        for i, t in ipairs(state.project.tracks) do
            if t.selected then
                table.remove(state.project.tracks, i)
                table.insert(state.project.tracks, index + 1, t)
                return true
            end
        end
        return false
    end
    r.GetProjExtState = function(_, namespace, key)
        return 1, state.project.extstate[namespace .. key] or ""
    end
    r.SetProjExtState = function(_, namespace, key, value)
        mutate(); state.project.extstate[namespace .. key] = value; return 1
    end
    r.CountTrackMediaItems = function(t) return #t.items end
    r.GetTrackMediaItem = function(t, index) return t.items[index + 1] end
    r.GetSetMediaItemInfo_String = strings
    r.GetMediaItemInfo_Value = function(it, key) return it[key] or 0 end
    r.SetMediaItemInfo_Value = function(it, key, value) mutate(); it[key] = value; return true end
    r.GetActiveTake = function(it) return it.takes[1] end
    r.CountTakes = function(it) return #it.takes end
    r.GetTake = function(it, index) return it.takes[index + 1] end
    r.TakeIsMIDI = function(t) return t.midi == true end
    r.GetMediaItemTakeInfo_Value = function(t, key) return t[key] or 0 end
    r.SetMediaItemTakeInfo_Value = function(t, key, value) mutate(); t[key] = value; return true end
    r.GetTakeNumStretchMarkers = function(t) return t.stretch_markers or 0 end
    r.CountTakeEnvelopes = function(t) return #t.envelopes end
    r.GetTakeEnvelope = function(t, index) return t.envelopes[index + 1] end
    r.GetSetMediaItemTakeInfo_String = function(t, key, value, set)
        t.strings = t.strings or {}; return strings(t, key, value, set)
    end
    r.AddMediaItemToTrack = function(t)
        if options.insertion_error then error("injected media insertion error") end
        mutate(); local it = item(0, 1); it.takes = {}; t.items[#t.items + 1] = it; return it
    end
    r.AddTakeToMediaItem = function(it) mutate(); local t = take(); it.takes[#it.takes + 1] = t; return t end
    r.SetMediaItemTake_Source = function(t, source)
        mutate(); assert(not state.destroyed[source]); source.attached = true; t.source = source; return true
    end
    r.DeleteTrackMediaItem = function(t, it)
        mutate()
        for index, candidate in ipairs(t.items) do
            if candidate == it then table.remove(t.items, index); return true end
        end
        return false
    end
    r.GetItemStateChunk = function() return true, "<ITEM\n<TAKE\n>\n>\n" end
    r.SetItemStateChunk = function(it, chunk) mutate(); it.chunk = chunk; return true end
    r.GetTrackStateChunk = function() return true, "<TRACK\nNAME MUSIC\n>\n" end
    r.SetTrackStateChunk = function(t, chunk)
        mutate(); assert(chunk:find("<VOLENV2", 1, true)); t.envelopes[#t.envelopes + 1] = envelope(); return true
    end
    r.GetTrackEnvelopeByChunkName = function(t) return t.envelopes[1] end
    r.CountTrackEnvelopes = function(t) return #t.envelopes end
    r.GetTrackEnvelope = function(t, index) return t.envelopes[index + 1] end
    r.GetSetEnvelopeInfo_String = strings
    r.SetTrackAutomationMode = function(t, mode) mutate(); t.automation_mode = mode end
    r.CountAutomationItems = function(env) return #env.ais end
    r.GetSetAutomationItemInfo = function(env, index, key, value, set)
        local automation = ai(env, index)
        if set then mutate(); automation[key] = value end
        return automation[key] or 0
    end
    r.GetSetAutomationItemInfo_String = function(env, index, key, value, set)
        return strings(ai(env, index), key, value, set)
    end
    r.InsertAutomationItem = function(env, pool, position, length)
        mutate()
        env.ais[#env.ais + 1] = {D_POOL_ID = pool, D_POSITION = position, D_LENGTH = length,
            strings = {}, points = {}}
        return #env.ais - 1
    end
    r.CountEnvelopePointsEx = function(env, index) return #ai(env, index).points end
    r.DeleteEnvelopePointEx = function(env, index, point)
        mutate(); table.remove(ai(env, index).points, point + 1); return true
    end
    r.InsertEnvelopePointEx = function(env, index, time, value)
        local automation = ai(env, index)
        assert(time >= automation.D_POSITION and time < automation.D_POSITION + automation.D_LENGTH,
            "automation endpoint is outside item (native REAPER drops right-boundary points)")
        mutate(); automation.points[#automation.points + 1] = {time = time, value = value}; return true
    end
    r.Envelope_SortPointsEx = function(env, index)
        mutate(); table.sort(ai(env, index).points, function(a, b) return a.time < b.time end)
    end
    r.GetEnvelopeScalingMode = function() return 1 end
    r.ScaleToEnvelopeMode = function(mode, value)
        assert(mode == 1); state.scaling_calls = state.scaling_calls + 1; return value * 2
    end
    r.Undo_BeginBlock = function()
        state.begin_count = state.begin_count + 1; state.snapshot = copy(state.project)
    end
    r.Undo_EndBlock = function() state.end_count = state.end_count + 1 end
    r.Undo_DoUndo2 = function()
        state.undo_count = state.undo_count + 1
        -- Native REAPER Undo restores tracks/items, but project extstate survives.
        local extstate = state.project.extstate
        state.project = copy(state.snapshot)
        state.project.extstate = extstate
    end
    state.undo = r.Undo_DoUndo2
    r.PreventUIRefresh = function(delta) state.refresh = state.refresh + delta end
    r.ShowMessageBox = function(message) state.errors[#state.errors + 1] = message end
    r.ShowConsoleMsg = function(message) state.warnings[#state.warnings + 1] = message end
    r.TrackList_AdjustWindows = function() end
    r.UpdateArrange = function() state.updated = true end
    state.run = function()
        local script_file = assert(io.open(SCRIPT, "r"))
        local script_text = script_file:read("*a")
        script_file:close()
        if options.quiet then script_text = script_text:gsub("DIAGNOSTICS = true", "DIAGNOSTICS = false", 1) end
        state.result = assert(load(script_text, "@" .. SCRIPT, "t", {reaper = r, math = math, pairs = pairs, ipairs = ipairs,
            type = type, tonumber = tonumber, tostring = tostring, table = table, string = string, assert = assert,
            error = error, xpcall = xpcall, debug = debug}))()
        assert(state.refresh == 0, "unbalanced UI refresh")
        return state
    end
    return state
end
local function find_track(state, name)
    for _, t in ipairs(state.project.tracks) do if t.name == name then return t end end
    error("missing track " .. name)
end
local function generated(state, kind)
    local result = {}
    for _, t in ipairs(state.project.tracks) do
        for _, it in ipairs(t.items) do
            if it.strings[MARKER] == "PODCAST_ASSEMBLER:" .. kind then result[#result + 1] = it end
        end
    end
    table.sort(result, function(a, b) return a.D_POSITION < b.D_POSITION end)
    return result
end
local function success(state)
    assert(#state.errors == 0, table.concat(state.errors, "\n"))
    assert(state.result == true, "successful assembly did not report success to harness")
    assert(state.begin_count == state.end_count and state.undo_count == 0)
end

-- Ripple collapse, source-rate trim, exact-threshold recorded break,
-- alternating jingles overlapping speech, and full WAV boundaries.
local a, b, c, d, e = item(0, 10, 2, 1), item(10.5, 5), item(17.5, 10), item(31.5, 10), item(51.5, 10)
local state = mock(project({track("", {e, c, a, d, b})})):run()
success(state)
assert(#state.project.tracks == 3)
for index, name in ipairs({"MUSIC", "VOICE", "ROOM TONE"}) do assert(state.project.tracks[index].name == name) end
close(a.takes[1].D_STARTOFFS, 1.2); close(a.D_LENGTH, 9.8); close(a.D_POSITION, 6)
close(a.D_FADEINLEN, 0.008); close(b.D_POSITION, 15.8)
close(c.D_POSITION - b.D_POSITION - b.D_LENGTH, 2.2)
local jingles = generated(state, "JINGLE")
assert(#jingles == 3)
assert(jingles[1].takes[1].source.path:match("jingle_b%.wav$"))
assert(jingles[2].takes[1].source.path:match("jingle_a%.wav$"))
assert(jingles[3].takes[1].source.path:match("jingle_b%.wav$"))
local intro, outro = generated(state, "INTRO")[1], generated(state, "OUTRO")[1]
close(intro.D_LENGTH, 12); close(intro.D_POSITION, 0); assert(not intro.chunk)
close(outro.D_LENGTH, 8); close(outro.D_POSITION, e.D_POSITION + e.D_LENGTH - 5)
local patches = generated(state, "ROOM_TONE")
assert(#patches == 1); close(patches[1].D_POSITION, b.D_POSITION - 1)
close(patches[1].D_LENGTH, 2); close(patches[1].D_FADEINLEN, 0.5)
close(patches[1].D_FADEOUTLEN, 0.5)
local music = find_track(state, "MUSIC")
close(music.D_VOL, 10 ^ (-10 / 20))
local env = music.envelopes[1]
assert(#env.ais == 1 and #env.points == 1 and env.points[1].value == 0.83)
close(env.ais[1].D_POSITION + env.ais[1].D_LENGTH, outro.D_POSITION + outro.D_LENGTH + 0.05)
close(env.ais[1].points[1].value, 2 * 10 ^ (-3 / 20))
assert(state.scaling_calls == #env.ais[1].points)
local trace = table.concat(state.warnings)
for _, message in ipairs({"STAGE: validate assets", "CONFIG START_TRIM=", "source-offset=1.000000 -> 1.200000",
    "decision=collapse to previous end", "JINGLE accepted:", "Envelope point 1:", "SUCCESS:"}) do
    assert(trace:find(message, 1, true), "missing diagnostic: " .. message)
end

-- Manual current edits and user content survive a rebuild; voice does not
-- receive another trim/collapse/pre-roll shift. Only marked content is rebuilt.
local user_item = item(100, 2)
music.items[#music.items + 1] = user_item
env.points[#env.points + 1] = {time = 100, value = 0.42}
b.D_POSITION = b.D_POSITION + 0.4
local current_position, current_offset, current_length = b.D_POSITION, b.takes[1].D_STARTOFFS, b.D_LENGTH
state:run(); success(state)
close(b.D_POSITION, current_position); close(b.takes[1].D_STARTOFFS, current_offset); close(b.D_LENGTH, current_length)
assert(#state.project.tracks == 3 and #generated(state, "INTRO") == 1 and #generated(state, "OUTRO") == 1)
assert(#generated(state, "ROOM_TONE") == 0 and #env.ais == 1 and #env.points == 2)
local found = false
for _, it in ipairs(music.items) do found = found or it == user_item end
assert(found, "manual music item was deleted")

-- Undo must restore the authoritative track marker even though extstate
-- survives, so running again performs the first preparation exactly once.
local undone = mock(project({track("", {item(0, 10, 2, 1)})})):run()
success(undone)
assert(find_track(undone, "VOICE").strings["P_EXT:PODCAST_ASSEMBLER_VOICE_PREPARED"] == "1.0")
undone:undo()
assert(undone.project.extstate.PODCAST_ASSEMBLERvoice_prepared == "1.0")
assert(not undone.project.tracks[1].strings["P_EXT:PODCAST_ASSEMBLER_VOICE_PREPARED"])
undone:run()
assert(#undone.errors == 0, table.concat(undone.errors))
close(find_track(undone, "VOICE").items[1].takes[1].D_STARTOFFS, 1.2)

-- Multiple seam patches use bounded, different offsets and never stretch.
local seam_state = mock(project({track("VOICE", {item(0, 10), item(10.5, 5), item(16, 4)})})):run()
success(seam_state)
local seam_patches = generated(seam_state, "ROOM_TONE")
assert(#seam_patches == 2 and seam_patches[1].takes[1].D_STARTOFFS ~= seam_patches[2].takes[1].D_STARTOFFS)
for _, patch in ipairs(seam_patches) do
    local t = patch.takes[1]
    assert(t.D_STARTOFFS >= 0 and t.D_STARTOFFS + patch.D_LENGTH <= t.source.length)
    close(t.D_PLAYRATE, 1)
end

-- A chain of mini breaks must never manufacture a long break. Classify the
-- original 1.9s gap before trims, then widen real breaks for the longer jingles.
local clips = {item(15.5, 30), item(46, 30), item(76.5, 30), item(108.4, 30), item(142.4, 30), item(177.4, 30)}
local overlap_state = mock(project({track("VOICE", clips)}),
    {lengths = {intro = 33.481417, outro = 29.158583, jingle_a = 20.553104, jingle_b = 17.233771}}):run()
success(overlap_state)
for i = 2, 4 do close(clips[i].D_POSITION, clips[i - 1].D_POSITION + clips[i - 1].D_LENGTH) end
close(clips[5].D_POSITION - clips[4].D_POSITION - clips[4].D_LENGTH, 17.233771 - 7)
close(clips[6].D_POSITION - clips[5].D_POSITION - clips[5].D_LENGTH, 20.553104 - 7)
local long_jingles = generated(overlap_state, "JINGLE")
assert(#long_jingles == 2 and #generated(overlap_state, "ROOM_TONE") == 3)
local overlap_env = find_track(overlap_state, "MUSIC").envelopes[1]
for i, cue in ipairs(long_jingles) do
    local left, right = clips[i + 3], clips[i + 4]
    local gap_start, gap_end = left.D_POSITION + left.D_LENGTH, right.D_POSITION
    close(cue.D_LENGTH, i == 1 and 17.233771 or 20.553104)
    close(cue.D_POSITION + cue.D_LENGTH / 2, (gap_start + gap_end) / 2)
    assert(cue.D_POSITION < gap_start and cue.D_POSITION + cue.D_LENGTH > gap_end)
    close(gap_start - cue.D_POSITION, 3.5)
    close(cue.D_POSITION + cue.D_LENGTH - gap_end, 3.5)
    local points = {}
    for _, p in ipairs(overlap_env.ais[1].points) do
        if p.time >= cue.D_POSITION and p.time <= cue.D_POSITION + cue.D_LENGTH then
            points[#points + 1] = p
        end
    end
    assert(#points == 4, "jingle must ramp across speech without ducked plateaus")
    close(points[1].time, cue.D_POSITION); close(points[1].value, 0)
    close(points[2].time, gap_start + 0.5); close(points[2].value, 2 * 10 ^ (-3 / 20))
    close(points[3].time, gap_end - 0.5); close(points[3].value, points[2].value)
    close(points[4].time, cue.D_POSITION + cue.D_LENGTH); close(points[4].value, 0)
end
local long_intro = generated(overlap_state, "INTRO")[1]
close(long_intro.D_POSITION, 0); close(long_intro.D_LENGTH, 33.481417)
assert(long_intro.D_LENGTH - clips[1].D_POSITION > 17 and not long_intro.chunk)
local long_outro = generated(overlap_state, "OUTRO")[1]
close(long_outro.D_POSITION, clips[6].D_POSITION + clips[6].D_LENGTH - 22)

-- Intro holds full until shortly before speech, then decreases throughout;
-- outro reaches full at speech end and holds it until its final fade.
for _, cue in ipairs({long_intro, long_outro}) do
    local points = {}
    for _, p in ipairs(overlap_env.ais[1].points) do
        if p.time >= cue.D_POSITION and p.time <= cue.D_POSITION + cue.D_LENGTH then
            points[#points + 1] = p
        end
    end
    assert(#points == (cue == long_intro and 4 or 5))
    if cue == long_intro then
        close(points[2].time, clips[1].D_POSITION - 2)
        close(points[2].value, points[1].value)
    else
        close(points[2].time, clips[6].D_POSITION + clips[6].D_LENGTH - 1.5)
        close(points[2].value, 2 * 10 ^ (-10 / 20))
    end
    for i = 2, #points do
        if (cue == long_intro and i == 2) or (cue == long_outro and i == 4) then
            close(points[i].value, points[i - 1].value)
        elseif cue == long_intro or i == #points then assert(points[i].value < points[i - 1].value)
        else assert(points[i].value > points[i - 1].value) end
    end
    close(points[#points].value, 0)
    local speech_boundary = cue == long_intro and clips[1].D_POSITION + 2
        or clips[6].D_POSITION + clips[6].D_LENGTH
    local duck_point = points[3]
    close(duck_point.time, speech_boundary)
    close(duck_point.value, 2 * 10 ^ ((cue == long_intro and -18 or -3) / 20))
end

-- Rebuilding expanded breaks must not add silence again or change source edits.
local spaced_positions = {}
for i, clip in ipairs(clips) do spaced_positions[i] = clip.D_POSITION end
overlap_state:run(); success(overlap_state)
for i, clip in ipairs(clips) do close(clip.D_POSITION, spaced_positions[i]) end

-- Removing a mini gap also moves later clips at long boundaries; reject a
-- locked later item before mutating anything, even if it is not at a seam.
local locked = item(25, 10); locked.C_LOCK = 1
local locked_state = mock(project({track("VOICE", {item(6, 10), item(16.5, 4), locked})})):run()
assert(locked_state.result == false and locked_state.mutations == 0)
assert(table.concat(locked_state.errors):find("locked and would need moving", 1, true))

-- A clip too short for trims survives intact; near-minimum trimmed clips
-- receive reduced fades, and a short ambience source safely reduces patches.
local short, tiny = item(0, 0.15), item(0.4, 0.21)
local short_state = mock(project({track("", {short, tiny})}), {lengths = {room_tone = 0.01}}):run()
success(short_state)
close(short.D_LENGTH, 0.15); close(short.takes[1].D_STARTOFFS, 0)
close(tiny.D_LENGTH, 0.01); close(tiny.D_FADEINLEN, 0.005)
local short_patch = generated(short_state, "ROOM_TONE")[1]
close(short_patch.D_LENGTH, 0.01); close(short_patch.takes[1].D_STARTOFFS, 0)
assert(table.concat(short_state.warnings):find("trimming skipped", 1, true))
assert(table.concat(short_state.warnings):find("edge fades reduced", 1, true))

-- Predictable validation failures never open an undo block or mutate tracks.
for _, case in ipairs({
    {options = {missing = "intro.wav"}, pattern = "/repo/assets/audio/intro.wav"},
    {options = {source_fail = "jingle_b"}, pattern = "Unable to load jingle_b"},
    {tracks = {track("one", {item(0, 10)}), track("two", {item(20, 10)})}, pattern = "Cannot identify VOICE"},
    {tracks = {track("VOICE", {})}, pattern = "no usable audio items"},
}) do
    local failed = mock(project(case.tracks or {track("", {item(0, 10)})}), case.options):run()
    assert(#failed.errors == 1 and failed.errors[1]:find(case.pattern, 1, true), table.concat(failed.errors))
    assert(failed.mutations == 0 and failed.begin_count == 0 and failed.undo_count == 0)
    assert(failed.result == false and table.concat(failed.warnings):find("ERROR during", 1, true))
    for _, source in ipairs(failed.opened) do assert(failed.destroyed[source]) end
end

-- A runtime failure rolls back voice trim, newly created tracks and markers.
local rollback = mock(project({track("", {item(0, 10, 2, 1)})}), {insertion_error = true}):run()
assert(#rollback.errors == 1 and rollback.errors[1]:find("changes were undone", 1, true))
assert(rollback.begin_count == 1 and rollback.end_count == 1 and rollback.undo_count == 1)
assert(#rollback.project.tracks == 1 and rollback.project.tracks[1].name == "")
close(rollback.project.tracks[1].items[1].D_LENGTH, 10)
close(rollback.project.tracks[1].items[1].takes[1].D_STARTOFFS, 1)
assert(not rollback.project.tracks[1].strings["P_EXT:PODCAST_ASSEMBLER_VOICE_PREPARED"])
for _, source in ipairs(rollback.opened) do assert(rollback.destroyed[source]) end

-- Disabling detailed diagnostics keeps warnings/fatal context visible and
-- still accepts the boolean CONFIG flag without changing assembly behavior.
local quiet = mock(project({track("", {item(0, 0.15), item(0.4, 1)})}), {quiet = true}):run()
success(quiet)
assert(#quiet.warnings > 0)
for _, message in ipairs(quiet.warnings) do assert(message:find("WARNING:", 1, true)) end
local quiet_error = mock(project({track("", {item(0, 10)})}), {quiet = true, missing = "intro.wav"}):run()
assert(quiet_error.result == false and quiet_error.mutations == 0)
assert(#quiet_error.warnings == 1 and quiet_error.warnings[1]:find("ERROR during validate assets", 1, true))
print("Podcast Assembler mocked checks passed")
