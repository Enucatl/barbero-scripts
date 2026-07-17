from __future__ import annotations

import json
import os
import re
import urllib.parse
import urllib.request
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Any

import yaml

from .models import EditSegment, Episode
from .timeline import cleaned_to_original
from .util import file_hash, object_hash, read_json, write_json


@dataclass(frozen=True)
class Utterance:
    id: str
    start: float
    end: float
    original_start: float
    original_end: float
    text: str
    confidence: float
    flags: tuple[str, ...] = ()


def deepgram_options(episode: Episode) -> dict[str, str]:
    options = {
        "model": "nova-3",
        "language": "it",
        "smart_format": "true",
        "utterances": "true",
        "paragraphs": "true",
        "punctuate": "true",
    }
    if episode.keyterms:
        options["keyterm"] = ":1".join(episode.keyterms) + ":1"
    return options


def request_deepgram(audio: Path, episode: Episode) -> dict[str, Any]:
    key = os.environ.get("DEEPGRAM_API_KEY")
    if not key:
        raise RuntimeError("DEEPGRAM_API_KEY is not set; use --response-json to import output")
    url = "https://api.deepgram.com/v1/listen?" + urllib.parse.urlencode(deepgram_options(episode))
    request = urllib.request.Request(
        url,
        data=audio.read_bytes(),
        headers={"Authorization": f"Token {key}", "Content-Type": "audio/flac"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=3600) as response:  # noqa: S310
        return json.load(response)


def transcribe(episode: Episode, response_json: Path | None = None) -> dict[str, Any]:
    audio = episode.work_dir / "cleaned.flac"
    edit_map = episode.work_dir / "edit-map.json"
    if not audio.is_file() or not edit_map.is_file():
        raise RuntimeError("run prepare before transcribe")
    options = deepgram_options(episode)
    fingerprint = object_hash({"audio": file_hash(audio), "options": options})
    manifest_path = episode.work_dir / "transcription-manifest.json"
    response_path = episode.work_dir / "deepgram.json"
    if response_json:
        payload = read_json(response_json)
    elif manifest_path.exists() and response_path.exists():
        old = read_json(manifest_path)
        if old.get("fingerprint") == fingerprint:
            return read_json(response_path)
        payload = request_deepgram(audio, episode)
    else:
        payload = request_deepgram(audio, episode)
    write_json(response_path, payload)
    write_json(manifest_path, {"fingerprint": fingerprint, "options": options})
    return payload


def utterances_from_deepgram(
    payload: dict[str, Any], edit_map: list[EditSegment]
) -> list[Utterance]:
    raw = payload.get("results", {}).get("utterances", [])
    result: list[Utterance] = []
    for index, item in enumerate(raw, 1):
        start, end = float(item["start"]), float(item["end"])
        confidence = float(item.get("confidence", 1.0))
        flags: list[str] = []
        low_words = [
            word for word in item.get("words", []) if float(word.get("confidence", 1)) < 0.8
        ]
        if confidence < 0.85 or low_words:
            flags.append("low-confidence")
        text = str(item["transcript"]).strip()
        if re.search(r"\b(?:1[0-9]{3}|20[0-9]{2})\b", text):
            flags.append("date")
        if any(mark in text for mark in ('"', "“", "”", "«", "»")):
            flags.append("quotation")
        words = re.findall(r"\b[A-ZÀ-ÖØ-Þ][\wÀ-ÿ'-]+\b", text)
        if len(words) > 1:
            flags.append("named-entity")
        result.append(
            Utterance(
                id=f"U-{index:05d}",
                start=start,
                end=end,
                original_start=cleaned_to_original(start, edit_map),
                original_end=cleaned_to_original(end, edit_map),
                text=text,
                confidence=confidence,
                flags=tuple(flags),
            )
        )
    return result


def apply_corrections(
    utterances: list[Utterance], corrections: dict[str, dict[str, Any]]
) -> tuple[list[Utterance], list[dict[str, str]]]:
    known = {item.id for item in utterances}
    unknown = set(corrections) - known
    if unknown:
        raise ValueError(f"corrections refer to unknown utterances: {sorted(unknown)}")
    changed: list[dict[str, str]] = []
    result: list[Utterance] = []
    for item in utterances:
        correction = corrections.get(item.id)
        if not correction:
            result.append(item)
            continue
        text = str(correction.get("text", item.text))
        if correction.get("reviewed") is True:
            flags: tuple[str, ...] = ()
        else:
            flags = item.flags + ("correction-review",)
        result.append(replace(item, text=text, flags=flags))
        if text != item.text:
            changed.append({"id": item.id, "before": item.text, "after": text})
    return result, changed


def load_corrections(path: Path) -> dict[str, dict[str, Any]]:
    if not path.exists():
        return {}
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
