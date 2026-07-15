import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def run_validator(script_name: str, *args: str, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / script_name), *args],
        cwd=cwd or REPO_ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


def write_skill(root: Path, name: str, frontmatter: str, body: str = "Use this skill for tests.\n") -> Path:
    skill_dir = root / "skills" / name
    skill_dir.mkdir(parents=True)
    path = skill_dir / "SKILL.md"
    path.write_text(f"---\n{frontmatter}---\n\n{body}", encoding="utf-8")
    return path


def write_dictionary_entry(root: Path, filename: str, frontmatter: str, body: str) -> Path:
    dictionary_dir = root / "skills" / "aesthetic-literacy" / "aesthetics"
    dictionary_dir.mkdir(parents=True, exist_ok=True)
    path = dictionary_dir / filename
    path.write_text(f"---\n{frontmatter}---\n\n{body}", encoding="utf-8")
    return path


VALID_DICTIONARY_BODY = """**Palette**: red, blue

**Type**: geometric sans

**Texture**: smooth

**Shape**: circles

**Motion**: subtle fades

**Spatial**: layered

**Cultural markers**: test markers

**Non-negotiables**: required features

**Connotation**: optimistic
"""


def write_profile(root: Path, filename: str, frontmatter: str, body: str = "# Test profile\n") -> Path:
    profiles_dir = root / "knowledge" / "aesthetics"
    profiles_dir.mkdir(parents=True, exist_ok=True)
    path = profiles_dir / filename
    path.write_text(f"---\n{frontmatter}---\n\n{body}", encoding="utf-8")
    return path


def test_validate_skills_accepts_valid_skill_fixture(tmp_path: Path):
    write_skill(
        tmp_path,
        "valid-skill",
        "name: valid-skill\ndescription: Valid test skill.\nmetadata:\n  hermes:\n    tags: [test]\n    related_skills: []\n",
    )

    result = run_validator("validate_skills.py", str(tmp_path / "skills"))

    assert result.returncode == 0, result.stdout + result.stderr
    assert "1/1 skills valid" in result.stdout


def test_validate_skills_rejects_missing_frontmatter(tmp_path: Path):
    skill_dir = tmp_path / "skills" / "missing-frontmatter"
    skill_dir.mkdir(parents=True)
    (skill_dir / "SKILL.md").write_text("name: missing-frontmatter\n", encoding="utf-8")

    result = run_validator("validate_skills.py", str(tmp_path / "skills"))

    assert result.returncode == 1
    assert "missing YAML frontmatter" in result.stdout


def test_validate_skills_rejects_directory_name_mismatch(tmp_path: Path):
    write_skill(tmp_path, "directory-name", "name: other-name\ndescription: Valid test skill.\n")

    result = run_validator("validate_skills.py", str(tmp_path / "skills"))

    assert result.returncode == 1
    assert "does not match parent directory" in result.stdout


def test_validate_skills_rejects_long_description(tmp_path: Path):
    write_skill(tmp_path, "long-description", f"name: long-description\ndescription: {'x' * 1025}\n")

    result = run_validator("validate_skills.py", str(tmp_path / "skills"))

    assert result.returncode == 1
    assert "description is longer than 1024 characters" in result.stdout


def test_validate_skills_rejects_empty_body(tmp_path: Path):
    write_skill(tmp_path, "empty-body", "name: empty-body\ndescription: Valid test skill.\n", body="")

    result = run_validator("validate_skills.py", str(tmp_path / "skills"))

    assert result.returncode == 1
    assert "body is empty" in result.stdout


def test_validate_skills_rejects_invalid_metadata_shape(tmp_path: Path):
    write_skill(
        tmp_path,
        "bad-metadata",
        "name: bad-metadata\ndescription: Valid test skill.\nmetadata:\n  hermes:\n    tags: test\n",
    )

    result = run_validator("validate_skills.py", str(tmp_path / "skills"))

    assert result.returncode == 1
    assert "metadata.hermes.tags must be an array of strings" in result.stdout


def test_validate_dictionary_accepts_full_entry_and_counts_redirects(tmp_path: Path):
    write_dictionary_entry(
        tmp_path,
        "good-entry.md",
        "slug: good-entry\nlabel: Good Entry\nfamily: test-family\naliases: []\n",
        VALID_DICTIONARY_BODY,
    )
    write_dictionary_entry(
        tmp_path,
        "redirect-entry.md",
        "slug: redirect-entry\nlabel: Redirect Entry\nfamily: test-family\nredirect: good-entry\nsuperseded_by: good-entry\n",
        "> Superseded by good-entry.\n",
    )

    result = run_validator("validate_dictionary.py", str(tmp_path / "skills" / "aesthetic-literacy" / "aesthetics"))

    assert result.returncode == 0, result.stdout + result.stderr
    assert "1 full entries valid" in result.stdout
    assert "1 redirects valid" in result.stdout


def test_validate_dictionary_counts_failed_redirects_separately(tmp_path: Path):
    write_dictionary_entry(
        tmp_path,
        "good-entry.md",
        "slug: good-entry\nlabel: Good Entry\nfamily: test-family\n",
        VALID_DICTIONARY_BODY,
    )
    write_dictionary_entry(
        tmp_path,
        "bad-redirect.md",
        "slug: bad-redirect\nlabel: Bad Redirect\nfamily: test-family\nredirect: ''\n",
        "> Missing redirect target.\n",
    )

    result = run_validator("validate_dictionary.py", str(tmp_path / "skills" / "aesthetic-literacy" / "aesthetics"))

    assert result.returncode == 1
    assert "1 full entries valid" in result.stdout
    assert "0 redirects valid" in result.stdout
    assert "1 redirects failed" in result.stdout


def test_validate_dictionary_rejects_slug_filename_mismatch(tmp_path: Path):
    write_dictionary_entry(
        tmp_path,
        "filename-slug.md",
        "slug: different-slug\nlabel: Filename Slug\nfamily: test-family\n",
        VALID_DICTIONARY_BODY,
    )

    result = run_validator("validate_dictionary.py", str(tmp_path / "skills" / "aesthetic-literacy" / "aesthetics"))

    assert result.returncode == 1
    assert "does not match filename" in result.stdout


def test_validate_dictionary_rejects_missing_required_frontmatter(tmp_path: Path):
    write_dictionary_entry(tmp_path, "missing-family.md", "slug: missing-family\nlabel: Missing Family\n", VALID_DICTIONARY_BODY)

    result = run_validator("validate_dictionary.py", str(tmp_path / "skills" / "aesthetic-literacy" / "aesthetics"))

    assert result.returncode == 1
    assert "Missing required field: 'family'" in result.stdout


def test_validate_dictionary_rejects_missing_dimension_labels(tmp_path: Path):
    body = VALID_DICTIONARY_BODY.replace("**Motion**: subtle fades\n\n", "")
    write_dictionary_entry(tmp_path, "missing-motion.md", "slug: missing-motion\nlabel: Missing Motion\nfamily: test-family\n", body)

    result = run_validator("validate_dictionary.py", str(tmp_path / "skills" / "aesthetic-literacy" / "aesthetics"))

    assert result.returncode == 1
    assert "Missing required body label: '**Motion**:'" in result.stdout


def test_validate_dictionary_rejects_missing_non_negotiables_and_connotation(tmp_path: Path):
    body = VALID_DICTIONARY_BODY.replace("**Non-negotiables**: required features\n\n", "").replace("**Connotation**: optimistic\n", "")
    write_dictionary_entry(tmp_path, "missing-contract.md", "slug: missing-contract\nlabel: Missing Contract\nfamily: test-family\n", body)

    result = run_validator("validate_dictionary.py", str(tmp_path / "skills" / "aesthetic-literacy" / "aesthetics"))

    assert result.returncode == 1
    assert "Missing required body label: '**Non-negotiables**:'" in result.stdout
    assert "Missing required body label: '**Connotation**:'" in result.stdout


def test_validate_dictionary_warning_mode_reports_target_schema_gaps_without_failing(tmp_path: Path):
    write_dictionary_entry(
        tmp_path,
        "legacy-entry.md",
        "slug: legacy-entry\nlabel: Legacy Entry\nfamily: test-family\naliases: []\n",
        VALID_DICTIONARY_BODY,
    )

    result = run_validator(
        "validate_dictionary.py",
        "--schema-mode",
        "warn",
        str(tmp_path / "skills" / "aesthetic-literacy" / "aesthetics"),
    )

    assert result.returncode == 0, result.stdout + result.stderr
    assert "WARN  legacy-entry.md" in result.stdout
    assert "Missing target frontmatter field: 'era'" in result.stdout
    assert "Missing target body section: '## Scope'" in result.stdout
    assert "target-schema warning" in result.stdout


def test_validate_dictionary_strict_mode_fails_target_schema_gaps(tmp_path: Path):
    write_dictionary_entry(
        tmp_path,
        "legacy-entry.md",
        "slug: legacy-entry\nlabel: Legacy Entry\nfamily: test-family\naliases: []\n",
        VALID_DICTIONARY_BODY,
    )

    result = run_validator(
        "validate_dictionary.py",
        "--schema-mode",
        "strict",
        str(tmp_path / "skills" / "aesthetic-literacy" / "aesthetics"),
    )

    assert result.returncode == 1
    assert "Missing target frontmatter field: 'status'" in result.stdout
    assert "Missing target body section: '## Frontend / UI Guidance'" in result.stdout


def test_validate_dictionary_rejects_redirect_target_that_does_not_exist(tmp_path: Path):
    write_dictionary_entry(
        tmp_path,
        "bad-redirect.md",
        "slug: bad-redirect\nlabel: Bad Redirect\nfamily: test-family\nredirect: missing-entry\nsuperseded_by: missing-entry\n",
        "> Superseded by missing-entry.\n",
    )

    result = run_validator("validate_dictionary.py", str(tmp_path / "skills" / "aesthetic-literacy" / "aesthetics"))

    assert result.returncode == 1
    assert "Redirect target 'missing-entry' does not exist" in result.stdout


def test_validate_profile_accepts_valid_profile_with_aliases(tmp_path: Path):
    path = write_profile(
        tmp_path,
        "valid-profile.md",
        "slug: valid-profile\nlabel: Valid Profile\nfirst_researched: '2026-06-01'\nlast_updated: '2026-06-02'\nsource: mixed\nimage_count: 10\nevidence_level: standard\nnew_aesthetic: true\naliases: [\"valid alias\"]\n",
    )

    result = run_validator("validate_profile.py", str(path))

    assert result.returncode == 0, result.stdout + result.stderr


def test_validate_profile_rejects_missing_frontmatter_by_default(tmp_path: Path):
    profiles_dir = tmp_path / "knowledge" / "aesthetics"
    profiles_dir.mkdir(parents=True)
    path = profiles_dir / "plain.md"
    path.write_text("# Plain markdown\n", encoding="utf-8")

    result = run_validator("validate_profile.py", str(path))

    assert result.returncode == 1
    assert "no YAML frontmatter found" in result.stdout


def test_validate_profile_can_allow_missing_frontmatter_explicitly(tmp_path: Path):
    profiles_dir = tmp_path / "knowledge" / "aesthetics"
    profiles_dir.mkdir(parents=True)
    path = profiles_dir / "plain.md"
    path.write_text("# Plain markdown\n", encoding="utf-8")

    result = run_validator("validate_profile.py", "--allow-missing-frontmatter", str(path))

    assert result.returncode == 0, result.stdout + result.stderr
    assert "SKIP" in result.stdout


def test_validate_profile_rejects_aliases_that_are_not_array_of_strings(tmp_path: Path):
    path = write_profile(
        tmp_path,
        "bad-aliases.md",
        "slug: bad-aliases\nlabel: Bad Aliases\nfirst_researched: '2026-06-01'\nlast_updated: '2026-06-02'\nsource: mixed\nimage_count: 10\nevidence_level: standard\nnew_aesthetic: true\naliases: bad alias\n",
    )

    result = run_validator("validate_profile.py", str(path))

    assert result.returncode == 1
    assert "aliases" in result.stdout


def test_validate_profile_rejects_evidence_level_image_count_mismatch(tmp_path: Path):
    path = write_profile(
        tmp_path,
        "bad-evidence.md",
        "slug: bad-evidence\nlabel: Bad Evidence\nfirst_researched: '2026-06-01'\nlast_updated: '2026-06-02'\nsource: mixed\nimage_count: 9\nevidence_level: standard\nnew_aesthetic: true\n",
    )

    result = run_validator("validate_profile.py", str(path))

    assert result.returncode == 1
    assert "standard evidence requires image_count >= 10" in result.stdout


def test_validate_profile_rejects_last_updated_before_first_researched(tmp_path: Path):
    path = write_profile(
        tmp_path,
        "bad-dates.md",
        "slug: bad-dates\nlabel: Bad Dates\nfirst_researched: '2026-06-03'\nlast_updated: '2026-06-02'\nsource: mixed\nimage_count: 5\nevidence_level: limited\nnew_aesthetic: true\n",
    )

    result = run_validator("validate_profile.py", str(path))

    assert result.returncode == 1
    assert "last_updated must be on or after first_researched" in result.stdout


def test_validate_profile_warning_mode_reports_target_sections_without_failing(tmp_path: Path):
    path = write_profile(
        tmp_path,
        "legacy-profile.md",
        "slug: legacy-profile\nlabel: Legacy Profile\nfirst_researched: '2026-06-01'\nlast_updated: '2026-06-02'\nsource: mixed\nimage_count: 10\nevidence_level: standard\nnew_aesthetic: true\naliases: []\n",
    )

    result = run_validator("validate_profile.py", "--schema-mode", "warn", str(path))

    assert result.returncode == 0, result.stdout + result.stderr
    assert "WARN  legacy-profile.md" in result.stdout
    assert "Missing target body section: '## Dimension Synthesis'" in result.stdout
    assert "target-schema warning" in result.stdout


def test_validate_profile_strict_mode_fails_missing_target_sections(tmp_path: Path):
    path = write_profile(
        tmp_path,
        "legacy-profile.md",
        "slug: legacy-profile\nlabel: Legacy Profile\nfirst_researched: '2026-06-01'\nlast_updated: '2026-06-02'\nsource: mixed\nimage_count: 10\nevidence_level: standard\nnew_aesthetic: true\naliases: []\n",
    )

    result = run_validator("validate_profile.py", "--schema-mode", "strict", str(path))

    assert result.returncode == 1
    assert "Missing target body section: '## Research Updates'" in result.stdout


def test_aesthetic_schema_audit_reports_dictionary_profile_mismatches(tmp_path: Path):
    write_dictionary_entry(
        tmp_path,
        "shared-entry.md",
        "slug: shared-entry\nlabel: Dictionary Label\nfamily: test-family\nera: contemporary\naliases: [\"dictionary alias\"]\nstatus: canonical\nevidence_level: legacy\nrelated: []\nsubsets: []\n",
        """## Scope

## 7-Dimension Profile

**Palette**: red

**Type**: sans

**Texture**: smooth

**Shape**: circles

**Motion**: fades

**Spatial**: layered

**Cultural markers**: test

## Non-Negotiables

**Non-negotiables**: required features

## Connotation

## Related / Subsets

## Frontend / UI Guidance

## CSS Translation

## Typography / Fonts

## Cultural / Ethical Notes

## Anti-Patterns
""",
    )
    write_dictionary_entry(
        tmp_path,
        "dictionary-only.md",
        "slug: dictionary-only\nlabel: Dictionary Only\nfamily: test-family\n",
        VALID_DICTIONARY_BODY,
    )
    write_profile(
        tmp_path,
        "shared-entry.md",
        "slug: shared-entry\nlabel: Profile Label\nfirst_researched: '2026-06-01'\nlast_updated: '2026-06-02'\nsource: mixed\nimage_count: 10\nevidence_level: standard\nnew_aesthetic: false\naliases: [\"profile alias\"]\n",
        """## Dimension Synthesis

## Image Descriptions

## Analysis

## Connections

## Research Updates
""",
    )
    write_profile(
        tmp_path,
        "profile-only.md",
        "slug: profile-only\nlabel: Profile Only\nfirst_researched: '2026-06-01'\nlast_updated: '2026-06-02'\nsource: mixed\nimage_count: 10\nevidence_level: standard\nnew_aesthetic: true\naliases: []\n",
    )

    result = run_validator("audit_aesthetic_schema.py", "--root", str(tmp_path))

    assert result.returncode == 0, result.stdout + result.stderr
    assert "dictionary/profile mismatch for shared-entry: label" in result.stdout
    assert "dictionary/profile mismatch for shared-entry: evidence_level" in result.stdout
    assert "dictionary entry has no research profile: dictionary-only" in result.stdout
    assert "research profile has no dictionary entry: profile-only" in result.stdout


def test_validate_links_accepts_existing_relative_markdown_and_image_paths(tmp_path: Path):
    docs = tmp_path / "docs"
    images = tmp_path / "screenshots"
    docs.mkdir()
    images.mkdir()
    (docs / "target.md").write_text("# Target\n", encoding="utf-8")
    (images / "shot.png").write_text("not really an image", encoding="utf-8")
    (docs / "source.md").write_text("[Target](target.md)\n![Shot](../screenshots/shot.png)\n", encoding="utf-8")

    result = run_validator("validate_links.py", str(tmp_path))

    assert result.returncode == 0, result.stdout + result.stderr
    assert "markdown files checked" in result.stdout


def test_validate_links_rejects_broken_relative_paths(tmp_path: Path):
    docs = tmp_path / "docs"
    docs.mkdir()
    (docs / "source.md").write_text("[Missing](missing.md)\n![Missing Shot](../screenshots/missing.png)\n", encoding="utf-8")

    result = run_validator("validate_links.py", str(tmp_path))

    assert result.returncode == 1
    assert "broken relative link" in result.stdout
    assert "missing.png" in result.stdout


def test_validate_links_rejects_absolute_filesystem_paths(tmp_path: Path):
    docs = tmp_path / "docs"
    docs.mkdir()
    (docs / "source.md").write_text("[Host File](/etc/passwd)\n", encoding="utf-8")

    result = run_validator("validate_links.py", str(tmp_path))

    assert result.returncode == 1
    assert "absolute filesystem path" in result.stdout


def test_validate_links_rejects_paths_that_escape_root(tmp_path: Path):
    outside = tmp_path.parent / "outside.md"
    outside.write_text("# Outside\n", encoding="utf-8")
    docs = tmp_path / "docs"
    docs.mkdir()
    (docs / "source.md").write_text("[Outside](../../outside.md)\n", encoding="utf-8")

    result = run_validator("validate_links.py", str(tmp_path))

    assert result.returncode == 1
    assert "escapes validation root" in result.stdout
