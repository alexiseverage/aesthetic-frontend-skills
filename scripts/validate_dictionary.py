#!/usr/bin/env python3
"""Validate curated aesthetic dictionary entries."""

from __future__ import annotations

import argparse
import sys
import unicodedata
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

from validation_common import is_string_list, missing_body_markers, split_frontmatter

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DICTIONARY_DIR = REPO_ROOT / "skills" / "aesthetic-literacy" / "aesthetics"
REQUIRED_FIELDS = ("slug", "label", "family")
TARGET_REQUIRED_FIELDS = ("era", "aliases", "status", "evidence_level", "related", "subsets")
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
TARGET_BODY_SECTIONS = (
    ("## Scope", ("## Scope",)),
    ("## 7-Dimension Profile", ("## 7-Dimension Profile",)),
    ("**Palette**:", ("**Palette**:",)),
    ("**Type**:", ("**Type**:",)),
    ("**Texture**:", ("**Texture**:",)),
    ("**Shape**:", ("**Shape**:",)),
    ("**Motion**:", ("**Motion**:",)),
    ("**Spatial**:", ("**Spatial**:",)),
    ("**Cultural markers**:", ("**Cultural markers**:",)),
    ("## Non-Negotiables", ("## Non-Negotiables", "**Non-negotiables**:")),
    ("## Connotation", ("## Connotation", "**Connotation**:")),
    ("## Related / Subsets", ("## Related / Subsets",)),
    ("## Frontend / UI Guidance", ("## Frontend / UI Guidance",)),
    ("## CSS Translation", ("## CSS Translation",)),
    ("## Typography / Fonts", ("## Typography / Fonts",)),
    ("## Cultural / Ethical Notes", ("## Cultural / Ethical Notes",)),
    ("## Anti-Patterns", ("## Anti-Patterns",)),
)


@dataclass(frozen=True)
class IdentityReference:
    path: Path
    field: str
    canonical_owner: str


def dictionary_paths(root: Path) -> list[Path]:
    if root.is_file():
        return [root]
    return sorted(root.glob("*.md"))


def is_redirect(frontmatter: dict[str, object]) -> bool:
    return "redirect" in frontmatter or "superseded_by" in frontmatter


def normalize_identity(value: str) -> str:
    """Normalize public names across case, whitespace, and punctuation variants."""
    normalized = unicodedata.normalize("NFKC", value).casefold()
    words = "".join(
        character if character.isalnum() else " " for character in normalized
    ).split()
    return " ".join(words)


def redirect_target(frontmatter: dict[str, object]) -> tuple[str, str] | None:
    for field in ("redirect", "superseded_by"):
        value = frontmatter.get(field)
        if isinstance(value, str) and value.strip():
            return field, value
    return None


def collection_errors(paths: list[Path]) -> dict[Path, list[str]]:
    """Validate identities and redirect graphs that require collection-wide context."""
    errors: dict[Path, list[str]] = defaultdict(list)
    records: dict[str, tuple[Path, dict[str, object]]] = {}
    for path in paths:
        frontmatter, _ = split_frontmatter(path)
        if frontmatter is None or "__frontmatter_type_error__" in frontmatter:
            continue
        slug = frontmatter.get("slug")
        if isinstance(slug, str) and slug == path.stem:
            records[slug] = (path, frontmatter)

    redirects = {
        slug: target
        for slug, (_, frontmatter) in records.items()
        if (target := redirect_target(frontmatter)) is not None
    }
    owner_cache: dict[str, str | None] = {}
    reported_cycles: set[frozenset[str]] = set()

    def resolve_owner(slug: str, trail: list[str]) -> str | None:
        if slug in owner_cache:
            return owner_cache[slug]
        redirect = redirects.get(slug)
        if redirect is None:
            owner_cache[slug] = slug
            return slug

        field, target = redirect
        path = records[slug][0]
        if target == slug:
            errors[path].append(
                f"Self-redirect: {path.name} field '{field}' targets its own slug '{slug}'"
            )
            owner_cache[slug] = None
            return None
        if target in trail:
            cycle = trail[trail.index(target) :] + [slug]
            cycle_key = frozenset(cycle)
            if cycle_key not in reported_cycles:
                reported_cycles.add(cycle_key)
                edges = []
                for cycle_slug in cycle:
                    cycle_path, cycle_frontmatter = records[cycle_slug]
                    cycle_field, cycle_target = redirect_target(cycle_frontmatter) or (
                        "redirect",
                        "",
                    )
                    edges.append(
                        f"{cycle_path.name} field '{cycle_field}' -> '{cycle_target}'"
                    )
                message = "Redirect cycle detected: " + "; ".join(edges)
                for cycle_slug in cycle:
                    errors[records[cycle_slug][0]].append(message)
                    owner_cache[cycle_slug] = None
            return None
        if target not in records:
            owner_cache[slug] = None
            return None

        owner = resolve_owner(target, [*trail, slug])
        owner_cache[slug] = owner
        return owner

    for slug in records:
        resolve_owner(slug, [])

    identities: dict[str, list[IdentityReference]] = defaultdict(list)
    for slug, (path, frontmatter) in records.items():
        owner = owner_cache.get(slug)
        if owner is None:
            continue
        values: list[tuple[str, str]] = [("slug", slug)]
        label = frontmatter.get("label")
        if isinstance(label, str) and label.strip():
            values.append(("label", label))
        aliases = frontmatter.get("aliases")
        if isinstance(aliases, list):
            values.extend(
                (f"aliases[{index}]", alias)
                for index, alias in enumerate(aliases)
                if isinstance(alias, str) and alias.strip()
            )
        for field, value in values:
            identity = normalize_identity(value)
            if identity:
                identities[identity].append(IdentityReference(path, field, owner))

    for identity, references in sorted(identities.items()):
        if len({reference.canonical_owner for reference in references}) < 2:
            continue
        ordered = sorted(references, key=lambda reference: (reference.path.name, reference.field))
        details = "; ".join(
            f"{reference.path.name} field '{reference.field}' (resolves to '{reference.canonical_owner}')"
            for reference in ordered
        )
        message = f"Identity '{identity}' conflicts across canonical owners: {details}"
        for path in {reference.path for reference in ordered}:
            errors[path].append(message)

    return errors


def target_schema_warnings(frontmatter: dict[str, object], body: str, known_slugs: set[str]) -> list[str]:
    warnings: list[str] = []
    for field in TARGET_REQUIRED_FIELDS:
        if field not in frontmatter:
            warnings.append(f"Missing target frontmatter field: '{field}'")

    for field in ("era", "status", "evidence_level"):
        value = frontmatter.get(field)
        if value is not None and (not isinstance(value, str) or not value.strip()):
            warnings.append(f"Field '{field}' must be a non-empty string")
    evidence_level = frontmatter.get("evidence_level")
    if isinstance(evidence_level, str) and evidence_level not in {"limited", "standard"}:
        warnings.append("Field 'evidence_level' must be one of: limited, standard")
    for field in ("aliases", "related", "subsets"):
        value = frontmatter.get(field)
        if value is not None and not is_string_list(value):
            warnings.append(f"Field '{field}' must be an array of strings")
    for field in ("related", "subsets"):
        value = frontmatter.get(field)
        if isinstance(value, list) and all(isinstance(item, str) for item in value):
            for slug in value:
                if slug not in known_slugs:
                    warnings.append(f"Field '{field}' references unknown dictionary slug: '{slug}'")

    for section in missing_body_markers(body, TARGET_BODY_SECTIONS):
        warnings.append(f"Missing target body section: '{section}'")
    return warnings


def validate_entry(path: Path, *, schema_mode: str = "legacy", known_slugs: set[str] | None = None) -> tuple[list[str], list[str], bool]:
    errors: list[str] = []
    warnings: list[str] = []
    known_slugs = known_slugs or set()
    frontmatter, body = split_frontmatter(path)
    if frontmatter is None:
        return ["missing YAML frontmatter"], warnings, False
    if "__frontmatter_type_error__" in frontmatter:
        return [f"YAML frontmatter must be an object, got {frontmatter['__frontmatter_type_error__']}"], warnings, False

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
        elif known_slugs and target not in known_slugs:
            errors.append(f"Redirect target '{target}' does not exist")
        return errors, warnings, True

    for canonical_label in missing_body_markers(body, FULL_ENTRY_LABELS):
        errors.append(f"Missing required body label: '{canonical_label}'")

    if schema_mode != "legacy":
        warnings = target_schema_warnings(frontmatter, body, known_slugs)
        if schema_mode == "strict":
            errors.extend(warnings)
            warnings = []
    return errors, warnings, False


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate curated aesthetic dictionary entries")
    parser.add_argument(
        "--schema-mode",
        choices=("legacy", "warn", "strict"),
        default="legacy",
        help="Target schema enforcement: legacy default, warn-only audit, or strict failures",
    )
    parser.add_argument("root", nargs="?", default=str(DEFAULT_DICTIONARY_DIR), help="Dictionary directory or markdown file")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    root = Path(args.root)
    paths = dictionary_paths(root)
    if not paths:
        sys.exit(f"No dictionary entries found under {root}")

    failed = 0
    redirects = 0
    redirect_failures = 0
    full_entries = 0
    full_entry_failures = 0
    warning_count = 0
    known_slugs = {path.stem for path in paths}
    identity_errors = collection_errors(paths)
    for path in paths:
        errors, warnings, redirect = validate_entry(path, schema_mode=args.schema_mode, known_slugs=known_slugs)
        errors.extend(identity_errors.get(path, []))
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
        elif warnings:
            warning_count += len(warnings)
            print(f"  WARN  {path.name}")
            for warning in warnings:
                print(f"          {warning}")
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
    if warning_count:
        print(f"{warning_count} target-schema warning(s)")
    if failed:
        print(f"{failed} dictionary entries failed")
        sys.exit(1)


if __name__ == "__main__":
    main()
