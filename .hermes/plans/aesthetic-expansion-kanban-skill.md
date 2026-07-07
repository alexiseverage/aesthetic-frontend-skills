# Aesthetic Expansion Kanban Skill Implementation Plan

> **For Hermes:** Implement directly in this worktree with a small TDD loop because the deliverable is a documentation/skill artifact plus repository metadata.

**Goal:** Add a reusable project-owned Hermes skill that captures the Kanban-first aesthetic expansion workflow from research collection through final integration review.

**Architecture:** Create a new skill directory under `skills/` so it ships with this repository and can be installed like the other project skills. Add focused regression tests that verify the skill exists, is listed in `skills.sh.json`, and contains the workflow requirements from the Kanban task.

**Tech Stack:** Markdown skill format with YAML frontmatter, Python pytest repository checks, existing `make test` / `make check` validation.

---

### Task 1: Write regression tests for the new workflow skill

**Objective:** Capture the required skill existence, metadata, Kanban graph, source strategy, configurable variables, and verification warnings before implementation.

**Files:**
- Create: `tests/test_aesthetic_expansion_kanban_skill.py`

**Steps:**
1. Assert `skills/aesthetic-expansion-kanban/SKILL.md` exists and has YAML frontmatter with `name: aesthetic-expansion-kanban`.
2. Assert `skills.sh.json` includes `aesthetic-expansion-kanban`.
3. Assert the skill text includes the exact pipeline stages, Pinterest-public-first source strategy, worktree requirement, configurable repository variables, verification gates, and live-deploy truthfulness warning.
4. Run `python3 -m pytest tests/test_aesthetic_expansion_kanban_skill.py -q` and expect failure until the skill is created.

### Task 2: Implement the skill artifact

**Objective:** Add a reusable, general skill for future aesthetic additions that decomposes work into durable Kanban tasks.

**Files:**
- Create: `skills/aesthetic-expansion-kanban/SKILL.md`
- Modify: `skills.sh.json`
- Modify: `README.md`

**Steps:**
1. Write frontmatter with trigger-focused description and stable metadata.
2. Include sections for prerequisites, configurable variables, exact Kanban decomposition, source collection strategy, worker/task specs, verification gates, and final integration review.
3. Keep concrete examples generic with placeholders like `<topic>`, `<slug>`, `<skills_repo>`, and `<showcase_repo>` rather than hardcoding lotto/casino only.
4. Document that global profile installation should be proposed rather than performed by workers unless explicitly authorized for the active profile.

### Task 3: Verify and hand off for review

**Objective:** Prove the artifact is valid within the repository tooling and surface review metadata.

**Files:**
- Inspect all changed files with `git diff`.

**Steps:**
1. Run `make test`.
2. Run `make check`.
3. Inspect `git status --short` and changed file paths.
4. Leave a Kanban comment with changed files and command results, then block as `review-required` for human review.
