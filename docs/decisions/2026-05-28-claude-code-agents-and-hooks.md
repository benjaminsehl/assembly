# 2026-05-28 Claude Code Agents and Hooks

## Status

Accepted

## Context

Assembly already authored three specialist personas (`code-reviewer`,
`security-auditor`, `test-engineer`) under `.agents/personas/`, and the `review`
and `ship` skills promise to "fan out to specialist reviewers in parallel." But
the bundle never declared them as plugin agents: `.claude-plugin/plugin.json` had
no `agents` key, and `.agents/personas/` is not the default `agents/` discovery
path, so on Claude Code there was nothing to fan out to. The personas README also
claimed they were "auto-discovered (no path config needed)," which was incorrect.

Separately, Assembly's safety model is prose. The scaffold grants maximum default
permissions (`bypassPermissions` on Claude Code, `approval_policy = "never"` on
Codex) for speed, and relies on an "ask-first floor" in [`SPEC.md`](../../plugins/assembly/docs/SPEC.md)
— confirm before merging, deploying, destructive ops, etc. — that the model is
asked to honor. There was no runtime enforcement of that floor.

Claude Code plugins support two surfaces that Codex does not: subagents and hooks.
The reference adaptation is Addy Osmani's `agent-skills`, which ships the same
three agents plus a `SessionStart` hook.

## Options Considered

- **Do nothing** — keep personas as docs. Leaves `review`/`ship` fan-out broken on
  Claude Code and the safety floor unenforced.
- **Move personas to `agents/`** — breaks `validate_plugin.py`, which requires the
  files at `.agents/personas/`, and duplicates content if both paths are kept.
- **Declare existing persona files in `plugin.json` `agents` + add plugin-level
  hooks** — activates what already exists with no move and no duplication.
  *(Chosen.)*
- **Add many more agents / an orchestrator** — rejected; the repo's own
  orchestration-patterns catalog warns against router and deep-tree anti-patterns,
  and the platform blocks subagents spawning subagents anyway.

## Decision

On the Claude Code runtime only, the bundle now ships:

1. **Agents.** `.claude-plugin/plugin.json` declares an `agents` array pointing at
   the existing `.agents/personas/*.md` files (no move). Each persona declares a
   `model` (Sonnet for `code-reviewer`/`test-engineer`, Opus for
   `security-auditor`) that can be tuned per persona.
2. **Hooks** in `plugins/assembly/hooks/`:
   - `session-start.sh` (SessionStart) — orients each session to `docs/status.md`,
     the current phase, and recommended next skills. Silent when there is no
     `docs/status.md`.
   - `ask-first-guard.sh` (PreToolUse on `Bash`) — returns
     `permissionDecision: "ask"` when a command looks like a floor action (merge,
     ready, non-draft PR, release, force/main/delete push, branch/history
     destruction, deploy, publish, `rm -rf`). Everything else passes through.

Codex manifests, marketplace, and skills are unchanged except a version bump to
keep both runtimes in sync. Both manifests move to `0.10.0`.

## Why This Wins

- Activation, not new surface area: the agents already existed and were already
  documented; this makes the documented behavior real on Claude Code.
- The guard converts Assembly's central safety prose into runtime enforcement — it
  is the counterweight that makes the scaffold's maximum default permissions safe,
  reintroducing friction only at irreversible boundaries.
- Bounded cost surface: two short hook scripts and one manifest array. No protocol
  abstraction, no runtime detection inside skills, consistent with the dual-runtime
  decision ([2026-05-27](2026-05-27-dual-runtime-claude-code.md)).

## Consequences

- **Easier:** `review`/`ship` fan-out resolves to real subagents on Claude Code;
  every session self-orients; the floor is enforced even under `bypassPermissions`.
- **Harder / riskier:** two more bash scripts to maintain and keep cross-platform
  (they run under Git Bash on Windows). The guard biases toward asking, so it may
  occasionally prompt on a benign command (one keystroke approves), and it cannot
  see money, credential, or external-messaging actions that are not shell commands
  — those stay governed by the protocol and tool-level permission prompts.
- **Unaffected:** Codex behavior. Agents and hooks are invisible to it; it keeps
  the shared skills and its own approval policy.

## Out of Scope

- Additional agents or any orchestrator persona.
- Opt-in hooks (e.g. citation caching, simplify-ignore) from the upstream
  reference — deferred until there is a proven need.
- Codex-side equivalents of agents/hooks (the runtime has no such concept).
