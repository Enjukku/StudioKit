---
type: reference
scope: universal
status: active
updated: 2026-10-20
source: J003
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-20

Source file: `Game_Designer_Part_2_Research.txt`, lines 179-366 (plus registry entries, lines 367-630, for every cited ID); paraphrased; the paper stays outside git.

# Game design research, part 2B: levels, social, playtests, critique, live content, AI review (paper lines 179-366)

## 0. How to read this file

Cite as `P2:<line>` plus the paper's own IDs, e.g. `P2:185 [D11]`. A tag stays with its claim. "none cited" means the paper gives no source ID for that row (the row is the paper's own method, tagged OPINION). UNSPECIFIED means "the paper gives no value"; it is not zero and not a default.

| field | value |
| --- | --- |
| Paper | "Game Designer Research Part 2: The Craft of Design Review" (P2:1). Research cutoff 21 October 2026 (P2:18) |
| Audience stated | the AI game designer that supports an owner-led Roblox studio; the owner decides, the agent reviews, diagnoses and proposes (P2:18) |
| Lines in this file | P2:179-366: section 4 (levels and encounters), 5 (multiplayer and social, Roblox communication and audience eligibility), 6 (playtests), 7 (pre-build critique, ranking fixes), 8 (live content), 9 (AI reviewer process, "Do not do", open questions). Sections 1-3 (P2:22-177) are in `03-loops-systems.md` |
| Craft vs platform | Roblox sources give platform facts only; the craft foundation comes from other industry sources (P2:20, outside this range) |
| Tag meaning | VERIFIED = official facts inspected directly, or published measurements within their stated scope; studio-reported numbers are verified "as reported", not audited. EXPERIENCE = an attributed practitioner's account or judgment. OPINION = the paper's own method, interpretation or value choice (P2:20) |
| Registry rule | The registry supports facts and attributed practices. Templates and proposed operating rules stay OPINION (P2:369) |

Counts of the paper's lists (check C1): level artifact node fields 10; level and encounter checklist 9; test protocol 7 steps; playtest record template 12 fields; feature review checklist 9; review finding template 13 fields; update evaluation template 10 fields; AI review procedure 12 steps; "Do not do" 9 items; open questions 8; rule-table rows 3 + 3 + 3 + 2 + 3 + 4 = 18.

## 1. Section 4: levels and encounters (P2:179-213)

### 1.1 Rules from the text

| id | rule (paraphrased) | tag | source | P2 |
| --- | --- | --- | --- | --- |
| 4.01 | Hayashida says Super Mario 3D Land is where he became strict about one level concept that is developed through four stages: learning, complication, an unexpected variation, and a demonstration of mastery. He describes it as evolving through Galaxy and Galaxy 2, not as a timeless formula used the same way in every Nintendo game. He ties 3D Land stage length to short train journeys, not to a fixed universal session length | EXPERIENCE | D10 | 181 |
| 4.02 | Teaching sequence in 4 steps: (1) expose a mechanic in a low-confound situation; (2) require its use in a more demanding arrangement; (3) change one relationship so that rote execution no longer works; (4) ask for an independent application. For each step, state what the player should infer and what observed action would show it. The paper calls this four-step version an adaptation: useful for some instructional action levels, not a required structure for every open world, horror scene, puzzle or social area | OPINION | none cited | 183 |
| 4.03 | Left 4 Dead AI pacing has four phases: build-up, peak, fade, relaxation. The implementation holds the peak for 3-5 seconds and relaxes for 30-45 seconds or until the players have travelled far enough forward. Bosses are outside the adaptive pacing control. The paper separates pacing frequency from difficulty amplitude. These are that game's parameters, not a recommended Roblox encounter clock | VERIFIED (documented implementation; the registry tags the claimed design benefit EXPERIENCE) | D11 | 185 |
| 4.04 | Minecraft: Education Edition's 2021 guide separates paths, breadcrumbs, landmarks, waypoints, soft and hard boundaries, and decorative size from playable content. Scope is classroom worlds, not all of Minecraft and not all genres | EXPERIENCE | D24 | 187 |

### 1.2 Level review artifact (P2:189-195, tag OPINION)

Required elements of the artifact:

| # | requirement | P2 |
| --- | --- | --- |
| A1 | An annotated route graph, not only a beauty image | 191 |
| A2 | At every node, record the 10 fields in the next table | 191 |
| A3 | Show sightlines and scale from the real gameplay camera | 191 |
| A4 | Mark where players may lose orientation and how they find their bearings again | 191 |
| A5 | At crossings, the routes must differ in something meaningful. The paper lists 7 kinds of difference: timing, information, exposure, resource use, skill demand, exploration, expression | 191 |

Node fields (10). The paper lists the names only and gives no definition of any field:

| # | field | P2 |
| --- | --- | --- |
| N1 | entry view | 191 |
| N2 | visible and hidden goals (one item in the paper) | 191 |
| N3 | action choices | 191 |
| N4 | information | 191 |
| N5 | commitment | 191 |
| N6 | risk | 191 |
| N7 | reward | 191 |
| N8 | recovery | 191 |
| N9 | exit | 191 |
| N10 | optional content | 191 |

Route walk-through and boundary tests:

| # | requirement | P2 |
| --- | --- | --- |
| R1 | Run the route as 5 player types: uninformed, returning, expert, grouped, and a player who misses an optional clue | 193 |
| R2 | Trace what happens after 4 events: a wrong turn, a death, a disconnect, a depleted resource | 193 |
| R3 | Check that checkpoints keep what the player learned, instead of only repeating transit | 193 |
| R4 | Test boundaries with the movement tools players really have | 193 |
| R5 | A visible obstacle must explain its rule and stay consistent when the player's abilities change | 193 |

Encounter requirements:

| # | requirement | P2 |
| --- | --- | --- |
| E1 | For each enemy, state the behavior it elicits from the player | 195 |
| E2 | If two enemies differ only in health, name the reason both belong | 195 |
| E3 | Examine 6 kinds of combination: overlapping attacks, escape routes, camera occlusion, safe-space exhaustion, resource recovery, simultaneous demands | 195 |
| E4 | An enemy that is fair alone can form an unfair combination | 195 |
| E5 | Telegraphs must be usable at the moment of decision, not only visible on a paused screenshot | 195 |

### 1.3 Level and encounter review checklist (9 items, P2:197-207)

The paper's frame (tag OPINION): these are testable review questions, not a demand that all games use the same level grammar.

| # | item | pass when | reason | tag | source | P2 |
| --- | --- | --- | --- | --- | --- | --- |
| L1 | Routes | Intended destinations and optional alternatives can be found without an evaluator rescuing the player | Intended exploration and accidental disorientation need different fixes | OPINION | none cited | 199 |
| L2 | Landmarks | Orientation cues stay distinguishable from the relevant approach directions and cameras | Being unique in decoration is not enough if the player never perceives the cue | OPINION | none cited | 200 |
| L3 | Teaching | The player meets a comprehensible use of the mechanic before a demanding variation, unless deliberate confusion is the approved aim | A test should be able to tell learning from luck | OPINION | none cited | 201 |
| L4 | Escalation | More challenge names the demand that changed and the skill it tests | Adding hazards with no learning hypothesis can create arbitrary difficulty | OPINION | none cited | 202 |
| L5 | Readability | Important geometry, actors and hazard boundaries are clear under target screens, effects and multiplayer occupancy | The production scene can make a clean grey box invalid | OPINION | none cited | 203 |
| L6 | Pacing | Transitions between intensity, recovery, anticipation and discovery have a stated purpose | Constant maximum intensity removes contrast and may hide decision chances | OPINION | none cited | 204 |
| L7 | Boundaries | Collision, fall and reset rules, inaccessible areas and recovery paths match the visible world | Mismatched affordances teach rules that cannot be relied on | OPINION | none cited | 205 |
| L8 | Social | Group flow, late joining, separation and recovery are handled explicitly where they apply | A solo route can become a bottleneck or a way to exclude people in a party | OPINION | none cited | 206 |
| L9 | Failure | The cost of failure, the retry route and the information gained match the intended challenge | Repetition should test the skill, not add irrelevant waiting by accident | OPINION | none cited | 207 |

### 1.4 Rule table of section 4 (3 rows, P2:209-213)

| rule | number | tag | source and date | P2 |
| --- | --- | --- | --- | --- |
| The four-step teaching idea has an exact game attribution | 4 steps; 3D Land explicitly | EXPERIENCE | D10, 2012-04-13 | 211 |
| Pacing values are not general difficulty standards | 3-5 s peak; 30-45 s relax or distance | VERIFIED, historical implementation | D11, 2009 | 212 |
| A large environment is not automatically more play | No transferable size threshold | EXPERIENCE | D24, 2021-06 | 213 |

## 2. Section 5: multiplayer and social design (P2:215-240)

### 2.1 Rules from the text

| id | rule (paraphrased) | tag | source | P2 |
| --- | --- | --- | --- | --- |
| 5.01 | In Left 4 Dead, enemy mechanics create rescue needs and punish separation through the fiction. Resource sharing and automatic supportive callouts lower the cost of coordination. The designers explicitly rejected invisible leashes and teleporting stragglers as heavy-handed enforcement | EXPERIENCE | D12 | 217 |
| 5.02 | Design interdependence with understandable chances to help, not compulsory dependence that lets one player hold everyone hostage | OPINION | none cited | 217 |
| 5.03 | Riot frames matchmaking as a tradeoff among fair matches, preferred positions, and queue duration. The 2018 retrospective compares real queue outcomes and does not announce one best queue length | EXPERIENCE | D22 | 219 |
| 5.04 | Riot's player-dynamics account treats harmful interaction partly as an environment-design problem, and aims for a rewarding social experience, not only punishment | EXPERIENCE | D23 | 219 |
| 5.05 | Cooperation should stay understandable without unrestricted chat or voice. Provide shared-state cues, readable help requests and a safe exit. Check friend joining, group separation, mixed progression and language differences in real configurations. A social KPI must be reviewed together with spam, exclusion, coercion and recovery, never optimized alone | OPINION | none cited | 234 |

### 2.2 Group lifecycle review (P2:221, OPINION, none cited)

Review the whole lifecycle in 8 stages, in this order:

| # | stage |
| --- | --- |
| G1 | discover or join a friend |
| G2 | understand the shared objective |
| G3 | coordinate |
| G4 | contribute visibly |
| G5 | resolve differences |
| G6 | survive a mismatch or a disconnection |
| G7 | finish |
| G8 | continue together, or leave safely |

The paper adds: friendship value is not the same as adding a party button. Test 6 conditions: mixed experience levels, late joins, unequal unlocks, language differences, play without voice, and a player who wants to leave.

### 2.3 Competition, status and abuse (P2:223-227, all OPINION, none cited)

| topic | what the paper says | P2 |
| --- | --- | --- |
| Competition: what to demand | Both outcome fairness and understandable agency | 223 |
| Competition: what to inspect (8) | skill-estimation uncertainty, party advantage, role assignment, population at low-traffic times, rematches, match duration, surrender, anti-smurf assumptions | 223 |
| Competition: do not | Do not guarantee that every match will be close (a fair pre-match estimate can still end decisively). Do not optimize retention by secretly forcing losses. Do not make matchmaking claims that the real system does not support | 223 |
| Status and showing off | Specify what is visible, to whom, and what it signifies. The paper names 6 possible meanings: skill, generosity, creativity, tenure, identity, spending. Test that desirable status can be reached without humiliating others or shutting newcomers out of effective play. Do not confuse visible purchase with earned mastery | 225 |
| Abuse: separate cases | Tell apart theft, deception or sabotage that the game rules allow ("agreed") from targeted harassment and exploitation | 227 |
| Abuse: what to inspect (6) | blocking, kicking, hostage-taking, unwanted contact, unfair resource loss, abusive trade | 227 |
| Abuse: pairing rule | Pair every potentially harmful affordance with 4 things: prevention, visibility, recovery, safe exit | 227 |
| Abuse: muting | Muting must not make essential cooperation impossible | 227 |
| Abuse: reports and sanctions | Needed where they apply, but they cannot repair incentives that reward antisocial play | 227 |
| Abuse: events | Review new event incentives for accidental kill stealing or competition between teammates | 227 |

### 2.4 Roblox communication and audience eligibility (P2:229-234)

The facts are in the table "Roblox platform facts" (section 7 of this file; RF01-RF10). The craft rule beside them is 5.05 above. The paper gives no further detail on chat. It does not name which chat or voice features exist at which tier or age.

### 2.5 Rule table of section 5 (3 rows, P2:236-240)

| rule | number | tag | source and date | P2 |
| --- | --- | --- | --- | --- |
| Cooperation can be embedded in enemy and resource design | 4 survivors in the case | EXPERIENCE | D12, 2009-03 | 238 |
| Matchmaking is multi-objective | 3 stated objectives | EXPERIENCE | D22, 2018-03-14 | 239 |
| Prevention belongs in game structure | No universal effect size established | EXPERIENCE | D23, 2022-05-12 | 240 |

## 3. Section 6: playtests and feedback (P2:242-267)

### 3.1 Rules from the text

| id | rule (paraphrased) | tag | source | P2 |
| --- | --- | --- | --- | --- |
| 6.01 | Valve separates 6 methods: direct observation, think-aloud, questions, surveys, statistics, experiments. Each has weaknesses: think-aloud can change play; averages hide extremes; observers interpret behavior; leading questions and group questions bias answers. The slides label some displayed statistics as simulated, so those charts must not be cited as measured Valve results | EXPERIENCE | D13 | 244 |
| 6.02 | Portal's postmortem links narrative revisions to what players already feel, and removes a frustrating companion-cube obstacle setup instead of defending it | EXPERIENCE | D14 | 244 |
| 6.03 | Supercell's 2026 retrospective: Squad Busters closed betas of 5,000 players, then more than 140,000 players. D7 retention 29% then 38%. The second beta also reported D1 61% and D3 44% | VERIFIED (studio-reported) | D29 | 246 |
| 6.04 | The team says beta-to-global behavior differed, and that insufficient testing of meta and long-term retention was a mistake | EXPERIENCE | D29 | 246 |
| 6.05 | The source's sweeping warning about drawing conclusions from 100,000-plus players is called a practitioner interpretation. Large samples can give precise estimates for the wrong population, environment or observation window. It does not mean large-sample inference is impossible in itself | practitioner interpretation (the paper gives no tag word) | D29 | 246 |
| 6.06 | No universal participant count, tester-to-designer ratio, iteration count or fun score was established in the inspected sources. Diagnostic tests: prioritize diverse relevant failure modes. Population estimates or A/B tests: plan precision and power from expected variability and meaningful effect, account for repeated observations and group assignment, and declare the observation horizon before reading results. Do not substitute an invented "five users prove it" rule | OPINION | none cited | 258 |

### 3.2 Test protocol (7 steps, P2:248-256, tag OPINION)

| # | step | detail | P2 |
| --- | --- | --- | --- |
| T1 | Ask a decision-driving question | "Is the game fun?" is too coarse. Example that can drive a change decision: do first-time players infer, unaided, that cover changes enemy targeting? | 250 |
| T2 | Choose the required population and stage | Recruit nonexperts for onboarding and relevant experts for depth; neither replaces the other. Record 6 things: prior familiarity, device and input, language, solo or friend context, progression state, how recruited | 251 |
| T3 | Fix a playable scenario and a facilitator script | Explain the testing process, not the solution. Record every intervention; assisted success is not independent success | 252 |
| T4 | Collect synchronized observation and events | Track 10 things: goal inference, time to first meaningful action, attempts, path choices, repeated error, unexplained failure, resource decisions, recovery, voluntary continuation, stopping reason. Use only the metrics the hypothesis needs; do not collect irrelevant personal data | 253 |
| T5 | Ask neutral follow-ups after the relevant behavior | Use questions like "What were you trying to do?" and "What did you expect?" Avoid "Was our combat satisfying?" Keep three things apart: the player's experience, their causal explanation, their proposed fix | 254 |
| T6 | Triangulate | Telemetry finds patterns; observation gives context; questions expose intention; controlled variants help separate causes. Disagreement is useful: a player may say "easy" while failing repeatedly because the presentation feels childish, or say "unfair" despite a balanced numeric outcome because counterplay was unreadable | 255 |
| T7 | Register a finding | Record 10 things: build, segment, denominator, uncertainty, timestamps, hypothesized cause, alternative cause, severity, change, retest. Treat "no problem observed" as limited evidence, not proof of absence | 256 |

### 3.3 Playtest record template (12 fields, P2:260-261, tag OPINION)

| # | field | what goes in it |
| --- | --- | --- |
| PT1 | Test ID and date | an identifier |
| PT2 | Decision | what this test can change |
| PT3 | Hypothesis and competing explanation | both |
| PT4 | Build and configuration | revision, device, input, network, solo or group |
| PT5 | Participants | recruitment criteria, prior familiarity, actual count and exclusions |
| PT6 | Task and intervention | instructions, assistance and exposure |
| PT7 | Observations | events, errors, choices, pauses, retries and quotations, kept separate |
| PT8 | Measures | definitions, denominators, observation windows and missing data |
| PT9 | Results | actual values, uncertainty and segment differences |
| PT10 | Interpretation | what is supported and what is not |
| PT11 | Next action | fix, another test or owner decision |
| PT12 | Privacy | consent and handling that suit the participants and the data |

### 3.4 Rule table of section 6 (3 rows, P2:263-267)

| rule | number | tag | source and date | P2 |
| --- | --- | --- | --- | --- |
| Method limitations are part of evidence | No universal sample size | EXPERIENCE | D13, 2009-03 | 265 |
| A large short test cannot establish long-term fit | 5,000 to more than 140,000 players; D7 29% to 38% | VERIFIED, studio-reported | D29, 2026-02-10; updated 2026-02-12 | 266 |
| Narrative intent should be checked against experience | No universal recall threshold | EXPERIENCE | D14, 2008-02 | 267 |

## 4. Section 7: pre-build critique and ranking fixes (P2:269-297)

### 4.1 Rules from the text

| id | rule (paraphrased) | tag | source | P2 |
| --- | --- | --- | --- | --- |
| 7.01 | Schell Games' official page describes lenses as perspective-specific questions for diagnosing experiences, and as a shared review language. It is not a publicly inspected scoring system and not a controlled validation study | EXPERIENCE | D27 | 271 |
| 7.02 | A critique is incomplete if it names an unwanted symptom without a plausible mechanism or an observable test | OPINION | none cited | 273 |
| 7.03 | Use an ordinal rubric, not a pseudo-scientific total. Mark each criterion Pass, Fail or Unproven. Unproven is not Pass, and is not a claim that the feature is bad. Never average a blocker away with attractive art or content volume | OPINION | none cited | 275 |
| 7.04 | Severity labels are proposed internal labels, not industry-standard numeric scores | OPINION | none cited | 275 |
| 7.05 | Rank fixes by explicit reasoning. Show the components; do not invent exact weighted arithmetic | OPINION | none cited | 277 |
| 7.06 | Prefer fixing the enabling cause over compensating for symptoms. Three examples: unreadable attack, so repair telegraph and camera before adding health; no strategic alternatives, so revise situations before adding upgrades; empty transit, so revise route and activity placement before raising movement speed everywhere | OPINION | none cited | 277 |
| 7.07 | When uncertainty is high and the decision is expensive, the best next task may be a test rather than a feature | OPINION | none cited | 277 |
| 7.08 | A feature is ready to build only when its unresolved questions are understood and accepted by the owner, not when a checklist has decorative ticks | OPINION | none cited | 280 |

Critique order (9 steps, P2:273, OPINION): (1) intended audience and promise; (2) causal loop; (3) choice and information; (4) skill and learning; (5) systemic consistency; (6) social consequences; (7) content feasibility; (8) time and monetization constraints; (9) evidence adequacy.

Severity scale (P2:275, OPINION):

| level | meaning |
| --- | --- |
| Blocker | contradicts the core promise, safety, fairness or feasibility |
| Major | frequent or substantial harm |
| Minor | local polish |

Fix-ranking components (7, P2:277, OPINION): harm magnitude, affected population, recurrence, downstream coupling, evidence confidence, reversibility, cost.

### 4.2 Feature review checklist (9 items, P2:279-289)

The paper's frame (OPINION): a feature is ready to build only when its unresolved questions are understood and accepted by the owner. The heading promises "reasons", but the paper gives none for these items (see W01).

| # | item | pass when | reason | tag | source | P2 |
| --- | --- | --- | --- | --- | --- | --- |
| F1 | Purpose | The feature supports a named player outcome and pillar; the cheaper alternative of omitting it was considered | not stated in the paper | OPINION | none cited | 281 |
| F2 | Behaviour | Inputs, states, transitions, consequences and interruptions are specified so two implementers would not build incompatible rules | not stated in the paper | OPINION | none cited | 282 |
| F3 | Authority | The rules say who decides shared outcomes and how disagreements, reconnects and duplicate actions resolve | not stated in the paper | OPINION | none cited | 283 |
| F4 | Craft fit | UI, VFX, sound, animation and world presentation communicate the same event and priority | not stated in the paper | OPINION | none cited | 284 |
| F5 | Acceptance | Criteria are observable in the build and cover failure and boundary paths, not only the happy path | not stated in the paper | OPINION | none cited | 285 |
| F6 | Measurement | The intended effect and the countervailing harms have defined observations; the chosen metric cannot be improved just by making the experience worse | not stated in the paper | OPINION | none cited | 286 |
| F7 | Dependency | Prerequisites, integration order, tuning references, content workload and migration needs are recorded | not stated in the paper | OPINION | none cited | 287 |
| F8 | Safety and policy | Relevant restrictions, abuse cases, accessibility needs and audience assumptions have been reviewed | not stated in the paper | OPINION | none cited | 288 |
| F9 | Decision | The owner has approved the necessary scope and tradeoff; proposed alternatives are not presented as final direction | not stated in the paper | OPINION | none cited | 289 |

### 4.3 Review finding template (13 fields, P2:291-292, tag OPINION)

| # | field | what goes in it |
| --- | --- | --- |
| FT1 | Finding ID | a stable reference |
| FT2 | Artifact and build | the exact revision |
| FT3 | Player consequence | what happens, and to whom |
| FT4 | Evidence mark | VERIFIED, EXPERIENCE or OPINION |
| FT5 | Evidence | observation, source, sample and context |
| FT6 | Reproduction or reasoning | steps or causal chain |
| FT7 | Severity rationale | harm, exposure, reversibility and dependency |
| FT8 | Minimal fix | a specific rule, data or content change |
| FT9 | Alternative | a different tradeoff |
| FT10 | Risks introduced | possible regression |
| FT11 | Acceptance check | an observable result |
| FT12 | Owner decision | pending, or the exact decision |
| FT13 | Resolution | verified result, or remaining uncertainty |

### 4.4 Rule table of section 7 (2 rows, P2:294-297)

| rule | number | tag | source and date | P2 |
| --- | --- | --- | --- | --- |
| Apply perspective-specific questions | Official page says more than 100 lenses | EXPERIENCE | D27, undated; accessed 2026-10-21 | 296 |
| Never average away a fundamental failure | Proposed ordinal rubric, not a benchmark | OPINION | Author synthesis 2026-10-21 | 297 |

## 5. Section 8: live content design (P2:299-316)

The section title says "not release engineering" (P2:299): it is about design of live content, not about how to ship it.

### 5.1 Rules from the text

| id | rule (paraphrased) | tag | source | P2 |
| --- | --- | --- | --- | --- |
| 8.01 | Supergiant says Hades' modular structure and narrative were designed to evolve with Early Access feedback | EXPERIENCE | D20 | 301 |
| 8.02 | 2XKO's 2025 balance statement values giving players time to develop counterplay and protecting learned core functionality, rather than changing things for novelty alone | EXPERIENCE | D21 | 301 |
| 8.03 | The stated 2026 intention was about five-week balance patches. Win rates of 47% and 53% were investigation triggers in that particular game: not universal intervention thresholds, and not proof of the actual later schedule | VERIFIED | D21 | 301 |
| 8.04 | A content plan states what kind of freshness each addition supplies. The paper lists 7 kinds: new decision, new combination, different social goal, expressive material, mastery ceiling, narrative development, recontextualized familiar content | OPINION | none cited | 303 |
| 8.05 | More items are not automatically more depth: they may dilute discovery, make choices unreadable, or invalidate old investments. Keep repeatable systemic variation apart from one-use authored content, and budget both honestly | OPINION | none cited | 303 |
| 8.06 | New rewards must not crowd out the ordinary activity the game wants players to enjoy. Repeated events should not rest only on fear of missing irreplaceable power | OPINION | none cited | 305 |
| 8.07 | After release, inspect exposure and adoption separately from outcomes. Track whether players reached the new decision and chose to return, not only whether an announcement caused a temporary spike | OPINION | none cited | 307 |
| 8.08 | Longer sessions can mean enjoyment, confusion, compulsion or a slower economy; read them together with other evidence | OPINION | none cited | 307 |
| 8.09 | Before any causal claim, separate balance fixes, content novelty, marketing effects and seasonal return patterns | OPINION | none cited | 307 |

Event or season review (9 points, P2:305, OPINION): entry requirements; late-join and comeback path; learning cost; meaningful activity; individual and team conflicts; intended stopping point; permanence or reset; effect on the existing economy; what stays valuable afterward.

Before release, name 6 things (P2:307, OPINION): audience, expected behavioral mechanism, success signal, harm guardrails, analysis window, alternative causes.

After release, compare 6 cohorts (P2:307, OPINION): new, existing, returning, solo, grouped, and relevant progression cohorts.

### 5.2 Update evaluation template (10 fields, P2:309-310, tag OPINION)

| # | field | what goes in it |
| --- | --- | --- |
| U1 | Update promise | the player benefit |
| U2 | Content and system changes | a versioned list |
| U3 | Eligible audience and exposure | who could experience it |
| U4 | Baseline and comparison | the same cohort, or a justified control; calendar and acquisition changes |
| U5 | Measures | engagement, return, quality, fairness, safety and technical health, as relevant to the change |
| U6 | Guardrails | unacceptable harms |
| U7 | Observation window | chosen from the mechanism and the available sample, not a generic duration |
| U8 | Rollout and recovery | approved release scope, monitoring and rollback |
| U9 | Result | measured values and uncertainty |
| U10 | Decision | keep, revise, revert or continue observing, with reasons |

### 5.3 Rule table of section 8 (3 rows, P2:312-316)

| rule | number | tag | source and date | P2 |
| --- | --- | --- | --- | --- |
| Cadence should protect learning as well as deliver novelty | About 5-week intention, not a general rule | EXPERIENCE/VERIFIED | D21, 2025-11-17 | 314 |
| Outlier metrics start an investigation | 47% / 53% for 2XKO at the source date | VERIFIED, scoped thresholds | D21, 2025-11-17 | 315 |
| Design modularity around intended evolution | No universal cadence | EXPERIENCE | D20, updated 2025-07-16 | 316 |

## 6. Section 9: process for an AI reviewer (P2:318-363)

### 6.1 AI review procedure (12 steps, P2:319-332, tag OPINION)

Frame: use it for a loop, economy, level plan or feature. It is an auditable reasoning method, not an automated substitute for creative direction (P2:320).

| # | step | detail | P2 |
| --- | --- | --- | --- |
| S1 | Identify | The artifact, its version, the owner decision and the question being asked. Keep approved intent apart from suggestions, references and discarded variants | 321 |
| S2 | Extract a causal model | Loop: goal, action, state change, feedback, next decision. System: stocks, flows, dependencies, incentives. Level: routes, information, challenge. Feature: inputs, states, outputs | 322 |
| S3 | Build a claim ledger | Mark each claim VERIFIED, EXPERIENCE or OPINION; keep the source date and scope; isolate unsourced values. Mark a proposed value as a hypothesis, not as a fact in an authoritative tone | 323 |
| S4 | Check internal consistency before aesthetic criticism | Follow a representative success path, a failure path, a boundary condition and the relevant multiplayer disagreement. Find contradictions among documents, tuning data, marketing and the actual build | 324 |
| S5 | Test against the approved fantasy and target players | Ask what a player does, perceives, chooses, learns and repeats. Do not replace the owner's desired experience with the evaluator's preferred genre | 325 |
| S6 | Apply the relevant pass/fail checklists | Each failure cites an observed example or a missing artifact. Record the kind of issue: observed player problem, implementation contradiction, plausible risk, or unresolved preference | 326 |
| S7 | Search for adversarial and cross-system cases | Where they apply: optimal-but-unfun strategies, griefing, collusion, dominant builds, resource runaway, reward farming, interrupted saves, low-information decisions | 327 |
| S8 | Rank fixes | By consequence, confidence, exposure, dependency and reversibility. No invented weighted score. Policy violations and data-loss risks can block release independently of uncertain taste judgments. Separate launch blockers from experiments and polish | 328 |
| S9 | Propose a minimal fix and an alternative | The alternative keeps a different tradeoff. State what changes, why it should help, what could get worse, the craft work needed, and how a test would tell the options apart | 329 |
| S10 | Present one recommendation to the owner | With the strongest contrary evidence. Ask for a decision only where direction, scope, cost or acceptable risk is still unresolved. Do not reopen settled decisions without material new evidence | 330 |
| S11 | After an approved change | Update the canonical specification and the tuning revision, verify integration, rerun the affected tests. A repaired local symptom does not show the whole design improved | 331 |
| S12 | Close the review | Give each finding one of 5 dispositions: fixed and checked, accepted risk, deferred with reason, rejected with reason, awaiting evidence. Keep failed hypotheses so the next agent does not rediscover them as new ideas | 332 |

### 6.2 "Do not do" list (9 items, P2:334-345)

| # | prohibition (paraphrased) | tag | source | P2 |
| --- | --- | --- | --- | --- |
| X1 | Do not report ideas as completed prototypes, and do not report historical project attrition as a universal quota | VERIFIED | D02, D03, D04, D05 (written "D02-D05") | 337 |
| X2 | Do not invent target session lengths, retention benchmarks, drop rates or difficulty tolerances. Put unsupported numbers into the assumptions ledger | OPINION | none cited | 338 |
| X3 | Do not let the fastest reward path displace the activity that defines the game. The Diablo III auction-house judgment is the case, not a blanket ban on markets | EXPERIENCE | D17 | 339 |
| X4 | Do not assume goals full of instructions preserve self-directed discovery. Don't Starve's abandoned task list is a counterexample | EXPERIENCE | D19 | 340 |
| X5 | Do not treat short-horizon beta retention as validation of long-term systems. Squad Busters' reported mismatch is the counterexample | VERIFIED | D29 | 341 |
| X6 | Do not read metrics without context, and do not accept every requested solution as the right cause | EXPERIENCE | D13, D16 | 342 |
| X7 | Do not copy another game's parameters without its mechanics, audience and evidence | OPINION | none cited | 343 |
| X8 | Do not equate more rewards with more meaningful progress, more health with fair difficulty, more content with depth, or more time played with player value | OPINION | none cited | 344 |
| X9 | Do not present the AI's imagined playthrough, invented personas or numerical model as human playtest evidence | OPINION | none cited | 345 |

### 6.3 Open questions and evidence limits (8 items, P2:347-356)

| # | open question or limit (paraphrased) | P2 |
| --- | --- | --- |
| Q1 | Which Roblox audience, devices, relationship contexts and session constraints apply to this studio? Resolve with current official platform facts and the studio's own cohort data | 349 |
| Q2 | What real D1, D7 and D30 baselines and distributions exist for the relevant Roblox genre? No cross-platform number in the dossier answers it | 350 |
| Q3 | What share of the intended experience is mastery, expression, discovery, social belonging, narrative or comfortable repetition? The owner must choose; the AI cannot infer it from revenue goals | 351 |
| Q4 | What sample size and duration are adequate for the specific decision? No source sets a transferable universal count | 352 |
| Q5 | How do proposed fairness aids behave under real input latency, camera, readability and adversarial multiplayer conditions? Kirby's single-player account does not settle it | 353 |
| Q6 | Which content, economy and social changes caused a measured retention change, and which only came with it? Most studio accounts here are not controlled experiments | 354 |
| Q7 | The widely repeated Zelda terrain-triangle account was not verified in an accessible primary transcript. Do not add it as established fact. Use the verified Nintendo affordance accounts and the Minecraft Education guidance instead | 355 |
| Q8 | Source dates for some surviving Iwata Asks and Blizzard pages are not displayed. Mark them undated; do not rebuild exact dates from memory. A game's release year is not a publication date | 356 |

### 6.4 Rule table of section 9 (4 rows, P2:359-363)

The paper's table header has no separator row and the table sits after the open questions (see W12).

| rule | number | tag | source and date | P2 |
| --- | --- | --- | --- | --- |
| Preserve units, population and time window with every value | No invented defaults | OPINION | Author synthesis 2026-10-21 | 360 |
| Distinguish analytic walk-throughs from player evidence | No synthetic playtest counts | OPINION | Author synthesis 2026-10-21 | 361 |
| Recommend fixes and discriminating tests without overriding the owner | No invented weighted total | OPINION | User brief and synthesis 2026-10-21 | 362 |
| Recheck the changed design in the actual build | Scope matched to the change | OPINION | Author synthesis 2026-10-21 | 363 |

## 7. Roblox platform facts (every Roblox fact in P2:179-366)

All tagged VERIFIED by the paper. R12 and R08 are live docs: the registry gives no publication date, only the access date 2026-10-21, so the pages can change. R32 is dated. The paper's own caveat for the whole group: roadmap announcements, including future offline play, are not capabilities that are available now (P2:232).

| # | fact | number | date of measurement | source | P2 | paper's caveat |
| --- | --- | --- | --- | --- | --- | --- |
| RF01 | Kids tier covers ages 5-8 | ages 5-8 | live doc, accessed 2026-10-21 | R12 | 230 | Described as current documentation |
| RF02 | Select tier is for age-checked users aged 9-15 | ages 9-15 | live doc, accessed 2026-10-21 | R12 | 230 | Described as current documentation |
| RF03 | There is an age-checked 16+ tier | age 16+ | live doc, accessed 2026-10-21 | R12 | 230 | The paper gives no name and no rules for this tier |
| RF04 | The tiers come with "transitional access conditions" | no number | live doc, accessed 2026-10-21 | R12 | 230 | The conditions are not listed |
| RF05 | Availability to players under 16 involves: verification, 2FA, suitable maturity labels, fee or subscription requirements, and evaluation | 5 items listed (2FA = two-factor authentication) | live doc, accessed 2026-10-21 | R12 | 230 | The fee or subscription amounts and the verification method are not given |
| RF06 | The current threshold is 250 unique plays by highly engaged age-checked users within 60 days; the paper says these are not arbitrary visits | 250 unique plays; 60 days | live doc, accessed 2026-10-21 | R12 | 230 | The paper does not say which step or tier the threshold gates (W06). "Highly engaged" is not defined |
| RF07 | Chat access varies with tier, consent and region | no number | live doc, accessed 2026-10-21 | R12 | 230 | No detail on which chat features apply where; the paper stops at this one sentence |
| RF08 | Intentional co-play is a current discovery signal. The paper lists joins, invites and private servers as part of it | no number | live doc, accessed 2026-10-21 (R08); announcement 2026-09-11 (R32) | R08, R32 (cited together) | 232 | A platform signal, not proof that any particular reward causes healthy cooperation. The paper does not say which source holds which part (W07) |
| RF09 | Roblox's September 2026 announcement describes discovery as increasingly age-aware | September 2026 (registry date 2026-09-11) | 2026-09-11 | R32 | 232 | n/a |
| RF10 | Roadmap announcements, including future offline play, are not automatically available capabilities | no number | not stated | R08, R32 (cited together) | 232 | Treat as a rule for reading announcements, not as a feature list |

## 8. Source table (every ID cited in P2:179-366)

Titles are as in the registry; the .txt dropped punctuation, so titles are lightly restored. "Excerpt" shows the registry's key excerpt only when it is under 10 words (and only the part that fits for D05, D21, D03, R08, R12). "Scope" is the registry's scope note paraphrased; the registry gives no scope line for R-sources. Registry notes (P2:369): dates separate publication, revision and measurement; the registry supports facts and attributed practices, while templates and operating rules are OPINION. Every URL was marked as inspected or verified by the primary-source research (P2:369); I did not open any.

| ID | title | author or org | date | URL | registry evidence | excerpt | scope note (paraphrased) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| D02 | Ask the Developer Vol. 11: Super Mario Bros. Wonder, Chapter 1 | Nintendo (Tezuka, Mouri, Hayashida, Sato, Kondo) | 2023-10-17 | https://www.nintendo.com/en-gb/News/2023/October/Ask-the-Developer-Vol-11-Super-Mario-Bros-Wonder-Chapter-1-2460393.html | EXPERIENCE; VERIFIED reported count | "There were just so many ideas." | Nintendo-hosted recollection; counts verified as reported, not audited |
| D03 | Iwata Asks: Splatoon, 2. Then Rabbits | Nintendo (Iwata and the Splatoon team) | undated; accessed 2026-10-21 | https://www.nintendo.com/en-za/Iwata-Asks/Iwata-Asks-Splatoon/Splatoon/2-Then-Rabbits/2-Then-Rabbits-1021367.html | EXPERIENCE; VERIFIED reported counts | "having that prototype to play with" (part of a longer excerpt) | Seventy is an idea count, not a count of implemented prototypes. The interview concerns the first Splatoon |
| D04 | Ilkka Paananen BAFTA Games Lecture | Ilkka Paananen | 2016-09-06 | https://www.bafta.org/media-centre/press-releases/ilkka-paananen-bafta-games-lecture/ | EXPERIENCE; VERIFIED scoped reported counts | "these are not just some early prototypes." | Not a denominator of all ideas or prototypes; does not imply a universal 90% prototype kill target; founder account, not an audited experiment |
| D05 | The Next Chapter of Supercell | Ilkka Paananen | 2023-02-15 | https://supercell.com/en/news/next-chapter/ | EXPERIENCE; VERIFIED historical reported counts | "launched 5 hit games but we have killed 30+" (part of a longer excerpt) | Historical self-report, not the current portfolio, and not an all-ideas denominator |
| D10 | The Structure of Fun: Learning from Super Mario 3D Land's Director | Christian Nutt interviewing Koichi Hayashida | 2012-04-13 | https://www.gamedeveloper.com/design/the-structure-of-fun-learning-from-i-super-mario-3d-land-i-s-director | EXPERIENCE | "you have a clear concept in the beginning" | Primary interview hosted by trade press. Not a claim that every Nintendo level, or Super Mario 3D World, came from this exact account |
| D11 | The AI Systems of Left 4 Dead | Michael Booth, Valve | 2009 (no month) | https://cdn.fastly.steamstatic.com/apps/valve/2009/ai_systems_of_l4d_mike_booth.pdf | VERIFIED documented implementation; EXPERIENCE claimed design benefit | "Algorithm adjusts pacing, not difficulty" | Zero-indexed PDF pages are cited. The parameters belong to this L4D implementation, not to universal timing standards |
| D12 | Replayable Cooperative Game Design: Left 4 Dead | Michael Booth, Valve | 2009-03 | https://cdn.fastly.steamstatic.com/apps/valve/2009/GDC2009_ReplayableCooperativeGameDesign_Left4Dead.pdf | EXPERIENCE | "Ensure cooperation is the only winning strategy" | A case-specific cooperative design argument, not proof that forced dependence suits every multiplayer game |
| D13 | Valve's Approach to Playtesting: The Application of Empiricism | Mike Ambinder, Valve | 2009-03 | https://cdn.akamai.steamstatic.com/apps/valve/2009/GDC2009_ValvesApproachToPlaytesting.pdf | EXPERIENCE | "Averages hide extreme examples" | Do not report simulated charts as measured results. No universal sample size or fun threshold is established |
| D14 | Integrating Narrative and Design: A Portal Post Mortem | Kim Swift and Erik Wolpaw, Valve | 2008-02 | https://cdn.akamai.steamstatic.com/apps/valve/2008/GDC2008_PortalPostMortem.pdf | EXPERIENCE | "Adjust story to enhance what players are already feeling." | A studio postmortem, not a controlled causal estimate of narrative effectiveness |
| D16 | Slay the Spire: Metrics Driven Design and Balance | Anthony Giovannetti, Mega Crit | 2019 | https://media.gdcvault.com/gdc2019/presentations/Giovannetti_Anthony_SlayTheSpire.pdf | EXPERIENCE; VERIFIED reported historical counts | "Data is evidence, but not a conclusion." | Content counts are historical. Feedback-message counts, if used, are not unique testers. Does not prove that metrics alone caused the success |
| D17 | Diablo III Auction House Update | John Hight, Blizzard Entertainment | undated (registry); "VERIFIED announced date" is also noted | https://news.blizzard.com/en-gb/article/10974978/diablo-iii-auction-house-update | EXPERIENCE; VERIFIED announced date | "it ultimately undermines Diablo's core game play" | A developer's causal judgment, not a measured controlled effect. The publication date is not shown on the inspected page. Applies to this game's goal, not to all trading systems |
| D19 | Intrinsic vs. Extrinsic rewards | Jamie Cheng and Kevin Forbes, Klei Entertainment | 2012; updated 2025-05-21 | https://support.klei.com/hc/en-us/articles/360035456011-Intrinsic-vs-Extrinsic-rewards | EXPERIENCE | "made it feel like a list of chores." | A studio experience, not a universal reward-crowding effect, and not a check of the psychology studies cited inside the essay |
| D20 | Hades FAQ | Supergiant Games | 2018-12-07; updated 2025-07-16 | https://www.supergiantgames.com/blog/hades-faq/ | EXPERIENCE | "a real sense of place and story to it" | The FAQ describes design intent and features, not controlled retention effects and not a cadence benchmark |
| D21 | 2XKO: Live Balance Philosophy | Patrick "pattheflip" Miller, Riot Games | 2025-11-17 | https://2xko.riotgames.com/en-us/news/dev/2xko-live-balance-philosophy/ | EXPERIENCE; VERIFIED stated intentions and triggers | "not interested in changing things" (part of a longer excerpt) | A dated intended cadence, not a check of the real later schedule. Thresholds are specific to this game; spotting an outlier does not prescribe the fix |
| D22 | [Dev] Making Matchmaking Better | RiotSapMagic and GET IN GAME, Riot Games | 2018-03-14 | https://www.leagueoflegends.com/en-gb/news/dev/dev-making-matchmaking-better/ | EXPERIENCE | "create fair matches" | A historical League retrospective, not a universal queue-time target, and not evidence for forced win or loss patterns |
| D23 | Player Dynamics Design: Looking Behind the Curtain | Weszt "Vonburgermeister" Hart, Riot Games | 2022-05-12 | https://www.riotgames.com/en/news/player-dynamics-design-looking-behind-the-curtain | EXPERIENCE | "to change behavior, change the environment." | A practitioner framework; the article establishes no general, quantified drop in toxicity |
| D24 | Minecraft: Education Edition Design Guide | Mojang/Microsoft, Minecraft Education | 2021-06 | https://education.minecraft.net/content/dam/education-edition/software-downloads/Minecraft_Education_Edition_Design_Guide_June_2021.pdf | EXPERIENCE; VERIFIED documented guidance | "DO NOT: Confuse scenery for content" | Scope is designed classroom worlds. Do not carry old technical limits or timing numbers over to current Minecraft or to Roblox |
| D27 | The Art of Game Design | Schell Games | undated; accessed 2026-10-21 | https://schellgames.com/art-of-game-design/ | EXPERIENCE; VERIFIED overview description | "a specific perspective or a mental checklist." | An official overview, not the full book. Do not invent lens numbers or book quotations. No validated total scoring model is established |
| D29 | The Best Games Haven't Been Made Yet | Ilkka Paananen | 2026-02-10; updated 2026-02-12 | https://supercell.com/en/news/the-best-games-havent-been-made-yet/ | EXPERIENCE; VERIFIED reported test counts and metrics | "Don't skip testing meta and long term retention." | Self-reported; not a transferable Roblox benchmark; not a controlled causal result |
| R08 | Discovery: current ranking signals and content quality restrictions | Roblox | undated live doc; accessed 2026-10-21 | https://create.roblox.com/docs/discovery | VERIFIED | "organically joined from the Recommended" (part of a longer excerpt) | none given in the registry |
| R12 | Roblox Kids and Select | Roblox | undated live doc; accessed 2026-10-21 | https://create.roblox.com/docs/production/publishing/kids-and-select | VERIFIED | "250 unique plays by highly engaged age-checked users" (part of a longer excerpt) | none given in the registry |
| R32 | RDC 2026: The World Needs More Play | Roblox | 2026-09-11 | https://about.roblox.com/newsroom/2026/09/rdc-2026-the-world-needs-more-play | VERIFIED | "Our discovery ranking system is increasingly age-aware" | none given in the registry |
| U01 | User supplied research brief | Studio owner | provided 2026-10-21 | the two research prompts supplied by the owner for these papers (no URL) | OPINION studio operating instruction | "The agent proposes and documents; the owner decides." | The two prompts set the requested scope, the final three pitches and the owner's decision rights. Cited in P2:362 only as "User brief", not by the ID |

Named without an ID in P2:179-366: Kirby's single-player account (P2:353) matches registry entry D06 (Ask the Developer Vol. 4, Kirby and the Forgotten Land, Nintendo/HAL Laboratory, 2022-03-24; scope: no universal tolerance or measured effect size, and a single-player accessibility and feel case that does not set competitive collision rules); the Zelda "verified Nintendo affordance accounts" (P2:355) match D08 and D09 (Tears of the Kingdom, 2023-05-09). These matches are my reading of the text; the paper does not give the IDs in this range.

## 9. Claims to fact-check (every number and Roblox fact in P2:179-366)

Fact-checking is a separate ticket; nothing here has been checked against the web. Count: 36 rows.

| # | claim | P2 line | source |
| --- | --- | --- | --- |
| 1 | Kids tier is for ages 5-8 | 230 | R12 |
| 2 | Select tier is for age-checked 9-15 | 230 | R12 |
| 3 | There is an age-checked 16+ tier, with transitional access conditions | 230 | R12 |
| 4 | Under-16 availability needs verification, 2FA, suitable maturity labels, fee or subscription requirements and evaluation | 230 | R12 |
| 5 | Threshold: 250 unique plays by highly engaged age-checked users within 60 days | 230 | R12 |
| 6 | Chat access varies with tier, consent and region | 230 | R12 |
| 7 | Intentional co-play (joins, invites, private servers) is a current discovery signal | 232 | R08, R32 |
| 8 | September 2026 announcement: discovery increasingly age-aware (registry date 2026-09-11) | 232, 621 | R32 |
| 9 | Future offline play is a roadmap announcement, not an available capability | 232 | R08, R32 |
| 10 | Hayashida: 3D Land was where he became strict about the four-stage level concept; evolved through Galaxy and Galaxy 2; stage length tied to short train journeys; interview date 2012-04-13 | 181, 211 | D10 |
| 11 | Left 4 Dead AI: peak held 3-5 s; relax 30-45 s or enough forward travel; bosses outside adaptive pacing; four phases; year 2009 | 185, 212 | D11 |
| 12 | Minecraft Education Edition design guide (June 2021) separates paths, breadcrumbs, landmarks, waypoints, soft and hard boundaries, decorative size from playable content | 187, 213 | D24 |
| 13 | Left 4 Dead: enemies create rescue needs and punish separation; resource sharing and automatic callouts; designers rejected invisible leashes and teleporting stragglers; 4 survivors in the case; 2009-03 | 217, 238 | D12 |
| 14 | Riot matchmaking: tradeoff among 3 objectives (fair matches, preferred positions, queue duration); retrospective dated 2018-03-14 | 219, 239 | D22 |
| 15 | Riot player dynamics: harmful interaction as partly an environment-design problem; 2022-05-12 | 219, 240 | D23 |
| 16 | Valve playtesting: 6 methods and their weaknesses; some displayed statistics labelled simulated; 2009-03 | 244, 265 | D13 |
| 17 | Portal postmortem: narrative revisions tied to what players feel; companion-cube obstacle setup removed; 2008-02 | 244, 267 | D14 |
| 18 | Squad Busters closed betas: 5,000 players, then more than 140,000 | 246, 266 | D29 |
| 19 | Squad Busters D7 retention 29% then 38% | 246, 266 | D29 |
| 20 | Second beta: D1 61%, D3 44% | 246 | D29 |
| 21 | Supercell team said beta-to-global behavior differed and testing of meta and long-term retention was insufficient | 246 | D29 |
| 22 | D29 dates: 2026-02-10, updated 2026-02-12 | 266 | D29 |
| 23 | The source's warning about drawing conclusions from 100,000-plus players (the paper's own reading of it) | 246 | D29 |
| 24 | Schell Games' official page describes lenses as perspective-specific questions and a shared review language | 271 | D27 |
| 25 | Schell Games' official page says more than 100 lenses | 296 | D27 |
| 26 | Hades: modular structure and narrative designed to evolve with Early Access feedback; FAQ 2018-12-07, updated 2025-07-16 | 301, 316 | D20 |
| 27 | 2XKO 2025 balance statement values counterplay time and protecting learned core functionality | 301 | D21 |
| 28 | 2XKO stated 2026 intention: about five-week balance patches | 301, 314 | D21 |
| 29 | 2XKO win rates of 47% and 53% as investigation triggers | 301, 315 | D21 |
| 30 | D21 date 2025-11-17 | 314, 315 | D21 |
| 31 | "Do not do" X1: idea counts and project attrition (D02-D05) must not be read as completed prototypes or a universal quota | 337 | D02, D03, D04, D05 |
| 32 | Diablo III auction-house removal judged to undermine the core loop | 339 | D17 |
| 33 | Don't Starve (Klei): explicit task list displaced discovery | 340 | D19 |
| 34 | Squad Busters: beta retention did not validate long-term systems | 341 | D29 |
| 35 | Zelda terrain-triangle account was not verified in a primary transcript | 355 | none (paper's own statement) |
| 36 | Some Iwata Asks and Blizzard pages show no date | 356 | not given (D03, D07, D17, D18 match by the registry's "undated" entries) |

## 10. Contradictions and weak spots

Nothing here is fixed; it is for the lead and the fact-check ticket.

| id | problem | P2 lines |
| --- | --- | --- |
| W01 | The feature review checklist heading promises "reasons" but none of its 9 items has one. The level checklist (9 items) does give a reason per item. The only reason-like text for the feature checklist is the frame sentence (ready to build only when the owner accepts the open questions) | 279-289, 197-207 |
| W02 | Rule table row 1 of section 4 tags "four-step teaching" EXPERIENCE with D10, but the text (L183) says the four-step sequence is an OPINION adaptation. The two lists of four also differ. D10's stages (L181): learning, complication, unexpected variation, demonstration of mastery. The L183 steps: low-confound exposure, demanding arrangement, altered relationship, independent application. The row title ("exact game attribution") reads stronger than the text, which says the stages evolved across games and are not a formula | 181, 183, 211 |
| W03 | D11 pacing numbers (3-5 s peak, 30-45 s relax "or sufficient forward travel") have no month in the date (2009) and "sufficient forward travel" has no distance. The text tags the sentence VERIFIED; the registry splits it (VERIFIED implementation, EXPERIENCE for the claimed benefit). The paper itself says these are not Roblox clocks | 185, 212, 432 |
| W04 | The number "4 survivors in the case" (D12) appears only in the rule table, not in the text of section 5 and not in the registry entry. D12's key excerpt ("cooperation is the only winning strategy") points the opposite way from the paper's own advice against compulsory dependence (L217); the registry scope note handles this as a case-specific argument. L217 mixes an EXPERIENCE sentence and an OPINION sentence in one paragraph | 217, 238, 439-441 |
| W05 | The "more than 100 lenses" figure (D27, L296) conflicts with the registry's scope note for D27, which says not to invent lens numbers; the registry key excerpt does not carry a number. The number appears only in the rule table, not in the text of section 7 | 271, 296, 531 |
| W06 | R12 threshold: the paper does not say what 250 unique plays within 60 days gates (it follows the sentence on under-16 availability and "evaluation", but it never says it applies to that step, to Kids, or to Select). "Highly engaged" has no definition. The "16+ tier" has no name, and "transitional access conditions", fee or subscription requirements, and verification method are named but not described. Chat access has one sentence ("varies with tier, consent and region") and no specifics, although the section is titled "Roblox communication". R12 is a live doc with an access date only | 229-230 |
| W07 | Section 5's Roblox paragraph cites R08 and R32 together for both the co-play discovery signal and the roadmap caveat. The paper does not say which source holds which statement. The registry's R08 excerpt is about users who organically joined from Recommended and does not itself show co-play, invites or private servers. The R32 excerpt supports only "age-aware". The mention of future offline play has no registry text behind it | 232, 581-583, 620-623 |
| W08 | Section 5's rule table has no row for the Roblox facts (R12, R08, R32) and none for the group lifecycle, competition, status or abuse rules (all OPINION, none cited). The row "Prevention belongs in game structure" has no number, only "no effect size established" | 221-240 |
| W09 | D29: the table row titled "A large short test cannot establish long-term fit" lists numbers (D7 29% to 38%) that rose between betas, while the lesson comes from a beta-to-global gap for which the paper gives no numbers. The mapping of 29% to the first beta and 38% to the second is read from the order of words ("then"). D1 61% and D3 44% appear in the text but not in the table. Retention definition, platform and cohort are not given. Tag mix inside one paragraph: VERIFIED (numbers, studio-reported), EXPERIENCE (mistake statement), untagged practitioner interpretation (100,000-plus warning). The game name Squad Busters is not in the registry title | 246, 266, 540-543 |
| W10 | The fix-ranking criteria differ across three places. Section 7 lists 7 components: harm magnitude, affected population, recurrence, downstream coupling, evidence confidence, reversibility, cost. Procedure step 8 lists 5: consequence, confidence, exposure, dependency, reversibility (no cost, no recurrence, no population). The finding template's severity rationale lists 4: harm, exposure, reversibility, dependency. The paper gives no rule for which list to use and no combining rule | 277, 292, 328 |
| W11 | Blocker is defined as contradicting the core promise, safety, fairness or feasibility (L275). Step 8 says policy violations and data-loss risks can block release independently (L328). Policy and data loss are not named in the Blocker definition, so a reader could rank them Major | 275, 328 |
| W12 | The section 9 rule table (4 rows) has a malformed header (no separator row), sits after the open-questions list, and has no D, R or U source ID: the sources are "Author synthesis" and "User brief and synthesis". The registry's ID for the brief is U01, but the table does not use it. Its "number" column holds phrases ("No invented defaults", "Scope matched to the change"), not numbers | 359-363, 625-629 |
| W13 | "Do not do" items X1 and X5 carry the VERIFIED tag on a prohibition. The tag fits the underlying counts, not the instruction. X1 cites the range "D02-D05", four sources with different scopes, and gives no numbers (the counts are in P2:35-37, outside this range) | 337, 341 |
| W14 | D17 is "undated" in the registry, yet its evidence line reads "VERIFIED announced date". The only announced date in the paper is in a table row outside this range (P2:175, "removal planned for 2014-03-18"). Open question Q8 also says Blizzard pages show no date | 175, 356, 467-471 |
| W15 | The 47% / 53% win-rate thresholds (D21) have no scope: which characters or players, which rank or population, which sample size, which window. The row tag is mixed (EXPERIENCE/VERIFIED). The text says the intention is for 2026 while the source date is 2025-11-17. "About five weeks" does not say whether it covers global or all balance patches | 301, 314, 315 |
| W16 | The playtest template has a Privacy field ("consent and handling appropriate to the participants") but no rule on who may be tested. Roblox's age tiers (L230) and the audience rules are not tied to recruiting or consent anywhere in section 6 | 251, 261, 230 |
| W17 | Sections 6 and 7 define methods (the protocol, both templates, the rubric, severity labels) that are all OPINION and have no evidence of effectiveness. The paper says so itself for the rubric; it should be applied as a process, not quoted as an industry standard | 248, 260, 275, 291 |
| W18 | Open question Q5 refers to "Kirby's single-player account" and Q7 to "verified Nintendo affordance accounts" without IDs in this range. Neither question is answered anywhere in P2:179-366 | 353, 355 |
| W19 | The paper's research date (21 October 2026) and all registry access dates are one day after the date on this kit file (2026-10-20) | 369 |
| W20 | The "Do not do" ban on invented retention benchmarks (X2) and the open question on Roblox D1/D7/D30 baselines (Q2) mean the paper supplies no Roblox retention number. The only retention numbers in this range (D29: 29%, 38%, 61%, 44%) are from another game and platform and must not be used as targets | 246, 338, 350 |
