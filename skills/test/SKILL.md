---
name: test
description: Use when proving behavior, adding tests, reproducing bugs, or verifying browser/runtime behavior with evidence.
---

# Test

## Purpose

Turn expected behavior or a bug report into proof: failing tests first when possible, then passing tests and runtime evidence.

## Underlying skills

- `test-driven-development`
- `browser-testing-with-devtools`
- `debugging-and-error-recovery`

## Workflow

1. State that the `test` workflow is active and identify the behavior or bug under test.
2. Read the existing test framework, commands, and nearby test style.
3. For new behavior, use `test-driven-development` to write tests that describe the expected outcome.
4. For bugs, use the Prove-It pattern: reproduce the bug with a failing test before fixing.
5. For browser or UI behavior, use `browser-testing-with-devtools` or the available browser tooling for real runtime evidence.
6. If reproduction or verification fails unexpectedly, use `debugging-and-error-recovery` to isolate the cause.
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

