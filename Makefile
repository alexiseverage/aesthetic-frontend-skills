.PHONY: doctor validate test check

doctor:
	./scripts/doctor.sh

validate:
	python3 scripts/validate_profile.py
	python3 scripts/validate_skills.py
	python3 scripts/validate_dictionary.py
	python3 scripts/validate_links.py

test:
	python3 -m pytest tests -q

check: doctor validate test
