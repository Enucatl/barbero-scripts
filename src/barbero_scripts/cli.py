from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

from .audio import prepare, speaker_totals
from .models import Episode
from .render import render_recording, render_transcript, validate_episode
from .transcript import transcribe
from .util import read_json


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(prog="barbero")
    commands = result.add_subparsers(dest="command", required=True)
    prepare_parser = commands.add_parser("prepare", help="diarize and clean an episode")
    prepare_parser.add_argument("config", type=Path)
    prepare_parser.add_argument("--diarization-json", type=Path)
    speakers = commands.add_parser("speakers", help="review or select the retained speaker")
    speakers.add_argument("config", type=Path)
    choice = speakers.add_mutually_exclusive_group(required=True)
    choice.add_argument("--show", action="store_true")
    choice.add_argument("--select")
    transcription = commands.add_parser("transcribe", help="transcribe cleaned episode")
    transcription.add_argument("config", type=Path)
    transcription.add_argument("--response-json", type=Path)
    rendering = commands.add_parser("render", help="render committed editorial documents")
    rendering.add_argument("config", type=Path)
    validation = commands.add_parser("validate", help="validate editorial references")
    validation.add_argument("episode_dir", type=Path)
    return result


def set_selected_speaker(path: Path, speaker: str) -> None:
    payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    payload["selected_speaker"] = speaker
    path.write_text(yaml.safe_dump(payload, sort_keys=False, allow_unicode=True), encoding="utf-8")


def main() -> None:
    args = parser().parse_args()
    if args.command == "validate":
        errors = validate_episode(args.episode_dir)
        if errors:
            for error in errors:
                print(f"ERROR: {error}", file=sys.stderr)
            raise SystemExit(1)
        print("Editorial validation passed")
        return
    episode = Episode.load(args.config)
    if args.command == "prepare":
        manifest = prepare(episode, args.diarization_json)
        print(f"Retained {manifest['cleaned_seconds']:.1f}s as {manifest['selected_speaker']}")
    elif args.command == "speakers":
        segments = read_json(episode.work_dir / "diarization.json")["segments"]
        from .audio import parse_diarization

        totals = speaker_totals(parse_diarization({"segments": segments}))
        if args.show:
            for speaker, seconds in totals.items():
                selected = " *" if speaker == episode.selected_speaker else ""
                print(f"{speaker}: {seconds:.1f}s{selected}")
        else:
            if args.select not in totals:
                raise SystemExit(f"speaker {args.select!r} is absent from diarization")
            set_selected_speaker(args.config, args.select)
            print(f"Selected {args.select}; re-run prepare")
    elif args.command == "transcribe":
        payload = transcribe(episode, args.response_json)
        count = len(payload.get("results", {}).get("utterances", []))
        print(f"Stored {count} utterances")
    elif args.command == "render":
        directory = args.config.parent
        render_transcript(episode, directory / "transcript.it.md")
        render_recording(directory / "script.en.md", directory / "script.recording.md")
        print("Rendered transcript.it.md and script.recording.md")


if __name__ == "__main__":
    main()
