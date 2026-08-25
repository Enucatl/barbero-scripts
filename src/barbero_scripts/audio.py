from __future__ import annotations

import os
import subprocess
import urllib.parse
import urllib.request
from collections import defaultdict
from dataclasses import asdict
from pathlib import Path
from typing import Any

from .models import EditSegment, Episode, Segment
from .timeline import build_edit_map, merge_segments
from .util import file_hash, object_hash, read_json, write_json


def parse_diarization(payload: dict[str, Any]) -> list[Segment]:
    segments = payload.get("segments")
    if not isinstance(segments, list):
        raise ValueError("diarization response must contain a segments list")
    parsed = [
        Segment(float(item["start"]), float(item["end"]), str(item["speaker"])) for item in segments
    ]
    if any(item.start < 0 or item.end <= item.start for item in parsed):
        raise ValueError("diarization contains an invalid time range")
    return sorted(parsed, key=lambda item: item.start)


def diarize_pcm(pcm_path: Path) -> list[Segment]:
    deepgram_key = os.environ.get("DEEPGRAM_API_KEY")
    if deepgram_key:
        query = urllib.parse.urlencode(
            {
                "model": "nova-3",
                "language": "it",
                "diarize": "true",
                "utterances": "true",
                "smart_format": "true",
            }
        )
        request = urllib.request.Request(
            "https://api.deepgram.com/v1/listen?" + query,
            data=pcm_path.read_bytes(),
            headers={
                "Authorization": f"Token {deepgram_key}",
                "Content-Type": "audio/wav",
            },
            method="POST",
        )
        with urllib.request.urlopen(request, timeout=3600) as response:  # noqa: S310
            payload = __import__("json").load(response)
        return [
            Segment(
                float(item["start"]),
                float(item["end"]),
                f"SPEAKER_{int(item.get('speaker', 0)):02d}",
            )
            for item in payload.get("results", {}).get("utterances", [])
        ]
    token = os.environ.get("HF_TOKEN")
    if not token:
        raise RuntimeError(
            "diarization needs --diarization-json, DEEPGRAM_API_KEY, "
            "or pyannote.audio plus HF_TOKEN"
        )
    try:
        from pyannote.audio import Pipeline  # type: ignore[import-not-found]
    except ImportError as error:
        raise RuntimeError("install pyannote.audio to run live diarization") from error
    pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization-3.1", use_auth_token=token)
    annotation = pipeline(str(pcm_path))
    return [
        Segment(float(turn.start), float(turn.end), str(speaker))
        for turn, _, speaker in annotation.itertracks(yield_label=True)
    ]


def speaker_totals(segments: list[Segment]) -> dict[str, float]:
    totals: defaultdict[str, float] = defaultdict(float)
    for segment in segments:
        totals[segment.speaker] += segment.duration
    return dict(sorted(totals.items(), key=lambda item: item[1], reverse=True))


def prepare(episode: Episode, diarization_json: Path | None = None) -> dict[str, Any]:
    if not episode.source.is_file():
        raise FileNotFoundError(f"source audio not found: {episode.source}")
    episode.work_dir.mkdir(parents=True, exist_ok=True)
    pcm_path = episode.work_dir / "diarization.wav"
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-v",
            "error",
            "-i",
            str(episode.source),
            "-ac",
            "1",
            "-ar",
            "16000",
            str(pcm_path),
        ],
        check=True,
    )
    try:
        if diarization_json:
            payload = read_json(diarization_json)
            segments = parse_diarization(payload)
        else:
            segments = diarize_pcm(pcm_path)
            payload = {"segments": [asdict(item) for item in segments]}
        write_json(episode.work_dir / "diarization.json", payload)
        totals = speaker_totals(segments)
        if len(totals) > 1 and episode.selected_speaker is None:
            raise ValueError(
                "multi-speaker audio requires an explicit retained speaker; "
                "run barbero speakers --select"
            )
        selected = episode.selected_speaker or next(iter(totals), None)
        if not selected or selected not in totals:
            raise ValueError(f"selected speaker {selected!r} is absent from diarization")
        retained = merge_segments([item for item in segments if item.speaker == selected], gap=1.5)
        edit_map = build_edit_map(retained)
        export_flac(episode.source, retained, episode.work_dir / "cleaned.flac")
        manifest = {
            "source": str(episode.source),
            "source_sha256": file_hash(episode.source),
            "diarization_sha256": object_hash(payload),
            "selected_speaker": selected,
            "speaker_seconds": totals,
            "cleaned_seconds": sum(item.duration for item in retained),
            "segments": [asdict(item) for item in edit_map],
        }
        write_json(episode.work_dir / "edit-map.json", manifest)
        return manifest
    finally:
        pcm_path.unlink(missing_ok=True)


def export_flac(source: Path, segments: list[Segment], destination: Path) -> None:
    if not segments:
        raise ValueError("no retained speech segments")
    selection = "+".join(
        f"between(t,{segment.start:.3f},{segment.end:.3f})" for segment in segments
    )
    audio_filter = f"aselect='{selection}',asetpts=N/SR/TB"
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-v",
            "error",
            "-i",
            str(source),
            "-af",
            audio_filter,
            "-ac",
            "1",
            "-ar",
            "16000",
            "-compression_level",
            "8",
            str(destination),
        ],
        check=True,
    )


def load_edit_segments(path: Path) -> list[EditSegment]:
    payload = read_json(path)
    return [EditSegment(**item) for item in payload["segments"]]
