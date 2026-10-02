# Final source-fidelity review — episode 013

Reviewed 2026-10-02. **Recommendation: blocked by one newly introduced chronology contradiction, FS-001.** The final otherwise applies the user's selected changes faithfully, preserves every rejected target, and retains the source's substantive argument and examples. This is a final text review, not a renewed request to accept rejected historical corrections.

The coordinator confirmed the requested host configuration as **gpt-6-astra, high reasoning, fresh context (`fork_turns: none`)**. That is requested configuration, not independently measured model telemetry. I did not write the adaptation, read the listener review, or receive the writer's self-assessment. I read the complete settled Italian, complete final English, brief, all 41 quotation records, all 29 claim records, all 35 source records, all 34 active decision records, and the original source review with its follow-up. I inspected the complete draft-to-final diff and used the frozen draft for deterministic checks. The historical queue was consulted as provenance; it was not treated as an active decision package. Existing documentary research remains the evidence base; no new external retrieval or audio/performed listening was undertaken.

## Actual inputs

Hashes were calculated from file bytes with `sha256sum`; paths are relative to `editorial-v2/` unless stated otherwise.

| Input | SHA-256 |
|---|---|
| `../script.it.md` | `40d4433f29e3d0da07235e91730b9ba487954ec6d39fd53e0ff19f21ec209bb9` |
| `brief.md` | `e70bdfbfbed1f900320efac6a08846827d9efb00d35d3a3efcc4bb5aee986251` |
| `quotes.yaml` | `88d14227ff6d18c54332ba0ca7b018e87842b21f3b7f415a2098692d12dd6971` |
| `claims.yaml` | `83b041304eeea35bbb8bb1a7f01d95738efde42b0da403dab2561c5868654f33` |
| `sources.yaml` | `75ad7e709fdfdbd27df6024a5a1f36f49de2254edfe392895a655be462829759` |
| `script.draft.en.md` | `8e6f34e62412bc04f56ba54d6a093b257dc18c3d3a9760379f33e51e5796a173` |
| `decisions.yaml` | `fbb92fc5bec927653a6eef063b65b7e4bbdf35bcead7a500ac220beacd93c61f` |
| `review.source.md` | `99459d6e3be4b1fb364f36acfd495e526e66b6165dc58978db47b26b3b408f9c` |
| `script.en.md` | `95574fa23c22c0993c45981c974c8923f687f532ebd6faed39b6ca0d34585860` |

Instruction files relative to repository root:

| Input | SHA-256 |
|---|---|
| `.agents/skills/produce-barbero-episode-v2/SKILL.md` | `58f8ff2de287ae1aee366198f358573d0d4da4a7a6e432f9c672d7f03dfcd044` |
| `.agents/skills/produce-barbero-episode-v2/references/review-and-decisions.md` | `6789e65b004165b9efe985ad890fa75bef7baf3d47736f9d6d3063ceb88b565f` |

## FS-001 — blocking — inconsistent date for Abbo's book

**Location:** CH-005, U-00335–00343, U-00356–00361, U-00407–00417; final lines 189, 205, 237. Dependencies: accepted ED-006; rejected ED-008 and ED-010; C-012, SRC-011/012.

The final introduces the book with:

> Around 994, he writes a short book addressed to the French kings Hugh Capet and Robert.

It then says:

> Not so much lately—we're in 998—but in the past, from time to time, and people had to work quite hard to calm everybody down.

And concludes:

> By 998, when Abbo writes, these are memories of his youth.

All three passages concern the same act of writing and recalling earlier episodes. The surrounding narration supplies no later revision or second work that would reconcile them. The settled Italian consistently uses 998; the dossier supports a probable date around 994. The contradiction is created by this particular combination of decisions, rather than inherited unchanged from the lecture. The earlier source review explicitly identified ED-006/008/010 as a linked date dependency.

**Disposition: unresolved.** The final correctly reproduces the decisions, so this is not an application error. Replacing or deleting either retained date changes factual wording inside an explicitly rejected target. Reverting the accepted date changes approved wording. Neither is a strictly routine grammar or referent repair, and no choice has been silently made.

The smallest concrete reconciliations are listed here solely to resolve the new contradiction. They do not reopen the rejected Advent, rumor-circulation, youth, creed, or other historical interventions.

1. **Keep the approved approximate date and align only its two callbacks:** replace `Not so much lately—we're in 998—but in the past` with `Not so much lately—we're around 994—but in the past`; replace `By 998, when Abbo writes, these are memories of his youth.` with `By around 994, when Abbo writes, these are memories of his youth.` All other rejected wording stays intact.
2. **Keep the two retained 998 callbacks and revise only the introductory date:** replace `Around 994, he writes a short book addressed to the French kings Hugh Capet and Robert.` with `In 998, he writes a short book addressed to the French kings Hugh Capet and Robert.` This preserves the approved addressees but relinquishes the accepted dating correction and its documentary support.

Either reconciliation needs an explicit targeted decision. The skill states: “A material change to previously approved wording requires renewed approval of that change; never silently transfer approval to different wording.” The coordinator should record the chosen exact repair in the draft/decision history, reapply deterministically, and recheck these three locations. No full research restart is needed.

## Complete coverage and continuity

| Chapter and source range | Final review outcome |
|---|---|
| CH-001, U-00001–00069 | Friends' surprise, myth definition, general apocalyptic expectations versus universal shutdown, and Romantic framing survive. Opening retains the authorized series-finale position. |
| CH-002, U-00070–00129 | Carducci's role is introduced as approved. Questions, sunrise payoff, Lavallée catalogue and rough-translation frame survive. Accepted live-joke removal leaves two coherent quotation paragraphs with the same attribution. |
| CH-003, U-00130–00240 | All three documentary cases, contract details, Gerbert/magic, handshake/notary, sharecropping/Olmi and retired-adviser material remain. ED-001–004/031 rejections are preserved. Existing source/evidence qualifications are not new blockers. |
| CH-004, U-00241–00334 | Chroniclers, known-ending/blank-pages joke, Revelation uncertainty, quotation, interpretation and sect digression survive. Accepted ED-005 correctly identifies the opening excerpt; ED-032 limits the local documentary conclusion without removing the earlier narrative. |
| CH-005, U-00335–00417 | Examples, King Robert's direct address, Paris preacher, Richard, calendar reasoning, 908/970 and technical-expression joke survive. “Still around 970” retains its antecedent because ED-009 was rejected. Only FS-001 prevents continuity approval. Dual dedication does not invalidate the specific closing address to Robert. |
| CH-006, U-00418–00503 | Bible, Augustine, hypothetical objection, Thiota and coercive ending retain their source functions. Accepted ED-011 removes Augustine's priority claim while leaving his importance and quotation intact. ED-012–014 rejected wording is preserved. |
| CH-007, U-00504–00620 | The live callback is removed consistently with CH-002. Historian's embarrassment, preparation aside, copying mechanism and complete chronicler sequence survive. Accepted ED-015 describes Sigebert's arrangement; ED-016/017 retained material introduces no new cross-reference defect. |
| CH-008, U-00621–00724 | Accepted ED-033 places the origin story in the historians' constructed picture, and the following examples sustain that viewpoint. Bettinelli quotations, narrator glosses and Carducci callback survive. Rejected ED-018 publication wording remains. |
| CH-009, U-00725–00807 | Ideological setting, historical qualification and Barbero's explicit personal judgment survive. All three rejected priority changes remain unapplied; the paragraph sequence stays coherent. |
| CH-010, U-00808–00907 | Accepted ED-022/023/024/025/027 produce coherent 1999-before-2008 chronology, an explicitly personal reading of ideological motivation, and an attributed translation-center thesis. Controversy, partial-reading disclaimer, retained polemical paraphrase and conclusion remain. Rejected ED-026/034 are not reopened. Finale farewell matches the authorized release order. |

No additional substantive omission, translation repair, naming inconsistency, newly broken callback, or quotation/commentary join was found. This is a text-based full-narration and source-continuity judgment, not performed-listening evidence.

## Quotations and attribution

All 41 Q records were compared with their surviving final treatments and the supplied Italian. None of the 14 accepted decisions introduces a protected authoritative quotation span: ED-003 and ED-007 were rejected. The entire diff confirms that the inherited quoted words are unchanged. ED-005 changes the Revelation introduction only; ED-028 removes an interruption between the two Lavallée spans only.

- Q-001–004 retain Carducci's rhetorical questions, traditional attribution nested inside Carducci, inherited selected clauses, and Lavallée's expressly rough translation. The approved cut changes neither quotation text nor attribution.
- Q-005–011 retain contextual documentary speech. Fulda is introduced with “In effect”; Tortona explicitly as paraphrase; Farfa as a loose translation. Rejection of the proposed recovered clauses means neither “by us or our successors” nor “alongside us” has been silently inserted. The existing historical issues remain documented in the dossier and rejected decisions, rather than being relabeled authenticated edition translations.
- Q-012 ends at Revelation 20:3a, before Satan's release; Q-013 supplies the interpretation outside the quotation. No unspoken continuation or new Bible translation was inserted.
- Q-014–020 retain document report versus lecturer dramatization. The creed and Advent treatments are the user's retained source renderings. Richard's profanity remains explicitly a comic gloss. No literal transcription of the unrecovered reply is claimed.
- Q-021–023 preserve their bounded scriptural clauses; Paul's interruption stays outside quotation marks. Q-024 remains a marked composite recap. Q-025 retains Augustine's main sentence and uncertainty. Q-026's rejected inference stays narration, without a new authoritative quotation claim.
- Q-027–033 retain annalist/chronicle reporting and reconstructed speech. Thiota's alleged confession stays qualified; Sigebert's imagined reasoning is not offered as a recovered continuous Latin quotation. The user-retained Godel/Trithemius treatments remain subject to their existing source limitations.
- Q-034 remains a contextual translation of an unlocated lecture quotation. Q-035 preserves its repaired syntax and keeps Barbero's explanatory gloss outside the quoted fragments. Q-036 keeps the inherited excerpt boundary. Q-037 preserves “must have,” not eyewitness certainty.
- Q-038–041 remain attributed summaries of Gouguenheim. The strong retained Q-040 formulations are framed as Barbero's summary, with the partial-reading disclaimer and the distinction between pages seen and the whole book preserved. Rejection of ED-026 is respected; their exact book wording remains unrecovered.

The existing evidence limitations remain: exact Lavallée 1844 collation and pupilhood; full Tortona terms; contemporary timing of Gerbert's magic reputation; selected generalizations about labor, authorship and sects; the Godel/Trithemius source chains; Q-034's original location; and exact severe Gouguenheim formulations. The ledger and rejected decisions also document divergences retained by user choice. None is silently repaired, newly certified, or proposed again here.

## Disposition of prior source findings and selected changes

| Prior finding | Final disposition |
|---|---|
| SF-001 | Repaired by accepted ED-032. Its exact narrower bridge is present. Rejected related qualifications remain retained with the user's recorded reasons/choices. |
| SF-002 | Refined proposed ED-014 was rejected. Its proposed preaching-right defect never entered the final. Retain the source treatment under that rejection; no renewed proposal. |
| SF-003 | Refined proposed ED-003 was rejected. Its proposed quotation/paraphrase join never entered the final. The original explicitly loose translation remains. |
| SF-004 | Refined proposed ED-017 was rejected. Retain the lecture's attribution and Renaissance frame under that choice; no renewed proposal. |
| SF-005 | Conditional on ED-009, which was rejected. Original 970 antecedent remains, so “still” is coherent and requires no repair. |
| FS-001 | Unresolved new date contradiction; exact bounded options above. |

Actual active totals are **14 accepted, 20 rejected, zero pending**. The preliminary handoff's 16/18 count was corrected before this report; no decision was changed to match the mistaken count.

Accepted IDs: ED-005, ED-006, ED-011, ED-015, ED-022, ED-023, ED-024, ED-025, ED-027, ED-028, ED-029, ED-030, ED-032, ED-033. All accepted wording is present exactly, with the empty ED-028 replacement implemented as its precise cut.

Rejected IDs: ED-001, ED-002, ED-003, ED-004, ED-007, ED-008, ED-009, ED-010, ED-012, ED-013, ED-014, ED-016, ED-017, ED-018, ED-019, ED-020, ED-021, ED-026, ED-031, ED-034. Every rejected `current_text` remains an exact substring of the final. Their rejection is the disposition of the historical/editorial choices, not evidence that each retained factual assertion has been independently confirmed.

## Checks actually run and remaining work

I used bounded `sed` reads for the full source and final; `rg -n` to locate date dependencies and active decisions; `sha256sum` for actual input hashes; and `diff -u script.draft.en.md script.en.md` for the complete selected change set. Diff exit 1 indicated the expected differences.

A read-only inline `uv run --no-sync python` check using installed PyYAML, `pathlib`, `hashlib`, `collections.Counter`, and `re` independently passed these assertions: frozen base and all five active input hashes match; all 34 targets are unique in the base and have matching target hashes; accepted intervals do not overlap; applying accepted replacements in descending immutable-base offset order exactly reproduces the final; all 20 rejected target strings survive; every comment and H1/H2 heading is unchanged; ten chapter markers, 41 distinct Q IDs and 29 distinct C IDs survive; and accepted protected-span lists are all empty. Its result was `{'reject': 20, 'accept': 14}` and final hash `95574fa23c22c0993c45981c974c8923f687f532ebd6faed39b6ca0d34585860`.

Only this report was written. The original source review, scripts, decisions and ledgers were preserved. Once the user explicitly resolves FS-001, the coordinator can record that bounded repair, reapply and verify the final, then request a targeted source recheck of CH-005's date dependencies. Subject to that repair and the coordinator's other applicable verification, this source review identifies no further work required before recording. **Current status remains blocked; no audio/performed listening assessed.**

## Targeted follow-up — authorized date reconciliation, 2026-10-02

**Current source-review recommendation: ready-for-recording. FS-001 is repaired; no unresolved source-review blocker remains.** This supersedes the pre-repair recommendation above, while retaining that audit and its hashes. It is a targeted follow-up under the same confirmed reviewer configuration, not a second full review. The report before this append had SHA-256 `cd8f4074c0448de7f2f129123beab0d19a489fbc3b559257eeb19de9197ee648`.

The user explicitly authorized exactly two date-only alignments, recorded as accepted ED-035 and ED-036. The authorized second wording differs slightly from option 1 above and was checked against the actual new decision, rather than assuming approval of the review's suggested text:

| Decision | Exact original | Exact authorized replacement |
|---|---|---|
| ED-035 | `we're in 998` | `we're around 994` |
| ED-036 | `By 998, when Abbo writes,` | `Around 994, when Abbo writes,` |

I reread all of CH-005 and its CH-004/006 joins, inspected the complete archived-final-to-current-final diff, read ED-035/036 and their decision provenance, checked the preserved historical decision records, and reran the bounded deterministic assertions. The new final differs from the reviewed pre-repair final only by those two exact replacements.

Fresh hashes calculated from actual bytes:

| Input | SHA-256 |
|---|---|
| `script.en.md` | `56a5b645814913a7ffef8b30b9c8d204df122ffe45469c3adb406829724a6cc7` |
| `decisions.yaml` | `2b1254d7db47cdd598597fc0a2fe4faabdb1e7ca1c68f434618481caf8e60c81` |
| `script.before-date-reconciliation.en.md` | `95574fa23c22c0993c45981c974c8923f687f532ebd6faed39b6ca0d34585860` |
| `script.draft.en.md` | `8e6f34e62412bc04f56ba54d6a093b257dc18c3d3a9760379f33e51e5796a173` |
| `review.source.md` | `99459d6e3be4b1fb364f36acfd495e526e66b6165dc58978db47b26b3b408f9c` |

The source, brief and three ledger hashes were independently checked against the unchanged active input manifest again and match the values recorded above. The current queue contains **36 resolved decisions: 16 accepted and 20 rejected**. The first 34 active records exactly equal the corresponding 34-record historical snapshot, including their original rejections; only ED-035/036 add newly authorized active interventions.

**FS-001 disposition: repaired by explicit user authorization.** All three statements about Abbo's writing now consistently say around 994. No exact year is substituted for that uncertainty. The singular address to Robert remains supported by the existing source review; the earlier-life episodes and the retained 970 antecedent/callback remain coherent. The creed, Advent, circulation, suppression, youth and other rejected treatments are intact. In particular, neither rejected ED-008 nor ED-010 has been applied as a whole. Their full original targets cease to match only where the user separately authorized these two date strings to change.

The read-only `uv run --no-sync python` follow-up passed: exact two-change equivalence to the archived final; immutable-base deterministic reproduction using all 36 decisions; frozen/input/target hashes; accepted-interval nonoverlap; exact preservation of the first 34 decision records in history; retained rejected wording after only the two authorized substitutions; three approximate-994 mentions and no 998 mention within CH-005; retained “We're still around 970” callback; and unchanged comments. `diff -u script.before-date-reconciliation.en.md script.en.md` showed only the two authorized lines. No quoted words changed, so the preceding complete quotation audit remains applicable.

No new source-fidelity issue was found in the repaired passages or dependencies. The preceding full narration review remains valid for the unchanged remainder. The user-retained historical treatments and documentary limitations remain explicitly recorded; they are neither reopened nor certified beyond their evidence. Final overall readiness remains subject to the coordinator's other applicable checks. No audio/performed listening was assessed, and this reviewer changed only this report.
