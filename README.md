# Barbero Scripts

Private editorial tooling for producing researched, recording-ready English adaptations of
Alessandro Barbero lectures. Source audio is immutable; media and provider output live outside
Git, while reviewed text and research ledgers are committed here.

## Layout and setup

- Raw audio: `~/data/barbero/raw` (read-only)
- Working artifacts: `~/data/barbero/editorial/<episode>` (not committed)
- Reviewed artifacts: `episodes/<episode>`

```bash
uv sync
uv run barbero prepare episodes/007-come-scoppiano-le-guerre/episode.yaml
uv run barbero speakers episodes/007-come-scoppiano-le-guerre/episode.yaml --show
uv run barbero speakers episodes/007-come-scoppiano-le-guerre/episode.yaml --select SPEAKER_00
uv run barbero transcribe episodes/007-come-scoppiano-le-guerre/episode.yaml
uv run barbero render episodes/007-come-scoppiano-le-guerre/episode.yaml
uv run barbero validate episodes/007-come-scoppiano-le-guerre
```

`prepare` creates a temporary 16 kHz mono PCM, obtains diarization, selects the speaker with the
most total speech, exports that speaker's segments to FLAC, and writes a timeline edit map. It can
consume a provider-neutral diarization JSON with `--diarization-json`; otherwise it uses Deepgram
when `DEEPGRAM_API_KEY` is set, or `pyannote.audio` when installed and `HF_TOKEN` is set. Raw PCM
is removed after successful export.

`speakers` reports duration by speaker and records a human override. Re-run `prepare` after an
override. `transcribe` submits the complete cleaned FLAC to Deepgram Nova-3 using
`DEEPGRAM_API_KEY`; `--response-json` imports an existing response without network access.

`render` converts the provider response to stable utterances and renders corrected Italian and
recording copies. Corrections are supplied in the working directory as `corrections.yaml`, keyed
by utterance ID. To approve unchanged text, omit `text`:

```yaml
U-00042:
  reviewed: true
U-00117:
  text: "Testo italiano corretto."
  reviewed: true
```

`validate` fails on unresolved transcript review flags, broken script markers, or incomplete
quotation and claim records.

The reusable two-pass, text-only correction and contextual-verification instructions are in
[`prompts/transcript-correction.md`](prompts/transcript-correction.md). Substitute the transcript
and working correction paths for each episode. The first pass proposes conservative corrections;
the second resolves review flags by accepting or correcting text from full-episode context.

Structural outlining and research-target extraction use
[`prompts/episode-outline.md`](prompts/episode-outline.md) and
[`prompts/research-target-extraction.md`](prompts/research-target-extraction.md). These passes map
the lecture and seed pending ledgers before any external source research begins.

## Provider-neutral diarization format

```json
{"segments": [{"start": 1.2, "end": 5.7, "speaker": "SPEAKER_00"}]}
```

All generated files include input/configuration hashes. A changed source, speaker selection, or
transcription configuration invalidates downstream cache entries.
