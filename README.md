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
uv run barbero init \
  --number 21 \
  --slug come-pensava-un-uomo-del-medioevo-il-cavaliere \
  --title "Come pensava un uomo del Medioevo: il cavaliere" \
  --source ~/data/barbero/raw/21_Come_pensava_un_uomo_del_Medioevo_Il_cavaliere_2011_3.mp3 \
  --keyterm Medioevo \
  --keyterm cavaliere
uv run barbero prepare episodes/007-come-scoppiano-le-guerre/episode.yaml
uv run barbero speakers episodes/007-come-scoppiano-le-guerre/episode.yaml --show
uv run barbero speakers episodes/007-come-scoppiano-le-guerre/episode.yaml --select SPEAKER_00
uv run barbero transcribe episodes/007-come-scoppiano-le-guerre/episode.yaml
uv run barbero render episodes/007-come-scoppiano-le-guerre/episode.yaml
uv run barbero validate episodes/007-come-scoppiano-le-guerre
```

`init` creates a minimal, versioned episode directory and refuses to overwrite an existing one. It
does not copy audio or create generated transcript/provider artifacts.

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
Research batches use [`prompts/historical-research.md`](prompts/historical-research.md), which
requires original-language quotation checks, exact locators, conflicting evidence, and explicit
deferral rather than unsupported resolution.

Quotation provenance is researched one target at a time with
[`prompts/quotation-research.md`](prompts/quotation-research.md). The focused pass must use web
search, follow citations into digitized books and OCR, distinguish contemporary records from later
recollections, and accept practical evidence tiers rather than requiring an inaccessible critical
edition. Quotations are never assigned to broad research batches.

The researched lecture is adapted with [`prompts/english-adaptation.md`](prompts/english-adaptation.md).
It follows Barbero closely and has no fixed word-count or duration target; source fidelity and
natural spoken English take precedence over compression.

The complete supervised sequence is defined in
[`prompts/episode-workflow.md`](prompts/episode-workflow.md). It assigns non-overlapping agent work,
sets human approval gates, gives the validation commands, and keeps external artifacts out of Git.
After individual research tasks finish, [`prompts/research-audit.md`](prompts/research-audit.md)
checks evidence standards, treatments, deferrals, and source consistency across the episode. The
final continuity, conversational-English, pronunciation, and timed-read handoff use
[`prompts/performance-readiness.md`](prompts/performance-readiness.md).

## Provider-neutral diarization format

```json
{"segments": [{"start": 1.2, "end": 5.7, "speaker": "SPEAKER_00"}]}
```

All generated files include input/configuration hashes. A changed source, speaker selection, or
transcription configuration invalidates downstream cache entries.
