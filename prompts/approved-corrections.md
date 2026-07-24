# Apply approved accuracy corrections

Read `{translation_path}` and `{accuracy_notes_path}`. Stop if any decision is `pending`. Produce
`{corrected_path}` by applying exactly the current `proposed_correction` of notes marked `apply`;
preserve original wording for `retain-original`. The proposal is the sole authority for the scope
of a correction: do not infer additional changes from research ledgers, source records, category,
or other context. Mark every applied change with its `[N-...]` ID and never mark a retained note.

Integrate every approved correction naturally and invisibly into the narration. State the corrected
fact directly in Barbero's narrative voice. Never describe the correction process, contrast the
corrected fact with what Barbero said, or add fact-checking language such as “Barbero says,” “in
fact,” “actually,” “however,” “though estimates are disputed,” or “the evidence suggests” merely to
signal that a correction occurred. Include uncertainty or disagreement only when it is itself part
of the approved `proposed_correction`, and then express it as ordinary narrative content rather than
an editorial note. The `[N-...]` marker is the only trace of the intervention in the script.

Change nothing else: preserve meaning, order, detail, quotation wording, and all quotation markers.
For quotations, preserve the `source_replacement` boundary: never insert ledger wording for a
`not-applicable` or `unavailable` record, and never introduce untranslated Italian.
Run `barbero validate`. Edit only `{corrected_path}` and do not create a commit.
