# Eval briefs: progression-designer (progression-design + progression-craft)

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Built in J011. Run each brief with the `progression-designer` role in a fresh context; a separate grader (Sonnet, high) scores the must-pass checks from the files, not the hand-back. Hidden cases (not in the skills) live in `knowledge/jobs/J011-progression-designer/evals-hidden.md` and are given only to the grader.

## E1 — Incremental timeline from a brief
Brief: a small simulator game ("tap to mine, buy drills, drills mine for you, rebirth for a permanent multiplier"). Owner targets: first purchase in the first minute; a clear next goal every few minutes in session one; a soft slowdown before the first rebirth; the first rebirth should feel worth it. No earning rates, session lengths or prices are given. Ask: the feeling timeline, a model, runs for at least 3 policies, a chart, a verdict per target.
| ID | Must pass |
| --- | --- |
| E1-1 | Timeline rows written first, each with clock (active or calendar), observable sign, shape and purpose |
| E1-2 | Every invented number labelled `EXAMPLE ASSUMPTION` or `PROPOSAL`; no unlabelled pacing number anywhere |
| E1-3 | Model runs in `sim.py` exact mode; ≥ 3 named policies incl. one struggling or explorer variant; report paths cited |
| E1-4 | Rebirth: removed / kept / granted list and the prestige basis chosen with a reason; run 2 vs run 1 compared on the same goals |
| E1-5 | Soft wall placed on purpose (threshold declared from the timeline) and found by the report where intended |
| E1-6 | Each target: pass / fail / not testable with evidence; feelings stay hypotheses ("model pass ≠ fun") |
| E1-7 | 2-3 options with what the player feels differently, one recommendation, owner decision with a default |

## E2 — "The new sword doesn't feel stronger"
Brief: player attack 12 → 15 with the new sword; the zone's common enemy has 30 HP, the elite 60 HP; enemies scaled +20 % HP in the same update; attack interval 0.8 s. Owner: "the new sword doesn't feel stronger".
| ID | Must pass |
| --- | --- |
| E2-1 | Hits-to-kill and TTK computed before and after on the same reference enemies (with and without the HP change), with `curves.py`, both first-hit conventions stated |
| E2-2 | Names the breakpoint finding (e.g. common enemy 3 → 2 hits before scaling, but scaling cancels it) instead of quoting DPS +25 % |
| E2-3 | Smallest change options target a breakpoint on a named reference enemy (not "+X % damage"), each with its effect on TTD and the next zone |
| E2-4 | Brief to engineering or game designer in `rules/messages.md` form; values labelled; owner decides |

## E3 — "Players quit at level 12"
Brief: the analyst sends: median time to reach level 12 among players who reached it fell from 41 to 33 minutes after update 1.4; overall D7 dropped; level 12 needs 3× the XP of level 11 since 1.4.
| ID | Must pass |
| --- | --- |
| E3-1 | Flags survivor bias: completer-only time cannot show the wall; asks for eligible players, non-completers (censored) and observation windows |
| E3-2 | Checks the denominator and cohort maturity of D7; separates operations causes (crashes, acquisition, holidays) first |
| E3-3 | Lists competing explanations (cost, unclear objective, dull activity, combat failure, session time) and the data that tells them apart |
| E3-4 | Re-simulates 1.3 vs 1.4 under the same named policies; proposes the smallest lever; says what the analyst must measure to confirm |
| E3-5 | No causal claim from the before/after alone; non-significance not called equivalence |

## E4 — A paid egg with a luck boost
Brief: the owner wants a 25-Robux egg with a 2 % legendary pet that is needed to enter zone 3, plus a 99-Robux "2× luck" pass.
| ID | Must pass |
| --- | --- |
| E4-1 | Flags essential progress behind luck (zone 3) and proposes a deterministic or bounded route; does not approve it alone |
| E4-2 | Loads `platform-policy`: odds before purchase totalling 100 % with the rounding rule; luck pass shows its numeric effect and updated odds; `PolicyService` per player, fail closed; a complete route for restricted players (one of the documented treatments, hiding preferred) |
| E4-3 | Computes expected cost (c/p) AND the unlucky tail (attempts for 90 % and 99 %), and with the pass; never calls c/p the fair price |
| E4-4 | Every outcome gives the buyer some benefit; younger players and no-pushy-wording noted |
| E4-5 | Owner decision digest with options and a default; nothing called approved |

## E5 — "Prestige feels pointless"
Brief: rebirth resets everything except a rebirth counter that adds +10 % income per rebirth; the second run takes 90 % as long as the first.
| ID | Must pass |
| --- | --- |
| E5-1 | Simulates run 1 vs run 2 vs run 5 with the same policy; reports time to the same goals |
| E5-2 | Diagnoses with the reset keep/remove list and what changes for the player in the next run (new choices, not only speed) |
| E5-3 | Options: basis (lifetime / maximum / since reset), formula shape (fractional power with z^(1/α) consequence), what is kept, what new content a run opens; each with its effect on the timeline |
| E5-4 | No published game's constants copied as tuning; labels on every number |
