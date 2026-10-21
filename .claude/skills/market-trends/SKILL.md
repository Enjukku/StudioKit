---
name: market-trends
description: Read the Roblox market and outside trends honestly - what is rising early, growing core loops, trends that may move into Roblox, "proven loop + new theme + twist" opportunities, copying a loop vs expression. Use for "what's trending", "is this game rising", "is this loop saturated", "can we copy this", "why now". Never invents numbers; trend-scan is the how.
---

> Author: orchestrator · claude-opus-5-5 · medium · 2026-10-21. Kit skill: universal. J004. Evidence: owner research paper (notes `knowledge/reference/trends/01-roblox-data-loops.md` **N1**, `02-outside-access-scoring.md` **N2**), fact-checks `fact-check-roblox.md` (**FR**) and `fact-check-outside.md` (**FO**), 2026-10-20/21. Tags: **V** checked fact, **E** developer/creator statement, **O** method (OPINION). Every threshold is **PROPOSAL** until backtested or owner-approved.

# Market trends: what is rising, how sure we are, and what is free to use

## 1. When this skill starts
Someone needs market evidence: the weekly scan, a "why now" for a pitch, a check of a game, loop or outside trend, or a rights screen on an idea. It answers: what players are doing more of (with dates and labels), which loop it runs on, whether it is rising, steady or fading, whether the studio can still enter in time, what may be borrowed, and which 3 research opportunities are best supported. `trend-scan` is how the data is pulled and the report is built.

## 2. Read this file when
| You need | Open |
| --- | --- |
| The 7 labels; what each Roblox counter, chart, tracker figure and money fact means; checked numbers | `references/signals-and-metrics.md` |
| The loop line, 8 loop fields, families with dated evidence, proven loop + twist cases | `references/loops.md` |
| The chain from outside trend to Roblox, dated cases, what each platform's number means | `references/outside-trends.md` |
| What may be borrowed, Roblox IP and discovery tests, the rights gate per card | `references/copying-and-rights.md` |
| Gates, score with UNKNOWN ranges, the research card, timing, "too late" | `references/opportunities.md` |
| Formulas (g7, momentum, coverage, playtime estimate, half-life) and when they lie | `trend-scan/references/formulas.md` |
| How the game-designer uses your records | `game-concept/references/idea-method.md` §2, §5 |
| Anything players buy, roll, trade, watch; age; ads | `platform-policy` skill |

## 3. Steps (judging one signal)
1. **Name it exactly.** Roblox: universe ID (+ root place). Outside: platform + exact ID (channel ID, hashtag, sound ID, app ID). *Check:* no title-only identity.
2. **Label every number** (OFF, 3P-S, 3P-E, DEV, DER, MAN, UNKNOWN) with its window and read time. *Check:* no unlabelled number.
3. **Growth, not size.** Non-overlapping weeks with coverage; added players next to percent; troughs; momentum only as momentum. Young (< 14 days of our data) → "emerging lead". *Check:* no momentum called week-over-week.
4. **Alternative explanations.** Featuring, ads, an event, one creator video, a holiday, an update. Name them before calling it a trend.
5. **Find the loop.** Write the loop line and the 8 fields with confidence; separate theme from mechanic. With only a title, page text or tracker row, still write the loop as a **hypothesis** ("loop hypothesis from title/description, not observed") plus the check that would confirm it (watch recent gameplay). Identity needs an ID; a loop hypothesis does not.
6. **Breadth.** Independent games on the same loop growing; independent creators on the same topic; 2+ platforms. One source → "single source".
7. **Timing.** Is the early window still open (dated mass adoption already? many Roblox copies already?). Slack = window − high-case build − learning time; qualitative until the owner sets a threshold.
8. **Rights gate** (`copying-and-rights.md`) and policy gate (`platform-policy`).
On day 0 or with less than 14 days of history, steps 3-7 cannot be done: list them as "not checked" with what is missing, and use the emerging-lead form.
9. **Card, emerging lead or watch.** Gates → score with lower/upper range → research card, watch, or reject (`opportunities.md`). At most 3 cards a week.

## 4. Craft core
| ID | Practice | Evidence |
| --- | --- | --- |
| M-01 | **A label on every number.** Official, sampled, estimate, statement and derived numbers are never mixed in one column or one sentence without labels | N1 §1-2 O; owner 2026-10-20 |
| M-02 | **CCU is not users; visits are not players; ranks are not money.** No fixed multiplier from CCU to daily users or dollars | N1 §1 O; FR §2 |
| M-03 | **Other games' revenue and playtime are estimates** (3P-E, vendor, range) with **accuracy UNKNOWN**; no tracker model has been validated against owner actuals | N1 §5; FR TR2, TR4 V |
| M-04 | **Growth over non-overlapping weeks with coverage.** 24 h ÷ 7 d is momentum, not weekly growth. Show added players next to %, and coverage | N1 §8 O |
| M-05 | **A peak is the highest recorded sample.** Compare matched weekdays and troughs, not a live count against an event record | FR TR1 V; N1 §8 O |
| M-06 | **Discovery now looks at 28 days, per user.** A short spike does not rank; Top Trending = more time spent over 2 weeks, not money | FR C02, D01-D04 V |
| M-07 | **Track loops, not names.** Loop line + 8 fields; theme ≠ mechanic; one game in one primary family | N1 §11-12 O |
| M-08 | **A twist changes a decision.** A new noun on the same assets is not a twist; a twist alone does not guarantee staying power (Grow a Garden 2) | N1 §13 O; FR K15 V |
| M-09 | **Breadth beats one spike:** independent games, independent creators, 2+ platforms, rising troughs | N1 §8, N2 §5 O |
| M-10 | **Outside trends: speed, not stock.** Lifetime hashtag views and a song's total plays are stock; measure additions and new derivatives in equal windows | N2 §5 O |
| M-11 | **Dates have kinds:** announced, released, first observed, broke out, peaked. Lags are single-case upper bounds; no universal lead time | N2 §1-2 O; FO CS |
| M-12 | **Too late is a timing claim, not "no demand".** Durable families still carry original games with current evidence | N2 §8 O |
| M-13 | **Borrow the abstract loop, never expression.** Unknown rights = HOLD, not a small minus | FR I01-I05 V; N2 §9 O |
| M-14 | **Gates before score; UNKNOWN is a range, never a neutral 3**; a score is not a probability | N2 §9 O |
| M-15 | **Three cards, never three green lights;** "no qualified opportunity" is a valid week; last week's wrong calls are reported | N2 §10 O |
| M-16 | **Research priority, not a pick.** Order cards by evidence quality (non-overlapping growth > momentum > one snapshot), then breadth (independent games, creators, platforms), then completeness; ties go to the smaller build. Write "research priority", never "best path" or "recommended build" while a gate is open | lead rule after J004 evals |

## 5. Rules (final check, short)
- Never invent or recall a player count, date, rank or revenue: pull it, read it, or write UNKNOWN. Do not infer who made a source work (creator, fan, studio) unless the source says so. A tracker with no named vendor is "vendor not given".
- Only allowed access (registry `tools/trends/sources.json`): no scraping, no login bypass, no CAPTCHA; manual sources by hand only. No data collection from Roblox's own services or roblox.com pages at all (owner J004-D10); Roblox game numbers come only from what the owner reads and pastes (legal-only mode, J004-D12).
- No personal data: creators by channel ID only; no viewer data; no inferred ages.
- Franchise, creator, meme, song or other-game identity: HOLD without a licence. Anything players buy, roll, trade or watch: `platform-policy`.
- The scout proposes research priority; the game-designer designs; the owner decides. Thresholds are PROPOSAL.
- Keep the analyst's own-game data separate; never mix it into market numbers.

## 6. Self-check before returning
- [ ] Every number has a label, a window and a read time; every UNKNOWN is written as UNKNOWN; every derived figure carries its formula and assumption in its own row.
- [ ] No "probably real" or "likely" verdict while a gate or check is open: write what is open instead.
- [ ] Created dates (API or tracker) are never called launch dates; CCU differences are "average concurrent players added", not new players.
- [ ] No momentum called growth; no CCU turned into users or money; peaks called "highest recorded sample".
- [ ] Each rising item names its alternative explanation and its breadth (independent sources).
- [ ] Each card has the 9 record fields, loop line (observed or labelled hypothesis), an original theme direction, twist as a decision change visible to a new player in the first session, its main doubt, rights and policy gate, score range with completeness, smallest test and kill condition.
- [ ] Last week's cards and calls appear in "fading, rejected and wrong".

Project overlay: if `knowledge/overlays/market-trends.md` exists, read it after this file; it wins for this game.
