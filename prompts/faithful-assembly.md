# Faithful English assembly

Before starting, require every quotation in `quotes.yaml` to have `human_reviewed: true`. Stop if
any quotation is explicitly unreviewed; completed research alone is not approval.

Read `script.it.md` in full, then translate it chapter by chapter with the language model. Produce
`script.translation.faithful.en.md` with exactly the same numbered chapters, headings, coverage
comments, and marker sequence as the Italian source. A chapter is the translation unit: do not
translate isolated utterances or use Google Translate.

Translate closely in the context of the complete chapter. Preserve modality, repetition,
rhetorical structure, jokes, digressions, and every substantive detail. Translate Barbero's quoted
wording contextually at this stage. Do not insert recovered wording from `quotes.yaml`, fact-check,
compress, naturalize strongly, or add connective prose.

Verify complete ordered ID coverage and confirm that exact authoritative wording for every
eligible quotation is absent. Edit only `script.translation.faithful.en.md`.
