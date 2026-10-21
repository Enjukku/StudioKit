# Eval briefs: live-ops designer (live-ops-design + live-ops-craft)

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Built in J014. Run each brief with the `live-ops-designer` role in a fresh context, with a synthetic input pack (`knowledge/jobs/J014-live-ops-designer/test-pack/` or a pack made for the run, every file labelled SYNTHETIC). A separate grader (Sonnet, high) scores the must-pass checks from the files, not the hand-back. Hidden cases (not in the skills) live in `knowledge/jobs/J014-live-ops-designer/evals-hidden.md` and go only to the grader. Template coverage: update-plan (E1), feedback-sort (E1, E3), event-design (E2), patch-notes (E4, E5).

## E1 — "What should the next update be?" (big update, high effort)
Brief: the pack holds an analyst weekly page (D1 and D7 by cohort, a funnel with a step where 40 % of new mobile players stop, event participation), about 150 feedback items in 4 sources, a trend page, and builder capacity "one builder, 3 weeks after maintenance". Ask: sort the feedback and propose the next update.
| ID | Must pass |
| --- | --- |
| E1-1 | `feedback_count.py validate` and `count` run; output files cited; every count in the sort matches the tool output |
| E1-2 | Shares are per source ("authors / sampled authors"); no "% of players"; overlap "unknown" unless a shared key scheme is real |
| E1-3 | Urgent items (purchase or data loss) routed first, outside the ranking |
| E1-4 | Plan uses `update-plan.md`: each option is a hypothesis with evidence per clause; impact "unknown; test required" where no effect is measured; no invented decimals |
| E1-5 | The mobile funnel failure is weighed against louder feedback (loud vs silent; analyst behaviour check asked) |
| E1-6 | Exactly one recommendation, one cheaper alternative, deferred items with revisit triggers, counter-evidence, opportunity cost |
| E1-7 | Estimate tickets to engineering via the lead; no date without builder numbers; fits the stated capacity or says what is cut |
| E1-8 | Measurement brief for the analyst (cohort, outcome, guardrails, comparison label, window, decision rule) |

## E2 — Halloween event with a crate and a countdown deal
Brief: the owner wants a 2-week Halloween event: an event currency, a limited "Pumpkin Crate" bought with Robux-bought gems, a "last chance" shop deal with a countdown, and a push to bring lapsed players back. The game is rated Mild (Kids and Select can play).
| ID | Must pass |
| --- | --- |
| E2-1 | `event-design.md` filled: entrance, activity loop, true end and separate claim end with time zone, late-start and missed-day path, exit |
| E2-2 | Crate treated as a paid random item (indirect via gems): odds summing to 100 % before purchase, boosts change shown odds, PolicyService gate with a free or fixed path, every outcome a benefit |
| E2-3 | Countdown deal: true end, timer accurate and not restarting, discount genuine and not "very short" pressure; calm wording for younger players (FR-54, FR-57) |
| E2-4 | Return message: event listing / update announcement for all; personalized notification only for 13+ opted-in and only if player-specific; no dark patterns; no gating on opt-in |
| E2-5 | Amounts asked from the progression designer (issuance, event-only currency, abuse cases); no multiplier invented |
| E2-6 | Length justified from play opportunities and coverage, not a "best length"; maturity questionnaire re-check listed as owner action if the theme changes answers |
| E2-7 | Launch checklist L1-L12 with sources and read dates |

## E3 — "Discord is screaming for PvP"
Brief: 60 Discord messages ask for PvP; 52 come from 4 authors. In-game form: 3 of 210 respondents mention PvP. The analyst page shows veterans finish all content in 9 days.
| ID | Must pass |
| --- | --- |
| E3-1 | Counts by distinct author per source; the loud-author flag explained; messages kept as intensity |
| E3-2 | Discord described as engaged 13+ players, not the player base; in-game sample described with who could answer |
| E3-3 | Problem separated from solution (veterans run out of goals vs "add PvP") |
| E3-4 | Options include improving existing systems for veterans; PvP costed by builders before any promise |
| E3-5 | No Discord link or invite proposed inside the game; reply to the community follows the close-the-loop rules |

## E4 — "Did the event work?"
Brief: the analyst page shows DAU +35 % during a 3-week event, D7 of event-week new players unchanged, revenue up, with 60 % of event revenue from 2 % of payers; event currency balances 5× higher after the event; feedback: 40 authors say the final reward needs too many hours.
| ID | Must pass |
| --- | --- |
| E4-1 | No success claim from the spike; reads with the analyst's verdict and the failure-response table |
| E4-2 | Spending concentration and leftover currency named as guardrail problems for the progression designer |
| E4-3 | Decision: repeat / revise / retire / investigate with what would change it; actual vs estimated effort recorded |
| E4-4 | Post-update review fields all filled or marked unknown |
| E4-5 | Patch-notes fact sheet for the follow-up fix uses shipped values, separate claim deadline, "from your feedback" linked to the theme id; checks P1-P5 |

## E5 — Mid-event exploit
Brief: day 4 of an event; support reports and the analyst show players duplicating event currency through trading; 12 % of event currency now comes from 30 accounts.
| ID | Must pass |
| --- | --- |
| E5-1 | Incident routed to the lead at once with scope, evidence, reproducibility, safe mitigation (disable trading of the currency or the event shop by config if built) |
| E5-2 | No blind rollback; state-safe response asked from builders and the progression designer; legitimate gains protected |
| E5-3 | No refund promise (creators cannot refund Robux); no exploit steps in any player message |
| E5-4 | Patch-notes fact sheet "known issues" honest about scope with no invented fix date |
