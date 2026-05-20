# Codex Agent Skills

Load-bearing engineering workflows for Codex, organized around seven small lifecycle entry points.

This project is a Codex-native plugin adaptation of the lifecycle-command pattern from Addy Osmani's `agent-skills` repository. The goal is not to copy Claude Code slash commands directly. Codex plugins expose skills, so the seven command-like entry points are implemented as thin orchestrator skills that route into a larger self-contained skill library.

## Current Status

Usable local plugin. The plugin contains the seven entry skills, the underlying workflow skills, validation scripts, source notes, references, and install metadata.

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
- Codex plugin manifest scaffold: `.codex-plugin/plugin.json`
- Source notes: [docs/SOURCE_NOTES.md](docs/SOURCE_NOTES.md)

## Installation

See [docs/INSTALL.md](docs/INSTALL.md).
