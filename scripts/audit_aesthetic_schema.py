#!/usr/bin/env python3
"""Audit target-schema compliance and dictionary/profile consistency."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from validate_dictionary import dictionary_paths, is_redirect, target_schema_warnings as dictionary_target_warnings
from validate_profile import target_schema_warnings as profile_target_warnings
from validation_common import split_frontmatter

REPO_ROOT = Path(__file__).resolve().parent.parent


def markdown_frontmatter_and_body(path: Path) -> tuple[dict[str, Any] | None, str]:
    frontmatter, body = split_frontmatter(path)
    if frontmatter is None or "__frontmatter_type_error__" in frontmatter:
        return None, body
    return frontmatter, body


def dictionary_dir(root: Path) -> Path:
    return root / "skills" / "aesthetic-literacy" / "aesthetics"


def profiles_dir(root: Path) -> Path:
    return root / "knowledge" / "aesthetics"


def profile_paths(root: Path) -> list[Path]:
    directory = profiles_dir(root)
    if not directory.exists():
        return []
    return sorted(directory.glob("*.md"))


def load_by_slug(paths: list[Path]) -> dict[str, dict[str, Any]]:
    records: dict[str, dict[str, Any]] = {}
    for path in paths:
        frontmatter, _body = markdown_frontmatter_and_body(path)
        if not frontmatter:
            continue
        slug = frontmatter.get("slug")
        if isinstance(slug, str) and slug:
            records[slug] = frontmatter
    return records


def relationship_warnings(dictionary: dict[str, dict[str, Any]], profiles: dict[str, dict[str, Any]]) -> list[str]:
    messages: list[str] = []

    for slug in sorted(dictionary.keys() & profiles.keys()):
        entry = dictionary[slug]
        profile = profiles[slug]
        for field in ("label", "evidence_level", "aliases"):
            if field in entry and field in profile and entry[field] != profile[field]:
                messages.append(f"dictionary/profile mismatch for {slug}: {field}")

    for slug in sorted(dictionary.keys() - profiles.keys()):
        frontmatter = dictionary[slug]
        if is_redirect(frontmatter):
            continue
        messages.append(f"dictionary entry has no research profile: {slug}")

    for slug in sorted(profiles.keys() - dictionary.keys()):
        messages.append(f"research profile has no dictionary entry: {slug}")

    return messages


def audit(root: Path) -> list[str]:
    messages: list[str] = []
    dictionary_files = dictionary_paths(dictionary_dir(root)) if dictionary_dir(root).exists() else []
    profile_files = profile_paths(root)
    known_slugs = {path.stem for path in dictionary_files}

    for path in dictionary_files:
        frontmatter, body = markdown_frontmatter_and_body(path)
        if not frontmatter or is_redirect(frontmatter):
            continue
        for warning in dictionary_target_warnings(frontmatter, body, known_slugs):
            messages.append(f"dictionary target-schema warning for {path.stem}: {warning}")

    for path in profile_files:
        frontmatter, body = markdown_frontmatter_and_body(path)
        if not frontmatter:
            continue
        for warning in profile_target_warnings(body):
            messages.append(f"profile target-schema warning for {path.stem}: {warning}")

    messages.extend(relationship_warnings(load_by_slug(dictionary_files), load_by_slug(profile_files)))
    return messages


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=str(REPO_ROOT), help="Repository root to audit")
    parser.add_argument("--strict", action="store_true", help="Exit non-zero when audit warnings are present")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    root = Path(args.root)
    messages = audit(root)
    for message in messages:
        print(f"  WARN  {message}")
    print(f"{len(messages)} schema audit warning(s)")
    if args.strict and messages:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
