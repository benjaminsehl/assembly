---
name: ship
description: Use when deciding whether a change is ready to release; produces a binary GO or NO-GO decision with blockers, risks, evidence, and rollback criteria.
---

# Ship

## Purpose

Decide whether a change is ready to release. The decision is binary: `GO` or `NO-GO`. A `GO` requires verification evidence and a rollback plan. Ship also owns GitHub conversation: it opens the PR (draft or ready, founder picks) for branches `build` has pushed.

## References

- `references/workflows/qa-and-release.md`: ship mode, health-check mode, rollout, rollback.
- `references/security-checklist.md`: release security checks.
- `references/performance-checklist.md`: release performance checks.
- `references/testing-patterns.md`: verification evidence.

## Workflow

1. State that the `ship` workflow is active and identify the release candidate. If multiple slices are shippable, present 2-3 candidates with evidence and ask the founder to pick. Use the explicit options-list pattern.
2. Gather the diff, test/build/CI status, deployment path, feature flags, migrations, docs, and rollback mechanism.
3. Fan out specialist auditors in parallel by default: correctness, security, performance, data, migration, docs. Merge reports.
4. Apply the migration gate, tiered by traffic state:
   - Pre-live (no production traffic, no real users): reckless migrations are acceptable — drop tables, rename columns, no reverse SQL needed. Name the risk and proceed.
   - Live traffic (real users, real data): blocker by default. Require forward + reverse SQL, staging dry-run, locking analysis under concurrent writes, backfill plan, and a named owner who will watch the rollout. Missing any → NO-GO.
5. If no PR exists for the topic branch, open it now. Ask the founder whether to open as draft or ready. PR description uses product-impact framing: what user capability ships, not what files changed.
6. If a draft PR exists and the founder requests promotion to ready: confirm review is complete, simplification pass is done, verification is green, and the founder has explicitly authorized the ready transition.
7. Produce a single binary decision:
   - `GO`: verification green, blockers cleared, rollback trigger and procedure named, residual risks acknowledged, product-impact statement included.
   - `NO-GO`: blockers listed, recommended fixes named, next path to GO stated.
8. Do not run retro. Ship is pre-release only.

## Verification

- Decision is binary: `GO` or `NO-GO` — no tiers, no "soft go."
- Test, build, CI, or manual verification status is named.
- Specialist fan-out is named; skipped specialists are justified.
- Migration gate is applied with explicit traffic-state classification.
- Blockers are separated from recommended fixes.
- Rollback trigger conditions and procedure are present for live-traffic releases.
- PR state is named; draft PRs are marked ready only with explicit founder authorization.
- PR description uses product-impact framing (what ships for users, not what code changed).
- Any accepted risk is explicit.

## Stop Conditions

- The rollback path is unknown for a live-traffic change.
- Critical security, data-loss, migration, or compliance risk is unresolved.
- Required verification is unavailable and the founder has not accepted the risk.
- A live-traffic migration is missing forward/reverse SQL, staging dry-run, locking analysis, backfill plan, or named owner.
- Multiple shippable slices exist and choosing among them would be arbitrary.
