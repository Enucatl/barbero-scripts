from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


@dataclass(frozen=True)
class Segment:
    start: float
    end: float
    speaker: str

    @property
    def duration(self) -> float:
        return self.end - self.start


@dataclass(frozen=True)
class EditSegment:
    cleaned_start: float
    cleaned_end: float
    original_start: float
    original_end: float


@dataclass(frozen=True)
class Episode:
    slug: str
    number: int
    title: str
    source: Path
    work_dir: Path
    selected_speaker: str | None = None
    keyterms: tuple[str, ...] = ()

    @classmethod
    def load(cls, path: Path) -> Episode:
        raw: dict[str, Any] = yaml.safe_load(path.read_text(encoding="utf-8"))
        return cls(
            slug=str(raw["slug"]),
            number=int(raw["number"]),
            title=str(raw["title"]),
            source=Path(raw["source"]).expanduser(),
            work_dir=Path(raw["work_dir"]).expanduser(),
            selected_speaker=raw.get("selected_speaker"),
            keyterms=tuple(raw.get("keyterms", ())),
        )
