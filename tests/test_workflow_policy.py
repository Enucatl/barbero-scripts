from pathlib import Path


def test_episode_workflow_requires_native_codex_agents() -> None:
    repository = Path(__file__).resolve().parents[1]
    workflow = repository.joinpath("prompts/episode-workflow.md").read_text(encoding="utf-8")

    assert "Run every language-model editorial and review pass with native Codex agents" in workflow
    assert "Never send these passes through" in workflow
    assert "OpenRouter" in workflow
    assert "Gemini" in workflow
    assert "external model fallback" in workflow
