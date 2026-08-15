from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path
from xml.etree import ElementTree as ET

import pytest
import yaml

from barbero_scripts.publish import discover_episodes, markdown_html, publish_preview, stable_guid


def write_fixture(root: Path) -> tuple[Path, Path, Path, Path]:
    episodes = root / "episodes"
    audio = root / "audio"
    episode = episodes / "001-a-b-test"
    source_dir = audio / "001-a-b-test"
    episode.mkdir(parents=True)
    source_dir.mkdir(parents=True)
    metadata = {
        "slug": "001-a-b-test",
        "number": 1,
        "title": "Italian title",
        "source": "/unused",
        "work_dir": "/unused",
        "publication": {
            "title": "A & B <History>",
            "summary": "A concise & accurate summary.",
            "explicit": False,
            "published_at": "2026-08-01T10:00:00Z",
        },
    }
    (episode / "episode.yaml").write_text(yaml.safe_dump(metadata), encoding="utf-8")
    (episode / "script.en.md").write_text(
        "<!-- U-1 -->\n# Transcript\n\nLedger `C-1`.", encoding="utf-8"
    )
    research = episode / "in-depth"
    research.mkdir()
    (research / "C-1-note.md").write_text("# Research\n\nVerbatim note.", encoding="utf-8")
    source = source_dir / "001-a-b-test.opus"
    subprocess.run(
        [
            "ffmpeg",
            "-v",
            "error",
            "-f",
            "lavfi",
            "-i",
            "sine=frequency=440:duration=0.3",
            "-ar",
            "48000",
            "-ac",
            "1",
            "-c:a",
            "libopus",
            str(source),
        ],
        check=True,
    )
    artwork = root / "cover.png"
    subprocess.run(
        [
            "ffmpeg",
            "-v",
            "error",
            "-f",
            "lavfi",
            "-i",
            "color=c=red:s=64x64",
            "-frames:v",
            "1",
            str(artwork),
        ],
        check=True,
    )
    config = root / "podcast.yaml"
    config.write_text(
        yaml.safe_dump(
            {
                "title": "Show & Tell",
                "author": "Author",
                "subtitle": "Subtitle",
                "description": "Description",
                "language": "en",
                "type": "episodic",
                "category": "History",
                "explicit": False,
                "artwork": "cover.png",
                "hostname": "example.test",
                "copyright": "English material",
            }
        ),
        encoding="utf-8",
    )
    token = root / ".token"
    token.write_text("valid_secret_token_123", encoding="utf-8")
    return config, episodes, audio, token


def test_discovery_excludes_unpublished_and_orders(tmp_path: Path) -> None:
    _, episodes, audio, _ = write_fixture(tmp_path)
    unpublished = episodes / "002-unpublished"
    unpublished.mkdir()
    (unpublished / "episode.yaml").write_text(
        "slug: 002-unpublished\nnumber: 2\n", encoding="utf-8"
    )
    found = discover_episodes(episodes, audio)
    assert [episode.slug for episode in found] == ["001-a-b-test"]
    assert found[0].articles[0].name == "C-1-note.md"


def test_guid_and_markdown_are_deterministic(tmp_path: Path) -> None:
    script = tmp_path / "script.md"
    script.write_text("<!-- editorial U-1 -->\n# Heading", encoding="utf-8")
    assert stable_guid("slug") == stable_guid("slug")
    assert stable_guid("slug") != stable_guid("other")
    rendered = markdown_html(script)
    assert "<!-- editorial U-1 -->" in rendered
    assert "<h1>Heading</h1>" in rendered


def test_invalid_publication_metadata_fails(tmp_path: Path) -> None:
    _, episodes, audio, _ = write_fixture(tmp_path)
    path = next(episodes.glob("*/episode.yaml"))
    data = yaml.safe_load(path.read_text())
    del data["publication"]["summary"]
    path.write_text(yaml.safe_dump(data))
    with pytest.raises(ValueError, match="summary"):
        discover_episodes(episodes, audio)


def test_publish_generates_valid_feed_and_media(tmp_path: Path) -> None:
    config, episodes, audio, token = write_fixture(tmp_path)
    destination = publish_preview(config, episodes, audio, tmp_path / "published", token)
    media = next((destination / "media").glob("*.mp3"))
    assert re.fullmatch(r"001-a-b-test-[0-9a-f]{16}\.mp3", media.name)
    probe = json.loads(
        subprocess.run(
            [
                "ffprobe",
                "-v",
                "error",
                "-show_entries",
                "stream=codec_name,sample_rate,channels,bit_rate",
                "-of",
                "json",
                str(media),
            ],
            check=True,
            capture_output=True,
            text=True,
        ).stdout
    )
    stream = probe["streams"][0]
    assert stream["codec_name"] == "mp3"
    assert stream["sample_rate"] == "48000"
    assert stream["channels"] == 1
    assert 90_000 <= int(stream["bit_rate"]) <= 100_000
    tree = ET.parse(destination / "feed.xml")
    item = tree.find("./channel/item")
    assert item is not None
    assert item.findtext("title") == "A & B <History>"
    enclosure = item.find("enclosure")
    assert enclosure is not None
    assert int(enclosure.attrib["length"]) == media.stat().st_size
    assert enclosure.attrib["url"].startswith("https://example.test/valid_secret_token_123/")
    assert (destination / "episodes/001-a-b-test/research/C-1-note.html").is_file()
    transcript = (destination / "episodes/001-a-b-test/transcript.html").read_text()
    assert "<!-- U-1 -->" in transcript
