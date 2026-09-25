---
name: produce-barbero-episode-v2
description: Produce or resume a Barbero episode with the simplified GPT-6 Astra editorial workflow when the user requests the v2 skill or an Astra workflow trial. Establish the Italian source, research evidence, draft one English adaptation, independently review it, and apply editorial decisions to a recording script.
---

# Produce a Barbero episode — v2 trial

Create a faithful, engaging English adaptation with one writer responsible for the whole episode.
Use one English draft, independent source and listener reviews, and targeted repairs. Preserve
Barbero's argument, uncertainty, historical texture, dialogue, and comic timing. User instructions
and existing editorial decisions take precedence over the defaults below.

## Coexistence and scope

This is a second **skill**, not the CLI's existing `workflow_version: 2`. Keep the original
`produce-barbero-episode` skill and episode artifacts intact. For the selected episode directory
`EPISODE`, put this trial's editorial outputs in `EPISODE/editorial-v2/`, called `TRIAL` below.
The deliverable is `TRIAL/script.en.md`; it does not replace `EPISODE/script.en.md`.

Reuse an established Italian source read-only. For a new episode, use the existing audio and
transcription commands and establish the source as described in [source.md](references/source.md).
Do not migrate an existing episode or change its workflow version to activate this skill.

The existing `barbero status`, `validate`, application commands, and publisher do not understand
the trial's editorial artifacts. Use status only to understand source preparation. Perform the
checks specified here; never manufacture old intermediate scripts or review markers to satisfy
the old pipeline. A completed trial is a reviewed recording script, not a CLI-complete or published
episode. If publication is requested, complete the editorial work and identify the remaining
integration and recording requirements; do not export into the old workflow automatically.

## Models and ownership

Use `gpt-6-astra` at high reasoning for the episode writer, evidence synthesis, and both independent
reviews. This is a starting configuration for the trial, not a measured optimum. If the host cannot
provide that model, report the limitation and use an alternative only if the user authorizes it.
Instructions do not themselves configure a host's model.

Delegate independent research investigations when useful, grouping targets that share documents
or historical context. Keep separate provenance for each target. Give workers concrete inputs,
questions, allowed output paths, and completion checks. Workers return findings; one coordinator
owns shared ledgers and the English draft. Do not divide the final voice among chapter writers.

Use fresh reviewers for source fidelity and listener experience. They may run in parallel with
distinct report paths. Give them the actual materials and decisions, without the writer's
self-assessment or the other review. If independent contexts are unavailable, perform separate
reviews and disclose that limitation; do not label self-review independent.

## Workflow

1. **Source and brief.** Read [source.md](references/source.md). Resolve meaningful transcript
   uncertainties, verify source wording and ordered coverage, then read the whole episode. Create
   `brief.md` with the chapter map, narrative arc, terminology, research targets, and editorial
   requirements in one planning pass. Ask only for unresolved source choices that require the user.
2. **Evidence.** Read [evidence.md](references/evidence.md). Establish quotation provenance and
   investigate central, disputed, and selected incidental claims. Write the three research ledgers
   and `research-review.md`. Audit evidence sufficiency and contradictions before drafting.
   Document responsible deferrals rather than inventing certainty.
3. **One adaptation.** Read [adaptation.md](references/adaptation.md). Write
   `script.draft.en.md` directly in natural spoken American English with coherent tense and voice.
   Use the complete Italian, brief, and evidence as context. Prepare exact proposals for new
   material interventions in `decisions.yaml`; preserve source meaning pending approval.
4. **Fresh reviews.** Read [review-and-decisions.md](references/review-and-decisions.md). Produce
   `review.source.md` and `review.listener.md`. Repair demonstrable translation or language defects
   without changing editorial choices. Consolidate research and listener proposals into one
   current decision package. Present consequential choices together, with exact wording and evidence.
5. **Decide, apply, verify.** Apply decisions already supplied; request only outstanding decisions.
   Apply accepted patches deterministically from the frozen draft. Verify the affected passages,
   quotations, full-episode continuity, and structural invariants. Save `script.en.md` and
   `verification.md` with actual checks, input hashes, remaining limitations, and final status.

Do not impose a faithful English intermediate, tense files, naturalness files, per-chapter approval
rounds, a separate run ledger, or repeated full rewrites. A difficult passage may need a close
translation for diagnosis; that does not make it a new episode-wide stage. After relevant checks
pass, repeat work only when changes, failures, or unresolved findings warrant it.

## Resume and decisions

Inspect saved artifacts and their recorded input hashes before choosing the next action. File
existence alone does not establish completion. Reuse current source decisions, evidence, reviews,
and approved edits. A changed source or ledger requires review of affected descendants, not a
blanket restart or a hash-only refresh. Consult the phase references for the relevant contract.

Routine phrasing, grammatical repairs, and implementation choices need no approval. New factual
departures, authoritative quotation substitutions, substantive cuts/additions, and title changes
belong in the decision package unless explicitly authorized already. Never infer approval from
elapsed time, a recommendation, or a research verdict. Prior episode choices are context, not
blanket permission to make analogous cuts in a new episode.

Complete independent authorized work while a decision is outstanding. If a required decision
prevents further progress, present the concrete alternatives and evidence, link this skill, and
quote the relevant requirement. A request limited to analysis or one phase ends at that scope.
Do not record unheard audio as reviewed or claim performed-listening or model quality evaluations
that were not carried out.

Finish with the deliverable paths, checks actually completed, consequential choices, and concrete
remaining work. Preserve the source title. Commit, push, publish, or replace an existing canonical
script only when the user's request explicitly authorizes that action.
