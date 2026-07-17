from __future__ import annotations

from .models import EditSegment, Segment


def merge_segments(segments: list[Segment], gap: float = 0.25) -> list[Segment]:
    """Merge adjacent retained speech, preserving small natural pauses."""
    if not segments:
        return []
    ordered = sorted(segments, key=lambda item: item.start)
    merged = [ordered[0]]
    for item in ordered[1:]:
        previous = merged[-1]
        if item.speaker == previous.speaker and item.start - previous.end <= gap:
            merged[-1] = Segment(previous.start, max(previous.end, item.end), item.speaker)
        else:
            merged.append(item)
    return merged


def build_edit_map(segments: list[Segment]) -> list[EditSegment]:
    cursor = 0.0
    result: list[EditSegment] = []
    for segment in segments:
        result.append(EditSegment(cursor, cursor + segment.duration, segment.start, segment.end))
        cursor += segment.duration
    return result


def cleaned_to_original(seconds: float, edit_map: list[EditSegment]) -> float:
    for segment in edit_map:
        if segment.cleaned_start <= seconds <= segment.cleaned_end:
            return segment.original_start + seconds - segment.cleaned_start
    if edit_map and 0 <= seconds - edit_map[-1].cleaned_end <= 2.0:
        return edit_map[-1].original_end
    raise ValueError(f"cleaned timestamp {seconds:.3f} is outside the edit map")
