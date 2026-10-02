# Episode 019 — final verification

## Current American audience revision — 2026-10-02

Status: **ready-for-recording after the authorized audience revision**. The current `script.en.md` contains **12 English chapters and 7,315 spoken words**, excluding headings and comments. SHA-256: `9df48ed172470ab072452cee751829b277493cd4e4911e9bfc0a00f65a750ac1`.

The user subsequently authorized removal of conference framing, time warnings, regional insults and pronouns, Boccaccio and Montanari references, and Italian-audience assumptions; a three-episode trilogy introduction and broader fluency/transition polish were requested. The user also requested a before-and-after report with reasons, then specifically requested preserving the royal-money joke by explaining Salimbene's lack of concern about extra French taxes for the crusade. That final wording was read in context and checked after the independent review. See [the complete revision report](american-audience-edit-report.md) for every edited passage, rationale, and verification scope.

The current script is the earlier seven-decision result **plus this later authorized editorial pass**. It is no longer described by deterministic application of the original queue alone. Earlier decisions, hashes, reviews, and the frozen draft below remain historical records; the new instruction supersedes the affected retention decisions. The Italian source and source ledgers remain intact.

Checks passed: complete diff review; independent whole-script editorial read followed by the suggested local repairs; removal search; consecutive English headings; exact surviving chapter/evidence mapping comparison; exact protected Q-079 quotation; preserved recipe uncertainty; unchanged frozen draft; word count and final hash. CH-011 / U-00740–U-00769 is deliberately omitted, along with C-028–C-029 and Q-067–Q-070. The later user-approved slogan/Eco cut removes C-015 and Q-025; five approved vocabulary substitutions simplify alms/mendicants, habit, and commends. Those bounded follow-up edits received passage and transition checks, updated marker/count/hash checks, and a protected-quotation check after the earlier independent review. The final has 31 claim and 74 quotation markers. Surviving source chapter IDs remain unchanged despite renumbered English headings. No audio review or renewed historical fact-check is claimed. Existing evidence qualifications still apply.

## Earlier verification checkpoint — superseded for the current script

Status: **ready-for-recording**.

Deliverable: `script.en.md`, episode 019 **Il frate / The Friar**. The final contains 13 chapters and 8,398 spoken whitespace words, excluding Markdown headings and HTML comments. All 19 user choices are resolved: seven accepted, twelve rejected, zero pending. The final exactly equals deterministic application of the accepted replacements to the reviewed frozen draft.

## Decisions actually applied

Accepted: **ED-006, ED-009, ED-012, ED-013, ED-014, ED-017, ED-019**. These revise the Pisa dream, age description, exact humane quotation, first Franciscan/Dominican explanations, Montanari's role and royal visit. ED-019 includes the Mantua cut.

Rejected: **ED-001–005, ED-007–008, ED-010–011, ED-015–016, ED-018**. The user selected ED-019 instead of ED-008; only that one royal replacement was applied. Every other rejected current target survives unchanged. No adaptation introduction or additional infant-story qualification was inserted. The recorded ED-015 choice preserves the lecture greeting. Decisions and their user provenance are in decisions.yaml and brief.md; no recommendation was treated as permission.

## Actual verification and commands

The established source audit is reused: all 379 transcript uncertainties resolved against 825 rendered utterances, ordered chapter coverage once, exact assembled Italian after whitespace normalization, and no remaining review flags. The authoritative source and source decisions have not changed. The approximate birth range, spoken Latin and end-at-Grazie decision are preserved. No new whole-source audit was needed.

Root ran short `uv run python - <<'PY'` application/check commands using pathlib, hashlib, re, json and repository PyYAML. They verified required fields/enums and unique active IDs, all resolved decisions/provenance, actual active base/input hashes, exact accepted target hashes and unique matches, chapter membership, valid evidence references, preserved headings/comments/markers, and nonoverlapping accepted offsets. Rejected ED-008 overlaps accepted ED-019 by design and contributes no patch. Three history snapshots preserve superseded queues; the third records the complete user choices before adding their record to the brief and refreshing its documentation hash.

Accepted replacements were applied to the immutable base in descending original-offset order. A separate ascending-parts reconstruction matched the resulting text before writing. A differing existing final would have been preserved for investigation. Written final bytes matched the expected result. Result: **PASS — seven accepted replacements, twelve rejections, zero pending, 13 chapters, 79 quotation markers, 34 claim markers, one authoritative English span, 8,398 spoken words.** Final SHA-256: `1328a4915cad2fffe1b3ba61576589b1610f1dfd9d274bd2afb7cbcfbdd4ebf2`.

Root inspected the actual before/after diff with `git diff --no-index -- episodes/019-il-frate/editorial-v2/script.draft.en.md episodes/019-il-frate/editorial-v2/script.en.md`; exit1 indicates the seven intended changes. Surrounding CH-006/007/013 passages and user-preserved wording were checked. A final short Python check verified all accepted replacement texts survive, all rejected targets survive except the intentional ED-008 alternative, current hashes match, and both final review records identify the actual final file.

The source reviewer independently reconstructed the seven accepted offset patches and matched the final bytes. Its bounded applied-passage check passed the dream/consolation distinction, royal arrival/donor/speaker/tears/menu/callback, age/birth-range relation, ravioli uncertainty, role explanations and Q-079 quotation/commentary join. See review.source.md, final follow-up.

## Quotations and structural results

All 13 coverage comments equal the Italian comments. Headings, all chapter/research comments and the ordered 79 Q/34 C marker inventory equal the draft. No research marker was reassigned or omitted. The source title remains Il frate; the trial's faithful English title remains The Friar.

ED-012 / Q-079 is the sole authoritative English source quotation introduced in the final. Its exact protected wording matches the cited ledger translation, occurs once wholly within quotation marks, and ends before the separate cradle-song sentence. The source reviewer previously inspected the MGH Latin scan and now checked the applied boundary and narrative join. The final surviving authoritative inventory is recorded in research-review.md. Other English quoted passages remain contextual lecture renderings. The user-confirmed Latin remains an inherited transcript quotation, not a claim of critical-edition wording.

## Reviews and finding dispositions

The writer/evidence coordinator and two original independent reviewers used **GPT-6 Astra / high**. The original source and listener reviews used fresh contexts; the listener's blind English first read preceded source/evidence reconciliation. Reviewers did not read each other's reports. Their original hashes remain historical provenance. Bounded follow-ups reused the existing reviewers; the final narration read reused the coordinator and is not labeled a new independent review.

All SR-001–003 and LR-001–013 findings have final dispositions in decision-package.md. The six routine repairs remain checked and intact. Source/proposal defects are corrected; optional changes have their explicit accept/reject records. Repeated closing cues and the rarely-judges opinion are retained with reasons. No open routine or unresolved editorial finding remains.

The coordinator read the complete applied narration once from beginning to end, all 13 chapters, and recorded **pass** for understandability, information load, whole-episode rhythm and spoken American English. Scene order, returning people, thematic joins, quotation/commentary boundaries, comic timing and the humanity conclusion remain coherent. No additional repair was identified. See final-narration-review.md for chapter-by-chapter results and the four audience judgments.

## Evidence qualifications and scope

Ready-for-recording describes a verified adaptation of the user's choices. The user consciously retained paper chronology, death/announcement phrasing, weaver/physician description, letter-condition attribution, atheist label and the Sens comparison; these are not certified as corrected historical facts. The added 2011 presentation frame and Boccaccio gloss were rejected. Lecture-era references remain implicit; the source's repeated closings and broad judgment are retained audience tradeoffs.

The infant story remains attributed to Salimbene in its introduction. Recovering the humane quotation does not verify occurrence; the user rejected extra uncertainty and closing-attribution wording. That qualification and other primary-recovery gaps remain in the dossier. No unsupported originals, recipes or explanations were invented to remove deferrals.

No audio or performed listening was assessed by the agents. This final review is a text rehearsal. The user's three listening decisions concern source clips at /scratch/audio_clip/barbero-019/ and are recorded in the brief. The editorial v2 workflow is complete; recording is the next production step. Publication and canonical-workflow integration require a separate request.

## Input and output hashes

Paths are relative to editorial-v2. Unchanged source/discovery hashes are retained from the established checkpoint; changed editorial files and the final were hashed from actual current bytes. Historical input hashes remain in the reviews and queue history.

| File | SHA-256 |
|---|---|
| ../episode.yaml | `b51c5170e9979c7fe3b8358e5ee58ca12ef4a2e15498b3464981b8e5635e17dd` |
| ../transcript.it.md | `acbf509845350d8103145734fb2ed91749152a60c45118a61e0025868120fc92` |
| ../transcript-uncertainties.yaml | `ac0c241730b223737284986f74138b4257eb031c76ddbc8122f2276bd27796eb` |
| ../chapters.yaml | `17c88eba1840ce9bff37724ca87a1551de880bdc770b9263c6303305b6bb1bbf` |
| ../script.it.md | `a6f9fa952c5f80354e45aca418b6c99dedc0513506f17e0baa7bf58701247c98` |
| source-review.md | `391f66779c0a28a4dcd829dffbfb2e9584c2604314626c273523dcfbadad56e7` |
| brief.md | `6a870423f815db9c013d4a3cfdc3b73698d98418e919e67a3db343a8401247ae` |
| quotes.yaml | `ec2a095cb430ae608b9265f2ae1784fd876472480a79efdbdd6053b8e69275d0` |
| claims.yaml | `3fc0a6fc1a3a957398bd571a6b5d859a601cd5af7314dc242995a1783e276ae1` |
| sources.yaml | `380909ffca102aa0cea0b5b00ba34745892e7deb7bb958ea8180db1d46f4d3a9` |
| research-discovery.md | `805e41f1cbb1b5558f5afdabab56f8254437b0140b5c2a4b73213f36c8cd78ad` |
| research-latin-supplement.md | `8eddba5ac4583bdfa284675348ad89913aa4b5f56328010e660bbb1586bd54fc` |
| research-review.md | `e69dbdc07673b12ded56a8af536e27e8c51fbe3e5f99650da11fa49a3ca15ed2` |
| script.draft.en.md | `f5ebf4ba73ec46e2c148e74d67767b12835ec4bbfc39583cc1fe3757b5d5a1fe` |
| decisions.yaml | `8d9e14129bc311af3a65cdd41395a4196dc33c1bbed58c40eb6a713bcd13d323` |
| decision-package.md | `1befd2edf9433cd4e4411a94eac2e49535454c9a2beffbc9727ca3f71fa07c79` |
| review.source.md | `8231b4b561cbab8a9e52f1727e048843f91e86440fe1ad846b56c80ab00ff280` |
| review.listener.md | `3ebc5d2450372a12d6e32b1e9e2892c2e58cb707994c9bd4e6133adb491ad4b6` |
| script.en.md | `1328a4915cad2fffe1b3ba61576589b1610f1dfd9d274bd2afb7cbcfbdd4ebf2` |
| final-narration-review.md | `f6004c35d7e00b2cb153c8876f5790c5124aa9a552865a8b9160656e02fd58a5` |
