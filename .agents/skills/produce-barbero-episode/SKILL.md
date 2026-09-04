---
name: produce-barbero-episode
description: Produce or resume one Barbero English episode from source audio through validated editorial artifacts and an unlisted preview. Use only when explicitly invoked for this repository workflow.
---

# Produce a Barbero episode

Start with `uv run barbero status EPISODE --json`. Treat its validated artifact paths as the
authoritative resumable state; do not create a separate run ledger or redo completed stages.
Reject an overwrite of an existing episode unless the user explicitly authorizes it.

For each `machine` state, run the `next_action` using the existing `barbero` command. For each
`agent` state, give one agent only that stage's inputs, output contract, and linked reference.
Agents editing shared YAML run sequentially. Tense and naturalness chapter agents may run
concurrently only when each owns a distinct chapter file. Re-run JSON status and relevant
validation after every stage.

Pause at every `human` state. Never select a speaker, resolve transcript uncertainty, or accept or
reject content/listener proposals for the user. Stop on `invalid` and repair the named artifact
deterministically before continuing. Sol research stages may report blocked findings but must not
weaken the evidence standard or fall back to an external model.

## Stage references and routing

| Work | Reference | Model and effort |
|---|---|---|
| Transcript uncertainty pass | [transcript-review.md](references/transcript-review.md) | GPT-5.6 Luna, medium |
| Italian chapter definition | [italian-assembly.md](references/italian-assembly.md) | GPT-5.6 Luna, medium |
| Outline and research-target extraction | [outline.md](references/outline.md), [research-target-extraction.md](references/research-target-extraction.md) | GPT-5.6 Luna, high |
| Individual quotation research and bounded claim research | [quotation-research.md](references/quotation-research.md), [historical-research.md](references/historical-research.md) | GPT-5.6 Sol, high |
| Whole research audit | [research-audit.md](references/research-audit.md) | GPT-5.6 Sol, high |
| Faithful chapter translation | [faithful-translation.md](references/faithful-translation.md) | GPT-5.6 Luna, high |
| Unified quotation/accuracy proposals | [quotation-accuracy.md](references/quotation-accuracy.md), [content-review.md](references/content-review.md) | GPT-5.6 Luna, high |
| Chapter tense review | [chapter-tense.md](references/chapter-tense.md) | GPT-5.6 Luna, medium |
| Chapter naturalness review | [chapter-naturalness.md](references/chapter-naturalness.md) | GPT-5.6 Luna, high |
| Whole-episode listener review | [listener-review.md](references/listener-review.md) | GPT-5.6 Sol, high |
| Final consistency and integration verification | [final-consistency.md](references/final-consistency.md) | GPT-5.6 Luna, medium |

The semantic transcript pass changes `detection_status` from `acoustic-complete` to `complete`
only after scanning the full transcript context. The research audit must write
`research-audit.yaml` using the schema in its reference; translation remains blocked unless its
verdict is `ready` and every input hash still matches.

After final consistency, run `uv run barbero validate EPISODE`. Publish with `barbero
publish-preview` in its default tokenized mode only. Public publication, commits, pushes,
provider changes, and overwriting episodes require separate explicit authorization. Verify the
preview output and report its location; do not use `--public` by default.
