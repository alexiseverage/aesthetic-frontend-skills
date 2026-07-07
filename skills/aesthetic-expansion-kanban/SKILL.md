---
name: aesthetic-expansion-kanban
license: MIT
description: >
  Use this skill whenever adding one or more aesthetics to this repository and its showcase site,
  especially when the request mentions new aesthetics, niche visual styles, research collection,
  implementation briefs, website showcase components, visual QA, deployment readiness, or Kanban.
  It gives the exact Kanban-first expansion pipeline: research collection, synthesis, skills repo
  implementation, website showcase implementation, visual QA, reusable workflow capture, and final
  integration review. Prefer this skill over ad-hoc implementation so future aesthetic additions are
  source-grounded, reviewed, and truthful about live deployment state.
compatibility: Requires Hermes Kanban tools and project worktree access for code-producing tasks.
metadata:
  version: "1.0.0"
  layer: workflow
  status: stable
  tags: "kanban, workflow, aesthetic-expansion, research-pipeline, visual-qa, showcase"
  activation_keywords: "add aesthetics, new aesthetic entries, aesthetic expansion, update showcase, visual QA, Kanban aesthetic workflow, research corpus, implementation brief"
  depends_on: "aesthetic-literacy, aesthetic-research"
  known_limits: "Coordinates work; does not replace specialist skills for aesthetic analysis, frontend implementation, browser QA, or deployment operations."
  last_evaluated: ""
  eval_suite: "tests/test_aesthetic_expansion_kanban_skill.py"
---

# Aesthetic Expansion Kanban

## Summary

Use this skill to turn a request for new or updated aesthetics into a durable Hermes Kanban pipeline. The canonical flow is:

research collection -> synthesis -> skills repo implementation -> website showcase implementation -> visual QA -> final integration review

The purpose is to prevent shortcut additions that are visually under-researched, implemented only in one repository, untested in the showcase, or reported as live before deployment/domain truth has been verified.

## When to Use This Skill

Apply this skill when the user asks to:

- add one or more aesthetics to `aesthetic-frontend-skills`;
- research a niche, topical, vernacular, commercial, historical, or emerging visual style before adding it;
- create corresponding showcase pages/components for new aesthetics;
- coordinate research, implementation, QA, and review through Hermes Kanban;
- make a reusable workflow for future aesthetic additions.

Do not use this skill for a one-off explanation of an existing aesthetic; use `aesthetic-literacy` instead. Do not use it for applying an already-confirmed aesthetic to a product UI; use `aesthetic-application` and normal software-development workflow skills.

## Configurable Variables

Resolve these variables at the start of every run. Do not hardcode the lotto/casino project names into future tasks.

| Variable | Meaning | Example |
|---|---|---|
| `<topic>` | Human-readable expansion theme or family | `gambling`, `festival signage`, `regional food packaging` |
| `<slug-list>` | Comma-separated aesthetic slugs to add | `lotto, casino` |
| `<slug>` | One specific aesthetic slug | `lotto` |
| `<skills_repo>` | Canonical skills repository checkout | `<workspace>/aesthetic-frontend-skills` |
| `<showcase_repo>` | Canonical showcase website checkout | `<workspace>/aesthetic-frontend-skills-www` |
| `<research_root>` | Project-local research folder | `<skills_repo>/.hermes/research/<topic>-aesthetics/` |
| `<board>` | Hermes Kanban board slug or active board | `aesthetic-frontend-skills` |
| `<source_policy>` | Source access boundary | public-only, authenticated-user-authorized, internal archive |

If the user supplied an existing plan path, read it first and treat it as the scope record. If no plan exists, create one under `<skills_repo>/.hermes/plans/` before dispatching implementation tasks.

## Prerequisites and Grounding

1. Read the user's scope, any project plan, and all parent handoffs.
2. Inspect recent completed tasks for repository conventions, branch naming, authorship constraints, and verification commands.
3. Confirm canonical repository paths. For this project, prefer `<showcase_repo>` over similarly named non-canonical website checkouts unless the user explicitly says otherwise.
4. Discover valid Kanban assignees before creating cards. A misspelled assignee leaves work stranded.
5. Use the active Kanban board through `kanban_create`, `kanban_link`, `kanban_comment`, `kanban_block`, and `kanban_complete`; do not shell out to `hermes kanban`.

## Source Collection Strategy

Use a Pinterest-public-first approach, then broaden with source-diverse evidence. Public Pinterest is a discovery front door, not the only evidence base.

### Pinterest-public-first

- Start with public Pinterest search/pages/boards when available.
- Save pin or page URLs, image URLs when visible, captions/alt text, and outbound source links.
- Do not require private account access. If public Pinterest blocks meaningful collection, record the limitation and continue with supplemental sources unless the user explicitly authorizes authenticated access.
- Build query clusters per slug: `<slug> design`, `<slug> graphic design`, `<slug> poster`, `<slug> UI`, `<slug> ephemera`, plus domain-specific phrases.

### Supplemental sources

Use supplemental sources to avoid algorithm-only conclusions:

- official source galleries, archives, museums, vendors, standards bodies, or product pages relevant to the aesthetic;
- patent/manufacturing references when the aesthetic depends on material constraints, printing, packaging, security patterns, or fabrication;
- ephemera archives such as signs, matchbooks, tickets, receipts, packaging, menus, posters, catalogs, chips, playing cards, table felt, and other object-system evidence;
- stock/vector/image repositories only as secondary pattern evidence, not as cultural truth;
- books/articles/explainers for origin context and connotation, when available.

For gambling-related work, this specifically meant official lottery scratcher galleries, patent/manufacturing references for latex/silver scratch material and reveal windows, and casino ephemera including Las Vegas signage, chips, cards, table felt, matchbooks, and poster systems. For other topics, translate that pattern into the relevant official/material/ephemera sources.

### Evidence targets

- Target at least 20 references per primary `<slug>` when the aesthetic is new or under-documented.
- Add 8-12 contrast references when adjacent aesthetics are easy to conflate.
- Analyze every corpus through the 7-dimension framework: palette, type, texture, shape, motion, spatial conventions, cultural markers.
- Store raw corpus notes under `<research_root>/<slug>-corpus.md` and final implementation briefs under `<research_root>/implementation-brief.md`.

## Exact Kanban Decomposition Pattern

Create cards in this dependency order. Titles may include concrete slugs, but keep the structure intact.

### 1. Research fan-out

Create one card per primary slug:

- Title: `research: <slug> visual evidence corpus`
- Assignee: `researcher`
- Workspace: scratch is acceptable unless repository files must be written.
- Output: `<research_root>/<slug>-corpus.md` plus a reference/image manifest.
- Body must include: Pinterest-public-first queries, supplemental source categories, target reference count, 7-dimension annotation requirement, source access policy, and expected artifact paths.

For boundary/taxonomy questions, create a separate card:

- Title: `research: <topic> taxonomy + boundaries`
- Assignee: `researcher`
- Output: `<research_root>/taxonomy-boundaries.md`.
- Body must distinguish the requested slugs from parent categories and likely future siblings.

### 2. Synthesis fan-in

- Title: `synthesize <topic> aesthetics implementation brief`
- Assignee: `researcher`
- Parents: `parents=[research task ids]`
- Output: `<research_root>/implementation-brief.md`.
- Body must require final slugs, labels, dimension tables, include/avoid markers, accessibility risks, connotation notes, contrast guidance, file-path acceptance criteria, and test/check expectations for implementers.

### 3. Skills repository implementation

- Title: `implement <slug-list> aesthetic literacy entries`
- Assignee: `engineer`
- Parents: `parents=[synthesis task id]`
- Workspace: worktree under `<skills_repo>`; code-producing tasks require a worktree.
- Required outputs normally include:
  - `skills/aesthetic-literacy/aesthetics/<slug>.md`
  - `knowledge/aesthetics/<slug>.md`
  - index/count updates in `skills/aesthetic-literacy/SKILL.md`
  - tests or validation updates when the repository has coverage for selected entries.
- Body must require inspection of neighboring entries before writing and use of existing repository verification commands.

### 4. Website showcase implementation

- Title: `implement website showcase components for <slug-list>`
- Assignee: `engineer`
- Parents: `parents=[skills repo implementation task id]`
- Workspace: worktree under `<showcase_repo>`; code-producing tasks require a worktree.
- Required outputs depend on website conventions, commonly showcase components, registry/catalog updates, screenshots, and route visibility.
- Body must require inspecting recent showcase components before coding, using accessible interaction patterns, providing reduced-motion/fallback behavior where relevant, and avoiding misleading real-world functionality. For gambling-adjacent demos, visible copy must state the demo is fictional, non-real, and non-monetary.
- Verification: run the website's current equivalents of typecheck/lint/test/build, such as `pnpm check`, `pnpm test`, and `pnpm build`.

### 5. Visual QA gate

- Title: `visual QA <topic> showcases`
- Assignee: a real browser/QA-capable profile discovered from the environment.
- Parents: `parents=[website implementation task id]`
- Output: screenshots and QA notes for catalog cards, detail pages/modals, important interactive states, console/page errors, and responsive or reduced-motion checks.
- Body must specify viewport dimensions, screenshot destinations, route expectations, and any critical interaction to verify.

### 6. Reusable workflow capture

- Title: `create reusable Kanban skill for <topic> aesthetic expansion pipeline`
- Assignee: `engineer`
- Parents: `parents=[visual QA task id]`
- Output: a reusable skill or procedure update that generalizes the workflow and records lessons learned.
- Use this card when a new expansion revealed reusable process knowledge. If this skill already covers the lesson, patch this skill rather than creating a duplicate.

### 7. Final integration review and deployment readiness

- Title: `final integration review and deployment readiness`
- Assignee: orchestrator/default reviewer chosen by the user or board convention.
- Parents: `parents=[visual QA task id, reusable workflow task id]`
- Output: final review notes, merge/deployment readiness decision, and any follow-up cards.
- This task is a review gate, not a rubber stamp. It must inspect diffs, handoffs, screenshots, test output, authorship/branch constraints, and deployment truth.

## Worker Body Template

Use this template when creating implementation or QA cards:

```markdown
Read the project plan first: <plan_path>
Read all parent handoffs.

Goal: <one-sentence outcome>

Canonical paths:
- Skills repo: <skills_repo>
- Showcase repo: <showcase_repo>
- Research root: <research_root>

Required inputs:
- <research_root>/implementation-brief.md
- Relevant corpus and boundary files

Required outputs:
- <file paths or screenshot paths>

Constraints:
- Use a git worktree for code-producing tasks.
- Inspect neighboring files/components before editing.
- Keep repository variables configurable; do not hardcode this topic into reusable workflow docs.
- Do not claim deployment/live-site success unless source state, deployment state, and custom-domain state have all been verified.

Verification gates:
- Run the repository's documented tests/checks/builds.
- Report exact commands and real outputs.
- Block with review-required after code changes unless the board explicitly allows self-completion.
```

## Verification Gates

Every pipeline should include these verification gates:

1. Research completeness: reference counts, source diversity, public/access limitations, and contrast evidence are explicit.
2. Synthesis completeness: final slugs, dimension tables, include/avoid lists, connotation, accessibility risks, and acceptance criteria are present.
3. Skills repo correctness: dictionary entries and knowledge profiles follow existing schema/conventions; counts/indexes are updated; repository validation passes.
4. Website correctness: showcase routes/components are visible, interactions are accessible, reduced-motion/fallback behavior is handled, and fictional/sensitive domains are clearly framed.
5. Visual QA: screenshots exist for catalog and detail/interactive states; console/page errors are checked; QA notes say what was actually inspected.
6. Final review: source diffs, PRs, checks, screenshots, and handoffs are inspected before readiness is reported.

## Live-Deploy Truthfulness Warning

The live-deploy truthfulness warning matters because source, deployment, and custom-domain state can diverge. Do not say an aesthetic is live just because code was merged, a preview deployment passed, or an old deployment was promoted. A final reviewer must distinguish:

- source state: the commit/branch containing the intended changes;
- deployment state: the deployment that was built from that source and whether it is Ready/Production;
- custom-domain state: what the public domain actually serves.

If the live site appears to show the wrong app shell, stale content, or a missing route, stop promoting historical deployments. Re-ground on the intended source checkout, verify locally, make a fresh deployment from that checkout, and then verify public route/content markers.

## Installation and Profile Safety

This is a project-owned workflow skill and should live in `<skills_repo>/skills/aesthetic-expansion-kanban/` so it travels with the repository.

Do not install into `~/.hermes/skills` from a Kanban worker by default. Global profile installation affects the active user's Hermes environment and may be the wrong profile. Instead:

1. Report the project-owned skill path in the handoff.
2. Propose global installation only if the user wants this workflow available outside the repository.
3. If explicitly authorized, install or update the active profile's skill through the supported Hermes skill tools for that profile, not by copying into another profile's directory.

## Completion Handoff

When this pipeline creates or updates code or skills, include:

- skill path(s) or artifact paths;
- changed files;
- exact tests/checks/builds run and their results;
- PR URL if a PR was opened;
- known limitations or follow-up cards;
- whether global installation was skipped, proposed, or explicitly performed.
