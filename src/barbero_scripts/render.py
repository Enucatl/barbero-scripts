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
COVERAGE = re.compile(
    r"<!-- (?:chapter: (CH-\d{3}); )?transcript: (U-\d{5})[–-](U-\d{5})"
    r"(?:; omissions: ([^>]+))? -->"
)
CHAPTER_HEADING = re.compile(r"^## (\d+)\.\s+(.+)$", re.MULTILINE)
NATURALNESS_REVIEW = re.compile(r"<!-- naturalness-reviewed: (CH-\d{3}) -->\n?")
TENSE_REVIEW = re.compile(r"<!-- tense-reviewed: (CH-\d{3}) -->\n?")
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


def assemble_italian_script(directory: Path) -> None:
    """Assemble reviewed transcript utterances without changing their spoken text."""
    transcript_path = directory / "transcript.it.md"
    chapter_path = directory / "chapters.yaml"
    transcript = transcript_path.read_text(encoding="utf-8")
    blocks = re.split(r"(?=^## U-\d{5}\b)", transcript, flags=re.MULTILINE)[1:]
    utterances: dict[str, str] = {}
    for block in blocks:
        identifier = TRANSCRIPT_ID.search(block)
        if identifier is None:
            continue
        parts = block.strip().split("\n\n", 1)
        if len(parts) != 2:
            raise ValueError(f"transcript utterance {identifier.group()} has no text")
        utterances[identifier.group()] = parts[1].strip()

    chapters = yaml.safe_load(chapter_path.read_text(encoding="utf-8")) or []
    title = transcript.splitlines()[0].removeprefix("# ").removesuffix(" — Italian transcript")
    lines = [f"# {title} — copione italiano", ""]
    for chapter in chapters:
        chapter_id = str(chapter["id"])
        number = int(chapter_id.removeprefix("CH-"))
        start_id = str(chapter["start"])
        end_id = str(chapter["end"])
        lines.extend(
            [
                f"## {number}. {chapter['title']}",
                "",
                f"<!-- chapter: {chapter_id}; transcript: {start_id}–{end_id} -->",
                "",
            ]
        )
        start = int(start_id[2:])
        end = int(end_id[2:])
        chapter_text = " ".join(utterances[f"U-{value:05d}"] for value in range(start, end + 1))
        lines.extend([chapter_text, ""])
        markers = chapter.get("markers", [])
        if markers:
            marker_text = " ".join(f"[{item}]" for item in markers)
            lines.extend([f"<!-- research: {marker_text} -->", ""])
    (directory / "script.it.md").write_text("\n".join(lines), encoding="utf-8")


def initialize_italian_review(directory: Path) -> None:
    """Create an explicit review checklist with every item approved by default."""
    destination = directory / "italian-review.yaml"
    if destination.exists():
        raise FileExistsError(f"review checklist already exists: {destination}")
    transcript = (directory / "transcript.it.md").read_text(encoding="utf-8")
    chapters = yaml.safe_load((directory / "chapters.yaml").read_text(encoding="utf-8")) or []
    payload = {
        "utterances": [
            {"id": identifier, "reviewed_audio": True}
            for identifier in _ordered_transcript_ids(transcript)
        ],
        "chapters": [
            {"id": str(chapter["id"]), "complete_ordered_coverage": True} for chapter in chapters
        ],
    }
    destination.write_text(
        yaml.safe_dump(payload, sort_keys=False, allow_unicode=True), encoding="utf-8"
    )


def initialize_naturalness_chapters(directory: Path) -> None:
    """Split tense-reviewed English into independently reviewable chapter files."""
    source = (directory / "script.tense.en.md").read_text(encoding="utf-8")
    headings = list(CHAPTER_HEADING.finditer(source))
    destination = directory / "naturalness"
    destination.mkdir(exist_ok=True)
    for index, heading in enumerate(headings, start=1):
        chapter_id = f"CH-{index:03d}"
        path = destination / f"{chapter_id}.md"
        if path.exists():
            raise FileExistsError(f"naturalness chapter already exists: {path}")
        end = headings[index].start() if index < len(headings) else len(source)
        chapter_text = source[heading.start() : end].strip()
        path.write_text(
            f"<!-- naturalness-reviewed: {chapter_id} -->\n{chapter_text}\n", encoding="utf-8"
        )


def assemble_naturalness_chapters(directory: Path) -> None:
    """Assemble reviewed naturalness chapters without rewriting them."""
    tense = (directory / "script.tense.en.md").read_text(encoding="utf-8")
    title = tense.splitlines()[0].removesuffix(" — assembled faithful translation")
    chapters = _chapter_coverage((directory / "script.it.md").read_text(encoding="utf-8"), "", [])
    parts: list[str] = []
    for chapter_id, _, _ in chapters:
        path = directory / "naturalness" / f"{chapter_id}.md"
        text = path.read_text(encoding="utf-8")
        if NATURALNESS_REVIEW.findall(text) != [chapter_id]:
            raise ValueError(f"naturalness chapter is not reviewed: {chapter_id}")
        parts.append(NATURALNESS_REVIEW.sub("", text).strip())
    body = "\n\n".join(parts)
    (directory / "script.spoken.en.md").write_text(f"{title}\n\n{body}\n", encoding="utf-8")


def initialize_tense_chapters(directory: Path) -> None:
    """Split corrected English into independent chapter-level tense reviews."""
    source = (directory / "script.corrected.en.md").read_text(encoding="utf-8")
    headings = list(CHAPTER_HEADING.finditer(source))
    destination = directory / "tense"
    destination.mkdir(exist_ok=True)
    for index, heading in enumerate(headings, start=1):
        chapter_id = f"CH-{index:03d}"
        path = destination / f"{chapter_id}.md"
        if path.exists():
            raise FileExistsError(f"tense chapter already exists: {path}")
        end = headings[index].start() if index < len(headings) else len(source)
        chapter_text = source[heading.start() : end].strip()
        path.write_text(
            f"<!-- tense-reviewed: {chapter_id} -->\n{chapter_text}\n", encoding="utf-8"
        )


def assemble_tense_chapters(directory: Path) -> None:
    """Assemble reviewed tense chapters without rewriting them."""
    corrected = (directory / "script.corrected.en.md").read_text(encoding="utf-8")
    title = corrected.splitlines()[0]
    chapters = _chapter_coverage((directory / "script.it.md").read_text(encoding="utf-8"), "", [])
    parts: list[str] = []
    for chapter_id, _, _ in chapters:
        path = directory / "tense" / f"{chapter_id}.md"
        text = path.read_text(encoding="utf-8")
        if TENSE_REVIEW.findall(text) != [chapter_id]:
            raise ValueError(f"tense chapter is not reviewed: {chapter_id}")
        parts.append(TENSE_REVIEW.sub("", text).strip())
    body = "\n\n".join(parts)
    (directory / "script.tense.en.md").write_text(f"{title}\n\n{body}\n", encoding="utf-8")


def finalize_consistency(directory: Path) -> None:
    """Use the assembled script unchanged when no narrow consistency edits are needed."""
    spoken = (directory / "script.spoken.en.md").read_text(encoding="utf-8")
    (directory / "script.en.md").write_text(spoken, encoding="utf-8")


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


def _marker_sequence(text: str, prefixes: set[str]) -> list[str]:
    return [
        f"{match.group(1)}-{match.group(2)}"
        for match in MARKER.finditer(text)
        if match.group(1) in prefixes
    ]


def _ordered_transcript_ids(text: str) -> list[str]:
    return [match.group(1) for match in re.finditer(r"^## (U-\d{5})\b", text, re.MULTILINE)]


def _chapter_coverage(text: str, label: str, errors: list[str]) -> list[tuple[str, str, str]]:
    sections = list(COVERAGE.finditer(text))
    if not sections:
        errors.append(f"{label} has no chapter-level transcript coverage")
        return []
    headings = list(CHAPTER_HEADING.finditer(text))
    if len(headings) != len(sections):
        errors.append(f"{label} chapter headings and coverage comments differ")
    result: list[tuple[str, str, str]] = []
    for index, section in enumerate(sections, start=1):
        chapter = section.group(1) or f"CH-{index:03d}"
        start_id, end_id = section.group(2, 3)
        start, end = (int(value[2:]) for value in (start_id, end_id))
        if start > end:
            errors.append(f"{label} has reversed coverage {start_id}–{end_id}")
        result.append((chapter, start_id, end_id))
    return result


def _validate_exact_coverage(
    chapters: list[tuple[str, str, str]], expected_ids: list[str], label: str, errors: list[str]
) -> None:
    covered: list[str] = []
    for _chapter, start_id, end_id in chapters:
        start = int(start_id[2:])
        end = int(end_id[2:])
        if start <= end:
            covered.extend(f"U-{number:05d}" for number in range(start, end + 1))
    chapter_ids = [chapter for chapter, _, _ in chapters]
    expected_chapters = [f"CH-{number:03d}" for number in range(1, len(chapters) + 1)]
    if chapter_ids != expected_chapters:
        errors.append(f"{label} chapter IDs are not sequential")
    if covered != expected_ids:
        errors.append(f"{label} does not have exact ordered utterance coverage")


def _validate_italian_wording(transcript: str, script: str, errors: list[str]) -> None:
    blocks = re.split(r"(?=^## U-\d{5}\b)", transcript, flags=re.MULTILINE)[1:]
    utterances: dict[str, str] = {}
    for block in blocks:
        identifier = TRANSCRIPT_ID.search(block)
        parts = block.strip().split("\n\n", 1)
        if identifier is not None and len(parts) == 2:
            utterances[identifier.group()] = parts[1].strip()
    headings = list(CHAPTER_HEADING.finditer(script))
    coverages = list(COVERAGE.finditer(script))
    for index, coverage in enumerate(coverages):
        start_id, end_id = coverage.group(2, 3)
        start = int(start_id[2:])
        end = int(end_id[2:])
        identifiers = [f"U-{number:05d}" for number in range(start, end + 1)]
        if any(identifier not in utterances for identifier in identifiers):
            continue
        expected = " ".join(utterances[identifier] for identifier in identifiers)
        limit = headings[index + 1].start() if index + 1 < len(headings) else len(script)
        actual = re.sub(r"<!--.*?-->", "", script[coverage.end() : limit], flags=re.DOTALL).strip()
        if actual != expected:
            errors.append(f"Italian script changes spoken wording in {coverage.group(1)}")


def _looks_italian(text: str) -> bool:
    words = set(re.findall(r"[a-zàèéìòù]+", text.lower()))
    return len(words & ITALIAN_FUNCTION_WORDS) >= 3


def _normalized_wording(text: str) -> str:
    """Ignore Markdown line wrapping while preserving every word and punctuation mark."""
    return " ".join(text.split())


def validate_episode(directory: Path) -> list[str]:
    errors: list[str] = []
    transcript_path = directory / "transcript.it.md"
    if not transcript_path.exists():
        return ["missing transcript.it.md"]
    transcript = transcript_path.read_text(encoding="utf-8")
    if "[REVIEW:" in transcript:
        errors.append("transcript contains unresolved review flags")
    transcript_id_order = _ordered_transcript_ids(transcript)
    transcript_ids = set(transcript_id_order)

    italian_first = (directory / "script.it.md").exists()
    staged_schema = (
        italian_first
        or (directory / "accuracy-notes.yaml").exists()
        or (directory / "script.translation.en.md").exists()
    )
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
        "italian": directory / "script.it.md",
        "faithful": directory / "script.translation.faithful.en.md",
        "translation": directory / "script.translation.en.md",
        "corrected": directory / "script.corrected.en.md",
        "spoken": directory / "script.spoken.en.md",
        "tense": directory / "script.tense.en.md",
        "final": directory / "script.en.md",
    }
    texts = {
        name: path.read_text(encoding="utf-8") for name, path in paths.items() if path.exists()
    }
    chapter_contract: list[tuple[str, str, str]] = []
    italian_ready = True
    if italian_first:
        chapter_contract = _chapter_coverage(texts["italian"], "Italian script", errors)
        _validate_exact_coverage(chapter_contract, transcript_id_order, "Italian script", errors)
        _validate_italian_wording(transcript, texts["italian"], errors)
        review_path = directory / "italian-review.yaml"
        if not review_path.exists():
            errors.append("missing italian-review.yaml")
            italian_ready = False
        else:
            review = yaml.safe_load(review_path.read_text(encoding="utf-8")) or {}
            utterance_reviews = review.get("utterances", []) if isinstance(review, dict) else []
            reviewed_ids = [
                str(item.get("id"))
                for item in utterance_reviews
                if isinstance(item, dict) and item.get("reviewed_audio") is True
            ]
            if reviewed_ids != transcript_id_order:
                errors.append("Italian audio reviews do not exactly match transcript ID order")
                italian_ready = False
            chapter_reviews = review.get("chapters", []) if isinstance(review, dict) else []
            reviewed_chapters = [
                str(item.get("id"))
                for item in chapter_reviews
                if isinstance(item, dict) and item.get("complete_ordered_coverage") is True
            ]
            if reviewed_chapters != [item[0] for item in chapter_contract]:
                errors.append("Italian chapter reviews are incomplete or out of order")
                italian_ready = False
        research_started = (
            any(
                (directory / name).exists()
                and (yaml.safe_load((directory / name).read_text(encoding="utf-8")) or [])
                for name in ("quotes.yaml", "claims.yaml", "sources.yaml")
            )
            or (directory / "outline.md").exists()
        )
        if not italian_ready and research_started:
            errors.append("research is blocked until the Italian checkpoint passes")

    utterance_path = directory / "translation.utterances.en.yaml"
    if staged_schema and not italian_first:
        utterance_records = _load_records(utterance_path, "utterance translation", errors)
        utterance_ids = list(utterance_records)
        if utterance_ids != transcript_id_order:
            errors.append("utterance translations do not exactly match transcript ID order")
        for identifier, item in utterance_records.items():
            if not item.get("text"):
                errors.append(f"utterance translation {identifier} has no text")
    if italian_first and "faithful" not in texts:
        errors.append("missing script.translation.faithful.en.md")
    if "faithful" in texts:
        unreviewed_quotes = [
            identifier
            for identifier, item in ledgers["Q"].items()
            if item.get("human_reviewed") is False
        ]
        if unreviewed_quotes:
            errors.append(
                "faithful translation is blocked by unreviewed quotations: "
                + ", ".join(unreviewed_quotes)
            )
    legacy_final = "Legacy pre-staged adaptation" in texts.get("final", "")
    if staged_schema and "final" in texts and not legacy_final and "spoken" not in texts:
        errors.append("final script requires script.spoken.en.md")
    for stage in ("faithful", "translation", "corrected", "tense", "spoken", "final"):
        if stage not in texts or not italian_first:
            continue
        coverage = _chapter_coverage(texts[stage], f"{stage} script", errors)
        if coverage != chapter_contract:
            errors.append(f"{stage} script chapter boundaries differ from Italian script")
        _validate_exact_coverage(coverage, transcript_id_order, f"{stage} script", errors)

    if "faithful" in texts:
        for identifier, item in ledgers["Q"].items():
            replacement = item.get("translation")
            if (
                item.get("source_replacement") == "eligible"
                and replacement
                and str(replacement) in texts["faithful"]
            ):
                errors.append(f"faithful translation prematurely uses wording for {identifier}")
    if "translation" in texts:
        for identifier, item in ledgers["Q"].items():
            replacement = item.get("translation")
            if item.get("source_replacement") == "eligible" and replacement:
                for stage in ("translation", "corrected", "tense", "spoken", "final"):
                    if stage in texts and _normalized_wording(str(replacement)) not in (
                        _normalized_wording(texts[stage])
                    ):
                        errors.append(f"{stage} does not use eligible wording for {identifier}")
    if italian_first:
        ordered_stages = [
            stage
            for stage in (
                "italian",
                "faithful",
                "translation",
                "corrected",
                "tense",
                "spoken",
                "final",
            )
            if stage in texts
        ]
        for before, after in zip(ordered_stages, ordered_stages[1:], strict=False):
            prefixes = {"SRC", "Q", "C"}
            if before in {"corrected", "tense", "spoken"}:
                prefixes.add("N")
            if _marker_sequence(texts[before], prefixes) != _marker_sequence(
                texts[after], prefixes
            ):
                errors.append(f"{after} script does not preserve {before} markers in order")
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
    for stage in ("corrected", "tense", "spoken", "final"):
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
    if (
        "corrected" in texts
        and "spoken" in texts
        and "tense" in texts
        and "final" in texts
        and not legacy_final
    ):
        for prefix, label in (("Q", "quotation"), ("C", "claim"), ("N", "correction")):
            if _markers(texts["corrected"], {prefix}) != _markers(texts["tense"], {prefix}):
                errors.append(f"tense script does not preserve {label} markers")
            if _markers(texts["tense"], {prefix}) != _markers(texts["spoken"], {prefix}):
                errors.append(f"spoken script does not preserve tense-reviewed {label} markers")
            if _markers(texts["spoken"], {prefix}) != _markers(texts["final"], {prefix}):
                errors.append(f"final script does not preserve spoken {label} markers")

    if italian_first and "spoken" in texts:
        chapter_dir = directory / "naturalness"
        assembled_parts: list[str] = []
        for chapter, _, _ in chapter_contract:
            path = chapter_dir / f"{chapter}.md"
            if not path.exists():
                errors.append(f"missing naturalness output {chapter}")
                continue
            chapter_text = path.read_text(encoding="utf-8")
            reviews = NATURALNESS_REVIEW.findall(chapter_text)
            if reviews != [chapter]:
                errors.append(f"naturalness output {chapter} is not explicitly reviewed")
            assembled_parts.append(NATURALNESS_REVIEW.sub("", chapter_text).strip())
        if len(assembled_parts) == len(chapter_contract):
            spoken_body = texts["spoken"].split("\n", 1)[1].strip()
            if "\n\n".join(assembled_parts) != spoken_body:
                errors.append("spoken script is not the verbatim naturalness chapter assembly")
    if italian_first and "tense" in texts:
        chapter_dir = directory / "tense"
        assembled_parts = []
        for chapter, _, _ in chapter_contract:
            path = chapter_dir / f"{chapter}.md"
            if not path.exists():
                errors.append(f"missing tense output {chapter}")
                continue
            chapter_text = path.read_text(encoding="utf-8")
            reviews = TENSE_REVIEW.findall(chapter_text)
            if reviews != [chapter]:
                errors.append(f"tense output {chapter} is not explicitly reviewed")
            assembled_parts.append(TENSE_REVIEW.sub("", chapter_text).strip())
        if len(assembled_parts) == len(chapter_contract):
            tense_body = texts["tense"].split("\n", 1)[1].strip()
            if "\n\n".join(assembled_parts) != tense_body:
                errors.append("tense script is not the verbatim tense chapter assembly")
    return errors
