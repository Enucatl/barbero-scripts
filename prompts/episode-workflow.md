# Episode workflow controller

Run `{episode_directory}` in strict sequence. Preserve stable IDs and human decisions. Audio,
provider responses, corrections, and logs remain in external `work_dir`; reviewed artifacts belong
in the episode directory.

1. Prepare/select audio and transcribe. Use `transcript-correction.md`, rerender, and then use
   `italian-source.md` to create chapter metadata, `script.it.md`, and `italian-review.yaml`.
   A human must compare every utterance with audio and approve every chapter's exact ordered
   coverage. Validation blocks everything below until this passes.
2. From `script.it.md`, generate `outline.md` and seed `quotes.yaml` and `claims.yaml`. Research
   quotations individually and claims in bounded batches, maintain `sources.yaml`, and run the
   research audit. Markers may be added only in comments or at their spoken passage; they cannot
   change Italian wording. Research never authorizes script corrections.
3. Use `faithful-assembly.md` to translate `script.it.md` directly, chapter by chapter, into
   `script.translation.faithful.en.md`. Do not translate isolated utterances or use Google
   Translate. Translate Barbero's quotations contextually; do not use recovered source wording yet.
4. Use `quotation-replacement.md` as a separate pass to create `script.translation.en.md`.
   Substitute exact ledger wording only for `source_replacement: eligible`.
5. Run `accuracy-review.md`. Human gate: every note must be `apply` or `retain-original`; any
   `pending` decision blocks all downstream output. Preserve existing human decisions and approved
   corrections when rerunning a pilot.
6. Use `approved-corrections.md` to create `script.corrected.en.md`.
7. Run `chapter-tense.md` independently for every chapter. Require one explicitly reviewed
   `tense/CH-NNN.md` per chapter, then concatenate their contents in order—removing only the review
   comments—into `script.tense.en.md`. Do not rewrite during assembly.
8. Run `chapter-naturalness.md` independently for every chapter from the tense-reviewed assembly.
   Require one explicitly reviewed `naturalness/CH-NNN.md` per chapter, then concatenate their
   contents in order—removing only the review comments—into `script.spoken.en.md`. Do not rewrite
   during assembly.
9. Use `final-consistency.md` once to create `script.en.md` from `script.spoken.en.md`. Only terminology, names,
   cross-chapter references, and accidental assembly joins may change. Return material problems to
   the chapter that introduced them.

At each gate parse YAML, resolve references, verify exact ordered utterance coverage, identical
chapter boundaries, marker order, quotation eligibility, and human decisions. Finish with:

```bash
uv run ruff format .
uv run ruff check .
uv run pytest -q
uv run barbero validate {episode_directory}
```

Legacy validation exists only to inspect unmigrated episodes. Episode 008 is the pilot. Do not
modify other episode artifacts and do not commit unless explicitly requested.
