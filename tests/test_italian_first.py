from pathlib import Path

import yaml

from barbero_scripts.render import (
    _chapter_coverage,
    _validate_exact_coverage,
    assemble_italian_script,
    assemble_naturalness_chapters,
    assemble_tense_chapters,
    finalize_consistency,
    initialize_italian_review,
    initialize_naturalness_chapters,
    initialize_tense_chapters,
    validate_episode,
)


def test_exact_coverage_rejects_gap_overlap_reversal_and_duplicate() -> None:
    expected = [f"U-{number:05d}" for number in range(1, 5)]
    cases = (
        [("CH-001", "U-00001", "U-00002"), ("CH-002", "U-00004", "U-00004")],
        [("CH-001", "U-00001", "U-00003"), ("CH-002", "U-00003", "U-00004")],
        [("CH-001", "U-00002", "U-00001"), ("CH-002", "U-00003", "U-00004")],
        [("CH-001", "U-00001", "U-00002"), ("CH-001", "U-00003", "U-00004")],
    )
    for chapters in cases:
        errors: list[str] = []
        _validate_exact_coverage(chapters, expected, "stage", errors)
        assert errors


def _write_complete_episode(directory: Path) -> None:
    transcript = """# Test — Italian transcript

## U-00001 · original 00:01

Dice parole contestuali.

## U-00002 · original 00:02

Poi conclude.
"""
    directory.joinpath("transcript.it.md").write_text(transcript)
    chapter = "<!-- chapter: CH-001; transcript: U-00001–U-00002 -->"
    markers = "[Q-001] [C-001]"
    directory.joinpath("script.it.md").write_text(
        f"# Test — copione italiano\n\n## 1. Inizio\n\n{chapter}\n\n"
        "Dice parole contestuali. Poi conclude.\n\n"
        f"<!-- research: {markers} -->\n"
    )
    directory.joinpath("italian-review.yaml").write_text(
        "utterances:\n"
        "  - id: U-00001\n    reviewed_audio: true\n"
        "  - id: U-00002\n    reviewed_audio: true\n"
        "chapters:\n  - id: CH-001\n    complete_ordered_coverage: true\n"
    )
    directory.joinpath("outline.md").write_text("# Outline\n")
    directory.joinpath("sources.yaml").write_text("- id: SRC-001\n")
    directory.joinpath("quotes.yaml").write_text(
        "- id: Q-001\n"
        "  barbero_utterances: [U-00001]\n"
        "  source_id: SRC-001\n"
        "  quotation_kind: direct\n"
        "  verdict: confirmed\n"
        "  source_replacement: eligible\n"
        "  translation: Authoritative words.\n"
    )
    directory.joinpath("claims.yaml").write_text(
        "- id: C-001\n  transcript: [U-00002]\n  supporting_sources: [SRC-001]\n"
    )
    directory.joinpath("accuracy-notes.yaml").write_text("[]\n")
    faithful = f"# Test\n\n## 1. Beginning\n\n{chapter}\n\nContextual words. {markers}\n"
    translated = faithful.replace("Contextual words.", "Authoritative words.")
    directory.joinpath("script.translation.faithful.en.md").write_text(faithful)
    directory.joinpath("script.translation.en.md").write_text(translated)
    directory.joinpath("script.corrected.en.md").write_text(translated)
    naturalness = (
        "<!-- naturalness-reviewed: CH-001 -->\n"
        f"## 1. Beginning\n\n{chapter}\n\nAuthoritative words. {markers}\n"
    )
    directory.joinpath("naturalness").mkdir()
    directory.joinpath("naturalness/CH-001.md").write_text(naturalness)
    spoken = f"# Test\n\n{naturalness.split(chr(10), 1)[1]}"
    directory.joinpath("script.spoken.en.md").write_text(spoken)
    tense = naturalness.replace("naturalness-reviewed", "tense-reviewed")
    directory.joinpath("tense").mkdir()
    directory.joinpath("tense/CH-001.md").write_text(tense)
    tense_script = f"# Test\n\n{tense.split(chr(10), 1)[1]}"
    directory.joinpath("script.tense.en.md").write_text(tense_script)
    directory.joinpath("script.en.md").write_text(tense_script)


def test_complete_italian_first_episode_fixture(tmp_path: Path) -> None:
    _write_complete_episode(tmp_path)
    assert validate_episode(tmp_path) == []


def test_unresolved_italian_review_blocks_research(tmp_path: Path) -> None:
    _write_complete_episode(tmp_path)
    review = tmp_path / "italian-review.yaml"
    review.write_text(
        review.read_text().replace("reviewed_audio: true", "reviewed_audio: false", 1)
    )
    assert "research is blocked until the Italian checkpoint passes" in validate_episode(tmp_path)


def test_chapter_boundaries_must_match_italian(tmp_path: Path) -> None:
    _write_complete_episode(tmp_path)
    path = tmp_path / "script.corrected.en.md"
    path.write_text(path.read_text().replace("U-00002", "U-00001"))
    assert "corrected script chapter boundaries differ from Italian script" in validate_episode(
        tmp_path
    )


def test_quote_wording_is_delayed_until_replacement(tmp_path: Path) -> None:
    _write_complete_episode(tmp_path)
    path = tmp_path / "script.translation.faithful.en.md"
    path.write_text(path.read_text().replace("Contextual words.", "Authoritative words."))
    assert "faithful translation prematurely uses wording for Q-001" in validate_episode(tmp_path)


def test_faithful_translation_requires_manual_quote_review(tmp_path: Path) -> None:
    _write_complete_episode(tmp_path)
    path = tmp_path / "quotes.yaml"
    path.write_text(path.read_text() + "  human_reviewed: false\n")
    assert "faithful translation is blocked by unreviewed quotations: Q-001" in validate_episode(
        tmp_path
    )


def test_missing_naturalness_chapter_blocks_assembly(tmp_path: Path) -> None:
    _write_complete_episode(tmp_path)
    (tmp_path / "naturalness/CH-001.md").unlink()
    assert "missing naturalness output CH-001" in validate_episode(tmp_path)


def test_missing_tense_chapter_blocks_assembly(tmp_path: Path) -> None:
    _write_complete_episode(tmp_path)
    (tmp_path / "tense/CH-001.md").unlink()
    assert "missing tense output CH-001" in validate_episode(tmp_path)


def test_tense_chapter_round_trip(tmp_path: Path) -> None:
    _write_complete_episode(tmp_path)
    (tmp_path / "tense/CH-001.md").unlink()
    (tmp_path / "script.tense.en.md").unlink()
    initialize_tense_chapters(tmp_path)
    assemble_tense_chapters(tmp_path)
    assert "<!-- tense-reviewed: CH-001 -->" in (tmp_path / "tense/CH-001.md").read_text()
    assert "Authoritative words." in (tmp_path / "script.tense.en.md").read_text()


def test_tense_initialization_uses_corrected_script(tmp_path: Path) -> None:
    _write_complete_episode(tmp_path)
    (tmp_path / "script.corrected.en.md").write_text(
        (tmp_path / "script.corrected.en.md")
        .read_text()
        .replace("Authoritative words.", "Corrected source words.")
    )
    (tmp_path / "tense/CH-001.md").unlink()
    initialize_tense_chapters(tmp_path)
    assert "Corrected source words." in (tmp_path / "tense/CH-001.md").read_text()


def test_naturalness_initialization_uses_tense_script(tmp_path: Path) -> None:
    _write_complete_episode(tmp_path)
    (tmp_path / "script.tense.en.md").write_text(
        (tmp_path / "script.tense.en.md")
        .read_text()
        .replace("Authoritative words.", "Tense-reviewed source words.")
    )
    (tmp_path / "naturalness/CH-001.md").unlink()
    (tmp_path / "script.spoken.en.md").unlink()
    initialize_naturalness_chapters(tmp_path)
    assemble_naturalness_chapters(tmp_path)
    assert "Tense-reviewed source words." in (tmp_path / "naturalness/CH-001.md").read_text()
    assert "Tense-reviewed source words." in (tmp_path / "script.spoken.en.md").read_text()


def test_final_consistency_starts_from_spoken_script(tmp_path: Path) -> None:
    _write_complete_episode(tmp_path)
    (tmp_path / "script.spoken.en.md").write_text("# Test\n\nNatural spoken wording.\n")
    finalize_consistency(tmp_path)
    assert (tmp_path / "script.en.md").read_text() == "# Test\n\nNatural spoken wording.\n"


def test_chapter_parser_rejects_reversed_range() -> None:
    errors: list[str] = []
    _chapter_coverage(
        "## 1. Test\n\n<!-- chapter: CH-001; transcript: U-00002–U-00001 -->",
        "Italian script",
        errors,
    )
    assert "Italian script has reversed coverage U-00002–U-00001" in errors


def test_italian_assembly_is_verbatim_and_review_starts_approved(tmp_path: Path) -> None:
    tmp_path.joinpath("transcript.it.md").write_text(
        "# Titolo — Italian transcript\n\n"
        "## U-00001 · original 00:01\n\nBeh, io... io parto.\n\n"
        "## U-00002 · original 00:02\n\nE poi, insomma, torno.\n"
    )
    tmp_path.joinpath("chapters.yaml").write_text(
        "- id: CH-001\n  title: Partenza e ritorno\n  start: U-00001\n  end: U-00002\n"
    )
    assemble_italian_script(tmp_path)
    script = tmp_path.joinpath("script.it.md").read_text()
    assert "Beh, io... io parto. E poi, insomma, torno." in script

    initialize_italian_review(tmp_path)
    review = yaml.safe_load(tmp_path.joinpath("italian-review.yaml").read_text())
    assert [item["id"] for item in review["utterances"]] == ["U-00001", "U-00002"]
    assert all(item["reviewed_audio"] is True for item in review["utterances"])
