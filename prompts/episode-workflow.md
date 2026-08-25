# Episode workflow controller (v2)

Run `{episode_directory}` in strict sequence. Preserve stable IDs, exact hashes, and human
decisions. Audio, provider responses, corrections, and logs remain in external `work_dir`; reviewed
artifacts belong in the episode directory.

## Agent execution policy

Run every language-model editorial and review pass with native Codex agents in the current Codex
session. Use native Codex sub-agents for independent, non-overlapping work when delegation is
authorized; otherwise use the primary agent. Never send these passes through OpenRouter, Gemini,
another external model API or CLI, or an external model fallback. If native Codex capacity is
unavailable, wait or ask the user rather than changing providers. This does not prohibit the
explicitly required research and transcription services.

1. Prepare audio. Multi-speaker audio requires an explicit retained-speaker selection; one-speaker
   audio is automatic. Transcribe with repeated Nova-3 keyterms and retained word evidence.
2. Run `transcript-correction.md`. Human gate 1 resolves only pending items in
   `transcript-uncertainties.yaml`. Italian assembly is blocked until none remain.
3. Assemble `script.it.md` with exact ordered utterance coverage. Produce the outline and research
   targets; research quotations separately from claims and run the research audit.
4. Translate complete chapters faithfully into `script.translation.faithful.en.md`. Research wording
   must not enter this baseline.
5. Run quotation-treatment and accuracy prompts into one hash-bound
   `content-corrections.yaml`. Every quotation appears exactly once. Human gate 2 sets each decision
   to `accept` or `reject`, editing `proposed_text` before acceptance when needed.
6. Run `barbero apply-content`. It refuses stale hashes, pending decisions, overlaps, missing
   evidence, or altered protected quote spans and writes `script.content.en.md` deterministically.
7. Run tense review and chapter naturalness separately. Initial chapter files are pending; agents
   replace the pending marker with the exact reviewed marker only after review. Assemble verbatim to
   `script.tense.en.md` and `script.spoken.en.md`.
8. Run `listener-review.md` on the whole spoken script plus outline. Human gate 3 accepts, rejects,
   or edits bounded proposals. No chapter reordering or boundary changes are allowed.
9. Run `barbero apply-listener-review` to create `script.editorial.en.md` and apply an accepted
   audience title to top-level `episode.yaml`. Run narrow final consistency afterward.

`barbero status {episode_directory}` reports the next machine action or one of the three human
queues. At every gate parse YAML, verify hashes, references, exact coverage, chapter identity,
marker order, quotation constraints, and decisions. Finish with:

```bash
uv run ruff format .
uv run ruff check .
uv run pytest -q
uv run barbero validate {episode_directory}
```

Legacy validation exists only for unmigrated episodes. Do not modify unrelated episode artifacts
and do not commit unless explicitly requested.
