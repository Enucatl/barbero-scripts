---
name: post-processing
description: Assemble and adjust Barbero English podcast episodes in REAPER using the repository's Lua post-processing script.
---

The user identifies the episode storage as `/export/scratch/barbero-english`.
The verified location in this environment is `/export/scratch/archive/barbero-english`.
Episode 020 is in `020-il-mercante/`, with processed `020-il-mercante.RPP`
and source `020-il-mercante-backup.RPP`.
Check both locations if storage moves.

The repository is `/export/docker/barbero-scripts`. The assembler is
`src/barbero_scripts/Podcast_Assembler.lua`; prepared music lives in `assets/audio`.
Read the post-processing section of `README.md` for current settings and usage.
Run `lua tests/test_podcast_assembler.lua` for the standalone regression checks.
`Podcast_Assembler_Debug.lua` is a synthetic integration harness for an empty
REAPER project, not an existing episode.

When creating the processed copy, rename the original project to
`<episode>-backup.RPP` and keep `<episode>.RPP` for the post-processed project.
Preserve an existing backup on subsequent rebuilds. Check jingle placement and editable MUSIC track-volume automation,
including the quiet lead-in, asymmetric rise/fall, and speech overlap. Rebuilds
preserve voice source edits but resize jingle breaks and shift subsequent clips
to achieve the configured speech overlaps.
