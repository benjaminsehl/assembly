---
name: new-project
description: Use when starting a new project, subproject, or substantial project slice; scaffolds root docs, phase gates, decisions, plans, specs, and status tracking.
---

# New Project

## Purpose

Create a lightweight project workspace in the repo's `docs/` tree that keeps product vision, proposal outcomes, prototype evidence, build plans, decisions, QA, release, and retro artifacts together.

## Underlying skills

- `product-discovery`
- `founder-review`
- `business-model-review`
- `spec-driven-development`
- `planning-and-task-breakdown`
- `documentation-and-adrs`

## Workflow

1. State that `new-project` is active and name the project, subproject, or project slice.
2. If the idea is raw, run `product-discovery` before scaffolding detailed specs.
3. Use `founder-review` and `business-model-review` when the project has meaningful product or business risk.
4. Use the repo's root `docs/` tree as the default documentation boundary unless the user explicitly wants a separate repo or package-level docs.
5. Inspect existing `docs/status.md`, `docs/projects`, nested `projects/`, `docs/plans`, `docs/specs`, ADRs, or `.agents` notes so the scaffold fits the local convention.
6. Treat projects as recursive: a repo can be a project, and features, clients, agent layers, or releases inside it can be subprojects.
7. Preserve the paper trail for Chesterton's fence: record why decisions exist before changing or removing them.
8. Read `references/project-phases.md` and `references/project-kernel-structure.md` for the phase model and folder contract.
9. Read `references/agent-operating-protocol.md` when the project needs agent behavior guidance.
10. Run `scripts/scaffold_project.py` from this plugin when a deterministic scaffold is useful, passing the target root, project name, slug, and optional parent project workspace.
11. If `AGENTS.md` already exists and the scaffold skips it, tell the user to merge `templates/AGENTS.md` manually instead of overwriting local instructions.
12. Fill the proposal phase with known outcomes, assumptions, principles, and what should become 10x better.
13. Save unknowns as explicit open questions instead of pretending alignment exists.
14. Recommend the next skill: usually `product-discovery`, `spec`, `prototype`, or `plan`.

## Verification

- A root or nested docs workspace exists without overwriting existing files unless explicitly requested.
- Proposal, prototype, build, and release phase files exist.
- Product vision, decisions, tech design, specs, plans, QA, and release folders exist.
- A child `projects/` folder exists so subprojects can carry their own paper trail.
- `docs/agent-guidance.md` exists, and root `AGENTS.md` exists or was explicitly skipped for manual merge.
- Current phase and next recommended skills are visible in project status.

## Stop Conditions

- The target repo or project slice is unclear and multiple scaffolds would be plausible.
- The project has no concrete outcome or user problem yet.
- Existing project docs conflict with the requested structure and merging them would risk losing context.
