---
name: build
description: Use when implementing the next planned task or a named vertical slice with tests, verification, and disciplined git hygiene.
---

# Build

## Purpose

Execute the build track for a named slice or the next inferred engineering gate. When the user invokes `build` with an empty or minimal prompt, orient from project docs and get to work on the first unambiguous step in the engineering spine.

Build can dispatch across `spec`, `plan`, implementation, `test`, `review`, `code-simplify`, and GitHub handoff behavior as needed. It should not stop merely because the user did not name a task if the project trail makes the next build action clear.

## References

- `references/workflows/engineering-delivery.md`: build mode, incremental implementation, test-first behavior, debugging, and git hygiene.
- `references/testing-patterns.md`: testing patterns and regression coverage.
- `references/project-phases.md`: build prerequisites and engineering phase gates.
- `references/agent-operating-protocol.md`: unclear prompts, skipped prerequisites, and hard boundaries.

## Workflow

1. State that the `build` workflow is active. If no target task was provided, say you are inferring the next build-track action from the project trail.
2. Orient from `AGENTS.md`, `docs/status.md`, relevant `docs/specs/`, `docs/plans/`, task files, current branch, and git status. Use the nearest project or subproject trail.
3. Determine the first unambiguous unfinished gate in this order:
   - Missing or stale build requirements: use `spec` behavior to draft or repair the spec when project docs make the desired outcome clear.
   - Approved spec but missing task breakdown: use `plan` behavior to create the next implementation plan.
   - Pending planned task: implement the first pending task unless the user named another one.
   - Implemented but unverified changes: use `test` behavior for targeted and practical regression checks.
   - Verified but unreviewed changes: use `review` behavior, then `code-simplify` when safe simplification is available.
   - Verified material GitHub-backed changes without handoff: commit, push, and open or update a descriptive draft PR.
4. If a missing prerequisite would materially change product direction, warn and ask before inventing it. If the missing prerequisite is mechanical and recoverable from existing docs, create or repair it and keep moving.
5. Load acceptance criteria, relevant source files, and project commands for the selected gate.
6. For behavior changes, write or identify the failing/targeted test before implementation where practical.
7. Make the smallest complete change that satisfies the selected gate.
8. If tests, build, or runtime checks fail, isolate the root cause before changing approach.
9. Run targeted verification and the broadest practical regression check.
10. Update task/status docs only after verification passes or skipped checks are explained.
11. For material changes in a GitHub-backed repo, follow the GitHub handoff from `references/workflows/engineering-delivery.md`: focused commit, push a topic branch, and open or update a descriptive draft PR unless the user asked for local-only work or handoff is blocked.

## Verification

- Changed files are named.
- Empty or minimal build prompts still produce an evidence-backed chosen gate instead of a generic stop.
- Tests or checks run are reported with results.
- The task acceptance criteria are satisfied.
- GitHub-backed work is committed, pushed, and linked to a descriptive draft PR when handoff is in scope and not blocked.
- Blocked handoff names the failed command or missing access, completed local work, verification status, and next recovery step.
- Any skipped verification has a concrete reason.

## Stop Conditions

- No project trail, named task, spec, plan, issue, or code evidence exists from which to infer a non-arbitrary build action.
- Multiple plausible build targets exist and choosing among them would be arbitrary.
- Missing product or design decisions would materially change what should be built and the user has not delegated those decisions.
- The next task is too broad to complete safely in one slice and cannot be split mechanically from existing docs.
- Verification fails and cannot be isolated without changing scope.
- The task crosses an ask-first boundary.
