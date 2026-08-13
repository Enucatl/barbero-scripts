# Authoritative quotation replacement

Read `{faithful_translation_path}`, `script.it.md`, and `quotes.yaml`. Produce
`{translation_path}` by replacing Barbero's rendering of each quotation whose record has
`source_replacement: eligible` with the ledger's authoritative English `translation`. Preserve its
`[Q-...]` marker, every chapter and coverage comment, and every unrelated word and marker.

Treat the quotation and Barbero's immediately surrounding delivery as one spoken passage. The
authoritative wording replaces his translation, summary, or representation of the same source; do
not retain that wording beside the replacement and make the listener hear the same content twice.
Remove only an adjacent rendering whose meaning is fully supplied by the source wording. Preserve
his setup, interpretation, examples, emphasis, jokes, and conclusions.

Preserve the original alternation between source and commentary. When Barbero quotes part of a
longer passage, pauses to explain it, and then continues quoting, divide the ledger translation at
the corresponding sentence or clause boundaries and put his commentary between those exact
excerpts. Never move the complete quotation before the explanation or collect all of his comments
after it. Across split excerpts, preserve every authoritative word in its original order; change
only quotation marks, boundary punctuation, or boundary capitalization required by the split.

For `unavailable`, `not-applicable`, paraphrased, or otherwise ineligible records, retain the
faithful contextual translation of Barbero. Do not improve surrounding prose, correct facts, or
perform general naturalness editing.

For each eligible record, compare the input, output, and Italian passage and verify that (1) every
authoritative word appears in order, whether continuously or in source-sized excerpts, (2) no
adjacent contextual rendering duplicates it, and (3) every explanatory interruption remains at
the same point in the argument. Read the complete resulting paragraph aloud. Edit only
`{translation_path}`.
