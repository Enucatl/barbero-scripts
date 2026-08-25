# Focused quotation research

Research exactly one quotation target: `{quotation_id}` in `{episode_directory}`.

You have web search available and must use it. Read the quotation ledger entry, its passage in
`script.it.md`, and the surrounding outline chapter before searching.

## Research brief

Start the task with a worksheet containing:

- Barbero's Italian wording and timestamp.
- An approximate English rendering clearly labeled as unverified.
- Claimed speaker, document, date, and setting.
- The precise evidence needed to verify the target.
- Likely primary sources, editions, archives, memoirs, diaries, and scholarly source families.
- Search queries in English and relevant original languages.
- Chronological, institutional, linguistic, or genealogical cautions.

## Search method

Focus the entire pass on this one target.

1. Search iteratively in English and the likely original language.
2. Follow citations recursively from scholarship into editions, archival catalogues, memoirs, and
   contemporary documents.
3. Open digitized books and search their OCR or full text; do not rely only on search-result
   snippets.
4. Check alternate editions, translations, volume numbering, document numbering, and pagination.
5. Separate distinct documents, meetings, dates, speakers, annotations, and later recollections
   that Barbero may have compressed into one scene.
6. Identify whether the surviving wording is a contemporary record, official protocol, later
   eyewitness recollection, memoir, scholarly attribution, or anecdotal tradition.
7. Continue until the quotation is responsibly established or the remaining provenance problem is
   specific and genuine.

Do not stop merely because an archival original, facsimile, or critical edition is inaccessible.
An accessible primary document, reputable documentary transcription, consistent contemporary
attestations, named eyewitness recollection, memoir with disclosed limitations, or strong
scholarly attribution may establish the target.

## Required result

Return:

- A clear verdict: `confirmed`, `confirmed in substance`, `misattributed`, `composite`, or
  `unresolved`.
- Exact original-language wording when recoverable.
- A direct English translation.
- Speaker, date, setting, document type, and transmission history.
- Exact publication and archival locators, with stable URLs or identifiers.
- A comparison showing how Barbero quotes, compresses, modernizes, dramatizes, misdates, or
  combines the evidence.
- Material limitations and the appropriate evidence tier.
- `quotation_kind`, `verdict`, and `source_replacement`. Replacement is `eligible` for a recovered
  direct original with reliable English wording. A composite may also be `eligible` when every
  component has recoverable English wording, clear source boundaries, and a ledger translation
  that joins only those documented components. Use `not-applicable` for paraphrases and composites
  with no cleanly recoverable component wording, and `unavailable` when reliable wording was not
  recovered.

Never back-translate Barbero, invent a locator, silently merge speakers or documents, or describe a
later recollection as a contemporary transcript.

The ledger `translation` field is always English. If `original_language: en`, copy `original_text`
exactly into `translation`; never translate an English original into Italian. For every other
language, store the researched direct English rendering, not Barbero's Italian wording.

## Ledger update

After reporting the evidence:

1. Add deduplicated source records to `sources.yaml`.
2. Update only `{quotation_id}` in `quotes.yaml`.
3. Preserve stable IDs and transcript references.
4. Record exact wording, direct translation, locator, evidence limitations, confidence, status,
   plus quotation kind, verdict, and source-replacement status.
5. Update the external research audit when one exists.
6. Parse YAML, resolve every source reference, and run editorial validation.

Research completion establishes technical source-replacement eligibility but does not approve a
content change. Human decisions belong only in the later unified content queue.

Do not edit other quotation or claim records and do not create a Git commit.
