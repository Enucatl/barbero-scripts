# Faithful English translation controller

Produce `{translation_path}` through three mandatory sequential passes. Do not launch a separate
Codex CLI or select another model.

1. Run `utterance-translation.md` to translate every transcript utterance independently with
   Google Translate into `{utterance_translation_path}`. This is the only pass permitted to use an
   external translation service.
2. Only after every utterance ID validates, run `translation-assembly.md` to create
   `{assembled_translation_path}` in longer coherent sections.
3. Only after assembly validates, run `translation-consistency.md` to create the final
   `{translation_path}` with consistent formatting, names, and spelling.

Do not combine these passes into one generation. Passes two and three use the model configured in
the current Codex session and must compare their output back to both the raw utterance translations
and the Italian transcript. Accuracy review
may begin only after all three artifacts pass validation. Do not create a commit.
