# Historical research resolution

Research the assigned quotation range `{quote_range}` and claim range `{claim_range}` for
`{episode_directory}`. Read the corrected transcript, outline, and existing ledgers first.

Research historical claims in bounded thematic batches. Research quotations individually using
`prompts/quotation-research.md`; do not batch multiple quotation targets into one agent task.

- Prefer primary documents, critical editions, scholarly publications, and institutional archives,
  but treat a critical edition as a preference rather than an absolute requirement.
- Record exact page, chapter, document, line, folio, or archival locators and stable identifiers.
- For quotations, locate the original-language wording and translate it directly into English.
- Never back-translate Barbero's Italian or silently turn his paraphrase into a quotation.
- Record supporting and conflicting evidence for claims, including evidence that changes the
  planned English treatment.
- Use `resolved` when the wording or historical substance is adequately established for responsible
  adaptation. Sufficient evidence may be an accessible primary document, a reputable documentary
  transcription, consistent contemporary attestations, or strong attribution in reliable
  scholarship. Do not defer an otherwise established item solely because a facsimile, archival
  original, or complete critical edition is inaccessible.
- Record the evidence tier and disclose material limitations in `research_note`, `translation_notes`,
  or the supporting evidence rather than converting every limitation into a deferral.
- Use `deferred` with a `deferred_reason` and a `script_treatment` chosen from `paraphrase`, `omit`,
  `label-anecdotal`, `qualify`, or `research-before-use` when responsible resolution is
  unavailable; never invent a locator or silently omit uncertainty.
- Deduplicate sources and preserve stable `Q`, `C`, and existing `SRC` identifiers.
- Do not alter entries outside the assigned ranges.

Before finishing, parse all YAML, verify every transcript and source reference, verify unique IDs,
and report resolved/deferred totals, substantive departures from Barbero, and remaining risks.
