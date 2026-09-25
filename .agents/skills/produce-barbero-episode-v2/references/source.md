# Source preparation and episode brief

`EPISODE` is an episode directory, `CONFIG` is its `episode.yaml`, and `TRIAL` is its
`editorial-v2/` subdirectory. Run repository commands from the repository root.

## Existing episode

Read the episode metadata, transcript, Italian script, chapter map, and existing source decisions.
Reuse them without rendering or assembling over completed files. Preserve accepted and rejected
editorial decisions that the user says apply to the trial; record their provenance in the brief.
An English draft or a completed flag is not evidence that the Italian was checked against audio.
Keep existing `Q` and `C` identifiers for the same source passages and allocate new IDs after the
existing sequence. Do not preserve a source marker while assigning its ID to a different target.

For an existing adaptation, inspect `content-corrections.yaml`, `listener-review.yaml` including
its history, legacy `accuracy-notes.yaml` where present, `review.md` implementation updates, and
the approved audience title in metadata. Later explicit user decisions override earlier proposals
or recommendations, including earlier sections of the same review. Record applicable decisions,
IDs, exact wording or scope, paths, and hashes in the brief. Resolve genuine conflicts from the
conversation or ask a focused question; do not silently resurrect a rejected edit. Pass this
decision record to the writer even when keeping the prior full English script out of its context.

If source problems appear, record the affected utterance, timestamp, ambiguity, and proposed
resolution for the user. Do not silently change the source to agree with historical research.
For a comparison against an existing adaptation, keep that English out of the writer's initial
context unless the user asks to use it; it can be used later to compare outcomes.

## New episode

Use the existing CLI only for source preparation:

| Need | Command, prefixed by `uv run barbero` |
|---|---|
| Scaffold the supplied episode identity and audio | `init --number N --slug SLUG --title TITLE --source AUDIO` |
| Diarize/prepare, or resume after speaker selection | `prepare CONFIG` |
| Inspect speaker choices | `speakers CONFIG --show` |
| Apply the user's speaker selection | `speakers CONFIG --select SPEAKER_ID` |
| Transcribe the retained audio | `transcribe CONFIG` |
| Render transcript and acoustic uncertainty queue | `render CONFIG` |
| Assemble the settled transcript using the chapter map | `assemble-italian EPISODE` |

Follow the repository's wake-run instructions for long commands. Preserve the generated
`workflow_version: 2`; that field belongs to the existing CLI. Do not initialize an existing
episode. `render` writes the transcript and external provider-derived artifacts, so use it only
when preparing or deliberately updating the source.

After speaker selection, reuse existing diarization with
`uv run barbero prepare CONFIG --diarization-json WORK/diarization.json`, where `WORK` is the
resolved `work_dir` from the metadata. Plain `prepare` may repeat diarization. Check saved provider
artifacts before rerunning preparation; do not repeat paid work merely to learn its status.

Read `transcript.it.md` in full. In `transcript-uncertainties.yaml`, preserve acoustic items and
prior resolutions; add semantic uncertainties for recognition errors, names, dates, foreign
expressions, quotations, and incoherence. Each new item has a stable ID, an existing utterance ID,
reasons, complete-utterance `proposed_text`, and `resolution.status: pending`. Inspect
`initialize_transcript_uncertainties` and `validate_transcript_uncertainties` in
`src/barbero_scripts/workflow.py` for the exact existing schema. Do not claim acoustic evidence
without inspecting it. Set `detection_status: complete` only after the full contextual scan.

The user resolves a meaningful uncertainty by supplying or accepting complete `resolved_text`;
store that with `resolution.status: resolved` and preserve the decision note. Rerender after
resolution. Any remaining `[REVIEW:...]` flag requires investigation; do not merely delete it.
Read the existing `corrections.yaml` contract if a provider-level correction is required.

After source resolution, define the chapter map and brief together. `chapters.yaml` is a list with
`id: CH-NNN`, `title`, `start: U-NNNNN`, and `end: U-NNNNN`. Ranges must cover every transcript
utterance once in order. Assemble the Italian script with the command above; never rewrite its
spoken text. Keep fillers, repetitions, dialogue, jokes, and digressions in this authoritative source.

Do not use `init-italian-review` as a verification shortcut: it automatically marks every utterance
as `reviewed_audio: true`. This trial does not require that legacy checklist. Document only the
source review actually performed.

## Source checks

Use deterministic checks to compare ordered transcript IDs with expanded chapter ranges, confirm
unique sequential chapter IDs and valid endpoints, and compare the Italian script with the
transcript after removing structural headings/comments and normalizing whitespace. Spoken words
and punctuation must remain unchanged. A preserved coverage comment alone proves no textual
fidelity. Check the uncertainty queue against the actual transcription fingerprint where the
provider artifacts are available.

For a newly prepared source, `uv run barbero validate EPISODE` can supplement these checks. It is
the old workflow's validator and does not fully verify source wording or the trial. On an existing
episode, distinguish unrelated old downstream findings from source defects; report source defects
and resolve them before relying on the source. Never describe a legacy pass as trial validation.

## `TRIAL/brief.md`

Keep a compact, durable episode brief containing:

- Source file paths and SHA-256 hashes of `episode.yaml`, `transcript.it.md`, `script.it.md`,
  `chapters.yaml`, and available transcript decisions; what was checked against text or audio.
- Audience and house style, supplied examples, explicit user preferences and inherited decisions.
- Opening thesis and narrative arc; each chapter's inclusive utterance range, original timestamps,
  argument, essential examples, dialogue, digressions, and intended listener experience.
- Names and terms requiring consistent English, useful first-use explanations, and scene chronology.
- Stable `Q-NNN` quotation/attribution targets and `C-NNN` claim targets in first-appearance order.
- Source ambiguities, missing evidence, and open editorial choices.

Cover the whole lecture. Do not equate an aside with expendable content. Do not set a compression
quota. Source title and episode identity remain authoritative; an English title is a proposal.
Read the complete source rather than only this brief when writing or reviewing the adaptation.
