import pytest

from barbero_scripts.models import Segment
from barbero_scripts.timeline import build_edit_map, cleaned_to_original, merge_segments


def test_timeline_maps_across_removed_segments() -> None:
    edit_map = build_edit_map([Segment(10, 20, "A"), Segment(30, 35, "A")])
    assert cleaned_to_original(5, edit_map) == 15
    assert cleaned_to_original(12, edit_map) == 32


def test_timeline_rejects_outside_timestamp() -> None:
    with pytest.raises(ValueError):
        cleaned_to_original(20, build_edit_map([Segment(1, 2, "A")]))


def test_timeline_tolerates_small_codec_endpoint_drift() -> None:
    edit_map = build_edit_map([Segment(10, 20, "A")])
    assert cleaned_to_original(11.5, edit_map) == 20


def test_merge_adjacent_segments_only_for_same_speaker() -> None:
    result = merge_segments([Segment(0, 1, "A"), Segment(1.1, 2, "A"), Segment(2.1, 3, "B")])
    assert result == [Segment(0, 2, "A"), Segment(2.1, 3, "B")]
