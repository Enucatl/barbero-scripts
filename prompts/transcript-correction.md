# Transcript correction pass

Review `{transcript_path}` in full and generate `{corrections_path}`.

## Editorial boundary

- Work only from the existing transcription and episode-wide historical context.
- Do not use or claim to have reviewed the audio.
- Read the complete transcript so later context can inform earlier corrections.
- Make only high-confidence corrections to spelling, punctuation, historical names, dates, and
  obvious speech-recognition errors.
- Preserve every utterance ID.
- Include only utterances that actually require changes.
- Replace the complete utterance text, not a fragment.
- Do not rewrite for style, smooth the speaker's spoken Italian, remove meaningful repetition or
  disfluency, alter substantive claims, or silently resolve genuine ambiguity.
- Leave uncertain passages unchanged and report their IDs at the end.

## Output format

Write valid YAML keyed by utterance ID:

```yaml
U-00001:
  text: "Complete corrected Italian utterance."
  reviewed: false
```

Always set `reviewed: false`. Text-only inference is not audio confirmation.

## Verification

Before finishing:

1. Parse the generated YAML.
2. Confirm every correction ID occurs in the transcript.
3. Confirm every entry contains exactly `text` and `reviewed`.
4. Confirm every `text` is non-empty and contains the complete replacement utterance.
5. Confirm every `reviewed` value is `false`.
6. Report the correction count and uncertain passages deliberately left unchanged.

Do not edit committed transcript or research files, and do not create a Git commit.

