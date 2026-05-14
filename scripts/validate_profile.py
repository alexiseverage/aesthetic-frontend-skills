#!/usr/bin/env python3
"""
validate_profile.py — Validate aesthetic knowledge profile frontmatter.

Usage:
    python scripts/validate_profile.py                    # validate all profiles
    python scripts/validate_profile.py knowledge/aesthetics/y2k.md  # validate one

Validates YAML frontmatter in knowledge/aesthetics/*.md against
skills/aesthetic-research/knowledge/schema.json.

Requirements: pyyaml (pip install pyyaml). No other third-party deps.
"""

import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional

try:
    import yaml
except ImportError:
    sys.exit("Error: pyyaml is required. Install it with: pip install pyyaml")


REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = REPO_ROOT / "skills" / "aesthetic-research" / "knowledge" / "schema.json"
PROFILES_DIR = REPO_ROOT / "knowledge" / "aesthetics"

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)


def load_schema() -> Dict:
    if not SCHEMA_PATH.exists():
        sys.exit(f"Schema not found at {SCHEMA_PATH}")
    with SCHEMA_PATH.open() as f:
        return json.load(f)


def extract_frontmatter(path: Path) -> Optional[Dict]:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None
    return yaml.safe_load(match.group(1))


def validate_against_schema(data: Dict, schema: Dict) -> List[str]:
    errors: List[str] = []

    required = schema.get("required", [])
    for field in required:
        if field not in data:
            errors.append(f"Missing required field: '{field}'")

    props = schema.get("properties", {})
    for field, spec in props.items():
        if field not in data:
            continue
        value = data[field]

        # Type check
        expected_type = spec.get("type")
        type_map = {
            "string": str,
            "integer": int,
            "boolean": bool,
            "number": (int, float),
            "array": list,
            "object": dict,
        }
        if expected_type and expected_type in type_map:
            if not isinstance(value, type_map[expected_type]):
                errors.append(
                    f"Field '{field}': expected {expected_type}, got {type(value).__name__}"
                )
                continue

        # Enum check
        if "enum" in spec and value not in spec["enum"]:
            errors.append(
                f"Field '{field}': value '{value}' not in allowed values {spec['enum']}"
            )

        # Pattern check (strings only)
        if "pattern" in spec and isinstance(value, str):
            if not re.fullmatch(spec["pattern"], value):
                errors.append(
                    f"Field '{field}': value '{value}' does not match pattern '{spec['pattern']}'"
                )

        # Format check for dates
        if spec.get("format") == "date" and isinstance(value, str):
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
                errors.append(
                    f"Field '{field}': value '{value}' is not a valid ISO 8601 date (YYYY-MM-DD)"
                )

        # Minimum check (integers)
        if "minimum" in spec and isinstance(value, (int, float)):
            if value < spec["minimum"]:
                errors.append(
                    f"Field '{field}': value {value} is below minimum {spec['minimum']}"
                )

    # Slug must match filename
    if "slug" in data:
        return errors  # filename check done at call site

    return errors


def validate_file(path: Path, schema: Dict) -> bool:
    frontmatter = extract_frontmatter(path)
    if frontmatter is None:
        print(f"  SKIP  {path.name} — no YAML frontmatter found")
        return True

    errors = validate_against_schema(frontmatter, schema)

    # Slug-filename consistency
    slug = frontmatter.get("slug")
    if slug and slug != path.stem:
        errors.append(
            f"Field 'slug': value '{slug}' does not match filename '{path.stem}'"
        )

    if errors:
        print(f"  FAIL  {path.name}")
        for err in errors:
            print(f"          {err}")
        return False

    print(f"  OK    {path.name}")
    return True


def main() -> None:
    schema = load_schema()

    if len(sys.argv) > 1:
        paths = [Path(p) for p in sys.argv[1:]]
    else:
        if not PROFILES_DIR.exists():
            sys.exit(f"Profiles directory not found: {PROFILES_DIR}\nRun scripts/doctor.sh to check your setup.")
        paths = sorted(PROFILES_DIR.glob("*.md"))
        if not paths:
            print("No profiles found in knowledge/aesthetics/ — nothing to validate.")
            return

    failed = 0
    for path in paths:
        if not path.exists():
            print(f"  ERROR {path} — file not found")
            failed += 1
            continue
        if not validate_file(path, schema):
            failed += 1

    total = len(paths)
    passed = total - failed
    print(f"\n{passed}/{total} profiles valid", end="")
    if failed:
        print(f", {failed} failed")
        sys.exit(1)
    else:
        print()


if __name__ == "__main__":
    main()
