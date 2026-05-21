---
name: learn
description: Use to capture project preferences, product lessons, recurring pitfalls, and reusable guidance without replacing Codex memory.
---

# Learn

## Purpose

Turn repeated lessons into reusable project guidance. This skill proposes durable notes; it does not silently edit global memory or override the Codex memory system.

## Underlying skills

- `documentation-and-adrs`
- `context-engineering`
- `retro`

## Workflow

1. State that `learn` is active and identify the lesson, preference, or recurring pattern.
2. Determine whether the lesson belongs in project docs, an ADR, a local skill, a README, or a future memory update request.
3. Use `context-engineering` to keep guidance scoped to the projects where it applies.
4. Use `documentation-and-adrs` to shape durable documentation when appropriate.
5. Use `retro` when the lesson comes from a shipped cycle or incident.
6. Output the proposed lesson, scope, destination, and exact wording.
7. Do not edit Codex memory unless the user explicitly asks for a memory update.

## Verification

- The lesson is evidence-based.
- Scope is clear: global, plugin, repo, feature, or product area.
- Destination is named.
- Wording is concise enough to be reused by future agents.

## Stop Conditions

- The lesson is speculative or based on a one-off event.
- The user asks to update memory but the required memory-update workflow has not been followed.
- The proposed guidance conflicts with existing project instructions.

