# Hooks

Plugin-level hooks that Claude Code loads from `hooks/hooks.json` when Assembly is
enabled. **Claude Code only** — Codex does not read this directory, so these hooks
are additive enhancements that degrade to nothing on the Codex runtime. The shared
`skills/` surface is identical in both.

These ship intentionally small, read-only or ask-only, and dependency-light. They
never modify files and never block a tool call on a missing dependency.

## Contents

- SessionStart primer
- Ask-first guard
- Design constraints
- Opting out

## SessionStart primer — `session-start.sh`

Runs when a session starts or resumes. If the working directory is an Assembly
project (it has `docs/status.md`), it injects a short orientation into the
session: read `docs/status.md` first, the current phase, the skills `status.md`
recommends next, the lifecycle spine, and the ask-first floor. If there is no
`docs/status.md`, it emits nothing and exits 0, so non-Assembly projects are
unaffected.

This operationalizes the project convention that *agents get one obvious place to
start: `docs/status.md`* — instead of relying on the user to remember to invoke a
skill at the top of every session.

## Ask-first guard — `ask-first-guard.sh`

A `PreToolUse` hook on the `Bash` tool. When a command looks like one of the
ask-first-floor actions, it returns `permissionDecision: "ask"` with a reason, so
the human confirms even when the project runs under `bypassPermissions`. It is the
runtime counterpart to the prose floor in [`docs/SPEC.md`](../docs/SPEC.md): the
scaffold grants maximum default permissions for speed, and this guard re-introduces
friction **only** at the irreversible boundaries.

It re-prompts on:

| Class | Examples |
| --- | --- |
| PR merge / ready / non-draft create / release | `gh pr merge`, `gh pr ready`, `gh pr create` (without `--draft`), `gh release create` |
| Force / main / delete pushes | `git push --force`, `git push … main`, `git push --delete` |
| Branch & history destruction | `git branch -D`, `git reset --hard`, `git clean -f…` |
| Deploy / publish | `wrangler deploy`, `vercel … --prod`, `netlify deploy`, `npm/pnpm/yarn/bun publish` |
| Destructive filesystem | `rm -rf` |

Anything else passes through untouched (a normal `git push` of a topic branch, for
example, is not flagged — that is the standard Assembly build handoff).

**Limits.** It only sees shell commands. Money movement, credential use, and
external messaging that happen through other tools are not detectable here; those
stay governed by the protocol and Claude Code's own tool-level permission prompts.
It biases toward asking, so it may occasionally ask about a benign command — a
single keystroke approves.

## Design constraints

- **No file mutation.** Both hooks are read-only / ask-only.
- **Graceful degradation.** The guard prefers `jq`, falls back to `python3`, and
  finally scans the raw payload; it never blocks a tool call because a tool is
  missing.
- **Cross-platform.** Plain `bash` + POSIX text tools. On Windows these run under
  Git Bash, the same as other plugin command hooks.
- **`${CLAUDE_PLUGIN_ROOT}`** resolves to this bundle so the hook commands find
  these scripts regardless of where the plugin is installed.

## Opting out

Plugin hooks run once the plugin is enabled. To disable them, disable the Assembly
plugin, or remove an entry from `hooks/hooks.json` in your local cache. To tune the
guard's command classes, edit `ask-first-guard.sh`.
