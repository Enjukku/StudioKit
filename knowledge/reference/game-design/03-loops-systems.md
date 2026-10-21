---
type: reference
scope: universal
status: active
updated: 2026-10-20
source: J003
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-20

Source file: `Game_Designer_Part_2_Research.txt`, lines 1-178 (plus registry entries, lines 367-630, for every cited ID); paraphrased; the paper stays outside git.

# Game design research, part 2A: loops, scales, prototypes, principles, systems, economies (paper lines 1-178)

## 0. How to read this file

Cite as `P2:<line>` plus the paper's own IDs, e.g. `P2:61 [R06]`. A tag stays with its claim. UNSPECIFIED in this file means "the paper gives no value"; it is not zero and not a default.

| field | value |
| --- | --- |
| Paper | "Game Designer Research Part 2: The Craft of Design Review" (P2:1) |
| Research cutoff | 21 October 2026 (P2:18). Source access dates in the registry are also 2026-10-21 |
| Audience stated | the AI game designer that supports an owner-led Roblox studio; the owner decides, the agent reviews, diagnoses and proposes (P2:18) |
| Companion | Part 1 covers ideas, hooks, preproduction and implementation briefs (P2:18). Not in this file |
| Craft vs platform | Roblox sources give platform facts only; the craft foundation comes from other industry sources (P2:20) |
| Lines not covered here | P2:179 onward (section 4 levels and encounters, and later). Registry entries not cited in P2:1-178 are listed after the source table |

Tag meanings (P2:20), in my words:

| tag | meaning | do not read it as |
| --- | --- | --- |
| VERIFIED | Official facts that were inspected directly, or published measurements within their stated scope. Studio-reported numbers count as verified "as reported", not independently audited | Proof that the number is audited, or that the practice works in every game |
| EXPERIENCE | An attributed practitioner's account or judgment | A controlled study |
| OPINION | The paper's own method, interpretation or value choice (also used for outside authors' theories, tagged "author framework" or "author theory") | An observed result |

Paper reminders that apply to every row: undated material keeps its access date (P2:20); the checklists are the paper's operationalisation, not validated predictors (P2:69, P2:158 intro says run every applicable item); policy facts are a dated snapshot and must be rechecked before launch (P2:154).

## 1. The 15 summary rules (P2:2-16)

Rule k sits on paper line k+1. "Body support" says where lines 22-177 discuss the rule; "none in range" means the body of P2:22-177 never uses the cited ID for that point (see weak spots W01-W03).

| # | rule (paraphrased) | tag | source IDs | P2 line | body support in P2:22-177 |
| --- | --- | --- | --- | --- | --- |
| 1 | Judge a design against the experience it intends (a decision, expression, comfort or a social experience), not against how much content it holds | OPINION | D01, D25, D26 | 2 | loops P2:26-33; disagreements P2:114 |
| 2 | Cook's learning loop links action, the system's response, feedback and a changed understanding; a narrative arc does not have to repeat | OPINION, author framework | D01 | 3 | P2:26, P2:29 |
| 3 | The "more than 2,000" Wonder figure counts sticky-note ideas; it is not a count of finished prototypes | VERIFIED | D02 | 4 | P2:37, P2:85 |
| 4 | Supercell's "one release, nine killed" covers two years and includes advanced projects, not only early prototypes | VERIFIED | D04 | 5 | P2:37, P2:87 |
| 5 | Prototype the uncertainty that could invalidate the game before polishing presentation | OPINION | D02-D05 | 6 | gate P2:41-45 (sources there give counts, not this rule; W05) |
| 6 | Nintendo examples keep rules understandable while letting familiar actions be used in new ways | EXPERIENCE | D06, D09 | 7 | P2:94, P2:98 (body shows leniency in feel and consistent affordance signs, not "new uses"; W04) |
| 7 | A strategic choice depends on context; expressive or comfortable play can serve other valid goals | OPINION | D08, D26 | 8 | P2:98, P2:114 |
| 8 | Valve's Left 4 Dead account separates how often pacing events come from how hard they are | VERIFIED | D11 | 9 | none in range (W03) |
| 9 | Mega Crit uses metrics together with expert play, community feedback and observed play | EXPERIENCE | D16 | 10 | P2:133 |
| 10 | Model creation, destruction, conversion and transfer of each resource separately before tuning rewards | OPINION | D28 | 11 | P2:127-131 |
| 11 | Blizzard removed an auction system it judged was undermining the intended monster-to-loot loop | EXPERIENCE | D17 | 12 | P2:137 |
| 12 | Klei found that an explicit task list pushed out discovery in its own survival game | EXPERIENCE | D19 | 13 | P2:116 |
| 13 | Matchmaking, cooperation incentives and room for abuse are part of design, not only post-launch moderation | OPINION | D12, D22, D23 | 14 | none in range (W03) |
| 14 | Test with the real audience at the real stage of progression; many early testers cannot show long-term validity | OPINION | D13, D29 | 15 | none in range (W03) |
| 15 | An AI reviewer should deliver evidence, failure mechanisms, options and tests that can fail; the creative director decides | OPINION | U01 | 16 | none in range; the source is the owner's own brief (W03) |

## 2. Section 1: core loops, scales, coupling, prototypes (P2:22-90)

### 2.1 Loop definition and arcs

| claim | tag | source | P2 |
| --- | --- | --- | --- |
| A loop is a repeated exchange between the player's mental model and a system that responds. An arc delivers an experience that may be consumed once. Cook treats both as ingredients, not rival genres | OPINION, author framework | D01 | 26 |
| Cook allows deliberate mixtures of one-shot arcs and repeatable loops | OPINION, author framework | D01 | 114 |
| A click, then an animation, then currency may be an interaction loop; it is not automatically a learning loop | OPINION | none cited | 29 |

### 2.2 The three scales (analytic scales, not timing standards)

| scale | sequence the paper lists | what the paper says to ask or do | what the paper warns | tag | source | P2 |
| --- | --- | --- | --- | --- | --- | --- |
| Moment | perceive a state, choose an action, execute it, perceive the consequence | Ask what information changes the next decision (the only scale with an explicit question; W06) | A click-animation-currency chain is not automatically a learning loop | OPINION | none cited | 29 |
| Session | select a purpose, prepare, do a bounded activity, resolve outcomes, reflect or change plan, stop or continue | Record the real distribution of session durations for the game | Do not assign every game a prescribed number of minutes. A run, a match, a building project or a social gathering can set the boundary | OPINION | none cited | 30 |
| Long term | choose an aspiration, develop skill, resources, relationships or expression, face changed possibilities, reassess the aspiration | Use days and weeks as an analysis horizon | Not a licence to require daily attendance | OPINION | none cited | 31 |

Opening statement (P2:28): the three scales are analytical tools, not universal timing standards.

### 2.3 Coupling between scales

| rule | tag | source | P2 |
| --- | --- | --- | --- |
| Draw the chain explicitly: session entry state, then moment decisions, then session outcome, then retained state, then changed options for the next session | OPINION | none cited | 33 |
| Label what resets, what persists and why | OPINION | none cited | 33 |
| If the only lasting change is a bigger multiplier that meets proportionally bigger costs, ask whether the next experience changes in a way the intended player values (anticipation, expression, comfortable accumulation count). This is an investigation, not an automatic rejection of incremental games | OPINION | none cited | 33 |
| If meta rewards make the most effective route skip the intended moment-to-moment play, the systems conflict | OPINION | none cited | 33 |

### 2.4 Prototype evidence: what each count covers

| case | count | exactly what it counts | what it does NOT count | source, date | tag | P2 |
| --- | --- | --- | --- | --- | --- | --- |
| Splatoon (first game, original interview) | 70 ideas; a prototype selected from them; 4 vs 4 already played | ideas, and the interaction scale of the chosen prototype | not 70 playable prototypes | D03, undated | VERIFIED (reported counts); registry also EXPERIENCE | 35, 86 |
| Splatoon lesson | no number | character and arena changes temporarily damaged the functional meaning of hiding and ink. Lesson: keep the tested interaction when presentation changes; it does not mean every studio must start with featureless cubes | n/a | D03 | EXPERIENCE | 35 |
| Super Mario Bros. Wonder | more than 2,000 sticky notes, then ideas chosen for prototypes | sticky-note ideas | not completed prototypes | D02, 2023-10-17 | VERIFIED (reported count; not independently audited per registry) | 4, 37, 85 |
| Supercell, 2016 lecture | 1 release and 9 killed games in the preceding 2 years | two years of games; many were advanced projects | not early prototypes only; not a denominator of all ideas or prototypes | D04, 2016-09-06 | VERIFIED (reported count) | 5, 37, 87 |
| Supercell, 2023 post | 5 hit launches and 30-plus kills by the author's latest count | historical self-report | not a current portfolio; not all-ideas denominator | D05, 2023-02-15 | VERIFIED (reported) | 37, 88 |

Paper's conclusion on these counts (P2:37, OPINION): none of the denominators supports a universal prototype quota or a target kill percentage. The 2023 statement is a snapshot of history. Registry scope for D04 adds: it does not imply a universal 90% kill target; it is a founder account, not an audited experiment.

### 2.5 Prototype review gate (OPINION, P2:39-45)

Required: a one-page experiment card with these 8 fields (P2:41).

| # | field |
| --- | --- |
| 1 | player promise |
| 2 | riskiest assumption |
| 3 | smallest playable situation that exposes it |
| 4 | target players |
| 5 | help the facilitator is allowed to give |
| 6 | observations |
| 7 | a contrasting explanation |
| 8 | the decision after the test |

| rule | tag | source | P2 |
| --- | --- | --- | --- |
| Test action feel separately from the long-term aspiration when needed, then test them combined. A paper economy model cannot show motor feel; a polished combat room cannot show a month-long economy | OPINION | none cited | 41 |
| PASS when the build can answer the risky question and the team can name a result that would make it change or drop the idea | OPINION | none cited | 43 |
| FAIL when success is defined as "testers liked it" | OPINION | none cited | 43 |
| FAIL when the only test is the designer demonstrating expert play | OPINION | none cited | 43 |
| FAIL when every disappointing result is blamed on missing polish without evidence | OPINION | none cited | 43 |
| Evidence of promise is triangulated, never a single metric. Look for: players understand an immediate intention; actions produce legible consequences; alternatives respond to context; players find or state a better strategy; repeats differ in a meaningful way; the intended audience chooses to continue when free to stop | OPINION | none cited | 45 |
| Confounds that can fake these signs: novelty, politeness, prizes for testing, no alternative available | OPINION | none cited | 45 |

### 2.6 Roblox audience and loop constraints (rules; the numbers are in section 5)

| rule | tag | source | P2 |
| --- | --- | --- | --- |
| The device split is an average over the year and over daily active users. It is not a 2026 measurement and not a session share. The 2.7 hours per DAU per day is an aggregate over the platform and the day, not a typical game session | VERIFIED | R01 | 49 |
| Age-check shares cover only the age-checked subset; they are not whole-platform age shares and are not directly comparable with older self-reported ages | VERIFIED | R02 | 50 |
| Regional DAU figures are counts of account activity, not a country-level market forecast | VERIFIED | R03 | 52 |
| Test the intended device, input and social setup; do not picture one typical Roblox player | OPINION | none cited | 54 |
| Mobile reach supports testing on mobile. It is not a rule that every loop must be short or shallow | OPINION | none cited | 54 |
| Age and region affect understanding, communication access and eligibility. They do not set an individual's taste or skill | OPINION | none cited | 54 |

### 2.7 Retention and session measurements, no invented targets

| rule | tag | source | P2 |
| --- | --- | --- | --- |
| Roblox defines average session time as total time divided by number of sessions, and separately shows how many new users are still present at each minute of their first session | VERIFIED | R04 | 57 |
| Roblox's advice to reach enjoyable play within the first five minutes is guidance. It is not a universal attention span and not a five-minute session target | VERIFIED | R04 | 57 |
| D1, D7, D30 measure exact-day returns by first-play cohort. Day 0 is first play; D7 is the eighth calendar day in this convention. Blank cells for cohorts that are too young are not zero. Changes in acquisition can change the cohort mix. The docs publish no universally good D1, D7 or D30 threshold | VERIFIED | R05 | 59 |
| Similar-game benchmarks update daily and show bands from the 50th to the 90th percentile. Comparison games have at least 100 DAU; the set can change and may fall back to genre or wider comparisons. The example D1 band of 12.11% to 18.73% shows how to read the chart; it is not a target. Overall-success tiers use a different comparison (top-1000 by rolling 30-day playtime) | VERIFIED | R06 | 61 |
| Discovery uses a 28-day horizon with early and later signals, so a new game need not wait 28 days to be distributed. The playtime ranking cap is 60 minutes per user per game per day; it is not a session limit. Cohort benchmarks are not direct ranking inputs | VERIFIED | R07, R08, R09 | 63 |
| Review the distribution and the segment, not only an average: new vs returning, acquisition source, device, region, party context where available | OPINION | none cited | 65 |
| D1 can point to an opening failure, D7 to weak reasons to continue, D30 to long-term problems; none of them proves a specific cause | OPINION | none cited | 65 |
| No public evidence in the paper ranks loop types by retention or sets a universal session length | OPINION | none cited | 65 |

### 2.8 Core loop pass/fail checklist (12 items, P2:68-81)

Framing (OPINION, P2:69): it operationalises the research; it is not a validated predictor of success. A readiness failure from missing evidence differs from an observed design failure; store both the verdict and its reason. The paper gives no reason sentence for any of the 12 items (W07). All 12 items: tag OPINION, source IDs: none cited.

| # | item | pass when | reason (paper) | P2 |
| --- | --- | --- | --- | --- |
| 1 | Goal | the intended player can state or show a meaningful immediate objective without the evaluator supplying it | none given | 70 |
| 2 | Action | an available input changes relevant world or game state, and the player can link it to the objective | none given | 71 |
| 3 | Choice | choices support the intended strategy, expression, social experience or comfort. Do not call purely cosmetic variety strategic depth | none given | 72 |
| 4 | Feedback | under target conditions the player can see what happened, what caused it and what they can do next | none given | 73 |
| 5 | Consequence | success, failure or partial progress changes the player's situation in the intended way | none given | 74 |
| 6 | Repeat | the next round brings a changed problem, improving skill, social consequence or expressive chance that fits the fantasy | none given | 75 |
| 7 | Mastery | an advertised mastery goal says what can be learned and how improvement is seen; otherwise record why mastery is not central to the approved experience | none given | 76 |
| 8 | Variety | variation changes decisions or experience, not just labels and surface assets | none given | 77 |
| 9 | Promise | ordinary play delivers the title's and pitch's action; note the actual path and time seen, without inventing a target | none given | 78 |
| 10 | Exit and return | the player can stop safely, can tell what persists, and has an honest reason to return with no punitive coercion | none given | 79 |
| 11 | Target conditions | the loop was evaluated on its intended input, device and relevant solo or social setup | none given | 80 |
| 12 | Evidence | claims name the build, cohort, sample, observation and uncertainty. FAIL FOR READINESS when no relevant test exists | none given | 81 |

### 2.9 Section 1 rule table (P2:83-90)

| rule | number | evidence mark | source, date | P2 |
| --- | --- | --- | --- | --- |
| Separate ideation from implemented prototypes | more than 2,000 sticky notes | VERIFIED, reported count | D02, 2023-10-17 | 85 |
| Test multiplayer at its actual interaction scale | 4v4 prototype; 70 ideas | VERIFIED, reported count | D03, undated original interview | 86 |
| Kill-rate denominators need stage and period | 1 release; 9 killed; preceding 2 years | VERIFIED, reported count | D04, 2016-09-06 | 87 |
| Historical portfolio counts are not universal quotas | 5 hits; 30+ killed | VERIFIED | D05, 2023-02-15 | 88 |
| Distinguish platform activity from game sessions | FY2025 mobile 83% | VERIFIED | R01, filed 2026-02-11 | 89 |
| Use exact-day cohort return and dated comparisons | D1, D7, D30; no universal target | VERIFIED | R05-R06, accessed 2026-10-21 | 90 |

## 3. Section 2: design principles as observable tests (P2:92-123)

### 3.1 Worked examples the paper uses

| example | what it shows | tag | source | P2 |
| --- | --- | --- | --- | --- |
| Kirby and the Forgotten Land | Attack hit detection takes camera perspective into account; a near-ground jump is allowed under the "Fuzzy Landing" approach. Aim: an action that looks successful should feel successful in 3D. Paper's reading (OPINION): this supports testing perceptual fairness; it does not justify secretly changing every competitive collision rule. Separate execution leniency, accessibility options, enemy strength and outcome assistance | EXPERIENCE (paper's reading OPINION) | D06 | 94 |
| Kid Icarus: Uprising, Fiend's Cauldron | Player picks the challenge. Intensity runs from 0.0 to 9.0, with 2.0 as standard. The stake is in-game hearts, explicitly not real money. Failure lowers intensity and part of the stake is lost. Do not use this as a justification for paid gambling | EXPERIENCE (Sakurai's description); numbers VERIFIED | D07 | 96 |
| Tears of the Kingdom, affordance signs | Consistent signs: immovable crates get ropes or cloth; unbreakable jars get lids | EXPERIENCE | D09 | 98 |
| Tears of the Kingdom, building | Both elaborate and minimal constructions are valid ways to progress; visible glue and a consistent attach sound signal assembly | EXPERIENCE | D08 | 98 |

### 3.2 The ten observable tests (OPINION; "review tests, not claims that admired studios share one doctrine", P2:100)

All ten: tag OPINION, source IDs none cited.

| # | test | how to check | fail when | P2 |
| --- | --- | --- | --- | --- |
| 1 | Clarity | Can the player infer the available actions, the relevant state and the immediate consequences? | essential distinctions are carried only by decorative variation, or by text the player cannot read while acting | 101 |
| 2 | Meaningful choice | Show two concrete game states in which different available actions are better | one option beats all others in every supported situation, unless that option deliberately serves expression or accessibility instead of strategic balance | 102 |
| 3 | Fairness | Rebuild a loss from information available before it. Pass if the rule was learnable and counterplay or a knowingly accepted risk existed | the explanation only works in hindsight; hit geometry is ambiguous; unavoidable punishment is passed off as a skill test | 103 |
| 4 | Learnability and mastery | Novices find a workable action; experts improve planning, execution, efficiency, creativity or teamwork | progression only removes initial friction and creates no richer decisions | 104 |
| 5 | Feedback and feel | Tell apart: input received, action committed, hit or miss, state change, goal consequence. Sound, motion and effects must inform as well as celebrate | (no fail rule stated) a particle burst cannot repair unclear causality | 105 |
| 6 | Pacing | Draw the room for recovery, anticipation, escalation, payoff and reflection | continuous maximum intensity, or a forced wait with no purposeful tension, observation, planning, social activity or rest | 106 |
| 7 | Difficulty | Name the skill being tested; separate perceptual, cognitive, motor, strategic, social and economic demands. Raising all together makes diagnosis hard | the required skill was never taught, or gear poverty is mislabelled as lack of skill | 107 |
| 8 | Surprise and discovery | Surprise should revise a model, not teach that the rules cannot be trusted. Keep room for inference; do not demand a checklist that explains every possible discovery | (no fail rule stated) | 108 |
| 9 | Expression | Support meaningful differences in solutions, build, identity, arrangement or social role | expression is advertised but every non-standard approach is blocked, or equally cosmetic choices are presented as power differences | 109 |
| 10 | Time respect | Show the commitment, save progress appropriately, make stopping legible, and avoid repeating solved chores only to delay access. Quiet play is not wasted time by nature | (no fail rule stated) | 110 |

### 3.3 Real disagreements and their scope

| disagreement | what each side says | paper's guidance | tag | source | P2 |
| --- | --- | --- | --- | --- | --- |
| Mastery vs wider experience | Koster: fun is progress in prediction and mastery, and he separates systems design from broader experience design. Sylvester: decisions matter, and he also grants socialising, imagination and creation beyond decisions | Do not turn either into "every second must be a hard choice". A contemplative or social game may keep a different promise | OPINION, author theories | D25, D26 | 114 |
| One-shot arcs vs repeatable loops | Cook allows deliberate mixes | same | OPINION, author framework | D01 | 114 |
| Quests vs exploration | Klei removed explicit quests in Don't Starve because they weakened exploratory motivation | Neither case proves quests or metaprogression are universally good or bad. Test whether the structure serves this game's intended motivation; descriptive fit is stronger evidence than a claimed universal psychology | EXPERIENCE (Klei); OPINION (paper's reading) | D19 | 116 |
| Metaprogression for access | Supergiant describes Hades as using permanent progression, difficulty modifiers and narrative to widen access | same | EXPERIENCE (Supergiant); OPINION | D20 | 116 |

### 3.4 Section 2 rule table (P2:118-123)

| rule | number | evidence mark | source, date | P2 |
| --- | --- | --- | --- | --- |
| Separate perceived contact from strict 3D alignment | no universal tolerance given | EXPERIENCE | D06, 2022-03-24 | 120 |
| Let challenge match player intent | intensity 0.0-9.0; standard 2.0 | VERIFIED, documented design | D07, undated interview | 121 |
| Signal exceptions to interaction rules | no numeric benchmark | EXPERIENCE | D09, 2023-05-09 | 122 |
| Do not equate mastery with all valuable experience | no numeric benchmark | OPINION, author theories | D25, 2025-11-03; D26, 2005-01-01 | 123 |

## 4. Section 3: systems, progression, economies, balance, rewards (P2:125-177)

### 4.1 Resource model

| rule | tag | source | P2 |
| --- | --- | --- | --- |
| Dormans' 2011 paper models four roles: sources, drains, converters and traders, including abstract resources such as health and ammunition. Simulating a rule model before building is the method's purpose; it is not proof that players enjoy it | VERIFIED | D28 | 127 |
| Record for each resource (10 fields): unit, owner, storage or cap, creation event, destruction event, transfer, conversion, spend choice, variability of acquisition, exploit surface | OPINION | none cited | 129 |
| Reconcile stocks: closing balance = opening balance + created or incoming - destroyed or outgoing; count conversions per resource type | OPINION | none cited | 129 |
| A payment between players changes distribution. It is not a system-wide sink unless a fee is destroyed | OPINION | none cited | 129 |
| Do not confuse wealth accumulation, currency supply, item scarcity and a market-price index | OPINION | none cited | 129 |

### 4.2 Modelling and testing an economy (OPINION, P2:131)

| rule | P2 |
| --- | --- |
| Use a spreadsheet or executable model with named assumptions and reproducible scenarios | 131 |
| Scenarios to run (9 groups, my count of the paper's list): new vs experienced player; efficient vs inefficient strategy; solo vs group; short vs long sessions; complete trading vs no trading; lucky vs unlucky draws; inactive return; maximum-earning route; adversarial transfer loops | 131 |
| Judge distributions and bottlenecks, not one average income curve | 131 |
| Search for these six problems: positive feedback that makes an early lead irreversible; negative feedback that erases a deserved skill lead; conversion arbitrage; stale sinks; currency starvation; stockpiles that trivialise the next update | 131 |
| A simulated player is an implementation of one strategy, not the population | 131 |

All rows: tag OPINION, source IDs none cited.

### 4.3 Balance

| claim or rule | tag | source | P2 |
| --- | --- | --- | --- |
| Riot's 2019 League framework separates four play audiences and distinguishes finding an outlier from choosing the right change; it uses different measures where elite win-rate samples are too small. The four audiences are not named in the paper | EXPERIENCE (row table says VERIFIED) | D15 | 133, 173 |
| Mega Crit's GDC slides describe expert testers, metrics, streamers, feedback and Ascension skill stratification | EXPERIENCE | D16 | 133 |
| At that talk: 3 characters, 250-plus cards, 150-plus items, 50-plus combats, 50-plus events, 20 sequential Ascension levels. Historical content counts, not targets for another game | VERIFIED | D16 | 133 |
| Balance workflow (6 steps): state the viable strategies and intended asymmetries; collect outcome and selection data per condition; inspect actual decisions and failure points; identify the mechanism; change the narrowest causal lever; retest the affected and the adjacent populations | OPINION | none cited | 135 |
| Track effectiveness conditional on: familiarity, opponent, map, team composition, unlock state, input conditions | OPINION | none cited | 135 |
| A low pick rate can mean unfamiliarity, weak presentation, narrow use or low power | OPINION | none cited | 135 |
| An aggregate 50% win rate can hide a polarised set of matchups. Equal win rate is not identical experience | OPINION | none cited | 135 |

### 4.4 When an economy damages core play

| claim | tag | source | P2 |
| --- | --- | --- | --- |
| Blizzard's removal of the Diablo III auction house is explained as: easy trade pulled the game away from its intended reward loop. Developer judgment, not a measured effect | EXPERIENCE | D17 | 137, 12 |
| Blizzard's earlier itemization journal discusses making rare rewards truly useful and labels targeted drops and guarantees as ideas under discussion. Do not describe them as features that shipped | EXPERIENCE | D18 | 137 |

### 4.5 Progression, rewards, long-term goals

| rule | tag | source | P2 |
| --- | --- | --- | --- |
| Progression needs a purpose beyond bigger numbers. For each unlock, name one of 7: new verb, new tradeoff, expression option, world access, mastery test, social responsibility, or a convenience that is intentionally wanted | OPINION | none cited | 139 |
| Judge reward cadence by time to a meaningful next choice and by the tail of unrewarded attempts, not only by average payouts | OPINION | none cited | 139 |
| Separate predictable skill recognition from uncertain discovery | OPINION | none cited | 139 |
| Where chance exists, explain odds and failure protection accurately; have monetisation policy reviewed separately with current Roblox documentation | OPINION | none cited | 139 |
| Long-term goals without coercion: offer several understandable aspirations; allow goals to change; keep earned progress where appropriate; make comeback paths explicit; separate optional events from mandatory power | OPINION | none cited | 141 |
| Do not prescribe streak loss, escalating absence penalties, fake scarcity or exhaustion-driven engagement as craft improvements | OPINION | none cited | 141 |
| Success measures include player-valued accomplishment and voluntary return, not only time extracted | OPINION | none cited | 141 |
| Describe a reward schedule as a rule, answering 5 points: what action or elapsed condition makes it eligible; fixed or variable amount or timing; what the player knows; what happens after repeated failure; whether absence loses anything | OPINION | none cited | 143 |
| Record expected outcomes and the unfavourable tail when they can be calculated | OPINION | none cited | 143 |
| Do not claim variable rewards are universally more fun; do not use uncertainty to hide costs | OPINION | none cited | 143 |
| State the purpose of any price: optional expression, access, convenience or power; review free-play and competitive effects separately | OPINION | none cited | 143 |
| Intrinsic vs extrinsic: Klei found an explicit task list displaced discovery in its game (see 3.3) | EXPERIENCE | D19 | 13, 116 |

### 4.6 Roblox monetisation and younger players

Numbers and dates are in section 5.

| rule or fact | tag | source | P2 |
| --- | --- | --- | --- |
| Roblox distinguishes one-time passes, repeatable developer products and recurring monthly in-game subscriptions. Rules ban misleading or pressured purchases, false scarcity, and sale timers that are inaccurate or restart. Eligibility per player varies with location, age and platform. A monetisation format is not evidence of design quality | VERIFIED | R13 | 146 |
| Paid randomness includes indirectly bought currency, keys, luck modifiers and pity systems. Before purchase, disclose possible final outcomes and the actual numerical odds, including relevant player-specific changes. PolicyService governs access and paid-item trading separately; restricted players need a compliant fallback or blocked access. Total odds are 100% with a rounding exception. This is platform guidance, not legal clearance for any jurisdiction | VERIFIED | R14 | 148 |
| Advertising Standards (updated 2026-10-09) prohibit personalising ads to users under 18 and prohibit incentivising users under 13 to engage with ads. Rewarded video is 13+, opt-in, with a predetermined, non-random reward and no forced progress gate. The standards hold format-specific limits and show an under-13 tension with the newer integrations guidance. Do not squash this into a blanket permission or a universal "all ads are 13+" rule | VERIFIED | R15 | 150 |
| Ad integrations need registration, review, labelling and GetCampaignEligibilityAsync checks; the guidance addresses audiences aged 12 or younger. Immersive ad delivery can fall back for ineligible users; experience eligibility does not guarantee an ad is served | VERIFIED | R16, R17 | 152 |
| Before estimating revenue, specify: free play, purchased benefit, recurrence, odds, eligibility, fulfilment, fallback | OPINION | none cited | 154 |
| Never make essential progression depend on an ad being served | OPINION | none cited | 154 |
| If policy texts conflict for the intended format, settle it through the current official flow, not an invented reading | OPINION | none cited | 154 |
| Recheck policy before launch; the research is a dated snapshot | OPINION | none cited | 154 |

### 4.7 Systems review checklist with reasons (10 items, P2:157-168)

Framing (OPINION, P2:158): run every applicable item; a real "not applicable" needs a stated reason, not an empty cell. All 10 items: tag OPINION; source IDs none cited except where noted.

| # | item | pass when | reason (paper, paraphrased) | source | P2 |
| --- | --- | --- | --- | --- | --- |
| 1 | Progression | each unlock changes capability, strategy, expression or access, in a way that is stated | a bigger number alone does not make a new experience | none | 159 |
| 2 | Power | old and new players are compared in every competitive or cooperative interaction | progression can remove meaningful participation for one group | none | 160 |
| 3 | Economy | all sources, sinks, transfers, caps, losses, refunds and persistence are listed | balances cannot be understood from prices alone | none | 161 |
| 4 | Exploit | repeated, concurrent, interrupted and replayed transactions are tested | the intended economic rule has to survive edge cases in implementation | none | 162 |
| 5 | Reward | what behaviour earns the reward and what players know about it are stated | unclear or coercive schedules can contradict the intended experience | none | 163 |
| 6 | Paid randomness | current Roblox restrictions, disclosures and per-player eligibility handling are verified | a design preference cannot waive platform policy | R14 (implied by section 4.6; row itself cites none) | 164 |
| 7 | Balance | the population, context, competing goals and unwanted dominance are defined | an aggregate average can hide extreme outcomes in subgroups | none | 165 |
| 8 | Tuning | every value has units, a rationale, a revision and a test | constants nobody can explain cannot be reviewed or changed safely | none | 166 |
| 9 | Interactions | cross-system effects, feedback loops included, are simulated or tested | rewards that look fine locally can add up to a runaway global advantage | none | 167 |
| 10 | Cadence | new content is told apart from repeatable systemic variation, and the production dependency is stated | an update plan beyond the team's capacity is not a workable design | none | 168 |

### 4.8 Section 3 rule table (P2:170-177)

| rule | number | evidence mark | source, date | P2 |
| --- | --- | --- | --- | --- |
| Separate resource functions | 4 resource roles | VERIFIED, method definition | D28, 2011-10-09 | 172 |
| Segment balance judgments | 4 audiences in historical framework | VERIFIED | D15, 2019-05-30 | 173 |
| Combine evidence, not metrics alone | 20 Ascension levels in 2019 account | VERIFIED/EXPERIENCE | D16, GDC 2019 | 174 |
| An economy can sabotage core play | removal planned for 2014-03-18 | EXPERIENCE | D17, undated | 175 |
| Specify actual paid outcome odds and eligibility | 100% total with stated rounding exception | VERIFIED | R14, accessed 2026-10-21 | 176 |
| Apply current age and format advertising rules | under-18 personalisation prohibited | VERIFIED | R15, updated 2026-10-09 | 177 |

## 5. Roblox platform facts (every Roblox fact in P2:1-178)

All tagged VERIFIED by the paper. "Live docs" means the registry gives no publication date, only the access date 2026-10-21; these pages can change. Recheck before launch (P2:154).

| # | fact | number | date or period | source | P2 | paper's caveat |
| --- | --- | --- | --- | --- | --- | --- |
| RF01 | Platform mix of average DAUs, full year | mobile 83%, desktop 14%, console 3% | FY2025 (year ended 2025-12-31); Form 10-K filed 2026-02-11 | R01 | 49, 89 | Latest full-year split the paper found; not a 2026 measurement; not a session share |
| RF02 | Hours per DAU per day, platform-wide | 2.7 hours | period not stated in the sentence; sits in the R01 (FY2025) paragraph | R01 | 49 | Aggregate over platform and day; not a typical game session |
| RF03 | Average daily active users | 123 million | Q2 2026 (quarter ended 2026-06-30); letter dated 2026-07-30 | R02 | 50 | n/a |
| RF04 | Hours engaged in the quarter | 29 billion | Q2 2026 | R02 | 50 | n/a |
| RF05 | Share of global DAUs that had age-checked | 57% | final seven days of June 2026 | R02 | 50 | Snapshot of the last seven days of the quarter |
| RF06 | Age mix inside the age-checked subset | under 13: 35%; 13-17: 38%; 18+: 27% | final seven days of June 2026 | R02 | 50 | Not whole-platform age shares; not directly comparable with older self-reported ages |
| RF07 | Regional average DAUs (rounded to millions in the source) | US and Canada 22; Europe 26; Asia-Pacific 41; elsewhere 34 (millions) | Q2 2026 (the paper's sentence says "Q2"; data sheet dated 2026-07-30) | R03 | 52 | Account-activity counts, not a country-level market forecast |
| RF08 | Average session time is total time divided by session count; Roblox separately tracks how many new users remain at each minute of the first session | no number | live docs, accessed 2026-10-21 | R04 | 57 | n/a |
| RF09 | Roblox recommends reaching enjoyable play within the first five minutes | 5 minutes | live docs, accessed 2026-10-21 | R04 | 57 | Guidance, not a universal attention span, not a session-length target |
| RF10 | Retention reports use D1, D7, D30 exact-day returns by first-play cohort; Day 0 is first play; D7 is the eighth calendar day; immature cohorts show blanks | D1, D7, D30 | live docs, accessed 2026-10-21 | R05 | 59 | Blanks are not zero; acquisition changes shift the cohort mix; no published good thresholds |
| RF11 | Benchmarks for similar games update daily and show percentile bands | 50th to 90th percentile | live docs, accessed 2026-10-21 | R06 | 61 | Set of games can change; may fall back to genre or wider comparison |
| RF12 | Comparison games need a minimum audience | at least 100 DAU | live docs, accessed 2026-10-21 | R06 | 61 | n/a |
| RF13 | Example D1 band in the benchmark chart | 12.11% to 18.73% | live docs, accessed 2026-10-21 (no game, genre or date given) | R06 | 61 | Shows how to read a chart; not a current target (W09) |
| RF14 | Overall-success tiers compare against the top 1000 games by rolling 30-day playtime | top 1000; 30 days | live docs, accessed 2026-10-21 | R06 | 61 | A different comparison from the cohort benchmarks |
| RF15 | Current discovery uses a 28-day horizon with early and later signals; a new game need not wait 28 days for distribution. Registry excerpt for R07 says the Recommended For You algorithm was expanded from a previous 7-day view | 28 days; previous 7 days | R07 dated 2026-06-15; R08 and R09 live docs | R07, R08, R09 | 63 | Per-claim mapping to R07, R08 or R09 is not given (W10) |
| RF16 | Playtime ranking cap | 60 minutes per user per game per day | R07-R09 (per-source mapping not given) | R07, R08, R09 | 63 | A ranking cap, not a session limit |
| RF17 | Cohort benchmarks are not direct ranking inputs | no number | R07-R09 | R07, R08, R09 | 63 | R09 registry excerpt says benchmarks and benchmark games do not impact the recommendation algorithm (W10) |
| RF18 | Product types: one-time pass, repeatable developer product, recurring monthly in-game subscription | 3 types; monthly | live docs, accessed 2026-10-21 | R13 | 146 | Format is not evidence of design quality |
| RF19 | Roblox rules forbid misleading, confusing or pressured purchases, false scarcity, and inaccurate or restarting sale timers | no number | live docs, accessed 2026-10-21 | R13 | 146 | Eligibility per player varies with location, age, platform |
| RF20 | Paid random items: includes indirectly bought currency, keys, luck modifiers, pity systems; disclose possible final outcomes and actual numerical odds, with relevant player-specific changes, before purchase | no number | live docs, accessed 2026-10-21 | R14 | 148 | Platform guidance, not legal clearance for any jurisdiction |
| RF21 | Total odds of a paid random item | 100% with a rounding exception (the exception is not specified) | live docs, accessed 2026-10-21 | R14 | 148, 176 | W11 |
| RF22 | PolicyService governs access and paid-item trading separately; restricted players need a compliant fallback or blocked access | no number | live docs, accessed 2026-10-21 | R14 | 148, 164 | n/a |
| RF23 | Advertising Standards: ads may not be personalised for users under 18; engagement of users under 13 may not be incentivised | 18; 13 | last updated 2026-10-09 | R15 | 150, 177 | Format-specific limits; an under-13 tension with the newer integrations guidance (W12) |
| RF24 | Rewarded video: age 13+, opt-in, predetermined non-random reward, no forced progress gate | 13+ | last updated 2026-10-09 | R15 | 150 | Do not generalise to all ads |
| RF25 | Major integrations changes in the Advertising Standards took effect | 2026-05-04 | per registry only (not in P2:1-178 body) | R15 | registry | n/a |
| RF26 | Ad integrations need registration, review, labelling and GetCampaignEligibilityAsync checks; guidance addresses audiences aged 12 or younger | 12 or younger | live docs, accessed 2026-10-21 | R16 | 152 | Source assignment within R16-R17 inferred (W10) |
| RF27 | Immersive ads can fall back for ineligible users; eligibility does not guarantee ads are served | no number | live docs, accessed 2026-10-21 | R17 | 152 | n/a |

## 6. Source table (every ID cited in P2:1-178)

Titles are as in the registry; the .txt dropped punctuation, so titles are lightly restored. "Excerpt" shows the registry's key excerpt only when it is under 10 words; longer excerpts are left out. "Scope" is the paper's own scope note paraphrased; the registry gives no scope line for R-sources. Registry notes (P2:369): dates separate publication, revision and measurement; the registry supports facts and attributed practices, while templates and operating rules are OPINION.

| ID | title | author or org | date | URL | registry evidence | excerpt | scope note (paraphrased) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| D01 | Loops and Arcs | Daniel Cook | 2012-04-30 | https://lostgarden.com/2012/04/30/loops-and-arcs/comment-page-1/ | OPINION (author theory) | "What repeats and what does not?" | A concept framework, not controlled proof that all games need identical loops |
| D02 | Ask the Developer Vol. 11: Super Mario Bros. Wonder, Chapter 1 | Nintendo (Tezuka, Mouri, Hayashida, Sato, Kondo) | 2023-10-17 | https://www.nintendo.com/en-gb/News/2023/October/Ask-the-Developer-Vol-11-Super-Mario-Bros-Wonder-Chapter-1-2460393.html | EXPERIENCE; VERIFIED reported count | "There were just so many ideas." | Nintendo-hosted recollection; counts verified as reported, not audited |
| D03 | Iwata Asks: Splatoon, 2. Then Rabbits | Nintendo (Iwata and the Splatoon team) | undated | https://www.nintendo.com/en-za/Iwata-Asks/Iwata-Asks-Splatoon/Splatoon/2-Then-Rabbits/2-Then-Rabbits-1021367.html | EXPERIENCE; VERIFIED reported counts | (11+ words, omitted) | Seventy is an idea count, not a count of implemented prototypes. The original interview concerns the first Splatoon |
| D04 | Ilkka Paananen BAFTA Games Lecture | Ilkka Paananen | 2016-09-06 | https://www.bafta.org/media-centre/press-releases/ilkka-paananen-bafta-games-lecture/ | EXPERIENCE; VERIFIED scoped reported counts | "these are not just some early prototypes." | Not a denominator of all ideas or prototypes; does not imply a universal 90% prototype kill target; founder account, not an audited experiment |
| D05 | The Next Chapter of Supercell | Ilkka Paananen | 2023-02-15 | https://supercell.com/en/news/next-chapter/ | EXPERIENCE; VERIFIED historical reported counts | (11 words, omitted) | Historical self-report; not the current portfolio; not an all-ideas denominator |
| D06 | Ask the Developer Vol. 4: Kirby and the Forgotten Land | Nintendo and HAL Laboratory (Ninomiya, Kumazaki, Kamiyama, Endo) | 2022-03-24 | https://www.nintendo.com/au/news-and-articles/ask-the-developer-vol-4-kirby-and-the-forgotten-land/ | EXPERIENCE | "we make sure it does connect" | No universal tolerance or measured effect size. A single-player feel and accessibility case does not set competitive collision rules |
| D07 | Iwata Asks: Kid Icarus Uprising, 4. Having the Players Choose | Nintendo (Iwata, Masahiro Sakurai) | undated | https://www.nintendo.com/en-gb/Iwata-Asks/Iwata-Asks-Kid-Icarus-Uprising/Iwata-Asks-Kid-Icarus-Uprising/4-Having-the-Players-Choose/4-Having-the-Players-Choose-207744.html | EXPERIENCE; VERIFIED documented design numbers | "This is a clear example of risk and return." | The source separates hearts from real money. Not a basis for paid gambling |
| D08 | Ask the Developer Vol. 9: The Legend of Zelda: Tears of the Kingdom, Part 4 | Nintendo (TotK team) | 2023-05-09 | https://www.nintendo.com/us/whatsnew/ask-the-developer-vol-9-the-legend-of-zelda-tears-of-the-kingdom-part-4/ | EXPERIENCE | "people can enjoy the game in their own way." | Studio intentions and implementation account; not a measured comparison of player creativity |
| D09 | Ask the Developer Vol. 9: The Legend of Zelda: Tears of the Kingdom, Part 5 | Nintendo (TotK team) | 2023-05-09 | https://www.nintendo.com/us/whatsnew/ask-the-developer-vol-9-the-legend-of-zelda-tears-of-the-kingdom-part-5/ | EXPERIENCE | "we've placed a lid on every single unbreakable jar." | Evidence for specific affordance decisions; not independent testing of the whole game |
| D11 | The AI Systems of Left 4 Dead | Michael Booth, Valve | 2009 | https://cdn.fastly.steamstatic.com/apps/valve/2009/ai_systems_of_l4d_mike_booth.pdf | VERIFIED documented implementation; EXPERIENCE claimed design benefit | "Algorithm adjusts pacing, not difficulty" | Zero-indexed PDF pages cited. Parameters belong to this L4D build, not universal timing standards |
| D12 | Replayable Cooperative Game Design: Left 4 Dead | Michael Booth, Valve | 2009-03 | https://cdn.fastly.steamstatic.com/apps/valve/2009/GDC2009_ReplayableCooperativeGameDesign_Left4Dead.pdf | EXPERIENCE | "Ensure cooperation is the only winning strategy" | Case-specific argument for cooperative design; not proof that forced dependence suits all multiplayer games |
| D13 | Valve's Approach to Playtesting: The Application of Empiricism | Mike Ambinder, Valve | 2009-03 | https://cdn.akamai.steamstatic.com/apps/valve/2009/GDC2009_ValvesApproachToPlaytesting.pdf | EXPERIENCE | "Averages hide extreme examples" | Do not report simulated charts as measured results. No universal sample size or fun threshold |
| D15 | [Dev] Champion Balance Framework | RiotRepertoir, Riot Games | 2019-05-30 | https://www.leagueoflegends.com/en-us/news/dev/dev-champion-balance-framework/ | EXPERIENCE; VERIFIED documented historical framework | "For this, there's no definitive framework." | Historical framework; its thresholds are not current verified rules and cannot move to unrelated games |
| D16 | [Slay the Spire] Metrics Driven Design and Balance | Anthony Giovannetti, Mega Crit | 2019 | https://media.gdcvault.com/gdc2019/presentations/Giovannetti_Anthony_SlayTheSpire.pdf | EXPERIENCE; VERIFIED reported historical counts | "Data is evidence, but not a conclusion." | Content counts are historical. Feedback-message counts, if used, are not unique testers. Does not prove metrics alone caused success |
| D17 | Diablo III Auction House Update | John Hight, Blizzard | undated | https://news.blizzard.com/en-gb/article/10974978/diablo-iii-auction-house-update | EXPERIENCE; VERIFIED announced date | "it ultimately undermines Diablo's core game play" | Developer's causal judgment, not a measured controlled effect. Publication date not shown on the inspected page. Applies to this game's goal, not to all trading systems |
| D18 | Developer Journal: Itemization Update | Travis Day, Blizzard | undated | https://news.blizzard.com/en-gb/article/10056636/developer-journal-itemization-update | EXPERIENCE | "Farm Monsters, Not the Auction House" | Ideas under discussion are not shipped features or proven outcomes. Publication date not on the inspected page |
| D19 | Intrinsic vs. Extrinsic rewards | Jamie Cheng and Kevin Forbes, Klei Entertainment | 2012; updated 2025-05-21 | https://support.klei.com/hc/en-us/articles/360035456011-Intrinsic-vs-Extrinsic-rewards | EXPERIENCE | "made it feel like a list of chores." | A studio experience; not a universal reward-crowding effect; the essay's cited psychology studies were not verified |
| D20 | Hades FAQ | Supergiant Games | 2018-12-07; updated 2025-07-16 | https://www.supergiantgames.com/blog/hades-faq/ | EXPERIENCE | "a real sense of place and story to it" | Describes design intent and features; not controlled retention effects or a cadence benchmark |
| D22 | [Dev] Making Matchmaking Better | RiotSapMagic and GET IN GAME, Riot Games | 2018-03-14 | https://www.leagueoflegends.com/en-gb/news/dev/dev-making-matchmaking-better/ | EXPERIENCE | "create fair matches" | Historical League retrospective; not a universal queue-time target or evidence for forced win/loss patterns |
| D23 | Player Dynamics Design: Looking Behind the Curtain | Weszt "Vonburgermeister" Hart, Riot Games | 2022-05-12 | https://www.riotgames.com/en/news/player-dynamics-design-looking-behind-the-curtain | EXPERIENCE | "to change behavior, change the environment." | A practitioner framework; no general measured reduction in toxicity |
| D25 | Game design is simple, actually | Raph Koster | 2025-11-03 | https://www.raphkoster.com/2025/11/03/game-design-is-simple-actually/ | OPINION (author theory) | "fun is basically about making progress on prediction." | Public essay; not a quote from an unseen book nor a universal controlled psychology result |
| D26 | Decision-Based Gameplay Design | Tynan Sylvester | 2005-01-01 | https://tynansylvester.com/2005/01/4/ | OPINION (author theory) | (11 words, omitted) | Public essay; not quoted from the book; not a claim that every moment needs a hard decision |
| D28 | Simulating Mechanics to Study Emergence in Games | Joris Dormans | 2011-10-09 | https://ojs.aaai.org/index.php/AIIDE/article/view/12477 | VERIFIED method description | "Sources create resources, drains destroy resources." | A formal design-model method; not a validated proxy for human enjoyment. Full text read at the author's university repository |
| D29 | The Best Games Haven't Been Made Yet | Ilkka Paananen | 2026-02-10; updated 2026-02-12 | https://supercell.com/en/news/the-best-games-havent-been-made-yet/ | EXPERIENCE; VERIFIED reported test counts and metrics | "Don't skip testing meta and long term retention." | Self-reported; not a transferable Roblox benchmark; not a controlled causal result |
| R01 | Roblox 2025 Form 10-K, "Our Users", printed p. 9 | Roblox | filed 2026-02-11; measurement year 2025 | https://d18rn0p25nwr6d.cloudfront.net/CIK-0001315098/10a8d222-cffe-4762-8037-14f34855646f.pdf | VERIFIED | (10 words, omitted) | no scope line in registry |
| R02 | Q2 2026 Shareholder Letter, age-check reporting and special note | Roblox | 2026-07-30; quarter ended 2026-06-30; age snapshot = last seven days of quarter | https://www.sec.gov/Archives/edgar/data/1315098/000162828026051059/ex991-robloxq22026earnin.htm | VERIFIED | "not directly comparable to historical self-reported data" | no scope line in registry |
| R03 | Q2 2026 Investor Relations Data Sheet, p. 3 | Roblox | 2026-07-30; measurement Q2 2026 | https://s27.q4cdn.com/984876518/files/doc_financials/2026/q2/Roblox-Q2-2026-Investor-Relations-Data-Sheet.pdf | VERIFIED | (10 words, omitted) | no scope line in registry |
| R04 | Engagement | Roblox | undated live docs; accessed 2026-10-21 | https://create.roblox.com/docs/production/analytics/engagement | VERIFIED | "divided by the number of sessions" | no scope line in registry |
| R05 | Retention | Roblox | undated live docs; accessed 2026-10-21 | https://create.roblox.com/docs/production/analytics/retention | VERIFIED | (12 words, omitted) | no scope line in registry |
| R06 | Analytics dashboard: benchmarks and breakdowns | Roblox | undated live docs; accessed 2026-10-21 | https://create.roblox.com/docs/production/analytics/analytics-dashboard | VERIFIED | "Benchmarks for similar games update daily" | no scope line in registry |
| R07 | Optimizing Discovery: How Great Games Reach Millions of Players on Roblox | Roblox | 2026-06-15 | https://about.roblox.com/newsroom/2026/06/optimizing-discovery-great-games-reach-millions-players-roblox | VERIFIED | (13 words, omitted; says the Recommended For You algorithm grew from a previous 7-day view) | no scope line in registry |
| R08 | Discovery: current ranking signals and content quality restrictions | Roblox | undated live docs; accessed 2026-10-21 | https://create.roblox.com/docs/discovery | VERIFIED | (12 words, omitted; says each signal is based on users who joined organically from Recommended) | no scope line in registry |
| R09 | Discovery FAQ | Roblox | undated live docs; accessed 2026-10-21 | https://create.roblox.com/docs/discovery-faq | VERIFIED | (10 words, omitted; says benchmarks and benchmark games do not impact the recommendation algorithm) | no scope line in registry |
| R13 | Monetization: product types and presentation rules | Roblox | undated live docs; accessed 2026-10-21 | https://create.roblox.com/docs/production/monetization | VERIFIED | (omitted; users must never be misled, confused or pressured into purchases) | no scope line in registry |
| R14 | Paid random items policy guidelines | Roblox | undated live docs; accessed 2026-10-21 | https://create.roblox.com/docs/production/monetization/paid-random-items | VERIFIED | "all possible outcomes and the actual numerical odds" | no scope line in registry |
| R15 | Advertising Standards | Roblox | last updated 2026-10-09; major integrations changes effective 2026-05-04 | https://en.help.roblox.com/hc/en-us/articles/13722260778260-Advertising-Standards | VERIFIED | (omitted; says ads may not be personalised for users under 18) | no scope line in registry |
| R16 | Ad integrations: campaign eligibility and young audiences | Roblox | undated live docs; accessed 2026-10-21 | https://create.roblox.com/docs/production/promotion/ad-integrations | VERIFIED | (omitted; concerns campaign audiences of players aged 12 or under) | no scope line in registry |
| R17 | Immersive ads: user-specific delivery | Roblox | undated live docs; accessed 2026-10-21 | https://create.roblox.com/docs/production/monetization/immersive-ads | VERIFIED | (omitted; eligibility does not guarantee ads are served) | no scope line in registry |
| U01 | User supplied research brief | Studio owner | provided 2026-10-21 | the two research prompts supplied by the owner | OPINION (studio operating instruction) | "The agent proposes and documents; the owner decides." | The two prompts set the requested scope, the final three pitches and the owner's decision rights |

Registry entries that exist but are not cited in P2:1-178 (left out of this file): D10, D14, D21, D24, D27, R12, R32. Registry has no R10 or R11.

## 7. Claims to fact-check (every number and Roblox fact in P2:1-178)

Fact-checking is a separate ticket; nothing here has been checked against the web. Count: 44 rows.

| # | claim | P2 line | source |
| --- | --- | --- | --- |
| 1 | Wonder: more than 2,000 sticky notes | 4, 37, 85 | D02 |
| 2 | Wonder count date 2023-10-17 | 85 | D02 |
| 3 | Splatoon: 70 ideas | 35, 86 | D03 |
| 4 | Splatoon: 4 vs 4 already played in the selected prototype | 35, 86 | D03 |
| 5 | Supercell: 1 release, 9 killed, preceding 2 years | 5, 37, 87 | D04 |
| 6 | Supercell lecture dated September 2016 (2016-09-06) | 37, 87 | D04 |
| 7 | Supercell: 5 hit launches, 30-plus kills (February 2023, 2023-02-15) | 37, 88 | D05 |
| 8 | Roblox FY2025 device split: mobile 83%, desktop 14%, console 3% of average DAUs | 49, 89 | R01 |
| 9 | Roblox: 2.7 hours per DAU per day | 49 | R01 |
| 10 | Form 10-K filed 2026-02-11 | 89 | R01 |
| 11 | Q2 2026: 123 million average DAUs | 50 | R02 |
| 12 | Q2 2026: 29 billion quarterly hours | 50 | R02 |
| 13 | Last seven days of June: 57% of global DAUs age-checked | 50 | R02 |
| 14 | Age-checked subset: 35% under 13, 38% 13-17, 27% 18+ | 50 | R02 |
| 15 | Q2 regional average DAUs: US and Canada 22, Europe 26, Asia-Pacific 41, elsewhere 34 (millions) | 52 | R03 |
| 16 | Average session time = total time / session count; tracks new users per minute of first session | 57 | R04 |
| 17 | Recommendation to reach enjoyable play within first five minutes | 57 | R04 |
| 18 | D1, D7, D30 exact-day cohort returns; Day 0 = first play; D7 = eighth calendar day; no published thresholds | 59, 90 | R05 |
| 19 | Benchmarks update daily; 50th to 90th percentile bands | 61 | R06 |
| 20 | Comparison games have at least 100 DAU; fall back to genre or wider sets | 61 | R06 |
| 21 | Example D1 range 12.11% to 18.73% | 61 | R06 |
| 22 | Overall-success tiers use top-1000 rolling-30-day playtime | 61 | R06 |
| 23 | Discovery uses a 28-day horizon with early and later signals | 63 | R07-R09 |
| 24 | Playtime ranking cap of 60 minutes per user per game per day | 63 | R07-R09 |
| 25 | Cohort benchmarks are not direct ranking inputs | 63 | R07-R09 |
| 26 | Kirby: camera perspective in attack hit detection; "Fuzzy Landing" near-ground jump (2022-03-24) | 94, 120 | D06 |
| 27 | Kid Icarus: intensity 0.0 to 9.0, standard 2.0; stake in hearts, not money | 96, 121 | D07 |
| 28 | TotK: ropes or cloth on immovable crates, lids on unbreakable jars (2023-05-09) | 98, 122 | D09 |
| 29 | TotK: elaborate and minimal builds valid; visible glue and a consistent attach sound | 98 | D08 |
| 30 | Koster essay (2025-11-03) and Sylvester essay (2005-01-01) positions | 114, 123 | D25, D26 |
| 31 | Klei removed explicit quests in Don't Starve | 116 | D19 |
| 32 | Hades uses permanent progression, difficulty modifiers and narrative to broaden access | 116 | D20 |
| 33 | Dormans 2011: sources, drains, converters, traders (2011-10-09) | 127, 172 | D28 |
| 34 | Riot 2019 League framework: four play audiences; different measures for small elite samples (2019-05-30) | 133, 173 | D15 |
| 35 | Mega Crit counts: 3 characters, 250+ cards, 150+ items, 50+ combats, 50+ events, 20 sequential Ascension levels | 133, 174 | D16 |
| 36 | Blizzard removed the Diablo III auction house; "removal planned for 2014-03-18" | 137, 175 | D17 |
| 37 | Itemization journal frames targeted drops and guarantees as ideas under discussion | 137 | D18 |
| 38 | Roblox product types: pass, developer product, recurring monthly subscription | 146 | R13 |
| 39 | Roblox bans misleading or pressured purchases, false scarcity, inaccurate or restarting timers | 146 | R13 |
| 40 | Paid random items: disclosure of outcomes and actual odds; includes currency, keys, luck modifiers, pity systems | 148 | R14 |
| 41 | Total odds 100% with a rounding exception; PolicyService handles access and paid-item trading | 148, 176 | R14 |
| 42 | Advertising Standards updated 2026-10-09: no personalising for under 18; no incentivising under 13; rewarded video 13+, opt-in, predetermined non-random reward, no forced progress gate | 150, 177 | R15 |
| 43 | Ad integrations: registration, review, labelling, GetCampaignEligibilityAsync; guidance for audiences aged 12 or younger | 152 | R16 |
| 44 | Immersive ads: fallback for ineligible users; eligibility does not guarantee fill | 152 | R17 |

## 8. Contradictions and weak spots

Nothing here is fixed; it is for the lead and the fact-check ticket.

| id | problem | P2 lines |
| --- | --- | --- |
| W01 | The word "VERIFIED" covers studio self-reports checked only "as reported" (D02, D04, D05, D16). A skill that says "verified count" would over-claim; the numbers are developer statements | 4, 5, 20, 85-88, 133 |
| W02 | Tags change inside one claim. L35: EXPERIENCE tag covers both the Splatoon event and the paper's lesson (lesson is the paper's reading). L96: EXPERIENCE sentence then VERIFIED numbers. D15 is tagged EXPERIENCE in the body (L133) but VERIFIED in the rule table (L173). D05 and D04 are labelled "EXPERIENCE; VERIFIED" in the registry but only VERIFIED in the tables. L174 uses "VERIFIED/EXPERIENCE" | 35, 96, 133, 173, 174 |
| W03 | Summary rules 8, 13, 14 and 15 cite D11, D12, D22, D23, D13, D29 and U01, but nothing in P2:22-177 discusses those sources. Rule 8's "frequency vs amplitude" wording is not in the D11 excerpt ("adjusts pacing, not difficulty"). The registry says D11 parameters are specific to L4D. U01 is the owner's own brief, so rule 15 is sourced to the instruction it carries out | 9, 14, 15, 16 |
| W04 | Rule 6 says Nintendo examples allow "new uses of familiar actions". The body shows Kirby feel-leniency and TotK affordance signs. The wording is the paper's inference. The TotK crate/rope/cloth and attach-sound details are not in the D08 and D09 excerpts and need the full text | 7, 94, 98 |
| W05 | Rule 5 (prototype the riskiest uncertainty first) cites D02-D05, which are idea and kill counts. They do not test the rule | 6, 37 |
| W06 | Only the moment scale has an explicit question (what information changes the next decision). Session and long term get instructions, not questions. The three scales and the coupling chain have no source ID; D01 supports only loops vs arcs | 29-33 |
| W07 | The core loop checklist gives no reason for any item and defines PASS only (the one FAIL is "FAIL FOR READINESS" for Evidence). Several systems checklist PASS conditions are tasks to do ("compare", "enumerate", "test"), not observable states. Neither checklist has a scoring rule | 70-81, 159-168 |
| W08 | The ten observable tests have no source IDs. Feedback and feel, Surprise and discovery, and Time respect state no fail condition | 101-110 |
| W09 | R06 example D1 band 12.11%-18.73% has no game, genre or date. The paper says it is a chart-reading example, so it must never become a target | 61 |
| W10 | R07-R09 are cited as a range for the 28-day horizon, the 60-minute cap and the benchmark claim, with no per-claim ID. The paper's "not direct ranking inputs" is softer than the R09 excerpt (benchmarks "do not impact" the algorithm). R16-R17 are also cited as a pair; the split in section 5 is inferred from registry titles and excerpts. R01's 2.7 hours has no stated period | 49, 63, 152 |
| W11 | "100% total with a rounding exception": the rounding rule (decimals, tolerance) is not given | 148, 176 |
| W12 | The paper itself says R15 has an under-13 tension with newer integrations guidance (R16) and leaves it open. Registry shows integrations changes effective 2026-05-04. The skill must not settle it | 150, 154 |
| W13 | Row L175 "removal planned for 2014-03-18": the date is not in the body text (L137), and the registry says D17 is undated and the publication date is not shown on the inspected page. The origin of the date is not explained | 137, 175 |
| W14 | D26 date 2005-01-01 looks like a placeholder day (URL path reads 2005/01/4) | 123 |
| W15 | The four audiences in Riot's framework are never named; D16 is named only as "Mega Crit" in the body (the game, Slay the Spire, is in the registry title only); Klei's game (Don't Starve) is named in the body but not in the registry title. D20's "broaden access" claim is not in the excerpt (the excerpt is about place and story) | 116, 133 |
| W16 | Mixed tag in rule table L86-87: the "rule" wording (test at actual interaction scale; denominators need stage and period) is the paper's inference placed in a VERIFIED row; the VERIFIED part is only the count | 86, 87 |
| W17 | Kid Icarus: "Failure lowers intensity and the stake is lost in part" is ambiguous about whether the stake is partly lost or partly returned | 96 |
| W18 | Hours-per-DAU (2.7, FY2025 per R01) and quarterly hours (29 billion, Q2 2026 per R02) are different periods and not comparable; the paper warns about aggregate use but the line does not state 2.7's period. L52 gives regional figures for "Q2" without the year | 49, 50, 52 |
| W19 | The paper's research date (21 October 2026) and all registry access dates are one day after the date on this kit file (2026-10-20). The same applies to the UI notes (05a) | 18, 369 |
| W20 | Roblox live-doc sources (R04, R05, R06, R08, R09, R13, R14, R16, R17) have only an access date, so none of the policy or analytics numbers has a publication date. The paper tells the reader to recheck before launch | 154 |
