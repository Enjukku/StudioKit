---
name: trend-scan
description: Run the trend scout's weekly market scan with the studio's data tools and write the weekly page - pull data only through official services used as their rules allow (Apple app charts, YouTube panel statistics), take in what the owner reads and pastes (RoTrends, SullyGnome, Roblox charts, Steam charts, Google Play, TikTok Creative Center, Instagram, Google Trends, Twitch), legal-only so no platform can ban the studio, keep the history, compute growth, breakout and fade flags with coverage, build the weekly page (Markdown + HTML charts) from the template, and hand off to the owner, the game designer and marketing. Covers the source-permission registry, keys in environment variables, storage limits (YouTube 30 days), formulas and their traps, manual-entry rules, the weekly steps, hand-off briefs, and the scout's own performance record. Use for "run the weekly scan", "update the trend data", "add this game to the watchlist", "what does the data say about X", "make the trend report". Read market-trends first (what the numbers mean); this skill is how. Never scrapes, never designs games.
---

> Author: orchestrator · claude-opus-5-5 · medium · 2026-10-21. Kit skill: universal. J004. Tools: `tools/trends/` (README there). Evidence: owner research paper (notes `knowledge/reference/trends/` 01, 02), fact-checks `fact-check-roblox.md` (**FR**), `fact-check-outside.md` (**FO**). All thresholds live in `tools/trends/config.json` and are **PROPOSAL**.

# Trend scan: pull, measure, write, hand off

## 1. When this skill starts
After `market-trends` (what each number means). Needs: the tools in `tools/trends/`, a watchlist at `<TREND_DATA_DIR>/watchlist.json` (copy `tools/trends/watchlist.example.json`), and any keys the owner has set. Nothing runs on a timer: the scout runs only when the owner asks (owner J004-D8).

## 2. Read this file when
| You need | Open |
| --- | --- |
| Which sources may run, how to read the manual ones, keys, storage | `references/sources.md` |
| Formulas, flags and when each number lies | `references/formulas.md` |
| The weekly page sections and columns | `templates/trends/weekly-report.md` |
| Briefs to the game-designer and marketing; asks into the scout | `references/handoffs.md` |
| Commands, store contract, record shape | `tools/trends/README.md` |
| What the numbers mean; loops; rights; the card | `market-trends` skill |
| Eval briefs for this role | `evals/briefs.md` |

## 3. Weekly steps
1. **Registry first.** `python tools/trends/trends.py registry`. Note every source that is not `allowed` and why; that goes in the page header (PERMISSION STATUS). *Check:* no tool is run for a refused source; Roblox automated reads stop after their `valid_until`.
2. **Collect allowed sources** (only those the registry allows). Our own growth numbers need samples **at most 60 min apart** (coverage gate, PROPOSAL), and the scout runs only on request (J004-D8), so our store holds snapshots: say so in the header. Two snapshots days apart give a "level then vs now" (DER, both times stated), never g7. Growth evidence comes from tracker history (RoTrends, SullyGnome) that the owner reads and pastes (legal-only mode, J004-D12). Run: `collect-apple`, `collect-youtube` (and `collect-steam` only after the owner rules it allowed). A refusal (exit 2) is reported, never worked around. *Check:* each run's record count and failures noted.
3. **Read manual sources by hand** (`references/sources.md` §2) into a CSV; `import-manual`. *Check:* 0 rejected rows left, or each rejection explained.
4. **Prune.** `python tools/trends/trends.py prune` (YouTube 30-day rule, pages included).
5. **Render data sections.** `python tools/trends/trends.py page`. It writes `trend-week-<date>.md` and `.html` with the measured columns, flags, coverage and charts. *Check:* coverage per game; flags held by the coverage gate are named.
6. **Fill the scout's sections** in a copy of `templates/trends/weekly-report.md` saved as `<data_dir>/pages/trend-week-<date>-scout.md`: 3 sentences, cards, loop families, outside trends, Steam and mobile, fading/rejected/wrong, rights flags, evidence ledger, scout performance. Use `market-trends` steps for each signal. *Check:* the 6-item self-check below.
7. **Watchlist upkeep.** Add rising games from the owner's standing chart read (R1) and from trackers by universe ID (`references/sources.md` §2 Universe IDs); keep the panel ≤ 50 games; add event windows you know of; remove nothing silently (moves go in the log).
8. **Hand off** (`references/handoffs.md`): owner + game-designer every week; marketing (role `marketing`, J012). Record cards and alerts in `<data_dir>/scout-log.md` (no YouTube API values), one row each: week · ID (universe / app / channel) · kind (card / lead / flag / watch) · claim · label · evidence (page section or URL) · decision or outcome · next check.

New watchlist games have no baseline: they show "emerging lead (n days)" until 2 full weeks exist. Say so; do not compare their first days with older games' weeks.

## 4. Craft core
| ID | Practice | Evidence |
| --- | --- | --- |
| S-01 | **The registry decides, not the HTTP code.** Only `allowed` rows run; `valid_until` ends a ruling; manual rows only by hand | FR §1, FO §3 O |
| S-02 | **Gaps stay gaps.** No backfill, no straight-line bridge, coverage printed with every window | N1 §8 O |
| S-03 | **Same panel, same definitions, every week:** same countries, channels, queries, chart and region; a change is logged and breaks comparison | N2 §5 O |
| S-04 | **Read time on every manual figure**; tracker means move live (FR K11-K13) | FR §3 V |
| S-05 | **One table per platform; no cross-platform sums** | N2 §5 O |
| S-06 | **Flag, then explain:** every breakout or fade flag gets featuring/ads/event/creator-video checks before it reaches a card | N1 §8 O |
| S-07 | **Report your own misses:** false alerts, missed breakouts found later, lead time, without hindsight | N2 §11 O |
| S-08 | **Pages are working copies:** every page is deleted 30 days after its last change; the scout log (`<data_dir>/scout-log.md`) keeps only IDs, dates, labels and decisions, never YouTube API values, and is never pasted from page sections | FO YT-03 V |

## 5. Rules (final check, short)
- No scraping, no browser automation on sites that forbid it, no login or CAPTCHA bypass, no account or key creation, no paid data. Keys only from environment variables.
- No personal data: no viewer data, no usernames, creators by channel ID only.
- Every number labelled (OFF, 3P-S, 3P-E, DEV, DER, MAN, UNKNOWN); revenue and playtime of other games are estimates with accuracy UNKNOWN.
- Thresholds are PROPOSAL; never present a flag as a prediction.
- The scout ranks research priority; it never designs, approves or commits budget. Own-game player data belongs to the analyst.
- Never name a file report*, summary*, findings* or analysis*.

## 6. Self-check before returning
- [ ] Registry state and every refusal are in the page header.
- [ ] Every number has a label, window and read time; momentum is never called weekly growth.
- [ ] Coverage shown; flags held by the gate are named; young games are "emerging leads".
- [ ] Each card: 9 record fields, loop line, twist as a decision change, rights/policy gate, score range + completeness, smallest test, kill condition.
- [ ] Last week's cards and flags are in "fading, rejected and wrong"; the scout log is updated.
- [ ] `prune` ran; no key, username or personal data in any file.

Project overlay: if `knowledge/overlays/trend-scan.md` exists, read it after this file; it wins for this game.
