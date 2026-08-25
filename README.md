# Barbero Scripts

Private editorial tooling for researched, recording-ready English translations of Alessandro
Barbero lectures. Source audio and provider responses live outside Git; reviewed text, decision
queues, research ledgers, and exact patch provenance are committed.

## Setup and episode creation

```bash
uv sync
export DEEPGRAM_API_KEY="$(vault kv get -field=deepgram-api-key kv/puppet)"
uv run barbero init \
  --number 21 --slug il-cavaliere --title "Il cavaliere" \
  --source ~/data/barbero/raw/21.mp3 \
  --keyterm Medioevo --keyterm cavaliere
uv run barbero prepare episodes/021-il-cavaliere/episode.yaml
uv run barbero speakers episodes/021-il-cavaliere/episode.yaml --show
uv run barbero speakers episodes/021-il-cavaliere/episode.yaml --select SPEAKER_00
uv run barbero transcribe episodes/021-il-cavaliere/episode.yaml
uv run barbero render episodes/021-il-cavaliere/episode.yaml
uv run barbero status episodes/021-il-cavaliere
```

Raw audio defaults to `~/data/barbero/raw`; working artifacts default to
`~/data/barbero/editorial/<episode>`; committed artifacts live in `episodes/<episode>`. `init`
creates a `workflow_version: 2` episode and refuses overwrite.

`prepare` diarizes, exports retained speech to FLAC, and records the cleaned-to-original timeline.
Single-speaker audio is selected automatically. Multi-speaker audio requires an explicit
`speakers --select` decision before preparation can finish. `transcribe` uses Deepgram Nova-3;
every `--keyterm` becomes a separate plain query parameter. Full provider output remains external,
while normalized utterances preserve word text, confidence, and cleaned/original timestamps.

## Three human queues

The internal stages remain specialized, but human review has three gates:

1. `transcript-uncertainties.yaml`: resolve what Barbero said. Acoustic thresholds initially flag
   words below 0.65, utterances below 0.80, and likely entities below 0.85. A contextual pass adds
   independent semantic concerns. Every new item is `pending`; resolution stores the complete
   utterance in `resolved_text`.
2. `content-corrections.yaml`: accept or reject researched quotation and accuracy treatments.
   Faithful translation remains isolated from recovered source wording. Every quotation appears
   exactly once in this queue. `barbero apply-content` checks hashes, exact single matches,
   overlaps, evidence, and protected quotation spans before creating `script.content.en.md`.
3. `listener-review.yaml`: accept or reject bounded whole-episode presentation changes after tense
   and chapter naturalness. `barbero apply-listener-review` creates `script.editorial.en.md` and
   applies an accepted public `audience_title`. It cannot reorder chapters or change boundaries.

Editing a proposal means changing its exact `proposed_text` and then setting `decision: accept`.
Rejected items do not alter output. Accepted changes receive invisible provenance comments.
`barbero status` identifies the next machine action or human queue.

## Editorial sequence

```text
audio → transcription + uncertainty detection → TRANSCRIPTION RESOLVER
      → exact Italian source → outline → quotation/claim research → research audit
      → faithful chapter translation → unified content proposals → CONTENT EDITOR
      → deterministic content application → tense → chapter naturalness
      → whole-episode listener proposals → LISTENER EDITOR
      → deterministic editorial application → narrow consistency → publication
```

The Italian source has exact ordered utterance coverage. Quotation research stays separate because
source boundaries, evidence tiers, locators, and transmission history need their own rules. Tense
and naturalness also stay separate: the former protects the historical-present invariant, while the
latter may rebuild sentences for oral English. Naturalness uses
`KEEP → CONTEXTUALIZE → GLOSS → REPLACE`, preserving historical texture instead of flattening
vocabulary. Whole-episode review owns attention hierarchy, orientation, callbacks, quotation
listenability, lecture residue, and the ending, with explicit anti-podcastification constraints.

The Italian `title` is immutable source metadata. For v2 episodes, `audience_title` owns the final
H1 and published English title; `publication` still owns summary, explicitness, and publication
time.

Reusable instructions are in `prompts/`, with the complete controller in
[`prompts/episode-workflow.md`](prompts/episode-workflow.md). All language-model editorial work uses
native Codex agents; transcription and cited research services are the explicit external-service
exceptions.

## Validation

```bash
uv run ruff format .
uv run ruff check .
uv run python -m pytest -q
uv run barbero validate episodes/021-il-cavaliere
```

V2 validation derives progress from validated artifacts and decisions rather than file presence
alone. It enforces hashes, exact patch matches, decision gates, chapter boundaries, coverage,
quotation constraints, deterministic output, and title propagation. Unmigrated completed episodes
continue through isolated legacy validation.

Provider-neutral diarization input is:

```json
{"segments": [{"start": 1.2, "end": 5.7, "speaker": "SPEAKER_00"}]}
```
