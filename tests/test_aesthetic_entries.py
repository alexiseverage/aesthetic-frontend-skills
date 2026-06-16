from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
SELECTED_AESTHETICS = {
    "high-performance-hmi": "High-performance HMI",
    "risograph": "Risograph",
    "mexican-rotulismo": "Mexican Rotulismo",
    "guochao": "Guochao",
    "decora-kei": "Decora Kei",
}
DIMENSION_HEADINGS = [
    "**Palette**",
    "**Type**",
    "**Texture**",
    "**Shape**",
    "**Motion**",
    "**Spatial**",
    "**Cultural markers**",
]
REQUIRED_PROFILE_SECTIONS = [
    "## Dimension Synthesis",
    "## Analysis",
    "## Connections",
    "## Research Updates",
]


def _frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    assert text.startswith("---\n"), f"{path} is missing YAML frontmatter"
    yaml_text = text.split("---", 2)[1]
    return yaml.safe_load(yaml_text)


def test_selected_aesthetic_dictionary_entries_exist_and_are_complete():
    for slug, label in SELECTED_AESTHETICS.items():
        path = REPO_ROOT / "skills" / "aesthetic-literacy" / "aesthetics" / f"{slug}.md"
        assert path.exists(), f"missing dictionary entry for {slug}"
        text = path.read_text(encoding="utf-8")
        metadata = _frontmatter(path)

        assert metadata["slug"] == slug
        assert metadata["label"] == label
        assert metadata["family"]
        assert metadata["era"]
        assert isinstance(metadata["aliases"], list)
        assert metadata["aliases"]

        for heading in DIMENSION_HEADINGS:
            assert heading in text, f"{slug} missing {heading}"
        assert "**Non-negotiables**" in text
        assert "## Connotation" in text or "**Connotation**" in text
        assert "**Related" in text or "## Related" in text


def test_selected_aesthetic_knowledge_profiles_exist_with_evidence_links():
    for slug, label in SELECTED_AESTHETICS.items():
        path = REPO_ROOT / "knowledge" / "aesthetics" / f"{slug}.md"
        assert path.exists(), f"missing knowledge profile for {slug}"
        text = path.read_text(encoding="utf-8")
        metadata = _frontmatter(path)

        assert metadata["slug"] == slug
        assert metadata["label"] == label
        assert metadata["new_aesthetic"] is False
        assert metadata["evidence_level"] in {"standard", "limited"}
        assert metadata["image_count"] >= 0
        assert "https://" in text, f"{slug} profile must retain source links"
        for section in REQUIRED_PROFILE_SECTIONS:
            assert section in text, f"{slug} missing {section}"


def test_aesthetic_literacy_index_includes_selected_aesthetics_and_count():
    text = (REPO_ROOT / "skills" / "aesthetic-literacy" / "SKILL.md").read_text(
        encoding="utf-8"
    )

    assert "curated dictionary of 62 major aesthetics" in text
    assert "62 total entries" in text
    for slug in SELECTED_AESTHETICS:
        assert slug in text
