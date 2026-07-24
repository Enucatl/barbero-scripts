from __future__ import annotations

from pathlib import Path

import yaml


def scaffold_episode(
    *,
    number: int,
    slug: str,
    title: str,
    source: Path,
    episodes_root: Path,
    work_root: Path,
    keyterms: tuple[str, ...] = (),
) -> Path:
    episode_slug = f"{number:03d}-{slug}"
    destination = episodes_root / episode_slug
    if destination.exists():
        raise FileExistsError(f"episode directory already exists: {destination}")

    destination.mkdir(parents=True)
    config = {
        "slug": episode_slug,
        "number": number,
        "title": title,
        "source": str(source),
        "work_dir": str(work_root / episode_slug),
        "selected_speaker": None,
        "keyterms": list(keyterms),
    }
    (destination / "episode.yaml").write_text(
        yaml.safe_dump(config, sort_keys=False, allow_unicode=True), encoding="utf-8"
    )
    (destination / "chapters.yaml").write_text("[]\n", encoding="utf-8")
    return destination
