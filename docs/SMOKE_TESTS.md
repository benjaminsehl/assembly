# Smoke Tests

These smoke tests verify that the seven entry skills route correctly. They are designed for throwaway projects so the workflows can be exercised without risking real work.

## Prerequisites

Register and enable the plugin, then restart Codex:

```bash
codex plugin marketplace add benjaminsehl/codex-agent-skills
```

If the plugin was already registered before the latest push:

```bash
codex plugin marketplace upgrade codex-agent-skills
```

## Test Matrix

| Entry skill | Smoke prompt | Expected evidence |
| --- | --- | --- |
| `spec` | "Use spec to define a tiny CLI that reverses lines from stdin." | Creates or proposes a spec with assumptions, commands, boundaries, and success criteria. |
| `plan` | "Use plan on the approved spec and create implementation tasks." | Creates a task list with acceptance criteria and verification steps. |
| `build` | "Use build to implement the first task." | Implements one slice, runs checks, and reports changed files. |
| `test` | "Use test to prove blank input returns blank output." | Adds or identifies a failing test first when practical, then passes it. |
| `review` | "Use review on the current diff." | Findings first, file/line references when issues exist, and test gaps. |
| `code-simplify` | "Use code-simplify on the changed files." | Behavior-preserving cleanup with verification evidence. |
| `ship` | "Use ship to decide whether this is ready to release." | GO/NO-GO, blockers, risks, evidence, and rollback procedure. |

## Manual Acceptance Checklist

- [ ] `spec` stops at review instead of drifting into implementation.
- [ ] `plan` writes tasks that can be completed one slice at a time.
- [ ] `build` does not silently skip tests.
- [ ] `test` uses the Prove-It pattern for bugs.
- [ ] `review` leads with findings instead of a summary.
- [ ] `code-simplify` preserves behavior.
- [ ] `ship` does not use subagents unless explicitly authorized.

