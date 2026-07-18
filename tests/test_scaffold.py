from pathlib import Path

import pytest
import yaml

from barbero_scripts.scaffold import scaffold_episode


def test_scaffold_creates_minimal_episode_files(tmp_path: Path) -> None:
    destination = scaffold_episode(
        number=21,
        slug="il-cavaliere",
        title="Il cavaliere",
        source=Path("/audio/21.mp3"),
        episodes_root=tmp_path / "episodes",
        work_root=Path("/work"),
        keyterms=("Medioevo", "cavaliere"),
    )

    config = yaml.safe_load((destination / "episode.yaml").read_text())
    assert destination.name == "021-il-cavaliere"
    assert config["slug"] == "021-il-cavaliere"
    assert config["work_dir"] == "/work/021-il-cavaliere"
    assert config["keyterms"] == ["Medioevo", "cavaliere"]
    assert (destination / "quotes.yaml").read_text() == "[]\n"
    assert not (destination / "transcript.it.md").exists()


def test_scaffold_refuses_to_overwrite_episode(tmp_path: Path) -> None:
    arguments = {
        "number": 21,
        "slug": "il-cavaliere",
        "title": "Il cavaliere",
        "source": Path("/audio/21.mp3"),
        "episodes_root": tmp_path,
        "work_root": Path("/work"),
    }
    scaffold_episode(**arguments)
    with pytest.raises(FileExistsError):
        scaffold_episode(**arguments)
