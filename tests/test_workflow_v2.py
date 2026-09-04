from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from barbero_scripts.models import Episode
from barbero_scripts.transcript import Utterance, Word, deepgram_options
from barbero_scripts.workflow import (
    apply_content_corrections,
    apply_listener_review,
    initialize_transcript_uncertainties,
    text_hash,
    validate_content_queue,
    validate_transcript_uncertainties,
)


def test_keyterms_are_repeated_plain_values() -> None:
    episode = Episode("x", 1, "x", Path("a"), Path("b"), keyterms=("one", "two"))
    assert deepgram_options(episode)["keyterm"] == ["one", "two"]


def test_acoustic_uncertainty_preserves_word_evidence(tmp_path: Path) -> None:
    word = Word("Laud", 1.1, 1.4, 11.1, 11.4, 0.5)
    utterance = Utterance("U-00001", 1, 2, 11, 12, "Laud", 0.9, words=(word,))
    path = tmp_path / "transcript-uncertainties.yaml"
    initialize_transcript_uncertainties(path, [utterance], "fingerprint")
    queue = yaml.safe_load(path.read_text())
    assert queue["detection_status"] == "acoustic-complete"
    assert queue["items"][0]["resolution"]["status"] == "pending"
    assert queue["items"][0]["reasons"][0]["words"][0]["original_start"] == 11.1
    assert validate_transcript_uncertainties(queue, [utterance], "other") == [
        "transcript uncertainties has a stale transcription fingerprint"
    ]


def test_semantic_only_uncertainty_is_pending(tmp_path: Path) -> None:
    utterance = Utterance("U-00001", 1, 2, 11, 12, "Nel 1637.", 0.99, flags=("date",))
    path = tmp_path / "transcript-uncertainties.yaml"
    initialize_transcript_uncertainties(path, [utterance], "fingerprint")
    item = yaml.safe_load(path.read_text())["items"][0]
    assert item["reasons"] == [
        {
            "kind": "semantic",
            "category": "date",
            "detail": "Contextual verification required for date.",
        }
    ]
    assert item["resolution"]["status"] == "pending"


def _write_content_fixture(directory: Path) -> str:
    base = (
        "# Faithful\n\n## 1. One\n\n"
        "<!-- chapter: CH-001; transcript: U-00001–U-00001 -->\n\nOld words.\n"
    )
    (directory / "script.translation.faithful.en.md").write_text(base)
    (directory / "quotes.yaml").write_text("- id: Q-001\n")
    current = "Old words."
    queue = {
        "schema_version": 1,
        "base_script": {
            "path": "script.translation.faithful.en.md",
            "sha256": text_hash(base),
        },
        "items": [
            {
                "id": "CC-001",
                "issue_types": ["quotation"],
                "target": {
                    "chapter_id": "CH-001",
                    "transcript": ["U-00001"],
                    "current_text": current,
                    "current_text_sha256": text_hash(current),
                },
                "proposed_text": "New “exact words.”",
                "reason": "Use the source wording.",
                "evidence_summary": "Primary source.",
                "references": {
                    "quotations": ["Q-001"],
                    "claims": [],
                    "sources": [],
                },
                "recommendation": "apply",
                "protected_quote_spans": ["exact words"],
                "decision": "accept",
                "decision_note": None,
            }
        ],
    }
    (directory / "content-corrections.yaml").write_text(
        yaml.safe_dump(queue, sort_keys=False, allow_unicode=True)
    )
    return base


def test_content_application_is_exact_and_marked(tmp_path: Path) -> None:
    _write_content_fixture(tmp_path)
    assert validate_content_queue(tmp_path) == []
    apply_content_corrections(tmp_path)
    output = (tmp_path / "script.content.en.md").read_text()
    assert "New “exact words.”" in output
    assert "<!-- content-correction: CC-001 -->" in output


def test_content_application_blocks_pending_and_overlap(tmp_path: Path) -> None:
    _write_content_fixture(tmp_path)
    path = tmp_path / "content-corrections.yaml"
    queue = yaml.safe_load(path.read_text())
    queue["items"][0]["decision"] = "pending"
    path.write_text(yaml.safe_dump(queue, sort_keys=False))
    with pytest.raises(ValueError, match="pending content decisions"):
        apply_content_corrections(tmp_path)


def test_listener_application_propagates_audience_title(tmp_path: Path) -> None:
    spoken = (
        "# Old public title\n\n## 1. One\n\n"
        "<!-- chapter: CH-001; transcript: U-00001–U-00001 -->\n\nDense words.\n"
    )
    (tmp_path / "script.spoken.en.md").write_text(spoken)
    (tmp_path / "quotes.yaml").write_text("[]\n")
    (tmp_path / "episode.yaml").write_text(
        "workflow_version: 2\ntitle: Titolo italiano\naudience_title: null\n"
    )
    queue = {
        "schema_version": 1,
        "base_script": {"path": "script.spoken.en.md", "sha256": text_hash(spoken)},
        "episode_assessment": {
            "must_understand": ["The point"],
            "must_remember": ["The scene"],
            "experience": ["The return"],
            "argument_or_narrative_spine": "A test.",
            "strengths_to_preserve": ["The scene"],
        },
        "recommendations": [
            {
                "id": "ER-001",
                "issue_type": "title-accessibility",
                "listener_need": "remember",
                "severity": "recommended",
                "outline_sections": [1],
                "target": {
                    "kind": "title",
                    "current_text": None,
                    "current_text_sha256": text_hash(""),
                },
                "proposed_text": "A Clear English Title",
                "reason": "Lead with the subject.",
                "preserves": ["Italian source title"],
                "quotation_refs": [],
                "decision": "accept",
                "decision_note": None,
            }
        ],
    }
    (tmp_path / "listener-review.yaml").write_text(
        yaml.safe_dump(queue, sort_keys=False, allow_unicode=True)
    )
    apply_listener_review(tmp_path)
    metadata = yaml.safe_load((tmp_path / "episode.yaml").read_text())
    assert metadata["title"] == "Titolo italiano"
    assert metadata["audience_title"] == "A Clear English Title"
    assert (tmp_path / "script.editorial.en.md").read_text().startswith("# A Clear English Title")
