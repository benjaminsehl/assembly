# Engineering Delivery Workflow

## Contents

- Spec
- Plan
- Build
- Test
- Review
- Code simplify

Use this reference from `spec`, `plan`, `build`, `test`, `review`, and `code-simplify`.

## Spec

- Define objective, users, constraints, commands, boundaries, success criteria, and open questions.
- Surface assumptions before treating the spec as final.
- Save the spec using the repo convention, usually `SPEC.md` or `docs/SPEC.md`.
- Stop at review before planning unless the user asks to continue.

## Plan

- Start from an approved spec or equivalent requirements.
- Break work into vertical slices with acceptance criteria and verification.
- Name dependencies and checkpoints.
- Save plan and todo files using the repo convention.
- Stop before implementation unless the user asks to continue.

## Build

- Implement one planned slice at a time.
- Write or identify the target test first for behavior changes when practical.
- Make the smallest complete change.
- Keep unrelated cleanup out of scope.
- Run targeted verification and the broadest practical regression check.
- Update task status only after verification passes or skipped checks are explained.

## Test

- For bugs, prove the bug with a failing test before fixing when practical.
- For new behavior, write tests that describe the intended outcome.
- Use browser/runtime verification for UI behavior.
- Report targeted and broader check results separately.

## Review

- Inspect the diff plus relevant surrounding code.
- Lead with findings ordered by severity.
- Include file and line references for concrete issues.
- Apply security, performance, and accessibility checklists only when their triggers apply.
- If there are no findings, say so and name residual risk.

## Code Simplify

- Preserve behavior exactly.
- Prefer clearer names, guard clauses, smaller functions, removed duplication, and deleted dead code.
- Characterize behavior before changing risky code.
- Verify after each meaningful step.
- Abandon simplifications that cannot be proved safe.
