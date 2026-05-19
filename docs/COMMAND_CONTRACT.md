# Command Contract

This contract defines the seven command-like entry skills. These are the stable interface humans will use; the deeper skills are implementation details.

Each entry skill must stay small. It may route, sequence, enforce gates, and summarize evidence. It must not duplicate the full deeper workflow.

## Shared Rules

Every entry skill must:

- Name the active workflow and the reason it applies.
- Load the smallest relevant context before acting.
- Prefer existing project conventions over generic process.
- Produce evidence, not vibes.
- Stop and ask when the next step would cross an `Ask first` boundary in `docs/SPEC.md`.

Every entry skill must not:

- Invent project commands that are not in the target repo.
- Mark work complete without verification evidence.
- Hide failures or skipped checks.
- Continue into a different lifecycle phase unless the user asked for that phase.

## `spec`

Purpose: Turn an idea or request into a reviewed specification before implementation.

Triggers:

- "Use spec"
- "Write a spec"
- "Define this before building"
- A new project, feature, or significant change with unclear requirements

Inputs:

- User goal
- Existing repo context, if any
- Known constraints, stack, commands, and boundaries

Underlying skills:

- `interview-me`
- `idea-refine`
- `spec-driven-development`

Required outputs:

- Assumptions surfaced before the spec is treated as final
- A saved spec, normally `SPEC.md` or `docs/SPEC.md`
- Open questions
- A clear review gate before planning or implementation

Stop conditions:

- Requirements are too ambiguous to define success criteria
- The user has not approved major assumptions
- The requested scope conflicts with repo boundaries or safety constraints

## `plan`

Purpose: Convert an approved spec into small, dependency-ordered tasks.

Triggers:

- "Use plan"
- "Break this down"
- "Create tasks"
- "Plan how to build this"

Inputs:

- Approved spec
- Relevant codebase structure
- Project commands and test strategy

Underlying skills:

- `planning-and-task-breakdown`
- `context-engineering`

Required outputs:

- Dependency graph or ordering rationale
- Task list with acceptance criteria
- Verification step for every task
- Checkpoints between phases
- Saved plan and todo file

Stop conditions:

- No spec exists and assumptions would be risky
- Tasks are too large to verify in focused sessions
- The plan requires external setup or credentials not yet approved

## `build`

Purpose: Implement exactly one planned vertical slice at a time.

Triggers:

- "Use build"
- "Implement the next task"
- "Continue from the plan"
- "Build task N"

Inputs:

- Approved task list
- Target task acceptance criteria
- Relevant source files and project commands

Underlying skills:

- `incremental-implementation`
- `test-driven-development`
- `debugging-and-error-recovery`
- `git-workflow-and-versioning`

Required outputs:

- Files changed
- Tests added or updated
- Verification commands run and results
- Task status update only after verification

Stop conditions:

- No task list exists
- The next task is ambiguous or too broad
- Tests or build fail and the root cause cannot be isolated safely
- The task crosses an `Ask first` boundary

## `test`

Purpose: Prove behavior with tests and runtime checks.

Triggers:

- "Use test"
- "Write tests"
- "Prove this bug"
- "Verify this behavior"

Inputs:

- Feature behavior or bug report
- Existing test framework and commands
- Reproduction details for bugs

Underlying skills:

- `test-driven-development`
- `browser-testing-with-devtools`
- `debugging-and-error-recovery`

Required outputs:

- Failing test first for new bug coverage where possible
- Passing targeted test after implementation or fix
- Full-suite or broader regression check when practical
- Browser/runtime evidence for UI behavior

Stop conditions:

- The behavior cannot be reproduced
- Test framework or dependencies are missing and installation is not approved
- A test would require sensitive data or unsafe external side effects

## `review`

Purpose: Review changes before merge with a bug-first, evidence-first posture.

Triggers:

- "Use review"
- "Review this PR"
- "Check this diff"
- "Is this ready to merge?"

Inputs:

- Staged changes, working tree diff, commits, or PR
- Spec or acceptance criteria where available
- Test/build output where available

Underlying skills:

- `code-review-and-quality`
- `security-and-hardening`
- `performance-optimization`

Required outputs:

- Findings first, ordered by severity
- File and line references for concrete issues
- Missing tests or verification gaps
- Short summary only after findings

Stop conditions:

- There is no accessible diff or changed scope
- Sensitive data would need to be printed to review
- The review scope is broader than the available context can support

## `code-simplify`

Purpose: Simplify code without changing behavior.

Triggers:

- "Use code-simplify"
- "Simplify this code"
- "Reduce complexity"
- "Make this easier to maintain"

Inputs:

- Target files or recent diff
- Existing tests
- Callers and behavior constraints

Underlying skills:

- `code-simplification`
- `code-review-and-quality`
- `test-driven-development`

Required outputs:

- Behavior-preserving changes only
- Explanation of simplification rationale
- Tests/build proving behavior is unchanged
- Reverted or abandoned simplifications if they break verification

Stop conditions:

- Behavior is not covered well enough and cannot be characterized
- Simplification would require broad architectural change
- The target includes user changes unrelated to the requested scope

## `ship`

Purpose: Decide whether a change is ready to release, with rollback criteria.

Triggers:

- "Use ship"
- "Can we ship this?"
- "Run pre-launch"
- "Give me a go/no-go"

Inputs:

- Current diff or release candidate
- Test/build/CI status
- Deployment or rollout context
- Known risks and rollback mechanism

Underlying skills:

- `shipping-and-launch`
- `ci-cd-and-automation`
- `security-and-hardening`
- `performance-optimization`
- `documentation-and-adrs`
- `deprecation-and-migration`
- `code-review-and-quality`

Required outputs:

- `GO` or `NO-GO`
- Launch blockers
- Recommended fixes
- Acknowledged risks
- Rollback trigger conditions and procedure
- Verification evidence

Codex-specific rule:

- Parallel specialist review is used only when the user explicitly authorizes subagents or parallel agent work. Without that authorization, `ship` performs the audit locally and states that the fan-out path was not used.

Stop conditions:

- Rollback path is unknown for a production-bound change
- Critical security, data-loss, or migration risk is unresolved
- Required verification is unavailable and the user has not accepted the risk

