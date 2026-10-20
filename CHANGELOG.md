# Changelog

> Author: kit-writer · claude-sonnet-5-5 · medium · 2026-10-20

## 0.3.1 (2026-10-20): Roblox docs in the kit (J001 step 0)

- The Roblox Creator Docs mirror now ships with the kit (`knowledge/external/roblox-creator-docs/`, upstream `7400643`), with its sync tool `tools/sync_roblox_docs.py` (ported from DestructionSimulator).
- New note `knowledge/reference/roblox/whats-new.md`: 2026 features, betas and rules from official Roblox posts, by skill area.
- Fixed the project-authored UI pages: base UIShadow and per-corner UICorner are live; Upgraded UIShadows and Upgraded UIGradients are beta and not publishable.

## 0.3.0 (2026-10-20): phase 3, orchestrator and agent-building system

- The kit ships only the orchestrator and the system; other roles are built from owner material (owner decision).
- `/build-agent` workflow; templates `templates/role.md` and `templates/skill/SKILL.md`.
- The lead loads the `orchestration` skill at the start of every owner request.
- Removed `/council` (outdated); `/agent-review` folded into `/improve` as a monthly step.

## 0.2.0 (2026-10-20): phase 2

- Knowledge rules (`rules/knowledge.md`): typed frontmatter, load-by-cost layers, scopes, superseding.
- Learning loop inside `/improve`: inbox drafts, weekly consolidation, promotion to lessons, skills, rules and overlays.
- Workflows: `/improve`, `/integrate`, `/kit-sync`, `/council`, `/agent-review`.
- Context tools: `context_packet`, `kb_index`, `eval_context`.
- Process tools: `improve_scan`, `agent_scorecard`.
- Gate: `python tools/verify.py`.
- New folders: `knowledge/lessons/`, `knowledge/overlays/`; inbox README updated.
- Research note: `knowledge/reference/studio/context-research-2026-10.md`.

## 0.1.0 (2026-10-20): phase 1

- Rules: company rulebook, owner profile, harness profiles (Claude Code, Codex).
- Orchestration skill and role roster.
- Job templates: job card, intent brief, beat sheet, ledger, decision digest, status block.
- Sync tool: `tools/sync_harness.py` generates `.claude/` and `.codex/`.
- Knowledge skeleton: index, game profile, ledgers, orchestration research.
