---
type: reference
scope: universal
status: draft
updated: 2026-10-24
source: owner chat 2026-10-24 (J023 session)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-24

# Juku Studios: the owner's ideas (input for the feasibility and design work)

Juku Studios = the owner's own external harness, a renamed fork of T3 Code (https://github.com/pingdotgg/t3code), adapted to the Studio Kit. Status: idea; feasibility not yet checked.

## Owner's words (verbatim)
- "I think it would be nice to have an interface similar to T3 code, because I mean the code is already right there. And then we can just rename it to Juku Studios and kind of integrate it into what I need"
- "I have two accounts. That I use because I max each one out, and when one is maxed out, I like to use the other one."
- "I like the idea of a flow plus flow map."
- "I would want to generate a little Claude like icon with like various like hats and characteristics to distinguish which agent it is in the visual, with a maybe like their like name above them"
- "I think I might want something similar to Obsidian in another tab ... my worry is ... my Obsidian usually grows too so big that it might be like difficult to render."

## Direction so far
| Part | Idea | Notes |
| --- | --- | --- |
| Accounts | Two Claude subscription logins plus Codex; switch when one is maxed out | Uses the CLIs' own logins (no API credits); usage meter per account |
| Images | Codex image generation instead of driving ChatGPT in a browser | Removes browser screenshots from agent contexts; check what the Codex plan covers |
| Front screen | Studio floor: a room per craft, agents as small figures walking hand-offs between rooms, the owner's desk with gate questions as buttons | Glance view: who works, who waits on the owner |
| Job view | Flow map: a lane per craft, one bar per agent run sized by tokens, arrows for hand-offs, gates as dashed lines | For spotting repeated passes, reviewer pile-ups and waits |
| Agent figures | One original mascot (not Anthropic's logo or mascot) with a hat and prop per role, the role name above it, a model badge (Opus / Sonnet / Haiku) | Colours from each role's `color:` key in `.agents/roles/` (25 roles have one); images made with the kit's reference-images pipeline |
| Knowledge tab | An Obsidian-like tab over the kit's `knowledge/` notes: note view, backlinks, search, graph | Today: 1,611 notes and 14,249 `[[links]]`. Render plan: local graph first (the open note and 1-2 hops), filters by type, scope and job, whole graph only on request with a WebGL canvas renderer, layout computed once from `tools/kb_index.py` output. Unique link to the job view: click an agent run and see the notes it read (the hand-back's `docs_read`) |
| Data | Job folders (`active.md`, ledgers, `crew.md`, `decisions.md`), `tools/usage_report.py --json`, subagent transcripts | The view only reads; it never edits kit files |

## Open
- License, Windows support, kit loading through the Agent SDK, two logins, upkeep: the feasibility check.
- Whether the knowledge tab also opens the owner's personal Obsidian vault, or only the kit's `knowledge/`.
