# Product Strategy Workflow

## Contents

- Discovery
- Founder critique
- Business model
- Design plan
- Prototype

Use this reference from `product-discovery` and `prototype`. It keeps product lenses available without exposing every lens as a triggerable skill.

## Discovery

- Restate the idea as a user problem.
- Treat the user as founder/product director; agents clarify and recommend, but do not silently take product authority.
- Default to interview mode for raw ideas, fuzzy directions, and short prompts.
- Ask a focused batch of high-leverage questions before judging the product unless the user explicitly asks the agent to decide.
- Identify target user, painful moment, current workaround, urgency, desired outcome, constraints, distribution path, and success evidence.
- Make what is being built, why it matters, and what good looks like explicit before recommending wedge, scope, or success criteria.
- Use delegated mode only when the user asks for recommendations or the project docs already provide enough evidence. Label assumptions clearly.
- Name alternatives and why they are insufficient.
- Pick a narrow wedge that can teach something real.
- Define evidence needed before build.
- Keep open questions visible; do not bury missing product choices inside confident recommendations.

## Founder Critique

Use when the risk is ambition, focus, scope, urgency, differentiation, or delight.

Verdict options:

- Expand: ambition is too small for the opportunity.
- Narrow: scope is too broad for the next learning step.
- Hold: direction is good enough; avoid churn.
- Stop: problem, user, or opportunity is not compelling enough.

Always include the smallest first slice if recommending expansion.

## Business Model

Use when viability depends on buyer, ICP, pricing, distribution, retention, or cost risk.

Check:

- User versus buyer.
- Pain intensity and budget owner.
- Willingness-to-pay hypothesis.
- Distribution channel.
- Retention loop.
- Gross margin or usage-cost risk.
- Evidence that can falsify the riskiest assumption.

## Design Plan

Use before implementing a user-facing UI or workflow.

Check:

- Primary user flow and primary action.
- Empty, loading, error, success, and permission states.
- Accessibility and responsive behavior.
- Interaction quality and product taste.
- AI-slop signals: generic layout, vague copy, decorative clutter, or missing real user state.

Output a design verdict: approved, approved with must-fixes, or not ready.

## Prototype

Use when the next question should be answered by something tangible before production build.

- Write the exact prototype question.
- Build the smallest artifact that answers it.
- Keep prototype code obviously temporary.
- Provide one command, URL, or file path to inspect it.
- Capture verdict: delete, continue, or absorb into build.
