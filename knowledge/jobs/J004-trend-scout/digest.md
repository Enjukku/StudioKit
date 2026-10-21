---
type: decision
scope: universal
status: active
updated: 2026-10-20
source: J004
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · medium · 2026-10-20


# Decision digest: 2026-10-20 (J004 G1)

| Job | Decision | Options | Recommendation | Default if no answer | By when |
| --- | --- | --- | --- | --- | --- |
| J004 | G1: approve the job card and brief | approve / change | approve | nothing starts | G1 |
| J004 | Skill books | 2 books (`market-trends` design, `trend-scan` craft) / other names | 2 books as named | 2 books as named | G1 |
| J004 | Effort for extractors, fact-checkers, grader | Sonnet high (J003 precedent) / Sonnet medium | high: the fact-check decides what the tools may legally call | high | G1 |
| J004 | Report format | Markdown only / Markdown + HTML page with charts | both: Markdown for the game-designer, HTML charts for the owner | both | G2 |
| J004 | Optional keys | YouTube and Twitch keys from the owner (env vars) / skip those two sources | add later: build and test both offline now, the owner adds keys when ready | build now, run without keys | G2 |

# Decision digest: 2026-10-21 (J004, during step 2-4)

| Job | Decision | Options | Recommendation | Default if no answer | By when |
| --- | --- | --- | --- | --- | --- |
| J004 | Roblox data after 2026-11-01 (new Terms §9.2 ban automated data gathering "in connection with ... use of ... AI" and "harvest any Content or data ... for any purpose"). First scan (T08): with A, only 10 complete days remain, so no week-over-week growth can be measured for Roblox games before the stop | A: collector allowed until 2026-10-31 only, off from 2026-11-01; owner asks Roblox in writing / B: no Roblox collection at all until Roblox answers / C: accept the risk and keep collecting | A | A (collector stops itself on 2026-11-01) | before 2026-11-01 |
| J004 | Rolimon's (licence: "personal, non-commercial transitory viewing only") | ask Rolimon's for written consent / do not use it for studio decisions | do not use until consent; use RoVitals by hand (no ban on hand reading) | not used | G2 |
| J004 | Steam current players (terms name end-user display, not internal analytics) | accept / ask Valve (webapi@valvesoftware.com) / skip | skip for now; Steam charts by hand | collector stays refused | G3 |
| J004 | Twitch (API data may be kept 24 h only) | ask Twitch for written storage permission / read by hand | read by hand | by hand | G3 |
| J004 | YouTube derived-metrics approval (needed for history beyond 30 days and channel rankings) | apply / no | no for now | 30-day rolling data only | G3 |
| J004 | Google Trends alpha API | apply / no | optional; by hand works | by hand | G3 |
