---
name: test
description: Use when proving behavior, adding tests, reproducing bugs, or verifying browser/runtime behavior with evidence.
---

# Test

## Purpose

Turn expected behavior or a bug report into proof: failing tests first when possible, then passing tests and runtime evidence. Coverage scales with criticality.

## References

- `references/workflows/engineering-delivery.md`: test mode, Prove-It pattern, and debugging.
- `references/testing-patterns.md`: test levels and scenario coverage.
- `references/qa-checklist.md`: user-flow QA scenarios.

## Workflow

1. State that the `test` workflow is active and identify the behavior or bug under test.
2. Read the existing test framework, commands, and nearby test style.
3. Classify criticality and set the coverage tier:
   - Critical path (money movement, auth, data integrity, irreversible operations): full coverage — unit + integration + scenario tests; characterization tests for adjacent legacy paths.
   - Standard feature (user-visible behavior, non-critical flows): targeted unit + one integration test for the happy path and one for the worst plausible failure.
   - Internal/utility (helpers, refactors of pure functions): targeted unit tests only.
4. Before modifying tested legacy code, write characterization tests that lock current behavior. Required for any change inside critical-path or standard-feature code.
5. For new behavior, write tests that describe the expected outcome before implementation.
6. For bugs, use the Prove-It pattern: reproduce the bug with a failing test before fixing.
7. For browser or UI behavior, use available browser tooling for real runtime evidence.
8. If reproduction or verification fails unexpectedly, isolate the cause before changing the code.
9. Run targeted tests first, then broader regression checks when practical.

## Verification

- Coverage tier is named with reasoning.
- Characterization tests exist before touching tested legacy code.
- The failing condition is demonstrated for bug fixes when possible.
- Targeted tests pass after the change.
- Broader checks are run or explicitly skipped with a reason.
- Browser issues include runtime evidence, not just code inspection.

## Stop Conditions

- The behavior cannot be reproduced from the available information.
- The test setup is missing and installing dependencies is not approved.
- Running the test would require unsafe external side effects or sensitive data exposure.
- Critical-path code needs characterization tests that cannot be written from current understanding — escalate to the founder.
