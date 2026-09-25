# Evidence before adaptation

Read the complete Italian and brief. Investigate every quotation or attributed paraphrase, central
causal/interpretive claims, historically disputed assertions, and a representative sample of
incidental facts. Keep `Q-NNN`, `C-NNN`, and `SRC-NNN` IDs stable across the trial.

Use retrieved evidence, not model recall, to establish a quotation or correction. Open supporting
sources; record locators and limitations. If retrieval is unavailable, preserve unresolved entries
and report the exact missing capability. Search relevant original languages, follow scholarly
citations, and distinguish editions and translations. Prefer primary documents and strong
scholarship; an inaccessible ideal edition need not block a responsibly established finding.

Related targets may share an investigation. Keep every quotation's speaker, document boundaries,
wording, and verdict separate. Researchers return evidence to one ledger owner. Do not authorize
multiple workers to edit the same YAML files concurrently.

## Trial ledgers

Each file is a YAML list. Use actual values, explicit nulls, and empty lists where unresolved.
These records are local to `TRIAL`, not inputs to the old application commands.

| File | Required fields per record |
|---|---|
| `quotes.yaml` | `id`, `transcript` (utterance IDs or inclusive ranges), `attribution`, `quotation_kind`, `source_ids`, `original_language`, `original_text`, `translation`, `locator`, `verdict`, `source_replacement`, `status`, `research_note` |
| `claims.yaml` | `id`, `transcript`, `claim`, `centrality`, `supporting_sources`, `conflicting_sources`, `status`, `research_note` |
| `sources.yaml` | `id`, `title`, `author`, `date`, `url` or `identifier`, `edition`, `locator`, `accessed`, `evidence_type`, `limitations` |

Use quotation kinds `direct`, `paraphrase`, or `composite`; verdicts `confirmed`,
`confirmed in substance`, `misattributed`, `composite`, or `unresolved`; replacement status
`eligible`, `not-applicable`, or `unavailable`. Research status is `pending`, `resolved`, or
`deferred`. Every deferral explains the remaining problem and its consequence for narration.
Claim centrality is `central`, `supporting`, or `sampled-incidental`.

Record exact original wording when recoverable, and a direct English translation. For an English
original, `translation` equals `original_text` exactly. Never back-translate Barbero and present the
result as a recovered source. Label translation dependencies, later recollections, anecdotes,
official records, and scholarly interpretations accurately. For composites, identify each component
and its locator; replacement is eligible only when wording and boundaries are recoverable.

The claim's research note must explain what the evidence supports, disputes, or leaves uncertain,
including denominators, chronology, attribution, and causal scope where relevant. A contested
interpretation is not automatically a factual error. Preserve Barbero's argument unless an approved
intervention changes it. Evidence sufficiency and editorial permission are separate decisions.

Existing ledgers may be reused after checking their relevance and provenance. Preserve their IDs
where reused, copy only needed records into the trial, and record their origin. Do not mark copied
research newly verified without inspecting its support.

## `research-review.md`

Audit the dossier once the investigations finish. Record the model/effort, input paths and SHA-256
hashes of the brief, Italian, and all three trial ledgers, quotation and claim totals, and a verdict
of `ready` or `blocked`. Explain treatment-changing findings, unresolved limitations, and proposed
interventions with their `Q`, `C`, and `SRC` references.

Check completeness against the Italian, validate YAML and all referenced IDs/ranges, deduplicate
sources, and reconcile contradictory dates, speakers, genealogy, institutions, and document types.
An inaccessible source may justify a disclosed deferral and a faithful contextual rendering.
If uncertainty prevents responsible narration of a central passage, report the blocking question
and options. Do not invent evidence or silently drop the passage.

Every quotation needs an explicit intended treatment: contextual rendering, proposed recovered
wording, exact excerpt, or clearly signalled paraphrase. Recovery does not require inserting an
entire long source passage; propose the relevant excerpt with its boundaries and reason. Preserve
Barbero's alternation between quoted fragments and commentary.
For every authoritative quotation in the draft or an accepted proposal, record the exact rendered
spans and their source IDs/locators in this review, including wording approved before the trial.
Use that inventory for final quotation checks, not only the new proposals' protected spans.

If any recorded input changes, review its evidence and downstream consequences before refreshing
the verdict. Updating hashes alone does not establish readiness. Approval of a factual change
belongs in `decisions.yaml`, even when the research verdict is certain.
