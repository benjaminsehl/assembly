---
name: project-status
description: Use when returning to a project for lightweight phase orientation, missing artifact detection, next decision gate, and next Codex skills.
---

# Project Status

## Purpose

Orient a returning session. Determine which project or subproject is active, whether it is in proposal, prototype, build, or release, then recommend the next skills and next action from evidence.

Keep this workflow lightweight. If the phase, paper trail, or recovery path is unclear, recommend `introspect` for the deeper audit and status repair pass.

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

1. State that `project-status` is active and identify the repo plus the project or subproject folder being assessed.
2. Inspect the root docs tree first: `docs/status.md`, `docs/projects/*/status.md`, nested `projects/*/status.md`, phase files, `docs/agent-guidance.md`, `docs/plans`, `docs/specs`, ADRs, open tasks, recent commits, and relevant `.agents` notes.
3. Read `references/project-phases.md` for phase gates, `references/agent-operating-protocol.md` for skipped-gate behavior, and `references/hyper-project-notes.md` when retrofitting a scattered project like Hyper.
4. Use `context-engineering` to map the current artifacts and avoid re-reading unrelated docs.
5. Apply Chesterton's fence: before recommending removal or replacement, identify the decision, principle, or historical artifact that explains why the current shape exists.
6. Classify the phase:
   - Proposal: outcomes, assumptions, principles, or success criteria are not aligned.
   - Prototype: direction needs tangible proof before production build.
   - Build: approved direction exists and implementation slices are active.
   - Release: built work needs QA, polish, ship decision, grading, and follow-up capture.
7. Use `documentation-and-adrs` to propose status-file updates when the repo has a project workspace.
8. Evaluate missing phase prerequisites and whether the user is trying to skip a gate.
9. If the phase is unclear, core artifacts are missing, or the project seems off track, recommend `introspect` before proceeding with build or release work.
10. Output current phase, evidence, missing artifacts, skipped-gate risks, next gate, next recommended skills, and one concrete next action.

## Verification

- The phase verdict cites actual files, diffs, commits, tasks, or notes.
- Missing artifacts are separated from optional polish.
- Skipped gates and their risks are named when the user asks to move ahead anyway.
- Recommended skills match the current phase and blockers.
- `introspect` is recommended when the project needs a deeper workflow-conformity audit or status update.
- The user can resume with one clear next action.

## Stop Conditions

- There is no accessible repo, project folder, or artifact trail to assess.
- Multiple project slices are active and choosing one would be arbitrary.
- The current state depends on private external systems that are unavailable.
