# Roadmap: Hermes As Assembly Orchestrator

Last updated: 2026-05-27
Status: post-1.0 roadmap

## Thesis

Hermes should orchestrate Assembly after Assembly's agent control loop is stable.

The right shape is not a fully autonomous app factory. It is a General Manager that coordinates Codex sessions, project state, specialist reviews, and founder approval gates across a roadmap.

## Stage 0: Assembly 1.0

Goal: prove the local protocol.

Hermes dependency:

- Stable project scaffold.
- Reliable `next`.
- Clear phase gates.
- Evidence-backed status.
- GitHub handoff discipline.
- Ask-first approval boundaries.

## Stage 1: Hermes Contract Spike

Goal: define how Hermes reads and writes Assembly project state.

Deliverables:

- `docs/tech-design/hermes-assembly-contract.md`.
- Structured status fields or frontmatter proposal.
- Skill invocation contract.
- Work assignment shape.
- Evidence packet shape.
- Approval boundary model.

Questions:

- Does Hermes call Codex directly, or prepare prompts for a human-triggered Codex session?
- Which status fields must be machine-readable?
- How should Hermes detect stale or contradictory project state?
- How does Hermes avoid overwriting founder/product judgment?

## Stage 2: Hermes Orchestrator Alpha

Goal: Hermes can manage one roadmap for one repo.

Capabilities:

- Read Assembly status and plans.
- Recommend the next Codex session.
- Spawn or prepare one bounded Codex task at a time.
- Track whether the task produced evidence.
- Pause for founder questions when product judgment is missing.
- Escalate blocked PRs, checks, comments, or approvals.

Non-goals:

- No autonomous merge or deploy.
- No multi-repo scheduling.
- No background code rewriting.

## Stage 3: Specialist Coordination

Goal: Hermes can coordinate sidecar specialist work without losing ownership.

Capabilities:

- Assign one patch owner.
- Spawn review, QA, research, or context-engineering sidecars.
- Merge their reports into a single decision.
- Create follow-up tasks without bloating the active session.

Quality bar:

- Every specialist output must cite artifacts, commands, files, or PR state.
- Hermes must know when a specialist result is advisory versus blocking.

## Stage 4: App Factory Roadmap Execution

Goal: Hermes can help run a portfolio of projects without replacing the founder.

Capabilities:

- Maintain roadmap state.
- Suggest which project should move next.
- Track product bets and evidence.
- Keep decisions and lessons connected across projects.
- Schedule periodic health checks and retros.

Founder gates:

- Product direction.
- Scope tradeoffs.
- Pricing/business model.
- Release go/no-go.
- External communication.
- Money, credentials, privacy, destructive actions.

## Stage 5: Dream And Desloppification

Goal: background quality loops become safe and useful.

Constraints:

- Read-only analysis should be the default.
- Write work should happen on branches with PRs.
- Refactors should be tied to explicit code-health findings.
- No silent broad rewrites.
- Every proposed cleanup should explain why users or future agents benefit.

## First Next Step After 1.0

Run a one-week Hermes contract spike. Do not build the orchestrator until the contract makes approval boundaries, evidence packets, and project-state reads boringly clear.
