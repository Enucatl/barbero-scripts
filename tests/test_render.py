from pathlib import Path

from barbero_scripts.render import render_recording, validate_episode


def test_recording_render_removes_research_markers_but_keeps_pronunciation(tmp_path: Path) -> None:
    source = tmp_path / "script.md"
    source.write_text("# Title\n\nHello [SRC-001] Sarajevo (sah-rah-YEH-voh). [C-001]\n")
    destination = tmp_path / "recording.md"
    render_recording(source, destination)
    assert destination.read_text() == "# Title\n\nHello Sarajevo (sah-rah-YEH-voh).\n"


def test_validation_resolves_markers_and_complete_quote(tmp_path: Path) -> None:
    (tmp_path / "transcript.it.md").write_text("reviewed")
    (tmp_path / "script.en.md").write_text("Text [SRC-001] [Q-001] [C-001]")
    (tmp_path / "sources.yaml").write_text("- id: SRC-001\n")
    (tmp_path / "quotes.yaml").write_text("""- id: Q-001
  source_id: SRC-001
  original_text: text
  translation: text
  locator: p. 1
  status: resolved
""")
    (tmp_path / "claims.yaml").write_text("- id: C-001\n  status: deferred\n")
    assert validate_episode(tmp_path) == []
