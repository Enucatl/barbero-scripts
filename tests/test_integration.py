import json
import subprocess
from pathlib import Path

from barbero_scripts.audio import prepare
from barbero_scripts.models import Episode
from barbero_scripts.transcript import transcribe


def test_prepare_and_import_mocked_transcription(tmp_path: Path) -> None:
    source = tmp_path / "fixture.wav"
    subprocess.run(
        [
            "ffmpeg",
            "-v",
            "error",
            "-f",
            "lavfi",
            "-i",
            "sine=frequency=440:duration=1",
            str(source),
        ],
        check=True,
    )
    diarization = tmp_path / "diarization.json"
    diarization.write_text(
        json.dumps({"segments": [{"start": 0, "end": 0.9, "speaker": "SPEAKER_00"}]})
    )
    episode = Episode("fixture", 0, "Fixture", source, tmp_path / "work")
    manifest = prepare(episode, diarization)
    assert manifest["selected_speaker"] == "SPEAKER_00"
    assert not (episode.work_dir / "diarization.wav").exists()

    response = tmp_path / "response.json"
    response.write_text(
        json.dumps({"results": {"utterances": [{"start": 0, "end": 0.8, "transcript": "Prova"}]}})
    )
    assert len(transcribe(episode, response)["results"]["utterances"]) == 1
