---
type: job
scope: universal
status: draft
updated: 2026-10-24
source: J022; Claude Code docs read 2026-10-24 (code.claude.com/docs/en/settings-reference, env-vars, model-config, sub-agents, mcp, prompt-caching, costs)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-24

# J022 settings proposal (the owner applies; agents never edit settings)

Put these in your **user** settings, `~/.claude/settings.json`, so every game and the kit get them. Project or local settings override user settings for one repository.

```json
{
  "autoCompactWindow": 500000,
  "env": {
    "CLAUDE_CODE_SUBAGENT_MODEL": "sonnet"
  }
}
```

| # | Setting | What it does | Why (J022 evidence) | Trade-off | Docs |
| --- | --- | --- | --- | --- | --- |
| S1 | `autoCompactWindow: 500000` (owner J023-D1: "under 500K"; 600 k considered) | Compacts when the context reaches 500 k tokens. Allowed range 100,000 to 1,000,000. Same as the env var `CLAUDE_CODE_AUTO_COMPACT_WINDOW`, or `/autocompact 200k` | Game build chats ran at a median of 413-462 k tokens per call with no automatic compaction. On a model with a 1M window the default compacts at about 967 k. The only two compactions seen were manual, at 948 k and 883 k | A compaction costs one summary call and drops detail. The kit keeps job state in files and re-loads skills after compaction (the first 5,000 tokens of each skill). A lower number saves more usage per call (200 k was J022's first proposal); a higher one keeps more detail | model-config "Set the auto-compact window"; settings-reference |
| S2 | `CLAUDE_CODE_SUBAGENT_MODEL: sonnet` | Model for general-purpose and workflow agents that get no model in the call or the definition | Helper agents fell back to Opus: 3 Explore agents in Reverse, and 14 general-purpose agents that read 513 M tokens in one GreatWallSim session (first hand tally, not deduplicated) | Kit roles pin their own model, so craft work stays on Opus. Does **not** change the built-in Explore and Plan agents: the kit rule says to use the kit `explore` role instead | env-vars; sub-agents "Choose a model" |

## Considered and not proposed
| Setting | Why not |
| --- | --- |
| `CLAUDE_CODE_DISABLE_1M_CONTEXT=1` (hard 200 k window) | Saves the most per call, but the owner chose 500 k (J023-D1) to keep sessions whole for longer |
| Turning MCP servers off per project (`/mcp` panel, `disabledMcpServers` in `~/.claude.json`) | MCP tools already load lazily (tool search is on by default), so unused servers cost little. Use it only for a server that agents misuse in a repository |
| `bashOutputMaxChars` / `BASH_MAX_OUTPUT_LENGTH` (default 30,000 characters) | Shell output was a small part of the context; the Tool calls rule (cut output at the source) covers it |
| `CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1` | It would also move pinned craft roles off Opus |
| A setting to drop earlier thinking | None is documented for Claude Code; the API keeps earlier thinking by default |

## How to check it worked
After a week, run `python tools/usage_report.py --root <game repo>` (or let `/improve` run it). Expected: fewer "big context" and "no compaction" flags and no "helper on Opus" flags; repair rounds no higher than before.
