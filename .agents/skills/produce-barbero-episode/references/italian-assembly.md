# Establish the Italian source

Begin only after the semantic transcript pass and the user's uncertainty decisions are complete.
Rerender the resolved transcript with `barbero render` when necessary. Read `{transcript_path}` in
full and define numbered chapters in `chapters.yaml` with complete ordered utterance coverage.
Preserve fillers, repetition, false starts, spoken grammar, jokes, and digressions. If a new
recognition problem appears, return it to the uncertainty queue for a user decision; do not edit
`corrections.yaml`, resolve pending items, or silently rewrite the transcript in this stage.

After defining chapters, run
`barbero assemble-italian {episode_directory}`. The assembler may join utterances into continuous
paragraphs and add punctuation already present in the transcript; it must not change the text that
would be recited. Research markers belong in HTML comments and must not alter spoken wording.

The exception queue replaces the full utterance checklist. Exact ordered coverage remains a
deterministic validation invariant. Do not create an outline, research ledger, translation, or
English script until every uncertainty is resolved and `barbero validate` confirms the checkpoint.
