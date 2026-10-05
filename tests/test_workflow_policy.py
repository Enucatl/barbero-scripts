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
        "source.md",
        "evidence.md",
        "adaptation.md",
        "review-and-decisions.md",
        "final-audience-review.md",
        "publication-summary.md",
    )
    for relative in references:
        assert (skill_dir / "references" / relative).is_file()
        assert f"references/{relative}" in skill


def test_episode_skill_model_routing_and_safety_boundary() -> None:
    repository = Path(__file__).resolve().parents[1]
    skill = repository.joinpath(".agents/skills/produce-barbero-episode/SKILL.md").read_text(
        encoding="utf-8"
    )

    assert "gpt-6-astra` at high reasoning" in skill
    assert "alternative only if the user authorizes it" in skill
    assert "fresh reviewers" in skill
    assert "Commit, push, publish" in skill
