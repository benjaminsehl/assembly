---
name: ship
description: Use when deciding whether a change is ready to release; produces a go/no-go decision with blockers, risks, evidence, and rollback criteria.
---

# Ship

## Purpose

Decide whether a change is ready to release. A `GO` decision requires verification evidence and a rollback plan.

## Underlying skills

- `shipping-and-launch`
- `ci-cd-and-automation`
- `security-and-hardening`
- `performance-optimization`
- `documentation-and-adrs`
- `deprecation-and-migration`
- `code-review-and-quality`

## Workflow

1. State that the `ship` workflow is active and identify the release candidate.
2. Gather the diff, test/build/CI status, deployment path, feature flags, migrations, docs, and rollback mechanism.
3. Use `code-review-and-quality` to check current changes for launch blockers.
4. Use `security-and-hardening` and `performance-optimization` for release-relevant risk.
5. Use `ci-cd-and-automation`, `documentation-and-adrs`, `deprecation-and-migration`, and `shipping-and-launch` for rollout readiness.
6. If the user explicitly authorized subagents or parallel agent work, run specialist review in parallel and merge the reports. Otherwise perform the audit locally and say fan-out was not used.
7. Produce a single `GO` or `NO-GO` decision with blockers, recommended fixes, acknowledged risks, rollback triggers, rollback procedure, and evidence.

## Verification

- Test, build, CI, or manual verification status is named.
- Blockers are separated from recommended fixes.
- Rollback trigger conditions and procedure are present.
- Any accepted risk is explicit.

## Stop Conditions

- The rollback path is unknown for a production-bound change.
- Critical security, data-loss, migration, or compliance risk is unresolved.
- Required verification is unavailable and the user has not accepted the risk.

