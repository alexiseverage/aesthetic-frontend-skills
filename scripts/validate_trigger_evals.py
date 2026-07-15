#!/usr/bin/env python3
"""Validate lightweight trigger-eval fixtures for public Agent Skills."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_FIXTURE_DIR = Path("tests/trigger-evals")


def public_skill_names(root: Path) -> set[str]:
    manifest_path = root / "skills.sh.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise ValueError("missing skills.sh.json") from None
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid skills.sh.json JSON: {exc}") from None

    names: set[str] = set()
    for grouping in manifest.get("groupings", []):
        for skill in grouping.get("skills", []):
            if isinstance(skill, str):
                names.add(skill)
    return names


def skill_directories(root: Path) -> set[str]:
    return {path.parent.name for path in (root / "skills").glob("*/SKILL.md")}


def load_json(path: Path) -> tuple[dict[str, Any] | None, str | None]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return None, f"invalid JSON: {exc}"
    if not isinstance(data, dict):
        return None, "fixture root must be an object"
    return data, None


def validate_example(example: Any, field: str) -> list[str]:
    errors: list[str] = []
    if not isinstance(example, dict):
        return [f"{field} entries must be objects"]
    request = example.get("request")
    reason = example.get("reason")
    if not isinstance(request, str) or not request.strip():
        errors.append(f"{field} entry missing non-empty request")
    if not isinstance(reason, str) or not reason.strip():
        errors.append(f"{field} entry missing non-empty reason")
    if field == "should_not_trigger":
        better_fit = example.get("better_fit")
        if not isinstance(better_fit, str) or not better_fit.strip():
            errors.append("should_not_trigger entry missing non-empty better_fit")
    return errors


def validate_fixture(path: Path) -> tuple[str, list[str], int, int]:
    errors: list[str] = []
    data, load_error = load_json(path)
    if load_error is not None:
        return path.stem, [load_error], 0, 0
    assert data is not None

    skill = data.get("skill")
    if not isinstance(skill, str) or not skill.strip():
        errors.append("missing non-empty skill")
        skill_name = path.stem
    else:
        skill_name = skill
        if skill != path.stem:
            errors.append(f"skill '{skill}' must match fixture filename '{path.stem}'")

    counts = {}
    for field in ("should_trigger", "should_not_trigger"):
        examples = data.get(field)
        if not isinstance(examples, list) or not examples:
            errors.append(f"{field} must be a non-empty array")
            counts[field] = 0
            continue
        counts[field] = len(examples)
        seen_requests: set[str] = set()
        for example in examples:
            errors.extend(validate_example(example, field))
            if isinstance(example, dict) and isinstance(example.get("request"), str):
                request = example["request"].strip().casefold()
                if request in seen_requests:
                    errors.append(f"duplicate {field} request: {example['request']}")
                seen_requests.add(request)

    return skill_name, errors, counts.get("should_trigger", 0), counts.get("should_not_trigger", 0)


def validate(root: Path) -> int:
    public = public_skill_names(root)
    discovered = skill_directories(root)
    fixture_dir = root / DEFAULT_FIXTURE_DIR
    fixtures = sorted(fixture_dir.glob("*.json")) if fixture_dir.exists() else []
    fixture_names = {path.stem for path in fixtures}

    failed = 0
    if public != discovered:
        failed += 1
        print("  FAIL  public skill surface")
        print(f"          skills.sh.json skills differ from skills/*/SKILL.md directories: manifest={sorted(public)} directories={sorted(discovered)}")

    if fixture_names != public:
        failed += 1
        print("  FAIL  trigger eval fixture set")
        print("          fixture set must match skills.sh.json public skills")
        print(f"          missing={sorted(public - fixture_names)} extra={sorted(fixture_names - public)}")

    passed_fixtures = 0
    for path in fixtures:
        skill, errors, positives, negatives = validate_fixture(path)
        if errors:
            failed += 1
            print(f"  FAIL  {path.relative_to(root)}")
            for error in errors:
                print(f"          {error}")
        else:
            passed_fixtures += 1
            print(f"  OK    {path.relative_to(root)}")
            print(f"          {skill}: {positives} should-trigger, {negatives} should-not-trigger")

    print(f"\n{passed_fixtures}/{len(public)} trigger eval fixtures valid", end="")
    if failed:
        print(f", {failed} failed")
        return 1
    print()
    return 0


def main() -> None:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else REPO_ROOT
    try:
        raise SystemExit(validate(root.resolve()))
    except ValueError as exc:
        print(f"  FAIL  trigger eval setup\n          {exc}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
