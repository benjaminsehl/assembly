---
name: build
description: Use when implementing the next planned task or a named vertical slice with tests, verification, and disciplined git hygiene.
---

# Build

## Purpose

Implement exactly one planned slice at a time, keeping the codebase working and leaving evidence that the task is complete.

## References

- `references/workflows/engineering-delivery.md`: build mode, incremental implementation, test-first behavior, debugging, and git hygiene.
- `references/testing-patterns.md`: testing patterns and regression coverage.

## Workflow

1. State that the `build` workflow is active and identify the target task.
2. Read `tasks/todo.md`, `tasks/plan.md`, or the named task source. Choose the first pending task unless the user names a different one.
3. Load the task acceptance criteria, relevant source files, and project commands.
4. For behavior changes, write or identify the failing/targeted test before implementation where practical.
5. Make the smallest complete change that satisfies the task.
6. If tests, build, or runtime checks fail, isolate the root cause before changing approach.
7. Run targeted verification and the broadest practical regression check.
8. Update the task status only after verification passes or skipped checks are explained.
9. Stage, commit, and push only when the user asked for publishing or the repo workflow requires it.

## Verification

- Changed files are named.
- Tests or checks run are reported with results.
- The task acceptance criteria are satisfied.
- Any skipped verification has a concrete reason.

## Stop Conditions

- No task list or named acceptance criteria exist.
- The next task is too broad to complete safely in one slice.
- Verification fails and cannot be isolated without changing scope.
- The task crosses an ask-first boundary.
