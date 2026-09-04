from pathlib import Path

import yaml


def test_episode_skill_is_explicit_and_references_exist() -> None:
    repository = Path(__file__).resolve().parents[1]
    skill_dir = repository / ".agents/skills/produce-barbero-episode"
    skill = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    metadata = yaml.safe_load((skill_dir / "agents/openai.yaml").read_text(encoding="utf-8"))

    assert metadata["policy"]["allow_implicit_invocation"] is False
    assert "$produce-barbero-episode" in metadata["interface"]["default_prompt"]
    assert not (repository / "prompts/episode-workflow.md").exists()
    references = (
        "transcript-review.md",
        "italian-assembly.md",
        "outline.md",
        "research-target-extraction.md",
        "historical-research.md",
        "quotation-research.md",
        "research-audit.md",
        "faithful-translation.md",
        "quotation-accuracy.md",
        "content-review.md",
        "chapter-tense.md",
        "chapter-naturalness.md",
        "listener-review.md",
        "final-consistency.md",
    )
    for relative in references:
        assert (skill_dir / "references" / relative).is_file()
        assert f"references/{relative}" in skill


def test_episode_skill_model_routing_and_safety_boundary() -> None:
    repository = Path(__file__).resolve().parents[1]
    skill = repository.joinpath(".agents/skills/produce-barbero-episode/SKILL.md").read_text(
        encoding="utf-8"
    )

    for route in (
        "GPT-5.6 Luna, medium",
        "GPT-5.6 Luna, high",
        "GPT-5.6 Sol, high",
    ):
        assert route in skill
    assert "external model" in skill
    assert "Pause at every `human` state" in skill
    assert "Public publication, commits, pushes" in skill
