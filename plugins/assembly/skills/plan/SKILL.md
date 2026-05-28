---
name: plan
description: Use when turning an approved spec into small, dependency-ordered tasks with acceptance criteria and verification steps.
---

# Plan

## Purpose

Break approved work into small, verifiable tasks that can be implemented one focused slice at a time. Each task carries a thin contract: acceptance criteria, verification, files touched, dependencies.

## References

- `references/workflows/engineering-delivery.md`: planning mode, slices, checkpoints, and verification.
- `references/project-phases.md`: build-phase entry gate.

## Workflow

1. State that the `plan` workflow is active and identify the spec or source requirements being planned.
2. Read the approved spec, relevant docs, project structure, and existing commands.
3. Keep only the relevant parts of the repo and spec in scope.
4. Map dependencies and choose a vertical-slice order.
5. Write each task with a thin contract:
   - Acceptance criteria (what done looks like).
   - Verification command or check.
   - Likely files touched.
   - Dependencies on other tasks.
6. Add checkpoints after meaningful phases.
7. If the plan crosses 5 tasks, flag it for founder review before saving. Ask whether to split the slice further or accept the larger plan.
8. Save the plan to `tasks/plan.md` and the execution checklist to `tasks/todo.md` unless the repo has a stronger convention.
9. Stop at a founder review gate before implementation.

## Mid-Plan Pivot

Plans are not contracts with the future. When `build` surfaces evidence that contradicts the plan (wrong assumption, hidden dependency, simpler path discovered), re-enter `plan` mid-stream: name the contradicting evidence, revise the affected tasks, update `tasks/plan.md`, and continue. Do not silently work around stale tasks.

## Verification

- Every task has acceptance criteria.
- Every task has a verification step.
- Every task names likely files and dependencies.
- Dependencies and checkpoints are explicit.
- Tasks are small enough for focused implementation sessions.
- Plans over 5 tasks have founder sign-off before saving.

## Stop Conditions

- No spec or equivalent requirements exist.
- The work cannot be split into safe verifiable slices.
- The plan requires credentials, external services, or irreversible changes that have not been approved.
- Spec discovery is stale or missing — route back to `spec`.
