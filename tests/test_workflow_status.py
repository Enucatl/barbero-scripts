from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest
import yaml

from barbero_scripts.cli import main
from barbero_scripts.workflow import (
    WorkflowStatus,
    research_audit_hashes,
    validate_research_audit,
    validate_v2_episode,
    workflow_state,
)


def _write_yaml(path: Path, value: object) -> None:
    path.write_text(yaml.safe_dump(value, sort_keys=False), encoding="utf-8")


def _prepared_episode(directory: Path) -> Path:
    work = directory / "work"
    work.mkdir()
    _write_yaml(
        directory / "episode.yaml",
        {
            "workflow_version": 2,
            "slug": "001-test",
            "number": 1,
            "title": "Test",
            "audience_title": None,
            "source": str(directory / "source.wav"),
            "work_dir": str(work),
            "selected_speaker": "SPEAKER_00",
        },
    )
    for name in ("edit-map.json", "deepgram.json", "transcription-manifest.json"):
        (work / name).write_text("{}\n", encoding="utf-8")
    return work


def test_status_json_contract_and_text_share_one_result(tmp_path: Path) -> None:
    state = workflow_state(tmp_path)

    assert state == WorkflowStatus(
        "initialization", "machine", "initialize episode", (), ("episode.yaml",)
    )
    assert json.loads(json.dumps(state.to_dict()))["stage"] == "initialization"
    assert state.render() == "next machine action: initialize episode"


def test_cli_text_and_json_status_parity(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    state = workflow_state(tmp_path)
    monkeypatch.setattr(sys, "argv", ["barbero", "status", str(tmp_path)])
    main()
    assert capsys.readouterr().out.strip() == state.render()

    monkeypatch.setattr(sys, "argv", ["barbero", "status", str(tmp_path), "--json"])
    main()
    assert json.loads(capsys.readouterr().out) == state.to_dict()


def test_acoustic_detection_requires_agent_before_human_queue(tmp_path: Path) -> None:
    _prepared_episode(tmp_path)
    queue = {
        "schema_version": 1,
        "transcription_fingerprint": "fixture",
        "detection_status": "acoustic-complete",
        "items": [
            {
                "id": "TU-001",
                "resolution": {"status": "pending", "resolved_text": None},
            }
        ],
    }
    _write_yaml(tmp_path / "transcript-uncertainties.yaml", queue)

    assert workflow_state(tmp_path).stage == "semantic_transcript_review"
    assert workflow_state(tmp_path).kind == "agent"
    queue["detection_status"] = "complete"
    _write_yaml(tmp_path / "transcript-uncertainties.yaml", queue)
    assert workflow_state(tmp_path).stage == "transcript_review"
    assert workflow_state(tmp_path).kind == "human"


def _research_ready_episode(directory: Path) -> None:
    _prepared_episode(directory)
    _write_yaml(
        directory / "transcript-uncertainties.yaml",
        {
            "schema_version": 1,
            "transcription_fingerprint": "fixture",
            "detection_status": "complete",
            "items": [],
        },
    )
    (directory / "transcript.it.md").write_text(
        "# Test\n\n## U-00001 · original 00:00\n\nTesto.\n", encoding="utf-8"
    )
    _write_yaml(
        directory / "chapters.yaml",
        [{"id": "CH-001", "title": "Test", "start": "U-00001", "end": "U-00001"}],
    )
    (directory / "script.it.md").write_text("# Test\n", encoding="utf-8")
    _write_yaml(directory / "italian-review.yaml", {"utterances": [], "chapters": []})
    (directory / "outline.md").write_text("# Outline\n", encoding="utf-8")
    _write_yaml(directory / "quotes.yaml", [{"id": "Q-001", "status": "resolved"}])
    _write_yaml(directory / "claims.yaml", [{"id": "C-001", "status": "resolved"}])
    _write_yaml(directory / "sources.yaml", [])


def test_research_audit_hashes_gate_translation_and_detect_staleness(tmp_path: Path) -> None:
    _research_ready_episode(tmp_path)
    assert workflow_state(tmp_path).stage == "research_audit"
    audit = {
        "schema_version": 1,
        "artifact_hashes": research_audit_hashes(tmp_path),
        "verdict": "ready",
        "blocking_findings": [],
        "summary_counts": {"quotations_resolved": 1, "claims_resolved": 1},
    }
    _write_yaml(tmp_path / "research-audit.yaml", audit)
    assert validate_research_audit(tmp_path) == []
    assert workflow_state(tmp_path).stage == "translation"

    (tmp_path / "outline.md").write_text("# Changed\n", encoding="utf-8")
    assert validate_research_audit(tmp_path) == ["research audit artifact hashes are stale"]
    assert workflow_state(tmp_path).kind == "invalid"


def test_translation_is_blocked_by_missing_or_blocked_audit(tmp_path: Path) -> None:
    _write_yaml(tmp_path / "episode.yaml", {"workflow_version": 2, "audience_title": None})
    (tmp_path / "script.translation.faithful.en.md").write_text("# Translation\n")
    assert "missing research-audit.yaml" in validate_v2_episode(tmp_path)

    for name in ("script.it.md", "outline.md", "quotes.yaml", "claims.yaml", "sources.yaml"):
        (tmp_path / name).write_text("[]\n" if name.endswith(".yaml") else "# Test\n")
    _write_yaml(
        tmp_path / "research-audit.yaml",
        {
            "schema_version": 1,
            "artifact_hashes": research_audit_hashes(tmp_path),
            "verdict": "blocked",
            "blocking_findings": ["Q-001 unresolved"],
            "summary_counts": {},
        },
    )
    assert "faithful translation is blocked by research audit verdict" in validate_v2_episode(
        tmp_path
    )
