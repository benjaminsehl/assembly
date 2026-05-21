---
name: test
description: Use when proving behavior, adding tests, reproducing bugs, or verifying browser/runtime behavior with evidence.
---

# Test

## Purpose

Turn expected behavior or a bug report into proof: failing tests first when possible, then passing tests and runtime evidence.

## References

- `references/workflows/engineering-delivery.md`: test mode, Prove-It pattern, and debugging.
- `references/testing-patterns.md`: test levels and scenario coverage.
- `references/qa-checklist.md`: user-flow QA scenarios.

## Workflow

1. State that the `test` workflow is active and identify the behavior or bug under test.
2. Read the existing test framework, commands, and nearby test style.
3. For new behavior, write tests that describe the expected outcome.
4. For bugs, use the Prove-It pattern: reproduce the bug with a failing test before fixing.
5. For browser or UI behavior, use available browser tooling for real runtime evidence.
6. If reproduction or verification fails unexpectedly, isolate the cause before changing the code.
7. Run targeted tests first, then broader regression checks when practical.

## Verification

- The failing condition is demonstrated for bug fixes when possible.
- Targeted tests pass after the change.
- Broader checks are run or explicitly skipped with a reason.
- Browser issues include runtime evidence, not just code inspection.

## Stop Conditions

- The behavior cannot be reproduced from the available information.
- The test setup is missing and installing dependencies is not approved.
- Running the test would require unsafe external side effects or sensitive data exposure.
