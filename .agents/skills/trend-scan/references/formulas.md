> Author: orchestrator · claude-opus-5-5 · medium · 2026-10-20. Kit reference: universal (J004). Evidence: owner research paper, notes `knowledge/reference/trends/01-roblox-data-loops.md` (**N1**) §5, §8, §9 and `02-outside-access-scoring.md` (**N2**) §4-§5, §8, §11. All formulas are the paper's method (OPINION); all thresholds are **PROPOSAL** and live in the trends tool config, never in prose. The trends tool computes these; this page says what they mean and when they lie.

# Formulas: what the numbers mean

## 1. Time and windows
- Store UTC; report in the studio timezone; keep collector time (`observed_at_utc`) and source time (`source_sample_at_utc`) apart (RP:91).
- **Day** = complete UTC day; **week** = 7 complete UTC days. Partial days are excluded from g7 (lead rule; the paper leaves "complete days" open, N1 I8).
- **Gap** = two samples further apart than `max_gap` (PROPOSAL 60 min). Gaps stay gaps: no straight-line bridge, nothing backfilled and labelled observed (RP:93).
- **Coverage** = covered minutes / intended minutes in the window. Print it next to every windowed number. Under the coverage gate (PROPOSAL 90 %) no automatic breakout flag (RP:93).

## 2. Roblox counters
| Quantity | Formula | Unit | Label | Lies when |
| --- | --- | --- | --- | --- |
| Player-hours | trapezoids between adjacent samples closer than `max_gap`: Σ (ccu_i + ccu_{i+1}) / 2 × Δt_h | player-hours | DER from OFF | coverage is low; outages; idle accounts |
| Time-weighted mean CCU | player-hours / covered hours | players | DER | window holds an event spike |
| g7 | mean7(this week) / mean7(previous week) − 1, non-overlapping complete weeks | % | DER | coverage differs between the weeks; an event sits in one week |
| Added CCU | mean7(this week) − mean7(previous week) | average concurrent players (not new players) | DER | — (always show next to g7: +200 % of 5 players is noise) |
| Acceleration | g7(this week) − g7(last week) | percentage points | DER | needs 3 weeks of history |
| Momentum | mean(last 24 h) / mean(last 7 d); show both forms: "×3.34 (+234 %), overlapping windows" | ratio | DER | **overlapping windows: never call it week-over-week growth**; report the ratio only, never the difference of the two means |
| Trough | lowest daily (or matched-hour) mean in the window | players | DER | compare matched weekdays only |
| Mean / peak | mean7 / max sample in 7 d | ratio | DER | high = steady play; low = spiky (events, ads, a video) |
| Visits added | visits(end) − visits(start) | entries | DER from OFF | visits are entries, not people or sales |
| Playtime estimate | 60 × player-hours / visits added | minutes per entry | **estimate** | teleports, idle accounts, delayed counters; not session length; not retention |
| Approval | up / (up + down); undefined at 0 votes | % | DER | cumulative votes are dominated by old players: use votes added in the window |
| Favorites added | favorites(end) − favorites(start) | count | DER | not loyalty or retention |

**Zero or missing baseline** → status "new / insufficient baseline", never ∞ (RP:95). **Young game** (< 14 days of our history) → "emerging lead (n days)", daily numbers only (RP:97).

**Never** turn CCU into daily users, visits into players, or players into money with a fixed multiplier (RP:16, RP:113). Peak concurrent is not a typical day: a 99 % drop from a one-hour record to a weekday count is true arithmetic and a useless retention figure (RP:99).

## 3. Flags (PROPOSAL; config values, need backtesting)
| Flag | Rule | Then |
| --- | --- | --- |
| Breakout | g7 ≥ +50 % **and** added CCU ≥ +100 **and** 3 matched days in a row above last week's matched days **and** coverage gate passed | check: featuring, ads, an event, one creator video; look for independent creator uptake and rising troughs (RP:97) |
| Fade | 2 negative non-overlapping weekly changes in a row **and** a lower matched trough | check seasonality and rival releases; keep event peaks and event-free series apart (RP:99) |
| Trend start (for backtests) | first of 3 matched days above 2 × median of the 4 weeks before, with a minimum audience | for scout performance only (RP:347) |

A spike that falls back, flat troughs, or falling visit increments is weaker evidence than broad, steady growth (RP:97).

## 4. Outside sources
| Quantity | Formula | Lies when |
| --- | --- | --- |
| View velocity (fixed video cohort) | views added / hours elapsed; compare equal back-to-back windows; add the median of age-matched videos | old videos gain views without new creators; one channel dominates |
| Creator breadth | distinct channels posting the topic in the window; top channel's share | search returns a selected set, not every upload: "observed uploads in this panel" |
| Google Trends | index 0-100, relative to the peak inside that exact query | never "searches doubled"; 0 can mean too little volume; reruns rescale |
| App store rank change | positions moved, with store, country, category, chart, date | rank 100 → 10 is 90 positions, not +900 % downloads |
| Steam Top Sellers | rank by revenue, trailing 24 h, last 3 h weighted | ordinal only; no dollar growth from rank |
| Twitch | viewer-hours = Σ viewers × Δt; broadcaster count | raids and events; category ≠ a Roblox universe |

Hashtag lifetime views are a stock, not a speed. A large sound can be falling (RP:268).

## 5. Money (estimates only)
- Other games' revenue is **always** a third-party estimate (label 3P-E, vendor, range, method) or UNKNOWN. Its accuracy is UNKNOWN: no independent validation exists (RP:72). Never write "about X Robux per day" without the vendor and its range.
- Official signals: Top Earning chart rank with date (ordinal); official disclosures that name a game (OFF, in their scope).
- Owned game only: cash contribution and DevEx value come from the analyst's authorised data, not from the scout.
- A money scenario is labelled "scenario", never "forecast" or "profit" (RP:113).

## 6. Scout performance (RP:467)
- **Breakout (for evaluation)** = a studio-set sustained player-hour level over a stated number of days.
- **Lead time** = breakout time − time of our first qualifying alert.
- **Precision** = matured alerts that became breakouts / matured alerts.
- **Recall** needs a fixed candidate set and a later census; report it only with that set named.
- No hindsight: a backtest may not use a later peak, a later title or a later disclosure.
