#!/usr/bin/env python3
"""
validate_profile.py — Validate aesthetic knowledge profile frontmatter.

Usage:
    python scripts/validate_profile.py
    python scripts/validate_profile.py knowledge/aesthetics/y2k.md
    python scripts/validate_profile.py --allow-missing-frontmatter notes/plain.md
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path
from typing import Any

try:
    from jsonschema import Draft7Validator, FormatChecker
except ImportError:
    sys.exit("Error: jsonschema is required. Install it with: pip install jsonschema")

try:
    import yaml  # noqa: F401 - imported to preserve clear dependency failure with validation_common
except ImportError:
    sys.exit("Error: pyyaml is required. Install it with: pip install pyyaml")

from validation_common import missing_body_markers, split_frontmatter

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = REPO_ROOT / "skills" / "aesthetic-research" / "knowledge" / "schema.json"
PROFILES_DIR = REPO_ROOT / "knowledge" / "aesthetics"
TARGET_BODY_SECTIONS = (
    ("## Dimension Synthesis", ("## Dimension Synthesis",)),
    ("## Image Descriptions", ("## Image Descriptions", "no image corpus was collected")),
    ("## Analysis", ("## Analysis",)),
    ("## Connections", ("## Connections",)),
    ("## Research Updates", ("## Research Updates",)),
)


def load_schema() -> dict[str, Any]:
    if not SCHEMA_PATH.exists():
        sys.exit(f"Schema not found at {SCHEMA_PATH}")
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def schema_errors(data: dict[str, Any], schema: dict[str, Any]) -> list[str]:
    validator = Draft7Validator(schema, format_checker=FormatChecker())
    errors: list[str] = []
    for error in sorted(validator.iter_errors(data), key=lambda item: list(item.path)):
        path = ".".join(str(part) for part in error.path)
        if path:
            errors.append(f"Field '{path}': {error.message}")
        else:
            errors.append(error.message)
    return errors


def parse_iso_date(value: Any) -> date | None:
    if not isinstance(value, str):
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        return None


def cross_field_errors(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    evidence_level = data.get("evidence_level")
    image_count = data.get("image_count")
    if isinstance(image_count, int):
        if evidence_level == "standard" and image_count < 10:
            errors.append("standard evidence requires image_count >= 10")
        if evidence_level == "limited" and image_count >= 10:
            errors.append("limited evidence requires image_count < 10")

    first_researched = parse_iso_date(data.get("first_researched"))
    last_updated = parse_iso_date(data.get("last_updated"))
    if first_researched and last_updated and last_updated < first_researched:
        errors.append("last_updated must be on or after first_researched")
    return errors


def target_schema_warnings(body: str) -> list[str]:
    return [f"Missing target body section: '{section}'" for section in missing_body_markers(body, TARGET_BODY_SECTIONS)]


def validate_file(
    path: Path,
    schema: dict[str, Any],
    *,
    allow_missing_frontmatter: bool,
    schema_mode: str,
) -> tuple[bool, int]:
    frontmatter, body = split_frontmatter(path)
    if frontmatter is None:
        print(f"  SKIP  {path.name} — no YAML frontmatter found" if allow_missing_frontmatter else f"  FAIL  {path.name}")
        if not allow_missing_frontmatter:
            print("          no YAML frontmatter found")
        return allow_missing_frontmatter, 0
    if "__frontmatter_type_error__" in frontmatter:
        print(f"  FAIL  {path.name}")
        print(f"          YAML frontmatter must be an object, got {frontmatter['__frontmatter_type_error__']}")
        return False, 0

    errors = schema_errors(frontmatter, schema)

    slug = frontmatter.get("slug")
    if isinstance(slug, str) and slug != path.stem:
        errors.append(f"Field 'slug': value '{slug}' does not match filename '{path.stem}'")

    errors.extend(cross_field_errors(frontmatter))

    warnings: list[str] = []
    if schema_mode != "legacy":
        warnings = target_schema_warnings(body)
        if schema_mode == "strict":
            errors.extend(warnings)
            warnings = []

    if errors:
        print(f"  FAIL  {path.name}")
        for error in errors:
            print(f"          {error}")
        return False, 0

    if warnings:
        print(f"  WARN  {path.name}")
        for warning in warnings:
            print(f"          {warning}")
        return True, len(warnings)

    print(f"  OK    {path.name}")
    return True, 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate aesthetic profile frontmatter")
    parser.add_argument(
        "--allow-missing-frontmatter",
        action="store_true",
        help="Skip markdown files without YAML frontmatter instead of failing them",
    )
    parser.add_argument(
        "--schema-mode",
        choices=("legacy", "warn", "strict"),
        default="legacy",
        help="Target schema enforcement: legacy default, warn-only audit, or strict failures",
    )
    parser.add_argument("paths", nargs="*", help="Profile markdown files to validate")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    schema = load_schema()

    if args.paths:
        paths = [Path(p) for p in args.paths]
    else:
        if not PROFILES_DIR.exists():
            sys.exit(f"Profiles directory not found: {PROFILES_DIR}\nRun scripts/doctor.sh to check your setup.")
        paths = sorted(PROFILES_DIR.glob("*.md"))
        if not paths:
            print("No profiles found in knowledge/aesthetics/ — nothing to validate.")
            return

    failed = 0
    warning_count = 0
    for path in paths:
        if not path.exists():
            print(f"  ERROR {path} — file not found")
            failed += 1
            continue
        valid, warnings = validate_file(
            path,
            schema,
            allow_missing_frontmatter=args.allow_missing_frontmatter,
            schema_mode=args.schema_mode,
        )
        warning_count += warnings
        if not valid:
            failed += 1

    total = len(paths)
    passed = total - failed
    print(f"\n{passed}/{total} profiles valid", end="")
    if failed:
        print(f", {failed} failed")
        sys.exit(1)
    if warning_count:
        print(f", {warning_count} target-schema warning(s)")
    else:
        print()


if __name__ == "__main__":
    main()
