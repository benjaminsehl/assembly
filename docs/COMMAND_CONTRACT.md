# Command Contract

This contract defines the command-like entry skills. These are the stable interface humans will use; the deeper skills are implementation details.

Each entry skill must stay small. It may route, sequence, enforce gates, and summarize evidence. It must not duplicate the full deeper workflow.

## Shared Rules

Every entry skill must:

- Name the active workflow and the reason it applies.
- Identify the current project phase when project docs are available.
- Load the smallest relevant context before acting.
- Prefer existing project conventions over generic process.
- Produce evidence, not vibes.
- Warn when the user asks to skip missing phase prerequisites, recommend the right double-back skill, and record skipped gates if the user insists.
- Stop and ask when the next step would cross an `Ask first` boundary in `docs/SPEC.md`.

Every entry skill must not:

- Invent project commands that are not in the target repo.
- Mark work complete without verification evidence.
- Hide failures or skipped checks.
- Overwrite an existing `AGENTS.md` while scaffolding.
- Continue into a different lifecycle phase unless the user asked for that phase.

If a prompt is unclear, the entry skill should state the inferred task, current phase, and recommended next skill, then ask a concise verification question before acting.

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

## `product-discovery`

Purpose: Pressure-test a raw product idea before spec work.

Triggers:

- "Use product-discovery"
- "Think through this idea"
- "Is this worth building?"
- A vague product idea where user pain, wedge, or evidence is unclear

Inputs:

- Product idea or opportunity
- Known user, market, or workflow context
- Any existing user feedback or personal pain evidence

Underlying skills:

- `interview-me`
- `idea-refine`
- `founder-product-critique`
- `spec-driven-development`

Required outputs:

- Target user and painful moment
- Current workaround or alternative
- Narrow lovable wedge
- Main risks and assumptions
- Next evidence step

Stop conditions:

- The user, pain, and urgency cannot be stated concretely
- The request is ready for implementation rather than discovery
- The next step would require spec or build work without user approval

## `founder-review`

Purpose: Review an idea, spec, or plan as a founder/CEO.

Triggers:

- "Use founder-review"
- "Give this a CEO review"
- "Challenge this plan"
- "What is the 10-star version?"

Inputs:

- Idea, spec, plan, roadmap, or feature proposal
- Target user and success criteria when available

Underlying skills:

- `founder-product-critique`
- `idea-refine`
- `planning-and-task-breakdown`

Required outputs:

- Verdict: Expand, Narrow, Hold scope, or Stop
- User-love opportunity
- Scope recommendation
- Riskiest assumption
- Next evidence step

Stop conditions:

- The artifact has no clear user or objective
- The review would silently change approved scope
- The issue is primarily engineering risk and should go through `review` or `health-check`

## `business-model-review`

Purpose: Evaluate whether a product or feature can become a viable business.

Triggers:

- "Use business-model-review"
- "Can this be a business?"
- "Review the pricing/distribution"
- "What business model fits this?"

Inputs:

- Product concept, feature, or roadmap
- Known users, buyers, alternatives, pricing, or distribution assumptions

Underlying skills:

- `business-model-evaluation`
- `idea-refine`
- `documentation-and-adrs`

Required outputs:

- ICP and buyer
- Willingness-to-pay hypothesis
- Distribution hypothesis
- Retention loop
- Biggest business risk
- Next validation step

Stop conditions:

- No plausible buyer, user, or strategic value is visible
- The request needs user discovery before business-model review
- The business assumption is being treated as proven without evidence

## `design-plan-review`

Purpose: Review planned UX before implementation.

Triggers:

- "Use design-plan-review"
- "Review this UI plan"
- "Check this design before building"
- A user-facing UI or workflow is planned but not implemented yet

Inputs:

- Spec, plan, design doc, screenshot, wireframe, or existing UI convention
- Target user and primary workflow

Underlying skills:

- `frontend-ui-engineering`
- `founder-product-critique`
- `performance-optimization`

Required outputs:

- Design verdict
- Must-fix UX issues
- Recommended improvements
- Approved build shape or stop reason

Stop conditions:

- There is no user flow or artifact to review
- Product intent is too unclear for UI critique
- The user asked for live UI testing, which belongs in `qa`

## `qa`

Purpose: Test the product like a real user after implementation.

Triggers:

- "Use qa"
- "QA this app"
- "Test this local app"
- "Find product bugs"

Inputs:

- Runnable app, URL, feature, or build instructions
- Known test account, setup state, or user flow when needed

Underlying skills:

- `live-qa-methodology`
- `browser-testing-with-devtools`
- `test-driven-development`
- `debugging-and-error-recovery`

Required outputs:

- Tested flows
- Bugs with severity and repro steps
- Evidence collected
- Fix/re-test status
- Regression recommendations

Stop conditions:

- No runnable target is available
- Auth or private data blocks safe testing
- The user asked for report-only QA and fixing would mutate code

## `health-check`

Purpose: Audit project health across product and engineering readiness.

Triggers:

- "Use health-check"
- "Audit this repo"
- "How healthy is this project?"
- "What is blocking confidence?"

Inputs:

- Repo, app, release candidate, or product area
- Project commands and docs

Underlying skills:

- `code-review-and-quality`
- `performance-optimization`
- `security-and-hardening`
- `documentation-and-adrs`
- `test-driven-development`

Required outputs:

- Health verdict
- Blockers and important fixes
- Product, engineering, and business-readiness risks
- Next recommended action

Stop conditions:

- The repo or target surface is not accessible
- Required checks would cause unsafe side effects
- The audit scope is too broad to be honest

## `retro`

Purpose: Capture what shipped, what users learned, what broke, and what should improve.

Triggers:

- "Use retro"
- "Run a retro"
- "What did we learn from this launch?"
- End of project, release, sprint, or work period

Inputs:

- Shipped changes, feedback, incidents, metrics, test/build health, or notes

Underlying skills:

- `documentation-and-adrs`
- `code-review-and-quality`
- `business-model-evaluation`
- `founder-product-critique`

Required outputs:

- Wins, misses, learnings, decisions, and next actions
- Product, engineering, and business lessons separated
- Durable guidance candidates

Stop conditions:

- There is no release, period, or artifact to review
- Private data needed for the retro is unavailable
- The user wants a memory update but has not explicitly requested it

## `learn`

Purpose: Capture durable project guidance without replacing Codex memory.

Triggers:

- "Use learn"
- "Remember this pattern"
- "Capture this project preference"
- "Make this reusable guidance"

Inputs:

- Lesson, preference, repeated pitfall, retro output, or project convention

Underlying skills:

- `documentation-and-adrs`
- `context-engineering`
- `retro`

Required outputs:

- Proposed lesson
- Scope
- Destination
- Exact wording
- Whether a formal memory update is needed

Stop conditions:

- The lesson is speculative or one-off
- The destination is unclear
- The user asks to edit Codex memory without explicitly requesting a memory update

## `new-project`

Purpose: Scaffold a resumable project-docs workspace and proposal gate for a new project, subproject, or major project slice.

Triggers:

- "Use new-project"
- "Start a new project"
- "Start a subproject"
- "Scaffold project docs"
- "Set up this project slice"

Inputs:

- Project name or working title
- Target repo and whether this is root-project work or a subproject slice
- Raw idea, desired outcomes, or existing notes

Underlying skills:

- `product-discovery`
- `founder-review`
- `business-model-review`
- `spec-driven-development`
- `planning-and-task-breakdown`
- `documentation-and-adrs`

Required outputs:

- Project workspace under `docs/`, `docs/projects/<slug>/`, or a parent project's `projects/<slug>/`
- Proposal, prototype, build, and release phase files
- Product vision, principles, decisions, tech-design, specs, plans, prototypes, QA, and release folders
- Child `projects/` folder for nested project paper trails
- `docs/agent-guidance.md`
- Root `AGENTS.md` when absent, or a manual-merge notice when it already exists
- Initial status file with current phase and next recommended skills
- Open questions where alignment is missing

Stop conditions:

- The target project slice is ambiguous
- There is no concrete outcome or user problem yet
- Existing docs conflict with the scaffold and need human choice before merging

## `prototype`

Purpose: Create a throwaway tangible artifact before production build work.

Triggers:

- "Use prototype"
- "Prototype this"
- "Let me play with it"
- "Try a few directions"
- "Sanity-check this workflow"

Inputs:

- Prototype question
- Repo conventions and runnable commands
- Product, UI, technical, or business risk to test

Underlying skills:

- `idea-refine`
- `frontend-ui-engineering`
- `business-model-evaluation`
- `documentation-and-adrs`

Required outputs:

- Clear prototype question
- Small runnable artifact, route, mock, model, or validation artifact
- One command, URL, or file path to inspect it
- Captured verdict: delete, continue, or absorb into build

Stop conditions:

- The question is too unclear to choose an artifact
- The user is actually asking for production implementation
- The prototype would require unsafe data or live integrations without approval

## `project-status`

Purpose: Determine the current project or subproject phase and recommend the next skills.

Triggers:

- "Use project-status"
- "What phase are we in?"
- "Where did we leave off?"
- "What skills should we use next?"
- "Help me resume this project"

Inputs:

- Repo, project folder, or subproject folder
- Status files, phase docs, specs, plans, decisions, open tasks, recent commits, and notes

Underlying skills:

- `context-engineering`
- `documentation-and-adrs`
- `product-discovery`
- `prototype`
- `build`
- `qa`
- `ship`
- `retro`
- `learn`

Required outputs:

- Current phase: proposal, prototype, build, or release
- Evidence for the phase verdict
- Historical decisions or principles that explain the current shape
- Missing required artifacts
- Missing phase prerequisites and skipped-gate risks
- Next decision gate
- Next recommended skills
- One concrete next action

Stop conditions:

- No accessible artifact trail exists
- Multiple active project slices exist and choosing one would be arbitrary
- Private external systems are required to know the current state
