---
name: reference-anthropic-docs-access
description: How to read Anthropic prompting and Claude Code docs with WebFetch (verbatim prompt, persisted files, model page URLs)
metadata:
  type: reference
---

Learned in J017-T01 (2026-10-21).

- platform.claude.com prompting pages return near-verbatim text when the prompt says "return full text verbatim". Large results are persisted to a tool-results file; read it in 400-500 line chunks.
- Per-model pages: `.../prompt-engineering/prompting-claude-{opus-5-5,sonnet-5-5,haiku-5-5,opus-5}`; effort at `/build-with-claude/effort`; thinking at `/build-with-claude/thinking-steering-and-cost`.
- code.claude.com pages (sub-agents, mcp, skills) exceed 100k chars: WebFetch cuts at 100000; call again with `offset: 100000` for tails (MCP tool search section is in the tail). Their output is a model extract, so re-fetch before trusting numbers.
- Grep on the persisted file works for long pages (memory page: used it to pull size/import rules).
