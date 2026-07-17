from __future__ import annotations

import re
from dataclasses import asdict
from pathlib import Path

import yaml

from .audio import load_edit_segments
from .models import Episode
from .transcript import apply_corrections, load_corrections, utterances_from_deepgram
from .util import read_json, write_json

MARKER = re.compile(r"\[(SRC|Q|C)-(\d{3})\]")
ANNOTATION = re.compile(r"\s*\[(?:SRC|Q|C)-\d{3}\]")
DEFERRED_TREATMENTS = {
    "paraphrase",
    "omit",
    "label-anecdotal",
    "qualify",
    "research-before-use",
}


def timestamp(seconds: float) -> str:
    total = round(seconds)
    return f"{total // 60:02d}:{total % 60:02d}"


def render_transcript(episode: Episode, destination: Path) -> None:
    payload = read_json(episode.work_dir / "deepgram.json")
    utterances = utterances_from_deepgram(
        payload, load_edit_segments(episode.work_dir / "edit-map.json")
    )
    corrected, diff = apply_corrections(
        utterances, load_corrections(episode.work_dir / "corrections.yaml")
    )
    lines = [
        f"# {episode.title} — Italian transcript",
        "",
        "<!-- Generated; correct through corrections.yaml. -->",
        "",
    ]
    for item in corrected:
        flags = " " + " ".join(f"[REVIEW:{flag}]" for flag in item.flags) if item.flags else ""
        lines.extend(
            [
                f"## {item.id} · cleaned {timestamp(item.start)} · "
                f"original {timestamp(item.original_start)}{flags}",
                "",
                item.text,
                "",
            ]
        )
    destination.write_text("\n".join(lines), encoding="utf-8")
    write_json(episode.work_dir / "correction-diff.json", diff)
    write_json(episode.work_dir / "utterances.json", [asdict(item) for item in corrected])


def render_recording(script: Path, destination: Path) -> None:
    text = script.read_text(encoding="utf-8")
    text = ANNOTATION.sub("", text)
    text = re.sub(r"^<!--.*?-->\s*", "", text, flags=re.MULTILINE)
    destination.write_text(text, encoding="utf-8")


def validate_episode(directory: Path) -> list[str]:
    errors: list[str] = []
    transcript = (directory / "transcript.it.md").read_text(encoding="utf-8")
    if "[REVIEW:" in transcript:
        errors.append("transcript contains unresolved review flags")
    ledgers: dict[str, dict[str, object]] = {}
    for prefix, name in (("SRC", "sources.yaml"), ("Q", "quotes.yaml"), ("C", "claims.yaml")):
        value = yaml.safe_load((directory / name).read_text(encoding="utf-8")) or []
        ledgers[prefix] = {str(item["id"]): item for item in value}
    script = (directory / "script.en.md").read_text(encoding="utf-8")
    for match in MARKER.finditer(script):
        identifier = f"{match.group(1)}-{match.group(2)}"
        if identifier not in ledgers[match.group(1)]:
            errors.append(f"script marker {identifier} has no ledger entry")
    for identifier, item in ledgers["Q"].items():
        required = ("source_id", "original_text", "translation", "locator", "status")
        if item.get("status") not in {"resolved", "deferred"}:
            errors.append(f"quotation {identifier} is neither resolved nor deferred")
        elif item.get("status") == "resolved" and any(not item.get(field) for field in required):
            errors.append(f"quotation {identifier} is incomplete")
        elif item.get("status") == "deferred" and (
            not item.get("deferred_reason")
            or item.get("script_treatment") not in DEFERRED_TREATMENTS
        ):
            errors.append(f"quotation {identifier} has no valid deferred treatment")
    for identifier, item in ledgers["C"].items():
        if item.get("status") not in {"resolved", "deferred"}:
            errors.append(f"claim {identifier} is neither resolved nor deferred")
        elif item.get("status") == "deferred" and (
            not item.get("deferred_reason")
            or item.get("script_treatment") not in DEFERRED_TREATMENTS
        ):
            errors.append(f"claim {identifier} has no valid deferred treatment")
    return errors
