---
name: plan
description: Use when turning an approved spec into small, dependency-ordered tasks with acceptance criteria and verification steps.
---

# Plan

## Purpose

Break approved work into small, verifiable tasks that can be implemented one focused slice at a time.

## Underlying skills

- `planning-and-task-breakdown`
- `context-engineering`

## Workflow

1. State that the `plan` workflow is active and identify the spec or source requirements being planned.
2. Read the approved spec, relevant docs, project structure, and existing commands.
3. Use `context-engineering` to keep only the relevant parts of the repo and spec in scope.
4. Use `planning-and-task-breakdown` to map dependencies and choose a vertical-slice order.
5. Write tasks with acceptance criteria, verification commands, likely files, and dependencies.
6. Add checkpoints after meaningful phases.
7. Save the plan to `tasks/plan.md` and the execution checklist to `tasks/todo.md` unless the repo has a stronger convention.
8. Stop at a human review gate before implementation.

## Verification

- Every task has acceptance criteria.
- Every task has a verification step.
- Dependencies and checkpoints are explicit.
- Tasks are small enough for focused implementation sessions.

## Stop Conditions

- No spec or equivalent requirements exist.
- The work cannot be split into safe verifiable slices.
- The plan requires credentials, external services, or irreversible changes that have not been approved.

