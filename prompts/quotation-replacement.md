# Quotation treatment proposals

Read `{faithful_translation_path}`, `script.it.md`, `quotes.yaml`, and the research ledgers. Add
quotation treatments to `{content_corrections_path}`; do not edit a script. Every `Q-NNN` record
must appear exactly once in `references.quotations`, including `not-applicable` and `unavailable`
no-change treatments.

Each `CC-NNN` item must follow the common content-correction schema: an exact bounded
`target.current_text` inside one chapter and its SHA-256, exact `proposed_text`, a concise reason
and evidence summary, ledger references, `recommendation: apply|retain`, and `decision: pending`.
Eligible authoritative wording belongs only in the proposal, never in the faithful baseline. Put
every exact source span that must survive unchanged in `protected_quote_spans`.

Replace the contextual rendering rather than duplicating it. A long authoritative quotation may
be split only at matching clause boundaries around Barbero's existing commentary; preserve every
source word in order. Consolidate overlapping quotation and accuracy treatments before opening the
queue. Do not improve prose, correct unrelated facts, or set a human decision.
