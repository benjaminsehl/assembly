# Decision: Autonomy and Escalation Model

Date: 2026-05-29

## Context

Assembly's earlier gating model was phase-and-ceremony based. The "ship gate" always asked the founder before opening even a draft PR, before promoting to ready, before merging, and before deploying — regardless of whether any product or UX question was actually at stake. In practice this interrupted the founder for engineering bookkeeping ("should I push a draft PR?") that the agent is better positioned to decide, while not cleanly guaranteeing that genuine product/UX decisions came back to the founder in terms a product director cares about.

The founder's stated intent: be in the loop for product and UX — always, framed in user-facing terms — and otherwise let the agent run autonomously, validating its own engineering with reviewer sub-agents. Pre-launch, the agent should be able to execute an entire roadmap end to end (multiple PRs, merges, deploys) when nothing is up for product/UX debate. Once there is live traffic, the founder wants back into the shipping loop.

## Decision

Escalation turns on two axes, not on phase ceremony.

### Axis 1 — Decision type (applies in every traffic state)

- Product and UX decisions always escalate to the founder, framed in product-implication language — user scenarios and experience/business tradeoffs, never engineering-implementation detail. An open product/UX decision pauses autonomous progress until the founder answers. Includes: what gets built and why, user-facing behavior, copy, flow, visual-design tradeoffs, scope cuts that change the experience, naming, positioning, pricing, and business model.
- Engineering decisions are the agent's to make and run autonomously. Quality is assured by reviewer sub-agents (`code-reviewer`, `security-auditor`, `test-engineer` personas fanned out in parallel) rather than founder approval. The founder is the product director, not the per-PR reviewer. Includes: architecture, libraries, file/module layout, test strategy, refactors, commit/branch hygiene, opening a PR and choosing draft vs ready, promoting to ready, and merging engineering-only changes.

### Axis 2 — Traffic state (founder-declared, default `pre-live`)

`docs/status.md` carries a `Traffic state:` field. Only the founder sets it; the agent never silently flips it. Absent or unknown means `pre-live`.

- `pre-live`: with no open product/UX decision and no always-ask floor item, the agent runs the whole roadmap autonomously — open PRs, run reviewer sub-agents, merge to the default branch, and deploy — across as many PRs as the roadmap needs, with no per-action approval.
- `live`: opening, reviewing, and readying PRs stay autonomous. Merging to the default branch becomes a founder GO/NO-GO; the agent prepares the decision (verification, residual risk, rollback) so the founder answers one product-impact question. Deploy follows the approved merge.

### Always-ask floor (any traffic state)

Money movement, credential/secret use, external messaging on the founder's behalf, privacy-sensitive data, irreversible destructive operations (force-push to default branch, deleting branches with unmerged work, dropping tables, deleting production data), merging to the default branch when `live`, and anything the target repo's local protocol marks ask-first.

## Founder Inputs

This model encodes three founder choices made on 2026-05-29:

1. Traffic state is founder-declared in `docs/status.md` (the agent does not infer or auto-flip it).
2. Pre-launch autonomy includes deploy, not just merge.
3. Under live traffic, the founder re-enters at the merge-to-default-branch gate; deploy follows the approved merge. (This refines the initial "re-enter only at deploy" answer: because a project may auto-deploy on merge, merge is the point where a change becomes part of the live product, so the live gate sits at merge. A release branch may later move the gate again; until a project adopts one, merge to the default branch is the live gate.)

## Why This Extends Rather Than Reverses

The prior model already had the right primitives — traffic-state tiering (in the migration gate), specialist reviewer fan-out, and a "ask in product-implication language" principle. This decision re-centers the model on those primitives instead of on PR-ceremony approvals. The safety floor is preserved in full; what changes is that engineering handoff (draft/ready, plus merge and deploy when `pre-live`) is no longer a founder interruption, and the live gate sits at merge to the default branch.

## Implications

- `ship` opens PRs, decides draft vs ready, runs reviewer sub-agents, merges, and deploys autonomously — asking the founder only at the live-traffic merge gate (deploy follows the approved merge).
- Reviewer sub-agents are the validation that previously came from founder PR review.
- Scaffolded projects start `pre-live` and carry the `Traffic state:` field in `docs/status.md`.
- The post-1.0 orchestrator inherits this traffic-state model: its "no autonomous merge/deploy" non-goal is scoped to live traffic, not pre-live.
- Validation asserts the new model's invariants (traffic state, product/UX escalation, reviewer sub-agents, always-ask floor) instead of the old always-ask-before-ready strings.

## Out of Scope

- Automatic detection of the pre-live to live transition.
- Removing or weakening the always-ask safety floor.
- Founder involvement in routine engineering decisions.
