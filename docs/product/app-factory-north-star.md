# North Star: Agentic App Factory

Last updated: 2026-05-27
Status: direction for 1.0 and beyond

## Vision

Assembly is the operating system for a human-led agentic app factory.

The factory does not remove the founder from the loop. It gives the founder a better team: agents that can ask the right questions, preserve product judgment, execute scoped work, test their own output, and hand off evidence clearly enough that future sessions can continue without losing the thread.

## Founder Role

The human user is the founder and product director.

They own:

- Taste and ambition.
- The user problem.
- What should become 10x better.
- What good looks like.
- Which tradeoffs are acceptable.
- Whether to proceed through major gates.

Agents own:

- Clarifying missing context.
- Turning intent into specs, plans, prototypes, code, tests, reviews, and release evidence.
- Naming risks and skipped gates.
- Preserving the paper trail.
- Performing bounded implementation and verification work.

## Product Promise

A founder should be able to return to any project and say `next`.

Assembly should then:

1. Find the relevant project or subproject.
2. Read the local trail.
3. Identify the phase and missing context.
4. Ask concise questions when product judgment is missing.
5. Dispatch to the next appropriate skill when the next step is clear.
6. Complete the work with verification and GitHub handoff where appropriate.
7. Update status so the next agent starts from evidence instead of guesswork.

## Quality Bar

Assembly should produce work that is:

- Lovable for users.
- Feasible for the current project.
- Engineered cleanly.
- Testable and reviewable.
- Business-aware.
- Honest about uncertainty.
- Easy for the next agent to resume.

## App Factory Shape

The eventual factory has four layers:

1. Assembly protocol: skills, phase gates, project trail, and GitHub handoff.
2. Project memory: docs, decisions, logs, notes, references, and status.
3. Specialist agents: product, design, engineering, QA, release, research, and context-engineering roles.
4. Hermes orchestration: a long-running coordinator that schedules and supervises Codex sessions against a roadmap.

## 1.0 Wedge

Assembly 1.0 proves only the first two layers and enough specialist coordination to be useful inside Codex.

Success means:

- The plugin is installable and visible.
- The project scaffold is reliable.
- `next` can drive the normal workflow without guessing.
- Product discovery interviews before deciding unless the founder delegates.
- Build work moves through spec, plan, implementation, verification, review, simplification, and PR handoff.
- Real projects leave enough evidence for future agents to resume.

## Post-1.0 Ambition

After 1.0, Hermes can become the General Manager for a roadmap.

Hermes should not be a blind autonomous builder. It should be a durable orchestration layer that:

- Maintains the roadmap.
- Chooses which Assembly skill or Codex session is needed next.
- Spawns bounded work sessions with explicit ownership.
- Waits for evidence.
- Escalates founder questions when product judgment is missing.
- Tracks quality, release readiness, and learning over time.

## Anti-Goals

- Do not turn every project into ceremony.
- Do not hide product assumptions.
- Do not let agents silently choose founder-level tradeoffs.
- Do not make Hermes responsible for product taste before Assembly's Codex loop is excellent.
- Do not optimize for impressive autonomy at the expense of inspectability.
