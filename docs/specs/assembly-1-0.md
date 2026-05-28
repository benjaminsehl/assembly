# Spec: Assembly 1.0

Last updated: 2026-05-27
Status: draft for review

## Objective

Assembly is a human-led toolkit for an agentic app factory.

In 1.0, it proves the human-led control loop in both Codex and Claude Code: read the project trail, identify phase and missing context, clarify what is being built, why it matters, and what good looks like, choose the next safe workflow, and leave evidence-backed handoff.

The user remains founder and product director. Agents help clarify intent, preserve reasoning, and execute scoped work; they do not silently take product authority.

Assembly 1.0 ships as a dual-runtime plugin: the same bundle installs and runs in both Codex and Claude Code, and must pass install and behavior smoke checks in both. Broader runtime portability stays out of scope. Hermes orchestration is the post-1.0 strategic horizon after the dual-runtime control loop is stable.

## User

Primary user: Sai acting as founder/product director, using Codex or Claude Code to shape, specify, build, test, and ship real products while retaining product judgment.

Secondary user: a serious builder who wants a compact, runtime-agnostic project operating system without maintaining a pile of overlapping lifecycle skills.

## Product Principles

- Personal reliability beats broad marketplace polish.
- The public skill surface stays small.
- `next` should be the normal continuation command.
- Human judgment leads; agents accelerate, clarify, and preserve it.
- Product judgment stays with the user unless explicitly delegated.
- Agents should ask enough questions to understand what is being built, why it matters, and what good looks like before making durable product or implementation choices.
- Build work should move when the next engineering gate is evidence-backed.
- Every material workflow leaves evidence future agents can inspect.
- GitHub-backed work should end in a reviewable PR handoff by default.
- Workflow gates should prevent skipped thinking without becoming ceremony.
- 1.0 proves the dual-runtime control loop before Hermes orchestration.

## Scope

Assembly 1.0 includes:

- A dual-runtime plugin named `assembly` that installs and runs in both Codex and Claude Code from the same bundle at `plugins/assembly/`.
- Exactly 12 public skills:
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
- Hermes orchestration implementation.
- Hosted dashboard, app-factory UI, or background automation.
- Deployment automation.
- Telemetry.
- Automatic branch deletion.
- Automatic merging without explicit user direction.
- Replacing specialized platform plugins such as GitHub, Browser, Cloudflare, iOS, macOS, or frontend builders.

## Behavior Requirements

### `next`

`next` must:

- Read `AGENTS.md`, `docs/status.md`, nearest subproject status, `.agents/log.md`, and referenced specs/plans when present.
- Identify the active phase: proposal, prototype, build, or release.
- Repair stale or missing status before proceeding when project-doc edits are in scope.
- Check whether the project trail answers what is being built, why it matters, and what good looks like before dispatching into planning or building.
- Ask the smallest useful set of concise questions when those answers are missing, keeping continuation lightweight instead of turning it into a survey.
- Choose the next unambiguous action from evidence.
- Ask one concise question when multiple plausible next actions exist.
- Dispatch to the right public skill instead of doing vague continuation work.
- Treat GitHub merge, deploy, destructive operations, credentials, external messaging, money movement, and privacy-sensitive work as explicit approval boundaries.

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
- Ask high-leverage questions before making product calls when the idea is raw or fuzzy.
- Use delegated mode only when the user explicitly asks the agent to decide, asks for recommendations, or project evidence is already strong.
- Label assumptions clearly in delegated mode.
- Cover user, painful moment, current workaround, urgency, desired outcome, wedge, constraints, distribution, success evidence, risks, and next skill.

### `build`

`build` must:

- Treat empty or minimal prompts such as `Use build` as permission to infer the first unambiguous build-track gate from project evidence.
- Follow the engineering spine when no task is named: spec repair, plan, implementation, test, review, code-simplify, GitHub handoff.
- Ask before inventing missing product or design decisions.
- Keep moving when the missing step is mechanical and recoverable from existing docs.
- Implement one slice at a time.
- Run targeted verification and the broadest practical regression check.

### GitHub Handoff

For material changes in a GitHub-backed repo, Assembly must:

- Inspect branch, remote, status, and existing PR state before committing.
- Commit focused changes on a topic branch.
- Push the branch.
- Open or update a descriptive draft PR with `gh`.
- Explain why the PR exists, the first principles behind the change, how the agent approached it, what changed, verification, risks, and follow-up.
- Run self-review.
- Run code simplification when reasonable.
- Keep the PR draft until verification, self-review, and simplification are complete.
- Ask before marking a draft PR ready.
- Run `gh pr ready` only after explicit user authorization.

Before merge, Assembly must:

- Check PR state, status checks, review decision, and unresolved review threads.
- Address actionable unresolved comments or report why they are not actionable.
- Keep the PR unmerged when there are failing checks, requested changes, unresolved blockers, or unresolved comments that materially affect correctness.
- Merge only after explicit user direction.
- If the user still asks to merge with accepted risk, name the unresolved risk before merging.

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
- The plugin exposes only the 12 intended public skills.
- `next` is reliable enough to use as the default continuation command.
- `project-status` can scaffold and repair a project trail without overwriting existing instructions.
- `product-discovery` asks before deciding unless decisions are delegated.
- `build` with an empty prompt infers and executes the next unambiguous build-track gate.
- Material GitHub-backed work produces a descriptive draft PR.
- Ready-for-review requires explicit user authorization.
- Merge requires explicit user direction and a clean review-thread/check state or acknowledged risk.
- Install, migration, conflict, and troubleshooting docs are accurate enough for a cold user.
- The release has smoke-test evidence and a short retro.

## Proof Evidence

Required:

- Assembly self-hosts this spec, release plan, QA evidence, and retro through its own project trail.
- CFO proves greenfield/restart setup, including scaffold, status, `next`, and a reviewable handoff.

Stretch:

- Hyper proves retrofit behavior against a high-context existing app. Hyper increases confidence, but it should not block 1.0 if Assembly and CFO prove the control loop.

## Deferred Aspirations

- Hermes orchestration.
- Hosted dashboards or app-factory UI.
- Background automation, dream/desloppification loops, and multi-project scheduling.
- Broad runtime portability beyond Codex and Claude Code.
- Automatic merges, deploys, branch deletion, or release automation.

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
- Use `gh` for GitHub PR metadata, comments, checks, and PR handoff.
- Report verification evidence.

Ask first:

- Before merging PRs.
- Before marking draft PRs ready.
- Before deploys.
- Before destructive operations.
- Before credential or privacy-sensitive work.
- Before external messaging, purchases, trades, money movement, or account changes.
- Before skipping missing product or release gates when risk materially changes.

Never:

- Merge with unresolved requested changes or material unresolved review comments unless the user explicitly accepts the risk.
- Overwrite existing project instructions during scaffold.
- Hide product assumptions behind confident recommendations.
- Leave material GitHub-backed work as only a local diff unless local-only was requested or handoff is blocked.
- Call 1.0 ready without real-project evidence.

## Resolved 1.0 Decisions

- Automated installer or migration helper: not required for 1.0. Docs plus conflict audit are enough if the cold install/upgrade smoke tests pass.
- Dream/desloppification: defer to the Hermes/app-factory roadmap. 1.0 may keep the concept visible only as future reference material.
- Hyper proof: stretch, not required. CFO is the required external proof project after Assembly self-hosting.
- Minimum release evidence: validator outputs, scaffold smoke results, behavior prompt notes, install/upgrade proof, GitHub handoff proof, and a short retro naming what worked, what felt brittle, and what Hermes should own next.
