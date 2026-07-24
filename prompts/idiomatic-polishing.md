# Final spoken-English controller

Produce the directly recordable `{script_path}` through two separate model passes using the model
configured in the current Codex session:

1. Run `spoken-english-rewrite.md` from `{corrected_path}` to `{spoken_draft_path}`.
2. Run `fidelity-read-aloud-audit.md` against both files to produce `{script_path}`.

Do not collapse these into one pass. The first pass is allowed to rewrite local sentence structure
aggressively for natural speech; the second is responsible for catching lost meaning, added prose,
quotation changes, and residual stiffness. Do not create a separate recording copy or commit.
Across both passes, approved corrections must sound like ordinary narration, never like visible
fact-checks; `[N-...]` markers alone record that a correction was made.
