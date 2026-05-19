# Codex Agent Skills

Load-bearing engineering workflows for Codex, organized around seven small lifecycle entry points.

This project is a Codex-native plugin adaptation of the lifecycle-command pattern from Addy Osmani's `agent-skills` repository. The goal is not to copy Claude Code slash commands directly. Codex plugins expose skills, so the seven command-like entry points will be implemented as thin orchestrator skills that route into a larger self-contained skill library.

## Current Status

Planning scaffold only. The plugin manifest, specification, and implementation plan are in place. The actual command skills and underlying skill library should be built only after the spec is reviewed.

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
│   └── ...
├── scripts/
└── assets/
```

## Source References

- Addy Osmani `agent-skills`: https://github.com/addyosmani/agent-skills
- Codex plugin manifest scaffold: `.codex-plugin/plugin.json`

## Installation

See [docs/INSTALL.md](docs/INSTALL.md).
