# History, Told Otherwise

[History, Told Otherwise](https://podcast.enucatl.com) is an independent podcast of English
adaptations of selected Alessandro Barbero history lectures. Each episode keeps Barbero’s
narrative voice and historical texture while adding careful source research, faithful translation,
and editorial work for an English-speaking listener. The project is unofficial and is not
affiliated with or endorsed by Alessandro Barbero.

The released website includes the episode catalogue and an RSS feed for Apple Podcasts or any
other podcast app: [podcast.enucatl.com](https://podcast.enucatl.com).

## The agentic research workflow

This repository contains the private production system behind the podcast. It is an explicit-only
Codex repository skill, [`$produce-barbero-episode`](.agents/skills/produce-barbero-episode/), that
coordinates bounded agents around durable, reviewable episode artifacts. Python owns deterministic
transformations, hashes, validation, and status; agents own interpretation, research, translation,
and editorial proposals.

### Model boundaries

- **GPT-5.6 Luna** handles bounded production work: transcript uncertainty review, chapter and
  outline structure, faithful translation, proposal drafting, tense, naturalness, and final
  integration.
- **GPT-5.6 Sol** handles evidence-heavy work: individual historical research, the whole research
  audit, and whole-episode listener synthesis.
- No external-model fallback is used. Sol may return a blocked finding; it may not lower the
  evidence standard.

### Artifact-gated progress

`barbero status EPISODE --json` reports the current `stage`, its `kind` (`machine`, `agent`,
`human`, `complete`, or `invalid`), the next action, blocking items, and relevant artifact paths.
The same result powers the human-readable status output, so an interrupted run resumes from the
last validated artifact rather than from a separate run ledger.

The durable checkpoints are deliberately visible:

- `transcript-uncertainties.yaml` begins at `acoustic-complete`; the semantic Luna pass must mark it
  `complete` before the transcript human gate opens.
- `script.it.md`, `outline.md`, the quotation/claim/source ledgers, and
  `research-audit.yaml` establish research readiness. The audit stores SHA-256 hashes of all five
  inputs; faithful translation is blocked if the audit is absent, blocked, or stale.
- `content-corrections.yaml` and `listener-review.yaml` are the remaining editorial decision
  queues. Humans accept or reject proposals; Python applies accepted patches exactly once and
  preserves quotation, chapter, and transcript boundaries.

## Running the pipeline

```bash
uv sync
uv run barbero init \
  --number 21 --slug il-cavaliere --title "Il cavaliere" \
  --source ~/data/barbero/raw/21.mp3
uv run barbero prepare episodes/021-il-cavaliere/episode.yaml
uv run barbero speakers episodes/021-il-cavaliere/episode.yaml --show
uv run barbero speakers episodes/021-il-cavaliere/episode.yaml --select SPEAKER_00
uv run barbero transcribe episodes/021-il-cavaliere/episode.yaml
uv run barbero render episodes/021-il-cavaliere/episode.yaml
uv run barbero status episodes/021-il-cavaliere --json
```

After the three human queues are resolved, validate and publish only the tokenized, unlisted
preview by default:

```bash
uv run barbero validate episodes/021-il-cavaliere
uv run barbero publish-preview
```

Public release, commits, pushes, provider changes, and overwriting an existing episode require
separate explicit authorization.

## Development

```bash
uv run ruff format .
uv run ruff check .
uv run pytest -q
```

Source audio and provider responses stay outside Git. Reviewed text, research ledgers, decision
queues, hashes, and patch provenance are committed under `episodes/`.
