from pathlib import Path

import pytest

from barbero_scripts.models import EditSegment, Episode
from barbero_scripts.transcript import (
    Utterance,
    apply_corrections,
    deepgram_options,
    utterances_from_deepgram,
)
from barbero_scripts.util import object_hash


def test_utterance_ids_and_original_timestamps_are_stable() -> None:
    response = {
        "results": {"utterances": [{"start": 1, "end": 2, "transcript": "Ciao", "confidence": 0.9}]}
    }
    items = utterances_from_deepgram(response, [EditSegment(0, 5, 10, 15)])
    assert (items[0].id, items[0].original_start, items[0].original_end) == ("U-00001", 11, 12)


def test_correction_merge_preserves_id_and_records_diff() -> None:
    item = Utterance("U-00001", 0, 1, 10, 11, "princip", 0.7, ("low-confidence",))
    result, diff = apply_corrections([item], {"U-00001": {"text": "Princip", "reviewed": True}})
    assert result[0].id == item.id
    assert result[0].flags == ()
    assert diff == [{"id": "U-00001", "before": "princip", "after": "Princip"}]


def test_review_without_text_keeps_original_and_clears_flags() -> None:
    item = Utterance("U-00001", 0, 1, 10, 11, "Princip", 0.7, ("low-confidence",))
    result, diff = apply_corrections([item], {"U-00001": {"reviewed": True}})
    assert result[0].text == "Princip"
    assert result[0].flags == ()
    assert diff == []


def test_unknown_correction_is_rejected() -> None:
    with pytest.raises(ValueError):
        apply_corrections([], {"U-99999": {"text": "x"}})


def test_transcription_cache_key_changes_with_options() -> None:
    episode = Episode("x", 1, "x", Path("a"), Path("b"), keyterms=("Sarajevo",))
    assert object_hash(deepgram_options(episode)) != object_hash(
        deepgram_options(Episode("x", 1, "x", Path("a"), Path("b")))
    )
