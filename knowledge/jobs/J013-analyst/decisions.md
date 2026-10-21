---
type: decision
scope: universal
status: active
updated: 2026-10-21
source: owner chat 2026-10-21
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# J013 decisions

| ID | date | decision | owner's words |
| --- | --- | --- | --- |
| J013-D1 | 2026-10-21 | Analyst runs on Sonnet, medium effort; Opus at high effort for a deep investigation | "Model: Sonnet, medium effort; Opus at high effort for a deep investigation (for example a big retention drop)." |
| J013-D2 | 2026-10-21 | Material: the owner's analyst research paper, checked; Roblox analytics facts, benchmarks and statistics rules first; unbacked claims dropped | "Use it as strong evidence, but not as gospel. Check claims that matter, especially Roblox analytics facts, benchmarks and statistics rules, and drop what you cannot back up." |
| J013-D3 | 2026-10-21 | The analyst decides what a feature logs; the J001 `analytics` skill covers the logging code | "It decides which events a new feature should log, using the approved analytics skill from J001 (that skill covers the logging code; this agent covers reading the data)." |
| J013-D4 | 2026-10-21 | Data tool on Roblox's official Open Cloud analytics APIs with saved history and tests; key only in the owner's environment | "a script that pulls the game's data through Roblox's official Open Cloud analytics APIs and saves the history ... The API key lives only in my environment, never in the repo or in chat." |
| J013-D5 | 2026-10-21 | Weekly report to owner, game designer, progression designer, marketing, live-ops designer | "It sends a weekly report to me, the game designer, the progression designer, marketing and the live-ops designer." |
| J013-D6 | 2026-10-21 | G1 approved (job card + brief). Digest items 2-11 had no explicit answer, so their defaults apply: start steps 2-5 now, G2 test when a slot is free; skills `analysis-design` + `analysis-craft`; tool pulls Analytics Query + Experiments read-only (Events only if it adds data); key in `ROBLOX_ANALYTICS_API_KEY`, history in `.tools/analytics-data/<universe id>/` (`ANALYTICS_DATA_DIR` override), on-demand pulls, stale-pull warning at 21 days; stats helper with tests; `analytics` description loses the reading triggers; G2 on the owner's live game if a key is set, else a labelled TEST dataset; Sonnet helpers at high; live-ops tickets held by the lead; weekly report on demand | "You may begin." |
| J013-D7 | 2026-10-21 | G3: the analyst is done; no further testing now. Defaults of `digest-g3.md` apply: verdict rule (a) default (L > 0 and middle estimate ≥ smallest worthwhile effect), `analytics` T-03 gets the server-decided-failure line, SRM alarm p < 0.0005, "analyst (planned)" pointers updated. The real-data run (item 4) waits until a game is made; mistakes found in game work feed the kit's improvement loop | "For now, the agent is just done. We're not going to do any testing right now. We will be doing a lot of testing with this kit in the future, making games. So we'll pick up mistakes and this kit should continue to keep updating and getting better." |
