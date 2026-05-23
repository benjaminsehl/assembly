# 2026-05-22 Root Docs Project Trail

## Status

Accepted

## Context

Assembly contains plugin-internal docs under `plugins/assembly/docs/`, but the repo itself also needs a project trail for evolving Assembly as a product.

## Options Considered

- Use only `plugins/assembly/docs/`.
- Put planning notes in root files.
- Create a root `docs/` workspace using Assembly's own scaffold.

## Decision

Use root `docs/` as the Assembly product/project workspace. Keep root `.agents/` for agent-only operating material. Keep plugin-internal docs focused on plugin distribution, contracts, and implementation details.

## Why This Wins

This lets Assembly dogfood its own project model without mixing product-discovery and phase-status artifacts into the installable plugin documentation.

## Consequences

Future agents should read `docs/status.md` before deciding what Assembly work to do, use `.agents/` for agent handoff context, then inspect `plugins/assembly/docs/` only when changing plugin behavior or docs.
