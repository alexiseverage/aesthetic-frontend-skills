.PHONY: doctor validate test check audit

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

test:
	python3 -m pytest tests -q

check: doctor validate audit test
