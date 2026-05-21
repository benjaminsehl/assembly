# Project Phases

Projects and substantial project slices move through four phases. A phase is not a ceremony; it is a confidence gate.

Projects can be nested. Use the same phase model for a whole repo, an app surface, an agent layer, a native client, or a single important feature. Keep the phase docs near the work they explain.

## 1. Proposal

Goal: align on why the project matters before optimizing how to build it.

Required evidence:

- What becomes 10x better as a result of the project.
- What good looks like at the end.
- Desired user, product, engineering, and business outcomes.
- Key assumptions.
- Principles that should guide trade-offs.
- Major risks and non-goals.
- Existing decisions or constraints that should not be removed casually.

Recommended skills:

- `new-project`
- `product-discovery`
- `founder-review`
- `business-model-review`
- `spec`

Exit gate: the user can judge future work against explicit outcomes, assumptions, principles, and success criteria.

## 2. Prototype

Goal: create tangible evidence before committing to full build direction.

Required evidence:

- The prototype question.
- The artifact the user can inspect, run, or feel.
- What changed in the direction because of the prototype.
- Decision: delete, continue, or absorb into build.

Recommended skills:

- `prototype`
- `design-plan-review`
- `founder-review`
- `business-model-review`
- `spec`

Exit gate: the prototype proves, changes, or rejects the direction clearly enough to plan production work.

## 3. Build

Goal: implement the approved direction in small, verifiable slices.

Required evidence:

- Approved spec and plan.
- Vertical slices with acceptance criteria.
- Tests and runtime checks.
- Updated tech design or decisions when needed.

Recommended skills:

- `plan`
- `build`
- `test`
- `review`
- `code-simplify`
- `health-check`

Exit gate: production behavior is implemented, verified, and ready for release QA and polish.

## 4. Release

Goal: ship or intentionally hold the work with product, engineering, and business evidence.

Required evidence:

- QA flows and bugs.
- Polish checklist.
- Go/no-go decision.
- Rollback path where relevant.
- Grade against proposal outcomes, principles, and "what good looks like."
- Follow-up work from discoveries.

Recommended skills:

- `qa`
- `review`
- `health-check`
- `ship`
- `retro`
- `learn`

Exit gate: the work has shipped or been held intentionally, the result is graded against the proposal, and future learning is captured.

## Status Output Shape

When asked what phase a project is in, answer with:

- Current phase.
- Evidence from files, commits, tests, plans, or notes.
- Missing required artifacts.
- Next decision gate.
- Next recommended skills.
- One concrete next action.

If this cannot be answered with confidence, recommend `introspect` for a deeper audit, `docs/status.md` repair, and recovery plan.
