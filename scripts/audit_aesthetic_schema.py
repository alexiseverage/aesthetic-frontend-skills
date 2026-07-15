#!/usr/bin/env python3
"""Audit consistency between canonical aesthetic entries and research profiles."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from validation_common import split_frontmatter

REPO_ROOT = Path(__file__).resolve().parent.parent


def markdown_frontmatter(path: Path) -> dict[str, Any] | None:
    frontmatter, _ = split_frontmatter(path)
    if frontmatter is None or "__frontmatter_type_error__" in frontmatter:
        return None
    return frontmatter


def dictionary_dir(root: Path) -> Path:
    return root / "skills" / "aesthetic-literacy" / "aesthetics"


def profiles_dir(root: Path) -> Path:
    return root / "knowledge" / "aesthetics"


def load_by_slug(directory: Path) -> dict[str, dict[str, Any]]:
    records: dict[str, dict[str, Any]] = {}
    if not directory.exists():
        return records
    for path in sorted(directory.glob("*.md")):
        frontmatter = markdown_frontmatter(path)
        if not frontmatter:
            continue
        slug = frontmatter.get("slug")
        if isinstance(slug, str) and slug:
            records[slug] = frontmatter
    return records


def audit(root: Path) -> list[str]:
    dictionary = load_by_slug(dictionary_dir(root))
    profiles = load_by_slug(profiles_dir(root))
    messages: list[str] = []

    for slug in sorted(dictionary.keys() & profiles.keys()):
        entry = dictionary[slug]
        profile = profiles[slug]
        for field in ("label", "evidence_level", "aliases"):
            if field in entry and field in profile and entry[field] != profile[field]:
                messages.append(f"dictionary/profile mismatch for {slug}: {field}")

    for slug in sorted(dictionary.keys() - profiles.keys()):
        frontmatter = dictionary[slug]
        if "redirect" in frontmatter or "superseded_by" in frontmatter:
            continue
        messages.append(f"dictionary entry has no research profile: {slug}")

    for slug in sorted(profiles.keys() - dictionary.keys()):
        messages.append(f"research profile has no dictionary entry: {slug}")

    return messages


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=str(REPO_ROOT), help="Repository root to audit")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    root = Path(args.root)
    messages = audit(root)
    for message in messages:
        print(f"  WARN  {message}")
    print(f"{len(messages)} schema audit warning(s)")


if __name__ == "__main__":
    main()
