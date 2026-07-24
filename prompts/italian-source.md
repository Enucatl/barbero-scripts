# Establish the Italian source

Read `{transcript_path}` in full. First reconstruct the entire episode continuously, in utterance
order, without rewriting or omitting anything. Review the reconstruction against the available
audio and put only demonstrable recognition corrections in the external `corrections.yaml`.
Preserve fillers, repetition, false starts, spoken grammar, jokes, and digressions.

After rerendering the corrected transcript, define numbered chapters in `chapters.yaml`, then run
`barbero assemble-italian {episode_directory}`. The assembler may join utterances into continuous
paragraphs and add punctuation already present in the transcript; it must not change the text that
would be recited. Research markers belong in HTML comments and must not alter spoken wording.

Initialize the audio checkpoint with `barbero init-italian-review`. Entries default to `true`; set
an utterance or chapter to `false` when review finds a problem. The file uses this schema:

```yaml
utterances:
  - id: U-00001
    reviewed_audio: true
chapters:
  - id: CH-001
    complete_ordered_coverage: true
```

List every utterance and chapter exactly once and in order. Do not create an outline, research
ledger, translation, or English script until `barbero validate` confirms this checkpoint.
