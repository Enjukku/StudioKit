> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Part of `game-design`. Sources: N4 §3 (playtests), N4 §5 (live content), N3 §2.7 (measurements), FR (RC09-RC18), FI. Tags as in SKILL.md. How to instrument and run A/B tests in Roblox: `analytics` skill. Revised by J018 maker game-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (§1 failure attribution, pain points, happy misreads; §1b what each input can prove; §4 roster, themes and maps over time).

# Playtests, measurements, live updates

## 1. Playtest protocol (7 steps, O)
1. **A decision-driving question.** Not "is it fun?" but e.g. "do first-time players infer, unaided, that cover changes enemy targeting?"
2. **Population and stage.** Non-experts for onboarding, relevant experts for depth; neither replaces the other. Record prior familiarity, device and input, language, solo or friends, progression state, how recruited.
3. **Fixed scenario and facilitator script.** Explain the test, not the solution. Record every intervention; assisted success is not independent success.
4. **Observation and events together.** Goal inference, time to first meaningful action, attempts, path choices, repeated errors, unexplained failure, resource decisions, recovery, voluntary continuation, stopping reason. Only the metrics the question needs; no irrelevant personal data.
5. **Neutral follow-ups after the behaviour.** "What were you trying to do?" "What did you expect?" After every failure: "What beat you, and what would you do differently?" (a fair loss names the player's own mistake; an unfair one names the game). Never "was our combat satisfying?" or "do you like it?": a question names the goal ("which of these feels most dangerous?"). Keep apart the experience, the player's explanation and the player's proposed fix: a requested fix points at a problem, and the problem is what I solve.
6. **Triangulate.** Telemetry finds patterns, observation gives context, questions show intention, controlled variants separate causes. Disagreement is information ("easy" while failing repeatedly; "unfair" despite balanced numbers when counterplay was unreadable).
7. **Register the finding:** build, segment, denominator, uncertainty, timestamps, hypothesised and alternative cause, severity, change, retest. "No problem observed" is limited evidence, not proof.

Before a change to a live game, play the current build and list its pain points (extra taps, confusion, missed information, dead walks) with where each was observed; every proposed change names the pain point it fixes. When players misread something in a way that is also fun (they use a hazard as a launch pad), consider changing the plan to use the misread instead of "fixing" it.

### 1b. What each input can prove
A verdict is only as good as its input. Label every check with the input it used and its status (gate-verified, MCP-verified, owner-confirmed, not verified).
| Input | Can show | Cannot show |
| --- | --- | --- |
| Spec, tuning table, config | intended values, rules, states | the read, the feel, timing on screen |
| One screenshot | layout, read order, contrast at one moment | timing, onsets, sound, repetition, cost |
| Frame sequence at a known frame rate (studio-operator capture) | timing in frames and ms, tells, feedback onset, celebration length | sound sync, real-device feel |
| Video with audio | sound and sync, the whole moment | device performance, other viewers' screens |
| Two-client capture | what a bystander and a threatened player each see | population behaviour |
| Play-test with players (protocol above) | understanding, choices, continuation, failure attribution | long-term retention |
| Analytics cohort | population behaviour over time | why |
A design is judged in the real build at the game camera on a phone viewport, moving, with effects, UI and other players on; a beauty shot or editor view proves nothing about play. Close every verdict with a "could not check" list: the step, the missing input, the capture or test that would close it.

Valve separates direct observation, think-aloud, questions, surveys, statistics and experiments, each with weaknesses (think-aloud changes play; averages hide extremes; leading and group questions bias answers) (D13 E). Portal's team changed the narrative to match what players already felt and removed a frustrating setup instead of defending it (D14 E). No universal tester count, iteration count or fun score exists; never use a "five users prove it" rule. For population estimates and A/B tests, plan precision from expected variation and the effect that matters, and fix the observation window before reading results (O).

Short tests cannot prove long-term fit: Supercell reports Squad Busters betas of 5,000 then 140,000+ players with D7 29 % then 38 %, and says behaviour after global launch differed and that testing meta and long-term retention too little was a mistake (D29, studio-reported; FI). Another game on another platform: never a target.

## 2. Playtest record (12 fields, O)
Test id and date · decision this test can change · hypothesis and competing explanation · build and configuration (revision, device, input, network, solo or group) · participants (criteria, familiarity, actual count, exclusions) · task and intervention · observations (events, errors, choices, pauses, retries, quotes, kept apart) · measures (definitions, denominators, windows, missing data) · results (values, uncertainty, segment differences) · interpretation (supported and not) · next action (fix, test, owner decision) · privacy (consent and handling). Store in `knowledge/design/playtests/<test-id>.md`.

An AI's imagined playthrough, an invented persona or a numerical model is **never** a playtest (N4 X9 O). Label it "analytic walkthrough".

## 3. Roblox measurement facts (FR, checked 2026-10-20)
| Fact | RC | Use it as |
| --- | --- | --- |
| Average session time = total time ÷ sessions; Roblox also shows how many new users remain at each minute of the first session | RC09 | a distribution to read, not a target |
| Roblox advises reaching fun within the first five minutes, with no long tutorials | RC10 | guidance for the opening, not a session length |
| D1, D7, D30 = exact-day returns by first-play cohort; D7 is the 8th calendar day; young cohorts show empty cells (not zero); Roblox publishes no good thresholds | RC11 | compare cohorts, read segments |
| Benchmarks update daily and show the 50th-90th percentile of similar games with ≥ 100 DAU, falling back to genre then all games; overall-success tiers use the top 1000 by rolling 30-day playtime (games over 30 days old) | RC12-RC15 | diagnosis; the band's low end is the median, not a floor |
| The docs' D1 example band 12.11 %-18.73 % is a worked example with no game, genre or date | RC14 | **never a target** |
| Benchmarks have no effect on ranking; discovery signals are in `game-concept/references/hook-promise.md` §5 | RC18 | |
| Platform 2.7 hours per DAU per day in 2025 is platform-wide, not a game session | RC02 | |

Read the distribution and the segment (new vs returning, source, device, region, party), not one average. D1 can point to an opening problem, D7 to weak reasons to continue, D30 to long-term problems; none proves a cause. No public evidence ranks loop types by retention or sets a universal session length (N3 §2.7 O).

## 4. Live content (N4 §5 O)
- Each addition states its kind of freshness: new decision · new combination · different social goal · expressive material · higher mastery ceiling · story development · familiar content in a new context.
- More items is not more depth: it can dilute discovery, make choices unreadable or devalue old investments. Budget repeatable systemic variation and one-use authored content separately.
- New rewards must not crowd out the ordinary activity the game wants players to enjoy; repeated events must not rest only on fear of missing irreplaceable power.
- Hades' modular structure and story were designed to evolve with Early Access feedback (D20 E). 2XKO protects learned core functions and gives players time to find counterplay; its 47 % / 53 % win-rate triggers and ~5-week patch intention belong to that game (D21; FI).
- Rosters and modes: a new character, unit or pet starts from the roster gap it fills (`preproduction/references/documents.md` §8); a mode change re-checks the balance of every unit in the new mode, because kits tuned for one mode interact differently in another. Check: the mode change ships with a balance-pass list that covers every unit.
- Themes for events and variants come from player data and fill their own niche (`systems-economy.md` §8); each recurring event states its tone shift against the last.
- Maps are revisited from evidence (`spaces.md` §8); a new world is a clear escape from the previous ones. Cosmetics refresh repeated play without touching balance.
- Event or season review (9): entry requirements · late-join and comeback path · learning cost · meaningful activity · individual vs team conflicts · intended stopping point · permanence or reset · effect on the existing economy · what stays valuable after.
- Before release name: audience, expected behaviour mechanism, success signal, harm guardrails, analysis window, alternative causes. After release compare new, existing, returning, solo, grouped and progression cohorts; read exposure and adoption apart from outcomes. Longer sessions can mean enjoyment, confusion, compulsion or a slower economy. Separate balance fixes, novelty, marketing and seasonal effects before any causal claim.

## 5. Update evaluation (10 fields, O)
Update promise (player benefit) · content and system changes (versioned) · eligible audience and exposure · baseline and comparison (same cohort or a justified control; calendar and acquisition changes) · measures (engagement, return, quality, fairness, safety, technical health as relevant) · guardrails (unacceptable harms) · observation window (from the mechanism and sample, not a generic duration) · rollout and recovery · result (values and uncertainty) · decision (keep, revise, revert, keep observing, with reasons).
