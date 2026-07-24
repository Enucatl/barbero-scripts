# Episode workflow controller

Run the supervised editorial workflow for `{episode_directory}` in strict sequence. Preserve stable
IDs and never overwrite human-approved work. External audio/provider artifacts remain under the
configured `work_dir`; reviewed text and ledgers belong in the episode directory.

1. Prepare audio, select the retained speaker, transcribe, and apply reviewed transcript
   corrections. Human approval of audio boundaries and every transcript review flag is mandatory.
2. Create the structural outline and seed claim and quotation ledgers. Research quotations one at
   a time with `quotation-research.md`, claims in bounded batches with `historical-research.md`,
   then run `research-audit.md`. Research records discrepancies but cannot authorize corrections.
3. Use the three-pass controller in `faithful-translation.md`: translate every utterance into
   `translation.utterances.en.yaml`, losslessly assemble `script.translation.assembled.en.md`, then
   format and normalize the final `script.translation.en.md`. Each pass is a separate sequential
   pass. Google Translate is permitted only for the raw utterance YAML in pass one. Passes two and
   three use the current session's model and may not call an external service, separate Codex CLI,
   or selected model. Validate every utterance before assembly and every eligible researched
   quotation verbatim afterward.
4. Only after the faithful translation exists and passes coverage checks, use
   `accuracy-review.md` to create `accuracy-notes.yaml`. Do not generate or present notes for human
   review before this prerequisite is met, and do not edit the translation during accuracy review.
5. Human gate: review every note. Notes default to `retain-original`; a human must explicitly
   change accepted corrections to `apply`. Do not create corrected or final scripts while any
   decision is `pending`.
6. Use `approved-corrections.md` to create `script.corrected.en.md`, applying only accepted notes.
7. Use the two-pass controller in `idiomatic-polishing.md`: create `script.spoken.en.md` with a
   strong conversational rewrite, then audit it against `script.corrected.en.md` to produce the
   annotated, directly recordable `script.en.md`. Keep research/correction markers, comments, and
   speaker notes for manual skipping. Never generate pronunciation cues or a recording copy.

At every gate parse YAML, resolve transcript/claim/quotation/source/note references, verify marker
sets and section coverage, and run `uv run barbero validate {episode_directory}`. Finish with:

```bash
uv run ruff format .
uv run ruff check .
uv run pytest -q
uv run barbero validate {episode_directory}
```

Pilot the workflow on episode 008. Stop at its human accuracy-decision gate; do not replace its
existing final script until all prior stages pass and every decision is resolved. Process later
episodes individually. Do not create Git commits unless explicitly requested.
