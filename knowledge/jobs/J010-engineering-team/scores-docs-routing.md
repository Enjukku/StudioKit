---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J010-T26, T27; 30 held-out cases eng-evals-hidden/docs-routing/cases.jsonl (written before the tool change; builder saw only the 10 practice cases in knowledge/evals/docs-retrieval.jsonl)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Roblox docs routing (owner 2026-10-21: every main agent finds its section of the Roblox docs)

30 hidden tasks across engineering, film, art, animation, rigging, environment, VFX, sound, UI, analytics, live-ops, marketing and policy; each names the Roblox docs page that answers it.

| Layer | Right page found | Cost |
| --- | --- | --- |
| Context packet before (mirror excluded) | 0 / 30 in the top 5 | free |
| Context packet after (new "Roblox docs" section) | 16 / 30 in the top 5 (17 in the top 10) | free, about 1.8 s per run |
| + explore scout (Haiku, low) on the 14 misses, returning paths and lines | 13 / 14 | one cheap scout run for 14 tasks |
| **Both layers** | **29 / 30** | |

The one miss: "light boxes get launched into the sky after they land". No docs page names this symptom; the first game found the cause only by measuring (study A03). That is the third layer's job (a Studio probe, `engineering-craft` → `references/probes.md`).

Wired in: `AGENTS.md` §0 routing rule; `knowledge/reference/roblox/docs-map.md` (sections per role); `explore` docs-lookup mode (paths and lines, no summaries); `researcher` reads the map; orchestration briefs name docs pages; `Agent` tool added to analyst, art-director, game-designer, live-ops-designer, marketing, progression-designer, reviewer, sound-designer, trend-scout, vfx-designer so they can send the scout. Not measured: whether agents follow the rule in real tasks (watch the "Docs read" lines in hand-backs).
