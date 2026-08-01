.PHONY: python-version doctor validate audit generated test check

python-version:
	python3 scripts/check_python_version.py

doctor:
	./scripts/doctor.sh

validate:
	python3 scripts/validate_profile.py --schema-mode strict
	python3 scripts/validate_skills.py
	python3 scripts/validate_trigger_evals.py
	python3 scripts/validate_dictionary.py --schema-mode strict
	python3 scripts/validate_links.py

audit:
	python3 scripts/audit_aesthetic_schema.py --strict

generated:
	python3 scripts/generate_aesthetic_index.py --check

test:
	python3 -m pytest tests -q

check: python-version doctor validate audit generated test
