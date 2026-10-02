# Episode 013 — audience revision verification

Status: **ready-for-recording for the authorized revision**. Completed 2026-10-02.

Deliverable: [script.en.md](script.en.md), **6,096 spoken words**, ten chapters. The previous version had 6,896 words: the revision removes 800 words (11.6%). [The full revision report](decision-package.md) records all 46 before/after changes, their issue numbers, and reasons. Issue 5 is now approved and applied; its closing disclaimer is removed at the user’s explicit instruction.

## Applied scope

- Issues 1–4 and 6: remove repeated closing announcements and the complete Aristotle/Greek/Arabic controversy; introduce the topic without underselling it; remove the sharecropping comparison and simplify the national-literature passage; remove the Protestant/Italy comparison while keeping the permitted tentative Texas reference; smooth narration into spoken American English.
- 29 routine language changes are incorporated into the refreshed frozen draft. 17 editorial changes are recorded as accepted ED-037–053 and applied deterministically. The user's explicit revision instructions authorize these changes; no extra approval round was needed.
- The preceding 36 decisions remain in queue history. Earlier rejected factual corrections remain retained, except that the user now authorized removing the complete Aristotle passage. The three issue-5 edits are applied as ED-051–053; the closing edit removes the disclaimer rather than reinterpreting its referent.
- All ten chapter headings and nonspoken provenance comments are preserved. Comments for removed narration remain as source references; they do not assert that every source passage is still narrated. Historical quotation wording is unchanged.

## Editorial review

A single fresh writer and two independent reviewers were launched with **gpt-6-astra, high reasoning**. The listener reviewer first read only the English and an American audience definition, recorded that impression, and then consulted the Italian, evidence, and decisions. Neither reviewer received the other's report or the writer's self-assessment.

- [Source review](audience-review.source.md): **pass**. Authorized cuts and surviving joins preserve the argument. One repeated opening label was repaired. At that review stage the issue-5 alternatives were assessed as suitable but remained unapplied. They have since been approved; the follow-up below records application.
- [Listener review](audience-review.listener.md): **pass for authorized scope**. Understandable; information load manageable; whole-episode rhythm effective; fluent spoken American English. No further script repair requested. Optional pope-context expansion, the permitted Texas aside, and the retained closing ambiguity were reconciled against source and user choices. The Abbone heading remains consistent with the required source headings while narration uses Abbo.

The final three minor changes remove doubled opening emphasis, a repeated topic label, and a redundant chapter-9 introduction. Both reviewers checked these joins without rerunning their full reviews. No performed audio was assessed.

## Bounded verification

The user explicitly instructed that hashing and rechecking everything was unnecessary. The v2 skill now makes diff and affected-passage checks the default for routine editorial revisions. Earlier completed full checks and hashes remain in historical reports; no fresh comprehensive audit was required to finish this revision.

The retained [verify.py](verify.py) checks only this revision's recorded changes: unique, nonoverlapping targets; exact final application; unchanged headings and comments; requested removals; and the approved issue-5 replacements present with the taking-sides disclaimer absent. It does not rehash the research dossier or repeat transcript/source audits.

Actual commands completed:

```sh
uv run --no-sync ruff format episodes/013-la-paura-dell-anno-mille/editorial-v2/verify.py
uv run --no-sync ruff check episodes/013-la-paura-dell-anno-mille/editorial-v2/verify.py
uv run --no-sync python episodes/013-la-paura-dell-anno-mille/editorial-v2/verify.py
```

Result: **pass**, recorded in [verification-checks.txt](verification-checks.txt). The revised listener-review instructions also passed skill validation before the later bounded-verification clarification; that clarification changes Markdown instructions only.

## Preserved prior work

The prior final, draft, verification, and decision package are preserved in their `before-audience-revision` files. Earlier research qualifications and factual editorial choices are unchanged; this audience revision does not claim to settle those historical questions. No production metadata, canonical episode script, recording, publication, or unrelated repository code was changed.


## Approved scope follow-up

Applied the two exact approved Abbo/Thiota clarifications. Removed the taking-sides sentence entirely because the user identified its referent as the deleted Aristotle dispute, and applied the remaining closing clarification about universal paralysis in 999. Checked the three transitions and exact patch application. Prior full reviews remain historical; no new reviewer round, dossier hashing, or source audit was performed.
