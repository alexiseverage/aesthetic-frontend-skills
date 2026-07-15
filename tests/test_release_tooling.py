import os
import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def test_repository_declares_root_mit_license():
    license_path = REPO_ROOT / "LICENSE"

    assert license_path.exists()
    text = license_path.read_text(encoding="utf-8")
    assert "MIT License" in text
    assert "Permission is hereby granted, free of charge" in text


def test_doctor_script_has_valid_bash_shebang_and_is_executable():
    doctor = REPO_ROOT / "scripts" / "doctor.sh"

    assert doctor.read_text(encoding="utf-8").splitlines()[0] == "#!/usr/bin/env bash"
    assert os.access(doctor, os.X_OK)


def test_python_validator_is_executable_for_direct_invocation():
    validator = REPO_ROOT / "scripts" / "validate_profile.py"

    assert validator.read_text(encoding="utf-8").splitlines()[0] == "#!/usr/bin/env python3"
    assert os.access(validator, os.X_OK)


def test_python_validation_dependencies_are_declared():
    requirements = REPO_ROOT / "requirements.txt"

    assert requirements.exists()
    names = {
        line.split("==", 1)[0].split(">=", 1)[0].strip().lower()
        for line in requirements.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    }
    assert {"pyyaml", "jsonschema", "pytest"}.issubset(names)


def test_makefile_exposes_standard_tooling_targets():
    makefile = REPO_ROOT / "Makefile"

    assert makefile.exists()
    text = makefile.read_text(encoding="utf-8")
    assert ".PHONY:" in text
    for target in ("doctor", "validate", "test", "check"):
        assert f"{target}:" in text


def test_copilot_template_uses_skills_cli_name():
    text = (REPO_ROOT / "copilot-instructions.template.md").read_text(encoding="utf-8")

    assert "npx skills" in text
    assert "npx skill`" not in text


def test_python_test_artifacts_are_ignored():
    gitignore = (REPO_ROOT / ".gitignore").read_text(encoding="utf-8")

    assert "__pycache__/" in gitignore
    assert ".pytest_cache/" in gitignore


def test_public_markdown_uses_portable_examples():
    user_facing_roots = [
        REPO_ROOT / ".hermes" / "plans",
        REPO_ROOT / "knowledge",
        REPO_ROOT / "skills",
        REPO_ROOT / "README.md",
        REPO_ROOT / "copilot-instructions.template.md",
    ]
    blocked_patterns = [
        re.compile("/" + r"home/[A-Za-z0-9._-]+"),
        re.compile("/" + r"Users/[A-Za-z0-9._-]+"),
        re.compile(r"~/Desktop\b"),
        re.compile(r"\b" + "another" + r"letter\b", re.IGNORECASE),
        re.compile(r"\btailscale\b|\btailnet\b|\.ts\.net\b", re.IGNORECASE),
        re.compile(r"workspace/" + "aesthetic", re.IGNORECASE),
    ]

    paths = []
    for root in user_facing_roots:
        if root.is_file():
            paths.append(root)
        elif root.exists():
            paths.extend(root.rglob("*.md"))
            paths.extend(root.rglob("*.json"))

    failures = []
    for path in sorted(paths):
        text = path.read_text(encoding="utf-8")
        for line_number, line in enumerate(text.splitlines(), 1):
            if any(pattern.search(line) for pattern in blocked_patterns):
                failures.append(f"{path.relative_to(REPO_ROOT)}:{line_number}: {line}")

    assert not failures
