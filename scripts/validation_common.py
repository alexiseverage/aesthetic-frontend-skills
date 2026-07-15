#!/usr/bin/env python3
"""Shared helpers for repository validation scripts."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import yaml

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---(?:\n|$)", re.DOTALL)
SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def split_frontmatter(path: Path) -> tuple[dict[str, Any] | None, str]:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None, text
    data = yaml.safe_load(match.group(1))
    if data is None:
        data = {}
    if not isinstance(data, dict):
        return {"__frontmatter_type_error__": type(data).__name__}, text[match.end() :]
    return data, text[match.end() :]


def is_string_list(value: Any) -> bool:
    return isinstance(value, list) and all(isinstance(item, str) for item in value)


def missing_body_markers(body: str, markers: tuple[tuple[str, tuple[str, ...]], ...]) -> list[str]:
    """Return canonical marker names whose accepted variants are absent from markdown body."""
    missing: list[str] = []
    for canonical, alternatives in markers:
        if not any(alternative in body for alternative in alternatives):
            missing.append(canonical)
    return missing
