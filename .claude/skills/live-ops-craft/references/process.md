> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `live-ops-craft`. Evidence: note `02` §6 (LP:431-518: 12 steps ST-01..ST-12, update brief UB, hand-off contract HO, post-update review PV, do-not-do DN), note `01` §7 (ranking). All O (the paper's operating method) unless marked. Owner rules: J014 brief.

# The live-ops cycle: from evidence to decision to review

Work folder: `knowledge/jobs/<job>/live-ops/`. One **live-ops log** there (`log.md`): evidence packets by cutoff date, decisions with ids, briefs sent, release records, reviews. The agent produces short decision artefacts on top of a detailed evidence record; it never sends the owner every raw comment and chart (LP:433).

## 1. The twelve steps and their gates
| # | Step | Output | Gate before the next step |
| --- | --- | --- | --- |
| 1 | **Intake:** analyst weekly page and findings, feedback sort, trend page, release state, builder capacity | evidence packet with a cutoff date (plan template §B) | missing inputs are written as missing; no invented studio data |
| 2 | **Validate:** metric definitions, cohort maturity, instrumentation, dates, sampling, source authority | data-quality and uncertainty notes | a change is not a logging or population artefact (ask the analyst) |
| 3 | **Protect:** instability, exploits, failed entitlements, serious harm | incident or mitigation request to its owner (§5) | urgent harm is not buried in the ranking |
| 4 | **Diagnose:** the constraint; symptom vs cause | problem statement + other explanations | evidence supports the problem; causal doubt stays visible |
| 5 | **Generate options:** improve, add, simplify or remove, communicate, investigate | bounded options for one player objective | every option fits the core game and has a mechanism |
| 6 | **Estimate:** builders, progression designer, marketing (handoffs §5, §3, §6) | impact and effort ranges, economy effects, risks | no unverified date, assumed licence or invented lift |
| 7 | **Rank** (§2) | `templates/live-ops/update-plan.md` | counter-evidence and opportunity cost visible |
| 8 | **Decide:** owner chooses | decision record with the owner's words | approval is concrete; silence is not approval |
| 9 | **Hand off:** update brief (§3) to each role | briefs (handoffs.md) | each owner accepts scope, estimate and dependencies |
| 10 | **Verify:** implementation, economy scenarios, usability, policy, measurement readiness | release-readiness record (§4) | required checks pass; promised behaviour matches shipped behaviour |
| 11 | **Release and monitor** | incident log, first operational read | stop conditions enforced; early activity is not called mature retention |
| 12 | **Evaluate and learn:** analyst reports; live-ops recommends | post-update review (§6) | no causal overclaim; real cost and counter-evidence kept |

Effort: medium; **high for a season plan or a big update** (owner J014-D1). Say which in the restatement.

## 1b. Gaps in the inputs (from the J014 G2 test)
| Gap | Do |
| --- | --- |
| only capacity by kind of work (no scope estimate) | rank, but label each option "pre-estimate: <capacity source>"; send estimate tickets; no date reaches the owner as committed until the builder answers |
| a role whose feasibility you need is missing from capacity (game designer, progression designer) | write the option's feasibility as "not yet reviewed"; ask the lead for that role's capacity; state the assumption in the plan |
| the analyst cannot cover a measurement plan in time | still write the decision rule and the primary outcome in the brief; propose the cheapest read (fold it into the weekly page); if nothing can measure it, label the update "unmeasured" and let the owner decide |
| urgent harm and no emergency authority agreed for this game | ask the owner the same day through the lead, with the compliant state as the recommendation (hide or disable what breaks a platform rule or harms players); repeat the ask; never act without authority, never bury it in the plan. Owner standing authority (J014-D6): hide or switch off anything that breaks a Roblox rule or loses players' purchases or progress, then tell the owner the same day; record it in the game's decisions at launch |

**Exploitable currency (check):** currency issued outside its designed sources, or a ledger that does not balance (issued ≠ spent + converted + held), or issuance concentrated in a few accounts. A surplus that balances is an economy design problem for the progression designer, not an incident.

## 2. Ranking (steps 5-7)
1. **Order of consideration:** urgent harm → the binding constraint for the studio's current objective → the smallest change that might remove it → only then attractive new systems (LP:214).
2. **"Fix the biggest drop-off" needs care:** compare affected players, the rate, the cohort's importance, the plausibly recoverable part and the cost. A normal exit after a good session differs from an early failure. A funnel drop can come from changed logging, a changed audience or an optional step: the analyst confirms the denominator before you name a cause (LP:216).
3. **Write each candidate as a hypothesis** (design L-04) and link each clause to evidence or "uncertain".
4. **Impact:** reach, plausible effect, duration, strategic weight. **Effort:** all delivery and ongoing costs. **Confidence:** strength of evidence for the problem and the mechanism, not your certainty. If reach and effect are measured: eligible population × justified incremental effect, uncertainty carried. Else "unknown; test required" (LP:220).
5. **Show three things:** the best-supported option, a cheaper useful alternative, and a reason to defer. Where evidence is weak, a small diagnostic or prototype may outrank a full feature. Name what each option displaces (LP:222).
6. **Mandatory fixes and dependencies are never outranked** by an impact × effort chart.
7. **Capacity check** (design `cadence-content.md` §3) before any date appears. For a package option, total each role's days across all its parts and compare with that role's free days; any part that is only *assumed* to be data or config work is listed as an assumption to confirm with the builders.
8. **The biggest silent problem gets a cheap next step this period** (a data-only cue, a config switch, a logging spec), not only "diagnose later", unless the builders say no cheap step exists.

## 3. The update brief (step 9; base for every hand-off)
Fields (LP:454-460): identity (decision id, title, version, owner approval, responsible lead) · player problem (cohort, evidence, baseline, source dates, uncertainty) · objective (primary behaviour or outcome; why now) · hypothesis (change → mechanism → outcome; alternatives) · scope (must deliver; optional only if capacity remains; excluded) · player journey (entry, first meaningful action, repeat activity, completion, next core action) · new / returning / veteran paths (access, comprehension, progression, preserved identity).
Then one brief per receiving role, in the `rules/messages.md` §2 format (handoffs.md §2-§7). What each role receives (LP:462-472):

| Role | Receives | Returns before any date is committed |
| --- | --- | --- |
| game designer | player promise, core-loop fit, activity constraints, interaction acceptance criteria, edge cases, the question the update must answer | the play spec; an unvalidated feature list is never presented as finished design |
| progression designer | target effort distribution, reward purpose, currency and item flows, existing ownership, catch-up needs, expiry and migration rules, monetization limits | validated amounts, issuance ranges, abuse cases; live-ops never invents a multiplier |
| builders (architect → feature- or quick-builder) | approved scope, dependencies, interfaces, device and performance limits, save and entitlement behaviour, exposure ids, safe-disable needs, acceptance criteria | feasibility, effort range, lead time, risks |
| marketing | approved benefit, audience, exact dates, eligibility, true reward terms, assets, channel limits, proof, fallback wording; the patch-notes fact sheet | announcement drafts for the owner; no teaser promises optional scope |
| analyst | hypothesis, cohort and assignment or exposure definitions, primary outcome, guardrails, comparison, windows, decision criteria | confirmation the question can be answered, or why not |
| release owner (lead) | launch checklist, sign-offs, incident contacts, stop conditions, rollback or disable behaviour, communication plan, review dates | go / no-go |

**Configs (V, FR-32):** Roblox configs change values without publishing. A config switch helps only if builders implemented and tested the behaviour; it does not undo saved rewards or migrations. Keep the config version and exposure record so the analyst knows which rules players had (LP:474).

## 4. Release-readiness record (step 10)
| Item | Evidence |
| --- | --- |
| scope shipped = scope approved | build version, config version |
| event checklist L1-L12 (`event-design.md` §E) | each row with source and read date |
| economy scenarios run (progression designer) | file |
| measurement ready (analyst): events firing, exposure ids, windows | analyst confirmation |
| safe disable tested; persistent-state response written | QA evidence |
| patch-notes fact sheet matches the build | `patch-notes.md` checks P1-P5 |
| incident responder named; stop conditions | names, thresholds |

## 5. Incidents (step 3 and 11)
Request format to the lead: what is happening, affected players and how known, reproducibility, harm now, safe mitigation options (disable a feature, config change), what must not be done (blind rollback of saved state), player message facts. Never post exploit steps. Never promise refunds (creators cannot give Robux refunds, FR-46), and never promise compensation ("we will add your missing items") in a draft player message before the owner decides it. Measurement or logging that an urgent item needs (for example a save-loss measure) goes to the analyst **now**, not after the plan is picked.

## 6. Post-update review (step 12; copy into the log as `review-<decision id>.md`)
| Field | Value |
| --- | --- |
| decision id; real release version and timestamps | |
| original hypothesis; approved success criteria | |
| what actually shipped; deviations; incidents | |
| assigned and exposed populations; exclusions; data quality | analyst |
| primary result and uncertainty; guardrail results | analyst verdict (`analysis-design` experiments-updates §6) |
| new, continuing, reactivated cohort results | analyst |
| revenue composition; post-event displacement | analyst |
| feedback changes; unresolved themes | feedback sort ids |
| actual active effort, elapsed time, support cost; estimate error | builders, lead |
| best explanation; credible alternatives; limits of causal attribution | |
| **decision: repeat / revise / retire / investigate** | |
| what becomes a reusable rule, with its evidence label | lesson draft in `knowledge/inbox/` |
| owner decision; next review trigger | owner's words |

## 7. Do-not-do (detection → replacement)
| Shortcut | Replace with |
| --- | --- |
| chase every request | a player problem, distinct-author counts, cohort, behaviour check |
| add a new system to every update | ask whether existing mechanics can meet the need; count future maintenance |
| copy an unrelated viral event | core fit, audience overlap, trend lifetime, rights |
| distant endgame content while a drop-off stays open | compare affected cohorts, reachability, the binding constraint |
| a date before builders estimate | accepted scope, dependencies, testing, support coverage |
| a retention lift from peak players or views | metric, denominator, cohort maturity, counterfactual |
| success from the launch spike | later cohorts and post-event behaviour |
| nerf every newly popular strategy | verify power, counterplay, discovery time |
| social rewards without testing behaviour | inspect spam, avoidance, abuse, harm to recipients |
| inflate event rewards without economy review | simulate total issuance and later demand |
| false scarcity, compulsory notifications | real deadlines, choice, truthful messages |
| random outcomes hidden behind currency or boosts | audit the whole paid chain and current odds |
| send younger players to Discord | in-game routes; current link rules |
| blind rollback of saved state | keep valid entitlements; test migration or compensation |
| AI confidence instead of unknown effort or effect | explicit unknowns; ask for estimates; a bounded test |
| treat an announced platform feature as available | confirm current docs and account access (Roblox's "Late 2026" roadmap items: FR-50, FR-53) |
