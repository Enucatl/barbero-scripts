# Final audience changes — The Merchant

All three genuinely new findings were decided individually: the user replied `a` to FR-004, FR-006, and FR-007, approving each exact displayed replacement. Four findings were already settled by earlier rejections and remain unchanged. No pending final-review decisions remain.

The final was regenerated from the frozen draft and 43 fully resolved material choices; no language-model regeneration or patching of the prior final was used. History snapshot 3 preserves the original 41 choices, draft version, reviewed script version, and exact FR-007 routine repair. The original 41 item records remain identical.

## FR-004 — Chapter 6 — War and the Ordinances of Justice

User instruction: literal `a`, approve the displayed proposal. Disposition: **Implemented as approved**.

Before:

```text
But the Florentine popolani are tougher. They want to try. They enact the Ordinances of Justice. Another name some of us remember from school: Giano della Bella.

What are these ordinances? Put simply, an extraordinary law.
```

After:

```text
But the Florentine popolani are tougher. They want to try. They enact the Ordinances of Justice.

What are these ordinances? Put simply, an extraordinary law.
```

The shared-school-memory cue introduces an unexplained Italian name. The user approved deleting that sentence. This leads directly from the Ordinances to their explanation, preserving the Florence–Arezzo contrast and legal argument while deliberately losing Giano’s name. Material cut recorded as ED-042.

## FR-006 — Chapter 9 — Offices, Justice, and Public Money

User instruction: literal `a`, approve the displayed proposal. Disposition: **Implemented as approved**.

Before:

```text
Because government taxes people. It taxes them to... But I don't want to go fishing for easy applause. I'm talking about Florence at the end of the thirteenth century.
```

After:

```text
Because government taxes people. But remember, I'm talking about Florence at the end of the thirteenth century.
```

The unfinished tax-purpose sentence and applause remark depend on live delivery. The user approved their replacement with the exact proposed wording. “But remember” preserves the teasing return to medieval Florence; the court-influence setup and subsequent public-money discussion stay unchanged. The applause joke is deliberately lost. Material cut recorded as ED-043.

## FR-007 — Chapter 1 — opening

User instruction: literal `a`, approve the displayed proposal. Disposition: **Implemented as approved**.

Before:

```text
Good evening again. I promised to talk about a medieval merchant: to try to understand how a merchant in the Middle Ages thinks, how he sees the world.
```

After:

```text
Let's talk about a medieval merchant and try to understand how he thinks, how he sees the world.
```

The original greeting and promise refer to a prior live occasion. The user approved a direct invitation into this episode. The subject, attempt to understand the merchant’s outlook, and conversational voice remain. Dino’s introduction and the later merchant/politician pivot follow unchanged. Routine adaptation recorded in draft history snapshot 3.

## Retained findings and unresolved work

| Finding | Disposition and reason |
|---|---|
| FR-001 | Retained by prior choice: rejected ED-032/035 preserve the broad religion rhetoric. |
| FR-002 | Retained by prior choice: rejected ED-028 preserves the Cencelli reference. |
| FR-003 | Retained by prior choice: rejected ED-006 preserves the kinship passage. |
| FR-005 | Retained by prior choice: rejected ED-031 preserves Chapter 11 baptism wording. |

No new finding was rejected. No final-review decision is unresolved. Earlier research deferrals and the deliberately retained tradeoffs remain as documented in verification.md; these audience edits do not resolve historical uncertainty.

## Actual verification

Command:

```sh
uv run --no-sync python /home/user/data/barbero/editorial/020-come-pensava-un-uomo-del-medioevo-il-mercante/apply-v2.py
```

Passed: frozen base/input hashes; 43 resolved material choices (18 accepted, 25 rejected); unchanged original 41 records; exact unique accepted targets and nonoverlapping intervals; complete quotation inventory; protected recovered spans; all rejected passages retained; headings and chapter/coverage/research markers preserved; exact deterministic output. A separate equality check proves that the output differs from the preserved reviewed script only by the three approved final-review edits. The actual unified diff contains exactly those three replacement hunks. Root read each resulting passage with its preceding/following paragraphs and the relevant Italian source. These edits affect no later name callback, historical quotation, or cross-chapter argument; they do not invalidate the independent full-episode review.

Results: **12 chapters; 801 source utterances covered in order; 43 visible quotations; 2 protected recovered spans; 7,585 spoken words**. The three edits remove 33 spoken words under the established heading/comment-exclusion method. Source/evidence inputs are unchanged, so earlier production checks remain applicable. No audio was listened to and no narration was performed. Recording itself remains outside this completed text workflow.

- Reviewed script SHA256: `8c1b1ece45b0e6fc2d9eaeb8b4b0514f82eb77c1bb2b180b57455bbe919e3647`.
- Final script SHA256: `f06bbd26e453e944a2d4923ad4b513eb664350fea1f137dfadc3e4c86feff8a2`.
- Current frozen draft SHA256: `ff94ee9e5bf8a9eba3746218ab5747bcdc2a4545eefc2f68a9d72b855ad14ae0`.
- Current decision queue SHA256: `eb2d8d32fc6c542031bbbe4dc16d9be57b8a0058f9cf15dccb126f27e0eaaddc`.
- Application checker SHA256: `a9d10a8627ae51a80f47b064a21033499a72e8481ea61fbe7342021bcd9c77ae`.


The independent GPT-6 Astra/high final-audience reviewer’s bounded follow-up passed on the final SHA256 `f06bbd26e453e944a2d4923ad4b513eb664350fea1f137dfadc3e4c86feff8a2`. All three actual replacements match the approved proposals. The Ordinances transition, tax/public-money transition, Dino introduction, and later merchant/politician reconsideration work in context. No further repair or reopened rejection is required. This follow-up reviewed only changed passages and their source/context; it did not repeat the full evaluation or assess audio. Status: **ready-for-recording**.
