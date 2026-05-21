---
name: introspect
description: Use when a project needs a deeper workflow audit, status repair, or recovery plan after project-status finds unclear phase, missing context, or skipped gates.
---

# Introspect

## Purpose

Audit how well a project or subproject conforms to the desired phase-aware project shape. Use this after `project-status` when the current phase is unclear, important context is missing, or the user asks what to do next and the project needs recovery rather than ordinary orientation.

The output should update the project paper trail when appropriate, especially `docs/status.md`, then give the user a grounded plan to get the project back on track.

## Underlying skills

- `project-status`
- `context-engineering`
- `documentation-and-adrs`
- `founder-product-critique`
- `business-model-evaluation`

## Workflow

1. State that `introspect` is active and identify the repo plus the project or subproject being audited.
2. Run the `project-status` workflow first to establish the current phase, likely missing artifacts, and candidate next skills.
3. Use `context-engineering` to map the relevant evidence without rereading unrelated docs:
   - `docs/status.md`
   - nearest `docs/projects/**/status.md`
   - `docs/agent-guidance.md`
   - `docs/phases/`
   - `docs/product/`
   - `docs/decisions/`
   - `docs/specs/`
   - `docs/plans/`
   - `docs/prototypes/`
   - `docs/qa/`
   - `docs/release/`
   - recent commits, open tasks, and issue or PR notes when available
4. Compare the evidence to `references/project-phases.md` and `references/agent-operating-protocol.md`.
5. Identify whether the project is:
   - On track: phase and next gate are clear.
   - Thin but usable: phase is clear, but important context should be filled soon.
   - Off track: phase, success criteria, decisions, or next gate are ambiguous.
   - Blocked: the next action depends on unavailable information, external systems, or user judgment.
6. Use `founder-product-critique` to flag user-love, ambition, scope, and "10-star product" gaps that explain why the project feels weak or underdefined.
7. Use `business-model-evaluation` when the project has a monetization, ICP, distribution, retention, or cost-risk assumption that affects what should happen next.
8. Use `documentation-and-adrs` to update `docs/status.md` when project-doc edits are in scope. The update should record current phase, conformity verdict, missing artifacts, skipped gates, next gate, next recommended skills, and one recovery plan.
9. Report the audit in a compact shape:
   - Current phase and confidence.
   - Conformity verdict.
   - Evidence checked.
   - Missing or weak artifacts.
   - Skipped gates or Chesterton's-fence risks.
   - Recovery plan.
   - Next recommended skills.
   - First concrete action.

## Verification

- The phase and conformity verdict cite actual files, commits, tasks, or notes.
- Missing required artifacts are separated from optional polish.
- Any `docs/status.md` update is described, or the reason for skipping it is stated.
- The recovery plan names the next decision gate and the next skills to use.
- User-love, engineering, and business concerns are separated when all three are relevant.

## Stop Conditions

- There is no accessible repo, project folder, or artifact trail to audit.
- Multiple active project slices are plausible and choosing one would be arbitrary.
- Updating `docs/status.md` would overwrite unrelated user work or project-doc edits are out of scope.
- The project state depends on private external systems that are unavailable.
