import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
RFC_PATH = REPO_ROOT / "docs" / "refactor-rfc-aesthetic-artifact-model.md"
CANONICAL_TEMPLATE_PATH = REPO_ROOT / "docs" / "templates" / "canonical-aesthetic-entry.md"
RESEARCH_LOG_TEMPLATE_PATH = REPO_ROOT / "docs" / "templates" / "research-log-entry.md"


def test_refactor_rfc_documents_three_artifact_model_and_enforcement_sequence():
    text = RFC_PATH.read_text(encoding="utf-8")

    required_phrases = [
        "canonical aesthetic entry",
        "structured research profile",
        "append-only research log",
        "audit/warning mode",
        "no-new-regressions",
        "batch migration",
        "strict default",
    ]
    for phrase in required_phrases:
        assert phrase in text


def test_schema_templates_document_required_frontmatter_and_sections():
    canonical_template = CANONICAL_TEMPLATE_PATH.read_text(encoding="utf-8")
    research_log_template = RESEARCH_LOG_TEMPLATE_PATH.read_text(encoding="utf-8")

    for phrase in [
        "slug:",
        "label:",
        "family:",
        "era:",
        "aliases:",
        "status: canonical",
        "evidence_level:",
        "related:",
        "subsets:",
        "## Scope",
        "## 7-Dimension Profile",
        "**Palette**:",
        "**Type**:",
        "**Texture**:",
        "**Shape**:",
        "**Motion**:",
        "**Spatial**:",
        "**Cultural markers**:",
        "## Non-Negotiables",
        "## Connotation",
        "## Related / Subsets",
        "## Frontend / UI Guidance",
        "## CSS Translation",
        "## Typography / Fonts",
        "## Cultural / Ethical Notes",
        "## Anti-Patterns",
    ]:
        assert phrase in canonical_template

    for phrase in [
        "logged_at:",
        "researcher:",
        "source_url:",
        "evidence_type:",
        "## Observation",
        "## Dimension Impact",
        "append-only",
    ]:
        assert phrase in research_log_template


def test_canonical_entry_template_passes_strict_dictionary_validation(tmp_path: Path):
    fixture = tmp_path / "example-aesthetic-slug.md"
    fixture.write_text(CANONICAL_TEMPLATE_PATH.read_text(encoding="utf-8"), encoding="utf-8")

    result = subprocess.run(
        [
            sys.executable,
            str(REPO_ROOT / "scripts" / "validate_dictionary.py"),
            "--schema-mode",
            "strict",
            str(fixture),
        ],
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0, result.stdout + result.stderr
