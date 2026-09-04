# Transcript correction and uncertainty detection

Read `{transcript_path}` in full and update `{uncertainties_path}`. Acoustic items already expose
the relevant word text, confidence, and cleaned/original timestamps. Independently add semantic
items for names, foreign expressions, dates, quotations, places, internal incoherence, and any
automatic correction that may change meaning. Do not claim acoustic evidence you did not inspect.

Correct only spelling, punctuation, historical names, dates, and obvious recognition errors.
Preserve every utterance ID and propose complete utterance text, never a fragment. Do not rewrite
style, smooth spoken Italian, remove meaningful repetition or disfluency, or alter claims.

Every machine-created item has `resolution.status: pending`. Agents may add reasons and a
conservative `proposed_text` but must not resolve it. A human resolves an item by storing the
complete resulting utterance, whether keeping current text, accepting the proposal, or editing it:

```yaml
resolution:
  status: resolved
  resolved_text: "Complete resulting Italian utterance."
  note: null
```

Acoustic or semantic reasons may be absent individually, but each item needs at least one. Preserve
prior human resolutions. Before finishing, parse the YAML; verify stable IDs, exact utterance
references, complete replacements, a fresh transcription fingerprint, and `pending` on every new
item. Only after that full contextual scan, change the queue's `detection_status` from
`acoustic-complete` to `complete`; this opens the human resolution gate. Report acoustic,
semantic-only, and pending counts. Do not edit committed transcript or research files and do not
create a commit.
