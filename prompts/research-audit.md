# Episode research audit

Audit all research ledgers for `{episode_directory}` after the individual quotation and claim
research tasks are complete. Read `script.it.md`, outline, `quotes.yaml`, `claims.yaml`,
and `sources.yaml` in full. This is a consistency and sufficiency review, not a new adaptation pass.

Use web search when checking a doubtful result, a missing locator, a contradiction, or an
unnecessary deferral. Prefer primary and scholarly sources, but apply the practical evidence
standard in `historical-research.md`: inaccessible facsimiles or critical editions do not make
otherwise established material unusable.

## Audit checks

- Every quotation or attributed paraphrase in the transcript has a stable quotation entry.
- Each resolved quotation has recoverable original text or a disclosed translation dependency,
  direct English translation, speaker, document type, date or context, exact locator, confidence,
  quotation kind, verdict, and source-replacement status.
- Every quotation `translation` is English; when `original_language: en`, it exactly equals
  `original_text`. Reject Italian or other intermediate-language translations.
- Composite wording, memoir evidence, protocols, marginal annotations, named recollections, and
  later anecdotes are labelled distinctly.
- A composite may use `source_replacement: eligible` only when every component is recoverable in
  English and its document boundary is disclosed; composite status alone does not force paraphrase.
- Every central claim and the intended incidental sample has supporting or conflicting evidence
  and a treatment that follows that evidence.
- Evidence standards are consistent across entries. Do not leave an item deferred merely because
  the best edition is inaccessible when contemporary attestations or strong scholarship establish
  it responsibly.
- Genuine negative findings remain deferred with a precise reason.
- Source records are deduplicated; IDs, URLs, identifiers, access dates, editions, and locators do
  not conflict.
- Genealogy, chronology, institutional setting, speaker identity, and document separation are
  checked wherever Barbero compresses a scene.
- Discrepancies are documented for the later accuracy review, not applied here.

## Output and edits

Report findings by severity: blocking, treatment-changing, and housekeeping. Correct ledger
inconsistencies that the evidence already resolves. Do not silently resolve an item that requires
substantial new research; instead perform that focused research or return it to an individual
research task.

Before finishing, parse every YAML file, confirm unique IDs and valid transcript/source references,
run editorial validation, and report:

- resolved and deferred totals;
- quotation entries by evidence type;
- claims that may require an accuracy note;
- remaining genuine risks;
- whether research is ready for faithful translation and accuracy review.

Do not edit the English script and do not create a Git commit.
