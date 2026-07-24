# Pass 3: faithful formatting and consistency

Read the Italian transcript, `{utterance_translation_path}`, `{assembled_translation_path}`, the
outline, and ledgers in full. Produce `{translation_path}` from the assembled draft.

Add proper Markdown formatting and make names, titles, dates, capitalization, transliteration,
and spelling consistent across the episode. Fix unclear joins and assembly mistakes. Preserve the
meaning, sequence, examples, repetition, digressions, jokes, and rhetorical structure of every
utterance. Do not perform the later idiomatic-polishing pass, factual correction, qualification,
compression, or research-driven omission. Do not alter eligible quotation wording or Q/C marker
sets. Add no pronunciation cues.

Audit every `[Q-...]` passage against `source_replacement`: `eligible` must retain the ledger's
English translation verbatim; `not-applicable` and `unavailable` must retain the faithful English
translation of Barbero and must not acquire ledger source wording. Reject untranslated Italian or
another non-English working language anywhere in the narration or quotations.

Compare every final section with both the utterance YAML and Italian transcript. Validate complete
coverage, all references, exact eligible quotation wording, and marker preservation. Edit only
`{translation_path}` and do not create a commit.
