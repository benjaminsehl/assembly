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
- `references/workflows/qa-and-release.md`: PR readiness and ask-first ready-for-review gates.

## Workflow

1. State that `next` is active and identify the repo plus project or subproject.
2. Read `AGENTS.md`, root `docs/status.md`, nearest subproject `status.md`, `.agents/log.md` when present, and any task/spec/plan file explicitly named by status.
3. Determine the active phase, last completed gate, missing required evidence, and whether the next step is safe to infer.
4. If status is stale, contradictory, or missing, perform the `project-status` repair behavior first: audit the project trail, update `docs/status.md` when project-doc edits are in scope, and report the recovery path.
5. Before dispatching into prototype, spec, plan, build, or release work, check whether the project trail answers what is being built, why it matters, and what good looks like. If those answers are missing and the user has not delegated judgment, ask 1-3 concise questions or route to `product-discovery`/`spec` as the next gate.
6. If the next step is clear and low-risk, load and follow that public skill's workflow before running the step:
   - Proposal gaps: use `product-discovery` or `spec`.
   - Prototype gaps: use `prototype`.
   - Build gaps: use `spec`, `plan`, `build`, `test`, `review`, or `code-simplify` as the next unfinished gate requires.
   - Release gaps: use `qa`, `review`, or `ship`.
   - GitHub handoff gaps: commit, push, draft PR, self-review, code-simplify, or ask before ready-for-review as the unfinished gate requires. Never run `gh pr ready` without explicit user authorization.
7. If multiple plausible next steps exist, ask one concise verification question instead of choosing arbitrarily.
8. If the user asks to skip missing prerequisites, warn once, name the skipped gate and risk, then proceed only when the user insists and no hard safety boundary applies.
9. End by naming the action taken, evidence used, status/docs updated or intentionally left unchanged, and the next expected gate.

## Verification

- The chosen next action cites project files, status, commits, tasks, tests, or plans.
- The response explains why this action is next instead of merely saying it was inferred.
- Ambiguous forks produce a concise question.
- Stale or missing status triggers repair behavior before continuation.
- Product-intent gaps around what, why, or what good looks like trigger concise questions or the appropriate double-back skill.
- Ready-for-review transitions require explicit user authorization.
- Skipped gates are recorded in the response and in `docs/status.md` when project-doc edits are in scope.

## Stop Conditions

- There is no accessible project trail and scaffolding or repair would be a separate user decision.
- Choosing among multiple active project slices would be arbitrary.
- The next action crosses a destructive, privacy-sensitive, credential, money, deployment, or external-message boundary without explicit approval.
