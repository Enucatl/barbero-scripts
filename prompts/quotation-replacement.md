# Authoritative quotation replacement

Read `{faithful_translation_path}`, `script.it.md`, and `quotes.yaml`. Produce
`{translation_path}` by replacing only quoted wording whose record has
`source_replacement: eligible` with the ledger's exact authoritative English `translation`.
Preserve its `[Q-...]` marker and every other word, chapter, coverage comment, and marker.

For `unavailable`, `not-applicable`, paraphrased, or otherwise ineligible records, retain the
faithful contextual translation of Barbero. Do not improve surrounding prose, correct facts, or
perform naturalness editing. Verify that eligible wording is absent from the input and exact in
the output. Edit only `{translation_path}`.
