from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
SELECTED_AESTHETICS = {
    "magical-girl": "Magical Girl",
    "witchcore": "Witchcore",
    "sports-scorebug": "Sports Scorebug",
    "konbini-utility": "Konbini Utility",
    "blue-note-jazz-modernism": "Blue Note Jazz Modernism",
    "harm-reduction-zine": "Harm Reduction Zine",
    "queer-nightlife-ephemera": "Queer Nightlife Ephemera",
    "prescription-label-clarity": "Prescription Label Clarity",
    "bloomberg-terminal-monochrome": "Bloomberg Terminal Monochrome",
    "cheminformatics-map-explorer": "Cheminformatics Map Explorer",
    "convenience-store-backoffice": "Convenience-Store Back-Office Grid",
    "b2b-quick-order-grid": "B2B Quick-Order Grid",
    "lotto": "Lotto Scratcher Commerce",
    "casino": "Casino Neon Tableplay",
    "cyberpunk": "Cyberpunk",
    "cassette-futurism": "Cassette Futurism",
    "nanopunk": "Nanopunk",
    "techno-noir": "Techno-noir",
    "apple-core-tech": "Apple-core Tech",
    "uncanny-android": "Uncanny Android / Humanoid Realism",
    "dieselpunk": "Dieselpunk",
    "steampunk": "Steampunk",
    "post-apocalyptic-scavenged-tech": "Post-apocalyptic / Scavenged Tech",
    "space-western": "Space Western",
    "cute-tech": "Kawaii / Cute-Tech",
    "companion-bot": "Companion-Bot / Pet-Bot",
    "mecha-kaiju": "Mecha / Kaiju",
    "anime-mecha-realism": "Anime Mecha-Realism",
    "biomechanical": "Biomechanical / Biopunk",
    "chibi-mecha": "Chibi Mecha",
    "gorpcore": "Gorpcore",
    "balletcore": "Balletcore",
    "barbiecore": "Barbiecore",
    "coastal-grandmother": "Coastal Grandmother",
    "goblincore": "Goblincore",
    "liminal-space-backrooms": "Liminal Space / Backrooms",
    "dreamcore-weirdcore": "Dreamcore / Weirdcore",
    "chinoiserie": "Chinoiserie",
    "gothic-revival": "Gothic Revival",
    "nu-goth-pastel-goth": "Nu-Goth / Pastel Goth",
    "cybersigilism": "Cybersigilism",
    "ai-slop-synthetic-corporate-art": "AI Slop / Synthetic Corporate Art",
    "tiki-polynesian-pop": "Tiki / Polynesian Pop",
    "wabi-sabi-slow-living": "Wabi-Sabi / Slow Living",
    "hauntology": "Hauntology",
    "chicano-lowrider-art": "Chicano Lowrider Art",
    "fairground-carnival-poster-art": "Fairground / Carnival Poster Art",
    "board-game-box-art": "Board Game Box Art",
    "trading-card-game-design": "Trading Card Game Design",
    "scandi-noir": "Scandi Noir",
    "ulm-school": "Ulm School / HfG Ulm",
    "polish-poster-school": "Polish Poster School",
    "shaker-design": "Shaker Design",
    "high-tech-architecture": "High-Tech Architecture / Structural Expressionism",
    "prairie-school": "Prairie School",
    "beaux-arts": "Beaux-Arts",
    "italian-radical-design": "Italian Radical Design",
    "new-objectivity": "New Objectivity / Neue Sachlichkeit",
    "japanese-metabolism": "Japanese Metabolism",
    "aesthetic-movement": "Aesthetic Movement",
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

    assert "curated dictionary of 122 major aesthetics" in text
    assert "122 total entries" in text
    for slug in SELECTED_AESTHETICS:
        assert slug in text


def test_lotto_realistic_scratchoff_guidance_is_specific():
    dictionary_text = (
        REPO_ROOT / "skills" / "aesthetic-literacy" / "aesthetics" / "lotto.md"
    ).read_text(encoding="utf-8").lower()
    profile_text = (REPO_ROOT / "knowledge" / "aesthetics" / "lotto.md").read_text(
        encoding="utf-8"
    ).lower()
    combined = f"{dictionary_text}\n{profile_text}"

    required_phrases = [
        "drag",
        "brush path",
        "grey/silver latex",
        "debris",
        "residue",
        "price badge",
        "lottery badge",
        "validation box",
        "void marker",
        "serial",
        "security print",
        "paper grain",
        "dense play grid",
        "fictional",
        "non-redeemable",
        "casino",
    ]

    for phrase in required_phrases:
        assert phrase in combined, f"lotto guidance missing: {phrase}"


def test_wave_1_zero_image_profiles_do_not_label_text_sources_as_image_descriptions():
    wave_1_slugs = [
        "ulm-school",
        "polish-poster-school",
        "shaker-design",
        "high-tech-architecture",
        "prairie-school",
    ]
    for slug in wave_1_slugs:
        path = REPO_ROOT / "knowledge" / "aesthetics" / f"{slug}.md"
        metadata = _frontmatter(path)
        assert metadata["image_count"] == 0

        text = path.read_text(encoding="utf-8")
        section = text.split("## Image Descriptions", 1)[1].split("## ", 1)[0]
        assert "No image corpus" in section, f"{slug} should state that no image corpus was collected"
        assert "Text/source review" not in section, f"{slug} should not present text sources as image descriptions"
        assert "1. https://" not in section, f"{slug} should not list source URLs as image descriptions"


def test_wave_1_profiles_do_not_retain_known_broken_review_urls():
    broken_urls = {
        "https://www.centrepompidou.fr/en/collection/oeuvre/cXjKAy",
        "https://franklloydwright.org/architecture/prairie-style/",
    }
    combined = "\n".join(
        (REPO_ROOT / "knowledge" / "aesthetics" / f"{slug}.md").read_text(encoding="utf-8")
        for slug in [
            "ulm-school",
            "polish-poster-school",
            "shaker-design",
            "high-tech-architecture",
            "prairie-school",
        ]
    )
    for url in broken_urls:
        assert url not in combined
