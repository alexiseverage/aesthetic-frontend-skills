import json
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_PATH = REPO_ROOT / "skills" / "aesthetic-expansion-kanban" / "SKILL.md"


def _frontmatter_and_body(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    assert text.startswith("---\n"), f"{path} is missing YAML frontmatter"
    _, yaml_text, body = text.split("---", 2)
    return yaml.safe_load(yaml_text), body


def test_aesthetic_expansion_kanban_skill_exists_with_trigger_metadata():
    assert SKILL_PATH.exists()

    metadata, body = _frontmatter_and_body(SKILL_PATH)
    description = metadata["description"]

    assert metadata["name"] == "aesthetic-expansion-kanban"
    assert "Kanban" in description
    assert "aesthetic" in description
    assert "research" in description
    assert "showcase" in description
    assert "visual QA" in description
    assert "## When to Use This Skill" in body


def test_aesthetic_expansion_kanban_skill_is_listed_for_installation():
    manifest = json.loads((REPO_ROOT / "skills.sh.json").read_text(encoding="utf-8"))
    skills = {
        skill
        for grouping in manifest["groupings"]
        for skill in grouping["skills"]
    }

    assert "aesthetic-expansion-kanban" in skills


def test_aesthetic_expansion_kanban_skill_documents_required_pipeline():
    text = SKILL_PATH.read_text(encoding="utf-8")

    for required in [
        "research collection -> synthesis -> skills repo implementation -> website showcase implementation -> visual QA -> final integration review",
        "Pinterest-public-first",
        "official source galleries",
        "patent/manufacturing references",
        "casino ephemera",
        "<skills_repo>",
        "<showcase_repo>",
        "<topic>",
        "worktree",
        "verification gates",
        "live-deploy truthfulness",
        "Do not install into `~/.hermes/skills`",
    ]:
        assert required in text


def test_aesthetic_expansion_kanban_skill_has_exact_kanban_decomposition_pattern():
    text = SKILL_PATH.read_text(encoding="utf-8")

    for task_title in [
        "research: <slug> visual evidence corpus",
        "research: <topic> taxonomy + boundaries",
        "synthesize <topic> aesthetics implementation brief",
        "implement <slug-list> aesthetic literacy entries",
        "implement website showcase components for <slug-list>",
        "visual QA <topic> showcases",
        "create reusable Kanban skill for <topic> aesthetic expansion pipeline",
        "final integration review and deployment readiness",
    ]:
        assert task_title in text

    assert "parents=[research task ids]" in text
    assert "parents=[synthesis task id]" in text
    assert "parents=[website implementation task id]" in text
