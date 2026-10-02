# Episode 014 — final audience verification

Date: 2026-10-02
Status: final-audience-review complete; recording script ready for recording.
Scope: the existing episode’s final audience stage; no workflow migration or publication.

Reviewed input SHA256: `58cf3e5f0ad6b0d1e40c075268b741edc21fa9cc6c362553c3399fbad158e1e4`
Final script SHA256 (both script.en.md and script.editorial.en.md): `db2e4557521722ff79b1bc49915b52cc6fd5a1f4aaf99df130bd97281aaebdf9`

All ten instructions resolved: FR-001–003 and FR-006–010 implemented; FR-004 implemented only the requested phrase, other suggestions declined; FR-005 rejected and retained. The exact 21 before/after replacements, user instructions, reasons, and retained dispositions are recorded in changes.final.md. Original first-impression review and input hash remain in review.final.md.

Applied using short local `uv run --no-sync python` scripts and the repository’s existing `_apply_patches`, starting from unchanged script.spoken.en.md. The updated listener-review.yaml preserves the previous full recommendation queue in review_history. That snapshot was reconstructed and matched the reviewed input exactly. No new v2 draft/decision format was introduced into this older episode.

Checks passed: all 21 targets unique; original 19 edits nonoverlapping; final output equals the exact authorized edits plus the two documented transition repairs; listener queue validates with no pending decisions; both script artifacts equal deterministic application; headings, chapter/transcript coverage, all comments, research markers, curly-quoted spans, and the exact unquoted Orwell sentence unchanged. Source, evidence ledgers, and spoken base unchanged. `git diff --check` passed.

A fresh gpt-6-astra/high context performed a bounded follow-up of actual changes against user instructions and relevant Italian passages. It confirmed fidelity and the custom constraints, including the retained count characterization and colonial framing. It found two redundant introductions at replacement joins, now removed: the repeated Cuneo introduction and adjacent “Boece says” attribution. Those final adjustments were checked directly. This was not a second full audience evaluation.

Affected transitions and callbacks remain coherent. Chapter 5 keeps its source sequence, protest, ban qualification, and Italy punch line. Chapter 6 distinguishes the invented Evenus from Malcolm/Margaret and retains the tax wordplay. Chapter 8 preserves the opening-wedding callback and explains godparenthood. Chapter 9 keeps the exploitation/legal-entitlement distinction and exact Orwell wording. FR-009 improves local fluency without changing the count story or dialogue.

Existing source qualifications and historical limitations in review.final.md remain, including the retained Amiens account, Violetta name-history assertions, and incompletely sourced individual wedding examples. No audio or performed listening was assessed. Readiness here concerns the reviewed text, not recording, rendering, or publication.

Reproduction check (from repository root):

```sh
uv run --no-sync python - <<'PYCODE'
from pathlib import Path
from barbero_scripts.workflow import load_yaml_mapping, validate_listener_queue, _apply_patches
p = Path('episodes/014-ius-primae-noctis')
assert validate_listener_queue(p) == []
q = load_yaml_mapping(p / 'listener-review.yaml')
assert all(r['decision'] != 'pending' for r in q['recommendations'])
s = (p / 'script.en.md').read_text()
out = _apply_patches(q, (p / 'script.spoken.en.md').read_text(), 'editorial-recommendation')
out = s.split('\n', 1)[0] + '\n' + out.split('\n', 1)[1]
assert out == s == (p / 'script.editorial.en.md').read_text()
print('PASS')
PYCODE
```
