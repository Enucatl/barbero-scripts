from __future__ import annotations

import hashlib
import re
from dataclasses import asdict
from pathlib import Path
from typing import Any

import yaml

from .transcript import Utterance

CONTENT_ISSUE_TYPES = {
    "quotation",
    "factual-error",
    "date",
    "name",
    "place",
    "attribution",
    "translation-ambiguity",
    "historical-context",
    "misleading-compression",
    "disputed",
    "material-uncertainty",
}
LISTENER_ISSUE_TYPES = {
    "title-accessibility",
    "hook",
    "spine",
    "cognitive-load",
    "orientation",
    "terminology",
    "proper-name-hierarchy",
    "callbacks",
    "quotation-audio",
    "lecture-residue",
    "cultural-assumptions",
    "buried-scenes",
    "climax-ending",
}
HUMAN_DECISIONS = {"pending", "accept", "reject"}
LISTENER_NEEDS = {"understand", "remember", "experience"}
PROHIBITED_PODCAST_LANGUAGE = (
    "but here's the twist",
    "here's where it gets interesting",
    "you won't believe",
    "let's dive in",
    "buckle up",
)
CHAPTER_HEADING = re.compile(r"^## \d+\.\s+.+$", re.MULTILINE)
CHAPTER_COVERAGE = re.compile(
    r"<!-- chapter: CH-\d{3}; transcript: U-\d{5}[–-]U-\d{5}(?:; omissions: [^>]+)? -->"
)
COVERAGE_RANGE = re.compile(r"<!-- chapter: (CH-\d{3}); transcript: (U-\d{5})[–-](U-\d{5})")
TRANSCRIPT_HEADING = re.compile(r"^## (U-\d{5})\b", re.MULTILINE)
QUOTED = re.compile(r"[\"“«](.+?)[\"”»]", re.DOTALL)
QUOTATION_TREATMENTS = {"exact-excerpt", "excerpt-with-paraphrase", "paraphrase"}
CONTENT_MARKER = re.compile(r"<!-- content-correction: (CC-\d{3}) -->")
TENSE_REVIEW = re.compile(r"<!-- tense-reviewed: (CH-\d{3}) -->\n?")
NATURALNESS_REVIEW = re.compile(r"<!-- naturalness-reviewed: (CH-\d{3}) -->\n?")


def text_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_yaml_mapping(path: Path) -> dict[str, Any]:
    value = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(value, dict):
        raise ValueError(f"{path.name} must contain a mapping")
    return value


def dump_yaml(path: Path, value: dict[str, Any]) -> None:
    path.write_text(
        yaml.safe_dump(value, sort_keys=False, allow_unicode=True, width=100),
        encoding="utf-8",
    )


def initialize_transcript_uncertainties(
    destination: Path,
    utterances: list[Utterance],
    transcription_fingerprint: str,
) -> None:
    if destination.exists():
        raise FileExistsError(f"uncertainty queue already exists: {destination}")
    items: list[dict[str, Any]] = []
    for utterance in utterances:
        low_words = [word for word in utterance.words if word.confidence < 0.65]
        entity_words = [
            word
            for index, word in enumerate(utterance.words)
            if index > 0 and word.text[:1].isupper() and word.confidence < 0.85
        ]
        semantic_flags = [
            flag for flag in utterance.flags if flag in {"date", "quotation", "named-entity"}
        ]
        if (
            utterance.confidence >= 0.80
            and not low_words
            and not entity_words
            and not semantic_flags
        ):
            continue
        evidence = low_words + [word for word in entity_words if word not in low_words]
        detail = "Low-confidence speech"
        if entity_words:
            detail = "Low-confidence likely critical entity"
        reasons: list[dict[str, Any]] = []
        if utterance.confidence < 0.80 or evidence:
            reasons.append(
                {
                    "kind": "acoustic",
                    "detail": detail,
                    "utterance_confidence": utterance.confidence,
                    "words": [asdict(word) for word in evidence],
                }
            )
        reasons.extend(
            {
                "kind": "semantic",
                "category": "name" if flag == "named-entity" else flag,
                "detail": f"Contextual verification required for {flag}.",
            }
            for flag in semantic_flags
        )
        items.append(
            {
                "id": f"TU-{len(items) + 1:03d}",
                "utterance_id": utterance.id,
                "timestamp": {
                    "cleaned_start": utterance.start,
                    "cleaned_end": utterance.end,
                    "original_start": utterance.original_start,
                    "original_end": utterance.original_end,
                },
                "current_text": utterance.text,
                "proposed_text": utterance.text,
                "reasons": reasons,
                "resolution": {"status": "pending", "resolved_text": None, "note": None},
            }
        )
    dump_yaml(
        destination,
        {
            "schema_version": 1,
            "transcription_fingerprint": transcription_fingerprint,
            "detection_status": "complete",
            "items": items,
        },
    )


def validate_transcript_uncertainties(
    queue: dict[str, Any],
    utterances: list[Utterance],
    transcription_fingerprint: str,
) -> list[str]:
    errors: list[str] = []
    if queue.get("schema_version") != 1:
        errors.append("transcript uncertainties has unsupported schema_version")
    if queue.get("transcription_fingerprint") != transcription_fingerprint:
        errors.append("transcript uncertainties has a stale transcription fingerprint")
    if queue.get("detection_status") != "complete":
        errors.append("transcript uncertainty detection is incomplete")
    known = {item.id: item for item in utterances}
    seen: set[str] = set()
    for item in queue.get("items", []):
        identifier = str(item.get("id", ""))
        utterance_id = str(item.get("utterance_id", ""))
        if not re.fullmatch(r"TU-\d{3}", identifier) or identifier in seen:
            errors.append(f"invalid or duplicate transcript uncertainty {identifier}")
        seen.add(identifier)
        if utterance_id not in known:
            errors.append(f"{identifier} references missing utterance {utterance_id}")
        elif item.get("current_text") != known[utterance_id].text:
            errors.append(f"{identifier} current_text is stale")
        reasons = item.get("reasons")
        if not isinstance(reasons, list) or not reasons:
            errors.append(f"{identifier} must have at least one reason")
        else:
            for reason in reasons:
                if not isinstance(reason, dict) or reason.get("kind") not in {
                    "acoustic",
                    "semantic",
                }:
                    errors.append(f"{identifier} has an invalid reason")
        resolution = item.get("resolution", {})
        status = resolution.get("status") if isinstance(resolution, dict) else None
        if status not in {"pending", "resolved"}:
            errors.append(f"{identifier} has invalid resolution status")
        if status == "resolved" and not isinstance(resolution.get("resolved_text"), str):
            errors.append(f"{identifier} resolved_text must contain the complete utterance")
        if status == "pending" and resolution.get("resolved_text") is not None:
            errors.append(f"{identifier} pending resolution must not have resolved_text")
    return errors


def resolve_utterances(
    utterances: list[Utterance], queue: dict[str, Any]
) -> tuple[list[Utterance], list[str]]:
    errors: list[str] = []
    resolutions: dict[str, str] = {}
    for item in queue.get("items", []):
        resolution = item.get("resolution", {})
        if resolution.get("status") == "pending":
            errors.append(f"pending transcript uncertainty {item.get('id')}")
        elif resolution.get("status") == "resolved":
            resolutions[str(item.get("utterance_id"))] = str(resolution.get("resolved_text"))
    if errors:
        return utterances, errors
    from dataclasses import replace

    return [
        replace(item, text=resolutions.get(item.id, item.text), flags=()) for item in utterances
    ], []


def _chapter_sections(text: str) -> dict[str, tuple[int, int]]:
    headings = list(CHAPTER_HEADING.finditer(text))
    sections: dict[str, tuple[int, int]] = {}
    for index, heading in enumerate(headings, 1):
        end = headings[index].start() if index < len(headings) else len(text)
        sections[f"CH-{index:03d}"] = (heading.start(), end)
    return sections


def _records(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    value = yaml.safe_load(path.read_text(encoding="utf-8")) or []
    return value if isinstance(value, list) else []


def _validate_base(
    queue: dict[str, Any], directory: Path, expected_path: str
) -> tuple[str, list[str]]:
    errors: list[str] = []
    base = queue.get("base_script", {})
    if not isinstance(base, dict) or base.get("path") != expected_path:
        return "", [f"base_script.path must be {expected_path}"]
    path = directory / expected_path
    if not path.exists():
        return "", [f"missing {expected_path}"]
    text = path.read_text(encoding="utf-8")
    if base.get("sha256") != text_hash(text):
        errors.append(f"{expected_path} has changed since the queue was created")
    return text, errors


def _validate_patch_items(
    queue: dict[str, Any],
    base_text: str,
    *,
    prefix: str,
    issue_types: set[str],
) -> list[str]:
    errors: list[str] = []
    sections = _chapter_sections(base_text)
    occupied: list[tuple[int, int, str]] = []
    seen: set[str] = set()
    for item in queue.get("items", queue.get("recommendations", [])):
        identifier = str(item.get("id", ""))
        if not re.fullmatch(rf"{prefix}-\d{{3}}", identifier) or identifier in seen:
            errors.append(f"invalid or duplicate patch id {identifier}")
        seen.add(identifier)
        kinds = item.get("issue_types", [item.get("issue_type")])
        if (
            not isinstance(kinds, list)
            or not kinds
            or any(kind not in issue_types for kind in kinds)
        ):
            errors.append(f"{identifier} has invalid issue type")
        if item.get("decision") not in HUMAN_DECISIONS:
            errors.append(f"{identifier} has invalid decision")
        if prefix == "CC" and item.get("recommendation") not in {"apply", "retain"}:
            errors.append(f"{identifier} has invalid recommendation")
        target = item.get("target", {})
        if not isinstance(target, dict):
            errors.append(f"{identifier} has invalid target")
            continue
        if prefix == "ER" and target.get("kind", "script") == "title":
            current = target.get("current_text")
            proposed = item.get("proposed_text")
            if not isinstance(current, (str, type(None))) or not isinstance(proposed, str):
                errors.append(f"{identifier} must contain exact current_text and proposed_text")
            elif target.get("current_text_sha256") != text_hash(current or ""):
                errors.append(f"{identifier} current_text hash is stale")
            if not item.get("reason"):
                errors.append(f"{identifier} has no reason")
            continue
        chapter_id = str(target.get("chapter_id", ""))
        if chapter_id not in sections:
            errors.append(f"{identifier} references missing chapter {chapter_id}")
            continue
        current = target.get("current_text")
        proposed = item.get("proposed_text")
        if not isinstance(current, str) or not isinstance(proposed, str):
            errors.append(f"{identifier} must contain exact current_text and proposed_text")
            continue
        if target.get("current_text_sha256") != text_hash(current):
            errors.append(f"{identifier} current_text hash is stale")
        start, end = sections[chapter_id]
        chapter = base_text[start:end]
        if chapter.count(current) != 1:
            errors.append(f"{identifier} current_text must match exactly once in {chapter_id}")
            continue
        absolute = (start + chapter.index(current), start + chapter.index(current) + len(current))
        heading_end = base_text.find("\n", start)
        if absolute[0] <= heading_end or CHAPTER_HEADING.search(current):
            errors.append(f"{identifier} may not alter a chapter heading")
        if CHAPTER_COVERAGE.search(current) or CHAPTER_COVERAGE.search(proposed):
            errors.append(f"{identifier} may not alter chapter coverage")
        for previous_start, previous_end, previous_id in occupied:
            if absolute[0] < previous_end and previous_start < absolute[1]:
                errors.append(f"{identifier} overlaps {previous_id}")
        occupied.append((*absolute, identifier))
        if not item.get("reason"):
            errors.append(f"{identifier} has no reason")
        if prefix == "CC":
            references = item.get("references", {})
            if not item.get("evidence_summary") or not isinstance(references, dict):
                errors.append(f"{identifier} has no evidence")
            for span in item.get("protected_quote_spans", []):
                if span not in proposed:
                    errors.append(f"{identifier} alters a protected quotation span")
    return errors


def validate_content_queue(directory: Path) -> list[str]:
    path = directory / "content-corrections.yaml"
    if not path.exists():
        return ["missing content-corrections.yaml"]
    queue = load_yaml_mapping(path)
    errors = [] if queue.get("schema_version") == 1 else ["unsupported content queue schema"]
    base, base_errors = _validate_base(queue, directory, "script.translation.faithful.en.md")
    errors.extend(base_errors)
    errors.extend(_validate_patch_items(queue, base, prefix="CC", issue_types=CONTENT_ISSUE_TYPES))
    quote_records = _records(directory / "quotes.yaml")
    quote_ids = {str(item.get("id")) for item in quote_records}
    claim_ids = {str(item.get("id")) for item in _records(directory / "claims.yaml")}
    source_ids = {str(item.get("id")) for item in _records(directory / "sources.yaml")}
    for quote in quote_records:
        if "human_reviewed" in quote:
            errors.append(f"quotation {quote.get('id')} uses removed field human_reviewed")
    represented: list[str] = []
    for item in queue.get("items", []):
        references = item.get("references", {})
        represented.extend(str(value) for value in references.get("quotations", []))
    for quote_id in sorted(quote_ids):
        if represented.count(quote_id) != 1:
            errors.append(f"quotation {quote_id} must appear exactly once in content corrections")
    if any(quote_id not in quote_ids for quote_id in represented):
        errors.append("content corrections reference an unknown quotation")
    for item in queue.get("items", []):
        references = item.get("references", {})
        for value in references.get("claims", []):
            if str(value) not in claim_ids:
                errors.append(f"{item.get('id')} references missing claim {value}")
        for value in references.get("sources", []):
            if str(value) not in source_ids:
                errors.append(f"{item.get('id')} references missing source {value}")
    return errors


def _apply_patches(queue: dict[str, Any], base_text: str, marker_label: str) -> str:
    changes: list[tuple[int, int, str]] = []
    sections = _chapter_sections(base_text)
    records = queue.get("items", queue.get("recommendations", []))
    for item in records:
        if item.get("decision") != "accept":
            continue
        target = item["target"]
        if target.get("kind", "script") == "title":
            continue
        chapter_start, chapter_end = sections[str(target["chapter_id"])]
        chapter = base_text[chapter_start:chapter_end]
        relative = chapter.index(target["current_text"])
        start = chapter_start + relative
        end = start + len(target["current_text"])
        replacement = item["proposed_text"] + f"\n<!-- {marker_label}: {item['id']} -->"
        changes.append((start, end, replacement))
    result = base_text
    for start, end, replacement in sorted(changes, reverse=True):
        result = result[:start] + replacement + result[end:]
    return result


def apply_content_corrections(directory: Path) -> None:
    errors = validate_content_queue(directory)
    queue = load_yaml_mapping(directory / "content-corrections.yaml")
    pending = [
        item.get("id") for item in queue.get("items", []) if item.get("decision") == "pending"
    ]
    if pending:
        errors.append("pending content decisions: " + ", ".join(map(str, pending)))
    if errors:
        raise ValueError("; ".join(errors))
    source = (directory / "script.translation.faithful.en.md").read_text(encoding="utf-8")
    output = _apply_patches(queue, source, "content-correction")
    if CHAPTER_HEADING.findall(output) != CHAPTER_HEADING.findall(source):
        raise ValueError("content corrections may not change chapter headings")
    if CHAPTER_COVERAGE.findall(output) != CHAPTER_COVERAGE.findall(source):
        raise ValueError("content corrections may not change chapter coverage")
    (directory / "script.content.en.md").write_text(output, encoding="utf-8")


def _validate_listener_quotes(directory: Path, queue: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    quotes = {str(item.get("id")): item for item in _records(directory / "quotes.yaml")}
    for item in queue.get("recommendations", []):
        refs = item.get("quotation_refs", [])
        proposed = str(item.get("proposed_text", ""))
        if item.get("issue_type") == "quotation-audio":
            if not refs:
                errors.append(f"{item.get('id')} quotation-audio item has no quotation reference")
            if item.get("quotation_treatment") not in QUOTATION_TREATMENTS:
                errors.append(f"{item.get('id')} has invalid quotation_treatment")
        for reference in refs:
            record = quotes.get(str(reference))
            if record is None:
                errors.append(f"{item.get('id')} references missing quotation {reference}")
                continue
            authoritative = str(record.get("translation") or record.get("original_text") or "")
            source_words = _lexical_words(authoritative)
            if item.get("issue_type") == "quotation-audio":
                target = item.get("target", {})
                target_words = _lexical_words(str(target.get("current_text", "")))
                cursor = 0
                for word in target_words:
                    if cursor < len(source_words) and word == source_words[cursor]:
                        cursor += 1
                if cursor != len(source_words):
                    errors.append(
                        f"{item.get('id')} target does not contain the full rendered quotation"
                    )
            for quoted in QUOTED.findall(proposed):
                quoted_words = _lexical_words(quoted)
                if not _contains_contiguous_words(source_words, quoted_words):
                    errors.append(f"{item.get('id')} alters authoritative quotation wording")
    return errors


def _lexical_words(text: str) -> list[str]:
    return [
        word.casefold() for word in re.findall(r"[^\W_]+(?:['’][^\W_]+)*", text, flags=re.UNICODE)
    ]


def _contains_contiguous_words(source: list[str], excerpt: list[str]) -> bool:
    if not excerpt:
        return False
    return any(
        source[start : start + len(excerpt)] == excerpt
        for start in range(len(source) - len(excerpt) + 1)
    )


def validate_listener_queue(directory: Path) -> list[str]:
    path = directory / "listener-review.yaml"
    if not path.exists():
        return ["missing listener-review.yaml"]
    queue = load_yaml_mapping(path)
    errors = [] if queue.get("schema_version") == 1 else ["unsupported listener queue schema"]
    base, base_errors = _validate_base(queue, directory, "script.spoken.en.md")
    errors.extend(base_errors)
    errors.extend(_validate_patch_items(queue, base, prefix="ER", issue_types=LISTENER_ISSUE_TYPES))
    assessment = queue.get("episode_assessment", {})
    required = {
        "must_understand",
        "must_remember",
        "experience",
        "argument_or_narrative_spine",
        "strengths_to_preserve",
    }
    if not isinstance(assessment, dict) or not required <= assessment.keys():
        errors.append("listener review has an incomplete episode assessment")
    for item in queue.get("recommendations", []):
        if item.get("listener_need") not in LISTENER_NEEDS:
            errors.append(f"{item.get('id')} has invalid listener_need")
        proposed = str(item.get("proposed_text", "")).casefold()
        if any(phrase in proposed for phrase in PROHIBITED_PODCAST_LANGUAGE):
            errors.append(f"{item.get('id')} uses prohibited stock-podcast language")
    errors.extend(_validate_listener_quotes(directory, queue))
    return errors


def apply_listener_review(directory: Path) -> None:
    errors = validate_listener_queue(directory)
    queue = load_yaml_mapping(directory / "listener-review.yaml")
    recommendations = queue.get("recommendations", [])
    pending = [item.get("id") for item in recommendations if item.get("decision") == "pending"]
    if pending:
        errors.append("pending listener decisions: " + ", ".join(map(str, pending)))
    metadata_path = directory / "episode.yaml"
    metadata = load_yaml_mapping(metadata_path)
    for item in recommendations:
        target = item.get("target", {})
        if target.get("kind") != "title" or item.get("decision") != "accept":
            continue
        if target.get("current_text") != metadata.get("audience_title") and item.get(
            "proposed_text"
        ) != metadata.get("audience_title"):
            errors.append(f"{item.get('id')} title target is stale")
    if errors:
        raise ValueError("; ".join(errors))
    source = (directory / "script.spoken.en.md").read_text(encoding="utf-8")
    output = _apply_patches(queue, source, "editorial-recommendation")
    if CHAPTER_HEADING.findall(output) != CHAPTER_HEADING.findall(source):
        raise ValueError("listener recommendations may not change chapter headings")
    if CHAPTER_COVERAGE.findall(output) != CHAPTER_COVERAGE.findall(source):
        raise ValueError("listener recommendations may not change chapter coverage")
    for item in recommendations:
        if item.get("target", {}).get("kind") == "title" and item.get("decision") == "accept":
            metadata["audience_title"] = item["proposed_text"]
    audience_title = metadata.get("audience_title")
    if not audience_title:
        raise ValueError("audience_title must be set before editorial application")
    lines = output.splitlines()
    if lines and lines[0].startswith("# "):
        lines[0] = f"# {audience_title}"
        output = "\n".join(lines) + ("\n" if source.endswith("\n") else "")
    dump_yaml(metadata_path, metadata)
    (directory / "script.editorial.en.md").write_text(output, encoding="utf-8")


def workflow_status(directory: Path) -> str:
    metadata = load_yaml_mapping(directory / "episode.yaml")
    if int(metadata.get("workflow_version", 1)) != 2:
        return "legacy workflow: run barbero validate"
    uncertainty = directory / "transcript-uncertainties.yaml"
    if not uncertainty.exists():
        return "next machine action: render transcript and uncertainty queue"
    queue = load_yaml_mapping(uncertainty)
    if any(
        item.get("resolution", {}).get("status") == "pending" for item in queue.get("items", [])
    ):
        return "human queue: transcription resolver (transcript-uncertainties.yaml)"
    if not (directory / "script.it.md").exists():
        return "next machine action: assemble Italian source"
    if not (directory / "content-corrections.yaml").exists():
        return "next machine action: research, translate, and propose content corrections"
    content = load_yaml_mapping(directory / "content-corrections.yaml")
    if any(item.get("decision") == "pending" for item in content.get("items", [])):
        return "human queue: content editor (content-corrections.yaml)"
    if not (directory / "script.content.en.md").exists():
        return "next machine action: apply content corrections"
    if not (directory / "script.spoken.en.md").exists():
        return "next machine action: tense and chapter-naturalness review"
    if not (directory / "listener-review.yaml").exists():
        return "next machine action: run whole-episode listener review"
    listener = load_yaml_mapping(directory / "listener-review.yaml")
    if any(item.get("decision") == "pending" for item in listener.get("recommendations", [])):
        return "human queue: listener editor (listener-review.yaml)"
    if not (directory / "script.editorial.en.md").exists():
        return "next machine action: apply listener review"
    if not (directory / "script.en.md").exists():
        return "next machine action: final consistency"
    return "workflow complete"


def _coverage(text: str) -> tuple[list[str], list[str]]:
    chapter_ids: list[str] = []
    utterance_ids: list[str] = []
    for chapter_id, start_id, end_id in COVERAGE_RANGE.findall(text):
        chapter_ids.append(chapter_id)
        start, end = int(start_id[2:]), int(end_id[2:])
        if start <= end:
            utterance_ids.extend(f"U-{number:05d}" for number in range(start, end + 1))
    return chapter_ids, utterance_ids


def validate_v2_episode(directory: Path) -> list[str]:
    errors: list[str] = []
    metadata = load_yaml_mapping(directory / "episode.yaml")
    if metadata.get("workflow_version") != 2:
        return ["episode is not workflow_version 2"]
    if "audience_title" not in metadata:
        errors.append("episode.yaml is missing audience_title")
    dependencies = {
        "script.translation.faithful.en.md": "script.it.md",
        "content-corrections.yaml": "script.translation.faithful.en.md",
        "script.content.en.md": "content-corrections.yaml",
        "script.tense.en.md": "script.content.en.md",
        "script.spoken.en.md": "script.tense.en.md",
        "listener-review.yaml": "script.spoken.en.md",
        "script.editorial.en.md": "listener-review.yaml",
        "script.en.md": "script.editorial.en.md",
    }
    for artifact, predecessor in dependencies.items():
        if (directory / artifact).exists() and not (directory / predecessor).exists():
            errors.append(f"{artifact} requires {predecessor}")
    uncertainty_path = directory / "transcript-uncertainties.yaml"
    if not uncertainty_path.exists():
        errors.append("missing transcript-uncertainties.yaml")
    else:
        queue = load_yaml_mapping(uncertainty_path)
        if queue.get("schema_version") != 1:
            errors.append("transcript uncertainties has unsupported schema_version")
        if not queue.get("transcription_fingerprint"):
            errors.append("transcript uncertainties has no transcription fingerprint")
        if queue.get("detection_status") != "complete":
            errors.append("transcript uncertainty detection is incomplete")
        for item in queue.get("items", []):
            resolution = item.get("resolution", {})
            if resolution.get("status") not in {"pending", "resolved"}:
                errors.append(f"{item.get('id')} has invalid resolution status")
            if not item.get("reasons"):
                errors.append(f"{item.get('id')} must have at least one reason")
            if resolution.get("status") == "resolved" and not isinstance(
                resolution.get("resolved_text"), str
            ):
                errors.append(f"{item.get('id')} resolved_text must contain the complete utterance")
        pending = any(
            item.get("resolution", {}).get("status") == "pending" for item in queue.get("items", [])
        )
        if pending and (directory / "script.it.md").exists():
            errors.append("Italian assembly is blocked by pending transcript uncertainties")
    transcript_path = directory / "transcript.it.md"
    if (
        transcript_path.exists()
        and "[REVIEW:" in transcript_path.read_text(encoding="utf-8")
        and (directory / "script.it.md").exists()
    ):
        errors.append("Italian assembly is blocked by unresolved transcript review flags")
    if transcript_path.exists() and (directory / "script.it.md").exists():
        transcript_ids = TRANSCRIPT_HEADING.findall(transcript_path.read_text(encoding="utf-8"))
        italian_text = (directory / "script.it.md").read_text(encoding="utf-8")
        chapter_ids, covered_ids = _coverage(italian_text)
        if chapter_ids != [f"CH-{number:03d}" for number in range(1, len(chapter_ids) + 1)]:
            errors.append("Italian script chapter IDs are not sequential")
        if covered_ids != transcript_ids:
            errors.append("Italian script does not have exact ordered utterance coverage")
    content_path = directory / "content-corrections.yaml"
    if content_path.exists():
        errors.extend(validate_content_queue(directory))
        content = load_yaml_mapping(content_path)
        pending = any(item.get("decision") == "pending" for item in content.get("items", []))
        if pending and (directory / "script.content.en.md").exists():
            errors.append("content application is blocked by pending decisions")
        if (directory / "script.content.en.md").exists() and not pending:
            expected = _apply_patches(
                content,
                (directory / "script.translation.faithful.en.md").read_text(encoding="utf-8"),
                "content-correction",
            )
            if (directory / "script.content.en.md").read_text(encoding="utf-8") != expected:
                errors.append("script.content.en.md is not the deterministic content application")
    listener_path = directory / "listener-review.yaml"
    if listener_path.exists():
        errors.extend(validate_listener_queue(directory))
        listener = load_yaml_mapping(listener_path)
        pending = any(
            item.get("decision") == "pending" for item in listener.get("recommendations", [])
        )
        if pending and (directory / "script.editorial.en.md").exists():
            errors.append("editorial application is blocked by pending listener decisions")
        if not pending and (directory / "script.editorial.en.md").exists():
            expected = _apply_patches(
                listener,
                (directory / "script.spoken.en.md").read_text(encoding="utf-8"),
                "editorial-recommendation",
            )
            if metadata.get("audience_title"):
                lines = expected.splitlines()
                if lines and lines[0].startswith("# "):
                    lines[0] = f"# {metadata['audience_title']}"
                    expected = "\n".join(lines) + (
                        "\n"
                        if (directory / "script.spoken.en.md").read_text().endswith("\n")
                        else ""
                    )
            if (directory / "script.editorial.en.md").read_text(encoding="utf-8") != expected:
                errors.append(
                    "script.editorial.en.md is not the deterministic listener application"
                )
    content_text = (
        (directory / "script.content.en.md").read_text(encoding="utf-8")
        if (directory / "script.content.en.md").exists()
        else ""
    )
    italian_coverage = (
        _coverage((directory / "script.it.md").read_text(encoding="utf-8"))[0:2]
        if (directory / "script.it.md").exists()
        else ([], [])
    )
    for stage in (
        "script.translation.faithful.en.md",
        "script.content.en.md",
        "script.tense.en.md",
        "script.spoken.en.md",
        "script.editorial.en.md",
        "script.en.md",
    ):
        path = directory / stage
        if (
            path.exists()
            and italian_coverage != ([], [])
            and _coverage(path.read_text(encoding="utf-8")) != italian_coverage
        ):
            errors.append(f"{stage} changes exact Italian chapter coverage")
    for stage in ("script.tense.en.md", "script.spoken.en.md", "script.editorial.en.md"):
        path = directory / stage
        if path.exists() and content_text:
            value = path.read_text(encoding="utf-8")
            if CHAPTER_HEADING.findall(value) != CHAPTER_HEADING.findall(content_text):
                errors.append(f"{stage} changes chapter headings")
            if CHAPTER_COVERAGE.findall(value) != CHAPTER_COVERAGE.findall(content_text):
                errors.append(f"{stage} changes chapter coverage")
    accepted_content = set()
    if content_path.exists():
        content = load_yaml_mapping(content_path)
        accepted_content = {
            str(item.get("id"))
            for item in content.get("items", [])
            if item.get("decision") == "accept"
        }
    for stage in ("script.content.en.md", "script.tense.en.md", "script.spoken.en.md"):
        path = directory / stage
        if path.exists() and accepted_content:
            markers = set(CONTENT_MARKER.findall(path.read_text(encoding="utf-8")))
            if markers != accepted_content:
                errors.append(f"{stage} does not preserve accepted content markers")
    chapter_ids = [
        f"CH-{index:03d}" for index, _ in enumerate(CHAPTER_HEADING.findall(content_text), 1)
    ]
    for folder, script_name, review_pattern, label in (
        ("tense", "script.tense.en.md", TENSE_REVIEW, "tense"),
        ("naturalness", "script.spoken.en.md", NATURALNESS_REVIEW, "naturalness"),
    ):
        script_path = directory / script_name
        if not script_path.exists():
            continue
        parts: list[str] = []
        for chapter_id in chapter_ids:
            chapter_path = directory / folder / f"{chapter_id}.md"
            if not chapter_path.exists():
                errors.append(f"missing {label} output {chapter_id}")
                continue
            chapter_text = chapter_path.read_text(encoding="utf-8")
            if review_pattern.findall(chapter_text) != [chapter_id]:
                errors.append(f"{label} output {chapter_id} is not explicitly reviewed")
            parts.append(review_pattern.sub("", chapter_text).strip())
        if len(parts) == len(chapter_ids):
            assembled_body = script_path.read_text(encoding="utf-8").split("\n", 1)[1].strip()
            if "\n\n".join(parts) != assembled_body:
                errors.append(f"{script_name} is not the verbatim {label} chapter assembly")
    if (directory / "script.en.md").exists() and not (
        directory / "script.editorial.en.md"
    ).exists():
        errors.append("final script requires script.editorial.en.md")
    if (directory / "script.en.md").exists() and metadata.get("audience_title"):
        first = (directory / "script.en.md").read_text(encoding="utf-8").splitlines()[0]
        if first != f"# {metadata['audience_title']}":
            errors.append("final script H1 does not match audience_title")
    return errors
