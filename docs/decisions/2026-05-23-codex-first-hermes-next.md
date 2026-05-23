# Decision: Codex First, Hermes Next

Date: 2026-05-23

## Context

Assembly could theoretically become a portable protocol with adapters for Codex, Claude Code, Hermes, and other agent runtimes. That is attractive long-term, but it risks turning the current 1.0 effort into a compatibility project instead of finishing the product-building stack that Sai will actually use every day.

The valuable near-term path is to make the Codex plugin excellent, then use Hermes as an orchestrator that can drive Codex sessions through Assembly's project workflow.

## Decision

Assembly 1.0 will focus on the Codex plugin.

Claude Code support is not a meaningful near-term priority. We can avoid blocking future portability by keeping the project protocol readable and runtime-aware, but we will not spend 1.0 work designing or generating Claude adapters.

After the Codex plugin is solid, the next strategic project is Hermes orchestration: Hermes as the product/roadmap operator, Codex as the focused builder executing Assembly-scoped work.

## Why

- Codex is the active daily build environment.
- The plugin still needs to prove its own workflow before adapters matter.
- Hermes orchestration is closer to the app-factory vision than Claude compatibility.
- Supporting multiple agent runtimes too early would add surface area before the core loop is excellent.

## Consequences

- 1.0 specs, release criteria, and proof projects should optimize for Codex.
- Claude can be mentioned only as future optional portability, not as planned roadmap work.
- Hermes orchestration should become the post-1.0 north star once Assembly's Codex flow is stable.
- Architecture choices should preserve clean boundaries between Assembly's project protocol and Codex-specific packaging, but only where doing so stays cheap.
