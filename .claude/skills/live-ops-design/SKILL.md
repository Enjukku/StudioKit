---
name: live-ops-design
description: Decide what a live Roblox game should do next and why - updates, events, seasons, limited-time content, new features and fixes - so players keep coming back and the game keeps growing, from evidence (the analyst's numbers, player feedback counted by distinct players per theme, the trend scout's dated signals) and inside the studio's real capacity. Covers the evidence contract, fixing harm before adding content, update rhythm vs capacity (Roblox's weekly / two-weeks-to-a-month / season guidance read in context), content types and the player problem each solves, events (entrance, activity, rewards, honest end, catch-up), honest urgency and Roblox's offer-presentation rules, notifications, announcements, paid random items, younger players and age bands, loud vs silent players, measuring with the analyst (observational vs Roblox Experiments), failing safely, economy, catch-up and burnout, and cases from durable games. Use when a game is live and the owner asks "what should we update next", "plan an event", "plan a season", "players are bored", "Discord wants X", "did the event work", "should we do a limited-time offer". Read by the live-ops designer first; game designer, progression designer, marketing and analyst read it for the shared rules. Proposes; the owner decides.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit skill: universal. Built in J014 from the owner's live-ops research paper (2026-10-21; VERIFIED / EXPERIENCE / OPINION tags kept) and its fact-checks (`knowledge/reference/live-ops/`: notes `01`, `02`; `fact-check-roblox.md` FR ids; `fact-check-cases.md` FG ids; `feedback-routes-fact-sheet.md` Q ids; all read 2026-10-21). Tags: **V** platform-documented · **E** someone's reported result, never a forecast · **O** the paper's or the kit's proposal.

# Live-ops design: what the game does next, and why

Live ops keep a renewable relationship between players and a game: a reason to return, an easy way to take part, a good experience on arrival, and confidence that what they built still matters. Novelty brings attention; reliable play, fair progress, friends and a credible future turn attention into continued play. An update is a means to that relationship, not the goal (LP:39, O).

## 1. When this skill starts
When a game is live, at every decision period (default: a weekly evidence review, which is **not** a weekly release, LP:433), after an incident, and when the owner asks what comes next. It answers, in order:
1. **Is anything harming players now?** Lost progress, failed purchases, safety, broken access, severe instability, exploitable currency. That goes first, to its owner, outside any ranking.
2. **What is the binding problem?** For which players, on what evidence (analyst + feedback + trends), with which other explanations.
3. **What is the smallest change that could remove it,** and what does it cost to build, test, support and keep?
4. **How will we know?** Predeclared with the analyst.
5. **What may we not do?** Roblox rules, younger players, the studio's capacity, the owner's gate.

How to run the cycle, fill the templates and brief other roles: `live-ops-craft`.

## 2. Read this file when
| You need | Open |
| --- | --- |
| Roblox's rhythm guidance, choosing a rhythm, capacity, content types, season pass, retirement | `references/cadence-content.md` |
| Events, honest urgency, announcements and notifications, Roblox rules on offers, paid random items, ages | `references/events-offers-rules.md` |
| The evidence contract, feedback sources and their populations, sorting, counting, loud vs silent, closing the loop | `references/evidence-feedback.md` |
| Measuring with the analyst, Roblox tools and their limits, reading results, failing safely, economy, catch-up, burnout | `references/measurement-health.md` |
| What durable games teach, with what not to copy | `references/cases.md` |
| Metric definitions, designs, verdicts | `analysis-design` (analyst) |
| Reward amounts, curves, economy simulation | `progression-design`, `progression-craft` |
| Loops and live-content design review | `game-design` (`references/playtest-live.md` §4-5) |
| Announcements, voice, store page | `marketing-design` |
| Policy code patterns (odds table, PolicyService, receipts) | `platform-policy` |
| Trend labels | `market-trends` |

## 3. Steps (the decision)
1. **Protect.** Route urgent harm to its owner now (incident request). *Check:* nothing urgent sits inside a ranking.
2. **Diagnose.** Name the constraint; separate symptom from cause; write other explanations. Never diagnose "not enough content" from a falling DAU chart alone: weak core loop, friction for arriving players, unreachable content, exhausting progress, costly return, competition, season, discovery change or a technical regression are all candidates (LP:41). *Check:* the analyst confirmed the denominator.
3. **Generate options** across improve / add / simplify or remove / communicate / investigate, all for the same player objective (LP:443). *Check:* each has a mechanism and fits the core game.
4. **Estimate.** Builders give effort and lead time, the progression designer gives economy feasibility, marketing gives channel limits. *Check:* no date, lift or licence assumed.
5. **Rank** by evidence, reach, reversibility, cost and fit; show the recommended option, a cheaper alternative and what is deferred, with counter-evidence and opportunity cost (`cadence-content.md` §3, craft `process.md`). *Check:* exactly one recommendation.
6. **Owner decides.** Silence is not approval. *Check:* decision recorded with the owner's words.
7. **After release, decide again:** repeat / revise / retire / investigate (`measurement-health.md` §4).

## 4. Craft core (what separates great live ops from weak)
| ID | Practice | Evidence |
| --- | --- | --- |
| L-01 | **Fix harm before buying attention.** A verified blocker in the existing game beats more content players cannot enjoy; a small paid-entitlement failure can outrank a large cosmetic complaint | O: paper rules 4, LP:214-216 |
| L-02 | **Rhythm = what players need × what the team can sustain.** Roblox's pages say weekly is ideal (monetization), every two weeks to a month (content cadence, under three weeks' effort each), a month for a season: different scopes, all recommendations. Never average them; never promise a public cadence without a credible minimum release behind it | V: FR-01..FR-07; E: Adopt Me moved from fixed Fridays to announced times, naming team and player wellbeing (FG-01) |
| L-03 | **Name the player problem before the content type.** "Add a season" is packaging. No source gives a portable lift for any content type | O: LP:131; OQ-01 |
| L-04 | **Hypothesis form:** for <cohort>, <problem> prevents <behaviour>; changing <cause> should improve <metric> through <mechanism>, without harming <guardrails>. Each clause has evidence or says "uncertain" | O: LP:218 |
| L-05 | **No fake precision.** Impact = reach × justified effect with its uncertainty; otherwise "unknown; test required". Never turn low / medium / high into decimals and rank on them | O: LP:220 |
| L-06 | **Count players, not messages.** Distinct authors per theme, per source, per window, with the count tool; messages are intensity; a Discord share is never "% of players" | O: paper rule 8; `tools/liveops/feedback_count.py` |
| L-07 | **Loud is not wrong, silent is not happy.** Weigh severity and reproducibility with prevalence; check silent cohorts in behaviour data | V: Roblox warns community feedback may be biased (FR-49); O: LP:262 |
| L-08 | **Events: entrance, activity, rewards, an honest end, a late-start path.** Length from observed play and team coverage; no optimum exists | O: LP:163-167; OQ-03; V: Roblox's "best events run 7-30 days" is guidance (FR-15) |
| L-09 | **Truthful urgency only.** Roblox requires genuine, fair discounts and forbids false scarcity and lying or restarting timers; it recommends calm wording with minors and forbids dark patterns in notifications. Truthful limited-time content is allowed and even recommended | V: FR-54, FR-55, FR-57, FR-19 |
| L-10 | **Predeclare with the analyst:** cohort, primary outcome matching the mechanism, guardrails, comparison, window, decision rule. Event charts are before/after, not causal; Experiments randomize config values for 14-60 days | O: paper rule 10; V: FR-26..FR-31 |
| L-11 | **Attention is not retention; a spike is not a result.** Peak players, views and launch-week lifts say nothing about return | E: Fortnite reported scale, not return (FG-05); Brawl Stars Ranked lifted one group then normalized while another fell (FG-15); O: LP:358 |
| L-12 | **Never promise what the studio cannot build in time.** Builder estimates, testing, support and rollback capacity before any external date | O: paper rule 14; owner brief J014 |
| L-13 | **Protect existing progress; give returners a way back.** Migration explained before new investment; catch-up removes obsolete friction, not achievements | O: LP:384-386; E: Clash Royale, Overwatch (`cases.md`) |
| L-14 | **Test what a reward makes players do.** A "social" reward can make play less social; a small visual addition can sink weak devices | E: Roblox's Uplift case (FR-52) |
| L-15 | **Decide after every release:** repeat / revise / retire / investigate; "insufficient evidence" is valid; record actual effort vs estimate | O: paper rule 15 |

## 5. Rules (final check, short)
- The owner decides scope, dates and trade-offs. Nobody in the studio can waive a Roblox rule: build the compliant version, name the rule, return `needs-decision`.
- No invented cadence, event length, retention target, lift, multiplier or price. Case results are EXPERIENCE with their scope, never forecasts.
- No date without builder estimates and approved capacity. No refund promises (creators cannot refund Robux, FR-46).
- Offers: genuine discounts, true end dates, accurate non-restarting timers, no false scarcity, calm wording for younger players. Paid random items, ads, maturity: `platform-policy` + `events-offers-rules.md` §4.
- No player ids or names to Discord or any chat app; no Discord link inside the game; Discord never the only route for information or feedback.
- Rewards and amounts come from the progression designer; numbers and causes from the analyst; estimates from builders.

## 6. Self-check before returning
- [ ] Urgent harm routed first, outside the ranking.
- [ ] Every number has its source, date, denominator and label; the analyst's numbers are not restated as causes.
- [ ] Feedback counts come from the tool, per source, with sampling stated.
- [ ] One recommendation, one cheaper alternative, deferred items with revisit triggers, counter-evidence shown.
- [ ] Every event and offer passes `events-offers-rules.md` §4 and the event checklist; age bands checked per surface.
- [ ] Measurement predeclared with the analyst; decision rule written.

Project overlay: if `knowledge/overlays/live-ops-design.md` exists, read it after this file; it wins for this game.
