---
type: reference
scope: universal
status: active
updated: 2026-10-20
source: J003
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-20

Source: Game_Designer_Part_1_Research.txt, lines 329-534 (sections 3 to 7) plus the registry entries at lines 535-982 for every ID cited here; paraphrased; the paper stays outside git.

# Game designer research part 1, sections 3-7: preproduction, working with leads, documents, working with the owner, process for an AI designer

## 0. Conventions used in this file

| item | meaning |
| --- | --- |
| RP:n | line n of the paper |
| tags | VERIFIED = published measurement, official platform fact or inspected artifact content, with its original scope. EXPERIENCE = a studio or designer reporting its own practice or results. OPINION = interpretation, recommendation or proposed template. VERIFIED never means causal proof, replication or universal fit (RP:22). |
| IDs | Source IDs resolve in section 9. "Author synthesis 2026-10-21" and "User brief 2026-10-21" appear in the paper's rule tables with no registry ID (see section 8, W15). The registry has one user entry, U01. |
| scope of the paper | Audience is the AI game designer in an owner-led Roblox studio (RP:18). All templates and proposed operating rules are OPINION, even when built on VERIFIED sources (RP:537). |
| numbers | N0 to N6 and F3 in section 11 are placeholders, never results. Sourced numbers appear only with their scope. |
| tag mismatches | Where the paper's inline tag differs from the registry tag for the same ID, both are shown (see section 8, W02-W04). |

## 1. Section 3: Preproduction (RP:329-383)

### 1.1 Purpose, stages, order of growth

| # | rule or statement (paraphrased) | tag | IDs | RP |
| --- | --- | --- | --- | --- |
| 3.1 | Riot's prototype exit criteria: an identified audience, playable risky innovations, shared understanding, and audience playtest evidence. Riot's engineering account separates "whether to build" from "how to build". Disposable code can be right for learning; it does not prove production architecture. | EXPERIENCE | P02, P03 | RP:330 |
| 3.2 | Use stage purposes, not a mandatory waterfall. Concept work clarifies the experience and the uncertainty. A pitch asks for a decision. Prototypes challenge risky assumptions. Preproduction joins the experience to the production method. A representative slice tests whether the needed quality can be made through a repeatable pipeline. Stage names vary. A negative result can send work backward without voiding the whole fantasy. | OPINION | none | RP:332 |
| 3.3 | Grow the concept in dependency order: (1) approve fantasy, intended audience, pillars and exclusions; (2) explore world and characters as ways to make role and action legible; (3) define the core choice and consequence; (4) identify the systems and content needed to repeat it. Fix only the decisions the next experiment or implementation needs; leave untested detail open. A missing choice gets an owner and the next evidence, not an invented answer. | OPINION | none | RP:334 |
| 3.4 | Rami Ismail calls a vertical slice a production prototype. Double Fine's Psychonauts 2 documentary shows pilot areas used to make quality concrete across exploration, puzzles, art and narrative. These are situated accounts, not a required number of pilots or a universal sequence. | EXPERIENCE (inline; P15 is OPINION in the registry) | P15, P13 | RP:336 |

### 1.2 Art exploration and functional pillars

| # | rule or statement (paraphrased) | tag | IDs | RP |
| --- | --- | --- | --- | --- |
| 3.5 | Riot puts artists inside prototype problem-solving and lets visual exploration run in parallel. Blizzard's Venture account: a paper drill concept changed after it failed to read in first-person 3D. Cheap art and early art direction are compatible. | EXPERIENCE | P04, P12 | RP:339 |
| 3.6 | Make concept art answer questions on six topics: silhouette and role; scale; readability in the playable camera; important materials; character relationships; the signature moment. Mood boards give references and anti-references; they do not show production cost or in-game clarity. Put a visual target next to an interactive test when appeal depends on tone, character or spectacle. | OPINION | none | RP:341 |
| 3.7 | Valve's Half-Life 2 process separated initial constraints from mechanics that stay proposals, and asked whether the intended experience happened and whether it was desirable. In Into the Breach, readable, deterministic combat decisions spread into UI, enemy and weapon constraints. | EXPERIENCE (inline; P06 and P16 are VERIFIED artifact content in the registry) | P06, P16 | RP:343 |
| 3.8 | A useful pillar states what the player should experience, which decisions it favours and which tempting feature it rejects. When pillars conflict, the owner picks a priority or authorizes a test. A slogan must not silently overrule an explicit creative decision. | OPINION | none | RP:345 |

### 1.3 T1 Pillars sheet template (RP:347-357), OPINION, 9 fields

Framing: a pillar is a constraint on decisions, not an adjective. Do not claim any particular number of pillars is optimal (RP:348).

| field | what it holds |
| --- | --- |
| Vision and owner | the approved fantasy and the person who decides |
| Pillar name | a plain statement of behavioural intention |
| Player evidence | what players should be able to do, perceive or choose if the pillar works |
| Required implications | systems, art, controls and social structures that must support it |
| Tradeoff | what the team will give up rather than weaken this pillar |
| Rejected example | a tempting feature that contradicts the pillar, and why |
| Conflict rule | how this pillar interacts with another pillar; who decides an unresolved conflict |
| Test | prototype condition, observation, failure signal and the next decision |
| Status | approved, proposed or retired; date; owner decision; links to affected specifications |

### 1.4 Published artifacts and their limits (RP:359-366)

| artifact | what the paper says | limit the paper states | tag | IDs | RP |
| --- | --- | --- | --- | --- | --- |
| Condor Diablo pitch (1994, published by David Brevik in 2016) | 8 pages; holds player activity, production assumptions and a schedule; expects revision; proposed turn-based play | evidence of a proposal only; not evidence that its estimates or every mechanic shipped | VERIFIED | P08 | RP:360 |
| FTL (GDC 2013) | began from the experience of captaining a starship while letting gameplay structures change | a counterexample to the idea that a fixed mechanics pitch is the only valid start | EXPERIENCE | P09 | RP:362 |
| My Work Is Not Yet Done pitch | public pitch includes identity, imagery, gameplay pillars, comparables, audience signals, remaining work and an ask | a successful pitch is not a validated cost estimate | VERIFIED | P17 | RP:364 |
| same pitch, author's later account | author later said the initial budget was too low and changed after publisher advice | same as above | EXPERIENCE | P18 | RP:364 |
| study guidance | study these artifacts for how they make decisions possible, not as templates to copy; a funding pitch needs information an internal concept review may not; Raw Fury's guidance is recipient-specific; the Valve and Into the Breach decks are process talks, not full internal design documents | - | OPINION | P14, P06, P16 | RP:366 |

### 1.5 T2 Preproduction plan and lead review template (RP:368-377), OPINION

Planning rule: schedule by unresolved risk, not by a claimed industry-standard week count. A stage may loop back when evidence breaks its premise. Give each review a question, an artifact, a decision owner and exit evidence (RP:369). The table has 7 review rows and 4 columns; it has no column for decision owner or exit evidence (see section 8, W01).

| review | inputs and responsible leads | decision to make | required output | RP |
| --- | --- | --- | --- | --- |
| Concept review | designer and trend scout; fantasy, evidence and alternatives | owner selects the experiment or rejects the concept | decision record and an explicit uncertainty list | RP:371 |
| Promise review | designer, marketing and art director; title, first image and signature moment | does the playable promise match what is advertised | approved promise; failed claims removed | RP:372 |
| Feasibility review | designer and architect; target hardware, player configuration, persistence and risky interactions | which technical or production risk could invalidate the fantasy | bounded risk prototypes and measured results | RP:373 |
| Style and readability review | art director, UI, VFX, animation, sound and level lead; cheap visual targets and a playable scene | can every craft communicate the same state and priority | shared state vocabulary and craft constraints | RP:374 |
| Core loop review | designer, level lead, architect and relevant crafts; grey box plus observations | is the intended choice and consequence present | revised loop, observations and next test | RP:375 |
| Production readiness review | all leads; representative slice, content workflow, dependencies and estimates | is there enough evidence to authorize the next scope | owner decision, remaining risks and explicit exclusions | RP:376 |
| Change review | affected leads; proposed change and impact map | does the benefit justify rework or a changed promise | versioned decision and synchronized briefs | RP:377 |

### 1.6 Section 3 rule table (4 rows, RP:379-383)

| rule | number | tag | source and date | RP |
| --- | --- | --- | --- | --- |
| Match prototype fidelity to the question | no standard stage duration found | OPINION | P02-P04, 2020-2021 | RP:380 |
| Exercise production as well as presentation | no universal slice size | OPINION | P15, 2022 | RP:381 |
| Treat old pitches as provisional artifacts | 8-page Diablo pitch | VERIFIED | P08, 1994 (published 2016) | RP:382 |
| Use pillars to record real tradeoffs | no optimal pillar count established | OPINION | P06 2006-2007 and P16 2019 | RP:383 |

## 2. Section 4: Working with the other leads (RP:385-404)

The paper's roles are proposed responsibilities for this studio, not a claim about how every source studio is organized (RP:386, OPINION). Start collaboration while the concept can still change (RP:386).

### 2.1 Each lead: what it owns, what it needs, when

The "reviews joined" column is read straight from the T2 table (section 1.5); the other columns are from RP:386-394.

| lead | owns (RP:386) | what the designer agrees or supplies with it | reviews joined (T2) | tag | RP |
| --- | --- | --- | --- | --- | --- |
| Designer (the AI) | the causal game model and its link to the fantasy | records the exact decision, owner, affected artifacts, open questions and next evidence after each early review (2.3) | Concept, Promise, Feasibility, Core loop, Production readiness, Change | OPINION | RP:386, 398 |
| Art director | visual direction | agree: what must read first; which silhouettes carry role information; what colour means; how scale supports the fantasy; which references are deliberately excluded. Review in the intended camera and device context. Art discovery may suggest a better mechanic if it strengthens the promise; design-to-art handoff is not one-way. | Promise, Style and readability, Production readiness | OPINION | RP:388 |
| Architect | technical strategy and measured constraints | name the risky claim exactly (simultaneous actor behaviour, destruction, persistence, shared ownership, streaming, recovery or another dependency). Ask under what conditions it works, how it fails, and which cheaper alternative keeps the experience. Technical prototypes need target conditions and measured results. An offline mockup does not settle network feasibility; a successful load test does not settle enjoyment. | Feasibility, Core loop, Production readiness | OPINION | RP:390 |
| Marketing | communication tests inside the approved promise | keep a promise ledger linking every title, image and trailer claim to a playable feature or to an explicitly unbuilt concept. Marketing evidence may change audience assumptions; it does not authorize inventing mechanics the team cannot deliver. | Promise, Production readiness | OPINION | RP:392 |
| Trend scout | (named in the intake step and in the reviews; the paper gives no ownership sentence) | separates persistent behaviour from temporary attention; identifies comparables | Concept, Production readiness | OPINION | RP:392, 371 |
| UI, VFX, sound, animation, levels (craft leads) | expressive and production choices within shared contracts | set a common event and state vocabulary. Agree which signals mean anticipation, commitment, success, failure, danger and recovery (6 signals). Review one representative interaction together, not each craft alone; contradictory cues can make individually polished work incoherent. | Style and readability (all five); Core loop (level lead and relevant crafts); Production readiness | OPINION | RP:394, 374-376 |
| All leads, general | - | involve crafts before assumptions become expensive; no universal meeting cadence | Change (affected leads) | OPINION | RP:401, 377 |

### 2.2 Source-studio practice the paper cites

| statement | tag | IDs | limit | RP |
| --- | --- | --- | --- | --- |
| Riot treats subject-matter expertise as a decision role while disciplines still take part in design conversations. Valve describes local team autonomy inside shared constraints, with mechanisms for global coherence. Neither means every contributor has an unbounded veto. | EXPERIENCE | P03, P06 | not a team-structure rule | RP:396 |

### 2.3 Early review close-out and decision rights (RP:398), OPINION, 5 recorded items

Each early review ends with: (1) the exact decision; (2) its owner; (3) affected artifacts; (4) unresolved questions; (5) the evidence needed next.

| role | rule |
| --- | --- |
| owner | settles creative direction and resource tradeoffs |
| leads | surface specialist risks and alternatives |
| the AI | records agreement; never fabricates a lead's approval; never treats silence as consent |

### 2.4 Section 4 rule table (4 rows, RP:400-404)

| rule | number | tag | source and date | RP |
| --- | --- | --- | --- | --- |
| Involve crafts before assumptions become expensive | no universal meeting cadence | OPINION | P03-P04, 2021 | RP:401 |
| Test presentation in the gameplay perspective | no universal mockup count | EXPERIENCE | P12, 2024 | RP:402 |
| Keep local decisions within shared constraints | no universal team structure | EXPERIENCE | P06, 2006-2007 | RP:403 |
| Record owner decisions and unresolved specialist risks | per consequential review | OPINION | Author synthesis 2026-10-21 | RP:404 |

## 3. Section 5: Turning a decided game into documents (RP:406-460)

### 3.1 Document architecture and states

| # | rule or statement (paraphrased) | tag | IDs | RP |
| --- | --- | --- | --- | --- |
| 5.1 | Use a short vision-and-pillars record linked to living feature, system, content and craft specifications. This is a recommended architecture, not evidence that successful studios dropped large design documents. Long documents keep context but fail when readers cannot find the current rule or when duplicated values drift. A one-page design works only if the omitted detail is unneeded or linked elsewhere. | OPINION | none | RP:407 |
| 5.2 | Keep explicit states for proposals, approved decisions, implemented behaviour and superseded versions (4 states). Each requirement names its source, owner, affected build and open questions. Keep a behavioural acceptance test separate from an experiential test: the build can meet every written rule while players stay confused or uninterested. | OPINION | none | RP:409 |
| 5.3 | Sakurai's official description stresses changing parameters during balance work as more people take part. It supports making tuning accessible; it supplies no universal data schema and no default cooldown. | EXPERIENCE (inline; P19 is OPINION in the registry) | P19 | RP:411 |
| 5.4 | Make exact whatever another craft cannot safely reinterpret: rules, conditions, permissions, states, timing relationships, units, resource changes, persistence, failure recovery. Leave art treatment, animation expression, sound character and engineering architecture with the accountable craft leads, inside agreed clarity and performance limits. If a value is unknown, write TBD, the deciding person and a test. Do not invent precision to make a brief look complete. | OPINION | none | RP:413 |

### 3.2 T3 Feature specification template (RP:415-431), OPINION, 15 fields

Framing: an implementation contract for decided behaviour; it must also name the choices that stay with a craft lead (RP:416).

| # | field | what it holds |
| --- | --- | --- |
| 1 | Feature ID, version and status | stable ID; status one of proposed, approved, implemented, retired |
| 2 | Purpose | the player problem; the pillar; the promised action; why the feature is needed |
| 3 | Scope and exclusions | what is included, omitted, and deliberately postponed |
| 4 | Actors and permissions | who may start, observe, interrupt, complete or reverse it |
| 5 | Prerequisites and inputs | player and world state, input actions, resources, ownership and network assumptions |
| 6 | State model | every state, entry condition, transition, timeout, interruption and terminal state |
| 7 | Rules and invariants | what must always hold, including multiplayer authority and persistent data |
| 8 | Tuning references | parameter IDs, units, allowed domain, current value, provenance, owner; unresolved values stay TBD |
| 9 | Outputs and feedback | world change, UI, animation, VFX, sound and analytics events, each linked to a state or event |
| 10 | Failure handling | disconnect, duplicate request, unavailable data, invalid target, cancellation, full inventory, and recovery where it applies |
| 11 | Dependencies | systems and craft assets; compatibility constraints; order of work |
| 12 | Acceptance criteria | Given an initial state, when an input or event, then an observable state and feedback, and an invariant remains true. Cover 5 paths: success, boundary, interruption, denied action, multiplayer disagreement |
| 13 | Test and instrumentation plan | test IDs, intended audience, device and network conditions, relevant event fields, privacy constraints, decision criterion |
| 14 | Open choices | craft-owned implementation or expression decisions and the bounds they must respect |
| 15 | Approval and change log | owner decision, lead reviews, superseded version, linked tuning revision |

### 3.3 T4 Tuning table contract (RP:433-442), OPINION, 7 fields

Rule: one authoritative data source; documentation links to its revision. A hand-written number copied into several briefs creates avoidable mismatch risk. This is a proposed workflow, not a measured failure rate (RP:434).

| field | required content |
| --- | --- |
| Parameter identity | stable key, system, meaning, owner |
| Value and units | current value or explicit TBD; seconds, distance, currency or another stated unit |
| Domain and relationships | legal minimum and maximum where known; dependencies and invariants |
| Provenance | source, calculation, experiment, or an explicitly untested starting hypothesis |
| Version and application | data revision, build revision, migration rule, server or client authority |
| Evaluation | intended behaviour, telemetry, test condition, result |
| Change record | old value, new value, reason, approver, rollback route |

### 3.4 T5 Per-craft brief template (RP:444-454), OPINION

Shared header, 5 items, present in every brief: the same approved fantasy; the relevant pillar; feature IDs; the state and event vocabulary; the current build and data revision. Exact rules belong to design; craft leads own expression within the agreed limits. An unresolved number is labelled TBD with an owner and a test and is never silently supplied by the model (RP:445).

8 craft rows, 3 columns each:

| craft | facts that must be exact before implementation | decisions left to the craft expert |
| --- | --- | --- |
| UI | inputs; state transitions; priority; strings that carry rules; numerical displays; accessibility needs; failure paths | layout, hierarchy and interaction treatment within readability and device limits |
| VFX | trigger event; affected space; duration dependency; gameplay meaning; visibility rules; information priority | shape, rhythm, material and visual character within signal clarity and performance limits |
| Sound | trigger and cancellation; source location; priority; gameplay information; repetition conditions; subtitle needs | timbre, motif, mix and expressive treatment within audibility and platform limits |
| Animation | gameplay states; actionable timing windows; movement constraints; interruption; contact; readable anticipation | pose, motion style, exaggeration and transitions that keep the specified mechanics |
| Art | interaction function; silhouette and scale constraints; readable states; camera and device context; rights; production budget | shape language, palette, materials and style interpretation, aligned with the art direction |
| Level | intended choices; mechanics taught; route connections; encounter conditions; boundaries; navigation; reset rules | spatial composition, sightlines, landmarks and pacing hypotheses to test |
| Engineering | authoritative rules; state machine; persistence; invariants; input and output contracts; target conditions; testability | architecture, algorithms and implementation strategy, subject to measured constraints |
| Marketing | approved promise; ordinary playable signature moments; audience evidence; restrictions; variant IDs | wording, composition and campaign execution that do not invent absent gameplay |

### 3.5 Section 5 rule table (4 rows, RP:456-460)

| rule | number | tag | source and date | RP |
| --- | --- | --- | --- | --- |
| Keep the current rule and data revision identifiable | no required document page count | OPINION | Author synthesis 2026-10-21 | RP:457 |
| Distinguish correct implementation from intended experience | two different evaluation questions | OPINION | P06, 2006-2007 | RP:458 |
| Make values editable with explicit meaning and units | no sourced default tuning values | OPINION | P19, 2022-12-06 | RP:459 |
| Supply all requested craft contracts | 8 craft brief types | OPINION | User brief and synthesis 2026-10-21 | RP:460 |

## 4. Section 6: Working with a creative director (RP:462-477)

| # | rule or statement (paraphrased) | tag | IDs | RP |
| --- | --- | --- | --- | --- |
| 6.1 | Ed Catmull's account of Pixar's Braintrust: candid advice, but the director keeps the final say. A useful film analogy; not permission for an AI to override a game owner. | EXPERIENCE | P11 | RP:463 |
| 6.2 | How to propose: lead a decision review with one recommendation, the player outcome it protects and the evidence that matters. Show alternatives only when they stand for a real experience, cost or risk tradeoff. Do not offer a menu just to avoid judgment. Do not hide uncertainty to look decisive. Include the strongest objection and the evidence that would change your view. | OPINION | none | RP:465 |
| 6.3 | Classify disagreement. Empirical dispute: needs a discriminating test. Technical dispute: needs a measured constraint and the specialist's alternatives. Taste and creative ambition: belong to the owner. Scope and acceptable risk: need an explicit decision. A binding safety, legal or platform restriction: a constraint to explain, not a score to average away. (5 classes.) | OPINION | none | RP:467 |
| 6.4 | How to push back: state the observed problem, its consequence for the approved fantasy, and a smaller change that may fix it. Keep bold intent where possible. After the owner chooses, record the decision and adapt the plan. Reopen only for material new evidence or an agreed reconsideration trigger. | OPINION | none | RP:469 |

### 4.1 T6 Decision record template (RP:471), OPINION, 13 items

Item 1 pairs ID and date, so the paper lists 13 items. A pending decision remains pending.

| # | field | what it holds |
| --- | --- | --- |
| 1 | decision ID and date | identifier and date |
| 2 | question | the question being decided |
| 3 | approved intent | the intent already approved |
| 4 | recommendation | the designer's single recommendation |
| 5 | material alternatives | alternatives that differ in experience, cost or risk |
| 6 | evidence and uncertainty | what supports it and what is not known |
| 7 | exact owner decision | the owner's decision, exactly |
| 8 | rationale | why |
| 9 | affected specifications, assets, tuning and tests | the artifacts that change |
| 10 | accountable leads | who answers for the follow-up |
| 11 | next verification | the next check |
| 12 | reconsideration trigger | what would reopen it |
| 13 | superseded decision | the earlier decision this replaces |

### 4.2 Section 6 rule table (4 rows, RP:473-477)

| rule | number | tag | source and date | RP |
| --- | --- | --- | --- | --- |
| Advice does not replace the deciding director | director keeps final say | EXPERIENCE | P11, 2014 | RP:474 |
| Present a recommendation and consequential alternatives | no required option count | OPINION | Author synthesis 2026-10-21 | RP:475 |
| Separate empirical disputes from creative preference | no universal scoring formula | OPINION | Author synthesis 2026-10-21 | RP:476 |
| Record decisions without inventing approval | every consequential change | OPINION | User brief 2026-10-21 | RP:477 |

## 5. Section 7: Process for an AI designer (RP:479-531)

### 5.1 Numbered idea method with explicit counts (RP:480-489), OPINION

Framing (RP:481): a configurable studio procedure, not an experimentally established optimum. Record the actual count and budget at every step. The N variables are placeholders, never reported results. The only fixed deliverable count is the owner's requested 3 final pitches. Source studies do not validate a universal Roblox concept funnel.

Count variables:

| variable | meaning | relation the paper states | RP |
| --- | --- | --- | --- |
| N0 | opportunities taken in from the trend scout | - | RP:482 |
| N1 | usable opportunity records | at most N0 | RP:482 |
| N2 | raw concepts generated; chosen from review capacity and available time; record who chose it and why | none stated to N1 | RP:483 |
| N3 | candidates after mechanism expansion | configurable | RP:484 |
| F3 | distinct mechanism families among N3 | measured from this batch, not configured | RP:484 |
| N4 | distinct candidates after dedup | at most N3 | RP:485 |
| N5 | candidates with evidence gaps and the cheapest discriminating test | none stated to N4 | RP:486 |
| N6 | tested or explicitly untested candidates | none stated to N5 | RP:487 |
| 3 | final pitches (the one fixed count) | exactly 3 if 3 defensible concepts exist | RP:481, 488 |
| 1 | chosen concept | owner picks | RP:489 |

Steps (all OPINION; no registry ID is cited per step):

| step | action (paraphrased) | record or output | RP |
| --- | --- | --- | --- |
| 1 Intake | Take in N0 opportunities from the trend scout. For each record: observation date, rising behaviour, audience, evidence, comparison period, outside-world trigger, alternative explanation (7 fields). Reject unsupported trend claims, not unusual fantasies. | N1 usable records, N1 at most N0 | RP:482 |
| 2 Search budget | Set the search budget before generating. Pick N2 raw concepts from review capacity and time; record who chose N2 and why. Generate independently across action, role, setting, threat, social relationship and consequence (6 axes). | N2 one-sentence concepts, unranked | RP:483 |
| 3 Expand | Expand distinct mechanisms, not synonyms. For each promising seed vary: what the player can do, what can go wrong, who changes the outcome, what persists (4 axes). Use, where each fits: inversion, distant analogy, a constraint, a counterfactual, an anti-cliche pass (5 techniques). | N3 candidates and F3 distinct mechanism families (N3 configurable; F3 measured) | RP:484 |
| 4 Deduplicate | Deduplicate by playable action and consequence. Group titles sharing action, reward and escalation for comparison, but keep distinct fantasies when theme, role, social meaning or audience appeal differs. Keep an unusual candidate when its failure mode is uncertain and cheap to test. | N4 distinct candidates, N4 at most N3 | RP:485 |
| 5 Independent critic | Run an independent critic pass after divergence. Check 7 criteria: fantasy, causal loop, first image, agency, hook delivery, scope, policy and IP risk. Mark each criterion FAIL, UNKNOWN, PLAUSIBLE or OBSERVED. Do not add scores into a fake precision total. | N5 candidates with evidence gaps and the cheapest discriminating test | RP:486 |
| 6 Owner selects or authorizes tests | Ask the owner to select, or to authorize tests, when taste or acceptable risk drives the decision. Test the uncertainty that could change the ranking. Report respondents, recruitment, build, variant exposure, measures and uncertainty, including negative evidence. | N6 tested or explicitly untested candidates; never quietly label an untested candidate validated | RP:487 |
| 7 Deliver pitches | Deliver exactly 3 concept pitches if 3 defensible concepts exist. If fewer survive, show the shortfall and ask for more exploration instead of filling the deck with known weak ideas. Name a recommendation and its tradeoff. Keep a materially different alternative when evidence cannot decide. | 3 pitches (T7 per pitch) | RP:488 |
| 8 After the owner picks 1 concept | Replace the funnel with an uncertainty register. Develop the chosen fantasy into pillars, loop, style targets, system dependencies, content examples, test plans and craft briefs. One chosen concept is not one frozen solution to every implementation problem. | uncertainty register plus the documents of section 3 above | RP:489 |

### 5.2 T7 Concept pitch template (RP:491-505), OPINION, 13 fields

Use one copy per pitch (3 pitches). Keep proposed content separate from evidence (RP:492).

| # | field | what it holds |
| --- | --- | --- |
| 1 | Concept ID and version | identifier, author, date, current decision |
| 2 | Title candidates | distinct titles and the promise each makes; do not imply a tested winner |
| 3 | One-line fantasy | form: As [role], I [consequential verb] so that [desired change], while [pressure or uncertainty] |
| 4 | Hook | one surprising action or relationship; why a player might want to try it |
| 5 | First image | camera view, readable player action, scale relationship, immediate stakes; label it as concept art |
| 6 | Core loop in one sentence | form: [goal] leads to [choice and action], then [feedback and consequence], then [a changed reason to act again] |
| 7 | Signature moment | ordinary inputs produce a demonstrable consequence; the art, animation, VFX and sound it needs |
| 8 | Why now | dated trend evidence, target audience, alternative explanation, what may be temporary |
| 9 | Familiar foundation and original contribution | named loop reference, changed rule, own expression, rights questions |
| 10 | Smallest buildable version | the complete promise-preserving interaction; excluded breadth; dependencies and target devices |
| 11 | Failure hypothesis | the strongest reason it may fail and the cheapest test that could show it |
| 12 | Evidence | source IDs, observed facts, untested assumptions, test results and their limits |
| 13 | Recommendation to owner | approve experiment, revise, hold or reject; alternatives and the cost of delay |

### 5.3 Checks from the chosen concept to an approved design baseline (RP:507-510), OPINION

Trace-back checks (RP:508), 7 statements:

| # | check |
| --- | --- |
| 1 | every document traces to the same promise and pillars |
| 2 | world and characters make the role intelligible |
| 3 | the opening teaches the decisive verb |
| 4 | the loop creates repeatable consequences |
| 5 | systems support that loop, not unrelated genre conventions |
| 6 | content examples show variation, not only volume |
| 7 | every craft brief uses the same state names and data revision; every uncertain assumption has an owner and a fitting test |

Before asking for production approval (RP:510):

| # | check |
| --- | --- |
| 1 | ask the receiving agents to restate the behaviour and name ambiguity |
| 2 | compare their interpretations |
| 3 | review a representative integrated moment, not only separate asset approvals |
| 4 | check device, network, social and policy assumptions against current platform evidence |
| 5 | keep known omissions and unproven scaling assumptions visible |
| 6 | the owner approves the next commitment, not a guarantee that the final game will be fun |

### 5.4 "Do not do" list (10 items, RP:512-522), all OPINION

| # | do not | reason or example the paper gives | IDs | RP |
| --- | --- | --- | --- | --- |
| D1 | declare a creativity method universally best from a narrow model/task result | recent studies show tradeoffs and judge sensitivity | A01, A02, A08 | RP:513 |
| D2 | treat novelty, owner taste and market demand as one score | personalization can improve one rating dimension and worsen another | A06 | RP:514 |
| D3 | claim an attractive AI proposal has survived execution | older-model study: 43 expert researchers, over 100 hours each, larger post-execution score drops for AI ideas; it motivates real tests, not a claim about current models | A13 | RP:515 |
| D4 | copy a successful game's expressive identity, or assume a licensed franchise example grants rights | - | L01, R18 | RP:516 |
| D5 | let a novelty critic kill every unproven premise before a cheap faithful experiment exists | - | A08 | RP:517 |
| D6 | postpone identity indefinitely while polishing disconnected parts | Supercell's 2026 retrospective names delayed hard decisions in Clash Mini and too little genre affinity in Hay Day Pop as situated failure lessons | P07 | RP:518 |
| D7 | confuse prototype code, a polished demo or a successful pitch with production readiness | - | P03, P15, P18 | RP:519 |
| D8 | invent durations, retention targets, scoring weights, content counts or owner approvals to finish a template | - | U01 | RP:520 |
| D9 | promise in marketing what ordinary play cannot deliver, or treat click appeal alone as proof of a durable loop | - | R07-R11, C19 | RP:521 |
| D10 | leave contradictory rules, unexplained tuning values or craft-state mismatches for implementers to settle alone | - | P06, P16 | RP:522 |

### 5.5 Open questions (7, RP:524-525), OPINION

The next useful evidence is project-specific. No source in the paper gives a universal answer or a guaranteed hit formula.

| # | question |
| --- | --- |
| Q1 | which mechanism families does the actual model miss under this owner's brief |
| Q2 | which generation method improves blinded owner preference and prototype survival at equal cost |
| Q3 | what separates the owner's fantasy preference from tolerance for production risk |
| Q4 | which first-image readings match what players actually do |
| Q5 | which promise the available leads can implement faithfully on target devices |
| Q6 | what scope can be produced repeatedly at the agreed quality |
| Q7 | which current Roblox cohorts and discovery definitions apply to this experience |

### 5.6 Section 7 rule table (4 rows, RP:527-531)

| rule | number | tag | source and date | RP |
| --- | --- | --- | --- | --- |
| Preserve actual counts and avoid invented quotas | N0 through N6 are configurable | OPINION | Author synthesis 2026-10-21 | RP:528 |
| Produce the requested final concept set | 3 pitches then 1 chosen concept | OPINION | User brief 2026-10-21 | RP:529 |
| Replace conjecture with scoped prototype evidence | no universal pass percentage | OPINION | P02 and A13, 2020-2026 | RP:530 |
| Stop at explicit unresolved decisions rather than inventing them | per blocked requirement | OPINION | Author synthesis 2026-10-21 | RP:531 |

## 6. Template inventory (check C1)

| id | template | location | count |
| --- | --- | --- | --- |
| T1 | Pillars sheet | RP:347-357 | 9 fields |
| T2 | Preproduction plan and lead review table | RP:368-377 | 7 review rows x 4 columns (review, inputs and leads, decision, required output) |
| T3 | Feature specification | RP:415-431 | 15 fields |
| T4 | Tuning table contract | RP:433-442 | 7 fields |
| T5 | Per-craft brief | RP:444-454 | 5 shared header items + 8 craft rows x 2 content columns |
| T6 | Decision record | RP:471 | 13 items (item 1 pairs ID and date) |
| T7 | Concept pitch | RP:491-505 | 13 fields |

## 7. Claims to fact-check (fact-checking is a separate ticket; none checked here)

| # | claim or number | scope the paper gives | RP | IDs |
| --- | --- | --- | --- | --- |
| F01 | Riot prototype exit criteria are four items: identified audience, playable risky innovations, shared understanding, audience playtest evidence | Riot R&D reported practice | RP:330 | P02, P03 |
| F02 | Riot engineering account separates "whether to build" from "how to build"; disposable code can be appropriate for learning | Riot reported practice; fresh code environment is not universal | RP:330 | P03 |
| F03 | Rami Ismail describes a vertical slice as a production prototype | practitioner view; stage terminology varies | RP:336 | P15 |
| F04 | Double Fine's Psychonauts 2 documentary shows pilot areas making quality concrete across exploration, puzzles, art and narrative | transcript spans inspected only at 18:56-23:53 and 35:29-38:59 | RP:336 | P13 |
| F05 | Riot places artists inside prototype problem-solving while allowing parallel visual exploration | Riot article; no staffing minimum | RP:339 | P04 |
| F06 | Blizzard Venture: a paper drill concept changed after it failed to read in first-person 3D | Blizzard News article, published 2024-04-17 | RP:339 | P12 |
| F07 | Valve Half-Life 2 process separates initial constraints from proposals and asks whether the intended experience happened and was desirable | 28-page GDC deck, 2006/2007 | RP:343 | P06 |
| F08 | Into the Breach: readable, deterministic combat decisions propagated into UI, enemy and weapon constraints | 49-page GDC 2019 deck; project-specific | RP:343 | P16 |
| F09 | Condor Diablo pitch: 8 pages, 1994, published by David Brevik in 2016, holds player activity, production assumptions and a schedule, expects revision, proposed turn-based play | PDF; only pages 1, 2, 7, 8 visually inspected per registry | RP:360, 382 | P08 |
| F10 | FTL GDC 2013 account begins from the experience of captaining a starship and lets gameplay structures change | only the session abstract was inspected | RP:362 | P09 |
| F11 | My Work Is Not Yet Done pitch includes identity, imagery, gameplay pillars, comparables, audience signals, remaining work and an ask | public Google Doc text; the PDF was not separately inspected | RP:364 | P17 |
| F12 | The author later said the initial budget was too low and changed after publisher advice | author article; one signing | RP:364 | P18 |
| F13 | Raw Fury pitch guidance is recipient-specific | current requirements, not historical proof | RP:366 | P14 |
| F14 | Riot gives subject-matter expertise a decision role; Valve gives local autonomy inside shared constraints with global-coherence mechanisms | reported experience | RP:396 | P03, P06 |
| F15 | Sakurai's official description emphasizes changing parameters during balance work as more people participate | only YouTube title, author, date and description were verified; video not reviewed | RP:411 | P19 |
| F16 | Ed Catmull: Pixar's Braintrust gives candid advice while the director has final say | film analogy | RP:463 | P11 |
| F17 | Count: exactly 3 final pitches; 1 chosen concept; 8 craft brief types; N0-N6 configurable | owner brief; studio procedure | RP:481, 488, 489, 460, 528, 529 | U01 (inferred for "User brief") |
| F18 | Older-model study: 43 expert researchers, over 100 hours each, larger post-execution score declines for AI ideas | older generator, NLP domain; the 43 and 100-hour figures appear nowhere else in the paper and not in the A13 registry entry | RP:515 | A13 |
| F19 | A01, A02, A08 show tradeoffs and judge sensitivity in creativity methods | narrow model/task results | RP:513 | A01, A02, A08 |
| F20 | A06: personalization can improve one rating dimension and worsen another | business-idea evaluation; no game-player validation | RP:514 | A06 |
| F21 | US Copyright Office guidance: game ideas are not copyright-protected (the paper cites L01 for "do not copy expressive identity / franchise rights") | US guidance only | RP:516 | L01 |
| F22 | Roblox Community Standards on repetitive content and IP (the paper cites R18 for the same do-not) | current standards at 2026-10-21 | RP:516 | R18 |
| F23 | Supercell's 2026 retrospective names delayed hard decisions in Clash Mini and insufficient genre affinity in Hay Day Pop as failure lessons | the registry scope note mentions only a monetization example; Clash Mini and Hay Day Pop are not in the registry text | RP:518 | P07 |
| F24 | Marketing must not promise what ordinary play cannot deliver; click appeal alone does not prove a durable loop (Roblox discovery sources R07-R11 and C19 cited) | Roblox discovery pages (live docs, accessed 2026-10-21; R07 dated 2026-06-15); C19 is an undated podcast transcript | RP:521 | R07, R08, R09, R10, R11, C19 |
| F25 | Rule-table dates: P02-P04 2020-2021; P15 2022; P08 1994 (pub. 2016); P06 2006-2007; P16 2019; P03-P04 2021; P12 2024; P11 2014; P19 2022-12-06; P02 and A13 2020-2026 | registry dates: P02 2020-06-18, P03 2021-02-23, P04 2021-05-21, P15 2022-09-26, P08 2016-03-19, P12 2024-04-17, P11 2014-03-12, P19 2022-12-06, A13 ICLR 2026 | RP:380-383, 401-403, 458-459, 474, 530 | various |

Roblox-specific facts in lines 329-534: none with a number. Only pointers to Roblox sources: R18 (RP:516), R07-R11 (RP:521), and unsourced calls to "current platform evidence" (RP:510) and "current Roblox cohorts and discovery definitions" (RP:525).

## 8. Contradictions and weak spots

| # | weak spot | RP |
| --- | --- | --- |
| W01 | The T2 plan paragraph asks each review to have a question, artifact, decision owner and exit evidence, but the table has no decision-owner or exit-evidence column. It has "inputs and leads", "decision" and "output". The owner is named only in some "decision" cells (Concept, Production readiness). | RP:369-377 |
| W02 | Tag mismatch: RP:336 tags the Ismail/Double Fine sentence EXPERIENCE, but P15 is OPINION in the registry (and the section 3 rule row for P15 is OPINION). | RP:336, 381, 852 |
| W03 | Tag mismatch: RP:411 tags the Sakurai sentence EXPERIENCE, but P19 is OPINION in the registry and the section 5 rule row is OPINION. The registry also says the full video was not reviewed. | RP:411, 459, 876 |
| W04 | Tag mismatch: P06 and P16 are VERIFIED artifact content in the registry, but RP:343 tags the Valve/Into the Breach sentence EXPERIENCE, and P16's scope says efficacy remains reported experience. The paper calls them process talks, not full design documents (RP:366). | RP:343, 366 |
| W05 | The FTL claim (captaining a starship; gameplay structures may change) is attributed to P09, but the registry says only the session abstract was read and warns against adding specifics. The key excerpt covers only the primacy of player experience. | RP:362, 825 |
| W06 | P08 pages: the registry says only pages 1, 2, 7 and 8 of the PDF were visually inspected; the paper makes claims about the whole pitch (content, schedule, "eight-page"). | RP:360, 819 |
| W07 | RP:481 says the only fixed deliverable count is the 3 pitches, yet the section 5 rule row fixes "8 craft brief types" (RP:460) and the section 7 rule row adds "1 chosen concept" (RP:529). Also "exactly 3" (RP:488) is conditional: fewer may be shown if fewer than 3 are defensible. | RP:481, 460, 488, 529 |
| W08 | The N variables have only partial relations: N1 at most N0 and N4 at most N3 are stated. No relation is given for N2 to N1, N3 to N2, N5 to N4 or N6 to N5. No default values exist by design; no way to measure F3 or to judge "distinct" is given in this range. | RP:482-487 |
| W09 | Step 5 asks for an "independent" critic but does not say what independence means (separate model, context or person). D1 and D5 warn that judge setups are sensitive and that critics must not kill unproven premises. The only guard stated is the UNKNOWN label. | RP:486, 513, 517 |
| W10 | Step 2 requires recording who chose N2 and why, but does not say whether the owner or the designer chooses; steps 6 and 7 assign owner roles only later. | RP:483, 487 |
| W11 | The A13 figures (43 researchers, over 100 hours each) appear only at RP:515, with no figure or number in the registry entry. They have no checkable anchor inside the paper. | RP:515, 611-615 |
| W12 | P07 is cited for Clash Mini and Hay Day Pop, but its registry scope note mentions only a monetization example and calls it a historical emergency target, not a default. The supporting text is not in the registry. | RP:518, 809-813 |
| W13 | R07-R11 and R18 have no "Scope" line in the registry, unlike most other entries, though D9 and D4 depend on them. R08-R11 are undated live documentation, known only as read on the access date. | RP:521, 516, 887-915 |
| W14 | Status vocabulary differs between templates: pillar status is approved, proposed or retired (RP:357); feature status is proposed, approved, implemented or retired (RP:417); section 5 prose lists proposals, approved decisions, implemented behaviour and superseded versions (RP:409); the decision record uses "superseded decision" (RP:471). "Retired" and "superseded" are not defined against each other. | RP:357, 417, 409, 471 |
| W15 | The rule tables' "number" column mostly holds statements such as "no universal ..." rather than numbers. Rows with a real count: 8-page Diablo (RP:382), 8 craft brief types (RP:460), 3 pitches then 1 (RP:529), N0-N6 (RP:528). Six rule rows cite only "Author synthesis 2026-10-21" (RP:404, 457, 475, 476, 528, 531) and three cite "User brief" (RP:460 with synthesis, 477, 529), probably U01 but not stated; none has a registry ID. | RP:379-531 |
| W16 | The rule row "Replace conjecture with scoped prototype evidence" cites "P02 and A13 2020-2026" with the number "no universal pass percentage"; no section 3-7 text states a pass percentage or discusses one. | RP:530 |
| W17 | The rule row "Test presentation in the gameplay perspective" is tagged EXPERIENCE (P12) and has no matching prose sentence in section 4; the only supporting story (Venture paper drill) sits in section 3. | RP:402, 339 |
| W18 | The lead list names a trend scout and the T2 table uses it, but the paper never gives the trend scout an ownership sentence like the other leads. | RP:386, 392 |
| W19 | The registry has no P05 or P10 entry (IDs skip them); range citations such as "P02-P04" therefore cover P02, P03, P04 only. | RP:380, 779-803 |
| W20 | The paper's date: research cutoff and access date are 2026-10-21, one day after this kit's current date of 2026-10-20. Dates in the registry should be read as given. | RP:18, 540 |
| W21 | Registry titles lost their punctuation (colons, apostrophes, hyphens) in the text file; the source table below restores a plain dash only to keep titles readable. | RP:539-981 |

## 9. Source table (every ID cited in lines 329-534)

Scope note = the paper's scope line, paraphrased. R07-R11 and R18 have no scope line. "Used at" lists the RP lines in this file's range. Accessed 2026-10-21 for all unless stated.

| ID | title | date | tag | URL | scope note (paraphrase) | used at |
| --- | --- | --- | --- | --- | --- | --- |
| A01 | Old Ideas, Novel Problems - The Instability of LLM-Based Novelty Evaluation (Sternlicht et al.) | posted 2026-10-01; version 2026-10-14 | VERIFIED measured study | https://arxiv.org/html/2610.02022v2 | some low-novelty labels partly assumed; narrow research domain; no game-ideation outcome validation | RP:513 |
| A02 | Evaluating LLM Creativity through Long-Tail Performance (Wang et al.) | 2026-10-09 | VERIFIED measured study | https://arxiv.org/html/2610.12998v1 | intervention result is not a frontier-model estimate; quality and originality proxies are incomplete | RP:513 |
| A06 | Aggregate vs Personalized Judges in Business Idea Evaluation - Evidence from Expert Disagreement (Hirota et al.) | 2026-07-02 / 2026-07-07 | VERIFIED measured study | https://aclanthology.org/2026.acl-industry.61.pdf | alignment sometimes gets worse; no game-player validation; matching a preference does not forecast market success | RP:514 |
| A08 | Beyond One Path - Evaluating and Enhancing Divergent Thinking in Interactive LLM Agents (Park et al.) | 2026-05-27 | VERIFIED measured study | https://arxiv.org/html/2605.28465v1 | small human-authored scenario set; predefined success paths; LLM-judged action properties; originality can fall while goal discovery rises | RP:513, 517 |
| A13 | The Ideation-Execution Gap - Execution Outcomes of LLM-Generated versus Human Research Ideas (Si, Hashimoto, Yang) | ICLR 2026 | VERIFIED measured study | https://arxiv.org/html/2506.20803v1 | old generator; NLP domain; human execution choices mediate outcomes; not a ceiling for present models | RP:515, 530 |
| C19 | Panic Podcast Episode 1 - Untitled Goose Game (transcript; Panic with House House and the publishing team) | undated (page shows an invalid date; none invented) | EXPERIENCE | https://podcast.panic.com/episodes/s01e01/transcript/ | transcript read, audio not watched; timing and influence statements are participant recollections | RP:521 |
| L01 | Games (US Copyright Office) | undated | VERIFIED official guidance | https://www.copyright.gov/register/tx-games.html | US copyright guidance only; not global clearance, trademark advice, or permission under Roblox rules | RP:516 |
| P02 | Prototype - Building a Game's Substance (Tom Cadwell, Riot Games) | 2020-06-18 | EXPERIENCE | https://www.riotgames.com/en/r-and-d-office/prototype-building-a-games-substance | official article read; "proof" is the author's wording, not statistical validation | RP:330, 380, 530 |
| P03 | Engineering in Riot R&D (Baris Yaman, Riot Games) | 2021-02-23 | EXPERIENCE | https://www.riotgames.com/en/r-and-d-office/engineering-in-riot-r-d | full article read; the fresh code environment is Riot's practice, not universal advice | RP:330, 380, 396, 401, 519 |
| P04 | Collaborative Creative in R&D (Andy Lang, Riot Games) | 2021-05-21 | EXPERIENCE | https://www.riotgames.com/en/r-and-d-office/collaborative-creative-in-r-d | full article read; do not turn its typical staffing into a universal minimum | RP:339, 380, 401 |
| P06 | Valve's Design Process for Creating Half-Life 2 (David Speyrer, Brian Jacobson, Valve) | 2006 (GDC listing); 2007 (slide copyright) | VERIFIED artifact content | https://cdn.akamai.steamstatic.com/apps/valve/2006/GDC2006_HL2DesignProcess.pdf | 28-page primary slide deck text read; reports studio experience, not a controlled study | RP:343, 366, 383, 396, 403, 458, 522 |
| P07 | What We've Learned from Failures (Supercell) | 2026-01-15 | EXPERIENCE | https://supercell.com/en/news/learning-from-failures/ | full official report read; its monetization example is a historical emergency target, not a recommended default | RP:518 |
| P08 | Diablo - Game Concept by Condor, Inc. (published by David Brevik) | 1994 (artifact); 2016-03-19 (publication) | VERIFIED artifact content | https://www.graybeardgames.com/download/diablo_pitch.pdf | PDF from the author-linked URL; pages 1, 2, 7 and 8 visually inspected; proposed plans, not shipped outcomes | RP:360, 382 |
| P09 | Designing Without a Pitch - FTL Postmortem (Matthew Davis, Justin Ma, Subset Games) | 2013 | EXPERIENCE | https://gdcvault.com/play/1018034/Designing-Without-a-Pitch-FTL | official GDC session abstract read; video not reviewed; add no further specifics | RP:362 |
| P11 | Pixar's Ed Catmull On How Disney Found Its Way To A Hit With Frozen (Ed Catmull, Fast Company) | 2014-03-12 | EXPERIENCE | https://www.fastcompany.com/3027544/getting-to-frozen-how-the-disney-braintrust-grew-up | first-person interview or byline read; film-process analogy, not game-development or AI-efficacy evidence | RP:463, 474 |
| P12 | Ready to Make History - A Look into Venture's Development (Daryl Tan, Miranda Moyer, Blizzard) | 2024-04-17 | EXPERIENCE | https://news.blizzard.com/en-us/article/24072104/ready-to-make-history-a-look-into-venture-s-development | full official Blizzard News mirror read; the original Overwatch URL returned 403 | RP:339, 402 |
| P13 | PsychOdyssey EP18 - What Good Looks Like (Double Fine / 2 Player Productions) | 2023-01-20 (site-listed) | EXPERIENCE | https://www.doublefine.com/dftv/psychodyssey-ep18-what-good-looks-like | documentary transcript read around 18:56-23:53 and 35:29-38:59; edited film; publication date is not filming date | RP:336 |
| P14 | How to Pitch to Raw Fury (Johan and David, Raw Fury) | n.d. (retrieved 2026-10-21) | OPINION | https://rawfury.com/how-to-pitch-to-raw-fury/ | full official guidance read; recipient-specific requirements, not historical proof or universal pitch rules | RP:366 |
| P15 | Prototypes & Vertical Slice (Rami Ismail) | 2022-09-26 | OPINION | https://ltpf.ramiismail.com/prototypes-and-vertical-slice/ | full article read; a practitioner's recommended distinction; stage terminology varies; do not copy universal timelines or prototype asset-use advice | RP:336, 381, 519 |
| P16 | Into the Breach Design Postmortem (Matthew Davis, Subset Games) | 2019 (GDC) | VERIFIED artifact content | https://media.gdcvault.com/gdc2019/presentations/Into%20the%20Breach%20Postmortem%20Final.pdf | 49-page primary deck text read; constraint choices are project-specific; efficacy remains reported experience | RP:343, 366, 383, 522 |
| P17 | Pitch to Raw Fury - My Work Is Not Yet Done (Spencer Yan, Sutemi Productions) | 2021 (pitch context); 2022-10-28 (public report) | VERIFIED artifact content | https://docs.google.com/document/d/189KJ3IcxRvf6gE9xs8u1_e6RJ3zkWr3XAVYC-WoCbpM/edit?usp=sharing | public Google Doc exported as text and read; original PDF link verified to exist but PDF contents not separately inspected | RP:364 |
| P18 | Publisher Pitch for My Work Is Not Yet Done (Spencer Yan) | 2022-10-28 | EXPERIENCE | https://spncryn.medium.com/pitch-to-raw-fury-for-my-work-is-not-yet-done-22d7e45c1993 | full author article read; one developer's account of one signing; not proof the template generally works or that the game shipped as planned | RP:364, 519 |
| P19 | Making Your Game Easy to Tune - Programming & Tech (Masahiro Sakurai) | 2022-12-06 | OPINION | https://www.youtube.com/watch?v=nGaajB8m5Q0 | YouTube title, author, date and description verified; full video and transcript not reviewed; add no claims about spreadsheets or implementation internals from secondary transcripts | RP:411, 459 |
| R07 | Optimizing Discovery - How Great Games Reach Millions of Players on Roblox (Roblox) | 2026-06-15 | VERIFIED | https://about.roblox.com/newsroom/2026/06/optimizing-discovery-great-games-reach-millions-players-roblox | no scope line in the registry | RP:521 |
| R08 | Discovery - current ranking signals and content quality restrictions (Roblox docs) | undated live documentation | VERIFIED | https://create.roblox.com/docs/discovery | no scope line in the registry | RP:521 |
| R09 | Discovery FAQ (Roblox docs) | undated live documentation | VERIFIED | https://create.roblox.com/docs/discovery-faq | no scope line in the registry | RP:521 |
| R10 | Thumbnails - personalization, testing result and authentic video (Roblox docs) | undated live documentation | VERIFIED | https://create.roblox.com/docs/production/publishing/thumbnails | no scope line in the registry | RP:521 |
| R11 | Publish games and places - metadata best practices (Roblox docs) | undated live documentation | VERIFIED | https://create.roblox.com/docs/production/publishing/publish-games-and-places | no scope line in the registry | RP:521 |
| R18 | Community Standards - repetitive content and intellectual property (Roblox) | current standards | VERIFIED | https://about.roblox.com/community-standards | no scope line in the registry | RP:516 |
| U01 | User supplied research brief (studio owner) | provided 2026-10-21 | OPINION (studio operating instruction) | the two research prompts supplied by the owner; no URL | the prompts set the requested scope, the final three pitches and owner decision rights | RP:520 |

Registry notes (RP:537): dates separate publication, revision and measurement where known; every URL was inspected or verified through primary-source research; the registry supports the factual statements and attributed practices; the templates and proposed operating rules remain OPINION; sources shared between the two companion papers keep the same evidence limits.
