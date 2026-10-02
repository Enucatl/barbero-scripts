"""Check this audience revision against its recorded edits, without repeating source audits.

Run from the repository root with uv run --no-sync python PATH/verify.py.
"""

import json
import re
from pathlib import Path

TRIAL = Path(__file__).resolve().parent


def verify() -> None:
    """Check exact changed passages, structure, and approved scope revisions."""
    before = (TRIAL / "script.before-audience-revision.en.md").read_text()
    edits = json.loads((TRIAL / "audience-edits.json").read_text())
    intervals = []
    for edit in edits:
        old, new = edit["before"], edit["after"]
        assert old and before.count(old) == 1, edit["chapter_id"]
        assert re.findall(r"<!--.*?-->", old, re.S) == re.findall(r"<!--.*?-->", new, re.S)
        start = before.index(old)
        assert re.findall(r"<!-- chapter: (CH-\d{3});", before[:start])[-1] == edit["chapter_id"]
        intervals.append((start, start + len(old), edit))
    intervals.sort(key=lambda entry: entry[0])
    assert all(a[1] <= b[0] for a, b in zip(intervals, intervals[1:], strict=False))
    expected = before
    for start, end, edit in reversed(intervals):
        expected = expected[:start] + edit["after"] + expected[end:]
    final = (TRIAL / "script.en.md").read_text()
    assert final == expected, "Final differs from recorded audience edits."
    assert re.findall(r"^#{1,2} .*", final, re.M) == re.findall(r"^#{1,2} .*", before, re.M)
    for proposal in json.loads((TRIAL / "audience-scope-proposals.json").read_text()):
        assert final.count(proposal.get("applied_text", proposal["after"])) == 1
        assert proposal["before"] not in final
    spoken = re.sub(r"<!--.*?-->", "", final, flags=re.S)
    spoken = re.sub(r"^#{1,2} .*", "", spoken, flags=re.M)
    for removed in (
        "Aristotle",
        "Mont Saint-Michel",
        "Protestant Texas",
        "Martinmas",
        "sharecropping",
        "one last thing",
        "we're nearly there",
        "taking sides",
    ):
        assert removed not in spoken, removed
    print(f"PASS: {len(edits)} recorded edits; headings/comments preserved; issue 5 applied.")
    print("Spoken English words:", len(re.findall(r"\b[\w’'-]+\b", spoken)))


if __name__ == "__main__":
    verify()
