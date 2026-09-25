# Independent review, decisions, and final verification

Use fresh Astra contexts at high reasoning for the two reviews. Both receive the brief, complete
Italian, full draft, evidence dossier, and existing decisions. Do not provide the writer's
self-assessment or the other review. Each reviewer owns only its report and returns proposed
repairs; the coordinator alone changes the draft or queue.

## Review reports

In `review.source.md`, check the full Italian against the English for substantive coverage,
modality, uncertainty, attribution, causal scope, chronology, names, dialogue, rhetorical function,
and exact quotations. Compare approved departures against the decision that authorized them.
Check the dossier's interpretation against its cited evidence where doubtful. Research findings
are not permission to silently substitute facts or make a contested interpretation definitive.

In `review.listener.md`, assess the full narrative arc, audience orientation, referents, vocabulary,
spoken rhythm, transitions, comic timing, quotation length, and argument hierarchy. Preserve strong
material explicitly. Recommend cuts only for a concrete listener benefit; do not impose a shorter
runtime or a compression target unless requested.

Each report records model/effort, input paths and SHA-256 hashes, all chapters covered, strengths,
and located findings. Each finding has a stable ID, chapter/utterance references, severity
(`blocking`, `material`, or `language`), evidence, and an exact suggested repair or decision.
Evaluate both the draft and proposed material changes; approval does not excuse a proposal from
source or listener review. Return a no-change result where appropriate.

Fix demonstrated translation/grammar defects without waiting for routine approval. Repair only
affected passages; ask the relevant reviewer to check the repair and dependencies. Reconcile
conflicting findings against the Italian, evidence, and user preferences. Put judgment calls in
the human package. Every finding must have a recorded disposition: repaired, proposed, retained
with reason, or unresolved. Preserve rejected user choices rather than proposing them again.

Before presenting the package, freeze the repaired draft and consolidate/rebase all pending
proposals against it. Combine overlapping interventions into one coherent choice. If meaningful
alternatives cannot be combined, present the alternatives and obtain a choice before materializing
nonoverlapping accepted patches. A material change to previously approved wording requires renewed
approval of that change; never silently transfer approval to different wording.

Preserve superseded versions in the queue's `history` as snapshots containing their original
`base_script`, `input_hashes`, `items`, and a `reason` for supersession. If a rejected target no longer
exists after an authorized draft repair, archive its original record rather than inventing a new
target or losing the rejection. Retain applicable rejected choices in the brief. Historical items
are evidence of prior choices, not active patches; their old text and sources need not match the
current draft or ledgers. Recheck changed evidence before keeping an accepted proposal active.

## `decisions.yaml`

Use this trial-specific schema. It is not accepted by the old `apply-content` or
`apply-listener-review` commands. Paths in `input_hashes` are relative to `TRIAL`.

```yaml
schema_version: 1
base_script:
  path: script.draft.en.md
  sha256: "actual SHA-256 of the complete frozen UTF-8 file"
input_hashes:
  ../script.it.md: "actual SHA-256"
  brief.md: "actual SHA-256"
  quotes.yaml: "actual SHA-256"
  claims.yaml: "actual SHA-256"
  sources.yaml: "actual SHA-256"
items: []
history: []
```

Each item has these fields:

| Field | Contract |
|---|---|
| `id` | Stable `ED-NNN` |
| `kind` | `fact`, `quotation`, `cut`, `addition`, or `title` |
| `chapter_id` | Existing `CH-NNN`; null only for a title |
| `transcript` | Relevant utterance IDs/ranges |
| `current_text` | Exact nonempty substring of the frozen draft, unique within that file |
| `current_text_sha256` | SHA-256 of that exact UTF-8 string, including whitespace |
| `proposed_text` | Complete replacement; an empty string is allowed for a cut |
| `reason` | Concrete issue, listener benefit, and what the proposal preserves |
| `evidence` | Supporting `Q`, `C`, `SRC`, and review-finding references, or an explanation for purely editorial choices |
| `protected_quote_spans` | Exact strings quoted from the identified source, in replacement order; empty when inapplicable |
| `recommendation` | `apply` or `retain` |
| `decision` | `pending`, `accept`, or `reject` |
| `decision_note` | User decision and its provenance; null until supplied |

A title target is the entire H1 line; it changes only the trial script, not episode metadata.
Script targets stay inside one chapter and preserve headings, chapter coverage, and research IDs.
Use larger context when a short passage is nonunique. Do not create no-op decisions for every
quotation; the research review records unchanged treatments. Every substantive departure must be
traceable to an approved proposal or an explicit prior authorization recorded in the brief.

Present a concise consolidated package with the exact current and proposed passages, reasons,
evidence, and disputed choices. Apply explicit decisions already given, including rejected changes.
Routine wording fixes are not new approval gates. Keep required unanswered decisions pending.

## Deterministic application

Use a deterministic text operation, not language-model regeneration, to create `script.en.md`.
The coordinator may use a short local Python check/application via `uv run python` and standard
library plus the repository's PyYAML. Follow this algorithm and report the actual command/result:

1. Parse the YAML, check unique active IDs, required fields and enums, and verify active input/base hashes.
   Verify source and review freshness; investigate changed inputs before issuing fresh hashes.
   Preserve history as recorded; do not require its old input hashes to match current files.
2. Require all active decisions resolved. Validate accepted target hashes and locate accepted
   targets exactly once in the immutable base. Check chapter membership, unchanged chapter
   boundaries/comments, valid evidence references, and nonoverlapping **accepted** target intervals.
   Rejected proposals are not applied and may overlap accepted cuts. Retain their recorded decision
   and evidence without requiring the rejected replacement to pass current application checks.
3. For accepted proposals, confirm protected quotation spans match the cited ledger wording, occur
   in the proposed text in order, and are actually presented as quotations. For excerpts, verify
   retained words and omitted boundaries; paraphrased portions stay outside quotation marks.
   Semantic presentation also needs the source review; a substring check alone is insufficient.
   Check all surviving authoritative spans in the evidence review's inventory as well, including
   inherited approved quotations. An approved excerpt/cut changes the expected inventory explicitly;
   retain its original provenance. Historical or rejected wording is not part of this output check.
4. Starting from the frozen draft each time, apply accepted replacements by original offsets in
   descending order. A rejection contributes no replacement; another explicitly accepted edit may
   affect that passage. Never patch a previously patched final file.
5. Before writing, check chapter/coverage/marker invariants and that the result exactly equals the
   expected application. If a final file already exists, allow an identical no-op; investigate a
   differing file and preserve user edits instead of overwriting it. Write a new final only after
   preconditions pass. Do not apply a partial queue or generate final text while decisions are pending.

The absence of a dedicated trial CLI is not permission to skip these checks or describe them as
already automated by the repository. Hashes should come from actual file bytes, not model output.

## Final review and `verification.md`

Check the applied passages against the Italian, evidence, and exact decisions. Check consequences
across chapters, especially renamed people, earlier/later references, repeated explanations, scene
chronology, and quotation/commentary joins. Read the final narration from beginning to end. If a
repair is needed, record it in the draft/decision history and reapply with fresh verified hashes;
do not make unexplained edits only in the final. Recheck affected findings and dependencies rather
than reflexively rerunning every investigation.

Record:

- Actual source, brief, research, draft, queue, review, and final file hashes; writer/reviewer models
  and efforts, and whether reviews used fresh contexts.
- Source wording and ordered coverage results, ledger/reference checks, exact decision application,
  protected quotation checks, and the commands used for deterministic verification.
- Disposition of every review finding, accepted/rejected decision totals, final English word count,
  continuity/read-aloud text review outcome, and unresolved evidence qualifications.
- Status `ready-for-recording` only when required decisions are resolved, findings are addressed,
  the final reflects the reviewed choices, and all applicable checks pass; otherwise `blocked`
  with the precise remaining work. Say whether audio/performed listening was actually assessed.

Review reports retain their original input hashes. When repairs change a reviewed file, append a
follow-up identifying the new hashes and findings/dependencies rechecked; do not relabel an old
report as a new full review. If the scope of change invalidates the whole review, perform it again.
An unchanged completed trial can resume from current verification rather than repeat production.

Report `TRIAL/script.en.md` as the trial recording script. Export to the canonical episode or
publication requires a separately requested integration step because the old validators expect
the original staged artifacts. Do not change production metadata or claim a preview was built.
