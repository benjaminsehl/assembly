# Codex Agent Skills

A personal product-building operating system for Codex, spanning project setup, product discovery, prototypes, business viability, design, engineering, QA, release, and learning.

This project is a Codex-native plugin adaptation of lifecycle-command patterns from Addy Osmani's `agent-skills`, with product/company workflow inspiration from Garry Tan's GStack and composable engineering-workflow inspiration from Matt Pocock's `skills`. The goal is not to copy Claude Code slash commands directly. Codex plugins expose skills, so command-like entry points are implemented as thin orchestrator skills that route into a larger self-contained skill library.

## Current Status

Usable public plugin. The plugin contains project lifecycle, product, prototype, design, business, QA, engineering, launch, retro, and learning entry skills, plus underlying workflow skills, validation scripts, source notes, references, and install metadata.

## Project Lifecycle

Every project or major project slice should be resumable through four phases:

1. **Proposal:** define what becomes 10x better, what good looks like, outcomes, assumptions, and principles.
2. **Prototype:** create tangible proof so the direction can be felt or tested before full build.
3. **Build:** implement approved slices with tests, reviews, and tech-design updates.
4. **Release:** QA, polish, ship or hold, grade against the proposal, and capture follow-up learning.

Use `new-project` to scaffold `docs/project/` or `docs/projects/<slug>/`, `prototype` to create throwaway proof, and `project-status` when returning to a repo and asking what phase it is in.

## Lenses

- **User love:** `new-project`, `product-discovery`, `prototype`, `founder-review`, `design-plan-review`, `qa`, `retro`
- **Engineering excellence:** `project-status`, `spec`, `plan`, `build`, `test`, `review`, `code-simplify`, `health-check`, `ship`
- **Business viability:** `business-model-review`, `founder-review`, `prototype`, `retro`

## Design Shape

```text
codex-agent-skills/
|-- .codex-plugin/plugin.json
|-- docs/
|   |-- SPEC.md
|   `-- PLAN.md
|-- tasks/
|   `-- todo.md
|-- skills/
|   |-- spec/
|   |-- plan/
|   |-- build/
|   |-- test/
|   |-- review/
|   |-- code-simplify/
|   |-- ship/
|   |-- product-discovery/
|   |-- founder-review/
|   |-- business-model-review/
|   |-- design-plan-review/
|   |-- qa/
|   |-- health-check/
|   |-- retro/
|   |-- learn/
|   |-- new-project/
|   |-- prototype/
|   |-- project-status/
|   `-- ...
|-- references/
|-- agents/
|-- scripts/
`-- assets/
```

## Validation

```bash
python3 scripts/validate_plugin.py
python3 scripts/validate_skill_graph.py
```

## Source References

- Addy Osmani `agent-skills`: https://github.com/addyosmani/agent-skills
- Garry Tan `gstack`: https://github.com/garrytan/gstack
- Codex plugin manifest scaffold: `.codex-plugin/plugin.json`
- Source notes: [docs/SOURCE_NOTES.md](docs/SOURCE_NOTES.md)

## Installation

See [docs/INSTALL.md](docs/INSTALL.md).
