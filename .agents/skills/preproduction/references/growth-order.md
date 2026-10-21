> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Part of `preproduction`. Sources: owner 2026-10-20 (growth order and leads, J003), N2 §1-§2 and §5.3 (dependency order, T2 lead reviews, close-out, readiness checks), O unless marked. The decision-owner and exit-evidence columns are a J003 addition (the paper asks for them but its table has none, N2 W01).

# Growth order: one step, one owner decision

## 1. The steps
The owner's order (owner): fantasy, style direction, key characters and moments, world, core loop, features, content. The paper's dependency rule decides what each step must settle: fix only what the next experiment or build needs; leave untested detail open; a missing choice gets an owner and the next evidence, not an invented answer (N2 3.3). Steps can overlap (the architect starts on risky claims at step 1); a failed test can send work back a step without voiding the fantasy (P-01).

| # | Step | Settles (minimum) | Leads in | Owner decides | Documents |
| --- | --- | --- | --- | --- | --- |
| 1 | **Fantasy and promise** | fantasy line, audience, device mix, title, first image, signature moment, the risky claims | trend scout (why now), marketing (promise), architect (risky claims) | the promise and its open risks | vision record, promise ledger, `concept` key art of the fantasy (`reference-images`) |
| 2 | **Pillars** | 3-5 pillars as decisions with exclusions and tests | art director, architect (read and object) | the pillars and their priority when they conflict | pillar sheets |
| 3 | **Style direction** | what reads first, silhouettes that carry role, colour meaning, scale, excluded references; one visual target next to a playable test when appeal depends on tone | art director (owns), UI, VFX, sound, animation (constraints) | the visual target | style section of vision record; art bible (`knowledge/design/art-bible.md`, art director owns the locks, owner approves) |
| 4 | **Key characters and moments** | characters as ways to make the role and action readable; 3-6 key moments as beat sheets (setup, decision, consequence, payoff) | art director, animator, VFX, sound | which moments define the game | world-and-characters, moment beat sheets (`templates/jobs/beat-sheet.md`), `concept` images of each key moment |
| 5 | **World** | places, routes, landmarks, the first view, where each moment happens | level lead (environment-designer), art director | the world shape | world-and-characters, level briefs (`level-design`) |
| 6 | **Core loop** | moment, session and long-term loops and how they couple; what resets, what persists; grey-box test plan | architect, level lead, crafts needed for the loop | the loop to prototype | core-loop, experiment cards (`game-design`) |
| 7 | **Features** | one spec per feature (15 fields), state names, tuning keys | architect (contracts), economy (if any), UI | which features are in, out, later | feature specs |
| 8 | **Content** | content examples that show variation, not only volume; the content pipeline and its data files | environment-designer, architect | the first content set | content plan in core-loop or feature specs |
| 9 | **Readiness** | §4 checks pass | all leads | approve the next commitment | decision record |

One decision per step goes into the owner's digest (lead), batched with any other open item. Default if no answer: the recommended option, marked PROPOSAL.

## 2. The seven lead reviews (N2 T2 + J003 columns)
| Review | Inputs and leads | Decision | Decision owner | Output | Exit evidence |
| --- | --- | --- | --- | --- | --- |
| Concept | designer + trend scout: fantasy, evidence, alternatives | select the experiment or reject | owner | decision record, uncertainty list | owner's words in `decisions.md` |
| Promise | designer, marketing, art director: title, first image, signature moment | does play match what is advertised | owner | approved promise; failed claims removed | promise ledger: every claim mapped |
| Feasibility | designer + architect: target devices, player count, persistence, risky interactions | which risk could kill the fantasy | owner (on the architect's evidence) | bounded risk prototypes, measured results | measurements on target conditions |
| Style and readability | art director, UI, VFX, animation, sound, level lead: cheap visual targets + a playable scene | can every craft show the same state and priority | owner (look); art director (consistency) | shared state vocabulary, craft constraints | one integrated capture reviewed by all crafts |
| Core loop | designer, level lead, architect, crafts: grey box + observations | is the intended choice and consequence present | owner | revised loop, observations, next test | playtest records (`game-design`) |
| Production readiness | all leads: representative slice, content workflow, dependencies, estimates | is there enough evidence to authorize the next scope | owner | decision, remaining risks, exclusions | §4 checks |
| Change | affected leads: proposed change + impact map | is the benefit worth the rework or changed promise | owner | versioned decision, synced briefs | every affected brief updated |

## 3. Close every early review the same way (N2 2.3)
1. The exact decision. 2. Its owner. 3. Affected files. 4. Open questions. 5. Evidence needed next. The owner settles direction and resource tradeoffs; leads raise specialist risks and alternatives; the designer records agreement, never fabricates a lead's approval, never reads silence as consent.

What each lead needs from the designer (N2 §2): art director: what must read first, which silhouettes carry role, what colour means, how scale supports the fantasy, excluded references, the real camera and device (art discovery may improve a mechanic; the handoff is two-way). Architect: the risky claim stated exactly, the conditions it must work under, how it may fail, a cheaper faithful alternative; an offline mockup does not settle network feasibility and a load test does not settle fun. Marketing: the promise ledger. Trend scout: the question to answer and the comparison period. Craft leads: the shared state vocabulary and one representative interaction to review together.

## 4. Readiness checks (N2 §5.3)
Trace-back (all must hold): every document traces to the same promise and pillars · world and characters make the role readable · the opening teaches the decisive verb · the loop creates repeatable consequences · systems support that loop, not genre habit · content examples show variation, not only volume · every craft brief uses the same state names and data revision; every open assumption has an owner and a test.

Before asking for production approval: (1) ask the receiving agents to restate the behaviour and name ambiguity; (2) compare their readings; (3) review one integrated moment, not only separate asset approvals; (4) check device, network, social and policy assumptions against current platform evidence; (5) keep known omissions and unproven scaling assumptions visible; (6) the owner approves the next commitment, not a guarantee of fun.
