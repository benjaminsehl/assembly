---
name: new-project
description: Use when starting a new project or substantial project slice; scaffolds project docs, proposal outcomes, phase gates, decisions, plans, specs, and status tracking.
---

# New Project

## Purpose

Create a lightweight project workspace that keeps product vision, proposal outcomes, prototype evidence, build plans, decisions, QA, release, and retro artifacts in one place.

## Underlying skills

- `product-discovery`
- `founder-review`
- `business-model-review`
- `spec-driven-development`
- `planning-and-task-breakdown`
- `documentation-and-adrs`

## Workflow

1. State that `new-project` is active and name the project or project slice.
2. If the idea is raw, run `product-discovery` before scaffolding detailed specs.
3. Use `founder-review` and `business-model-review` when the project has meaningful product or business risk.
4. Inspect the repo for existing `docs/project`, `docs/projects`, `docs/plans`, `docs/specs`, ADRs, or `.agents` project notes so the scaffold fits the local convention.
5. Read `references/project-phases.md` and `references/project-kernel-structure.md` for the phase model and folder contract.
6. Run `scripts/scaffold_project.py` from this plugin when a deterministic scaffold is useful, passing the target repo root, project name, and slug.
7. Fill the proposal phase with known outcomes, assumptions, principles, and what should become 10x better.
8. Save unknowns as explicit open questions instead of pretending alignment exists.
9. Recommend the next skill: usually `product-discovery`, `spec`, `prototype`, or `plan`.

## Verification

- A project workspace exists without overwriting existing files unless explicitly requested.
- Proposal, prototype, build, and release phase files exist.
- Product vision, decisions, tech design, specs, plans, QA, and release folders exist.
- Current phase and next recommended skills are visible in project status.

## Stop Conditions

- The target repo or project slice is unclear and multiple scaffolds would be plausible.
- The project has no concrete outcome or user problem yet.
- Existing project docs conflict with the requested structure and merging them would risk losing context.
