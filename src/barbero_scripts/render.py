from __future__ import annotations

import re
from dataclasses import asdict
from pathlib import Path
from typing import Any

import yaml

from .audio import load_edit_segments
from .models import Episode
from .transcript import apply_corrections, load_corrections, utterances_from_deepgram
from .util import read_json, write_json

MARKER = re.compile(r"\[(SRC|Q|C|N)-(\d{3})\]")
TRANSCRIPT_ID = re.compile(r"U-\d{5}")
TRANSCRIPT_RANGE = re.compile(r"^(U-\d{5})(?:[–-](U-\d{5}))?$")
QUOTE_KINDS = {"direct", "near-direct", "paraphrase", "slogan", "composite"}
QUOTE_VERDICTS = {
    "confirmed",
    "confirmed-in-substance",
    "misattributed",
    "composite",
    "unresolved",
}
SOURCE_REPLACEMENTS = {"eligible", "not-applicable", "unavailable"}
NOTE_CATEGORIES = {
    "factual-error",
    "misleading-compression",
    "disputed",
    "material-uncertainty",
}
DECISIONS = {"pending", "apply", "retain-original"}
COVERAGE = re.compile(r"<!-- transcript: (U-\d{5})[–-](U-\d{5}); omissions: ([^>]+) -->")
ITALIAN_FUNCTION_WORDS = {
    "anche",
    "che",
    "con",
    "della",
    "delle",
    "gli",
    "nella",
    "non",
    "sono",
    "una",
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


def _load_records(path: Path, label: str, errors: list[str]) -> dict[str, dict[str, Any]]:
    if not path.exists():
        errors.append(f"missing {path.name}")
        return {}
    value = yaml.safe_load(path.read_text(encoding="utf-8")) or []
    if not isinstance(value, list):
        errors.append(f"{path.name} must contain a list")
        return {}
    result: dict[str, dict[str, Any]] = {}
    for item in value:
        if not isinstance(item, dict) or "id" not in item:
            errors.append(f"{path.name} contains a record without an id")
            continue
        identifier = str(item["id"])
        if identifier in result:
            errors.append(f"duplicate {label} {identifier}")
        result[identifier] = item
    return result


def _references(value: Any, prefix: str) -> set[str]:
    if isinstance(value, str):
        return set(re.findall(rf"{prefix}-\d{{3}}", value))
    if isinstance(value, list):
        return {reference for item in value for reference in _references(item, prefix)}
    return set()


def _validate_transcript_references(
    records: dict[str, dict[str, Any]], transcript_ids: set[str], errors: list[str]
) -> None:
    for identifier, item in records.items():
        for value in item.values():
            if not isinstance(value, (str, list)):
                continue
            for token in value if isinstance(value, list) else [value]:
                if not isinstance(token, str) or not token.startswith("U-"):
                    continue
                match = TRANSCRIPT_RANGE.fullmatch(token)
                if not match:
                    errors.append(f"{identifier} has invalid transcript reference {token}")
                    continue
                for endpoint in filter(None, match.groups()):
                    if endpoint not in transcript_ids:
                        errors.append(
                            f"{identifier} references missing transcript utterance {endpoint}"
                        )


def _markers(text: str, prefixes: set[str]) -> set[str]:
    return {
        f"{match.group(1)}-{match.group(2)}"
        for match in MARKER.finditer(text)
        if match.group(1) in prefixes
    }


def _validate_coverage(text: str, transcript_ids: set[str], errors: list[str]) -> None:
    sections = list(COVERAGE.finditer(text))
    if not sections:
        errors.append("translation has no section-level transcript coverage")
        return
    expected = sorted(int(identifier[2:]) for identifier in transcript_ids)
    covered: set[int] = set()
    for section in sections:
        start, end = (int(value[2:]) for value in section.group(1, 2))
        if start > end:
            errors.append(f"translation has reversed coverage U-{start:05d}–U-{end:05d}")
            continue
        covered.update(range(start, end + 1))
        omissions = section.group(3).strip()
        if omissions != "none" and "|" not in omissions:
            errors.append(f"translation omission lacks a permitted reason: {omissions}")
    missing = [number for number in expected if number not in covered]
    if missing:
        errors.append(
            "translation coverage misses " + ", ".join(f"U-{number:05d}" for number in missing)
        )


def _looks_italian(text: str) -> bool:
    words = set(re.findall(r"[a-zàèéìòù]+", text.lower()))
    return len(words & ITALIAN_FUNCTION_WORDS) >= 3


def validate_episode(directory: Path) -> list[str]:
    errors: list[str] = []
    transcript_path = directory / "transcript.it.md"
    if not transcript_path.exists():
        return ["missing transcript.it.md"]
    transcript = transcript_path.read_text(encoding="utf-8")
    if "[REVIEW:" in transcript:
        errors.append("transcript contains unresolved review flags")
    transcript_ids = set(TRANSCRIPT_ID.findall(transcript))

    staged_schema = (directory / "accuracy-notes.yaml").exists() or (
        directory / "script.translation.en.md"
    ).exists()
    if (directory / "accuracy-notes.yaml").exists() and not (
        directory / "script.translation.en.md"
    ).exists():
        errors.append("accuracy review requires script.translation.en.md")
    ledgers = {
        "SRC": _load_records(directory / "sources.yaml", "source", errors),
        "Q": _load_records(directory / "quotes.yaml", "quotation", errors),
        "C": _load_records(directory / "claims.yaml", "claim", errors),
        "N": _load_records(directory / "accuracy-notes.yaml", "accuracy note", errors)
        if (directory / "accuracy-notes.yaml").exists()
        else {},
    }
    for records in ledgers.values():
        _validate_transcript_references(records, transcript_ids, errors)

    for prefix in ("Q", "C"):
        for identifier, item in ledgers[prefix].items():
            if staged_schema and "script_treatment" in item:
                errors.append(f"{identifier} uses removed field script_treatment")
            for source_id in _references(item, "SRC"):
                if source_id not in ledgers["SRC"]:
                    errors.append(f"{identifier} references missing source {source_id}")

    for identifier, item in ledgers["Q"].items():
        if not staged_schema:
            continue
        kind = item.get("quotation_kind")
        verdict = item.get("verdict")
        replacement = item.get("source_replacement")
        translation = item.get("translation")
        if kind not in QUOTE_KINDS:
            errors.append(f"quotation {identifier} has invalid quotation_kind")
        if verdict not in QUOTE_VERDICTS:
            errors.append(f"quotation {identifier} has invalid verdict")
        if replacement not in SOURCE_REPLACEMENTS:
            errors.append(f"quotation {identifier} has invalid source_replacement")
        if translation and _looks_italian(str(translation)):
            errors.append(f"quotation {identifier} translation is not English")
        if (
            item.get("original_language") == "en"
            and item.get("original_text")
            and translation != item.get("original_text")
        ):
            errors.append(f"quotation {identifier} English translation differs from original")
        if kind == "paraphrase" and replacement == "eligible":
            errors.append(f"quotation {identifier} cannot replace {kind} wording")
        if replacement == "eligible" and not translation:
            errors.append(f"quotation {identifier} has no replacement translation")

    for identifier, item in ledgers["N"].items():
        if "assessment" in item:
            errors.append(f"accuracy note {identifier} uses removed field assessment")
        if not item.get("proposed_correction"):
            errors.append(f"accuracy note {identifier} has no proposed_correction")
        if item.get("category") not in NOTE_CATEGORIES:
            errors.append(f"accuracy note {identifier} has invalid category")
        if item.get("decision") not in DECISIONS:
            errors.append(f"accuracy note {identifier} has invalid decision")
        for prefix in ("C", "Q", "SRC"):
            for reference in _references(item, prefix):
                if reference not in ledgers[prefix]:
                    errors.append(f"accuracy note {identifier} references missing {reference}")

    paths = {
        "assembled": directory / "script.translation.assembled.en.md",
        "translation": directory / "script.translation.en.md",
        "corrected": directory / "script.corrected.en.md",
        "spoken": directory / "script.spoken.en.md",
        "final": directory / "script.en.md",
    }
    texts = {
        name: path.read_text(encoding="utf-8") for name, path in paths.items() if path.exists()
    }
    utterance_path = directory / "translation.utterances.en.yaml"
    if staged_schema:
        utterance_records = _load_records(utterance_path, "utterance translation", errors)
        utterance_ids = list(utterance_records)
        expected_ids = sorted(transcript_ids)
        if utterance_ids != expected_ids:
            errors.append("utterance translations do not exactly match transcript ID order")
        for identifier, item in utterance_records.items():
            if not item.get("text"):
                errors.append(f"utterance translation {identifier} has no text")
        if "assembled" not in texts:
            errors.append("missing script.translation.assembled.en.md")
        else:
            _validate_coverage(texts["assembled"], transcript_ids, errors)
    legacy_final = "Legacy pre-staged adaptation" in texts.get("final", "")
    if "final" in texts and not legacy_final and "spoken" not in texts:
        errors.append("final script requires script.spoken.en.md")
    if "translation" in texts:
        _validate_coverage(texts["translation"], transcript_ids, errors)
        for identifier, item in ledgers["Q"].items():
            replacement = item.get("translation")
            if (
                item.get("source_replacement") == "eligible"
                and replacement
                and str(replacement) not in texts["translation"]
            ):
                errors.append(f"translation does not use eligible wording for {identifier}")
    if "assembled" in texts and "translation" in texts:
        for prefix, label in (("Q", "quotation"), ("C", "claim")):
            if _markers(texts["assembled"], {prefix}) != _markers(texts["translation"], {prefix}):
                errors.append(f"translation does not preserve assembled {label} markers")
    pending = {key for key, item in ledgers["N"].items() if item.get("decision") == "pending"}
    staged = "translation" in texts
    if pending and ("corrected" in texts or (staged and "final" in texts)):
        errors.append("corrected and final scripts are blocked by pending accuracy decisions")

    for stage, text in texts.items():
        for match in MARKER.finditer(text):
            identifier = f"{match.group(1)}-{match.group(2)}"
            if identifier not in ledgers[match.group(1)]:
                errors.append(f"{stage} script marker {identifier} has no ledger entry")

    applied = {key for key, item in ledgers["N"].items() if item.get("decision") == "apply"}
    retained = {
        key for key, item in ledgers["N"].items() if item.get("decision") == "retain-original"
    }
    for stage in ("corrected", "spoken", "final"):
        if stage not in texts:
            continue
        if stage == "final" and ("corrected" not in texts or legacy_final):
            continue
        note_markers = _markers(texts[stage], {"N"})
        for identifier in sorted(applied - note_markers):
            errors.append(f"{stage} script is missing applied marker {identifier}")
        for identifier in sorted(retained & note_markers):
            errors.append(f"{stage} script applies retained-original note {identifier}")

    if (
        "translation" in texts
        and "corrected" in texts
        and _markers(texts["translation"], {"Q"}) != _markers(texts["corrected"], {"Q"})
    ):
        errors.append("corrected script does not preserve quotation markers")
    if "corrected" in texts and "spoken" in texts and "final" in texts and not legacy_final:
        for prefix, label in (("Q", "quotation"), ("C", "claim"), ("N", "correction")):
            if _markers(texts["corrected"], {prefix}) != _markers(texts["spoken"], {prefix}):
                errors.append(f"spoken script does not preserve {label} markers")
            if _markers(texts["spoken"], {prefix}) != _markers(texts["final"], {prefix}):
                errors.append(f"final script does not preserve spoken {label} markers")
    return errors
