# Spec: Assembly 1.0

Last updated: 2026-05-24
Status: draft for review

## Objective

Assembly 1.0 should be a reliable personal Codex product-building stack.

The core promise: install Assembly, scaffold or orient a repo, say `next`, and have Codex know the project phase, missing context, correct workflow, and next useful action from local evidence instead of guessing.

Assembly 1.0 is Codex-first. Claude compatibility is out of scope. Hermes orchestration is the next strategic horizon after the Codex workflow is stable.

## User

Primary user: Sai building real products with Codex.

Secondary user: a serious builder who wants a compact Codex-native project operating system without maintaining a pile of overlapping lifecycle skills.

## Product Principles

- Personal reliability beats broad marketplace polish.
- The public skill surface stays small.
- `next` should be the normal continuation command.
- Product judgment stays with the user unless explicitly delegated.
- Build work should move when the next engineering gate is evidence-backed.
- Every material workflow leaves evidence future agents can inspect.
- GitHub-backed work should end in a reviewable PR handoff by default.
- Workflow gates should prevent skipped thinking without becoming ceremony.
- Hermes orchestration should stay visible as the post-1.0 path, but must not delay 1.0.

## Scope

Assembly 1.0 includes:

- A Codex plugin named `assembly`.
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
  - `docs/prototypes/`
  - `docs/qa/`
  - `docs/release/`
  - `docs/projects/`
  - `reference/`
- Subproject scaffolding under `docs/projects/<slug>/`.
- A black composer icon and plugin metadata that render cleanly in Codex.
- Validation scripts for plugin shape, skill graph, local skill conflicts, and scaffold behavior.
- User docs for install, upgrade, migration from old lifecycle skills, and everyday workflow.
- GitHub handoff rules for draft PRs, review, simplification, ready-for-review, review comments, and merge gates.

## Out Of Scope

- Claude Code adapter generation.
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

## Success Criteria

Assembly 1.0 is ready when:

- A fresh Codex session can see and invoke `assembly:next`.
- `codex plugin marketplace add benjaminsehl/assembly` works for a new install.
- `codex plugin marketplace upgrade assembly` picks up the latest version.
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

- Install from the public marketplace root.
- Upgrade from an older installed version.
- Confirm the composer icon and plugin metadata are visible after refresh or new session.
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

## Open Questions

- Should 1.0 include an automated installer or migration helper, or are docs plus conflict audit enough?
- How much of dream/desloppification belongs in 1.0 references versus the Hermes orchestration roadmap?
- Is Hyper required for 1.0, or should it remain a stretch proof after CFO?
- What minimum smoke evidence should be captured in the release retro?
