# Pass 2: lossless translation assembly

Read the Italian transcript, raw Google utterance translations, outline, and quotation ledger in
full. Using the current session's model, assemble the utterance translations into coherent
paragraphs and longer outline sections in `{assembled_translation_path}`. Join fragments and
correct language errors, names, referents, idioms, and misunderstandings exposed by context, but
do not summarize, compress, reorder, add explanations, or omit substantive repetition.

For every quotation, obey `source_replacement`. When `eligible`, replace only the quoted wording
with the current ledger `translation` verbatim and attach `[Q-...]`; when `not-applicable` or
`unavailable`, do not copy or insert the ledger `translation` or `original_text`: faithfully
translate Barbero's transcript wording in context and attach `[Q-...]` to that passage. The ledger
`translation` field must be English in all cases, but it authorizes script wording only when
`source_replacement: eligible`. Add applicable `[C-...]` and useful `[SRC-...]`
markers. Give every section an inclusive transcript-range comment and report every permitted
omission with its range and reason.

Do not call Google or another external translation/model service in this pass. Before finishing,
account for every utterance ID against the assembled section, verify every
eligible quotation verbatim, scan the assembled prose for untranslated Italian, and confirm the
Q/C marker sets. Edit only
`{assembled_translation_path}` and do not create a commit.
