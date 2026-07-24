# Accuracy review

Require `{translation_path}` to exist and pass section-level coverage validation before starting.
If it is missing or incomplete, stop: accuracy notes cannot sensibly be reviewed against a
baseline that does not yet exist. Compare that faithful translation with the transcript and
complete research ledgers. Write findings to `{accuracy_notes_path}`; do not edit any script.

Record only demonstrable factual errors, misleading compression, genuinely disputed claims, and
material uncertainty. Each YAML record must contain a stable `N-001`-style ID, transcript range,
optional `claim_ids`, `quotation_ids`, and `source_ids`, `category` (`factual-error`,
`misleading-compression`, `disputed`, or `material-uncertainty`), `original_assertion`,
`proposed_correction`, and `decision: retain-original`. Put the precise, minimally scoped script
change in `proposed_correction`, written as natural replacement narration rather than a fact-checking
note or a comparison with Barbero's assertion. Do not add a separate assessment field. This conservative default
preserves Barbero unless a human explicitly changes the decision to `apply`; the reviewer may add
`decision_note`.

Resolve every reference, distinguish evidence from inference, and leave no research finding hidden
in prose outside the ledger. Do not create a commit.
