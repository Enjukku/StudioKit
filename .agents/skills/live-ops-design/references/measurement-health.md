> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `live-ops-design`. Evidence: notes `02` §3-4 (LP:338-399), Roblox fact-check FR-06, FR-26..FR-34, FR-46. The analyst owns metric definitions, designs and verdicts: `analysis-design/references/experiments-updates.md` (§6 verdicts, §7 updates and events) and `metrics-roblox.md`. This file says what live-ops must bring to the analyst and how it decides after. Tags: V · E · O. Revised by J018 maker live-ops-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (§4 promise, tier and identity rows).

# Measuring an update, failing safely, long-term health

## 1. Roles (O)
The **analyst** owns metric definitions, data quality, design, analysis and uncertainty. **Live-ops** owns the decision hypothesis and reads the result with the analyst (LP:340). Live-ops never states a lift, a cause or a "win" the analyst has not given.

## 2. Predeclare before release (paper rule 10)
In the update brief, agreed with the analyst before release: target population · exposure or assignment definition · primary outcome (matching the mechanism) · guardrails · baseline · comparison design · observation windows · decision rule. A returner event is judged on **qualified reactivation and later play**, not total DAU (LP:340).

- **Reactivation (O).** Choose an inactivity window L from the game's behaviour (no universal L). Rate = eligible lapsed players who returned in the window ÷ all eligible lapsed players in the stated denominator: all lapsed accounts, contacted accounts, notification recipients or experiment assignments are different questions (LP:342).
- **Retention.** D1, D7, D30 are observation windows, not targets. Roblox's own retention page fills a cohort's D7 only after 7 days (FR-33). No mature D7 for immature cohorts. Report new, continuing and reactivated players apart (LP:344).

## 3. What each Roblox tool can show (V, read 2026-10-21)
| Tool | Can show | Cannot show | FR |
| --- | --- | --- | --- |
| Roblox's own event method: data vs the week before and after | a before/after description | a control group | FR-06 |
| Event analytics chart: up to 3 past events; 7 days before, 7 or 14 after | patterns and questions | causation (no control); which of 7/14 applies is not documented | FR-26, FR-27 |
| Experiments: 14-60 days; in-game config tests up to 2 variants + control; matchmaking tests up to 3 variants; random assignment at first `GetValue` | a causal effect of a config value | an event as such, unless the event is gated by a config value; anything in a game too small ("under 1,000 DAU might struggle") | FR-28..FR-31 |
| Early metrics (playtime, payer conversion, ARPU every 5 min in the first 24 h) | early harm | launch decisions ("Do not use them for launch decisions") | FR-30 |
| Configs: change values without publishing | timed content, safe switches | a rollback of saved rewards, migrations or trades | FR-32 |

**Design notes (O, analyst decides):** player-level assignment can leak when the change touches a shared economy, servers or friend groups. A global holiday event may have no clean simultaneous control: keep that limit visible. Compare assigned populations (intention to treat); track exposure separately; never drop unsuccessful participants after seeing results; never stop at a lucky moment; never change the primary metric after release; a non-significant result is not proof of no effect. If traffic is too low, do not run a test for a green dashboard: use instrumentation checks, usability research, a bounded rollout or a clearly labelled observational comparison (LP:348-352).

**Revenue (O).** Separate payer conversion, spend per payer, revenue per active user, total receipts and categories. Check displacement (new spend replacing old), pull-forward and dependence on a few large purchases. No guessed Robux-to-cash rate (LP:354).

## 4. Reading results: questions before verdicts (O, LP:356-363)
| Observation | Ask | Direction |
| --- | --- | --- |
| DAU rises, later return does not | new or lapsed players? qualified? did the core disappoint? | improve the landing and core before repeating promotion |
| Revenue rises, retention or fairness worsens | is spend concentrated? did urgency or power cause harm? | review monetization and guardrails; no unconditional win |
| Low event participation | did eligible players see and understand the entrance? is it accessible? | repair discovery and access before dropping the theme |
| High participation, completion collapses | where does progress stall: requirement, bug, skill, time, reward relevance? | fix that bottleneck; no blanket reward inflation |
| Event improves, core queues decline | did the event move existing play instead of adding value? | adjust schedule, integration or queues |
| Numbers move but data is inconsistent | version mismatch, missing events, assignment errors, delayed cohorts? | fix evidence quality; result "unknown" meanwhile |
| Players say the event was not what they expected | did the look, sound, UI or announcement promise something the activity did not give? | fix the mismatch in the next run's brief; re-theme the activity, not the lobby |
| Rare rewards get no reaction; common ones feel the same | are event rewards in the right tiers; did a frequent reward hold a high tier? | re-place the tier rows with the progression designer before the next run |
| Players did not recognise the variants | which anchors did the variants lose? | restore the anchors in the next variants; the art director's anchors list |

**Close with a decision (paper rule 15):** **repeat** (mechanism and cost support it) · **revise** (a specific fixable bottleneck) · **retire** (value too low or harm too high) · **investigate** (inconclusive). "Insufficient evidence" is a valid result. Record what would change the decision, and compare estimated with actual effort (LP:367). The analyst's five verdicts (`experiments-updates.md` §6) feed this decision; they are not replaced by it.

## 5. When an update fails (O, with V facts)
1. Stop ongoing harm under the authority agreed before launch.
2. Keep logs and the deployed version.
3. Disable the broken feature when that is safer than reverting the build. A code rollback does **not** undo saved currency, trades, purchases or progress, and a restore can erase legitimate gains. Builders and the progression designer define the state-safe response **before** launch (LP:365).
4. Tell players the known scope; correct entitlements through supported means.
5. Never promise refunds: creators cannot give Robux or money refunds; players go to Roblox Customer Support (FR-46, V).

## 6. Long-term health (O unless marked)
- **Economy.** Roblox's economy page links sources, sinks and reward value and warns that a generous event can leave a currency surplus and lower later spending; its fishing example is fictitious, and its safest suggestion is an event-only currency spent in an event shop. It gives no safe multiplier (FR-34, V). Every reward amount, issuance range and abuse case (alt accounts, automation, trading, stacking bonuses) comes from the progression designer (`progression-design`). A per-player cap does not cap total supply when accounts multiply (LP:380).
- **Inflation is about prices and purchasing power,** not balances. A fixed-price shop suffers lost scarcity or exhausted demand instead. The fix may be better goals or optional desirable sinks, not higher prices (LP:382).
- **Protect existing progress.** Prefer new choices, expression and situational use over raw power that obsoletes old content. If power must grow, the progression designer states how difficulty, matchmaking, returner access and earlier purchases adapt. Never sell a paid advantage as the fix for a difficulty spike the update created (LP:384).
- **Three player groups.** New players need a short path to the main appeal. Veterans need mastery, identity and respect for past effort. Returning players need an explanation of changes, a clear next goal, basic competence restored and access to social play: optional recaps, guided loadouts, simpler prerequisites, earnable catch-up, not every missed tutorial at once (LP:386; Overwatch, Clash Royale in `cases.md`).
- **Player burnout** shows as falling voluntary play, abandoned stacked chores, avoided claim routines, feedback about pressure: signals, not diagnoses. Cut simultaneous chores, allow breaks and late entry, keep optional play optional. Never stretch sessions by making tasks slower (LP:390).
- **Studio burnout (AI studio).** Owner review overload, endless exceptions, piled-up defects, a growing maintenance surface. More plans can overload the owner faster than code adds capacity. Track support load, escaped defects, rework and estimate accuracy beside content output. A reusable event framework must make each event cheaper to run; if every event adds unique infrastructure, it has not (LP:392).
