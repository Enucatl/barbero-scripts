# Verification — reviewed trial recording script

Status: **ready-for-recording**. Step 5 and the independent final-audience evaluation are complete. The user approved FR-004, FR-006, and FR-007 individually with literal `a`; all three exact edits have been applied and verified. FR-001, FR-002, FR-003, and FR-005 remain under existing rejected choices. The deterministic application and bounded independent follow-up passed. No required editorial decision remains. No audio listening, performed narration, recording, canonical export, preview build, or publication was performed.

Trial script: `script.en.md`. The user resolved all 41 editorial choices individually and then instructed “continue with the pipeline now that you have the decisions”. Sixteen accepted replacements were applied by root’s deterministic checker from the unchanged frozen draft. Twenty-five rejections retain their exact current passages. User approval “a” for ED-041 was saved by root on resumption after the earlier recording command omitted its write; its provenance is retained in the active queue. No material approval has been inferred from the earlier Italian transcript authorization.

## Provenance and freshness

The sole source/evidence coordinator and whole-episode writer is GPT-6 Astra at high reasoning, as configured and confirmed by root. This step-5 reread uses that continuing context; it is not an independent audience review. The separate source and listener reviewers were each assigned GPT-6 Astra/high in fresh contexts; their reports preserve their own original hashes and targeted follow-ups. The listener’s first pass read only English. Those completed reviews cover the frozen draft/proposals, not a fictitious fresh read of the applied output. Root independently reports a complete applied-output text review (lines 1–244, 245–485, 486–end); root runtime model/effort was not independently checked by this coordinator. No writer, root, or reviewer claims audio listening or a performed narration in these artifacts.

The coordinator read the complete 725-line applied English in consecutive untruncated batches 1–190, 191–370, 371–550, 551–725. Rechecked all 16 accepted Italian ranges and each relevant quotation’s original language/translation and claim research notes, then the applied passages and cross-chapter joins. Existing complete Italian/source/evidence reading remains documented in source-review and research-review; there was no unnecessary pipeline restart.

Before appending current rejection choices to the brief, preserved the exact existing resolved queue base/input/items as history snapshot 2. Snapshot 1 retains the original 39 pending proposals. Only the active brief input hash changed; proposal text, decisions, decision notes, frozen draft, final script, and evidence ledgers are unchanged. The decision package now reports actual outcomes; all exact before/after code blocks are byte-identical to their presentation version.

## Deterministic checks

Actual command, run successfully before and after the bounded brief/hash update:

```sh
uv run --no-sync python /home/user/data/barbero/editorial/020-come-pensava-un-uomo-del-medioevo-il-mercante/apply-v2.py
```

The existing output matched the deterministic application, so these coordinator runs were no-ops for the script. One intervening launch had a misspelled directory and failed before execution; the corrected command above then passed. Checks cover schema/enums, actual base/input hashes, all decisions resolved, unique accepted targets/current hashes, chapter membership, valid ranges/evidence references, disjoint accepted intervals, original quote inventory and its accepted deltas, protected quote wording/order/quotation boundaries, rejection retention, unchanged headings/coverage/research markers, and exact output equality. The checker preserves an existing differing final rather than overwriting it.

Results: **16 accepted; 25 rejected; 0 pending; 12 chapters; 801 utterances covered once in source order; 51 Q / 51 C / 19 SRC records; 43 visible output quotations; 2 newly protected recovered spans; 7,618 spoken words**. Word count removes Markdown headings and HTML comments, then splits remaining text on whitespace; it is not a timing estimate. All chapter coverage comments exactly match the assembled Italian. Previous source validation established exact approved utterance wording and provider fingerprint `5b071592a7a8d8111db7cab1ef572462cedf777eec43c8d3b0c5c1109cc341aa`; current Italian SHA remains unchanged. No raw-provider rewrite occurred.

## Accepted passages against source and evidence

| Choices | Applied result and dependency check |
|---|---|
| ED-002/003/005 | Funeral becomes narrative in the Frescobaldi square; allowance concerns citizens still in exile; battle appears early rather than literally first. Seating/status, unequal reward, and martial-honor scene remain. |
| ED-008/010/018 | Bounded Farinata, employers-association, and Italian student-protest glosses make existing allusions intelligible. No American analogy replaces them. |
| ED-019 | CH-007 consistently calls the assembly building the Baptistery. Later retained CH-011 wording is separately documented below. |
| ED-022/023/040 | Crossbow bolt lodges in a board; interdict gets a limited public-services gloss; public-council framing precedes the exact recovered speech. Silver cup, new coins, huge/small joke, lingering inspection, and refusal remain. |
| ED-026/027 | Party awards go to two sons plus a young relative, funded from poor spinners; conclusion concerns elite exploitation. Generic “on war” avoids the earlier Arezzo campaign while remaining lecturer dramatization. |
| ED-030/036 | White affiliation is explicit; recent priorate gives one year’s protection against most prosecutions, with possible moderation kept conditional. Political defeat, Dante contrast, and alliance of richest merchants with nobles remain. |
| ED-038 | Festering knee and tormenting treatment retain the graphic justice ending without asserting gangrene or one month. The omitted dog is not silently added. |
| ED-041 | Only live time-check and its following space removed; the White/Black transition now starts cleanly. No historical content or later conclusion cut. |

## Quotation integrity

`research-review.md` retains all 45 original DQ records and adds a complete exact FQ-001–043 output inventory. Forty spans survive unchanged. Five old spans are replaced/removed and three new spans occur through accepted edits. ED-023’s public-council sentence and ED-026’s spinning-wheel nickname exactly match their cited Q translations and appear in quotation marks in the applied output. The changed ED-027 accusation is contextual dramatization, not recovered historical speech. ED-002’s funeral setup is now paraphrase. Rejected recovered alternatives ED-016/024/033 were not imported. Surviving contextual renderings retain original provenance and limitations; rejecting a correction does not turn them into newly recovered authoritative wording.

## Complete text-based audience judgment

**Understandability.** The argument remains clear: noble prestige and armed kinship constrain a merchant’s world; merchant government prizes law and collective discussion but fails against factional violence; Dino turns toward imperial hope and divine justice. Recurring examples explain the institutions. Explicit accepted glosses help the modern American listener. The retained Cencelli reference and building/fiscal inconsistencies are recorded choices, not newly discovered application failures.

**Information load.** Many names and institutions appear, but Dino, nobles, popolo, and the final White/Black split provide a stable thread. Funeral seating, the murder council, beans, silver cup, and poor spinners make abstract relations concrete. The accepted third recipient in the knighthood story adds no extra name to remember. No compression quota or additional cuts are warranted by this check.

**Whole-episode rhythm.** Explanation alternates with dialogue, irony, and scenes. The kinship refusal, cardinal’s long look, seventh-office joke, sharpen-weapons reversal, and divine-justice close retain their payoffs. Removing the premature time-check improves the transition into the final substantial movement. Repetitions and professor/tax/contemporary-politics asides still carry the lecturer’s voice.

**Fluent spoken American English.** Sentences are generally natural and performable; necessary historical-present narration and retrospective/quoted tenses remain coherent. The short recovered cardinal sentence is slightly formal but framed and intelligible. Live-delivery restarts and rhetorical exaggerations deliberately retained by the source and user choices remain audible as lecture texture. This is a text-based read-aloud judgment, not an actual performed reading or listening test. No demonstrable implementation defect requires a script change.

## Explicit retained tradeoffs and evidence limits

ED-023 accepted with ED-025 rejected leaves “without public councils” followed later by “no vote is needed”; this is an informed retained distinction/broadening. ED-019 accepted with ED-031 rejected leaves the later Baptistery/cathedral switch and universal baptism claim. ED-007 rejected with ED-030/036 accepted leaves early rhetorical indifference to factions alongside later explicit White membership. The accepted paragraphs themselves are coherent and exact; none of these mixed choices licenses an unapproved repair or repeat approval request.

The user also retained the broad religion assertions and oath remorse (ED-032–035), the Cencelli allusion (ED-028), Uberti return/fifty-year account (ED-009), sack lottery/eligibility account (ED-017), nighttime constraint (ED-021), and installed-then-collapsed compromise (ED-029). All other rejected wording remains exact. These limits are editorial choices, not evidence confirmation. Deferred Q-039 remains a documented mismatch. Deferred claims C-002, C-004, C-012, C-013, C-025, C-042, C-051 retain research qualifications about business scale, Latin literacy, all-noble bishops, surnames, starvation, reason, and punitive medical narrative; accepted ED-038 narrows the medical wording without pretending every historical component is independently verified. Other resolved ledger records may resolve research by identifying a conflict, not by validating the lecturer’s wording. Edition-specific chapter numbering remains tied to its source. The interdict gloss has general retrospective medieval support, not a retrieved Florence decree.

## Every review-finding outcome


All findings have an outcome; rejected editorial improvements are retained by explicit user choice, not left unanswered. No repeat approval is requested.

| Finding | Applied outcome / retained choice |
|---|---|
| LR-001 | Repaired before decisions: commune lexical explanation remains. |
| LR-002 | ED-010 accepted: Confindustria gloss applied. |
| LR-003 | Repaired before decisions: physical-handling interruption removed. |
| LR-004 | Repaired before decisions: Arezzo false start resolved; ED-013 rejected, so starvation remains. |
| LR-005 | ED-018 accepted: 1968/1977 student-protest orientation applied. |
| LR-006 | ED-019 accepted; ED-031 rejected. CH-007 Baptistery fixed; CH-011 cathedral/universal claim consciously retained. |
| LR-007 | ED-040 accepted: bounded interdict gloss applied. |
| LR-008 | ED-023 accepted; ED-025 rejected. Public-councils source speech applied; later no-vote callback retained by choice. |
| LR-009 | ED-028 rejected: Cencelli allusion remains unexplained. |
| LR-010 | ED-041 accepted: time-check removed; faction transition preserved. |
| LR-011 | ED-032/034/035 rejected: sweeping religion opening and argument retained. |
| LR-012 | ED-014 rejected: original broad legal account retained; revised proposal terminology is not in output. |
| LR-013 | ED-020 rejected: original bean scene retained. |
| LR-014 | ED-039 rejected: original bishop negotiation/murder motivation retained. |
| LR-015 | ED-027 accepted: generic “on war” accusation applied. |
| SR-001 | ED-036 accepted: one year’s protection against most prosecutions applied; blood-crime exception documented in evidence. |
| SR-002 | ED-026 accepted including extended conclusion: Party honors/poor spinners and exploitation takeaway applied. |
| SR-003 | ED-031 rejected: universal baptism/cathedral wording retained. |


Accepted IDs: ED-002, ED-003, ED-005, ED-008, ED-010, ED-018, ED-019, ED-022, ED-023, ED-026, ED-027, ED-030, ED-036, ED-038, ED-040, ED-041.

Rejected IDs: ED-001, ED-004, ED-006, ED-007, ED-009, ED-011, ED-012, ED-013, ED-014, ED-015, ED-016, ED-017, ED-020, ED-021, ED-024, ED-025, ED-028, ED-029, ED-031, ED-032, ED-033, ED-034, ED-035, ED-037, ED-039.

## Step-5 artifact hashes — historical provenance

- `../episode.yaml`: `34af042e39b867f8ba36ec0acf313152ca162b0c15cc7377680dbcf605e1fe6d`
- `../transcript.it.md`: `b0eb338b676cf8a61d4c0c3bdd562df362835e6c033ff72107271e025876c44b`
- `../transcript-uncertainties.yaml`: `6db00bf3f582fb9d67b5ee98f20ed9fdbb2e73396418ca53b10b564b89b5fc40`
- `../chapters.yaml`: `24e8bbd7b24bfc9979a46230b040295fd68c7a9a56ebb2edc30250fcdaa4e59e`
- `../script.it.md`: `2f2e1fd40f59f134eb62eb19c60b2c1cf9f2473ce658b50e5e8a6bc0e6ca7bc5`
- `brief.md`: `322250796a8258e64539feb3098010e9ac455f277a120efbd7efbe0815323bf2`
- `source-review.md`: `47a40fa717231ce3e6dd42d68616458564333014e389ab5b38dd2024921a6038`
- `quotes.yaml`: `4cc4261073d30e049c8695509f77386fb2375fd9466f21b88b8f2740db9a7d51`
- `claims.yaml`: `50a7396a3ef110558e13602331c30f1560b1dca0b55c3e0e6cc8d8f2e44a6bd6`
- `sources.yaml`: `4097eb2a852d1a4a6131b0577a01eb33fa2ab35234f87390cb57bb87bc9dcd1f`
- `research/quotations.md`: `45b166c6fb77858b48a08395fedcccb02cbb01380a74c3250fc196098ad5f975`
- `research/claims.md`: `2ac3ab98aeec0a9fdfadae8bc8a2c9956b0661d67879bf257947f85831190fd1`
- `script.draft.en.md`: `1a151fa40cef11f5402df880ca0e7ef56edb0f76bc76ec6119a90e4cd6dfae1e`
- `decisions.yaml`: `379f6ef03a60d23ba7295bd0ebb9c2803229f9611b7563e2640cccda93598678`
- `decision-package.md`: `7ee3f5c0ba072765215e9d6c5135274c7f0741ec05591d9def1e537c816fb9f4`
- `review.source.md`: `ab80da011d479c475005e4493e60a8e58bb27c5934c027838434c56c28aa7d87`
- `review.listener.md`: `c7970424f9aab46aaf39937f1744198b6953298db1a9da2203d05f5a513a3b9b`
- `research-review.md`: `a1212b1ca104df59e750dc662173c3b774c41b383ec6be69a5c842d84be7c5ae`
- `script.en.md`: `8c1b1ece45b0e6fc2d9eaeb8b4b0514f82eb77c1bb2b180b57455bbe919e3647`

External deterministic checker SHA-256: `fb8c84cae43845f2e8d17a000bbcb965171914fe609b78e68e0436e6d0a6a705`.

Historical step-6 handoff before the audience review: freeze this exact applied script for a fresh English-only first read. Provide the source/evidence/decisions only after that initial assessment, preserve the existing explicit rejections, and handle any actual new findings through the skill’s bounded decision/reapplication process. Recording readiness remains ungranted until that stage and required follow-up are complete.

## Step 6 — independent audience review completed

Completed review SHA256: `6b9f22685d7238d82552c86f48f65ae8369f08e470d9e8e0f606445f1e17af8e` (before user directions).

A fresh GPT-6 Astra/high reviewer read the complete applied English and compiled final-audience prompt first, saved its independent first impression, then read the Italian source, relevant local evidence, and all 41 active decisions. Earlier reviews, brief, verification, and writer explanations remained withheld. Root read the complete report and reconciliation. The reviewer recommends retaining the episode and its detail; no general compression or episode omission is warranted. Its separate bounded check found all 41 decision outcomes correctly applied. No implementation defect was found.

FR-004, FR-006, and FR-007 were each approved under the user’s literal `a` and are now implemented exactly. No final-review finding remains Pending. FR-001 maps to rejected ED-032/035; FR-002 to rejected ED-028; FR-003 to rejected ED-006; FR-005 to rejected ED-031. The English-only provisional labels remain as historical first-impression evidence; the report's reconciliation dispositions govern. Before the approved final-review edits, root confirmed the reviewed script SHA256 `8c1b1ece45b0e6fc2d9eaeb8b4b0514f82eb77c1bb2b180b57455bbe919e3647`; the resulting version is recorded below. The user supplied all three required directions through the established one-at-a-time review. `changes.final.md` now records the exact implementation and outcome. No audio listening or performed narration was assessed.

## Final application and recording readiness

The unchanged source/evidence and prior full reviews are reused. Root checked the actual diff and changed passages, not a repeated whole-episode audit. History snapshot 3 preserves the prior queue/base/input values, original 41 records, reviewed script, and exact routine FR-007 opening repair. The new frozen draft differs from the old draft only by FR-007; ED-042 and ED-043 are the separately approved FR-004 and FR-006 cuts. Original 41 active records remain identical. The queue has **43 fully resolved material choices: 18 accepted, 25 rejected, 0 pending**; the routine opening repair is additional, not counted as a material choice.

Actual command:

```sh
uv run --no-sync python /home/user/data/barbero/editorial/020-come-pensava-un-uomo-del-medioevo-il-mercante/apply-v2.py
```

Passed actual base/input hashes; schema and evidence IDs; unique target hashes, chapter membership, valid source ranges and disjoint accepted intervals; exact original-choice preservation; complete quotation inventory, protected spans and rejected-passage retention; exact deterministic output. The expected output is also independently constrained to the preserved reviewed script with exactly the three approved final-review replacements. The actual unified diff has three replacement hunks and no other change. Headings, 12 chapter/coverage ranges, 801 ordered source utterances, and research markers remain unchanged. The output has **43 visible quotations, 2 protected recovered spans, and 7,585 spoken words** (headings/comments excluded), 33 fewer than the reviewed version. The source title and canonical episode files are preserved.

Root inspected each changed passage with its adjacent paragraphs and relevant Italian utterances: opening U-00001–00003, Ordinances U-00377–00379, taxation U-00534–00539. Each change follows the user’s exact wording. Giano’s sentence and the applause joke are deliberate approved losses; the opening is a presentation adaptation. No historical assertion, recovered quotation, legal explanation, later callback, or previously rejected interpretation changes.

The independent GPT-6 Astra/high final reviewer’s bounded follow-up passed on the implemented version: all three exact replacements match; the Ordinances join, tax/public-money transition, Dino introduction, and later merchant/politician reconsideration remain natural and understandable. The reviewer assessed only the changed passages and surrounding source/context, found no defect, and reopened no rejected choice. This does not replace or mislabel the preserved independent full-episode assessment. All seven final-review findings now have effective outcomes: FR-004/006/007 implemented; FR-001/002/003/005 retained by prior choice. Every required instruction is resolved.

Existing research deferrals and consciously retained tradeoffs remain as documented above. No audio listening or performed narration was assessed. Text-workflow status: **ready-for-recording**. The remaining production task is recording; no publication or canonical integration is authorized by this status.

### Resulting versions

- `script.draft.en.md` SHA256: `ff94ee9e5bf8a9eba3746218ab5747bcdc2a4545eefc2f68a9d72b855ad14ae0`.
- `decisions.yaml` SHA256: `eb2d8d32fc6c542031bbbe4dc16d9be57b8a0058f9cf15dccb126f27e0eaaddc`.
- `script.en.md` SHA256: `f06bbd26e453e944a2d4923ad4b513eb664350fea1f137dfadc3e4c86feff8a2`.
- `review.final.md` SHA256: `f128d69cc87568066853c0cb6052b8188ed6b4e9d39288ccd1240decd83cfffe`.
- `changes.final.md` SHA256: `d4f38da478fbba10359506051f016fe4c233af7d18929e1dbc542ea84a568a3a`.
- `decision-package.md` SHA256: `39ae089ca2bf1da7ad049e1ccd91fac6e44a18698072f1113f199bc515501a10`.
- External application checker SHA256: `a9d10a8627ae51a80f47b064a21033499a72e8481ea61fbe7342021bcd9c77ae`.
