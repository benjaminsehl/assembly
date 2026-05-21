# Agent Operating Protocol

Use this protocol at the start of meaningful project work and whenever the user returns after time away.

## Contents

- Orient first
- Phase prerequisites
- Skill routing
- Status escalation
- Prompt clarity
- Missing prerequisites
- Hard boundaries
- Output expectations

## Orient First

1. Read `docs/status.md` if it exists.
2. If the work is inside a subproject, read the nearest `docs/projects/**/status.md` that matches the requested area.
3. Check `docs/phases/`, `docs/product/`, `docs/decisions/`, `docs/specs/`, `docs/plans/`, and relevant child `projects/`.
4. State the current phase and the skill you are using when that materially affects the work.

## Phase Prerequisites

Proposal needs:

- Product vision.
- Product principles.
- Desired outcomes.
- Assumptions.
- What good looks like.

Prototype needs:

- Prototype question.
- Artifact plan.
- Success criteria.
- Link back to the proposal.

Build needs:

- Approved spec.
- Implementation plan.
- Acceptance criteria.
- Verification path.

Release needs:

- QA scope.
- Ship criteria.
- Rollback or hold criteria.
- Grade against the original proposal.

## Skill Routing

- Unknown phase, returning session, scaffold, recovery, retro, or durable project learning: use `project-status`.
- Raw idea, product ambition, business viability, or planned UX critique: use `product-discovery`.
- Tangible learning before production build: use `prototype`.
- Requirements before coding: use `spec`.
- Task breakdown after spec: use `plan`.
- Implementation: use `build`.
- Verification: use `test` or `qa`.
- Pre-merge quality: use `review` or `code-simplify`.
- Release decision: use `ship`.

## Status Escalation

`project-status` is the first stop. It should answer the phase and next skill when the paper trail is clear, and switch into repair mode when it is not.

Use repair mode when:

- The current phase is ambiguous.
- Required artifacts for the apparent phase are missing or contradictory.
- The user asks "what should we do?" and the answer depends on repairing project context.
- The project has skipped gates that should be recorded before more work continues.
- `docs/status.md` is stale, absent, or no longer matches the actual work.

## Prompt Clarity

If the user prompt is unclear, state the inferred task and verify before acting.

Use this shape:

```text
I think you want me to <inferred task>. I see the project is in <phase>. I would use <skill> next because <reason>. Is that right?
```

Ask only when the ambiguity changes the work, risk, or phase.

## Missing Prerequisites

If the prompt is clear but the current phase is missing important context:

1. Warn briefly.
2. Name the missing prerequisite.
3. Recommend the double-back skill.
4. Ask only if skipping would materially change scope or risk.

Use this shape:

```text
I can do that, but we are missing <artifact>. The safer next step is <skill> so we can <reason>. If you still want to proceed, I will continue and mark this as a skipped gate.
```

If the user insists, proceed unless the request crosses a hard safety boundary. In the final response, record the skipped gate and risk. When editing project docs is in scope, also update `docs/status.md`.

## Hard Boundaries

User insistence does not override:

- Privacy and credential boundaries.
- Destructive filesystem or data operations.
- External messages, purchases, trades, money movement, or account changes.
- Security, legal, medical, or financial safety checks.
- Repository instructions that explicitly require confirmation.

## Output Expectations

For phase-sensitive work, the final response should include:

- Phase used.
- Skill used or recommended.
- Evidence checked.
- Missing prerequisites, if any.
- Verification performed.
- Skipped gates, if the user insisted on skipping them.
