# Recording and sound design guide

Use this guide for recording Barbero adaptations with a RØDE XDM-100 and Reaper. The priorities,
in order, are a quiet room, consistent microphone technique, an engaged natural performance,
clean editing, and restrained processing. Plugins cannot repair poor placement or a reflective
room.

## Recording setup

The XDM-100 is an end-address dynamic microphone: speak into its top, not its side.

- Place it 8–12 cm (3–5 inches) from the mouth.
- Aim it 20–30 degrees off-axis toward the corner of the mouth.
- Keep it level with or slightly above the mouth.
- Use the supplied pop shield and shock mount.
- Keep the mouth-to-microphone distance constant while performing.
- Monitor through the microphone's headphone output.

Record in the quietest, least reflective room available. Use curtains, bookcases, duvets, or
acoustic panels at nearby reflection points. Turn off fans, air conditioning, noisy computers,
and other intermittent sources. Record 20–30 seconds of room tone at the start of every session.

Use Reaper for processing rather than printing UNIFY effects into the recording. Disable UNIFY's
compressor, gate, Big Bottom, and Aural Exciter while tracking. UNIFY may still be used for gain,
firmware, routing, and direct monitoring.

## Reaper project settings

- Sample rate: 48 kHz.
- Recording format: WAV.
- Bit depth: 24-bit PCM.
- Channel format: mono.
- Automatic backups: every 2–3 minutes.
- Disable recording-time normalization.

Set gain while performing the loudest passage at full intensity:

- Normal speech should sit around -24 to -18 dBFS.
- Strong passages should peak around -15 to -10 dBFS.
- Absolute peaks should remain below -6 dBFS.
- Never approach 0 dBFS.

Recommended tracks are narration, pickups, archival clips, music, sound effects, room tone, and a
master reference.

## Session method

Record one script heading or approximately 5–10 minutes at a time. Before each section, announce
its number or title, pause for two seconds, and begin. After a mistake, stop, leave a short pause or
make a visible marker spike, and restart from the beginning of the sentence.

Do not stop for every harmless imperfection. Record pickups immediately after each section so the
voice, distance, room, and energy still match. Take a short break every 20–30 minutes.

Mark the performance script consistently:

- `/` for a short pause.
- `//` for a full pause.
- Underline the operative word in a thought.
- Use arrows for rising or falling energy.

Aim for thoughtful conversation rather than an announcer voice. Let quotations become characters
through a modest change of energy, not an impersonation. Accelerate slightly through escalating
dates and telegrams, pause before reversals and jokes, and slow down for unfamiliar names and
causal explanations. A useful average is 145–160 words per minute, with local variation.

## Editing

Edit for credibility rather than mechanical perfection. Preserve natural breaths, changes in
tempo, and pauses that support thought. Remove mistakes, restarts, distracting breaths, loud mouth
clicks, furniture noise, accidental duplicate sentences, and dead air that breaks momentum.

Do not remove every breath. Use 5–20 ms crossfades at edits and cut against matching room tone,
not digital silence. Prefer item gain or volume automation over aggressive compression: raise
unusually quiet phrases by 1–3 dB and lower isolated loud phrases by 1–4 dB.

## Processing chain

Treat these values as starting points, not requirements. Adjust by ear against an unprocessed
reference and bypass the chain frequently.

### High-pass filter

Use ReaEQ at approximately 65–80 Hz with a 12 dB/octave slope. Raise it only until rumble
disappears; back it down if the voice loses weight.

### Corrective equalization

Start flat and make small, broad adjustments:

- Reduce 180–350 Hz by 1–3 dB if the voice is muddy or boxy.
- Reduce 700 Hz–1.2 kHz gently if it sounds nasal.
- Add 1–2 dB around 2.5–4.5 kHz only if intelligibility needs help.
- Reduce 3–6 kHz instead if the voice is harsh.
- Add a very gentle 9–12 kHz shelf only when useful.

Do not automatically boost both bass and treble.

### De-essing

Use ReaXcomp or a dedicated de-esser around 5–8 kHz. It should normally reduce only 1–4 dB and
activate only on strong sibilants.

### Compression

Starting settings for ReaComp:

- Ratio: 2.5:1 to 3:1.
- Attack: 10–20 ms.
- Release: 80–150 ms.
- RMS size: 5–10 ms.
- Soft knee enabled.
- Average gain reduction: 2–4 dB.
- Maximum reduction on the loudest moments: approximately 6 dB.

The result should sound steadier, not flattened.

### Noise control

Avoid a hard gate on long narration. Prefer close placement, room treatment, manual cleanup, or a
gentle downward expander that reduces ambience by 6–12 dB without erasing it. Apply spectral noise
reduction only when necessary and at the lowest effective setting. Steady low room noise is less
distracting than metallic denoising artifacts.

### Limiting and loudness

Place a true-peak limiter last, with a -1 dBTP ceiling, and use it only for occasional peaks.

For podcast delivery:

- Stereo programme: approximately -16 LUFS integrated.
- Mono programme: approximately -19 LUFS integrated.
- Maximum true peak: -1 dBTP.
- A spoken-word loudness range around 5–10 LU is a reasonable result.

Keep a 48 kHz, 24-bit WAV archival master. A mono delivery MP3 may use 96–128 kbps; use stereo when
music or archival material genuinely needs a stereo field.

Before recording a full episode, process and export a representative 60-second passage. Check it
on studio headphones, ordinary earbuds, a phone speaker, and a car system.

## Minimal sound design

The lecture supplies the drama. Sound should mark structure and then leave.

### Musical theme

Use one restrained instrumental theme with low strings or piano and, optionally, a faint
mechanical pulse. Avoid military marches, national motifs, trailer impacts, or constant ominous
drones.

- Opening: 8–12 seconds, with two seconds of music alone before narration.
- Midpoint: one 3–5 second return at a major structural turn.
- Ending: enter quietly beneath the final lines and continue for 15–25 seconds under credits.

### Document transition

Create one recurring 1–2 second cue from a muted telegraph or typewriter strike, a light paper
movement, and optionally one low musical note. Treat it as the sound of the diplomatic countdown,
not a literal reenactment.

For the Second World War episode, useful placements are:

- Ciano's 11 August meeting with Ribbentrop.
- The arrival of the missions in Moscow on 12 August.
- Hitler's message to Stalin on 20 August.
- The events of 31 August.
- Immediately before the invasion at dawn.

Five appearances across the episode are enough.

### Archival audio

Use no more than one or two short archival clips unless the episode specifically depends on them.
Introduce the speaker, play roughly 8–15 seconds, and resume narration without adding explanatory
music. Authentic voices are more effective when rare.

### Mixing music and effects

- Begin music approximately 26–32 dB below narration and adjust by ear.
- Fade over 1–3 seconds rather than switching abruptly.
- High-pass music around 80–120 Hz if it masks vocal weight.
- Consider a gentle 2–4 dB music reduction around 2–4 kHz.
- Duck music another 2–3 dB beneath quotations, dates, and unfamiliar names.
- Keep transitions audible but unobtrusive, typically peaking around -18 to -14 dBFS.

Silence is part of the design. Before the Nazi–Soviet pact or the invasion, a deliberate pause is
usually more effective than a dramatic hit.

## Final quality check

Listen to the complete programme without looking at the timeline. Confirm that edits disappear,
music never competes with consonants, archival clips are intelligible, pauses feel intentional,
and processing remains stable between recording sessions. Measure integrated loudness and true
peak only after the complete mix is assembled.
