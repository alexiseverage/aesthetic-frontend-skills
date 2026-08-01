import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
VERSION_CHECK = REPO_ROOT / "scripts" / "check_python_version.py"


def run_version_check(version: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(VERSION_CHECK), "--runtime-version", version],
        text=True,
        capture_output=True,
        check=False,
    )


def test_python_version_check_accepts_minimum_supported_version():
    result = run_version_check("3.10.0")

    assert result.returncode == 0, result.stdout + result.stderr


def test_python_version_check_rejects_python_39_with_actionable_error():
    result = run_version_check("3.9.6")

    assert result.returncode == 1
    assert "Python 3.10 or newer is required" in result.stderr
    assert "found 3.9.6" in result.stderr
    assert "rerun make check" in result.stderr
