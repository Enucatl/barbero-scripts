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

`validate` resolves transcript, ledger, and marker references; checks quotation replacement rules;
and enforces the human accuracy-decision gate and marker preservation between script stages.

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

The researched lecture moves through a three-pass faithful-translation workflow followed by three
editorial passes. The translation controller first creates `translation.utterances.en.yaml`, then
losslessly assembles `script.translation.assembled.en.md`, and finally formats and normalizes
`script.translation.en.md`. See
([`faithful-translation.md`](prompts/faithful-translation.md)), accuracy review
([`accuracy-review.md`](prompts/accuracy-review.md)), human-approved corrections
([`approved-corrections.md`](prompts/approved-corrections.md)), and idiomatic polishing
([`idiomatic-polishing.md`](prompts/idiomatic-polishing.md)). The versioned artifacts are
`script.translation.en.md`, `accuracy-notes.yaml`, `script.corrected.en.md`,
`script.spoken.en.md`, and the annotated, directly recordable `script.en.md`. The spoken draft is a
strong conversational rewrite; a separate fidelity/read-aloud audit compares it with the corrected
script before producing the final. Research never authorizes a correction: every accuracy note
defaults to `retain-original`, and corrections require a human to opt in with `apply`. Any
`pending` decision still blocks downstream scripts. The faithful translation must exist and pass
coverage checks before accuracy notes are generated or presented for human review.
Pass one uses Google Translate only to create the raw utterance-by-utterance YAML. Sequential agents
inheriting the model configured in the current Codex session then correct and assemble it and run
the final formatting/consistency pass. External translation services are forbidden after pass one;
separate Codex processes and model selection are forbidden throughout. Quotations
marked `source_replacement: eligible` must use the ledger's recovered English wording verbatim.
Every quotation ledger `translation` is English. Records marked `not-applicable` or `unavailable`
never supply script wording; those passages use a faithful contextual translation of Barbero.
Composite records may be `eligible` when every component has recoverable English wording and clear
document boundaries; the exact assembled ledger wording is then used.

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
