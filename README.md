# Codex Agent Skills

A personal product-building operating system for Codex, spanning product discovery, business viability, design, engineering, QA, and launch.

This project is a Codex-native plugin adaptation of lifecycle-command patterns from Addy Osmani's `agent-skills`, with product/company workflow inspiration from Garry Tan's GStack. The goal is not to copy Claude Code slash commands directly. Codex plugins expose skills, so command-like entry points are implemented as thin orchestrator skills that route into a larger self-contained skill library.

## Current Status

Usable public plugin. The plugin contains product, design, business, QA, engineering, launch, retro, and learning entry skills, plus underlying workflow skills, validation scripts, source notes, references, and install metadata.

## Lenses

- **User love:** `product-discovery`, `founder-review`, `design-plan-review`, `qa`, `retro`
- **Engineering excellence:** `spec`, `plan`, `build`, `test`, `review`, `code-simplify`, `health-check`, `ship`
- **Business viability:** `business-model-review`, `founder-review`, `retro`

## Design Shape

```text
codex-agent-skills/
├── .codex-plugin/plugin.json
├── docs/
│   ├── SPEC.md
│   └── PLAN.md
├── tasks/
│   └── todo.md
├── skills/
│   ├── spec/
│   ├── plan/
│   ├── build/
│   ├── test/
│   ├── review/
│   ├── code-simplify/
│   ├── ship/
│   ├── product-discovery/
│   ├── founder-review/
│   ├── business-model-review/
│   ├── design-plan-review/
│   ├── qa/
│   ├── health-check/
│   ├── retro/
│   ├── learn/
│   └── ...
├── references/
├── agents/
├── scripts/
└── assets/
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
