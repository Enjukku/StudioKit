<!-- > Author: orchestrator · claude-opus-5-5 · medium · 2026-10-20. Kit template: universal (J004). Skills: market-trends (what each number means), trend-scan (how to fill it). Copy to <TREND_DATA_DIR>/pages/trend-week-<YYYY-MM-DD>-scout.md and fill it next to the tool-rendered trend-week-<YYYY-MM-DD>.md/.html (trend-scan §3 step 6). Delete these comments. -->
<!-- Labels on every number: [OFF] official · [3P-S] third-party sampled · [3P-E] third-party estimate · [DEV] developer statement · [DER] derived (formula named) · [MAN] manual entry · UNKNOWN (never 0). Quotes under 15 words. -->

# Trend week ending <YYYY-MM-DD> (UTC unless the game profile sets a studio timezone)

| Field | Value |
| --- | --- |
| As of | <exact timestamp, UTC and studio time> |
| Data coverage | <per window: covered hours / intended hours, %; watchlist size; days of history> |
| Permission status | <approved / limited / blocked, per source group; link to tools/trends/sources.json rows> |
| Decision asked | <approve bounded prototype / research ticket / watch / reject / none> |
| Previous week | <link to last week's file> |

## 1. This week in 3 sentences
1. <The biggest measured change in demand, with its number, label and window.>
2. <The loop + theme worth a closer look and its time window, or "no qualified build opportunity".>
3. <The one assumption that would reverse the recommendation if it is wrong.>

## 2. Top 3 opportunities (research priority, not build approval)
<!-- Fewer than 3 when fewer are defensible. Never pad. Each card = the game-designer's 9-field record + card fields. -->

### O1 <working title: original identity, no franchise or other game's name>
| Field | Value |
| --- | --- |
| Observation date | <YYYY-MM-DD> |
| Rising player behaviour | <what players do more of, in one line> |
| Proven loop | <loop line: action → reward → reinvestment → harder goal; returns because …> |
| New theme | <one line> |
| Twist (new decision) | <one line: the decision or consequence that changes> |
| Audience and device | <named cohort and devices; no inferred child profiles> |
| Evidence | <source, metric, window, number + label; at least 2 independent sources or "single source"> |
| Comparison period | <window vs window, non-overlapping> |
| Outside trigger | <event, season, meme, update, release; or none found> |
| Alternative explanation | <ads, featuring, an event, a one-off creator video, …> |
| Lasting or temporary | <lasting / temporary / unclear, and why> |
| Money | <official earning rank with date / developer statement / third-party estimate (range, vendor) / UNKNOWN> |
| Competition | <named universe IDs; close-substitute count and how they were found> |
| Rights and policy gate | <pass / HOLD / fail + reason (copyright, trademark, Roblox IP, platform-policy)> |
| Score | <known points; lower–upper range for UNKNOWN dimensions; completeness %; not a success chance> |
| Smallest test | <time/cost cap, success signal, stop condition, evidence still needed> |
| Decision owner, next review | <owner (creative) / game-designer (loop, scope); YYYY-MM-DD> |

### O2 …
### O3 …

### Emerging leads (not scored, not cards; form: market-trends `opportunities.md` §4b)
| ID and name | What was seen [label, window, read time] | Loop (hypothesis or observed) | Why it might matter | Missing evidence | Rights gate | Next check |
| --- | --- | --- | --- | --- | --- | --- |

## 3. Rising Roblox games
<!-- From the history store. g7 only with 2 full non-overlapping weeks; else "emerging lead (n days)". -->
| Game (universe ID / root place) | Loop family | Created [OFF] (not a launch date) / first seen by us | Latest sample playing [OFF] (UTC) | 7d mean CCU this wk / last wk [DER] | g7 % / added CCU [DER] | Accel. pp [DER] | 24h mean / 7d mean (momentum, not WoW) [DER] | 7d trough [DER] | Visits added [OFF→DER] | Favorites added [OFF→DER] | Approval % [DER] | Earning rank, date [OFF] | Revenue [3P-E or UNKNOWN] | Coverage % | Sources | Confidence and gap |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Breakout flags (PROPOSAL thresholds): <list or "none">. Fade flags: <list or "none">. Event or featuring this week: <list>.

## 4. Rising loop families
| Family (loop line) | 7d player-hours, panel [DER] | Share change vs last wk, same panel [DER] | Games growing independently | Leaders | New entrants | Theme or mechanic driving it | Saturation signs | Counter-example |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 5. Outside trends
<!-- One table per platform. Never add numbers across platforms. -->
| Platform | Topic (exact ID: channel, sound, hashtag, app) | First dated source | New derivative this week | Region / language | Measure, window, denominator [label] | Velocity | Roblox adaptation seen (universe IDs) | IP route | Window estimate and doubt |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 6. Steam and mobile watch
| App ID / store + country | Demo or full | Rank (definition, date) [OFF] | Current players or licensed estimate [label] | Repeated player behaviour | Touch and co-op fit | Roblox competitors (universe IDs) | Next check |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 7. Fading, rejected and wrong last week
| Earlier claim (week, ID) | New evidence | Source / correction | Why the reading changed | Action (stop / update / keep watching) |
| --- | --- | --- | --- | --- |

## 8. Rights and policy flags
| Item | Risk (copyright / trademark / Roblox IP / discovery originality / platform-policy) | Status (pass / HOLD / fail) | Evidence |
| --- | --- | --- | --- |

## 9. Evidence ledger (appendix)
| Claim ID | Label + provenance | Metric and unit | Period | Observed at | Source sample at | Published / effective date | URL or store row | Quote (< 15 words) | Assumptions | Doubt | Storage expiry | Next check |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 10. Owner reads requested for next week
| ID | Source and page | Region | Window | Fields | Priority |
| --- | --- | --- | --- | --- | --- |
| R1 | Roblox charts: Most Popular, Top Trending, Up-and-Coming (top 50, game URLs) | your country | now | rank, game URL | standing |

## 11. Scout performance
| Alerts matured | False alerts | Breakouts missed (found later) | Lead time before breakout | Decisions changed | Access or policy failures | Method fix for next week |
| --- | --- | --- | --- | --- | --- | --- |
