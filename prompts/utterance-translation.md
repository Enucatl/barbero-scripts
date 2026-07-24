# Pass 1: raw utterance translation

Read `{transcript_path}` and send every `U-00001`-style utterance independently to Google Translate
from Italian to English. Write `{utterance_translation_path}` as YAML:

```yaml
- id: U-00001
  text: "Faithful English translation"
```

Include every transcript ID exactly once and in order, including short fragments. Do not merge
utterances, fact-check, improve, compress, omit, add connective prose, or consult an existing
English script. Google output is a raw intermediate draft: do not present it for human accuracy
review or use it as the final translation.

After writing, verify exact ID equality and order against the transcript. Edit only
`{utterance_translation_path}` and do not create a commit.
