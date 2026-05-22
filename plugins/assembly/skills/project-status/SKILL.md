---
name: project-status
description: Project orientation gateway. Use when returning to work, starting/scaffolding a project, checking phase, repairing stale status, or asking what to do next.
---

# Project Status

## Purpose

Orient the project before work continues. Determine the active project or subproject, current phase, missing prerequisites, next gate, and next skill.

This is also the gateway for project start, scaffold, and repair. Do not route to separate `new-project` or `introspect` skills; use the references below.

## References

- `references/project-phases.md`: phase gates and status output shape.
- `references/project-kernel-structure.md`: root `docs/` and recursive subproject structure.
- `references/agent-operating-protocol.md`: unclear prompts, missing prerequisites, skipped gates, and safety boundaries.
- `references/workflows/project-lifecycle.md`: scaffold, status, repair, retro, and learning modes.
- `references/hyper-project-notes.md`: only for retrofitting scattered Hyper-style notes.

## Workflow

1. State that `project-status` is active and identify the repo plus project or subproject.
2. Inspect `docs/status.md`, nearest `docs/projects/**/status.md`, phase files, product docs, decisions, specs, plans, QA/release notes, `.agents/log.md`, relevant `.agents/notes/`, `reference/`, open tasks, and recent commits.
3. If project docs are missing and the user is starting or restarting work, use scaffold mode from `references/workflows/project-lifecycle.md` and `scripts/scaffold_project.py`.
4. Classify the phase:
   - Proposal: outcomes, assumptions, principles, or success criteria are not aligned.
   - Prototype: direction needs tangible proof before production build.
   - Build: approved direction exists and implementation slices are active.
   - Release: built work needs QA, polish, ship decision, grading, and follow-up capture.
5. Apply Chesterton's fence: name the decision, principle, or historical artifact that explains the current shape before recommending replacement.
6. If phase, status, or recovery path is unclear, run repair mode: audit conformance, update `docs/status.md` when project-doc edits are in scope, and produce a recovery plan.
7. Output current phase, evidence, missing artifacts, skipped-gate risks, next gate, next recommended skills, and one concrete next action.

## Verification

- The phase verdict cites actual files, diffs, commits, tasks, or notes.
- Missing artifacts are separated from optional polish.
- Skipped gates and their risks are named when the user asks to move ahead anyway.
- Recommended skills match the current phase and blockers.
- `docs/status.md` is updated when project-doc edits are in scope, or the reason for not updating it is stated.
- The user can resume with one clear next action.

## Stop Conditions

- There is no accessible repo, project folder, or artifact trail to assess.
- Multiple project slices are active and choosing one would be arbitrary.
- The current state depends on private external systems that are unavailable.
