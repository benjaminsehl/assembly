---
name: ship
description: Use when deciding whether a change is ready to release; produces a go/no-go decision with blockers, risks, evidence, and rollback criteria.
---

# Ship

## Purpose

Decide whether a change is ready to release. A `GO` decision requires verification evidence and a rollback plan.

## References

- `references/workflows/qa-and-release.md`: ship mode, health-check mode, rollout, rollback, retro, and learning capture.
- `references/security-checklist.md`: release security checks.
- `references/performance-checklist.md`: release performance checks.
- `references/testing-patterns.md`: verification evidence.

## Workflow

1. State that the `ship` workflow is active and identify the release candidate.
2. Gather the diff, test/build/CI status, deployment path, feature flags, migrations, docs, and rollback mechanism.
3. Check current changes for launch blockers across correctness, security, performance, data, migration, and docs.
4. Use health-check mode from `references/workflows/qa-and-release.md` only for broad periodic readiness, not ordinary diff review.
5. If the user explicitly authorized subagents or parallel agent work, run specialist review in parallel and merge the reports. Otherwise perform the audit locally and say fan-out was not used.
6. Produce a single `GO` or `NO-GO` decision with blockers, recommended fixes, acknowledged risks, rollback triggers, rollback procedure, evidence, and post-release learning capture.

## Verification

- Test, build, CI, or manual verification status is named.
- Blockers are separated from recommended fixes.
- Rollback trigger conditions and procedure are present.
- Any accepted risk is explicit.

## Stop Conditions

- The rollback path is unknown for a production-bound change.
- Critical security, data-loss, migration, or compliance risk is unresolved.
- Required verification is unavailable and the user has not accepted the risk.
