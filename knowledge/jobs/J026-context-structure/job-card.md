---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J026
supersedes: []
---
> Author: orchestrator (side session) · claude-opus-5-5 · default · 2026-10-24

# Job card: J026 context structure and docs use

Owner words (relayed by the lead chat, verbatim): "they're not fully grasping their role, and then they're not properly looking at the Roblox documentation. And that makes me wonder if we are setting up the context unoptimally. And I don't want you to just like guess what good context structure looks like... I want you to look at more like Anthropic employees, saying what context should look like." And: "I'm wondering if it would be better to use Obsidian, if there's any benefit in that, or if that's really just like a some sort of like MD structure."

| Key | Value |
| --- | --- |
| Problem | Agents may not use their role, books and the Roblox docs mirror. Is the context set up badly? |
| Constraints | Evidence, not guesses. Anthropic primary sources. No edits before the owner picks. Keep the J024 run cut (72 % fewer runs). Session < 500k context. |
| Type, size | Kit research and proposal (no game recipe). M by effort, no G1/G3 build stages: the owner picks fixes from `proposal.md`. |
| Success test | A ranked fix list, each with its cost, tied to measured failures and to Anthropic sources; a plain Obsidian answer. |
| Outputs | `research-anthropic.md`, `research-loading.md` (Sonnet researchers), `measured-agents.md`, `proposal.md`, `scripts/` |
| Linked | Side session "Lead skips specialist agents" (routing; note `routing-failure-proposal.md` in the shared side-session notes). Its F-fixes and J026 F5 overlap. |
| Status | Owner picked F1, F2, F3 (J026-D1). Built 2026-10-24, not committed. Re-measure after one game week with `scripts/pass3.py` and `scripts/claims2.py` (`proposal.md` §3). |
| Built (J026-D1) | F1 `tools/hooks/subagent_context.py` (docs sections and key pages; runs with no open job; cap 4,000 characters, key pages cut before `Run:` lines) · F2 `tools/sync_harness.py` `docs_block` (generated "Roblox docs" lines after each role's first paragraph, Claude and Codex) · F3 `tools/context_packet.py docs` (brief `docs:` key; pages in the role's sections first), `rules/messages.md` §2 and §9, `orchestration` §10, `templates/jobs/intent-brief.md` · one source: `context_packet.role_docs` reads `knowledge/reference/roblox/docs-map.md` (header note added) · docs: `rules/knowledge.md` §2-3, `tools/hooks/README.md`, `templates/role.md` · tests: `test_hooks.py` (+4), `test_sync_harness.py` (+1) |
| Not built | Saved job workflows (`.agents/workflows/jobs/*.js`) build their own agent prompts without a `docs:` key; their agents still get F1 and F2. The `docs` ranking is the packet's existing mirror ranker: it can list off-topic pages (for example `input/` pages for a save task), so the lead cuts them. |
