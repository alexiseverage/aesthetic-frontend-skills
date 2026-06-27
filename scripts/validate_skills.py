#!/usr/bin/env python3
"""Validate Agent Skills SKILL.md files for portable repository compliance."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

from validation_common import SLUG_RE, is_string_list, split_frontmatter

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SKILLS_DIR = REPO_ROOT / "skills"


def skill_paths(root: Path) -> list[Path]:
    if root.is_file():
        return [root]
    return sorted(root.glob("*/SKILL.md"))


def metadata_errors(metadata: Any) -> list[str]:
    errors: list[str] = []
    if metadata is None:
        return errors
    if not isinstance(metadata, dict):
        return ["metadata must be an object"]
    hermes = metadata.get("hermes")
    if hermes is None:
        return errors
    if not isinstance(hermes, dict):
        return ["metadata.hermes must be an object"]
    for field in ("tags", "related_skills"):
        if field in hermes and not is_string_list(hermes[field]):
            errors.append(f"metadata.hermes.{field} must be an array of strings")
    return errors


def validate_skill(path: Path) -> list[str]:
    errors: list[str] = []
    frontmatter, body = split_frontmatter(path)
    if frontmatter is None:
        return ["missing YAML frontmatter"]
    if "__frontmatter_type_error__" in frontmatter:
        return [f"YAML frontmatter must be an object, got {frontmatter['__frontmatter_type_error__']}"]

    name = frontmatter.get("name")
    if not isinstance(name, str) or not name.strip():
        errors.append("Missing required field: 'name'")
    elif not SLUG_RE.fullmatch(name):
        errors.append("Field 'name' must use lowercase hyphenated Agent Skills naming")
    elif name != path.parent.name:
        errors.append(f"Field 'name': value '{name}' does not match parent directory '{path.parent.name}'")

    description = frontmatter.get("description")
    if not isinstance(description, str) or not description.strip():
        errors.append("Missing required field: 'description'")
    elif len(description) > 1024:
        errors.append("description is longer than 1024 characters")

    if not body.strip():
        errors.append("body is empty")

    errors.extend(metadata_errors(frontmatter.get("metadata")))
    return errors


def main() -> None:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_SKILLS_DIR
    paths = skill_paths(root)
    if not paths:
        sys.exit(f"No SKILL.md files found under {root}")

    failed = 0
    for path in paths:
        errors = validate_skill(path)
        if errors:
            failed += 1
            print(f"  FAIL  {path}")
            for error in errors:
                print(f"          {error}")
        else:
            print(f"  OK    {path}")

    total = len(paths)
    passed = total - failed
    print(f"\n{passed}/{total} skills valid", end="")
    if failed:
        print(f", {failed} failed")
        sys.exit(1)
    print()


if __name__ == "__main__":
    main()
