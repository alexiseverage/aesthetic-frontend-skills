import json
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def run_validator(*args: str, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "validate_trigger_evals.py"), *args],
        cwd=cwd or REPO_ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


def test_trigger_eval_fixtures_match_public_skill_surface():
    fixtures_dir = REPO_ROOT / "tests" / "trigger-evals"
    fixtures = sorted(fixtures_dir.glob("*.json"))
    fixture_names = {path.stem for path in fixtures}
    manifest = json.loads((REPO_ROOT / "skills.sh.json").read_text(encoding="utf-8"))
    public_skills = {
        skill
        for grouping in manifest["groupings"]
        for skill in grouping["skills"]
    }

    assert fixture_names == public_skills

    for path in fixtures:
        data = json.loads(path.read_text(encoding="utf-8"))
        assert data["skill"] == path.stem
        assert len(data["should_trigger"]) >= 4
        assert len(data["should_not_trigger"]) >= 2


def test_validate_trigger_evals_reports_public_fixture_summary():
    result = run_validator()

    assert result.returncode == 0, result.stdout + result.stderr
    assert "2/2 trigger eval fixtures valid" in result.stdout
    assert "aesthetic-literacy: " in result.stdout
    assert "aesthetic-application: " in result.stdout


def test_validate_trigger_evals_rejects_unknown_fixture_skill(tmp_path: Path):
    skills_dir = tmp_path / "skills" / "known-skill"
    skills_dir.mkdir(parents=True)
    (skills_dir / "SKILL.md").write_text(
        "---\nname: known-skill\ndescription: Known test skill.\n---\n\nBody.\n",
        encoding="utf-8",
    )
    (tmp_path / "skills.sh.json").write_text(
        json.dumps({"groupings": [{"title": "Test", "skills": ["known-skill"]}]}),
        encoding="utf-8",
    )
    fixtures_dir = tmp_path / "tests" / "trigger-evals"
    fixtures_dir.mkdir(parents=True)
    (fixtures_dir / "unknown-skill.json").write_text(
        json.dumps(
            {
                "skill": "unknown-skill",
                "should_trigger": [{"request": "Use the known skill.", "reason": "positive"}],
                "should_not_trigger": [
                    {
                        "request": "Do something else.",
                        "better_fit": "out of scope",
                        "reason": "negative",
                    }
                ],
            }
        ),
        encoding="utf-8",
    )

    result = run_validator(str(tmp_path))

    assert result.returncode == 1
    assert "fixture set must match skills.sh.json public skills" in result.stdout
    assert "unknown-skill" in result.stdout
