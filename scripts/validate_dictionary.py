#!/usr/bin/env python3
"""Validate curated aesthetic dictionary entries."""

from __future__ import annotations

import sys
from pathlib import Path

from validation_common import is_string_list, split_frontmatter

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DICTIONARY_DIR = REPO_ROOT / "skills" / "aesthetic-literacy" / "aesthetics"
REQUIRED_FIELDS = ("slug", "label", "family")
FULL_ENTRY_LABELS = (
    ("**Palette**:", ("**Palette**:",)),
    ("**Type**:", ("**Type**:",)),
    ("**Texture**:", ("**Texture**:",)),
    ("**Shape**:", ("**Shape**:",)),
    ("**Motion**:", ("**Motion**:",)),
    ("**Spatial**:", ("**Spatial**:",)),
    ("**Cultural markers**:", ("**Cultural markers**:",)),
    ("**Non-negotiables**:", ("**Non-negotiables**:",)),
    ("**Connotation**:", ("**Connotation**:", "## Connotation")),
)


def dictionary_paths(root: Path) -> list[Path]:
    if root.is_file():
        return [root]
    return sorted(root.glob("*.md"))


def is_redirect(frontmatter: dict[str, object]) -> bool:
    return "redirect" in frontmatter or "superseded_by" in frontmatter


def validate_entry(path: Path) -> tuple[list[str], bool]:
    errors: list[str] = []
    frontmatter, body = split_frontmatter(path)
    if frontmatter is None:
        return ["missing YAML frontmatter"], False
    if "__frontmatter_type_error__" in frontmatter:
        return [f"YAML frontmatter must be an object, got {frontmatter['__frontmatter_type_error__']}"], False

    for field in REQUIRED_FIELDS:
        value = frontmatter.get(field)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"Missing required field: '{field}'")

    slug = frontmatter.get("slug")
    if isinstance(slug, str) and slug != path.stem:
        errors.append(f"Field 'slug': value '{slug}' does not match filename '{path.stem}'")

    aliases = frontmatter.get("aliases")
    if aliases is not None and not is_string_list(aliases):
        errors.append("Field 'aliases' must be an array of strings")

    redirect = is_redirect(frontmatter)
    if redirect:
        target = frontmatter.get("redirect") or frontmatter.get("superseded_by")
        if not isinstance(target, str) or not target.strip():
            errors.append("Redirect entries must declare a non-empty redirect or superseded_by target")
        return errors, True

    for canonical_label, alternatives in FULL_ENTRY_LABELS:
        if not any(alternative in body for alternative in alternatives):
            errors.append(f"Missing required body label: '{canonical_label}'")
    return errors, False


def main() -> None:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_DICTIONARY_DIR
    paths = dictionary_paths(root)
    if not paths:
        sys.exit(f"No dictionary entries found under {root}")

    failed = 0
    redirects = 0
    redirect_failures = 0
    full_entries = 0
    full_entry_failures = 0
    for path in paths:
        errors, redirect = validate_entry(path)
        if redirect:
            redirects += 1
        else:
            full_entries += 1
        if errors:
            failed += 1
            if redirect:
                redirect_failures += 1
            else:
                full_entry_failures += 1
            print(f"  FAIL  {path.name}")
            for error in errors:
                print(f"          {error}")
        else:
            kind = "redirect" if redirect else "entry"
            print(f"  OK    {path.name} ({kind})")

    print(f"\n{full_entries} full entries checked")
    print(f"{full_entries - full_entry_failures} full entries valid")
    print(f"{redirects - redirect_failures} redirects valid")
    if redirect_failures:
        print(f"{redirect_failures} redirects failed")
    if full_entry_failures:
        print(f"{full_entry_failures} full entries failed")
    if failed:
        print(f"{failed} dictionary entries failed")
        sys.exit(1)


if __name__ == "__main__":
    main()
