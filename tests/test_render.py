from pathlib import Path

from barbero_scripts.render import validate_episode


def write_episode(tmp_path: Path, decision: str = "retain-original") -> None:
    (tmp_path / "transcript.it.md").write_text("## U-00001 · original 00:01\n\nTesto")
    (tmp_path / "sources.yaml").write_text("- id: SRC-001\n")
    (tmp_path / "claims.yaml").write_text(
        "- id: C-001\n  transcript: [U-00001]\n  supporting_sources: [SRC-001]\n"
    )
    (tmp_path / "quotes.yaml").write_text(
        "- id: Q-001\n"
        "  barbero_utterances: [U-00001]\n"
        "  source_id: SRC-001\n"
        "  quotation_kind: direct\n"
        "  verdict: confirmed\n"
        "  source_replacement: eligible\n"
        "  translation: Verified words.\n"
    )
    (tmp_path / "accuracy-notes.yaml").write_text(
        "- id: N-001\n"
        "  transcript: [U-00001]\n"
        "  claim_ids: [C-001]\n"
        "  quotation_ids: [Q-001]\n"
        "  source_ids: [SRC-001]\n"
        "  category: factual-error\n"
        "  original_assertion: Original.\n"
        "  proposed_correction: Corrected.\n"
        f"  decision: {decision}\n"
    )
    (tmp_path / "script.translation.en.md").write_text(
        "<!-- transcript: U-00001–U-00001; omissions: none -->\nVerified words. [Q-001]"
    )
    (tmp_path / "translation.utterances.en.yaml").write_text("- id: U-00001\n  text: Original.\n")
    (tmp_path / "script.translation.assembled.en.md").write_text(
        "<!-- transcript: U-00001–U-00001; omissions: none -->\nVerified words. [Q-001]"
    )


def test_validation_accepts_applied_correction(tmp_path: Path) -> None:
    write_episode(tmp_path, "apply")
    text = "Verified words. Corrected. [Q-001] [N-001]"
    (tmp_path / "script.corrected.en.md").write_text(text)
    (tmp_path / "script.spoken.en.md").write_text(text)
    (tmp_path / "script.tense.en.md").write_text(text)
    (tmp_path / "script.en.md").write_text(text)
    assert validate_episode(tmp_path) == []


def test_validation_blocks_downstream_scripts_while_pending(tmp_path: Path) -> None:
    write_episode(tmp_path, "pending")
    (tmp_path / "script.corrected.en.md").write_text("Draft. [Q-001]")
    assert (
        "corrected and final scripts are blocked by pending accuracy decisions"
        in validate_episode(tmp_path)
    )


def test_validation_requires_translation_before_accuracy_review(tmp_path: Path) -> None:
    write_episode(tmp_path)
    (tmp_path / "script.translation.en.md").unlink()
    assert "accuracy review requires script.translation.en.md" in validate_episode(tmp_path)


def test_validation_requires_every_utterance_translation(tmp_path: Path) -> None:
    write_episode(tmp_path)
    (tmp_path / "translation.utterances.en.yaml").write_text("[]\n")
    assert "utterance translations do not exactly match transcript ID order" in validate_episode(
        tmp_path
    )


def test_validation_rejects_removed_assessment_field(tmp_path: Path) -> None:
    write_episode(tmp_path)
    path = tmp_path / "accuracy-notes.yaml"
    path.write_text(path.read_text() + "  assessment: Extra authority.\n")
    assert "accuracy note N-001 uses removed field assessment" in validate_episode(tmp_path)


def test_validation_rejects_marker_for_retained_note(tmp_path: Path) -> None:
    write_episode(tmp_path, "retain-original")
    text = "Verified words. Original. [Q-001] [N-001]"
    (tmp_path / "script.corrected.en.md").write_text(text)
    (tmp_path / "script.spoken.en.md").write_text(text)
    (tmp_path / "script.tense.en.md").write_text(text)
    (tmp_path / "script.en.md").write_text(text)
    assert "corrected script applies retained-original note N-001" in validate_episode(tmp_path)


def test_validation_rejects_invalid_replacement_combination(tmp_path: Path) -> None:
    write_episode(tmp_path)
    path = tmp_path / "quotes.yaml"
    path.write_text(
        path.read_text().replace("quotation_kind: direct", "quotation_kind: paraphrase")
    )
    assert "quotation Q-001 cannot replace paraphrase wording" in validate_episode(tmp_path)


def test_validation_allows_recoverable_composite_replacement(tmp_path: Path) -> None:
    write_episode(tmp_path)
    path = tmp_path / "quotes.yaml"
    path.write_text(path.read_text().replace("quotation_kind: direct", "quotation_kind: composite"))
    assert validate_episode(tmp_path) == []


def test_validation_requires_eligible_quote_wording(tmp_path: Path) -> None:
    write_episode(tmp_path)
    path = tmp_path / "script.translation.en.md"
    path.write_text(path.read_text().replace("Verified words.", "A loose rendering."))
    assert "translation does not use eligible wording for Q-001" in validate_episode(tmp_path)


def test_validation_rejects_italian_quotation_translation(tmp_path: Path) -> None:
    write_episode(tmp_path)
    path = tmp_path / "quotes.yaml"
    path.write_text(
        path.read_text().replace(
            "translation: Verified words.",
            "translation: Con i cechi ritorna anche il terrore nella città.",
        )
    )
    assert "quotation Q-001 translation is not English" in validate_episode(tmp_path)


def test_validation_preserves_markers_during_polishing(tmp_path: Path) -> None:
    write_episode(tmp_path, "apply")
    (tmp_path / "script.corrected.en.md").write_text("Verified words. Corrected. [Q-001] [N-001]")
    (tmp_path / "script.spoken.en.md").write_text("Verified words. Corrected. [Q-001] [N-001]")
    (tmp_path / "script.tense.en.md").write_text("Verified words. Corrected. [Q-001] [N-001]")
    (tmp_path / "script.en.md").write_text("Verified words. Corrected. [N-001]")
    assert "final script does not preserve tense-reviewed quotation markers" in validate_episode(
        tmp_path
    )
