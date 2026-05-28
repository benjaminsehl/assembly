# North Star: Human-Led, Agent-Executed Product Building

Last updated: 2026-05-28
Status: direction for 1.0 and beyond

## Vision

Assembly is the per-project operating system for human-led, agent-executed product building.

The human stays founder and product director. Agents do the execution — discovery interviews, specs, plans, code, tests, reviews, QA, release evidence — and ask concise questions when product direction is missing. Questions are always framed in product implications ("this would mean users can't X", "this changes the wedge from A to B"), never in engineering detail. The human's time stays on judgment, not on translating engineering decisions into product context.

"Agentic app factory" is the family of framings this idea has been described with elsewhere. Assembly is narrower: it lives inside one project at a time, with the human in the loop on product direction.

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

- Clarifying missing context in product-implication language, not engineering detail.
- Turning intent into specs, plans, prototypes, code, tests, reviews, and release evidence.
- Surfacing business, user, and viability concerns for founder judgment (flag, do not decide).
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
- Surfaces business, user, and viability concerns for founder judgment (does not decide them).
- Honest about uncertainty.
- Easy for the next agent to resume.

## System Shape

The eventual system has four layers:

1. Assembly protocol: skills, phase gates, project trail, and GitHub handoff.
2. Project memory: docs, decisions, logs, notes, references, and status.
3. Specialist agents: product, design, engineering, QA, release, research, and context-engineering roles.
4. Post-1.0 orchestration: an in-project coordinator that keeps agents executing through the lifecycle while pausing for founder product judgment at the right moments.

## 1.0 Wedge

Assembly 1.0 proves only the first two layers and enough specialist coordination to be useful inside Codex and Claude Code from the same plugin bundle.

Success means:

- The plugin is installable and visible.
- The project scaffold is reliable.
- `next` can drive the normal workflow without guessing.
- Product discovery interviews before deciding unless the founder delegates.
- Build work moves through spec, plan, implementation, verification, review, simplification, and PR handoff.
- Real projects leave enough evidence for future agents to resume.

## Post-1.0 Ambition

After 1.0, a post-1.0 orchestrator can become the in-project general manager.

That orchestrator should not be a blind autonomous builder. It should be a durable in-project layer that:

- Maintains the project roadmap.
- Chooses which Assembly skill or agent session is needed next.
- Spawns bounded work sessions with explicit ownership.
- Waits for evidence.
- Escalates founder questions in product-implication language when product judgment is missing.
- Tracks quality, release readiness, and learning over time.

Whether the orchestrator ever coordinates across multiple projects is an open question for after 1.0; the per-project loop is the only required scope.

## Anti-Goals

- Do not turn every project into ceremony.
- Do not hide product assumptions.
- Do not let agents silently choose founder-level tradeoffs.
- Do not ask the founder in engineering-implementation language when a product-implication framing is possible.
- Do not make the post-1.0 orchestrator responsible for product taste before Assembly's agent control loop is excellent.
- Do not optimize for impressive autonomy at the expense of inspectability.
