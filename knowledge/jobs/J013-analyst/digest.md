---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J013 G1
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Decision digest: 2026-10-21 (J013 G1)

| # | Decision | Options | Recommendation | Default if no answer |
| --- | --- | --- | --- | --- |
| 1 | G1 for J013 (`job-card.md`, `brief.md`) | approve / change | approve | waits for your answer |
| 2 | When J013 runs. Other jobs (J005, J008-J012) are open | (a) start fact-checks and the tool now; hold the G2 test until a slot is free; (b) wait | (a): steps 2-5 are mostly Sonnet work | (a) |
| 3 | Skill names. `analytics` already exists (logging code) | `analysis-design` + `analysis-craft` (kit pattern), or `player-data` + `player-data-craft` | `analysis-design` + `analysis-craft` | `analysis-design` + `analysis-craft` |
| 4 | What the tool pulls. Roblox has 3 read APIs: Analytics Query (metrics, breakdowns, funnel steps), Experiments (list, status, results), Events (still to check) | (a) Analytics Query + Experiments, both read-only; (b) Analytics Query only | (a): the A/B reading needs the Experiments results; both use the same read-only key | (a); Events only if the fact-check shows it adds data the other two do not |
| 5 | Key and history. Roblox keeps performance data (FPS, crashes, memory) for 28 days only; most other metrics for about 4 years | Key in environment variable `ROBLOX_ANALYTICS_API_KEY`; history in `.tools/analytics-data/<universe id>/` (outside git; another folder with `ANALYTICS_DATA_DIR`); pulls on demand, as for the trend scan (J004-D8) | as stated. Limit: if no pull runs for 4 weeks, the performance history has a gap; the weekly report warns when the last pull is older than 21 days | as stated |
| 6 | Calculations. The paper says no number may come from writing | (a) a small stats helper with tests: cohort age check, rate difference with interval, sample-size plan, sample-ratio check; (b) no helper, the agent calculates in each task | (a): the same formulas every time, checked once | (a) |
| 7 | The `analytics` skill's description today also triggers on "how is retention", "where do players quit", "did the update help" | Move those reading questions to the analyst's skills; `analytics` keeps logging code and the Experiments setup in code | as stated (a one-line change to the description and a pointer line) | as stated |
| 8 | G2 test subject. Needs a published game with data | (a) your live game: you make a read-only key (`universe.analytics:read`) in Creator Hub, set it as an environment variable on this PC, and tell me the universe ID (never the key). Then 1 pull, 1 weekly report (Sonnet medium), 1 deep question (Opus high); (b) a recorded test dataset, clearly labelled TEST | (a) if a game has 10+ daily players; else (b) | (b) if no key is set by G2 |
| 9 | Effort for the Sonnet helpers (extract+check, grade) | high / medium | high, as in J004, J009, J012 | high |
| 10 | Live-ops designer is planned, not built | the analyst writes its hand-off brief; the lead holds the tickets until the role exists | as stated | as stated |
| 11 | Weekly report timing | on demand (you or the lead ask) / a scheduled run | on demand, as you chose for the trend scan | on demand |
