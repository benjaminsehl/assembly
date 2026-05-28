---
name: next
description: Contextual next-action dispatcher. Use when the user says "next", "continue", "do the next thing", or asks to proceed through the normal project process.
---

# Next

## Purpose

Choose and perform the next normal workflow step without guessing. Use project docs, phase gates, and recent evidence to decide the next specific skill or action.

`next` is intentionally narrow: it is a dispatcher for continuation, not a replacement for `project-status` or the lifecycle skills.

## References

- `references/project-phases.md`: phase gates, required evidence, and recommended skills.
- `references/agent-operating-protocol.md`: unclear prompts, skipped prerequisites, and safety boundaries.
- `references/workflows/project-lifecycle.md`: status orientation, repair, retro, and learning modes.
- `references/workflows/qa-and-release.md`: PR readiness under the product-gates-first model.

## Workflow

1. State that `next` is active and identify the repo plus project or subproject.
2. Read `AGENTS.md`, root `docs/status.md`, nearest subproject `status.md`, `.agents/log.md` when present, and any task/spec/plan file explicitly named by status.
3. Determine the active phase, last completed gate, missing required evidence, and whether the next step is safe to infer.
4. If there is no Assembly project trail in this repo, do not stop and do not auto-scaffold. Ask the user once whether to scaffold the project (one-question handoff). On confirmation, hand off to `project-status` for scaffolding and continue from the new trail.
5. If status is stale, contradictory, or missing, perform the `project-status` repair behavior first: audit the project trail, update `docs/status.md` when project-doc edits are in scope, and report the recovery path.
6. Before dispatching into prototype, spec, plan, build, or release work, check whether the project trail answers the product gates:
   - What is being built.
   - Why it matters.
   - What good looks like.
   - Risks and non-goals.
   - Rollback or hold criteria (when the change touches production behavior).

   If any product gate is missing and the user has not delegated judgment, ask concise questions in product-implication language (never engineering-implementation detail). Flag business, user, and viability concerns; do not decide them. Route to `product-discovery` or `spec` when the gap is too large for inline questions.
7. If exactly one next step is unambiguous and low-risk, load and follow that public skill's workflow before running the step:
   - Proposal gaps: use `product-discovery` or `spec`.
   - Prototype gaps: use `prototype`.
   - Build gaps: use `spec`, `plan`, `build`, `test`, `review`, or `code-simplify` as the next unfinished gate requires.
   - Release gaps: use `qa`, `review`, or `ship`.
   - GitHub handoff gaps: commit, push, draft PR, self-review, code-simplify, then proceed through ready, merge, and deploy automatically when product gates are clear and verification is green. Honor the always-ask floor regardless of product-gate clarity.
8. If multiple plausible next steps exist, do not pick arbitrarily and do not ask a single narrow question. Lay out the 2-3 highest-leverage candidate next steps, cite the evidence that supports each, and ask the user to pick.
9. If the user asks to skip a missing prerequisite, warn once, name the skipped gate and the product risk it would have caught, then proceed only when the user insists and no always-ask floor item applies.
10. End by naming the action taken, evidence used, status/docs updated or intentionally left unchanged, and the next expected gate.

## Gating Model

- Product gates (what / why / what good looks like / risks / rollback) open the engineering rails. Once those gates are clear and verification is green, ready-for-review, merge, and deploy proceed automatically.
- Always-ask floor (regardless of product-gate clarity): money movement, credentials, privacy-sensitive data, external messaging, irreversible destructive operations (force-push to default branch, delete branches with unmerged work, drop tables, delete production data), and merge/deploy/ready transitions when verification is not green or material review concerns are unresolved.

## Verification

- The chosen next action cites project files, status, commits, tasks, tests, or plans.
- The response explains why this action is next instead of merely saying it was inferred.
- Ambiguous forks produce a 2-3-option pick list with evidence, not a single narrow question.
- Stale or missing status triggers repair behavior before continuation.
- Product-gate gaps trigger concise questions in product-implication language or the appropriate double-back skill.
- Ready-for-review, merge, and deploy proceed automatically when product gates are clear and verification is green; they ask when any product gate is unmet or when an always-ask floor item applies.
- Skipped gates are recorded in the response and in `docs/status.md` when project-doc edits are in scope.

## Stop Conditions

- The next action would touch an always-ask floor item without explicit founder approval: money movement, credentials, privacy-sensitive data, external messaging, irreversible destructive operations, or a merge/deploy/ready transition with unmet product gates or failing verification.
- Choosing among multiple active project slices would be arbitrary (use the 2-3-option pick list instead).
