# Transcript correction and verification

Review `{transcript_path}` in full and update `{corrections_path}`. Work only from the existing
transcription and episode-wide historical and linguistic context. Do not use or claim to have
reviewed the audio.

## Editorial boundary

- Read the complete transcript so later context can inform earlier corrections.
- Correct only spelling, punctuation, historical names, dates, and obvious speech-recognition
  errors.
- Preserve every utterance ID and replace complete utterance text, never a fragment.
- Do not rewrite for style, smooth the speaker's spoken Italian, remove meaningful repetition or
  disfluency, or alter substantive claims.
- Use contextual judgment to resolve awkward text. Do not defer merely because audio is
  unavailable.
- Leave an item unresolved only when it is genuinely unintelligible or historically ambiguous and
  choosing a reading would risk inventing content.

## Pass 1: propose corrections

Include only utterances that require changes. Keep proposals distinguishable from accepted text:

```yaml
U-00001:
  text: "Complete corrected Italian utterance."
  reviewed: false
```

## Pass 2: resolve review flags

Revisit every utterance carrying a review flag. The default outcome is to accept its existing text
or make the most contextually justified minor correction. Aim to resolve essentially the entire
queue.

For unchanged text, omit `text`:

```yaml
U-00002:
  reviewed: true
```

For corrected text, include the complete utterance:

```yaml
U-00003:
  text: "Complete corrected Italian utterance."
  reviewed: true
```

Preserve all previously accepted corrections when updating the file. Report any exceptional
unresolved IDs and explain precisely why contextual resolution would risk inventing content.

## Verification

Before finishing:

1. Parse the generated YAML.
2. Confirm every entry ID occurs in the transcript.
3. Confirm every entry contains `reviewed` and optionally `text`, with no other fields.
4. Confirm every supplied `text` is non-empty and contains the complete replacement utterance.
5. Confirm pass-one proposals use `reviewed: false` and pass-two decisions use `reviewed: true`.
6. Report counts for proposed corrections, unchanged approvals, corrected approvals, and unresolved
   passages.

Do not edit committed transcript or research files, and do not create a Git commit.

