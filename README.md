# Aesthetic Frontend Skills ✨

<p align="center"><strong><a href="https://aesthetic-design.art">aesthetic-design.art</a></strong> — documentation & full showcase</p>

[![skills.sh](https://skills.sh/b/alexiseverage/aesthetic-frontend-skills)](https://skills.sh/alexiseverage/aesthetic-frontend-skills)

A focused collection of AI agent skills for building aesthetically beautiful, creative web frontend UIs. Covers visual aesthetics end-to-end: from literacy and research through image analysis, asset generation, and token output.

**Scope boundary**: aesthetics only. Accessibility, performance, layout systems, and component architecture are explicitly out of scope.

## Skills Overview

| Skill | Layer | When to Use |
|---|---|---|
| [`aesthetic-literacy`](skills/aesthetic-literacy/SKILL.md) | foundation | Understand and characterize any named aesthetic across 7 formal dimensions |
| [`aesthetic-research`](skills/aesthetic-research/SKILL.md) | applied | Research unknown/niche aesthetics by collecting visual references from available image sources |
| [`image-analysis`](skills/image-analysis/SKILL.md) | applied | Extract implementable CSS values from collected reference images |
| [`asset-creation`](skills/asset-creation/SKILL.md) | applied (optional) | Generate images and SVG components using available image generation tools; convert SVGs to React components |
| [`aesthetic-application`](skills/aesthetic-application/SKILL.md) | applied | Translate a confirmed aesthetic into W3C design tokens, CSS custom properties, and component notes |
| [`aesthetic-expansion-kanban`](skills/aesthetic-expansion-kanban/SKILL.md) | workflow | Coordinate new aesthetic additions through Kanban research, synthesis, implementation, website showcase, visual QA, and final review |

---

### Examples

A small selection of generated components. Visit [aesthetic-design.art](https://aesthetic-design.art) for full documentation and a showcase of all supported aesthetics.

<table>
<tr>
  <td align="center" width="33%"><a href="screenshots/claymorphism-component.png"><img src="screenshots/claymorphism-component.png" width="220" alt="Claymorphism"/></a><br/><sub>Claymorphism</sub></td>
  <td align="center" width="33%"><a href="screenshots/dark-academia-component.png"><img src="screenshots/dark-academia-component.png" width="220" alt="Dark Academia"/></a><br/><sub>Dark Academia</sub></td>
  <td align="center" width="33%"><a href="screenshots/new-wave-typography-component.png"><img src="screenshots/new-wave-typography-component.png" width="220" alt="New Wave Typography"/></a><br/><sub>New Wave Typography</sub></td>
</tr>
<tr>
  <td align="center" width="33%"><a href="screenshots/op-art-component.png"><img src="screenshots/op-art-component.png" width="220" alt="Op Art"/></a><br/><sub>Op Art</sub></td>
  <td align="center" width="33%"><a href="screenshots/suprematism-component.png"><img src="screenshots/suprematism-component.png" width="220" alt="Suprematism"/></a><br/><sub>Suprematism</sub></td>
  <td align="center" width="33%"><a href="screenshots/vaporwave-component.png"><img src="screenshots/vaporwave-component.png" width="220" alt="Vaporwave"/></a><br/><sub>Vaporwave</sub></td>
</tr>
<tr>
  <td align="center" width="33%"><a href="screenshots/wartime-propaganda-component.png"><img src="screenshots/wartime-propaganda-component.png" width="220" alt="Wartime Propaganda"/></a><br/><sub>Wartime Propaganda</sub></td>
  <td align="center" width="33%"><a href="screenshots/web-2-gloss-component.png"><img src="screenshots/web-2-gloss-component.png" width="220" alt="Web 2.0 Gloss"/></a><br/><sub>Web 2.0 Gloss</sub></td>
  <td align="center" width="33%"><a href="screenshots/y2k-component.png"><img src="screenshots/y2k-component.png" width="220" alt="Y2K"/></a><br/><sub>Y2K</sub></td>
</tr>
</table>

## Quick Install

**Fastest — no clone needed:**

```bash
# All 6 skills, project-level (default)
npx skills add alexiseverage/aesthetic-frontend-skills

# All 6 skills, user-level (available across all your projects)
npx skills add alexiseverage/aesthetic-frontend-skills -g

# Individual skill
npx skills add alexiseverage/aesthetic-frontend-skills@aesthetic-literacy
```

For project-level installs, also scaffold the knowledge directory:

```bash
mkdir -p knowledge/aesthetics
```

For global installs (`-g`), create the global knowledge dir once:

```bash
mkdir -p ~/.agents/skills/knowledge/aesthetics
```

Then reload VS Code: **Command Palette → Developer: Reload Window**.

Or use a [git submodule](#as-a-git-submodule) if you want to pull updates.

---

## Using in Your Project

### 1. Install the skills

**Option A — User-scope install** (available across all your projects):

```bash
# Via npx skills (recommended)
npx skills add alexiseverage/aesthetic-frontend-skills -g

# Or copy manually
cp -r skills/* ~/.agents/skills/
```

Agents discover these automatically. For global installs, create the knowledge directory once:

```bash
mkdir -p ~/.agents/skills/knowledge/aesthetics
```

**Option B — Individual skill** (pick only what you need):

```bash
npx skills add alexiseverage/aesthetic-frontend-skills@aesthetic-literacy
npx skills add alexiseverage/aesthetic-frontend-skills@aesthetic-research
npx skills add alexiseverage/aesthetic-frontend-skills@image-analysis
npx skills add alexiseverage/aesthetic-frontend-skills@aesthetic-application
npx skills add alexiseverage/aesthetic-frontend-skills@asset-creation
npx skills add alexiseverage/aesthetic-frontend-skills@aesthetic-expansion-kanban
```

### 2. Register skills with your agent

Depending on your AI client or IDE, you may need to explicitly connect installed skills before your agent can use them. Consult your client's documentation for how to register or enable custom skills.

---

## Development

Install the Python validation dependencies before running local checks:

```bash
python3 -m pip install -r requirements.txt
```

The repository scripts are executable and can also be invoked with their
interpreters when a runtime strips executable bits:

```bash
make doctor      # ./scripts/doctor.sh
make validate    # python3 scripts/validate_profile.py
make test        # python3 -m pytest tests -q
make check       # doctor + validate + test

bash scripts/doctor.sh
./scripts/doctor.sh
python3 scripts/validate_profile.py
./scripts/validate_profile.py
```


