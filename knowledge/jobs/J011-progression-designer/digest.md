---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J011 G1
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Decision digest: 2026-10-21 (J011 G1)

| # | Decision | Options | Recommendation | Default if no answer |
| --- | --- | --- | --- | --- |
| 1 | G1 for J011 (`job-card.md`, `brief.md`) | approve / change | approve | waits for your answer |
| 2 | When J011 runs. Several L jobs are open (J002, J003, J005, J008, J009, J010); the company limit is 2 concurrent L jobs | (a) start now: extraction, fact-checks, tools, skills; G2 is the worked examples, which need no other job; (b) wait for a free slot | (a): steps 2-5 are Sonnet and tool work; nothing waits on another job | (a) |
| 3 | Skill names | `progression-design` + `progression-craft` (kit pattern) / other | `progression-design` + `progression-craft` | `progression-design` + `progression-craft` |
| 4 | Numbers the paper does not give (earning rates, session lengths, enemy stats) in the worked examples | (a) use published inputs where they exist (the paper's idle-game and XP-table models) and label every other input `EXAMPLE ASSUMPTION` in the data; (b) keep the RPG timeline symbolic, as the paper does | (a): you asked for a minute-to-month timeline with charts; the label stops anyone copying the numbers as tuning | (a) |
| 5 | First-game economy material | (a) read DestructionSimulator's economy, gear, pets, stage-strength, telemetry and decisions files read-only, keep universal lessons only; (b) paper only | (a): your own economy rulings are the best cases; game names and numbers are removed | (a) |
| 6 | Chart format | (a) one self-contained HTML file with SVG charts per run, standard library, opens in any browser; (b) PNG with matplotlib (needs a package) | (a): no install, opens offline, readable on a phone; I can also publish one as a private page for you to view | (a) |
| 7 | Split with `game-design` (it already has an economy section and a systems check) | (a) game-design judges the design; progression-design owns the math, timelines, simulation and tables; pointer lines both ways; (b) move the economy section into the new books | (a): smallest change, no copies | (a) |
| 8 | Effort for the Sonnet helpers (extract, fact-check, grade) | high / medium | high, as in J004-J009 | high |
| 9 | Analyst and live-ops designer are planned, not built | hand-off briefs name them; until they exist, the lead routes the ticket | as stated | as stated |

# Decision digest: 2026-10-21 (J011 G2)

| # | Decision | Options | Recommendation | Default if no answer |
| --- | --- | --- | --- | --- |
| 1 | G2: the new agent's first real work (the two worked examples, `tools/progression/examples/`) and its hidden-eval answers | approve / change | approve; the grader passed the examples 8/8; hidden evals 14 pass, 8 partial, 1 fail, and the missed steps are now in the self-checks | waits for your answer |
| 2 | Reference fix in the incremental example | A keep as is · B rising Replant requirement · C new content at Replant 10 | B: one number fixes the weak late loop (20 bigger Replants instead of 40 tiny ones) | B |
| 3 | Reference fix in the RPG example | B late assist for struggling players · C new weapon (needs a re-tune) | B now, C after a re-tune | B |
| 4 | Commit the example run files (2.9 MB, needed so anyone can re-check the charts byte for byte) | commit / keep only models and charts | commit | commit |
| 5 | Stale lines found in `platform-policy` (8) and `analytics` (4) by the Roblox fact-check (for example: six restricted-player treatments, not four; the trading flag covers all paid items) | fix now in a separate small kit job / later | a separate small job, edited by the lead | separate job |
| 6 | Remaining small tool gaps G-16..G-20 (lean plots, a hard-wall goal, wall kinds, options chart size) | fix before G3 / after the first real game job | after the first real game job: none blocks use | after |
