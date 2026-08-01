import json
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
AESTHETIC_LITERACY = REPO_ROOT / "skills" / "aesthetic-literacy"
AESTHETIC_APPLICATION = REPO_ROOT / "skills" / "aesthetic-application"


REQUIRED_SKILL_LOCAL_REFERENCES = [
    AESTHETIC_LITERACY / "references" / "aesthetic-index.md",
    AESTHETIC_LITERACY / "references" / "aesthetic-manifest.json",
    AESTHETIC_LITERACY / "references" / "artifact-schema.md",
    AESTHETIC_LITERACY / "references" / "canonical-entry-example.md",
    AESTHETIC_APPLICATION / "references" / "output-contract.md",
    AESTHETIC_APPLICATION / "references" / "token-template.md",
    AESTHETIC_APPLICATION / "references" / "css-translation-patterns.md",
]


def test_skill_local_references_exist_for_installed_users():
    for path in REQUIRED_SKILL_LOCAL_REFERENCES:
        assert path.exists(), f"missing installed-user reference: {path.relative_to(REPO_ROOT)}"
        text = path.read_text(encoding="utf-8")
        assert len(text.strip()) > 200, f"reference is unexpectedly thin: {path.relative_to(REPO_ROOT)}"


def test_generated_aesthetic_index_is_current():
    result = subprocess.run(
        [sys.executable, "scripts/generate_aesthetic_index.py", "--check"],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0, result.stdout + result.stderr
    assert "aesthetic-index.md is current" in result.stdout
    assert "aesthetic-manifest.json is current" in result.stdout


def test_generator_writes_public_manifest_and_detects_stale_output(tmp_path):
    index_path = tmp_path / "aesthetic-index.md"
    manifest_path = tmp_path / "aesthetic-manifest.json"
    command = [
        sys.executable,
        "scripts/generate_aesthetic_index.py",
        "--index-path",
        str(index_path),
        "--manifest-path",
        str(manifest_path),
    ]

    generated = subprocess.run(
        command,
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    assert generated.returncode == 0, generated.stdout + generated.stderr
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert manifest["schemaVersion"] == 1
    assert manifest["fullEntryCount"] == 126
    assert manifest["redirectCount"] == 1
    assert manifest["familyCount"] == 8
    assert [entry["slug"] for entry in manifest["entries"]] == sorted(
        entry["slug"] for entry in manifest["entries"]
    )
    assert all(
        {"slug", "label", "family", "status", "aliases"}.issubset(entry)
        for entry in manifest["entries"]
    )
    redirects = [entry for entry in manifest["entries"] if entry["status"] == "redirect"]
    assert redirects == [
        {
            "slug": "quiet-luxury",
            "label": "Quiet Luxury → see Warm Minimalism",
            "family": "contemporary-lifestyle",
            "status": "redirect",
            "aliases": [],
            "redirect": "warm-minimalism",
        }
    ]

    manifest_path.write_text("{}\n", encoding="utf-8")
    checked = subprocess.run(
        [*command, "--check"],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    assert checked.returncode == 1
    assert "aesthetic-manifest.json is stale" in checked.stdout

    regenerated = subprocess.run(command, cwd=REPO_ROOT, check=False)
    assert regenerated.returncode == 0
    index_path.write_text("# stale\n", encoding="utf-8")
    checked = subprocess.run(
        [*command, "--check"],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    assert checked.returncode == 1
    assert "aesthetic-index.md is stale" in checked.stdout


def test_skill_workflows_prefer_dictionary_entries_over_root_research_logs():
    literacy = (AESTHETIC_LITERACY / "SKILL.md").read_text(encoding="utf-8")
    application = (AESTHETIC_APPLICATION / "SKILL.md").read_text(encoding="utf-8")

    for text in [literacy, application]:
        assert "aesthetics/<slug>.md" in text
        assert "Do not load root research logs" in text
        assert "provenance, maintenance, or research" in text

    assert "references/aesthetic-index.md" in literacy
    assert "references/output-contract.md" in application
