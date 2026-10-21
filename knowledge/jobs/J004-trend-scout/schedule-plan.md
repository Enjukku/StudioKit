---
type: job
scope: universal
status: superseded
updated: 2026-10-21
source: J004 (owner: "A plan for running the scan every week automatically. Show it to me before setting anything up.")
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · medium · 2026-10-21

# Schedule plan: trend scan (NOT USED: owner chose on-demand runs only, J004-D8)

Replaced by the on-demand rule in [[jobs/J004-trend-scout/decisions]] (J004-D8) and `trend-scan` SKILL §1.

## 1. Why there are two schedules
Growth is measured from saved history. A scan once a week sees one moment, not growth. So:
- **Collectors** (plain Python scripts, no AI, no cost) take samples often and save them.
- **The weekly scan** (the trend-scout agent, Sonnet) reads the saved history once a week and writes the page.

## 2. What runs, how often
| Job | Command | When | Why this often |
| --- | --- | --- | --- |
| Roblox samples | `python tools/trends/trends.py collect-roblox` | every 15 min | the coverage gate needs samples no more than 60 min apart (PROPOSAL); 15 min leaves room for missed runs. About 6 requests per run for 30 games, far under the observed 300 per minute. **Stops by itself after 2026-10-31** unless you decide otherwise (digest: option A) |
| Apple app charts | `... collect-apple` | once a day | ranks move daily; the feed is made for daily download |
| YouTube panel | `... collect-youtube` | once a day | only after you set `YOUTUBE_API_KEY`; stays under the free quota |
| Prune | `... prune` | once a day | YouTube data and pages that show it must be gone after 30 days |
| Weekly scan | trend-scout agent: registry → collect → your manual readings → page → hand-off | Monday 09:00 (your time) | one page a week for you and the game-designer |
| Your manual readings | fill the CSV from the "owner reads" list on last week's page | before Monday's scan | TikTok, Instagram, Google Trends, Rolimon's (if consent), Steam charts and others may not be read by an AI |

## 3. Where it runs (options)
| Option | How | Good | Bad |
| --- | --- | --- | --- |
| **A. Your PC (recommended to start)** | Windows Task Scheduler runs the collectors; a Claude desktop scheduled task runs the weekly scan | free; data stays on your PC; keys stay in your user environment | samples stop while the PC sleeps or is off → gaps → the coverage gate holds flags. Set "wake to run" or accept gaps |
| B. On demand only | you say "run the weekly scan" | nothing to set up | no history between scans → no growth numbers, only snapshots |
| C. Small always-on server (later) | the same scripts on a cheap cloud machine | no gaps | monthly cost; keys and data on another machine; set up only when the data proves useful |
A cloud Claude routine cannot see the history on your PC, so it does not fit this design without moving the data.

## 4. What the Roblox decision changes
- **A (default):** collectors run until 2026-10-31 only. That gives about 10 days of Roblox history: enough for a baseline and daily numbers, **not enough for week-over-week growth** (needs 14 days). After that, Roblox numbers come from your own hand readings until Roblox answers in writing.
- **B:** no Roblox collector at all; the schedule is Apple, YouTube and your manual readings.
- **C:** the 15-minute collector keeps running after 2026-11-01 (not recommended).

## 5. Setup steps (only after your yes)
1. You copy `tools/trends/watchlist.example.json` to `.tools/trend-data/watchlist.json` (the first scan makes one for you).
2. Optional: you set `YOUTUBE_API_KEY` as a user environment variable (I give you the steps; you create the key; it never goes in a file).
3. I give you 4 `schtasks` commands (Roblox every 15 min, Apple, YouTube and prune daily) to run yourself, or I run them once you say so; each is shown before it runs. They are removed with one command each.
4. I create one Claude desktop scheduled task "Weekly trend scan", Monday 09:00, Sonnet medium (role default) with the weekly steps. You can pause or delete it in the app.
5. After 2 weeks we check: coverage %, gaps, cost, whether the page helped. Then keep, change or stop.

## 6. Cost and limits
- Collectors: no cost, a few seconds each.
- Weekly scan: one Sonnet session per week (medium effort by default).
- Your time: the manual readings; the page lists exactly which pages and fields, so you can skip any.
- Nothing posts, buys, signs up or contacts anyone.

## 7. Decisions for you
| Decision | Options | Recommendation | Default |
| --- | --- | --- | --- |
| Where | A PC / B on demand / C server | A | nothing set up |
| Weekly scan time | any | Monday 09:00 | Monday 09:00 |
| Weekly scan effort | medium (role default) / high | medium; raise if pages miss things | medium |
| Wake PC for collectors | yes / no | yes, if the PC is usually on at night | no |
