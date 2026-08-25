# Whole-episode listener review

Read all of `{spoken_path}` together with `{outline_path}` and write `{listener_review_path}`. Do
not edit the script. Assess what an intelligent contemporary American without period expertise
must understand, remember, and experience; identify the argument or narrative spine and strengths
to preserve.

Recommendations are bounded exact patches against `script.spoken.en.md`, each limited to one
chapter with a current-text SHA-256 and `decision: pending`. They may add a short gloss or
orientation sentence, compress an example run, substitute a description for an incidental name,
remove obsolete lecture framing, or excerpt a long quotation. They may not reorder chapters or
change boundaries. Title proposals use `target.kind: title` and update top-level `audience_title`;
the Italian `title` is immutable.

For each recommendation record `listener_need: understand|remember|experience`, severity,
outline sections, reason, what it preserves, and quotation references. Every surviving quoted word
must be exact source wording and every excerpt must name its `Q-NNN` record and remain clearly
distinguished from paraphrase.

For `issue_type: quotation-audio`, never emit a reminder or a no-op patch. Set
`target.current_text` to the complete rendered quotation passage exactly as it appears in
`script.spoken.en.md`, including its immediate introductory framing when the proposal changes that
framing. A short opening fragment is invalid. The target must contain all authoritative words from
the referenced `Q-NNN` record in their rendered order. Set `quotation_treatment` to exactly one of
`exact-excerpt`, `excerpt-with-paraphrase`, or `paraphrase`, and provide the complete replacement
passage in `proposed_text`. Any words retained inside quotation marks must remain verbatim; omitted
material may be summarized only outside quotation marks and must be unmistakably presented as
paraphrase.

Never manufacture suspense, generic podcast transitions, jokes, mechanical callbacks, gratuitous
analogies, or slang. Do not automatically delete digressions. In particular, avoid “but here's the
twist,” “here's where it gets interesting,” “you won't believe,” “let's dive in,” and “buckle up.”
The listener agent proposes; only a human accepts, rejects, or edits the exact proposal.
