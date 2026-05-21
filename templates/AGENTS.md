# Agent Instructions

This project follows a phase-aware product-building workflow.

## Start Here

Before meaningful work, read:

- `docs/status.md`
- The nearest matching `docs/projects/**/status.md`, if working in a subproject
- `docs/agent-guidance.md`
- Relevant files under `docs/phases/`, `docs/product/`, `docs/decisions/`, `docs/specs/`, and `docs/plans/`

If these files do not exist yet, use `new-project` to scaffold them.

## Phase Awareness

Always identify the current project phase before choosing a workflow:

- Proposal: align on outcomes, assumptions, principles, and what good looks like.
- Prototype: create tangible proof before production build.
- Build: implement approved specs in verified slices.
- Release: QA, polish, ship or hold, grade against proposal, and capture follow-up learning.

Use `project-status` when returning to a project or when the phase is unclear. If `project-status` finds an unclear phase, stale status, skipped gates, or missing core context, use `introspect` before proceeding. Do not start with `introspect` unless the user explicitly asks for it.

## Skill Routing

- New project or subproject: `new-project`
- Raw idea: `product-discovery`
- Scope or ambition review: `founder-review`
- Business viability: `business-model-review`
- UX before build: `design-plan-review`
- Tangible proof: `prototype`
- Requirements: `spec`
- Task breakdown: `plan`
- Implementation: `build`
- Tests and runtime verification: `test` or `qa`
- Quality pass: `review` or `code-simplify`
- Release decision: `ship`
- Afterward: `retro` and `learn`

## Unclear Prompts

If the prompt is unclear, state what you think the user wants, name the current phase, recommend the next skill, and verify before acting.

## Missing Phase Context

If the user asks to skip ahead while important phase context is missing, warn them, name the missing artifact, and recommend the double-back skill first.

If the user insists, proceed unless the request crosses a hard safety, privacy, destructive, credential, money movement, external messaging, or confirmation boundary. Record skipped gates in the final response and update `docs/status.md` when project-doc edits are in scope.

## Paper Trail

Preserve Chesterton's fence. Before changing or removing an existing structure, look for the decision, principle, plan, or status note that explains why it exists.
