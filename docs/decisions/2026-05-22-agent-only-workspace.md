# 2026-05-22 Agent-Only Workspace

## Status

Accepted

## Context

Assembly needs project docs that are useful to humans and agents, but some files exist only to steer agents. Putting all of that in `docs/` blurs the line between product/project reasoning and agent operating context.

## Options Considered

- Keep `docs/agent-guidance.md` beside the project status and phase files.
- Spread agent notes, logs, and guidance across project folders.
- Keep root `AGENTS.md` as the visible entrypoint and move the rest of the agent-only operating layer under `.agents/`.

## Decision

Keep `AGENTS.md` at the repo root and place other agent-only operating material under `.agents/`.

Instruction-like project files use uppercase names, such as `.agents/AGENT-GUIDANCE.md`. Records and working context use lowercase names, such as `.agents/log.md` and `.agents/notes/`.

Raw source material belongs in top-level `reference/`, not `.agents/` or `docs/`.

## Why This Wins

Agents still have an obvious root instruction file, while agent-only state stays out of the durable project paper trail. Humans can read `docs/` as the project's reasoning history without sorting through operational agent context, and future agents can still resume from `.agents/` when they need handoff details.

## Consequences

Scaffolds must create `.agents/AGENT-GUIDANCE.md`, `.agents/log.md`, `.agents/notes/`, and `reference/` instead of `docs/agent-guidance.md`. Existing projects that already have `docs/agent-guidance.md` should migrate that file into `.agents/AGENT-GUIDANCE.md` when adopting the updated Assembly scaffold.
