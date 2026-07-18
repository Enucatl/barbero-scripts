# Episode workflow controller

Run the complete editorial workflow for `{episode_directory}`. Treat each phase below as a gate:
verify its outputs before advancing, preserve stable IDs, and never overwrite human-approved work.
Generated audio, provider responses, corrections, hashes, and logs belong under the configured
external `work_dir`; only reviewed editorial artifacts belong in Git.

## Agent allocation

- Use one agent to review the complete transcript and produce corrections.
- Use one agent to outline the corrected transcript, then seed quotation and claim ledgers.
- Assign exactly one web-enabled research task per quotation using `quotation-research.md`.
- Assign historical claims in bounded thematic batches using `historical-research.md`.
- After all research tasks finish, use one agent with `research-audit.md` across the complete episode.
- Use one adaptation agent with `english-adaptation.md`, working in consecutive sections.
- Use one final agent with `performance-readiness.md` across the complete script.

Agents share the repository. Give each one non-overlapping files or ledger IDs, wait for it to
finish, inspect its changes, and validate before starting work that depends on those changes. Web
search must be enabled for quotation and historical research tasks. Never assume that a spawned
agent has searched merely because its prompt mentions sources; require citations and locators in
its result.

## Phase 1: initialize and prepare audio

If the episode directory does not exist, create it with `barbero init`. Confirm that the configured
source file is the intended immutable recording. Obtain provider credentials from the environment
or Vault without writing or printing them. Run:

```bash
uv run barbero prepare {episode_config}
uv run barbero speakers {episode_config} --show
```

Human gate: listen around every retained/removed boundary, confirm the dominant speaker, opening,
closing, and absence of clipped lecture speech. If necessary, select the speaker and rerun
`prepare`. Do not begin transcription until this is approved.

## Phase 2: transcribe and correct

Run `uv run barbero transcribe {episode_config}` and render the initial transcript. Use
`transcript-correction.md` against the entire transcript. The correction agent may use episode-wide
historical and linguistic context but must not claim to have listened to audio.

Human gate: review `corrections.yaml`, set every accepted decision to `reviewed: true`, and
spot-check low-confidence words, names, dates, quotations, and material corrections against audio.
Render again and require zero unresolved transcript review flags.

## Phase 3: map and seed research

Use `episode-outline.md`, then `research-target-extraction.md`. Verify continuous utterance
coverage, sequential stable IDs, timestamps, and YAML parsing. Commit the corrected transcript,
outline, and pending ledgers before external research begins.

## Phase 4: research

Research quotations individually and claims in thematic batches. Each task edits only its assigned
IDs. Require original-language text where recoverable, direct English translation, exact locators,
evidence limitations, and a script treatment. Accept established material without demanding an
inaccessible critical edition, but never invent provenance.

Run `research-audit.md` only after every research task has returned. Resolve audit findings, parse
all YAML, verify source references, and run editorial validation. Human gate: inspect genuine
deferrals and every planned departure from Barbero. Commit the complete research ledgers.

## Phase 5: adapt

Use `english-adaptation.md`. Complete sections in transcript order and keep the annotated script's
markers intact. Render the recording copy after each coherent block and run validation. Do not
compress toward a predetermined duration: preserve Barbero's sequence, accumulation, digressions,
and rhythm while writing idiomatic spoken English.

Human gate: review an early representative section for voice before the agent drafts the entire
episode. Once approved, keep the same style boundary through the end.

## Phase 6: finish

Use `performance-readiness.md`, update outline housekeeping, render, format, test, and validate:

```bash
uv run barbero render {episode_config}
uv run ruff format .
uv run ruff check .
uv run pytest -q
uv run barbero validate {episode_directory}
```

Human gate: perform and time the complete recording script aloud. Record actual duration and
reading rate. Apply only performance-driven edits that preserve researched meaning and quotation
wording, regenerate the recording copy, and repeat validation. The episode is complete only when
audio boundaries, transcript flags, research treatments, pronunciation, and the timed read-through
have all been approved.

## Version-control boundary

Keep commits phase-specific and reviewable. Never commit credentials, audio, provider JSON, model
caches, temporary PCM, or the external corrections file. Before every commit, inspect the diff and
preserve unrelated user changes. This controller does not authorize publishing, pushing, or
opening a pull request.
