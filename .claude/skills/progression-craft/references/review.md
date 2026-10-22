> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `progression-craft`. Sources: 03:PS7, PC1-PC3, CK1-CK15, DN1-DN10, OQ1-OQ5 (paper, all O: proposed studio practice, not measured thresholds). A blank evidence field is never a pass (03:CK preamble). Revised by J018 maker progression-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (failure modes for missing decisions, tier inversions, dead stretches and misplaced luck; checklist rows 16-20; don'ts 11-13).

# Failure modes, the review checklist, the don'ts

## 1. Failure modes to hunt before anyone sees the numbers (03:PS7)
| Failure | How it shows in the simulator report | First question |
| --- | --- | --- |
| Exploding waits | a step's wait jumps far above its neighbours; soft-wall flag | is this a planned wall with a purpose and exit, or an accident of r vs income? |
| Flattened meaningful rewards | reference metric (hits-to-kill, income/s, clear time) flat across several "upgrades" | is enemy or price scaling cancelling the benefit? |
| Unreachable prerequisite | goal blocked: prerequisite missing | is the unlock source in the data and reachable by the policy? |
| Dominant shortcut | one policy or route reaches every goal far faster | is the route meant to be best, or does it skip the content? |
| Cap below required cost | goal blocked: cap below cost | which cap upgrade comes first, and is it reachable? |
| Reset loop creates value | prestige award per run time grows without limit, or a reset is never worse than continuing | what does the reset keep that it should not? |
| Non-finite or precision loss | precision flag (> 2^53, or the smallest unit lost) | which unit, maximum and representation does the design need? |
| Zero income | goal blocked: unreachable, zero income | is there an earning source in that state? |
| No decision | two policies with different objectives buy the same things in the same order over a stretch (`tools.md` §6b) | is this a tutorial row, or should a choice open here? |
| Tier inversion | a tier's summed rate (all its events, every track) is above the sum of the tier below, or above its ceiling (`tools.md` §6a; `progression-design/references/reward-tiers.md` §5) | move the tier, or change how often it happens? |
| Dead stretch | the longest stretch with no step (with no step, completion or win where repeated runs or kills pay) is long against the session, and nothing on screen shows progress during it | which counter or midpoint shows the player they are getting closer? |
| Misplaced luck | seeds spread a skill goal more than the skill profiles do, or a goal meant for everyone is never reached by the struggling profile (`tools.md` §6c) | where should randomness sit, and is there a bounded fallback? |

## 2. Model pass vs design pass (03:PC2-PC3)
- **Model pass** (you can check it): required paths reachable for every supported policy, forbidden paths blocked, ledgers close with zero residual, generated tables match fixtures, expected numeric boundaries hold.
- **Design pass** (only the owner, after play): the trade-offs and the experienced pacing meet the brief. Neither a model pass nor high retention certifies enjoyable or ethical progression.

## 3. Review checklist (03:CK1-CK15; rows 16-20 are studio practice). Each row: pass / fail / not testable, with the evidence path.
| # | Item | Evidence to pass | If it fails |
| --- | --- | --- | --- |
| 1 | Experience specified | owner-approved target feelings and meaningful changes (decision id) | back to game designer and owner |
| 2 | Every numeric input has provenance | each value labelled published (source, version), owner (decision id), measured (dataset), PROPOSAL or EXAMPLE ASSUMPTION | remove it or get the decision |
| 3 | Units and index origins explicit | currency, XP, seconds, levels and owned-count origin defined in the model | fix dimensions and off-by-one |
| 4 | Formula and exported data agree | regenerated tables equal the versioned model; fixture test passes | block export; find the divergent input |
| 5 | Progression reachable | every required goal reached by every supported policy, or blocked on purpose with reason | repair the state or acquisition path |
| 6 | Time estimates include strategy | report names starting state, earning process, policy, session model | relabel as conditional; rerun |
| 7 | Power spikes intentional | each spike in the report matches a timeline row; breakpoint tables reviewed | change power, enemy thresholds or encounter |
| 8 | Prestige improves an approved objective | reset losses, kept assets and recovery path compared | rework the reset or state its non-efficiency purpose |
| 9 | Rewards carry meaning | each unlock names its benefit (`progression-design` D-02) | remove the empty milestone or add content |
| 10 | Economy accounting closes | ledger residual 0 per currency and scope | find missing, duplicated or misclassified events |
| 11 | Premium rules checked | current `platform-policy` review + owner fairness decision recorded | disable the offer; policy review |
| 12 | Simulated paths disclosed | policies, seeds, uncertainty, caps and missing human behaviour listed | stop presenting the model as a population forecast |
| 13 | Math tests passed | `tools/progression` tests + model fixtures green, with output | fix and rerun dependents |
| 14 | Gameplay tested | playtest record from this build and its participants | mark gameplay validation pending |
| 15 | Owner approved release values | exact data revision and scope of approval recorded | do not ship |
| 16 | Every track has decisions | four parts written per track; decision check run on two full reports | open a choice or mark the stretch as teaching |
| 17 | Rewards tiered by benefit and rate | when rewards change: tier table filled; each tier's summed rate inside its ceiling and below the tier under it, per named policy (full single-run reports) | move tiers or change rates; owner chooses |
| 18 | Celebrations follow confirmed results | every celebrated row's trigger is a ledger source, goal or step; paid rows pass the odds check, below-price rows uncelebrated, no outcome sells back into the price currency | fix the trigger or the tier |
| 19 | Numbers shown truthfully | display rule with fixtures in the UI brief; prerequisites export readable requirements | add the rule and the requirement text |
| 20 | Luck placed on purpose | randomness and skill written per track; luck vs skill runs read from `runs_summary` where luck matters | move the randomness or add a fallback |

## 4. Don'ts (03:DN1-DN10)
1. Never invent an XP rate, combat cadence or session benchmark to finish a table; keep it symbolic or label it `EXAMPLE ASSUMPTION`, and name the measurement that would replace it.
2. Never call a bigger nominal reward a power increase before comparing what it buys on the same content and time.
3. Never turn a designer's account or an observational study into a universal causal law; keep source type and population.
4. Never optimize a model player with knowledge a real player does not have yet, unless the policy is labelled omniscient.
5. Never pass a formula that is dimensionally right but impossible in play (spending the same currency twice, a locked prerequisite).
6. Never use continuous DPS for hit thresholds, or continuous income as a claim about an unmodelled tick cycle.
7. Never present the worked examples or any published game's numbers as values for the studio's game.
8. Never call arithmetic a playtest, or a cohort simulation telemetry.
9. Never change rounding, indexing, caps or reset rules silently between model, export and runtime.
10. Never approve your own creative decision, monetization exception or release.
11. Never tier a reward by its amount alone, or let a random roll decide how big it feels.
12. Never read rates from a `--lean` report or verdicts from the top-level `timeline` of a multi-run report.
13. Never show a rounded balance that looks affordable when it is not.

## 5. Open limits to state in every hand-back (03:OQ1-OQ5)
No universal wait per upgrade, rewards per session or genre speed exists; the efficient path is not everyone's path (show explorer, struggling and interrupted players); whether a plateau or reset is wanted is a player question, not a coefficient; arithmetic consistency is not a fun, compliant or tested game.
