# Episode 013 — final editorial verification

Status: **ready-for-recording**. Completed 2026-10-02.

Deliverable: [script.en.md](script.en.md), **6,896 spoken English words**, ten chapters.
The final SHA-256 is `56a5b645814913a7ffef8b30b9c8d204df122ffe45469c3adb406829724a6cc7`.
This is the v2 trial recording script. The original Italian title, episode metadata,
frozen draft and research ledgers are preserved. The existing CLI does not recognize
these trial editorial artifacts; this status is the editorial skill's completion status.

## Decisions and exact application

All **36 active decisions are resolved: 16 accepted, 20 rejected**. The original
34 individually resolved records survive unchanged in the second history snapshot.
The first history snapshot retains the earlier 29-item pending package. Historical
records are provenance, not active patches.

Accepted: ED-005, ED-006, ED-011, ED-015, ED-022, ED-023, ED-024, ED-025, ED-027,
ED-028, ED-029, ED-030, ED-032, ED-033, ED-035, ED-036.

Rejected: ED-001, ED-002, ED-003, ED-004, ED-007, ED-008, ED-009, ED-010, ED-012,
ED-013, ED-014, ED-016, ED-017, ED-018, ED-019, ED-020, ED-021, ED-026, ED-031,
ED-034.

The original accepted changes identify Carducci, introduce Revelation's actual excerpt,
correct Abbo's introduction and Augustine's priority wording, qualify Sigebert's
personal belief, frame the national-origin account as the early historians' perspective,
repair Gouguenheim's identity framing and book chronology, state his disputed Aristotle
thesis, and remove the paired Odifreddi live jokes. Rejected proposals contribute no patch.

The final mixed selection introduced one new continuity problem: ED-006's around-994
composition date conflicted with retained 998 callbacks in ED-008/010. Both fresh final
reviewers found it. The user then explicitly selected “Align only the two callbacks to
around 994 (Recommended)” after seeing these exact replacements:

| Decision | Frozen text | Approved replacement |
|---|---|---|
| ED-035 | `we're in 998` | `we're around 994` |
| ED-036 | `By 998, when Abbo writes,` | `Around 994, when Abbo writes,` |

These are separately recorded approvals. Every other part of rejected ED-008/010 stays
intact. The preceding final is preserved as `script.before-date-reconciliation.en.md`.
The final differs from that archive only in the two approved date strings. All patches
were applied by descending original offsets to the immutable frozen draft; no LLM
regenerated or directly rewrote the final narration.

## Checks actually completed

The saved [verify.py](verify.py) uses the standard library and the installed PyYAML.
Its runnable assertions check:

- Frozen draft and all active input hashes; matching reviewed source, metadata, chapter
  and transcript hashes; all source uncertainties resolved and their unchanged fingerprint
  and file hash matching the brief. This continuation reuses the earlier provider-source
  review rather than claiming a new acoustic review.
- Required decision fields and enums, unique IDs, decision provenance, accepted target
  hashes and unique locations, chapter membership, valid evidence references, and
  nonoverlapping accepted intervals. Rejected targets may overlap the two separately
  approved date repairs; they are not applied.
- Exact ordered coverage of all **907 transcript utterances** by **ten sequential chapters**;
  the Italian script's words and punctuation exactly matching the settled transcript
  after whitespace normalization.
- All chapter headings, coverage comments and research comments preserved, with exactly
  **41 Q markers and 29 C markers**. The independent source reviewer additionally checked
  the H1 and all selected change boundaries.
- All **16 current contextual quotation-inventory spans** surviving exactly. There are
  **zero newly accepted authoritative quotation substitutions**: ED-003 and ED-007 were
  rejected. Their proposed protected spans are excluded from the final inventory.
  Quotation/commentary boundaries and excerpt omissions were also read semantically by
  the source reviewer; substring checks alone are not the source review.
- The generated final exactly equaling the accepted immutable-base patch result. An
  existing identical final is a no-op; a differing final causes a failure, preserving it.
- The three Abbo composition references agreeing on around 994, without changing the
  unrelated 998 in the annalists' example. Spoken word count excludes headings/comments.

Actual commands, all successful:

```sh
uv run --no-sync ruff format episodes/013-la-paura-dell-anno-mille/editorial-v2/verify.py
uv run --no-sync ruff check episodes/013-la-paura-dell-anno-mille/editorial-v2/verify.py
uv run --no-sync python episodes/013-la-paura-dell-anno-mille/editorial-v2/verify.py
```

The final verification command's output and exit code are saved in
[verification-checks.txt](verification-checks.txt). The reviewers also independently
checked actual file hashes, the full change set and the targeted date-only diff.
The artifact's runnable assertions serve as its scope-specific check; the production
pipeline was not changed or subjected to unrelated test runs in this continuation.

## Editorial reviews and finding dispositions

The original fresh source and listener reviews, including their repaired-draft follow-ups,
retain their original reports and input hashes. Two new independent Astra contexts read
the complete final narration and their respective original review; neither received
the other review or the writer's self-assessment. Their initial audits are preserved
alongside targeted follow-ups for the two approved date changes:

- [final-review.source.md](final-review.source.md): ready-for-recording; no unresolved
  source-review blocker. Full Italian/final comparison, selected decision/evidence and
  quotation review; subsequent reread of chapter 5 and its joins.
- [final-review.listener.md](final-review.listener.md): ready-for-recording; no remaining
  listener work. Complete narration text review; subsequent reread of chapter 5 and
  its transition into chapter 6.

The coordinator also read the complete final narration before the date-only repairs
and checked the repaired composition references. Chapters, historical scene transitions,
royal referents, Richard's dialogue and 970 antecedent, book chronology, paired joke
removal, quotation joins, and the authorized series-finale opening/farewell remain coherent.

| Finding | Final disposition |
|---|---|
| SF-001 | Repaired by accepted ED-032's future-planning bridge. |
| SF-002 | Proposed ED-014 wording was refined before presentation, then rejected. Its proposed defect never entered the final; source treatment retained by explicit choice. |
| SF-003 | Proposed ED-003 quotation introduction was repaired before presentation, then rejected. The final retains its explicitly loose contextual translation. |
| SF-004 | Proposed ED-017 transition was repaired before presentation, then rejected. The lecture's attribution/frame is retained by explicit choice. |
| SF-005 | Conditional repair not triggered: ED-009 rejected, leaving the 970 antecedent and “still” coherent. |
| LI-001 | Repaired by accepted ED-030's first-use poet identification. |
| LI-002 | Repaired in the frozen draft; ominous signs/omens survive the selected changes. |
| LI-003 | Repaired in the frozen draft by naming King Robert; original pluralization withdrawn. The dual dedication and singular address remain coherent. |
| LI-004 | Conditional repair not triggered by rejected ED-009; original temporal antecedent retained. |
| LI-005 | ED-031 rejected, retaining the particular inference; accepted ED-032 repairs the general bridge. |
| LI-006 | Repaired by accepted ED-033's historians' viewpoint framing. |
| LI-007 | Retained with the recorded source-texture reason; no renewed cut or invented gloss. |
| LI-008 | Repaired in the frozen draft: Q-035 syntax and quotation/gloss separation; inventory matches. |
| LI-009 | Repaired in the frozen draft: pope and Pope Pius IX referents. |
| LI-010 | Retained by explicit rejection of ED-034; opening definition/reporting context remains. |
| FS-001 / FLI-001 | Repaired by separately accepted ED-035/036, then independently rechecked by both final reviewers. |

## Evidence qualifications and remaining work

Readiness reflects the reviewed, explicitly selected adaptation. Rejections do not establish
that the retained assertions are historically verified. The source report and ledgers preserve
the research qualifications: full Tortona lease terms, the exact 1844 Lavallée witness and
pupilhood, Bettinelli's unrecovered first excerpt and first-edition dating, Godel/Trithemius
source transmission, and the severe Gouguenheim paraphrase remain bounded by their documented
access limits. The user retained the rejected Fulda/Farfa, creed/Advent, prediction-spread,
Thiota, attribution, priority and closing-scope treatments. No new certainty is claimed.

No editorial blocker remains. Recording and a performed-audio assessment remain to be done.
No audio or performed listening was assessed in the source, writer, or reviewer stages.
No commit, push, publication, canonical-script replacement or preview build was performed.
Publication would require separately requested recording and integration with the legacy
pipeline; this script is the completed v2 editorial deliverable.

## Model-by-step report

This table distinguishes recorded authorship/configuration from actual execution telemetry.
The fresh reviewers were explicitly launched with `model: gpt-6-astra`,
`reasoning_effort: high`, and `fork_turns: none`. Earlier reviewer reports record the same
requested configuration; they expressly do not claim independently measured runtime telemetry.

| Step | Model or tool | Evidence and scope |
|---|---|---|
| Italian speech transcription | **Deepgram nova-3**, Italian | Actual transcription-manifest options. This is a speech recognizer, not an editorial LLM; reused in this continuation. |
| Initial contextual Italian/source-uncertainty review and source settlement | **Exact LLM not recorded** | `source-review.md` records the full contextual review, user acceptance and deterministic source checks, but no model identity. Do not infer one from the skill defaults. |
| Medieval-document research | **Exact investigator LLM not recorded** | `investigation.medieval.md` records its assignment, retrievals and limitations, but no model identity. The skill prescribed Astra/high; execution is not individually attested in that report. |
| Historiographical research | **Exact investigator LLM not recorded** | `investigation.historiography.md` has the same model-provenance limit. |
| Whole-source reading, chapter brief, evidence synthesis and ledger ownership | **gpt-6-astra, high reasoning** | Recorded writer/evidence-owner configuration in `brief.md` and `research-review.md`. |
| Entire English adaptation | **gpt-6-astra, high reasoning**, one writer | Recorded in the brief and evidence audit; one coherent draft, without separate chapter writers. |
| Original independent source review and repaired-draft follow-up | **gpt-6-astra, high reasoning** | `review.source.md`: requested configuration, initially fresh context, then the same reviewer for its bounded follow-up. |
| Original independent listener review and repaired-draft follow-up | **gpt-6-astra, high reasoning** | `review.listener.md`: equivalent configuration and independence record. |
| Editorial language repairs, revised proposals and evidence follow-up | **gpt-6-astra, high reasoning** for the writer/evidence follow-up; **Sol** recorded as coordinator | `research-review.md` follow-up records Astra/high; `brief.md` names Sol without an exact variant/effort. |
| Individual substantive editorial decisions | **User**, not an LLM | All original 34 choices and the two exact date-only follow-up approvals are recorded in `decisions.yaml`. Recommendations are not approvals. |
| Final independent source review and date-only recheck | **gpt-6-astra, high reasoning** | Explicit fresh reviewer launched in this continuation; owns only `final-review.source.md`. |
| Final independent listener review and date-only recheck | **gpt-6-astra, high reasoning** | Separate explicit fresh reviewer launched in this continuation; owns only `final-review.listener.md`. |
| This continuation's coordination, verification command and report | **Main Codex agent, GPT-6 family; exact variant/effort not exposed** | No more specific current host identity is available in the supplied session metadata. |
| Applying decisions, comparing source words, validating structure and computing hashes | **Python/PyYAML; no LLM narration regeneration** | Reproducible `verify.py` plus independent reviewers' read-only deterministic checks. |

## Actual file hashes

Paths below are relative to the trial directory. Hashes identify the final reviewed inputs
and outputs; earlier hashes inside retained reports refer to their stated historical snapshots.

| File | SHA-256 |
|---|---|
| `../episode.yaml` | `5135c3e3260e8b327deb09961776ac39cfb878201738d687345b68ab51ef4c06` |
| `../transcript.it.md` | `f17641ad0a1f0c7b400b6d34098bda2a6628dc6db079deb880a1d26271d73e73` |
| `../script.it.md` | `40d4433f29e3d0da07235e91730b9ba487954ec6d39fd53e0ff19f21ec209bb9` |
| `../chapters.yaml` | `e6b5821f83b5fafd7e2c1804ed0aeb3412c6271eb7437bb127add83e1648efdd` |
| `../transcript-uncertainties.yaml` | `c95fd0007c659a64cd01c80c2651f5e67cccb6c5ba392a4ae4aa99457c868f94` |
| `source-review.md` | `fe8ecb184ec1b83fc4c227e0bd79f9b2e44b6c22dde737f1215f36db1e12490f` |
| `brief.md` | `e70bdfbfbed1f900320efac6a08846827d9efb00d35d3a3efcc4bb5aee986251` |
| `investigation.medieval.md` | `59709543f2519cf68f9163604d19ca05e477b31ec97d993a05f6aa511442432e` |
| `investigation.historiography.md` | `22d6676c8867ea721d92e7314a1a6efa1b9789df1c8761521a00d0701c5c2515` |
| `quotes.yaml` | `88d14227ff6d18c54332ba0ca7b018e87842b21f3b7f415a2098692d12dd6971` |
| `claims.yaml` | `83b041304eeea35bbb8bb1a7f01d95738efde42b0da403dab2561c5868654f33` |
| `sources.yaml` | `75ad7e709fdfdbd27df6024a5a1f36f49de2254edfe392895a655be462829759` |
| `research-review.md` | `cf993f42ea3c238d012b62d0a861adcb76411b2c2cc5cbca06bc84c68b54513e` |
| `script.draft.en.md` | `8e6f34e62412bc04f56ba54d6a093b257dc18c3d3a9760379f33e51e5796a173` |
| `decisions.yaml` | `2b1254d7db47cdd598597fc0a2fe4faabdb1e7ca1c68f434618481caf8e60c81` |
| `decision-package.md` | `1bb755501f15b0d0d73c05d94f5e497a48a099950ac5d9dca766c0db165a45d8` |
| `review.source.md` | `99459d6e3be4b1fb364f36acfd495e526e66b6165dc58978db47b26b3b408f9c` |
| `review.listener.md` | `ee179d383ba77eb5da7f0b79d11c1efdab0e31c214fd4742d6ef484eb8423417` |
| `final-review.source.md` | `970334aae6c2714fcc514afa642d7a7654162b52f225f88d2d13734255436742` |
| `final-review.listener.md` | `16d10f7be83a9bf24c84f431511e5bae708a394e83d542345ba4496e300c804a` |
| `script.before-date-reconciliation.en.md` | `95574fa23c22c0993c45981c974c8923f687f532ebd6faed39b6ca0d34585860` |
| `script.en.md` | `56a5b645814913a7ffef8b30b9c8d204df122ffe45469c3adb406829724a6cc7` |
| `verify.py` | `2980ce789ebda81d270f932360b81260e7092ee5e0a805ae7d4ac48fa98348f4` |
| `verification-checks.txt` | `edd14fc7e18c28bacc55ebdab26f1ed281c3c50a067d2ae734d15823a0bcb5fc` |
