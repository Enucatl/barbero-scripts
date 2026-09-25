# Stage execution and handoffs

`EPISODE` is the repository-relative episode directory; `CONFIG` is `EPISODE/episode.yaml`.
Run commands from the repository root. The CLI and validators are the schema authority; inspect
`src/barbero_scripts/cli.py` and `workflow.py` when a contract is unclear. Existing episode files
may use legacy schemas and are not automatically templates for new work.

## Machine actions

Use `uv run barbero` before each command below. Choose the action from both status and the existing
artifacts; one stage can require several different commands.

| Stage or condition | Command |
|---|---|
| New episode with supplied identity and source | `init --number N --slug SLUG --title TITLE --source AUDIO` |
| Preparation, or resume after speaker selection | `prepare CONFIG` |
| Show speaker choices | `speakers CONFIG --show` |
| Record a speaker explicitly selected by the user | `speakers CONFIG --select SPEAKER_ID` |
| Missing transcription response or manifest | `transcribe CONFIG` |
| Create acoustic queue or rerender after transcript decisions | `render CONFIG` |
| Chapters defined and Italian script missing | `assemble-italian EPISODE` |
| Italian checkpoint missing after assembly | `init-italian-review EPISODE` |
| Content decisions complete | `apply-content EPISODE` |
| Start tense review | `init-tense EPISODE` |
| All tense chapter files reviewed | `assemble-tense EPISODE` |
| Start naturalness review | `init-naturalness EPISODE` |
| All naturalness chapter files reviewed | `assemble-naturalness EPISODE` |
| Listener decisions complete | `apply-listener-review EPISODE` |
| Final script ready | `validate EPISODE` |
| Recorded episode ready for preview | `publish-preview` |

Use the repository's long-command instructions for audio, transcription, and publication. Ask only
for missing identity/source information that cannot be recovered from the request or metadata.
Do not initialize an existing episode. On resume, inspect existing chapter review files before
initialization: the initializers reject existing files. Review unfinished chapters and assemble
them once all are complete. Never add a review marker merely to pass validation.

`finalize-consistency EPISODE` copies the editorial script unchanged. It can implement a reviewed
no-change result; it does not perform the final semantic review.

## Stage inputs and completion

Resolve placeholders using the selected episode and workflow version. For v2, `{corrected_path}`
in tense review means `script.content.en.md`; `{tense_path}` means `script.tense.en.md`;
`{spoken_path}` means `script.spoken.en.md`; `{editorial_path}` means `script.editorial.en.md`;
`{final_path}` means `script.en.md`. Obtain external audio/provider paths from `episode.yaml`.

Pass the exact chapter or target ID and input/output paths to each agent. Include the Italian
chapter, approved corrections, and protected quotation spans needed for its comparison. For
whole-episode reviews, include the full required source. Keep a single writer for shared ledgers
and assembled scripts. An agent's completion message must identify actual saved outputs and checks,
not just assert that the stage is done.

Run `validate EPISODE` at the checkpoint described by the stage reference, and inspect its errors
in context: expected missing downstream artifacts are not permission to skip a failed current
invariant. After a passing stage check, use `status EPISODE --json` to choose subsequent work.
If inputs change, review affected descendants before reusing them; file existence alone is not
evidence that a draft or decision remains applicable.

## Preview prerequisites and completion

The publisher scans the configured episodes root, not a positional episode argument. Read
`docs/podcast-preview.md` and the target's publication metadata before using it. The target needs
publication metadata and recorded audio at the configured audio root. If recording or required
metadata is missing, finish and validate the editorial artifacts and report those concrete missing
inputs. Do not synthesize a recording, invent a publication date, or claim a preview exists.

The default `publish-preview` command builds the tokenized site for eligible episodes. Verify the
target episode page, RSS entry, and media exist in the returned output. Only after successful target
verification, set `preview_published: true` in its `episode.yaml` and re-run status; the publisher
does not write this flag itself. A successful build containing only other episodes is insufficient.
This flag records local build completion, not network reachability. Current Caddy configuration
does not serve token-prefixed previews: report the local output path and this limitation. A request
for a reachable private preview needs a separately scoped serving change. Do not use `--public`
to work around that limitation without the user's explicit authorization.
