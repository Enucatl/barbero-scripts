from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
import uuid
from dataclasses import dataclass
from datetime import datetime
from email.utils import format_datetime
from pathlib import Path
from typing import Any
from xml.etree import ElementTree as ET

import markdown
import yaml
from jinja2 import Environment, PackageLoader, select_autoescape

GUID_NAMESPACE = uuid.UUID("42ada609-8ab7-5ec5-9766-bfc59ab43d17")
TOKEN_PATTERN = re.compile(r"[A-Za-z0-9_-]{16,128}")


@dataclass(frozen=True)
class PublishedEpisode:
    slug: str
    number: int
    title: str
    summary: str
    explicit: bool
    published_at: datetime
    source: Path
    script: Path
    articles: tuple[Path, ...]
    guid: str
    media_name: str = ""
    media_bytes: int = 0
    duration_seconds: int = 0


def stable_guid(slug: str) -> str:
    return str(uuid.uuid5(GUID_NAMESPACE, slug))


def read_token(path: Path) -> str:
    token = path.read_text(encoding="utf-8").strip()
    if not TOKEN_PATTERN.fullmatch(token):
        raise ValueError("preview token must be 16-128 URL-safe characters")
    return token


def _timestamp(value: Any, path: Path) -> datetime:
    if not isinstance(value, str):
        raise ValueError(f"{path}: publication.published_at must be an ISO UTC string")
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.utcoffset() is None or parsed.utcoffset().total_seconds() != 0:
        raise ValueError(f"{path}: publication.published_at must be UTC")
    return parsed


def discover_episodes(episodes_root: Path, audio_root: Path) -> list[PublishedEpisode]:
    episodes: list[PublishedEpisode] = []
    for metadata_path in sorted(episodes_root.glob("*/episode.yaml")):
        raw = yaml.safe_load(metadata_path.read_text(encoding="utf-8"))
        publication = raw.get("publication")
        if publication is None:
            continue
        missing = {"summary", "explicit", "published_at"} - publication.keys()
        if missing:
            raise ValueError(
                f"{metadata_path}: missing publication fields: {', '.join(sorted(missing))}"
            )
        if not isinstance(publication["explicit"], bool):
            raise ValueError(f"{metadata_path}: publication.explicit must be boolean")
        slug = str(raw["slug"])
        directory = metadata_path.parent
        source = audio_root / slug / f"{slug}.opus"
        script = directory / "script.en.md"
        if not source.is_file():
            raise ValueError(f"{metadata_path}: missing recorded audio {source}")
        if not script.is_file():
            raise ValueError(f"{metadata_path}: missing script.en.md")
        workflow_version = int(raw.get("workflow_version", 1))
        if workflow_version == 2:
            audience_title = raw.get("audience_title")
            if not audience_title:
                raise ValueError(f"{metadata_path}: audience_title is required for workflow v2")
            published_title = str(audience_title)
        else:
            if "title" not in publication:
                raise ValueError(f"{metadata_path}: missing publication fields: title")
            published_title = str(publication["title"])
        episodes.append(
            PublishedEpisode(
                slug=slug,
                number=int(raw["number"]),
                title=published_title,
                summary=str(publication["summary"]),
                explicit=publication["explicit"],
                published_at=_timestamp(publication["published_at"], metadata_path),
                source=source,
                script=script,
                articles=tuple(sorted((directory / "in-depth").glob("*.md"))),
                guid=stable_guid(slug),
            )
        )
    return sorted(episodes, key=lambda episode: episode.published_at, reverse=True)


def _probe(path: Path) -> tuple[int, int]:
    result = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "stream=channels",
            "-show_entries",
            "format=duration",
            "-of",
            "json",
            str(path),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    payload = json.loads(result.stdout)
    return int(payload["streams"][0]["channels"]), round(float(payload["format"]["duration"]))


def _encode(episode: PublishedEpisode, media_dir: Path) -> PublishedEpisode:
    channels, _ = _probe(episode.source)
    bitrate = "96k" if channels == 1 else "160k"
    temporary = media_dir / f".{episode.slug}.mp3"
    subprocess.run(
        [
            "ffmpeg",
            "-v",
            "error",
            "-y",
            "-i",
            str(episode.source),
            "-ar",
            "48000",
            "-b:a",
            bitrate,
            "-map_metadata",
            "-1",
            str(temporary),
        ],
        check=True,
    )
    digest = hashlib.sha256(temporary.read_bytes()).hexdigest()[:16]
    destination = media_dir / f"{episode.slug}-{digest}.mp3"
    temporary.replace(destination)
    _, duration = _probe(destination)
    return PublishedEpisode(
        **{
            **episode.__dict__,
            "media_name": destination.name,
            "media_bytes": destination.stat().st_size,
            "duration_seconds": duration,
        }
    )


def markdown_html(path: Path) -> str:
    return markdown.markdown(path.read_text(encoding="utf-8"), extensions=["extra", "sane_lists"])


def _duration(seconds: int) -> str:
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours}:{minutes:02d}:{seconds:02d}"


def _rss(config: dict[str, Any], episodes: list[PublishedEpisode], base_url: str) -> bytes:
    namespaces = {
        "itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd",
        "atom": "http://www.w3.org/2005/Atom",
        "content": "http://purl.org/rss/1.0/modules/content/",
        "podcast": "https://podcastindex.org/namespace/1.0",
    }
    for prefix, uri in namespaces.items():
        ET.register_namespace(prefix, uri)
    rss = ET.Element("rss", {"version": "2.0"})
    channel = ET.SubElement(rss, "channel")
    for tag, value in (
        ("title", config["title"]),
        ("link", f"{base_url}/"),
        ("description", config["description"]),
        ("language", config["language"]),
        ("copyright", config["copyright"]),
    ):
        ET.SubElement(channel, tag).text = str(value)
    ET.SubElement(
        channel,
        f"{{{namespaces['atom']}}}link",
        {"href": f"{base_url}/feed.xml", "rel": "self", "type": "application/rss+xml"},
    )
    ET.SubElement(channel, f"{{{namespaces['itunes']}}}author").text = config["author"]
    ET.SubElement(channel, f"{{{namespaces['itunes']}}}subtitle").text = config["subtitle"]
    ET.SubElement(channel, f"{{{namespaces['itunes']}}}explicit").text = str(
        config["explicit"]
    ).lower()
    ET.SubElement(channel, f"{{{namespaces['itunes']}}}type").text = config["type"]
    ET.SubElement(channel, f"{{{namespaces['itunes']}}}category", {"text": config["category"]})
    ET.SubElement(channel, f"{{{namespaces['itunes']}}}image", {"href": f"{base_url}/cover.png"})
    for episode in episodes:
        url = f"{base_url}/episodes/{episode.slug}/"
        item = ET.SubElement(channel, "item")
        for tag, value in (
            ("title", episode.title),
            ("description", episode.summary),
            ("link", url),
            ("pubDate", format_datetime(episode.published_at)),
            ("guid", episode.guid),
        ):
            ET.SubElement(item, tag, {"isPermaLink": "false"} if tag == "guid" else {}).text = value
        ET.SubElement(
            item,
            "enclosure",
            {
                "url": f"{base_url}/media/{episode.media_name}",
                "length": str(episode.media_bytes),
                "type": "audio/mpeg",
            },
        )
        ET.SubElement(item, f"{{{namespaces['itunes']}}}duration").text = _duration(
            episode.duration_seconds
        )
        ET.SubElement(item, f"{{{namespaces['itunes']}}}episode").text = str(episode.number)
        ET.SubElement(item, f"{{{namespaces['itunes']}}}episodeType").text = "full"
        ET.SubElement(item, f"{{{namespaces['itunes']}}}explicit").text = str(
            episode.explicit
        ).lower()
        ET.SubElement(item, f"{{{namespaces['itunes']}}}image", {"href": f"{base_url}/cover.png"})
        ET.SubElement(
            item,
            f"{{{namespaces['podcast']}}}transcript",
            {"url": f"{url}transcript.html", "type": "text/html", "rel": "transcript"},
        )
    return ET.tostring(rss, encoding="utf-8", xml_declaration=True)


def publish_preview(
    config_path: Path, episodes_root: Path, audio_root: Path, output_root: Path, token_path: Path
) -> Path:
    config = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    required = {
        "title",
        "author",
        "subtitle",
        "description",
        "language",
        "type",
        "category",
        "explicit",
        "artwork",
        "hostname",
        "copyright",
    }
    missing = required - config.keys()
    if missing:
        raise ValueError(f"{config_path}: missing fields: {', '.join(sorted(missing))}")
    token = read_token(token_path)
    episodes = discover_episodes(episodes_root, audio_root)
    if not episodes:
        raise ValueError("no recorded episodes with publication metadata")
    artwork = config_path.parent / config["artwork"]
    if not artwork.is_file():
        raise ValueError(f"missing artwork {artwork}")
    destination = output_root / token
    staging = output_root / f".{token}-{uuid.uuid4().hex}"
    try:
        (staging / "media").mkdir(parents=True)
        shutil.copy2(artwork, staging / "cover.png")
        encoded = [_encode(episode, staging / "media") for episode in episodes]
        base_url = f"https://{config['hostname']}/{token}"
        environment = Environment(
            loader=PackageLoader("barbero_scripts"), autoescape=select_autoescape()
        )
        index = environment.get_template("index.html").render(
            config=config,
            episodes=sorted(encoded, key=lambda episode: episode.number),
            base_url=base_url,
        )
        (staging / "index.html").write_text(index, encoding="utf-8")
        for episode in encoded:
            directory = staging / "episodes" / episode.slug
            directory.mkdir(parents=True)
            transcript = markdown_html(episode.script)
            articles = [(article.stem, markdown_html(article)) for article in episode.articles]
            page = environment.get_template("episode.html").render(
                config=config,
                episode=episode,
                transcript=transcript,
                articles=articles,
                base_url=base_url,
                duration=_duration(episode.duration_seconds),
            )
            (directory / "index.html").write_text(page, encoding="utf-8")
            (directory / "transcript.html").write_text(
                environment.get_template("transcript.html").render(
                    config=config, episode=episode, transcript=transcript
                ),
                encoding="utf-8",
            )
            research = directory / "research"
            for title, body in articles:
                research.mkdir(exist_ok=True)
                (research / f"{title}.html").write_text(
                    environment.get_template("article.html").render(
                        config=config, episode=episode, title=title, body=body
                    ),
                    encoding="utf-8",
                )
        (staging / "feed.xml").write_bytes(_rss(config, encoded, base_url))
        (staging / "robots.txt").write_text("User-agent: *\nDisallow: /\n", encoding="utf-8")
        output_root.mkdir(parents=True, exist_ok=True)
        previous = output_root / f".{token}-previous"
        if previous.exists():
            shutil.rmtree(previous)
        if destination.exists():
            destination.replace(previous)
        staging.replace(destination)
        if previous.exists():
            shutil.rmtree(previous)
    except BaseException:
        shutil.rmtree(staging, ignore_errors=True)
        raise
    return destination
