"""Count floors do not resolve representative-coverage or naming gaps."""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("profile_validator", Path(__file__).resolve().parents[1] / "scripts/validate_profile.py")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)

def test_large_limited_corpus_requires_specific_limitations():
    for invalid in (None, "", "   ", [], 42):
        assert validator.cross_field_errors({"image_count": 30, "evidence_level": "limited", "evidence_limitations": invalid})
    assert not validator.cross_field_errors({"image_count": 30, "evidence_level": "limited", "evidence_limitations": "All inspected objects are Finnish; wider regional coverage is unresolved."})

def test_standard_floor_and_small_limited_corpora_still_enforced():
    assert validator.cross_field_errors({"image_count": 9, "evidence_level": "standard"})
    assert not validator.cross_field_errors({"image_count": 9, "evidence_level": "limited"})
    assert not validator.cross_field_errors({"image_count": 30, "evidence_level": "standard"})
