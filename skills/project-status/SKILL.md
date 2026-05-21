---
name: project-status
description: Use when returning to a project to determine the current phase, missing artifacts, next decision gate, and the next Codex skills to invoke.
---

# Project Status

## Purpose

Orient a returning session. Determine whether the project is in proposal, prototype, build, or release, then recommend the next skills and next action from evidence.

## Underlying skills

- `context-engineering`
- `documentation-and-adrs`
- `product-discovery`
- `prototype`
- `build`
- `qa`
- `ship`
- `retro`
- `learn`

## Workflow

1. State that `project-status` is active and identify the repo and project folder being assessed.
2. Inspect `docs/project/status.md`, `docs/projects/*/status.md`, phase files, `docs/plans`, `docs/specs`, ADRs, open tasks, recent commits, and relevant `.agents` notes.
3. Read `references/project-phases.md` for phase gates and `references/hyper-project-notes.md` when retrofitting a scattered project like Hyper.
4. Use `context-engineering` to map the current artifacts and avoid re-reading unrelated docs.
5. Classify the phase:
   - Proposal: outcomes, assumptions, principles, or success criteria are not aligned.
   - Prototype: direction needs tangible proof before production build.
   - Build: approved direction exists and implementation slices are active.
   - Release: built work needs QA, polish, ship decision, grading, and follow-up capture.
6. Use `documentation-and-adrs` to propose status-file updates when the repo has a project workspace.
7. Output current phase, evidence, missing artifacts, next gate, next recommended skills, and one concrete next action.

## Verification

- The phase verdict cites actual files, diffs, commits, tasks, or notes.
- Missing artifacts are separated from optional polish.
- Recommended skills match the current phase and blockers.
- The user can resume with one clear next action.

## Stop Conditions

- There is no accessible repo, project folder, or artifact trail to assess.
- Multiple project slices are active and choosing one would be arbitrary.
- The current state depends on private external systems that are unavailable.
