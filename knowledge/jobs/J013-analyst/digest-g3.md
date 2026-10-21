---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J013 G2 result + G3 request
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Decision digest: 2026-10-21 (J013 G2 result, G3 request)

G2 ran on a SYNTHETIC TEST history (no key was set; default of G1 item 8). Results: `g2-scenario.md` (planted causes vs what the agent found), `grade-J013-hidden.md` (hidden cases, separate grader).

| # | Decision | Options | Recommendation | Default if no answer |
| --- | --- | --- | --- | --- |
| 1 | G3: approve the analyst agent (role `analyst`, skills `analysis-design` + `analysis-craft`, tool `tools/analytics/`, 4 templates) | approve / approve after a real-data run / change | approve now; run the real-data check (item 4) as the first live job | waits for your answer |
| 2 | Rule for "the test helped" (verdict "useful improvement") | (a) default: the whole likely range is above zero and the middle estimate reaches the smallest gain worth having; (b) strict: even the low end reaches that gain | (a): (b) needs far more players than small Roblox games have, so almost every test would end "inconclusive"; (a) still needs a real, positive effect | (a) |
| 3 | `analytics` skill rule T-03 says "log the success, not the attempt". The analyst needs failed tries and their reasons (not enough coins, requirement not met) | add one line: failures decided by the server may be logged as their own funnel step or custom event, after the server decides; client tries stay unlogged | add the line | add the line |
| 4 | First real-data run. Needs a published game | you create a key with `universe.analytics:read` + `universe:read` (no write), set `ROBLOX_ANALYTICS_API_KEY` on this PC (README §1), and tell me only the universe ID; the analyst then pulls, writes a weekly page and settles 6 open API facts (retention date, reporting lag, empty days, experiment stats, weekly bucket start, cohort denominator) in the game's overlay | when a game has 10+ daily players | waits for the key |
| 5 | Sample-ratio alarm level | p < 0.0005 (Microsoft; the paper) / p < 0.001 (other vendors) | 0.0005 | 0.0005 |
| 6 | After approval: update the other roles' files that still say "analyst (planned)" (marketing hand-offs, testing-measurement, trend-scan hand-offs, marketing launch timeline) | yes / no | yes (pointers only) | yes |
