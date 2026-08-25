# Exact migration targets intentionally mirror already committed prose.
# ruff: noqa: E501

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import yaml

from .util import file_hash
from .workflow import apply_content_corrections, dump_yaml, text_hash

HEADING = re.compile(r"^## \d+\.\s+.+$", re.MULTILINE)
COVERAGE = re.compile(r"<!-- chapter: CH-\d{3}; transcript: U-\d{5}[–-]U-\d{5} -->")


def _records(path: Path) -> list[dict[str, Any]]:
    value = yaml.safe_load(path.read_text(encoding="utf-8")) or []
    if not isinstance(value, list):
        raise ValueError(f"{path.name} must contain a list")
    return value


def _utterance_number(value: Any) -> int | None:
    matches = re.findall(r"U-(\d{5})", str(value))
    return int(matches[0]) if matches else None


def _chapter_for(record: dict[str, Any], chapters: list[dict[str, Any]]) -> str | None:
    for key in ("barbero_utterances", "transcript", "utterances"):
        number = _utterance_number(record.get(key))
        if number is not None:
            break
    else:
        return None
    for chapter in chapters:
        if int(str(chapter["start"])[2:]) <= number <= int(str(chapter["end"])[2:]):
            return str(chapter["id"])
    return None


def _chapter_bodies(text: str) -> dict[str, str]:
    headings = list(HEADING.finditer(text))
    result: dict[str, str] = {}
    for index, heading in enumerate(headings, 1):
        end = headings[index].start() if index < len(headings) else len(text)
        section = text[heading.end() : end]
        coverage = COVERAGE.search(section)
        if coverage is None:
            raise ValueError(f"CH-{index:03d} has no coverage marker")
        result[f"CH-{index:03d}"] = section[coverage.end() :].strip()
    return result


def _add_markers_to_chapter_files(directory: Path, accepted: dict[str, str]) -> None:
    for stage in ("tense", "naturalness"):
        for chapter_id, correction_id in accepted.items():
            path = directory / stage / f"{chapter_id}.md"
            text = path.read_text(encoding="utf-8").rstrip()
            marker = f"<!-- content-correction: {correction_id} -->"
            if marker not in text:
                path.write_text(f"{text}\n\n{marker}\n", encoding="utf-8")


def _listener_assessment(number: int) -> tuple[dict[str, Any], str]:
    if number == 138:
        return (
            {
                "must_understand": [
                    "Religious and constitutional conflict made Charles I's rule ungovernable.",
                    "Fear of social revolution fractured the coalition that had resisted the king.",
                ],
                "must_remember": [
                    "The execution scaffold frames the story.",
                    "The Scottish crisis forced Charles to recall Parliament.",
                ],
                "experience": [
                    "Escalation from court remoteness to civil war and the return to execution."
                ],
                "argument_or_narrative_spine": (
                    "A reform coalition defeats arbitrary rule, then splits when political reform "
                    "appears to threaten social order."
                ),
                "strengths_to_preserve": [
                    "Execution opening and closing return",
                    "soap-monopoly scene",
                    "Scottish crowd",
                    "Strafford trial",
                    "social-revolution argument",
                ],
            },
            "The English Civil War: How Reform Became Revolution",
        )
    return (
        {
            "must_understand": [
                "The supposed right of the first night is a late legend, not a medieval law.",
                "The myth manufactures evidence by misreading taxes, names, and later stories.",
            ],
            "must_remember": [
                "The boot trick and the friars' false tithe",
                "The false-etymology mechanism and Orwell's ending",
            ],
            "experience": ["A historical investigation in which each expected source fails."],
            "argument_or_narrative_spine": (
                "A detective search follows the alleged custom through missing medieval evidence "
                "and the later stories that taught Europe to believe it."
            ),
            "strengths_to_preserve": [
                "boot trick",
                "friars' false tithe",
                "false etymologies",
                "Orwell ending",
            ],
        },
        "The Myth of the Right of the First Night (*Ius Primae Noctis*)",
    )


def _script_recommendation(
    identifier: str,
    issue_type: str,
    listener_need: str,
    chapter_id: str,
    current: str,
    proposed: str,
    reason: str,
    preserves: list[str],
    outline_sections: list[int],
    quotation_refs: list[str] | None = None,
) -> dict[str, Any]:
    result = {
        "id": identifier,
        "issue_type": issue_type,
        "listener_need": listener_need,
        "severity": "recommended",
        "outline_sections": outline_sections,
        "target": {
            "kind": "script",
            "chapter_id": chapter_id,
            "current_text": current,
            "current_text_sha256": text_hash(current),
        },
        "proposed_text": proposed,
        "reason": reason,
        "preserves": preserves,
        "quotation_refs": quotation_refs or [],
        "decision": "pending",
        "decision_note": None,
    }
    if issue_type == "quotation-audio":
        result["quotation_treatment"] = "excerpt-with-paraphrase"
    return result


def _episode_recommendations(number: int, spoken: str, audience_title: str) -> list[dict[str, Any]]:
    title = {
        "id": "ER-001",
        "issue_type": "title-accessibility",
        "listener_need": "remember",
        "severity": "recommended",
        "outline_sections": [1],
        "target": {
            "kind": "title",
            "current_text": None,
            "current_text_sha256": text_hash(""),
        },
        "proposed_text": audience_title,
        "reason": "Lead with an English description and keep specialized wording secondary.",
        "preserves": ["immutable Italian source title"],
        "quotation_refs": [],
        "decision": "pending",
        "decision_note": None,
    }
    if number == 138:
        specifications = [
            (
                "ER-002",
                "lecture-residue",
                "experience",
                "CH-001",
                "So you’ve paid for a ticket\nto a lecture that will be very demanding, longer than usual and more complex than usual. Right now you think that’s what you want. We’ll see. ",
                "",
                "Remove ticket, applause, and lecture-length framing that no longer addresses the listener.",
                ["Barbero's dry self-deprecation", "the distinction between war and civil war"],
                [1],
            ),
            (
                "ER-003",
                "lecture-residue",
                "understand",
                "CH-001",
                "In any case, tonight we are talking about\nperhaps the least known of the three civil wars that we will cover in these three stages:\nthe English Civil War of the seventeenth century.",
                "Our subject is the English Civil War of the seventeenth century, perhaps the least known of these conflicts.",
                "Remove event-series and three-stage framing while naming the episode's subject directly.",
                ["the immediate turn to the execution scaffold"],
                [1],
            ),
            (
                "ER-004",
                "lecture-residue",
                "experience",
                "CH-007",
                "I hesitated for a long time over whether to give this example because,\nas I told you, tonight’s lecture will be rather long. Then I decided to give it anyway, because\none does not imagine that such things could happen in a seventeenth-century kingdom.",
                "Here is one example, because it is hard to imagine such a thing happening in a seventeenth-century kingdom.",
                "Keep the memorable soap-monopoly scene but remove obsolete lecture-length commentary.",
                ["the soap-monopoly scene", "Barbero's incredulity"],
                [7],
            ),
            (
                "ER-005",
                "orientation",
                "understand",
                "CH-009",
                "It is a spark struck in the other kingdom of which Charles is king, Scotland. In the Kingdom of\nScotland too. But Scotland is Calvinist.",
                "The spark that turns the English crisis into a war begins in Charles’s other kingdom: Scotland. Scotland is Calvinist.",
                "Reset the causal chain before the Scottish crisis and state why this theater matters.",
                ["Scotland as the trigger", "the religious contrast"],
                [9],
            ),
            (
                "ER-006",
                "lecture-residue",
                "remember",
                "CH-010",
                "Another who insists is someone I have not yet mentioned but whom, in this\nlast half hour—no, God willing, in these final fifteen or twenty minutes—we’ll mention again, because he is the protagonist of a dramatic episode: the Earl of Strafford, governor of\nIreland, one of the king’s chief and most trusted advisers.",
                "Another is the Earl of Strafford, governor of Ireland and one of the king’s chief and most trusted advisers. He will become the protagonist of a dramatic episode.",
                "Introduce Strafford by role and future importance without the live running-time callback.",
                ["Strafford's later dramatic role"],
                [10],
            ),
            (
                "ER-007",
                "proper-name-hierarchy",
                "remember",
                "CH-012",
                "Meanwhile, remember William Prynne,\nthe Puritan printer whose ears were cut off, cheeks branded, and who was imprisoned for\nlife?",
                "Meanwhile William Prynne returns—the Puritan printer whose ears were cut off, whose cheeks were branded, and who was imprisoned for life.",
                "Reintroduce Prynne through the scene the listener is most likely to remember.",
                ["Prynne's identity", "the later reversal involving Laud"],
                [12],
            ),
            (
                "ER-008",
                "quotation-audio",
                "understand",
                "CH-011",
                "So the chancellor speaks\nfor him, saying: “My lords, and you, the knights, citizens, and burgesses of the House of\nCommons: I doubt not but you rejoice at this day’s meeting ...; and good reason you have so\nto do, and with all humbleness of heart to acknowledge the great goodness of his majesty who,\nsequestering the memory of all former discouragements in preceding assemblies, is now, out of\na fatherly affection to his people and a confidence that they will not be failing in their\nduty to him, pleased graciously to invite you and all his loving subjects to a sacred unity\nof hearts and affection in the service of him and of the commonwealth.”",
                "So the chancellor speaks for him. He praises the king for setting aside earlier clashes and summoning Parliament out of “a fatherly affection to his people,” calling for “a sacred unity of hearts and affection in the service of him and of the commonwealth.”",
                "Shorten Q-014 while preserving its paternal appeal and call for political unity.",
                ["the king's appeal", "exact surviving source words"],
                [11],
                ["Q-014"],
            ),
            (
                "ER-009",
                "quotation-audio",
                "understand",
                "CH-013",
                "He lets Parliament know that if this continues—and here I\nquote—“... at last the common people (who in the mean time must be flattered, and to whom\nlicense must be given in all their wild humours, how contrary soever to established law, or\ntheir own real good) discover this arcanum imperii, that all this was done by them, but not\nfor them, grow weary of journey-work, and set up for themselves, call parity and independence\nliberty, devour that estate which had devoured the rest; destroy all rights and properties,\nall distinctions of families and merit; and by this means this splendid and excellently\ndistinguished form of government end in a dark equal chaos of confusion, and the long line of\nour many noble ancestors in a Jack Cade, or a Wat Tyler.”",
                "He warns Parliament that once common people realize the reforms were done by them but not for them, they may “set up for themselves,” destroy “all rights and properties,” and reduce government to “a dark equal chaos of confusion.”",
                "Shorten Q-017 while preserving its fear that popular mobilization will destroy property and hierarchy.",
                ["fear of popular revolution", "exact surviving source words"],
                [13],
                ["Q-017"],
            ),
            (
                "ER-010",
                "spine",
                "remember",
                "CH-013",
                "Thus war begins, amid a thousand fears, because everyone wants victory but\nfears a social revolution, which nobody wants.",
                "Thus war begins amid a thousand fears: everyone wants victory, but fear of social revolution now fractures the reform coalition.",
                "Make explicit the argument that fear of social revolution divides the king's opponents.",
                ["Barbero's causal claim", "the coalition fracture"],
                [13],
            ),
        ]
    else:
        specifications = [
            (
                "ER-002",
                "terminology",
                "understand",
                "CH-001",
                "Tonight's subject may be the best-known of the three we're covering in this series. I think we all have in mind this image that we associate with the Middle Ages, the *ius primae noctis*. I know, I just contradicted myself: we all know the image, but let's define it anyway.",
                "Tonight’s subject is the so-called right of the first night—*ius primae noctis*. The image is familiar, but let’s define it before using the Latin name.",
                "Introduce the English concept before asking listeners to retain the Latin term.",
                ["Barbero's opening definition", "the distinction between image and evidence"],
                [1],
            ),
            (
                "ER-003",
                "proper-name-hierarchy",
                "remember",
                "CH-001",
                "How many places have this story in their memory, in their tradition? Fiuggi; Sant'Agata di Puglia; Roccascalegna in Abruzzo; several villages in Liguria, Montalto Ligure, Onzo; several villages in Piedmont, Nizza Monferrato, Rocca Grimalda; even Ivrea, where the Ivrea Carnival—you know, the carnival where they throw oranges—is said today to originate in an episode in which an evil tyrant demands the *ius primae noctis* until a girl cleverer than the others rebels: Violetta, the beautiful miller's daughter.",
                "Versions of the story appear in towns across Italy. Ivrea’s orange-throwing carnival, for example, is now said to recall a clever miller’s daughter named Violetta rebelling against a tyrant who demanded the *ius primae noctis*.",
                "Condense incidental place names while preserving the vivid Ivrea example and its later dating clue.",
                ["Ivrea", "Violetta", "the spread of local legends"],
                [1],
            ),
            (
                "ER-004",
                "spine",
                "understand",
                "CH-002",
                "Let me quickly suggest two places to look. We have all this testimony, all these sources handed down from the Middle Ages. Where should the *ius primae noctis* show up?",
                "The investigation begins with a simple test: if this right existed, where should it appear in the sources handed down from the Middle Ages? Let’s start with two places.",
                "Make the detective method audible at the first major transition.",
                ["source-based inquiry", "Barbero's question"],
                [2],
            ),
            (
                "ER-005",
                "spine",
                "remember",
                "CH-006",
                "Picture one of these jurists at a desk piled high with law books. He's extremely learned, but he is also ready to believe anything.",
                "Now the investigation turns: the missing evidence begins to manufacture itself. Picture one of these jurists at a desk piled high with law books. He’s extremely learned, but also ready to believe anything.",
                "Signal the mechanism by which a myth begins producing its own documentary evidence.",
                ["the jurist scene", "Barbero's irony"],
                [6],
            ),
            (
                "ER-006",
                "terminology",
                "understand",
                "CH-006",
                "Medieval taxes had all kinds of local names. In France, a tax collected on various occasions—including, sometimes, marriage—could be called *coillage*. When notaries translated that word into Latin, some wrote *culagium*.",
                "Medieval taxes had all kinds of local names. In France, a tax sometimes collected at marriage was called *coillage*; in notarial Latin, it could become *culagium*.",
                "Keep *culagium* only with an immediate explanation of what the underlying tax was.",
                ["coillage", "culagium", "the false-etymology mechanism"],
                [6],
            ),
            (
                "ER-007",
                "terminology",
                "understand",
                "CH-006",
                "Here's another example. Medieval peasants sometimes paid a levy to feed the lord's horses—basically a fodder tax. In Italy, it was called *fodro*, a word related to the English “fodder.”",
                "Another example begins with a levy for feeding the lord’s horses—a fodder tax called *fodro*, a word related to the English “fodder.”",
                "Keep *fodro* with its useful immediate context and make the etymological setup easier to hear.",
                ["fodro", "the horse levy", "the later false derivation"],
                [6],
            ),
            (
                "ER-008",
                "buried-scenes",
                "experience",
                "CH-002",
                "Once the count sits down and extends his leg, she removes his spurs and deliberately pulls one boot at the wrong angle, leaving it stuck halfway off. Then she runs to safety while he is unable to pursue her. [N-001]",
                "Once the count sits down and extends his leg, she removes his spurs and deliberately pulls one boot at the wrong angle, leaving it stuck halfway off. Then she runs to safety while he is unable to pursue her. [N-001]",
                "Protect the boot trick as a foregrounded scene rather than compressing it with the surrounding examples.",
                ["the boot trick", "N-001"],
                [2],
            ),
            (
                "ER-009",
                "climax-ending",
                "remember",
                "CH-009",
                "That is fantastic because Orwell has identified the mechanism exactly.",
                "That is fantastic because Orwell has identified the mechanism exactly.",
                "Protect Orwell's ending as the final statement of how the myth manufactures a legal past.",
                ["Orwell's ending", "the invention-of-the-past mechanism"],
                [9],
            ),
        ]
    recommendations = [title]
    for specification in specifications:
        current = specification[4]
        if spoken.count(current) != 1:
            raise ValueError(
                f"listener migration target must match exactly once: {specification[0]}"
            )
        recommendations.append(_script_recommendation(*specification))
    return recommendations


def refresh_migrated_listener_review(directory: Path) -> None:
    metadata = yaml.safe_load((directory / "episode.yaml").read_text(encoding="utf-8")) or {}
    number = int(metadata["number"])
    if number not in {14, 138} or metadata.get("workflow_version") != 2:
        raise ValueError("listener migration refresh is limited to migrated episodes 014 and 138")
    assessment, audience_title = _listener_assessment(number)
    spoken = (directory / "script.spoken.en.md").read_text(encoding="utf-8")
    dump_yaml(
        directory / "listener-review.yaml",
        {
            "schema_version": 1,
            "base_script": {"path": "script.spoken.en.md", "sha256": text_hash(spoken)},
            "episode_assessment": assessment,
            "recommendations": _episode_recommendations(number, spoken, audience_title),
        },
    )


def migrate_completed_episode(directory: Path) -> None:
    metadata_path = directory / "episode.yaml"
    metadata = yaml.safe_load(metadata_path.read_text(encoding="utf-8")) or {}
    if metadata.get("workflow_version") == 2:
        raise ValueError(f"already migrated: {directory}")
    number = int(metadata["number"])
    if number not in {14, 138}:
        raise ValueError("initial v2 migration is limited to episodes 014 and 138")

    faithful_path = directory / "script.translation.faithful.en.md"
    corrected_path = directory / "script.corrected.en.md"
    faithful = faithful_path.read_text(encoding="utf-8")
    corrected = corrected_path.read_text(encoding="utf-8")
    faithful_bodies = _chapter_bodies(faithful)
    corrected_bodies = _chapter_bodies(corrected)
    if faithful_bodies.keys() != corrected_bodies.keys():
        raise ValueError("faithful and corrected chapter sets differ")

    chapters = _records(directory / "chapters.yaml")
    quotes_path = directory / "quotes.yaml"
    quotes = _records(quotes_path)
    notes = _records(directory / "accuracy-notes.yaml")
    quotes_by_chapter: dict[str, list[dict[str, Any]]] = {}
    notes_by_chapter: dict[str, list[dict[str, Any]]] = {}
    for quote in quotes:
        chapter = _chapter_for(quote, chapters)
        if chapter is None:
            raise ValueError(f"cannot place quotation {quote.get('id')}")
        quotes_by_chapter.setdefault(chapter, []).append(quote)
    for note in notes:
        chapter = _chapter_for(note, chapters)
        if chapter is None:
            raise ValueError(f"cannot place accuracy note {note.get('id')}")
        notes_by_chapter.setdefault(chapter, []).append(note)

    items: list[dict[str, Any]] = []
    accepted: dict[str, str] = {}
    for chapter_id in faithful_bodies:
        chapter_quotes = quotes_by_chapter.get(chapter_id, [])
        chapter_notes = notes_by_chapter.get(chapter_id, [])
        current = faithful_bodies[chapter_id]
        proposed = corrected_bodies[chapter_id]
        if not chapter_quotes and not chapter_notes and current == proposed:
            continue
        identifier = f"CC-{len(items) + 1:03d}"
        changed = current != proposed
        issue_types = {str(note.get("category")) for note in chapter_notes}
        if chapter_quotes:
            issue_types.add("quotation")
        if not issue_types:
            issue_types.add("translation-ambiguity")
        source_ids: set[str] = set()
        claim_ids: set[str] = set()
        protected: list[str] = []
        for record in [*chapter_quotes, *chapter_notes]:
            source_ids.update(re.findall(r"SRC-\d{3}", str(record)))
            claim_ids.update(re.findall(r"(?<!SR)C-\d{3}", str(record)))
        for quote in chapter_quotes:
            translation = quote.get("translation")
            if (
                quote.get("source_replacement") == "eligible"
                and isinstance(translation, str)
                and translation in proposed
            ):
                protected.append(str(translation))
        items.append(
            {
                "id": identifier,
                "issue_types": sorted(issue_types),
                "target": {
                    "chapter_id": chapter_id,
                    "transcript": [
                        str(chapters[int(chapter_id[3:]) - 1]["start"]),
                        str(chapters[int(chapter_id[3:]) - 1]["end"]),
                    ],
                    "current_text": current,
                    "current_text_sha256": text_hash(current),
                },
                "proposed_text": proposed,
                "reason": "Migrate the already reviewed quotation and accuracy treatment.",
                "evidence_summary": (
                    "Derived from the completed v1 quotation ledger and accuracy decisions; Git "
                    "history retains the pre-migration artifacts."
                ),
                "references": {
                    "quotations": [str(item["id"]) for item in chapter_quotes],
                    "claims": sorted(claim_ids),
                    "sources": sorted(source_ids),
                },
                "recommendation": "apply" if changed else "retain",
                "protected_quote_spans": protected,
                "decision": "accept" if changed else "reject",
                "decision_note": "Migrated from completed v1 human decisions.",
                "migration_references": [str(item["id"]) for item in chapter_notes],
            }
        )
        if changed:
            accepted[chapter_id] = identifier

    dump_yaml(
        directory / "content-corrections.yaml",
        {
            "schema_version": 1,
            "base_script": {
                "path": faithful_path.name,
                "sha256": text_hash(faithful),
            },
            "items": items,
        },
    )
    quote_lines = [
        line
        for line in quotes_path.read_text(encoding="utf-8").splitlines()
        if not re.match(r"^\s*human_reviewed:", line)
    ]
    quotes_path.write_text("\n".join(quote_lines) + "\n", encoding="utf-8")
    apply_content_corrections(directory)
    _add_markers_to_chapter_files(directory, accepted)

    metadata["workflow_version"] = 2
    metadata["audience_title"] = None
    dump_yaml(metadata_path, metadata)
    from .render import assemble_naturalness_chapters, assemble_tense_chapters

    assemble_tense_chapters(directory)
    assemble_naturalness_chapters(directory)
    dump_yaml(
        directory / "transcript-uncertainties.yaml",
        {
            "schema_version": 1,
            "transcription_fingerprint": file_hash(directory / "transcript.it.md"),
            "detection_status": "complete",
            "detection_mode": "migrated-reviewed",
            "acoustic_metadata": "unavailable",
            "items": [],
        },
    )
    refresh_migrated_listener_review(directory)

    for name in (
        "italian-review.yaml",
        "script.translation.en.md",
        "accuracy-notes.yaml",
        "script.corrected.en.md",
        "script.en.md",
    ):
        (directory / name).unlink(missing_ok=True)
