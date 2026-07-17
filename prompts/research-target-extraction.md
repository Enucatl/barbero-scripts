# Research-target extraction

Read `{transcript_path}` and `{outline_path}` in full. Seed `{quotes_path}` and `{claims_path}` with
research targets. Do not perform external research and do not populate `{sources_path}` in this
pass.

## Quotations ledger

Create one YAML record for every direct quotation, slogan, attributed phrase, paraphrased document,
or wording whose historical provenance matters:

```yaml
- id: Q-001
  barbero_utterances: [U-00001]
  barbero_timestamp: "00:00"
  attribution: "Person, institution, document, or unknown"
  source_id: null
  original_language: null
  original_text: null
  translation: null
  locator: null
  translation_notes: null
  confidence: null
  status: pending
  research_note: "What must be identified or verified"
```

## Claims ledger

Create one YAML record for every central causal or interpretive claim, all historically disputed
assertions, and a representative sample of incidental facts:

```yaml
- id: C-001
  claim: "Neutral statement of the claim made in the lecture"
  transcript: [U-00001]
  centrality: central
  supporting_sources: []
  conflicting_sources: []
  status: pending
  script_treatment: pending
  research_note: "Evidence needed and likely point of dispute"
```

Allowed `centrality` values are `central`, `supporting`, and `sampled-incidental`. Use inclusive
utterance ranges as strings such as `U-00001–U-00005` when a claim spans consecutive utterances.

## Editorial boundary

- Preserve the provisional `Q` and `C` identifiers assigned in the outline.
- Add a new sequential identifier only when the outline clearly missed a target.
- Do not invent bibliographic data, source text, translations, locators, or confidence ratings.
- Keep every unresolved research field explicitly null, empty, or `pending`.
- Separate Barbero's historical assertion from his modern analogy.
- Do not treat rhetorical framing as an independently researchable claim unless accuracy affects
  the adaptation.

## Verification

Before finishing:

1. Parse both YAML files.
2. Confirm all IDs are unique, sequential, and match outline markers.
3. Confirm every transcript reference exists.
4. Confirm each quotation has provenance questions and each claim has an evidence question.
5. Confirm no entry is marked resolved and no unsupported source metadata was introduced.
6. Report quotation and claim counts plus any outline inconsistencies.

Edit only `{quotes_path}` and `{claims_path}` and do not create a Git commit.

