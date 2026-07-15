import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PUBLIC_SKILLS = {"aesthetic-literacy", "aesthetic-application"}
REMOVED_PUBLIC_SKILLS = {
    "aesthetic" + "-expansion" + "-kanban",
    "aesthetic" + "-research",
    "image" + "-analysis",
    "asset" + "-creation",
}


def test_public_skill_directories_are_exactly_the_two_core_skills():
    discovered = {
        path.parent.name
        for path in (REPO_ROOT / "skills").glob("*/SKILL.md")
    }

    assert discovered == PUBLIC_SKILLS


def test_skills_manifest_lists_exactly_the_two_core_skills():
    manifest = json.loads((REPO_ROOT / "skills.sh.json").read_text(encoding="utf-8"))
    listed = {
        skill
        for grouping in manifest["groupings"]
        for skill in grouping["skills"]
    }

    assert listed == PUBLIC_SKILLS


def test_removed_public_skills_are_absent_from_repository_text():
    searchable_roots = [
        REPO_ROOT / ".hermes" / "plans",
        REPO_ROOT / "copilot-instructions.template.md",
        REPO_ROOT / "docs",
        REPO_ROOT / "knowledge",
        REPO_ROOT / "scripts",
        REPO_ROOT / "skills",
        REPO_ROOT / "tests",
        REPO_ROOT / "README.md",
        REPO_ROOT / "skills.sh.json",
    ]
    suffixes = {".md", ".json", ".py", ".sh"}

    paths = []
    for root in searchable_roots:
        if root.is_file():
            paths.append(root)
        elif root.exists():
            paths.extend(path for path in root.rglob("*") if path.suffix in suffixes)

    failures = []
    for path in sorted(paths):
        if path == Path(__file__):
            continue
        text = path.read_text(encoding="utf-8")
        for removed in REMOVED_PUBLIC_SKILLS:
            if removed in text:
                failures.append(f"{path.relative_to(REPO_ROOT)} contains {removed}")

    assert not failures
