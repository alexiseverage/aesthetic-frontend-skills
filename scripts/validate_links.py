#!/usr/bin/env python3
"""Validate relative links and image/screenshot references in markdown files."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

REPO_ROOT = Path(__file__).resolve().parent.parent
LINK_RE = re.compile(r"(!?)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
SKIP_DIRS = {".git", ".pytest_cache", "__pycache__", ".ruff_cache", ".worktrees"}


def markdown_paths(root: Path) -> list[Path]:
    if root.is_file():
        return [root]
    paths: list[Path] = []
    for path in root.rglob("*.md"):
        relative_parts = path.relative_to(root).parts
        if any(part in SKIP_DIRS for part in relative_parts):
            continue
        paths.append(path)
    return sorted(paths)


def should_check(target: str) -> bool:
    if not target or target.startswith("#") or target.startswith("mailto:"):
        return False
    parsed = urlparse(target)
    if parsed.scheme or parsed.netloc:
        return False
    return True


def target_error(source: Path, target: str, root: Path) -> str | None:
    path_part = unquote(target.split("#", 1)[0])
    if not path_part:
        return None
    target_path = Path(path_part)
    if target_path.is_absolute():
        return f"absolute filesystem path is not portable in {source}: {target}"

    resolved_root = root.resolve()
    resolved = (source.parent / target_path).resolve()
    try:
        resolved.relative_to(resolved_root)
    except ValueError:
        return f"relative link escapes validation root in {source}: {target}"
    if not resolved.exists():
        return f"broken relative link in {source}: {target}"
    return None


def validate_file(path: Path, root: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    for match in LINK_RE.finditer(text):
        target = match.group(2)
        if not should_check(target):
            continue
        error = target_error(path, target, root)
        if error:
            errors.append(error)
    return errors


def main() -> None:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else REPO_ROOT
    paths = markdown_paths(root)
    if not paths:
        sys.exit(f"No markdown files found under {root}")

    errors: list[str] = []
    for path in paths:
        errors.extend(validate_file(path, root))

    if errors:
        for error in errors:
            print(f"  FAIL  {error}")
        print(f"\n{len(errors)} broken relative link(s) found across {len(paths)} markdown files checked")
        sys.exit(1)

    print(f"{len(paths)} markdown files checked; no broken relative links found")


if __name__ == "__main__":
    main()
