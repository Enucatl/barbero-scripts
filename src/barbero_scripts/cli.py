from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml

from .audio import prepare, speaker_totals
from .migrate import migrate_completed_episode
from .models import Episode
from .publish import publish_preview
from .render import (
    assemble_italian_script,
    assemble_naturalness_chapters,
    assemble_tense_chapters,
    finalize_consistency,
    initialize_italian_review,
    initialize_naturalness_chapters,
    initialize_tense_chapters,
    render_transcript,
    validate_episode,
)
from .scaffold import scaffold_episode
from .transcript import transcribe
from .util import read_json
from .workflow import apply_content_corrections, apply_listener_review, workflow_state


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(prog="barbero")
    commands = result.add_subparsers(dest="command", required=True)
    initialization = commands.add_parser("init", help="scaffold a committed episode directory")
    initialization.add_argument("--number", type=int, required=True)
    initialization.add_argument("--slug", required=True)
    initialization.add_argument("--title", required=True)
    initialization.add_argument("--source", type=Path, required=True)
    initialization.add_argument("--episodes-root", type=Path, default=Path("episodes"))
    initialization.add_argument("--work-root", type=Path, default=Path("~/data/barbero/editorial"))
    initialization.add_argument("--keyterm", action="append", default=[])
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
    status = commands.add_parser("status", help="show the next workflow action or human queue")
    status.add_argument("episode_dir", type=Path)
    status.add_argument("--json", action="store_true", help="emit the workflow status as JSON")
    content = commands.add_parser(
        "apply-content", help="apply accepted content corrections deterministically"
    )
    content.add_argument("episode_dir", type=Path)
    editorial = commands.add_parser(
        "apply-listener-review", help="apply accepted listener recommendations deterministically"
    )
    editorial.add_argument("episode_dir", type=Path)
    migration = commands.add_parser(
        "migrate-v2", help="migrate completed episode 014 or 138 to workflow v2"
    )
    migration.add_argument("episode_dir", type=Path)
    italian = commands.add_parser("assemble-italian", help="assemble verbatim Italian chapters")
    italian.add_argument("episode_dir", type=Path)
    review = commands.add_parser("init-italian-review", help="create approved audio checklist")
    review.add_argument("episode_dir", type=Path)
    naturalness = commands.add_parser(
        "init-naturalness", help="split tense-reviewed English into chapter review files"
    )
    naturalness.add_argument("episode_dir", type=Path)
    spoken = commands.add_parser(
        "assemble-naturalness", help="assemble reviewed naturalness chapters"
    )
    spoken.add_argument("episode_dir", type=Path)
    tense = commands.add_parser(
        "init-tense", help="split corrected English into tense review files"
    )
    tense.add_argument("episode_dir", type=Path)
    tense_assembly = commands.add_parser("assemble-tense", help="assemble reviewed tense chapters")
    tense_assembly.add_argument("episode_dir", type=Path)
    final = commands.add_parser(
        "finalize-consistency", help="accept the assembled script without broader rewriting"
    )
    final.add_argument("episode_dir", type=Path)
    publication = commands.add_parser("publish-preview", help="build the unlisted podcast preview")
    publication.add_argument("--config", type=Path, default=Path("podcast.yaml"))
    publication.add_argument("--episodes-root", type=Path, default=Path("episodes"))
    publication.add_argument(
        "--audio-root", type=Path, default=Path("/scratch/archive/barbero-english")
    )
    publication.add_argument(
        "--output-root",
        type=Path,
        default=Path("/scratch/archive/barbero-english/published"),
    )
    publication.add_argument(
        "--public", action="store_true", help="publish at the hostname root without a token"
    )
    publication.add_argument("--token-file", type=Path, default=Path(".podcast-preview-token"))
    return result


def set_selected_speaker(path: Path, speaker: str) -> None:
    payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    payload["selected_speaker"] = speaker
    path.write_text(yaml.safe_dump(payload, sort_keys=False, allow_unicode=True), encoding="utf-8")


def main() -> None:
    args = parser().parse_args()
    if args.command == "publish-preview":
        try:
            destination = publish_preview(
                args.config,
                args.episodes_root,
                args.audio_root,
                args.output_root,
                None if args.public else args.token_file,
            )
        except (OSError, ValueError, RuntimeError) as error:
            raise SystemExit(str(error)) from error
        print(f"Published preview to {destination}")
        return
    if args.command == "init":
        try:
            destination = scaffold_episode(
                number=args.number,
                slug=args.slug,
                title=args.title,
                source=args.source,
                episodes_root=args.episodes_root,
                work_root=args.work_root,
                keyterms=tuple(args.keyterm),
            )
        except FileExistsError as error:
            raise SystemExit(str(error)) from error
        print(f"Created {destination}")
        return
    if args.command == "validate":
        errors = validate_episode(args.episode_dir)
        if errors:
            for error in errors:
                print(f"ERROR: {error}", file=sys.stderr)
            raise SystemExit(1)
        print("Editorial validation passed")
        return
    if args.command == "status":
        state = workflow_state(args.episode_dir)
        print(json.dumps(state.to_dict(), indent=2) if args.json else state.render())
        return
    if args.command == "apply-content":
        try:
            apply_content_corrections(args.episode_dir)
        except (OSError, ValueError) as error:
            raise SystemExit(str(error)) from error
        print("Created script.content.en.md")
        return
    if args.command == "apply-listener-review":
        try:
            apply_listener_review(args.episode_dir)
        except (OSError, ValueError) as error:
            raise SystemExit(str(error)) from error
        print("Created script.editorial.en.md")
        return
    if args.command == "migrate-v2":
        try:
            migrate_completed_episode(args.episode_dir)
        except (OSError, ValueError) as error:
            raise SystemExit(str(error)) from error
        print("Migrated episode to workflow v2")
        return
    if args.command == "assemble-italian":
        assemble_italian_script(args.episode_dir)
        print("Assembled script.it.md")
        return
    if args.command == "init-italian-review":
        try:
            initialize_italian_review(args.episode_dir)
        except FileExistsError as error:
            raise SystemExit(str(error)) from error
        print("Created approved italian-review.yaml")
        return
    if args.command == "init-naturalness":
        try:
            initialize_naturalness_chapters(args.episode_dir)
        except FileExistsError as error:
            raise SystemExit(str(error)) from error
        print("Created naturalness chapter files")
        return
    if args.command == "assemble-naturalness":
        assemble_naturalness_chapters(args.episode_dir)
        print("Assembled script.spoken.en.md")
        return
    if args.command == "init-tense":
        try:
            initialize_tense_chapters(args.episode_dir)
        except FileExistsError as error:
            raise SystemExit(str(error)) from error
        print("Created tense chapter files")
        return
    if args.command == "assemble-tense":
        assemble_tense_chapters(args.episode_dir)
        print("Assembled script.tense.en.md")
        return
    if args.command == "finalize-consistency":
        finalize_consistency(args.episode_dir)
        print("Created script.en.md")
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
        print("Rendered transcript.it.md")


if __name__ == "__main__":
    main()
