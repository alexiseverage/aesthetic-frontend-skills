from pathlib import Path
import sys

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from validate_dictionary import dictionary_paths, target_schema_warnings
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
    "storybook-gothic": "Storybook Gothic",
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
ENTERTAINMENT_SPECULATIVE_CANONICAL_BATCH = [
    "ai-slop-synthetic-corporate-art",
    "anime-mecha-realism",
    "apple-core-tech",
    "board-game-box-art",
    "casino",
    "cassette-futurism",
    "chibi-mecha",
    "cute-tech",
    "fairground-carnival-poster-art",
    "magical-girl",
    "mecha-kaiju",
    "nanopunk",
    "post-apocalyptic-scavenged-tech",
    "space-western",
    "steampunk",
    "trading-card-game-design",
    "uncanny-android",
]
PROFILE_BACKED_NONCANONICAL_BATCH = [
    "aesthetic-movement",
    "dreamcore-weirdcore",
    "liminal-space-backrooms",
    "nu-goth-pastel-goth",
]
CANONICAL_ENTRY_SECTIONS = [
    "## Scope",
    "## 7-Dimension Profile",
    "## Non-Negotiables",
    "## Connotation",
    "## Related / Subsets",
    "## Frontend / UI Guidance",
    "## CSS Translation",
    "## Typography / Fonts",
    "## Cultural / Ethical Notes",
    "## Anti-Patterns",
]
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


def test_entertainment_speculative_batch_uses_canonical_dictionary_schema():
    for slug in ENTERTAINMENT_SPECULATIVE_CANONICAL_BATCH:
        path = REPO_ROOT / "skills" / "aesthetic-literacy" / "aesthetics" / f"{slug}.md"
        text = path.read_text(encoding="utf-8")
        metadata = _frontmatter(path)

        assert metadata["status"] == "canonical", f"{slug} is not canonical"
        assert metadata["evidence_level"] in {"standard", "limited"}
        assert isinstance(metadata["related"], list)
        assert "subsets" in metadata
        for section in CANONICAL_ENTRY_SECTIONS:
            assert section in text, f"{slug} missing {section}"


def test_profile_backed_noncanonical_batch_has_no_target_schema_warnings():
    dictionary_root = REPO_ROOT / "skills" / "aesthetic-literacy" / "aesthetics"
    known_slugs = {path.stem for path in dictionary_paths(dictionary_root)}

    for slug in PROFILE_BACKED_NONCANONICAL_BATCH:
        path = dictionary_root / f"{slug}.md"
        text = path.read_text(encoding="utf-8")
        metadata = _frontmatter(path)

        assert metadata["status"] == "canonical", f"{slug} is not canonical"
        assert metadata["evidence_level"] in {"standard", "limited"}
        assert isinstance(metadata["related"], list)
        assert isinstance(metadata["subsets"], list)
        for section in CANONICAL_ENTRY_SECTIONS:
            assert section in text, f"{slug} missing {section}"
        assert target_schema_warnings(metadata, text, known_slugs) == []


def test_aesthetic_literacy_index_includes_selected_aesthetics_and_count():
    text = (REPO_ROOT / "skills" / "aesthetic-literacy" / "SKILL.md").read_text(
        encoding="utf-8"
    )

    assert "curated dictionary of 123 major aesthetics" in text
    assert "123 total entries" in text
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


def test_storybook_gothic_pilot_has_canonical_profile_and_append_only_log():
    dictionary_path = REPO_ROOT / "skills" / "aesthetic-literacy" / "aesthetics" / "storybook-gothic.md"
    profile_path = REPO_ROOT / "knowledge" / "aesthetics" / "storybook-gothic.md"
    log_path = REPO_ROOT / "knowledge" / "aesthetics" / "storybook-gothic" / "research-log.md"

    assert dictionary_path.exists(), "missing canonical Storybook Gothic dictionary entry"
    assert profile_path.exists(), "missing structured Storybook Gothic research profile"
    assert log_path.exists(), "missing append-only Storybook Gothic research log"

    dictionary = dictionary_path.read_text(encoding="utf-8")
    profile = profile_path.read_text(encoding="utf-8")
    research_log = log_path.read_text(encoding="utf-8")
    metadata = _frontmatter(dictionary_path)

    assert metadata["status"] == "canonical"
    assert metadata["evidence_level"] == "limited"
    assert "## Scope" in dictionary
    assert "## Frontend / UI Guidance" in dictionary
    assert "## CSS Translation" in dictionary
    assert "## Cultural / Ethical Notes" in dictionary
    assert "VistaPrint" in profile
    assert "logged_at:" in research_log
    assert "## Observation" in research_log
    assert "## Canonical Entry Impact" in research_log

    combined = f"{dictionary}\n{profile}\n{research_log}"
    forbidden_fragments = [
        "/" + "home/",
        "~" + "/.hermes",
        "aesthetic" + "-expansion" + "-kanban",
    ]
    for fragment in forbidden_fragments:
        assert fragment not in combined
