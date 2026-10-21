# Diagnosis: why players leave, stall, spend or stop

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `analysis-design`. Sources: owner's analyst paper (AP) §3, §4, §7 and Appendix A, extracted and fact-checked in `knowledge/reference/analyst/03-practice-diagnosis-reporting.md` (PR and C ids, live reads 2026-10-21) and `01-roblox-platform-facts.md` (RF ids). Tags: **V** documented · **E** reported by a studio or person, never a rule · **O** the paper's or studio's practice.

## 1. Turn "players are leaving" into a measurable symptom
"Players are leaving" is not a question yet (O, AP:149). Name which of these it is; each needs a different search:

| Symptom | First metric | Often confused with |
| --- | --- | --- |
| fewer arrivals | acquisition impressions, plays by source | a 2026-10-12 recording change |
| more join failures or crashes | crash count and rate, OOM exits, by device and place version | voluntary quitting |
| shorter sessions | session length by new vs returning | many new players arriving |
| fewer repeat sessions | sessions per player | a holiday week |
| lower return on day N | mature D1/D7/D30 cohorts | immature cohorts, a source mix change |
| stalled progression | milestone reached within a fixed window, with non-finishers | finishers-only timing |
| loss of established players | returning DAU, late-funnel steps, content completion | content exhaustion vs a new wall |

A lower peak CCU can sit next to unchanged retention; falling average session length can come from a wave of new players, not a worse game.

## 2. Find where it starts, then who it hits
1. **Locate the first credible break in time** (calendar date), then check it against the build, config, event, marketing and measurement calendars.
2. **Compare stable segments** that exist before the change: acquisition cohort and source, platform and OS, place version, country or locale, new vs returning, earlier progress. Use only dimensions the metric really has (catalog). Segment counts must add up to the total; explain "Unknown" and "Other".
3. Two separate charts (platform, then source) cannot show a joint platform × source effect.
4. If the player mix changed, recompute the rate with the old mix (a standardized rate: `analytics.py stats mix`): label it "adjusted" and show it next to the raw rate (O, AP:151).

## 3. Competing explanations (write the table before you pick a story)
| Explanation | If true we would see | Evidence against it | Who acts |
| --- | --- | --- | --- |
| Promise mismatch from acquisition | early exits concentrated in one source after a campaign or thumbnail change | similar exits across untouched sources | marketing |
| Loading or device regression | join failures, FPS or memory change in one version or device group | matched devices stable; failure reproduces elsewhere | engineering, game designer |
| Players cannot find the next action | eligible players stall before an obvious step; playtest confusion | they understand it but cannot afford it | game designer |
| Progression wall | more attempts, time or shortfall at one milestone | players progress but do not want to return | progression designer |
| Content exhausted | completion then lower return among advanced players | early cohorts fall just as much | live-ops designer |
| Economy or offer frustration | shortfall, failed or undelivered purchases plus matching feedback | complaints from an unrepresentative group with no behaviour change | progression designer, game designer |
| Measurement changed | the break lines up with a logging or pipeline change; independent measures disagree | the break persists in independent data | analyst, engineering |

(O, AP:153-163.) Look for the evidence *against* your favourite first. A finding that survives that search is worth reporting.

## 4. Funnels and progress
- Per step report: eligible entrants, completers, completion of those who reached the step, completion of all who started, time to complete, repeat attempts, unresolved (no terminal event yet) (O, AP:167).
- Rank fixes by **players affected × severity × evidence strength ÷ fix cost**, not by the biggest percentage drop: a small early drop can lose more people than a big late one.
- Keep five stages apart: **shown → eligible → attempted → succeeded → reward delivered**. A shop is not judged from buyers alone; a boss is not judged from wins alone (O, AP:169).
- Optional steps and different valid orders: a strict linear funnel calls normal play "quitting". Repeatable activities: attempt-level funnels for usability, player-level outcomes for retention.
- **Count the players who did not finish.** Time-to-milestone from finishers only makes a hard feature look fast (only skilled players finish). Use a fixed follow-up window and report the share who reached it next to the timing. "Not reached by the cut-off" is not "never" (O, AP:171; survival methods for censored playtime: S8, `02-statistics-experiments.md`). Survival curves need raw per-player data; with aggregate data, use the fixed-window share.
- Roblox funnel quirks: first instance of a step only, skipped steps auto-complete, filters on step 1 only, grouped by entry date (V RF-39).

## 5. Causal words (the ladder)
| We may say | Only when |
| --- | --- |
| "it happened" | we measured a change |
| "linked to" / "associated with" | we compared groups with fair adjustments |
| "consistent with" | a mechanism fits and nothing we checked contradicts it |
| "caused about X for these players" | a valid experiment, or a strong causal design (`experiments-updates.md` §5) |

(O, AP:189.) Predicting who will quit does not say what would keep them. A feature used mostly by loyal players may be a sign of loyalty, not its cause. When the mechanism is unknown, say: "we found where players are lost; we have not found why".

## 6. Player voice and observed play
- **Sources are filtered differently** (O, AP:348): in-game surveys only reach players who stayed long enough to see them; Roblox ratings come from players who chose to rate; Discord favours community regulars; social posts include onlookers and copies. Use authorized data only, minimal identifiers.
- **Count people, not comments**: theme rate = contributors who raised it ÷ contributors we heard from, in this source and window (the counting tool is `tools/liveops/feedback_count.py`, owned by the live-ops designer: reuse its counts, do not recount by hand). Where identity cannot be resolved, say "comments", not "players". Silence is not approval; quiet players are not happy players by default (O, AP:356; PR-R14).
- **Codebook** (versioned): topic, feature or stage, sentiment, report type (bug, comprehension, difficulty, fairness, preference, request), severity, evidence span, confidence, unknown/other. A comment can carry several themes. Keep the raw wording and source id; every summary points to exact examples. Keep the request ("double rewards") apart from the need ("progress feels stalled") (O, AP:352).
- **AI coding**: humans label a varied sample first (languages, devices, positive, negative, neutral, rare severe problems); compare the model's labels; fix the codebook; then bulk-code. Check per theme how often a label is right and how many real cases it caught. Never let a model invent a quit reason nobody wrote (O, AP:354). Roblox's AI feedback report is a lead to check, not a second source (V RF-53).
- **Observed play beats guessed reasons** (E): Riot combines surveys, analytics and lab studies (C15); a new champion's 36% release win rate climbed past 50% after about 35 games with it (C16-C17, one champion, sample not stated) — split by experience before calling a mechanic unbalanced. Valve treats designs as hypotheses and playtests as experiments; observers change behaviour, thinking aloud can interfere, averages hide extremes (C20-C23, second-hand reports of the 2009 talk). Ubisoft Toronto's research lead finds the gap between design intent and player experience; designers keep the fix (C25-C26). Microsoft's Halo study paired 7 months of data from 3M+ players with a 70-person survey (C28-C29; the "still need qualitative reading" lesson is the paper's inference, C30).
- **Playtests** (O, AP:185): recruit from the affected audience (new players, the right devices), not only staff, Discord regulars or big spenders; give a goal, do not coach, record what they do before asking why. A few repeated observations can justify a cheap usability fix; they do not measure how common the problem is.
- A severe reproducible bug deserves action even with few reports (O, AP:360).

## 7. Economy
- **Every coin must have a home** (O, AP:205): end stock = start stock + coins created (sources) − coins destroyed (sinks) + coins crossing the boundary + explicit adjustments (refunds, admin grants, resets, expiry, exploit reversals). Player-to-player trades cancel out across all players; market fees can be sinks; a currency exchange needs both sides. A change in which wallets are active changes the stock without anyone earning anything: reconcile it separately.
- Read sources and sinks **per active player and per hour of play**, wallets by tenure and progress, affordability of the next meaningful purchase, and how many players use each sink (O, AP:208).
- Average balance can rise because rich veterans are a bigger share, because players save on purpose, because a good sink vanished, or because of a duplication bug. A positive net flow is not automatically inflation: new players and new content can need more currency. Roblox's own heuristic (sources − sinks near zero; growing net → add sinks) is a balance hint (V RF-38), not a diagnosis.
- Traded economies: inflation = a fixed-quality basket of market prices rising with currency supply. Fixed-price shops cannot show price inflation; look at how fast rewards buy upgrades, inventory saturation, content skipping and lost scarcity (O, AP:210).
- **Questions for the progression designer** (O, AP:212): can an eligible non-payer afford the next intended step? how many active minutes and attempts does it take? are players spending on intended sinks, saving for an event, or stuck? which currency binds? do new rewards replace old ones? what happens after the first rebirth? Hand over one bottleneck and one test, never "add more sinks".

## 8. Purchases and payers
- Trace (O, AP:216): eligible → saw the offer → understood the value → prompt → confirmed purchase → benefit delivered → later use and return. Keep cancel, failure, not enough currency, policy restriction and delivery error apart where visible. A prompt is not a purchase; a client message is not a settled sale.
- First-time vs repeat payers by status *before* the period; report payer count, purchase frequency, basket, product mix, concentration and revenue per eligible player. Higher ARPPU can mean small spenders left; higher conversion with lower ARPPU can still be better (O, AP:218).
- **Never judge a price test among buyers only**: the change can change who buys. Compare all eligible players.
- King's discount experiment (E, PNAS 2016, 14M+ players, 9-70% discounts on large bundles of an unnamed game): revenue barely moved in three arms, the deepest-discount arm earned about 10% less (extract; verify before quoting), and almost all change came from people who already bought; buyers used big bundles fast rather than stockpiling (C09-C13). Lesson for Roblox: a discount's units sold is not the goal; check revenue, new payers, later spend and retention. Not an elasticity to copy.
- Roblox price optimization needs about 60,000 transactions in the previous 30 days in most cases; it re-tests at least every 90 days or sooner; a test takes about 3 weeks, then 4 weeks of review with 98% on new prices (V RF-30..31). Check for a running managed-price test before any other price change.

## 9. Fair monetization (constraints, never test variables)
- Paid random items (incl. Robux-funded currency and probability boosts): odds shown, summing to exactly 100% with the documented rounding note; per-player `PolicyService` restrictions respected (V RF-32; `platform-policy`).
- Clear offers, accurate prices and benefits, reliable delivery, a real path for non-payers; watch regret, frustration and return. No pressure aimed at vulnerable or young players; a revenue lift never excuses a misleading offer (O, AP:228).
- Supercell (E, C02-C05, interview 2026-09-01): retention is the main metric "most of the time"; players are told up front that tests run; players who miss the better variant get a make-up event later; under 100 A/B tests a quarter company-wide (about 10-20 per game). Lesson: in a shared Roblox world, unequal rewards touch friendships, competition and trading; a private shop-layout test and a server-wide currency test need different designs.

## 10. The diagnosis checklist ("players are leaving")
Run in order. PASS = the step was done and its evidence is recorded (a check that finds a defect is PASS, with the defect named); FAIL = the step could not be done or its evidence is missing: stop that inference and do the FAIL action. Keep the pull, the output and your judgment for each row (O, AP:495-513).

| # | Step | PASS when | FAIL action |
| --- | --- | --- | --- |
| 1 | Define the loss | outcome, population, dates, baseline, numerator, denominator named | rewrite "leaving" as a measurable question |
| 2 | Verify measurement | definitions stable, point status known, logging version known, totals reconcile, breaks marked | repair or bound the measurement first |
| 3 | Check maturity | compared cohorts have equal finished follow-up | wait, use mature cohorts, or label early signs separately |
| 4 | Check reliability | counts and uncertainty support the change; no unexplained missing segment | report "not enough evidence" and get the data |
| 5 | Check who arrived | source and new/returning mix; retained counts next to rates | recompute within comparable groups; do not blame onboarding yet |
| 6 | Check technical experience | joins, crash counts, FPS and memory tails by version and device | investigate those devices and builds; separate technical from chosen exits |
| 7 | Locate the break | eligible funnel denominators, unfinished attempts, time | name the missing measurement or look at sessions and playtests |
| 8 | Check progression | time, attempts, affordability, share reaching, non-finishers kept | test difficulty, clarity, resource shortfall and exhaustion separately |
| 9 | Check economy and purchases | sources, sinks, offer eligibility, delivery, fairness | reconcile currency and purchase flows before reading spend |
| 10 | Competing explanations | several mechanisms with predictions that could prove them wrong | write alternatives before recommending |
| 11 | Triangulate | behaviour agrees with observed play and feedback, or the gap is explained | recruit the affected players; look into the conflict |
| 12 | Bound the cause | wording matches the design (§5) | downgrade "caused" to "linked to", or design a test |
| 13 | One decision | one action with owner, players, expected mechanism, success measure, review date | return one next measurement or test, not a bundle of guesses |

A verified severe technical defect → recommend the repair now and keep the evidence; do not wait for a cohort to mature. Uncertain and costly → recommend the single most decision-relevant missing measurement or test. "Investigate everything" is not a recommendation (O, AP:513).
