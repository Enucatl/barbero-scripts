# Establish the Italian source

Read `{transcript_path}` in full. First reconstruct the entire episode continuously, in utterance
order, without rewriting or omitting anything. Review the reconstruction against the available
audio and put only demonstrable recognition corrections in the external `corrections.yaml`.
Preserve fillers, repetition, false starts, spoken grammar, jokes, and digressions.

Resolve every pending item in `transcript-uncertainties.yaml` against audio. “Keep current,” “use
proposal,” and “edit” all store the complete resulting utterance in `resolved_text`. After
rerendering the resolved transcript, define numbered chapters in `chapters.yaml`, then run
`barbero assemble-italian {episode_directory}`. The assembler may join utterances into continuous
paragraphs and add punctuation already present in the transcript; it must not change the text that
would be recited. Research markers belong in HTML comments and must not alter spoken wording.

The exception queue replaces the full utterance checklist. Exact ordered coverage remains a
deterministic validation invariant. Do not create an outline, research ledger, translation, or
English script until every uncertainty is resolved and `barbero validate` confirms the checkpoint.
