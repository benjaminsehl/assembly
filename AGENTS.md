# Codex Agent Skills

This repo builds the reusable Codex plugin for phase-aware product development.

## Start Here

Before changing the plugin, inspect:

- `README.md` for user-facing workflow guidance
- `docs/SPEC.md` for the plugin contract
- `docs/COMMAND_CONTRACT.md` for entry-skill behavior
- `references/agent-operating-protocol.md` for phase-aware agent behavior
- `scripts/validate_plugin.py` and `scripts/validate_skill_graph.py` for validation rules

## Phase-Aware Workflow

When working on this repo, follow the same protocol the plugin teaches:

- Identify whether the change is proposal, prototype, build, or release work.
- Use the relevant skill surface before editing.
- Use `project-status` first when the phase is unclear; use `introspect` only when status shows the project needs a deeper audit, recovery plan, or status repair.
- If a user asks to skip prerequisites, warn once, name the missing gate, then proceed if they insist unless a hard safety boundary applies.
- Preserve the paper trail for decisions that future agents will need.

## Editing Rules

- Keep entry skills thin.
- Put detailed guidance in `references/` or `templates/`.
- Do not overwrite downstream `AGENTS.md` files in scaffold behavior.
- Keep validators current when adding required files.

## Validation

Run before finalizing changes:

```bash
python3 scripts/validate_plugin.py
python3 scripts/validate_skill_graph.py
python3 -m py_compile scripts/validate_plugin.py scripts/validate_skill_graph.py scripts/scaffold_project.py
git diff --check
```
