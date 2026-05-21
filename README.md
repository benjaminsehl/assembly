# Codex Agent Skills

A personal product-building operating system for Codex: project setup, product discovery, prototypes, business viability, design, engineering, QA, release, retro, and learning.

This plugin turns command-like workflows into Codex skills. The entry skills stay small and load deeper workflow skills only when needed.

## Quick Start

Register the public marketplace:

```bash
codex plugin marketplace add benjaminsehl/codex-agent-skills
```

If it is already registered as a Git marketplace:

```bash
codex plugin marketplace upgrade codex-agent-skills
```

Then invoke skills in natural language:

```text
Use new-project to scaffold this project.
Use project-status to tell me what phase we are in and what skills to use next.
Use product-discovery on this idea.
Use prototype before we build this direction.
Use ship to decide whether this is ready.
```

## Project Docs Convention

The root project workspace is `docs/`. Subprojects live under `docs/projects/<slug>/`. Subprojects can have their own subprojects, so the structure is recursive.

```text
my-app/
|-- README.md
|-- docs/
|   |-- README.md
|   |-- status.md
|   |-- phases/
|   |   |-- proposal.md
|   |   |-- prototype.md
|   |   |-- build.md
|   |   `-- release.md
|   |-- product/
|   |   |-- vision.md
|   |   `-- principles.md
|   |-- decisions/
|   |   `-- README.md
|   |-- tech-design/
|   |   `-- README.md
|   |-- specs/
|   |   `-- README.md
|   |-- plans/
|   |   `-- README.md
|   |-- prototypes/
|   |   `-- README.md
|   |-- research/
|   |   `-- README.md
|   |-- qa/
|   |   `-- README.md
|   |-- release/
|   |   `-- README.md
|   `-- projects/
|       |-- agent-layer/
|       |   |-- status.md
|       |   |-- phases/
|       |   |-- decisions/
|       |   |-- specs/
|       |   |-- plans/
|       |   `-- projects/
|       `-- ios-client/
|           `-- ...
`-- src/
```

Why this shape:

- Agents get one obvious place to start: `docs/status.md`.
- Project reasoning is centralized instead of scattered across package folders.
- Subprojects still get their own paper trail.
- Chesterton's fence is visible: before changing something important, inspect nearby decisions, principles, plans, and phase notes.

## The Workflow

1. **Create or resume the project.**
   Use `new-project` for a new app, project, or subproject. Use `project-status` when returning after time away.

2. **Proposal phase.**
   Define what becomes 10x better, what good looks like, assumptions, principles, and risks. Use `product-discovery`, `founder-review`, and `business-model-review`.

3. **Prototype phase.**
   Build the smallest tangible artifact that answers the riskiest question. Use `prototype` and `design-plan-review`.

4. **Build phase.**
   Turn the approved direction into specs, plans, slices, tests, and reviewable implementation. Use `spec`, `plan`, `build`, `test`, `review`, and `code-simplify`.

5. **Release phase.**
   QA the product like a user, polish, make a go/no-go decision, ship or hold, then grade the result against the original proposal. Use `qa`, `health-check`, `ship`, `retro`, and `learn`.

## Skills By Phase

| Phase | Main question | Skills |
| --- | --- | --- |
| Orient | Where are we and what is next? | `project-status`, `learn` |
| Proposal | Is this worth doing, and what must be true? | `new-project`, `product-discovery`, `founder-review`, `business-model-review`, `spec` |
| Prototype | Can we feel or prove the direction? | `prototype`, `design-plan-review`, `founder-review` |
| Build | Can we implement this well? | `plan`, `build`, `test`, `review`, `code-simplify`, `health-check` |
| Release | Should this ship, and what did we learn? | `qa`, `ship`, `retro`, `learn` |

## Scaffolding

From this plugin checkout, scaffold a root project:

```bash
python3 scripts/scaffold_project.py --root /path/to/repo --name "Project Name"
```

Scaffold a subproject:

```bash
python3 scripts/scaffold_project.py \
  --root /path/to/repo \
  --parent docs \
  --name "Agent Layer" \
  --slug agent-layer
```

The script skips existing files by default. Use `--force` only when intentionally regenerating scaffold files.

## Toward An App Factory

The long-term idea is an agentic app factory that can repeatedly:

- clarify the product and business case,
- create a durable project paper trail,
- prototype the right proof,
- build in small verified slices,
- QA and ship with evidence,
- learn from the result,
- and resume cleanly months later.

This repo is the workflow kernel for that future. The current version is intentionally simple: skills, references, docs, and validators before any heavier automation.

## Validation

```bash
python3 scripts/validate_plugin.py
python3 scripts/validate_skill_graph.py
python3 -m py_compile scripts/validate_plugin.py scripts/validate_skill_graph.py scripts/scaffold_project.py
```

## Source References

- Addy Osmani `agent-skills`: https://github.com/addyosmani/agent-skills
- Garry Tan `gstack`: https://github.com/garrytan/gstack
- Matt Pocock `skills`: https://github.com/mattpocock/skills
- Benjamin Sehl `agent-kernel`: https://github.com/benjaminsehl/agent-kernel
- Install details: [docs/INSTALL.md](docs/INSTALL.md)
- Source notes: [docs/SOURCE_NOTES.md](docs/SOURCE_NOTES.md)
