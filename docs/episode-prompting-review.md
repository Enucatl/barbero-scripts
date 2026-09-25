# Episode prompting review

Reviewed on 2026-09-25 against the repository's skill, editorial references, CLI,
workflow state detection, and existing workflow tests. This update changes instructions and routing
expectations; it preserves artifact schemas, recorded editorial decisions, and episode content.

## Guidance and application

The official [GPT-6 prompting guidance](https://developers.openai.com/api/docs/guides/latest-model/gpt-6-astra.md#prompting-best-practices)
identifies sensitivity to conflicting skill instructions, unnecessary clarification pauses, and
the need to calibrate delegation and verification. It presents family-wide starting points based
on Astra behavior, with evaluation required for the selected model and workload. Here that means
explicit stage contracts, reuse of authorization, concrete human decisions, and bounded chapter
delegation. These are workflow choices, not evidence that a particular model produces better prose.

The [migration quickstart](https://developers.openai.com/api/docs/guides/latest-model/gpt-6-astra.md#migration-quickstart)
recommends preserving effective reasoning effort where supported. The focused production and
evidence work moves to GPT-6 Luna/Sol. All Luna stages use high reasoning, which GPT-6 Luna
supports. Whole-episode listener synthesis uses GPT-6 Astra at high reasoning because it integrates audience needs across
the complete script and outline. This is the project's workload judgment; evaluate it on
representative episodes. No OpenAI API client is present in this pipeline, so endpoint, sampling,
and SDK migrations are unnecessary. Codex must provide the selected models and tools; a Markdown
route does not configure the host automatically.

The official [skills documentation](https://developers.openai.com/codex/skills) supports progressive
loading of focused references. The existing single production skill remains explicitly invoked,
with its invocation policy preserved. Command details live in a reference loaded for execution.

## Findings addressed

| Previous instruction or gap | Updated behavior |
|---|---|
| GPT-5.6 routes | GPT-6 Luna/Sol with existing workload roles and efforts |
| Chapter-definition agent told to resolve human transcript uncertainties | Chapter definition consumes resolved transcript; new uncertainty returns to the queue |
| Every human state demanded a fresh pause | Apply decisions already supplied; request only outstanding decisions |
| Existing episode overwrite prohibition could block resume | Resume unfinished stages; replacing completed work still requires authorization |
| Prose `next_action` described as runnable | Concrete CLI mapping, including configuration vs directory arguments |
| Invalid artifacts required only deterministic repair | Stale research audits require renewed evidence review before hash refresh |
| Faithful translation required all recovered wording to be absent | Check that research replacements were not introduced; allow natural coincidence |
| Naturalness said both keep text and rewrite it | Preserve substantive content and approved corrections while rewriting prose |
| Research assumed retrieval tools and updated an ambiguous external audit | Report unavailable retrieval; refresh the durable audit in its designated stage |
| Successful publication command could omit target episode | Check recording/metadata prerequisites and verify target page, feed, and media |
| Tokenized build could be described as a reachable preview | Report local build completion; current Caddy serves no token-prefixed preview |

## Evaluation when changing models or prompts

Run editorial comparisons in a temporary copy of representative inputs, preserving originals and
human decisions. Record the model, effort, exact input revision, and checks with the comparison
results. Keep schema validation separate from editorial judgment; a valid file can still lose wit,
misrepresent a source, or sound translated.

| Representative task | Acceptance evidence |
|---|---|
| Transcript with an ambiguous name and a prior resolution | Complete uncertainty scan; prior decision preserved; new item pending; no claimed unheard audio |
| Quotation from a later recollection or composite source | Opened source and locator; disclosed provenance; no invented wording or merged attribution |
| Translation interleaving quotation and commentary | Complete ordered coverage; commentary stays between fragments; no premature research replacement |
| Historical-present chapter with flashback and exact quotation | Correct scene chronology and grammar; quotation unchanged |
| Naturalness chapter with an approved factual correction | Natural spoken English; approved meaning, quotation spans, markers, and substantive details retained |
| Stale audit or missing recording | Evidence re-reviewed or concrete blocker reported; no fabricated readiness or preview |
| Whole-episode listener synthesis | Complete script and outline considered together; proposals map to listener needs and remain bounded to the decision queue |

Use the existing workflow policy, status, Italian-first, and v2 tests for deterministic regression
checks. The skill validator checks packaging; a separate read-only scenario walkthrough checks
interpretation of the instructions. Neither establishes end-to-end GPT-6 editorial quality.
Before reducing reasoning effort or changing the tier split, compare actual generated research and
chapters against these criteria. This repository review does not regenerate or publish an episode.

The independent read-only walkthrough covered pending transcript decisions, stale audit inputs,
coincident quotation wording, missing recorded audio, and parallel naturalness work with an approved
correction. It also identified a legacy validator that rejects coincident recovered wording;
workflow v2 uses a separate validator. Completed legacy episodes retain their existing validation
behavior in this change. The walkthrough is not a generated-episode evaluation.
