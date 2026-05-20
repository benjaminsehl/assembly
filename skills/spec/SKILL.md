---
name: spec
description: Use when defining a project, feature, or significant change before implementation; turns intent into a reviewed specification.
---

# Spec

## Purpose

Define what should be built before coding starts. Surface assumptions, clarify success criteria, and save a spec that future planning and build work can trust.

## Underlying skills

- `interview-me`
- `idea-refine`
- `spec-driven-development`

## Workflow

1. State that the `spec` workflow is active and summarize the user goal in one or two sentences.
2. Read existing project docs and commands when a repo already exists.
3. Surface assumptions before treating the spec as final.
4. If the ask is still fuzzy, use `interview-me` or `idea-refine` to clarify the objective, users, constraints, and tradeoffs.
5. Use `spec-driven-development` to write a spec covering objective, stack, commands, structure, style, testing, boundaries, success criteria, and open questions.
6. Save the spec as `SPEC.md` or `docs/SPEC.md`, following the target repo's conventions.
7. Stop at a human review gate unless the user explicitly asks to continue into planning.

## Verification

- The spec file exists.
- Assumptions and open questions are visible.
- Success criteria are specific enough to test.
- Boundaries include always, ask first, and never categories.

## Stop Conditions

- Success cannot be defined from the current information.
- Major assumptions would be risky to make without user review.
- The request conflicts with repository or safety boundaries.

