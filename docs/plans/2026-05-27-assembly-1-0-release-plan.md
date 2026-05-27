# Plan: Assembly 1.0 Release

Last updated: 2026-05-27
Status: draft

## Goal

Release Assembly 1.0 as a reliable Codex-first project operating system for a human-led agentic app factory.

## Release Principle

1.0 should feel small, solid, and useful. It should not pretend to be Hermes yet.

## Milestones

### 1. Spec Gate

Outcome: the 1.0 behavior spec and north-star vision are coherent enough for implementation and proof.

Tasks:

- Align `docs/specs/assembly-1-0.md` with the human-led app factory vision.
- Add app-factory north-star and research synthesis docs.
- Define what is blocking for 1.0 versus deferred to Hermes.
- Update `docs/status.md` with the current gate and next skills.

Exit evidence:

- Spec names release blockers.
- Roadmap separates 1.0 from post-1.0.
- Status points to the right next action.

### 2. Codex Control Loop Release Candidate

Outcome: the plugin behavior matches the 1.0 spec.

Tasks:

- Verify `next` uses project status, phase gates, and clarification behavior.
- Verify `product-discovery` interviews by default.
- Verify minimal `build` prompts infer the next build-track gate.
- Verify GitHub handoff creates or updates descriptive draft PRs.
- Verify ready-for-review, merge, deploy, and privacy-sensitive actions remain ask-first boundaries.

Exit evidence:

- Validator output.
- Smoke prompt notes.
- One PR handoff using Assembly's own flow.

### 3. Assembly Self-Host Proof

Outcome: Assembly's own repo demonstrates the workflow from proposal through release.

Tasks:

- Use this branch as the spec/proposal proof.
- Turn accepted spec into implementation tasks.
- Run validators and smoke checks.
- Open or update a descriptive draft PR.
- Run self-review and code simplification where useful.
- Capture QA and release evidence.
- Capture a short retro after merge.

Exit evidence:

- PR includes why, principles, approach, verification, risks, and follow-up.
- `docs/qa/assembly-1-0-smoke-evidence.md` records actual checks.
- `docs/release/assembly-1-0-checklist.md` reaches a clear go/no-go.

### 4. CFO External Proof

Outcome: a real restart/greenfield project can use the scaffold and continuation loop.

Tasks:

- Run project-status/scaffold against `/Users/sai/cfo` only with explicit local scope.
- Confirm scaffold preserves any existing instructions.
- Update CFO status with phase and next gate.
- Run a minimal `next` or `project-status` continuation check.
- Record proof in `docs/projects/cfo-proof/status.md`.

Exit evidence:

- CFO proof status records what was tested and what was intentionally not changed.
- Any private finance data remains unstaged and unprinted.

### 5. Release

Outcome: Assembly 1.0 is public, installable, and locally upgraded.

Tasks:

- Confirm install and upgrade commands.
- Confirm active skill list exposes only the intended 12 public skills.
- Confirm composer icon and metadata render.
- Merge the release PR after explicit approval.
- Upgrade the local plugin.
- Record release retro.

Exit evidence:

- Tag or version bump.
- Local plugin cache shows the released version.
- Release checklist is complete or explicitly held.

## Deferred Until After 1.0

- Hermes orchestration implementation.
- Dream/desloppification automation.
- Hosted dashboard.
- Claude adapter.
- Automatic deploy/merge/branch cleanup.
- Background roadmap execution.

## Current Next Step

Finish the spec gate, then use `plan` to break the release candidate work into concrete implementation tasks.
