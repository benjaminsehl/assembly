# Agent Instructions

This project follows a phase-aware product-building workflow.

## Start Here

Before meaningful work, read:

- `docs/status.md`
- The nearest matching `docs/projects/**/status.md`, if working in a subproject
- `docs/agent-guidance.md`
- Relevant files under `docs/phases/`, `docs/product/`, `docs/decisions/`, `docs/specs/`, and `docs/plans/`

If these files do not exist yet, use `project-status` scaffold mode.

## Phase Awareness

Always identify the current project phase before choosing a workflow:

- Proposal: align on outcomes, assumptions, principles, and what good looks like.
- Prototype: create tangible proof before production build.
- Build: implement approved specs in verified slices.
- Release: QA, polish, ship or hold, grade against proposal, and capture follow-up learning.

Use `project-status` when returning to a project, scaffolding missing docs, repairing stale status, or when the phase is unclear.

## Skill Routing

- These route names refer to the Codex Agent Skills plugin's phase-aware lifecycle workflows.
- If another installed skill has the same name, prefer Codex Agent Skills for project lifecycle decisions in this repo.
- New project, subproject, status, repair, retro, or project learning: `project-status`
- Raw idea, scope, ambition, business viability, or UX before build: `product-discovery`
- Tangible proof: `prototype`
- Requirements: `spec`
- Task breakdown: `plan`
- Implementation: `build`
- Tests and runtime verification: `test` or `qa`
- Quality pass: `review` or `code-simplify`
- Release decision: `ship`

## Unclear Prompts

If the prompt is unclear, state what you think the user wants, name the current phase, recommend the next skill, and verify before acting.

## Missing Phase Context

If the user asks to skip ahead while important phase context is missing, warn them, name the missing artifact, and recommend the double-back skill first.

If the user insists, proceed unless the request crosses a hard safety, privacy, destructive, credential, money movement, external messaging, or confirmation boundary. Record skipped gates in the final response and update `docs/status.md` when project-doc edits are in scope.

## Paper Trail

Preserve Chesterton's fence. Before changing or removing an existing structure, look for the decision, principle, plan, or status note that explains why it exists.
