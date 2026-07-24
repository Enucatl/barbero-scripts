# Barbero Scripts

Private editorial tooling for producing researched, recording-ready English translations of
Alessandro Barbero lectures. Source audio is immutable; media and provider output live outside
Git, while reviewed text and research ledgers are committed here.

## Layout and setup

- Raw audio: `~/data/barbero/raw` (read-only)
- Working artifacts: `~/data/barbero/editorial/<episode>` (not committed)
- Reviewed artifacts: `episodes/<episode>`

```bash
uv sync
export DEEPGRAM_API_KEY="$(vault kv get -field=deepgram-api-key kv/puppet)"
# Fallback for local pyannote diarization:
export HF_TOKEN="$(vault kv get -field=huggingface-read-token kv/puppet)"
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

`render` converts the provider response to stable utterances and renders corrected Italian.
Corrections are supplied in the working directory as `corrections.yaml`, keyed
by utterance ID. To approve unchanged text, omit `text`:

```yaml
U-00042:
  reviewed: true
U-00117:
  text: "Testo italiano corretto."
  reviewed: true
```

`validate` resolves transcript, ledger, and marker references and enforces the Italian audio gate,
exact ordered utterance coverage, chapter identity, quotation replacement timing, chapter review,
and human accuracy-decision gates.

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

The authoritative spoken-content source is `script.it.md`, assembled verbatim from the stable,
timestamped `transcript.it.md`. Research cannot begin until a human has checked every utterance
against audio and approved every chapter's complete ordered coverage in `italian-review.yaml`.

The episode then progresses through research ledgers, a close language-model translation of each
complete Italian chapter into `script.translation.faithful.en.md`, and a distinct quotation replacement
pass producing `script.translation.en.md`. Only `source_replacement: eligible` records supply exact
ledger wording; all other quotations retain Barbero's contextual translation. Accuracy review and
human decisions produce `script.corrected.en.md`. Each chapter receives an independent conservative
naturalness review under `naturalness/`; their verbatim assembly is `script.spoken.en.md`. A narrow
whole-episode consistency pass produces `script.en.md` without restructuring or new transitions.
Research never directly authorizes corrections, pending decisions block downstream files, and
authoritative quotations remain exact after replacement.

The complete supervised sequence is defined in
[`prompts/episode-workflow.md`](prompts/episode-workflow.md). It assigns non-overlapping agent work,
sets human approval gates, gives the validation commands, and keeps external artifacts out of Git.
After individual research tasks finish, [`prompts/research-audit.md`](prompts/research-audit.md)
checks evidence standards, discrepancies, deferrals, and source consistency across the episode.
No pronunciation data or separate recording copy is generated; record directly from `script.en.md`
and manually skip its annotations.

The reusable microphone, Reaper, editing, processing, delivery, and minimal sound-design workflow
is in [`docs/recording-and-sound-design.md`](docs/recording-and-sound-design.md).

## Provider-neutral diarization format

```json
{"segments": [{"start": 1.2, "end": 5.7, "speaker": "SPEAKER_00"}]}
```

All generated files include input/configuration hashes. A changed source, speaker selection, or
transcription configuration invalidates downstream cache entries.
