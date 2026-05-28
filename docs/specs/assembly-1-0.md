# Spec: Assembly 1.0

Last updated: 2026-05-27
Status: draft for review

## Objective

Assembly is the per-project operating system for human-led, agent-executed product building.

In 1.0, it proves the human-led control loop in both Codex and Claude Code: read the project trail, identify phase and missing context, clarify what is being built, why it matters, and what good looks like, choose the next safe workflow, and leave evidence-backed handoff.

The user remains founder and product director. Agents help clarify intent in product-implication language (not engineering detail), preserve reasoning, and execute scoped work; they do not silently take product authority, and they flag business, user, and viability concerns rather than deciding them.

Assembly 1.0 ships as a dual-runtime plugin: the same bundle installs and runs in both Codex and Claude Code, and must pass install and behavior smoke checks in both. Other agent runtimes (Pi, OpenCode, etc.) may be added later but stay out of 1.0 scope. A post-1.0 orchestrator is the strategic horizon after the agent control loop is stable.

## User

Primary user: Ben acting as founder/product director, using agents in Codex and Claude Code to shape, specify, build, test, and ship real products while retaining product judgment.

Assembly is built in public. Other builders who want a coherent agentic product-building lifecycle are free to adopt it, but they are not the audience 1.0 is designed around.

## Product Principles

- Personal reliability beats broad marketplace polish.
- The public skill surface stays small.
- The skill surface and skill-behavior contracts are means to high agent execution quality, not ends in themselves. Revise the surface, the spine, or the defaults when evidence shows a different shape produces better-quality agent output, better context engineering, or better subagent delegation.
- `next` should be the normal continuation command.
- Human judgment leads; agents accelerate, clarify, and preserve it.
- Product judgment stays with the user unless explicitly delegated.
- Agents ask in product-implication language, never in engineering-implementation detail when a product framing is possible.
- Agents flag business, user, and viability concerns for founder judgment; they do not decide them.
- Agents should ask enough questions to understand what is being built, why it matters, and what good looks like before making durable product or implementation choices.
- Build work should move when the next engineering gate is evidence-backed.
- Every material workflow leaves evidence future agents can inspect, so vision coherence stays high across multiple sessions and multiple agents.
- GitHub-backed work should end in a reviewable PR handoff by default.
- Workflow gates should prevent skipped thinking without becoming ceremony.
- 1.0 proves the agent control loop before post-1.0 orchestration.

## Scope

Assembly 1.0 includes:

- A dual-runtime plugin named `assembly` that installs and runs in both Codex and Claude Code from the same bundle at `plugins/assembly/`.
- A small public skill surface, sized for high agent execution quality. The 1.0 candidate set is these 12 skills, subject to revision based on quality evidence:
  - `next`
  - `project-status`
  - `product-discovery`
  - `prototype`
  - `spec`
  - `plan`
  - `build`
  - `test`
  - `qa`
  - `review`
  - `code-simplify`
  - `ship`
- A root project scaffold with:
  - `AGENTS.md`
  - `.agents/AGENT-GUIDANCE.md`
  - `.agents/log.md`
  - `.agents/notes/`
  - `docs/`
  - `docs/status.md`
  - `docs/phases/`
  - `docs/product/`
  - `docs/decisions/`
  - `docs/specs/`
  - `docs/plans/`
  - `docs/tech-design/`
  - `docs/research/`
  - `docs/prototypes/`
  - `docs/qa/`
  - `docs/release/`
  - `docs/projects/`
  - `reference/`
- Subproject scaffolding under `docs/projects/<slug>/`.
- A black composer icon and plugin metadata that render cleanly in both Codex and Claude Code.
- Validation scripts for plugin shape, skill graph, local skill conflicts, and scaffold behavior.
- User docs for install, upgrade, migration from old lifecycle skills, and everyday workflow.
- GitHub handoff rules for draft PRs, review, simplification, ready-for-review, review comments, and merge gates.

## Out Of Scope

- Runtimes other than Codex and Claude Code.
- Post-1.0 orchestrator implementation.
- Hosted dashboard, app-factory UI, or background automation.

## Gating Model

Assembly's gating is product-direction-first. Once the product gates are clear and verification is green, engineering execution proceeds without per-action approval up to (and including) pushing the topic branch. PR opening, ready promotion, merge, and deploy are ship-owned and always ask before proceeding. The founder's time stays on direction and on the ship gate.

### Product gates (must be clear before the rails open)

Before agents proceed past discovery into build or release work, the project trail must answer:

- What is being built.
- Why it matters.
- What good looks like.
- Risks and non-goals.
- Rollback or hold criteria (for any change that touches production behavior).

When any of these is missing, agents ask in product-implication language and pause work until the trail answers.

### Engineering rails (proceed without per-action approval once product gates pass)

Once product gates are clear and verification is green, `build` may:

- Commit and push focused changes on a topic branch.
- Run self-review and code simplification.

### Ship gate (always asks)

Regardless of product-gate clarity, `ship` asks before:

- Opening a PR (draft or ready, founder picks).
- Marking a draft PR ready-for-review.
- Merging the PR.
- Running the project's deploy path.
- Deleting merged branches.

### Always-ask floor (regardless of product-gate clarity)

These actions require explicit founder approval even when product gates are clear:

- Money movement, purchases, trades, account changes.
- Credentials, secrets, or privacy-sensitive data.
- External messaging (Slack, email, social, customer-facing).
- Irreversible destructive operations: force-push to default branches, delete branches with unmerged work, drop tables or databases, delete production data.
- Merging or deploying when verification is not green, review threads are unresolved with material correctness concerns, or product gates are not clear.

## Behavior Requirements

### `next`

`next` must:

- Read `AGENTS.md`, `docs/status.md`, nearest subproject status, `.agents/log.md`, and referenced specs/plans when present.
- Identify the active phase: proposal, prototype, build, or release.
- Repair stale or missing status before proceeding when project-doc edits are in scope.
- Check whether the project trail answers the product gates (what / why / what good looks like / risks / rollback) before dispatching into planning, building, or release work.
- Ask the smallest useful set of concise questions in product-implication language when product gates are missing, keeping continuation lightweight instead of turning it into a survey.
- Choose the next unambiguous action from evidence.
- Ask one concise question when multiple plausible next actions exist.
- Dispatch to the right public skill instead of doing vague continuation work.
- Honor the always-ask floor regardless of product-gate clarity.

### `project-status`

`project-status` must:

- Scaffold new projects and subprojects without overwriting existing `AGENTS.md`.
- Preserve existing `.agents/AGENT-GUIDANCE.md`, `.agents/notes/README.md`, and `reference/README.md` under force scaffolding.
- Append to `.agents/log.md` instead of rewriting history.
- Diagnose current phase, missing prerequisites, skipped gates, and next recommended skills.
- Update `docs/status.md` when repair is in scope.

### `product-discovery`

`product-discovery` must:

- Default to interview mode.
- Treat the user as founder/product director, not a requirements oracle.
- Clarify what, why, and what good looks like before recommending wedge, scope, or success criteria.
- Ask high-leverage questions in product-implication language before making product calls when the idea is raw or fuzzy.
- Flag business, user, and viability concerns; do not decide them.
- Use delegated mode only when the user explicitly asks the agent to decide, asks for recommendations, or project evidence is already strong.
- Label assumptions clearly in delegated mode.
- Cover user, painful moment, current workaround, urgency, desired outcome, wedge, constraints, distribution, success evidence, risks, and next skill.

### `build`

`build` must:

- Treat empty or minimal prompts such as `Use build` as permission to infer the first unambiguous build-track gate from project evidence.
- Default to the engineering spine when no task is named: spec repair, plan, implementation, test, review, code-simplify, GitHub handoff.
- Vary from the default spine when project evidence and agent quality outcomes warrant a shorter or reordered shape (e.g., spec and plan already exist and are sufficient — jump to implementation).
- Ask before inventing missing product or design decisions; questions are in product-implication language, not engineering detail.
- Keep moving when the missing step is mechanical and recoverable from existing docs.
- Implement one slice at a time.
- Delegate to specialized subagents when the work shape calls for it.
- Run targeted verification and the broadest practical regression check.

### GitHub Handoff

For material changes in a GitHub-backed repo, Assembly must:

- Inspect branch, remote, status, and existing PR state before committing.
- Commit focused changes on a topic branch.
- Push the branch.
- Open or update a descriptive draft PR.
- Explain why the PR exists, the first principles behind the change, how the agent approached it, what changed, verification, risks, and follow-up.
- Run self-review.
- Run code simplification when reasonable.
- Always ask before marking the PR ready-for-review. Promote to ready only with explicit founder authorization, with product gates clear (what / why / what good looks like / risks / rollback), verification green, review/simplification complete, and no always-ask floor item triggered.
- Always ask before merging. Confirm product gates, verification, and review-thread/check state before requesting merge authorization.
- Always ask before deploying. Confirm rollback criteria and post-merge verification before requesting deploy authorization.
- Honor the always-ask floor on top: money, credentials, external messaging, irreversible destructive ops.

Before any merge or deploy proceeds, Assembly must:

- Check PR state, status checks, review decision, and unresolved review threads.
- Address actionable unresolved comments or report why they are not actionable.
- Block the action when there are failing checks, requested changes, unresolved blockers, or unresolved comments that materially affect correctness.
- If the founder explicitly accepts a risk, name the unresolved risk before proceeding.

## Project Phase Requirements

### Proposal

Required evidence:

- What becomes 10x better.
- What good looks like.
- Desired outcomes.
- Assumptions.
- Principles.
- Risks and non-goals.
- Decision records for durable choices.

Exit gate: the user can judge future work against explicit outcomes and principles.

### Prototype

Required evidence:

- Prototype question.
- Inspectable artifact.
- Success criteria.
- Decision: delete, continue, or absorb into build.

Exit gate: the prototype proves, changes, or rejects the direction clearly enough to plan production work.

### Build

Required evidence:

- Approved spec.
- Implementation plan.
- Acceptance criteria.
- Verification path.
- Updated decisions or tech design when needed.

Exit gate: production behavior is implemented, verified, reviewed, simplified where useful, and ready for release QA.

### Release

Required evidence:

- QA scope.
- Ship criteria.
- Rollback or hold criteria.
- PR readiness.
- Grade against proposal outcomes and principles.
- Follow-up work.

Exit gate: the work has shipped or been held intentionally, and learning is captured.

## 1.0 Proof Projects

Required:

- Assembly self-hosts its own workflow from proposal through release.
- CFO proves a greenfield or restart project setup.

Stretch:

- Hyper proves retrofit behavior against a high-context existing app.

## 1.0 Release Blockers

Assembly 1.0 must not ship until:

- A fresh Codex session can see and invoke `assembly:next`.
- A fresh Claude Code session can see and invoke `assembly:next` after `/plugin install assembly@assembly`.
- `codex plugin marketplace add benjaminsehl/assembly` works for a new install.
- `codex plugin marketplace upgrade assembly` picks up the latest version.
- `/plugin marketplace add benjaminsehl/assembly` followed by `/plugin install assembly@assembly` works for a new Claude Code install.
- `/plugin marketplace update assembly` picks up the latest version in Claude Code.
- The plugin exposes only the candidate public skill surface (currently 12 skills); any drift from that set is intentional and recorded.
- `next` is reliable enough to use as the default continuation command.
- `project-status` can scaffold and repair a project trail without overwriting existing instructions.
- `product-discovery` asks before deciding unless decisions are delegated.
- `build` with an empty prompt infers and executes the next unambiguous build-track gate.
- Material GitHub-backed work produces a descriptive draft PR.
- The gating model is implemented: product gates open the engineering rails up through push; the ship gate always asks before opening PRs, promoting to ready, merging, or deploying; the always-ask floor (money, credentials, external messaging, irreversible destructive ops) is honored regardless of product-gate clarity.
- Install, migration, conflict, and troubleshooting docs are accurate enough for a cold user.
- The release has smoke-test evidence and a short retro.

## Proof Evidence

Required:

- Assembly self-hosts this spec, release plan, QA evidence, and retro through its own project trail.
- CFO proves greenfield/restart setup, including scaffold, status, `next`, and a reviewable handoff.

Stretch:

- Hyper proves retrofit behavior against a high-context existing app. Hyper increases confidence, but it should not block 1.0 if Assembly and CFO prove the control loop.

## Deferred Aspirations

- Post-1.0 orchestration.
- Hosted dashboards or app-factory UI.
- Background automation, dream/desloppification loops, and multi-project scheduling.
- Broad runtime portability beyond Codex and Claude Code.
- Telemetry: no near-term plans, but not permanently excluded; revisit when there is a quality reason to add it, with explicit founder consent.
- Absorbing platform-plugin behavior (GitHub, Browser, Cloudflare, iOS, macOS, frontend builders) into Assembly skills: 1.0 composes specialized plugins where they're effective; the boundary may evolve later based on whether those plugins stay current and reliable.
- Automatic merges, deploys, branch deletion, or release automation. With the locked decisions, `ship` always asks before opening PRs or promoting to ready; auto-merge and auto-deploy are not in scope for 1.0.

## Verification Plan

Run from repo root:

```bash
python3 plugins/assembly/scripts/validate_plugin.py
python3 plugins/assembly/scripts/validate_skill_graph.py
python3 plugins/assembly/scripts/audit_skill_conflicts.py
python3 -m py_compile plugins/assembly/scripts/validate_plugin.py plugins/assembly/scripts/validate_skill_graph.py plugins/assembly/scripts/scaffold_project.py plugins/assembly/scripts/audit_skill_conflicts.py
git diff --check
```

Scaffold smoke tests:

- Root project scaffold creates the expected `docs/`, `.agents/`, and `reference/` shape.
- Subproject scaffold creates nested project docs under `docs/projects/<slug>/`.
- Existing `AGENTS.md` is skipped and reported.
- Force scaffolding preserves protected guidance files and appends to `.agents/log.md`.

Behavior smoke prompts:

- `Use next to do the next normal thing.`
- `Use project-status to tell me what phase this project is in.`
- `Use product-discovery on this idea.`
- `Use product-discovery and make the calls for this idea.`
- `Use build.`
- `Use build, then push this up.`
- `Use build to address unresolved PR review comments on PR #1.`
- `Use qa on this local app.`
- `Use ship to decide whether this is ready.`

Install smoke tests:

- Install from the public marketplace root in Codex.
- Install from the public marketplace in Claude Code via `/plugin marketplace add` and `/plugin install`.
- Upgrade from an older installed version in both runtimes.
- Confirm the composer icon and plugin metadata are visible after refresh or new session in both runtimes.
- Confirm old conflicting lifecycle skills are reported by the conflict audit.

## Boundaries

Always:

- Prefer repo conventions over generic workflow.
- Keep entry skills thin and references deep.
- Preserve a local paper trail.
- Use the runtime's GitHub tooling for PR metadata, comments, checks, and PR handoff.
- Report verification evidence.

Ask first (the always-ask floor; applies regardless of product-gate clarity):

- Before money movement, purchases, trades, or account changes.
- Before credential or privacy-sensitive work.
- Before external messaging (Slack, email, social, customer-facing).
- Before irreversible destructive operations: force-push to default branches, delete branches with unmerged work, drop tables or databases, delete production data.
- Before merging, deploying, or marking ready when product gates are not clear, verification is not green, or review threads have material unresolved correctness concerns.
- Before skipping a missing product gate when risk materially changes.

Never:

- Proceed past product gates with material gaps unfilled, except when the founder explicitly accepts a named risk.
- Merge or deploy with unresolved requested changes or material unresolved review comments unless the founder explicitly accepts the risk.
- Overwrite existing project instructions during scaffold.
- Hide product assumptions behind confident recommendations.
- Leave material GitHub-backed work as only a local diff unless local-only was requested or handoff is blocked.
- Call 1.0 ready without real-project evidence.

## Resolved 1.0 Decisions

- Automated installer or migration helper: not required for 1.0. Docs plus conflict audit are enough if the cold install/upgrade smoke tests pass.
- Dream/desloppification: defer to the post-1.0 orchestrator / app-factory roadmap. 1.0 may keep the concept visible only as future reference material.
- Hyper proof: stretch, not required. CFO is the required external proof project after Assembly self-hosting.
- Minimum release evidence: validator outputs, scaffold smoke results, behavior prompt notes, install/upgrade proof, GitHub handoff proof, and a short retro naming what worked, what felt brittle, and what the post-1.0 orchestrator should own next.
