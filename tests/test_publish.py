from __future__ import annotations

import json
import re
import shutil
import subprocess
from pathlib import Path
from xml.etree import ElementTree as ET

import pytest
import yaml

import barbero_scripts.publish as publish_module
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
    assert (destination / "favicon.ico").is_file()
    assert (destination / "apple-touch-icon.png").is_file()


def test_public_publish_uses_root_urls(tmp_path: Path) -> None:
    config, episodes, audio, _ = write_fixture(tmp_path)
    destination = publish_preview(config, episodes, audio, tmp_path / "published", None)

    assert destination == tmp_path / "published"
    tree = ET.parse(destination / "feed.xml")
    item = tree.find("./channel/item")
    assert item is not None
    enclosure = item.find("enclosure")
    assert enclosure is not None
    assert enclosure.attrib["url"].startswith("https://example.test/media/")


def test_publish_adds_audio_resume_support_to_both_pages(tmp_path: Path) -> None:
    config, episodes, audio, _ = write_fixture(tmp_path)
    destination = publish_preview(config, episodes, audio, tmp_path / "published", None)

    pages = [
        (destination / "index.html").read_text(encoding="utf-8"),
        (destination / "episodes/001-a-b-test/index.html").read_text(encoding="utf-8"),
    ]
    for page in pages:
        assert 'data-play="001-a-b-test"' in page
        assert page.count('<audio id="podcast-audio"') == 1
        assert 'const keyPrefix = "barbero-audio-position:"' in page
        assert "localStorage.getItem(keyPrefix + selected.play)" in page
        assert 'audio.addEventListener("pause", () => { save(); updateButtons(); })' in page
        assert 'audio.addEventListener("ended"' in page
        assert 'rel="icon" href="https://example.test/favicon.ico"' in page
        assert 'rel="apple-touch-icon" href="https://example.test/apple-touch-icon.png"' in page


def test_publish_reuses_media_when_source_is_unchanged(tmp_path: Path, monkeypatch) -> None:
    config, episodes, audio, token = write_fixture(tmp_path)
    destination = publish_preview(config, episodes, audio, tmp_path / "published", token)
    media = next((destination / "media").glob("*.mp3"))
    real_run = publish_module.subprocess.run

    def fail_if_media_encode(command, **kwargs):
        if (
            command
            and command[0] == "ffmpeg"
            and any(isinstance(part, str) and part.startswith("scale=") for part in command)
        ):
            return real_run(command, **kwargs)
        raise AssertionError("unchanged media should not be re-encoded")

    monkeypatch.setattr(publish_module.subprocess, "run", fail_if_media_encode)
    rebuilt = publish_preview(config, episodes, audio, tmp_path / "published", token)

    rebuilt_media = next((rebuilt / "media").glob("*.mp3"))
    assert rebuilt_media.name == media.name
    assert rebuilt_media.read_bytes() == media.read_bytes()


def test_encode_reencodes_when_source_digest_changes(tmp_path: Path, monkeypatch) -> None:
    _, episodes, audio, _ = write_fixture(tmp_path)
    episode = discover_episodes(episodes, audio)[0]
    previous_media = tmp_path / "previous"
    previous_media.mkdir()
    (previous_media / "old.mp3").write_bytes(b"old")
    (tmp_path / "media").mkdir()
    calls = []

    def fake_run(command, **kwargs):
        calls.append(command)
        Path(command[-1]).write_bytes(b"new")

    monkeypatch.setattr(publish_module, "_probe", lambda path: (1, 1))
    monkeypatch.setattr(publish_module.subprocess, "run", fake_run)
    encoded = publish_module._encode(
        episode,
        tmp_path / "media",
        previous_media,
        {
            episode.slug: {
                "source_sha256": "stale",
                "media_name": "old.mp3",
                "duration_seconds": 1,
            }
        },
    )

    assert encoded.media_name.endswith(".mp3")
    assert calls and calls[0][0] == "ffmpeg"


def test_publish_uses_episode_artwork_and_latest_first(tmp_path: Path) -> None:
    """Publish custom artwork with a cover fallback and preserve publication order."""
    config, episodes, audio, token = write_fixture(tmp_path)
    older = episodes / "001-a-b-test"
    newer = episodes / "002-newer"
    shutil.copytree(older, newer)
    metadata = yaml.safe_load((newer / "episode.yaml").read_text())
    metadata.update(slug=newer.name, number=2)
    metadata["publication"].update(title="Newest episode", published_at="2026-08-02T10:00:00Z")
    (newer / "episode.yaml").write_text(yaml.safe_dump(metadata), encoding="utf-8")
    shutil.copy2(tmp_path / "cover.png", newer / "illustration.jpg")
    (audio / newer.name).mkdir()
    shutil.copy2(
        audio / older.name / f"{older.name}.opus", audio / newer.name / f"{newer.name}.opus"
    )

    discovered = discover_episodes(episodes, audio)
    assert [episode.slug for episode in discovered] == [newer.name, older.name]
    assert discovered[0].artwork_name == "episodes/002-newer/illustration.jpg"
    assert discovered[1].artwork is None
    assert discovered[1].artwork_name == "cover.png"

    destination = publish_preview(config, episodes, audio, tmp_path / "published", token)
    illustration = destination / discovered[0].artwork_name
    assert illustration.read_bytes() == (newer / "illustration.jpg").read_bytes()
    assert not (destination / "episodes" / older.name / "illustration.jpg").exists()
    items = ET.parse(destination / "feed.xml").findall("./channel/item")
    assert [item.findtext("title") for item in items] == ["Newest episode", "A & B <History>"]
    images = [
        item.find("{http://www.itunes.com/dtds/podcast-1.0.dtd}image").attrib["href"]
        for item in items
    ]
    base_url = "https://example.test/valid_secret_token_123"
    assert images == [f"{base_url}/{episode.artwork_name}" for episode in discovered]
    index = (destination / "index.html").read_text(encoding="utf-8")
    assert index.index("Newest episode") < index.index("A &amp; B &lt;History&gt;")


def test_trilogy_titles_and_navigation(tmp_path: Path) -> None:
    config, episodes, audio, _ = write_fixture(tmp_path)
    original = episodes / "001-a-b-test"
    second = episodes / "002-second"
    shutil.copytree(original, second)
    (audio / second.name).mkdir()
    shutil.copy2(
        audio / original.name / f"{original.name}.opus", audio / second.name / f"{second.name}.opus"
    )
    for directory, number, title, date in (
        (original, 1, "War & Peace: First <Act>", "2026-08-02T10:00:00Z"),
        (second, 2, "War & Peace: Second Act", "2026-08-01T10:00:00Z"),
    ):
        path = directory / "episode.yaml"
        data = yaml.safe_load(path.read_text())
        data.update(slug=directory.name, number=number)
        data["publication"].update(title=title, published_at=date)
        path.write_text(yaml.safe_dump(data))
    data = yaml.safe_load(config.read_text())
    data["trilogies"] = [
        {
            "title": "War & Peace",
            "episodes": [
                {"number": 1, "subject": "First <Act>"},
                {"number": 2, "subject": "Second Act"},
                {"number": 3, "subject": "Third Act"},
            ],
        }
    ]
    config.write_text(yaml.safe_dump(data))
    destination = publish_preview(config, episodes, audio, tmp_path / "published", None)
    index = (destination / "index.html").read_text()
    first = (destination / "episodes" / original.name / "index.html").read_text()
    second_page = (destination / "episodes" / second.name / "index.html").read_text()
    transcript = (destination / "episodes" / original.name / "transcript.html").read_text()
    assert '<span class="trilogy-prefix">War &amp; Peace:</span> First &lt;Act&gt;' in index
    assert "Trilogy · Episode 1/3" in first
    assert "Trilogy · Episode 2/3" in second_page
    assert "Trilogy · Episode 1/3" in transcript
    assert (
        first.split('<nav class="trilogy-nav"')[1].split("</nav>")[0].count('aria-current="page"')
        == 1
    )
    assert f'/episodes/{original.name}/" aria-current="page"' in first
    assert f'/episodes/{second.name}/"' in first
    assert "Third Act</span> <small>Not yet published</small>" in first
    assert "Third Act</a>" not in first
    items = ET.parse(destination / "feed.xml").findall("./channel/item")
    assert [item.findtext("title") for item in items] == [
        "War & Peace: First <Act>",
        "War & Peace: Second Act",
    ]
    assert [item.findtext("guid") for item in items] == [
        stable_guid(original.name),
        stable_guid(second.name),
    ]
    assert all(
        item.find("enclosure").attrib["url"].startswith("https://example.test/media/")
        for item in items
    )


def test_invalid_trilogy_catalogue(tmp_path: Path) -> None:
    config, episodes, audio, _ = write_fixture(tmp_path)
    data = yaml.safe_load(config.read_text())
    data["trilogies"] = [
        {
            "title": "Series",
            "episodes": [
                {"number": 1, "subject": "One"},
                {"number": 2, "subject": "Two"},
                {"number": 3, "subject": "Three"},
            ],
        }
    ]
    config.write_text(yaml.safe_dump(data))
    with pytest.raises(ValueError, match="title disagrees"):
        publish_preview(config, episodes, audio, tmp_path / "published", None)
    data["trilogies"][0]["episodes"][0]["number"] = 2
    with pytest.raises(ValueError, match="multiple series slots"):
        publish_module._series_memberships(data, discover_episodes(episodes, audio))
