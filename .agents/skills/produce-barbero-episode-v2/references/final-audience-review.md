# Final audience evaluation and user-directed edits

Run this stage after the recording script has passed the preceding application and verification
checks. Use a new reviewer context with `gpt-6-astra` at high reasoning, separate from the writer
and earlier reviewers. Give it the complete current `TRIAL/script.en.md` and the prompt below;
withhold earlier reviews and the writer's explanations so its first impression is independent.
After that first impression is recorded, provide the Italian source, relevant evidence, and
existing editorial decisions to check proposed solutions for fidelity and settled choices.
Record the model, effort, fresh-context use, and reviewed script version in `TRIAL/review.final.md`.
The skill's model-availability rule applies; if a fresh context is unavailable, disclose that
limitation and request the user's direction before substituting self-review for this stage.

## Compiled reviewer prompt

Review this complete English episode from the point of view of a contemporary American reader
without specialist historical or Italian cultural knowledge. It is intended for spoken narration,
so also judge whether a listener can follow it on first hearing. I prefer simple, contemporary,
natural American English. Give me a candid final evaluation and actionable findings. Do not edit
the script yet.

Assess the episode overall and give explicit judgments on:

- **Understandability:** Is the argument or story clear? Identify missing context, unclear
  referents, assumed knowledge, and explanations that are difficult to follow.
- **Information load:** Does it overwhelm the reader or listener with names, dates, references,
  digressions, or dense explanations? Consider their cumulative effect across the episode.
- **Rhythm:** Does the narration keep its momentum? Identify slow stretches, abrupt transitions,
  repetition, and interruptions to a scene or a joke's setup and payoff. Preserve effective detail.
- **Fluency:** Does it sound like natural spoken American English? Locate clunky Italian syntax,
  literal translations, stiff phrasing, and sentences that are awkward to say or hear.
- **Vocabulary:** Flag unnecessarily complicated, obscure, formal, or dated words. Suggest familiar
  contemporary wording when it preserves the meaning. Keep precise historical terms when useful,
  proposing a brief explanation where needed. Do not flatten the speaker's voice or alter exact
  source quotations just to make every word simple.
- **Live conference references:** Locate references to the venue, people in the room, slides,
  the occasion, other talks, or audience reactions. Propose removal or adaptation for a standalone
  episode, explaining what context, meaning, or comic timing the proposed change must preserve.
- **Suitability for this audience:** If the episode or a passage depends heavily on Italian
  language, pronunciation, or literature, assess whether an American audience can follow and
  enjoy it with reasonable context. You may propose cutting a passage or omitting the entire
  episode from the English series. Explain the specific obstacle, what would be lost, and whether
  a practical adaptation could make it work. An Italian subject alone is not a reason to remove it.

Start with an overall judgment and the strengths worth preserving. Then list findings by stable
ID (`FR-001`, `FR-002`, and so on), ordered by their likely effect on the audience. For each,
give the chapter/location and exact current passage where applicable, explain the issue and its
effect, propose a concrete solution (sample wording where useful), and explain why that solution
fits. Identify tradeoffs or uncertainty. An episode-level removal proposal should identify the
episode and its relevant dependencies rather than invent a single passage target. A no-change
assessment is valid; do not manufacture issues or impose a shorter runtime.

I will go through the findings manually, one by one, and write what I want implemented as a custom
solution for each point. Your proposals are suggestions, not authorization to edit. Wait for my
instructions; preserve points I reject or choose to retain. When implementing my instructions,
ask about a genuine conflict or ambiguity that materially changes the result. After the approved
changes are applied, give me a report showing each change's exact before and after, which issue
it fixes, and why it was done that way. Include retained and unresolved findings with their
disposition so I can see what remains.

## Decisions, application, and change report

Save the evaluation in `review.final.md` and present it to the user without changing script files.
Reconcile source/evidence checks in the report after the independent first impression; preserve
existing rejected choices unless the user explicitly reopens them. Record each finding's user
instruction and disposition under its stable ID. An unanswered point stays pending. The user may
answer one at a time or together; continue authorized work on answered points without treating
silence on the others as acceptance. This stage explicitly waits for user direction even for
routine wording repairs.

Implement the user's custom solution rather than assuming approval of the reviewer's sample.
Use the established draft/decision history and deterministic application procedure. Routine
wording changes belong in the draft history; material departures belong in `decisions.yaml`
with their explicit authorization. Resolve dependencies and overlapping instructions before
applying patches. Preserve the reviewed version or its exact before passages for the report.
Follow the existing prohibition on producing a partially applied decision queue; preparing
answered points does not authorize a partial final script while required decisions are pending.

Whole-episode omission is an editorial recommendation until the user decides. Record an accepted
omission as a decision not to take this episode forward; retain the source and trial artifacts.
It does not authorize deleting files, changing the series catalog, or publishing changes.

After application, save `TRIAL/changes.final.md` with a row or entry for every implemented change:
finding ID and location, exact before text, exact after text (or an explicit removal), the issue
fixed, the user's instruction, and the reasoning behind the chosen implementation. Explain how
the wording improves the reader/listener experience and what meaning or narrative function it
preserves. Record rejected, retained, unresolved, and episode-omission decisions separately from
text changes. Include the actual verification outcome and any remaining limitations.

Verify the actual diff against the instructions, check changed passages against the source and
evidence where relevant, preserve protected quotations and chapter/coverage markers, and check
affected transitions, callbacks, rhythm, and cross-chapter dependencies. Update `verification.md`
with the resulting script version and final-review dispositions. Reuse preceding checks for
unchanged inputs; repeat the independent evaluation only if subsequent changes invalidate it.
Declare `ready-for-recording` only when the required final-review decisions and applicable checks
are complete. An episode the user elects to omit is recorded as omitted, not ready for recording.
