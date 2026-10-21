---
type: reference
scope: universal
status: active
updated: 2026-10-20
source: J003
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-20

Source: `Game_Designer_Part_1_Research.txt`, lines 1-328 (summary rules, section 1 ideation with cases 1-15 and the idea scoring rubric, section 2 hook and promise) plus registry entries 535-982 for every ID cited. Paraphrased; the paper stays outside git. Cases 16-18 of the paper are withheld by order (ticket J003-T01) and are not in this file.

# Game designer research, part 1A (paper lines 1-328): ideation, cases, rubric, hook

Reading rule for a skill that uses this file: keep the tag next to every claim. OPINION is the paper's own proposal, never a platform rule and never a measured result. EXPERIENCE is a practitioner account, not a study. VERIFIED is a published measurement or inspectable artifact with its original scope, not proof that it works for any game. Cite as `GP1:<line>` plus the paper's own IDs, e.g. `GP1:45 [A08]`. "Check" flags a possible paper problem; nothing was fixed.

## 1. Source card

| field | value |
| --- | --- |
| What it is | Part 1 of an owner-supplied research paper for an AI game designer in an owner-led Roblox studio. Title line: "From Ideas to an Approved Plan" (GP1:1) |
| Research cutoff | 21 October 2026 (GP1:18) |
| Companion | Part 2 covers gameplay craft and design review (GP1:18). Not in this file |
| Stated aim | An agent that can originate ambitious concepts, explain its reasoning, expose uncertainty and produce coherent implementation briefs. The owner chooses direction. A pitch, an attractive image or a complete spec does not show players will enjoy the game (GP1:20) |
| This file covers | GP1:1-328. Not covered here: section 3 onward (preproduction, pillars, leads, documents, creative director, the 8-step idea method with N0-N6 counts, the concept pitch template, "Do not do", open questions), GP1:329-531 |
| Evidence convention | VERIFIED = published measurements, official platform facts or directly inspected artifact contents, with original scope. EXPERIENCE = a studio or designer reporting practice or outcomes from own work. OPINION = interpretation, recommendation or proposed template. VERIFIED is not causal proof, independent replication or universal applicability (GP1:22) |
| Source IDs | Resolve to dated records and short exact excerpts in the registry (GP1:535-982). Undated sources carry the access date, not an invented day. Proposed numbers and open parameters are kept apart from observed numbers (GP1:22) |
| Registry note | Excerpts under 20 words; registry supports facts and attributed practices; templates and proposed operating rules stay OPINION; every URL was "inspected or verified" (GP1:537) |
| Citation form used here | `GP1:<line>` for the paper line; `[X##]` for the paper's source ID |

## 2. The 15 summary rules (GP1:2-16)

| id | rule (my words) | tag | source IDs | GP1 | check |
| --- | --- | --- | --- | --- | --- |
| S01 | The owner keeps creative authority. Proposals, tests and approvals are three separate records | OPINION | U01 | 2 | |
| S02 | A creativity result belongs to one named model, task and judge. Do not stretch it to all AI systems in 2026 | VERIFIED | A01-A13 | 3 | A scoping instruction tagged VERIFIED |
| S03 | Search for different player decisions and consequences, not for a longer list of reskinned premises | OPINION | A04, A10 | 4 | A04 and A10 do not test game mechanics (GP1:39 says distinct meanings are not yet distinct enjoyable mechanics) |
| S04 | Splitting divergence (generate) from selection improved path discovery in one bounded 2026 study. The tradeoffs depend on the model | VERIFIED | A08 | 5 | One small study, see E08 |
| S05 | Keep a bold but uncertain concept visible when a cheap test can settle its main risk | OPINION | A01, A08 | 6 | Neither source tests keeping concepts alive |
| S06 | Learn the owner's choices and the reasons. Past taste is never a permanent ban on novelty | OPINION | A06, A11 | 7 | |
| S07 | State the fantasy as a role, a consequential action and a wanted outcome before listing features | OPINION | P01, C01-C25 | 8 | C01-C25 cover cases 1-12 only; Roblox cases cite R-IDs |
| S08 | The action promised by title and thumbnail must exist in ordinary play, not only in the trailer | OPINION | R07-R11 | 9 | |
| S09 | A useful prototype tests whether to make the game. Preproduction also tests how to make it | EXPERIENCE | P02, P03 | 10 | Prescriptive rule tagged EXPERIENCE |
| S10 | Art can shape the concept early while prototype assets stay cheap | EXPERIENCE | P04, P12 | 11 | Prescriptive rule tagged EXPERIENCE |
| S11 | Cut breadth before cutting the action, relationship or consequence that makes the fantasy distinctive | OPINION | C01-C25 | 12 | |
| S12 | Write pillars as decisions and exclusions with an observable player effect | OPINION | P06, P16 | 13 | Detail is in section 3-4, outside this extract |
| S13 | Give each craft exact state and rule contracts. Leave expressive choices to the accountable lead | OPINION | P03, P04 | 14 | Detail outside this extract |
| S14 | Keep tuning values in one versioned source, with units, rationale, uncertainty and tests | OPINION | P19 | 15 | Detail outside this extract |
| S15 | Present exactly 3 defensible final pitches as requested. Never fabricate evidence or pad the shortlist with known failures | OPINION | U01 | 16 | The "3" is the owner's request (U01), not a research finding |

## 3. Why generic output happens, and how to diagnose a batch (GP1:26-30)

Five failure types the evidence keeps apart. They are not interchangeable (GP1:26, VERIFIED):

| failure type | note |
| --- | --- |
| Repetition inside one output | separate from the rest |
| Similarity across a portfolio of outputs | A10 measures this as category coverage |
| Low novelty | |
| Low usefulness | |
| Poor fit to the preference | |

Possible causes of convergence (GP1:30, OPINION, not experimentally established for the studio's current model):

| id | cause |
| --- | --- |
| G1 | The prompt hands the model the same familiar references |
| G2 | The setup rewards polished averages |
| G3 | Criticism is asked for before any alternatives exist |
| G4 | Novelty is defined only through vocabulary |
| G5 | Preference data favour familiar text (typicality bias). Part of the convergence is attributed to this by A12 (VERIFIED, GP1:28) |

Diagnosis method (GP1:30, OPINION, proposed design method):

| step | action |
| --- | --- |
| D1 | Take the actual batch. Group the ideas by action, by information, by resource, by relationship and by consequence |
| D2 | If the groups are nearly identical, ask whether the new fantasy, role or social meaning still gives the target audience a distinct reason to care |
| D3 | A change that is only cosmetic proves neither value nor worthlessness. Do not call it either |
| D4 | These five groups are a proposed method. They are not causes shown in the studio's current model |

Related: A10 reports that an early output constrains later ones (fixation) (registry excerpt, GP1:595). The registry flags that the same model generated and categorised, one domain, coverage measured rather than commercial quality (GP1:597).

## 4. AI evidence items A01-A13

Order follows the paper (descending date). "Historical model" = the paper's own word or a plain equivalent ("older", "old", "small") for that result. A blank in that column means the paper does not say.

| id | date (registry) | tag | model(s) and task | the number, with unit | paper's stated limit | historical model? | GP1 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E01 A01 | 2026-10-01, v 2026-10-14; text: October 2026 | VERIFIED | Novelty judging of research ideas. GPT-5.4 pairwise accuracy. Judges: GPT-5.1/5.2/5.4 and Claude Sonnet 4.5/Opus 4.5/4.6 | Accuracy moved 52.6 percentage points between closely related prompts | Do not treat one AI novelty score as fact. Some negative labels were assumed. Does not test Roblox concepts. Registry: narrow research domain, no game-ideation outcome check | not stated | 33, 540 |
| E02 A02 | 2026-10-09 | VERIFIED | 237 prompts. Llama-3.1-8B-Instruct, Gemma-3n-E4B-it, OLMo-3-7B-Think, Qwen3-8B. Temperature raised to 1.5x baseline | Mean novelty +10.7%; overall quality -15.4%. Relative changes in that paper's proxy metrics | Motivates checking quality next to novelty. Does not give the effect on a current frontier model. Registry: quality and originality proxies incomplete | YES ("historical/small-model") | 35, 546-549 |
| E03 A03 | first posted 2026-10-02, v 2026-10-09 | VERIFIED | IdeaScientist: specialised research roles plus cross-domain retrieval; 277 held-out problems. Backbones Claude-4.8-Opus and GPT-5.4 | Claude-4.8-Opus: 77.7 vs 68.7 (SDK comparison). GPT-5.4: 71.9 vs 69.5. Gaps 9.0 and 2.4 score points, not relative percent | Compares the whole harness, not the cause of role separation or analogy retrieval. A 50-paper human comparison adds to automated judging. Proposals not executed. Model-memory contamination possible. Registry: main judging by Qwen3.6-27B | not stated | 37, 552-555 |
| E04 A04 | 2026-09-24 | VERIFIED | Optimised perspective (persona) sets, Gemma-4-31B-it, Alternative Uses task, versus task-only prompting | Response diversity +78.8%; originality +26.1%; judged holistic creativity +13.9% (all relative); validity 98.5% | Generation budgets task-specific. Qwen3.6-27B and embeddings did much of the evaluation. Distinct semantic responses are not yet distinct enjoyable mechanics. Registry: one backbone, largely automated judging, not a commercial test | not stated | 39, 558-561 |
| E05 A05 | 2026-07-29 | VERIFIED | Preregistered metaphor study. GPT-4o-2024-08-06 assistance conditions. Separate exploratory simulation with Claude Sonnet 4.6 and Qwen3.5-27b | 644 writers, 351 evaluators. Finding is directional: first AI ideas compressed collective diversity; refining human-originated seeds preserved it | Do not merge the old-model human experiment and the newer-model simulation into one causal claim. Registry: simulation not preregistered, metaphor domain, diversity is not quality | YES for the human experiment ("old-model") | 41, 564-567 |
| E06 A06 | 2026-07-02 / 2026-07-07 | VERIFIED | Aggregate vs personalised expert-history judges, gpt-5-mini-2025-08-07, rating product ideas | Agreement (Krippendorff alpha) on need validity 0.189 to 0.404; on competitive advantage -0.028 to -0.119 | Personalised histories did not improve every dimension. Not game-demand forecasts. Registry: no game-player validation; matching preference is not forecasting success | not stated | 66, 570-573 |
| E07 A07 | 2026-07-01 | VERIFIED | AGC-Bench, paired creative-instruction experiment, 18 models, five tasks | Length-adjusted within-model dz = 1.40; 99.4% validity among 2,700 generations | Larger cohort mixes model vintages and task metrics; domain rankings vary. Asking for creative alternatives is worth testing. Not a universal ranking or market prediction. Registry: different cohorts for two manipulations, scoring mixed | mixed vintages | 43, 576-579 |
| E08 A08 | 2026-05-27 | VERIFIED | ReDNA: candidate generation split from goal/failure-conditioned selection; ten authored scenarios; 56 predefined paths; GPT-5.4 and Claude Sonnet 4.6 | GPT-5.4 path discovery 27/56 to 38/56. Sonnet 4.6 30/56 to 41/56, while its action-originality score fell 2.764 to 2.616 | Better goal discovery and better novelty can diverge. Small task; action-property metrics rest on LLM judgment. Registry: small human-authored scenario set | not stated | 45, 582-585 |
| E09 A09 | 2026-03-12 | VERIFIED | Idea-Catalyst, Qwen3-14B, 400 scientific analogy instances | Top-1 novelty win rate 83.25 vs 68.00 (Guided Dual Retrieval); usefulness 65.75 vs 70.25 | Supports testing structured mechanism transfer, not random noun mixes. Originality and usefulness do not always rise together. Registry: LLM preference evaluation, retrospective data, no game evaluation | YES ("historical-model method") | 47, 588-591 |
| E10 A10 | 2026-02-23 | VERIFIED | Fitness-product ideas, GPT-4o-2024-11-20; default pool, ordinary-persona prompting, fitness-entrepreneur persona, human pool | Category combinations covered: default 88; ordinary persona 210; entrepreneur persona 164; human pool 206. 99 human or simulated participants per comparison, ten ideas each | Historical-model, domain-specific coverage evidence, not a current-model game-design ceiling. Registry: same model generates and categorises; one domain; portfolio coverage, not commercial quality | YES | 26, 594-597 |
| E11 A11 | 2025-11-12 | VERIFIED | LiteraryTaste: pairwise choices; fine-tuned ModernBERT-large predictor | 100 pairwise choices from each of 60 people. Personal-choice accuracy 75.8% with 90 examples vs 67.7% for collective-preference prediction | Older-model short-text result. Accuracy and sample count do not transfer to a prompting-only designer. Registry: fine-tuned encoder, text tastes not gameplay, sample count not an onboarding requirement | YES ("older-model") | 68, 600-603 |
| E12 A12 | first posted 2025-10-01, v 2026-07-15 | VERIFIED | Verbalized Sampling; attributes part of convergence to typicality bias in preference data; 2025 model cohort | Diversity gains 1.6 to 2.1 times direct prompting | Evaluates historical models even in the July 2026 version. Some settings lost quality. Candidate counts were experimental settings, not an optimum. Registry: probability verbalisation does not certify calibrated probabilities; no universal best candidate count; human study mostly single-annotator items | YES | 28, 606-609 |
| E13 A13 | ICLR 2026 (no day) | VERIFIED | Execution study of LLM-generated vs human research ideas (NLP domain) | In this extract: none. Outside the range, GP1:515 gives 43 expert researchers, over 100 hours each, larger post-execution score declines for AI ideas | Registry: old generator, NLP domain, human execution choices mediate outcomes, not a present-model ceiling. GP1:515: motivates real tests, not a claim of current-model incapability | YES ("older-model", GP1:515) | 3 (range only), 612-615; 515 |

How to reuse an intervention (GP1:49, OPINION):

| id | rule |
| --- | --- |
| U1 | Reproduce an intervention with the reported model configuration before adopting it |
| U2 | Publication in 2026 does not show a model is current on 21 October. The papers mostly omit exact execution dates |
| U3 | Hold the brief, model version, generation budget and evaluation format constant; compare against a competent baseline; keep the rejected ideas |
| U4 | Assess mechanism-family diversity, owner preference and prototype survival as three separate results |

## 5. Human methods and their transfer to an AI designer (GP1:51-63)

| id | method | evidence and limit | proposed use | failure to detect | tag of the evidence cell | IDs given |
| --- | --- | --- | --- | --- | --- | --- |
| M1 | Generate broadly, then cut | Practice at Nintendo and Double Fine; no universal best count | A configurable budget, then an independent selection | Many near-duplicates posing as breadth | EXPERIENCE | none in the row (D02, P20 in GP1:61) |
| M2 | Combine distant ideas | Task-specific scientific analogy studies; game transfer untested | Map an outside mechanism to a player action and its consequence | A list of unrelated theme nouns | VERIFIED | none in the row |
| M3 | Apply constraints | Specific game cases; no general effect size in the paper | Remove a default action or resource and trace the result | Constraints that remove the central fantasy | EXPERIENCE | none in the row |
| M4 | Ask "what if" or invert a rule | As a general method for current models | Reverse roles, information, rewards or failure, then model the consequences | Surprise with no playable causal chain | OPINION | none in the row |
| M5 | Borrow trends and real events | Trend observations can be sourced; inferring success from them is opinion | Borrow the human behaviour or tension, not unlicensed expression | Short-lived attention mistaken for durable play | VERIFIED (observations) / OPINION (success inference) | none in the row |
| M6 | Name clichés to avoid | Opinion unless tested locally | Temporarily ban familiar mechanisms to widen search | Incoherence rewarded just for being unusual | OPINION | none in the row |
| M7 | Separate generator and critic | Bounded 2026 path-discovery evidence | Keep the alternatives, then inspect validity and promise | A critic that rejects novelty only for being uncertain | VERIFIED | none in the row (A08 by context, see E08) |

Notes on the table (OPINION unless marked):

| id | note | tag | source IDs | GP1 |
| --- | --- | --- | --- | --- |
| N1 | Nintendo's Wonder process collected more than 2,000 sticky-note ideas. That is not 2,000 built prototypes. Double Fine's Amnesia Fortnight is a studio-specific pitch-and-prototype practice. Neither gives the right idea count for a small AI studio | EXPERIENCE | D02, P20 | 61 |
| N2 | Split feasibility in two: the interaction that defines the fantasy, and the surrounding production burden. A destructive-world concept may need convincing local cause and effect before a vast world. A mystery may need a working clue network before simulated planets | OPINION | none | 63 |
| N3 | The architect should offer cheaper faithful ways to build it and never quietly drop the interesting part. Mark the remaining risk and let the owner decide if it is worth testing | OPINION | none | 63 |

## 6. Learning the owner's taste without narrowing novelty (GP1:65-72)

| id | statement | tag | source IDs | number with scope | GP1 |
| --- | --- | --- | --- | --- | --- |
| T1 | Personalised expert histories did not help every dimension. See E06 | VERIFIED | A06 | alpha need validity 0.189 to 0.404; competitive advantage -0.028 to -0.119 (product-idea rating, gpt-5-mini-2025-08-07) | 66 |
| T2 | Examining actual pairwise choices works for short text with a fine-tuned predictor. See E11 | VERIFIED | A11 | 75.8% at 90 examples vs 67.7% (100 choices x 60 people) | 68 |
| T3 | Store the compared concepts, the decision, the reason, the context and any later reversal | OPINION | none | none | 70 |
| T4 | Separate rejecting a fantasy from rejecting its scope, its pitch quality or its technical risk | OPINION | none | none | 70 |
| T5 | Keep close-fit ideas, adjacent exploration and deliberate wildcards available, with no fixed proportions | OPINION | none | none | 70 |
| T6 | Ask about contrasting experiences instead of repeating the owner's favourite words | OPINION | none | none | 70 |
| T7 | An owner may prefer a game that current audience evidence does not support. Show the mismatch clearly; do not replace the owner's authority | OPINION | none | none | 70 |
| T8 | A proven loop with a new theme can be a strong concept when the theme changes the wanted role, the emotional meaning, the social context or the first-image appeal. The twist need not be a technically new mechanic | OPINION | none | none | 72 |
| T9 | Judge the resulting experience against the owner's intended audience, not by giving originality only to unfamiliar rules | OPINION | none | none | 72 |

## 7. Borrowing a loop without copying expression (GP1:74-77)

| id | item | tag | source IDs | GP1 |
| --- | --- | --- | --- | --- |
| B1 | The US Copyright Office separates a game's idea and method of play from its protectable expression. This is US guidance, not clearance for the world | VERIFIED | L01 | 75 |
| B2 | Roblox also prohibits unauthorised IP use under its own rules | VERIFIED | R18 | 75 |
| B3 | Having no copyright in an abstract rule does not license: characters, art, code, music, text, branding, or presentation confusingly similar to another's. Other rights can apply | VERIFIED (scope as in L01, R18) | L01, R18 | 75 |
| B4 | Method: describe the borrowed functional structure; name the new decision or consequence; create original expression; review any rights-sensitive resemblance before release | OPINION | none | 77 |
| B5 | Do not claim that a loop clone, a renamed franchise or a parody is automatically safe | OPINION | none | 77 |
| B6 | A licensed success is evidence about that licensed product. It is not permission for this studio to borrow that IP | OPINION | none | 77 |

May borrow: the idea and the method of play (the functional structure of the loop). Must change or must not take: characters, art, code, music, text, branding, any confusingly similar presentation.

## 8. The case roster: rules for reading it (GP1:79-80)

All OPINION unless noted. The paper lists 18 concepts, 15 here.

| id | rule |
| --- | --- |
| R1 | The roster is chosen on purpose. It shows possibilities. It shows neither hit rates nor causal laws |
| R2 | Sales, active users, awards and views are different outcomes. Do not add them together |
| R3 | Every first image, signature-moment reading and smallest version is an analytical proposal. None is a rebuilt original pitch |
| R4 | A smallest version names functional scope only. It gives no staffing, budget or validated content count |
| R5 | Timing, distribution, community, execution and updates can explain success as much as the concept does |
| R6 | Each case: the evidence lines are tagged VERIFIED or EXPERIENCE with source IDs; the fields "fantasy and promise", "curiosity and stakes", "first image", "shareable moment", "loop and twist", "smallest version", "transfer" are tagged OPINION (GP1:86 and the same line in cases 2-12) |

In the case tables, "evidence" rows carry the paper's tag and sources. The seven field rows are OPINION and have no source IDs.

### Case 1 Splatoon (GP1:82-93)

| row | content | tag | source IDs |
| --- | --- | --- | --- |
| evidence | Nintendo describes swapping ink-shooting rabbits for a squid/human split. That made ink movement and wall painting hang together | EXPERIENCE | C01, C02 |
| evidence | 4.95 million original Wii U units worldwide, life-to-date as of 2026-03-31, bundles and downloads included | VERIFIED | C03 |
| fantasy and promise | A stylish shape-shifting squid whose paint is weapon, territory and escape route | OPINION | - |
| curiosity and stakes | Can I turn this enemy-held surface into my own route before the match ends? | OPINION | - |
| first image | A humanoid splashes a wall, transforms and swims straight up it | OPINION | - |
| loop and twist | Team shooter / territory contest, but shots also build movement infrastructure and visible team progress | OPINION | - |
| shareable moment | A threatened player vanishes into their own paint, flanks, and reverses the territory result | OPINION | - |
| smallest version | Compact territory arena; opposing paint colours; a paint weapon; transform-and-swim; a clear territory finish | OPINION | - |
| transfer | Look for one material or verb that does several emotionally coherent jobs, instead of adding unrelated features | OPINION | - |

### Case 2 Portal (GP1:95-106)

| row | content | tag | source IDs |
| --- | --- | --- | --- |
| evidence | The creators report a rough first room in week one, playtesting at once, and dryness seen after 15-30 minutes that led to narrative work. Limited animation staff helped shape the disembodied antagonist | EXPERIENCE | C04 |
| evidence | Won Game of the Year, Innovation and Best Design at the 2008 GDCA | VERIFIED | C05 |
| fantasy and promise | Escape a hostile lab by making two distant places adjacent | OPINION | - |
| curiosity and stakes | What can this impossible tool do, and can I trust the voice that directs me? | OPINION | - |
| first image | A character sees themselves through a doorway they just made, then falls into one portal and flies out of another | OPINION | - |
| loop and twist | Spatial puzzle solving where player-placed topology replaces fixed routes | OPINION | - |
| shareable moment | An apparently impossible gap solved with a self-made spatial shortcut | OPINION | - |
| smallest version | Compact rooms with spectacular portal traversal, plus enough taunting voice to suggest an adversary | OPINION | - |
| transfer | Cut content breadth, not the impossible verb. Test comprehension separately from longer-term dramatic motivation | OPINION | - |

### Case 3 Minecraft (GP1:108-119)

| row | content | tag | source IDs |
| --- | --- | --- | --- |
| evidence | Official description joins exploration, creation and surviving the night | VERIFIED | C06 |
| evidence | Anniversary timeline records 300 million copies in 2023 | VERIFIED | C08 |
| evidence | Persson's 2011 postmortem: unexpected player interest kept Creative mode; he names timing and several explanations for success | EXPERIENCE | C07 |
| fantasy and promise | Carve a home and a personal history out of a world you can rearrange | OPINION | - |
| curiosity and stakes | What is over the ridge, under this block, or outside my unfinished shelter after dark? | OPINION | - |
| first image | A raw hillside becomes a lit refuge while night gathers around it | OPINION | - |
| loop and twist | Gather, craft, build, survive; the same editable terrain gives both resources and the expressive medium | OPINION | - |
| shareable moment | An extraordinary build, a disastrous breach, or an ingenious rescue made of ordinary blocks | OPINION | - |
| smallest version | A bounded landscape, a small block vocabulary, gathering/building and a meaningful environmental threat; or a separate creative test with no threat | OPINION | - |
| transfer | Protect player authorship. Watch for unexpected uses; the designer's preferred mode is not the only fantasy | OPINION | - |

### Case 4 Stardew Valley (GP1:121-132)

| row | content | tag | source IDs |
| --- | --- | --- | --- |
| evidence | Press kit frames an inherited farm and a damaged community as a new-life premise; four years of solo development; over 41 million copies across platforms as of December 2024. The paper adds: success does not imply a small production effort | VERIFIED | C09 |
| fantasy and promise | Leave alienating work and become someone whose daily care makes a place flourish | OPINION | - |
| curiosity and stakes | What can this neglected plot become, and who will I come to know? | OPINION | - |
| first image | The same farmhouse framed by weeds, then by a thriving garden arranged by the player | OPINION | - |
| loop and twist | Farm-management routines fused with community relationships, exploration and restoration | OPINION | - |
| shareable moment | A harvest, a relationship milestone, or a beautiful farm that shows the player's priorities | OPINION | - |
| smallest version | A plot and crop cycle, a home, a responsive neighbour, a visible communal repair goal | OPINION | - |
| transfer | Stakes need not mean danger. A clear before/after can make ordinary verbs aspirational. Removing every sign of belonging shrinks the fantasy, not only the scope | OPINION | - |

### Case 5 Among Us (GP1:134-145)

| row | content | tag | source IDs |
| --- | --- | --- | --- |
| evidence | Innersloth names a Mafia-like childhood game and The Thing as inspirations; a three-person team released in 2018, before the summer-2020 breakout | EXPERIENCE | C10 |
| evidence | Almost 500 million MAU in November 2020. This is monthly active users: not purchases, not simultaneous players | VERIFIED | C10 |
| fantasy and promise | Keep a spaceship alive while finding which friend is secretly sabotaging you, or lie well enough to destroy the crew | OPINION | - |
| curiosity and stakes | Who was really in that room, and will the group believe me before another player dies? | OPINION | - |
| first image | Cheerful crewmates doing jobs while one slips from a vent beside a body | OPINION | - |
| loop and twist | Social deduction, with physical movement, witnessed whereabouts, chores and sabotage creating the evidence | OPINION | - |
| shareable moment | A persuasive accusation, a disastrous innocent vote, or a betrayal by a trusted friend | OPINION | - |
| smallest version | A compact map, a hidden-traitor role, varied tasks, reporting, discussion and voting | OPINION | - |
| transfer | Design the situation that gives players something consequential to say. A chat channel alone does not | OPINION | - |

### Case 6 Vampire Survivors (GP1:147-158)

| row | content | tag | source IDs |
| --- | --- | --- | --- |
| evidence | Developer description combines minimal time-survival input, power choices and gold spent between attempts. BAFTA gave it Best Game and Game Design on 2023-03-30 | VERIFIED | C11, C12 |
| fantasy and promise | Become an absurdly powerful storm surrounded by a hostile crowd | OPINION | - |
| curiosity and stakes | What will these upgrades combine into, and can my build survive the next density spike? | OPINION | - |
| first image | A tiny vulnerable figure, set against the same figure filling the screen with attacks | OPINION | - |
| loop and twist | Survive, collect, choose upgrades, repeat; automatic attacks shift attention to positioning and build decisions | OPINION | - |
| shareable moment | A precarious survival turns into overwhelming screen-clearing power | OPINION | - |
| smallest version | A compact arena, escalation, contrasting attack choices and a visible combination payoff | OPINION | - |
| transfer | Simplify execution; keep agency and transformation. A huge particle count without consequential choices keeps the spectacle and loses the engine of the fantasy | OPINION | - |

### Case 7 Balatro (GP1:160-171)

| row | content | tag | source IDs |
| --- | --- | --- | --- |
| evidence | LocalThunk's retrospective traces an online "Big Cheat" game into a chips-times-multiplier score attack before Jokers existed. He first played Slay the Spire in May 2023. A friend's dozens of beta hours encouraged expansion | EXPERIENCE | C13 |
| evidence | Publisher announced over five million units on 2025-01-21 | VERIFIED | C14 |
| fantasy and promise | Turn an ordinary hand of cards into an outrageous scoring machine | OPINION | - |
| curiosity and stakes | Can I build a combination strong enough to beat the next requirement with limited hands? | OPINION | - |
| first image | Familiar playing cards, strange Jokers, and a modest score erupting into an implausible total | OPINION | - |
| loop and twist | Hand selection and score attack, with run-long deck changes and rule-altering synergies | OPINION | - |
| shareable moment | An unlikely hand sets off a chain of multipliers beyond expectation | OPINION | - |
| smallest version | A standard deck, escalating targets, a compact shop, enough interacting modifiers to find a surprising engine | OPINION | - |
| transfer | Borrow a familiar visual grammar, then make the consequences surprising. Do not infer that deliberate ignorance of competitors is a general best practice | OPINION | - |

### Case 8 Slay the Spire (GP1:173-184)

| row | content | tag | source IDs |
| --- | --- | --- | --- |
| evidence | Mega Crit describes a card-game and roguelike combination; its GDC 2019 slides report over 1.5 million copies sold | VERIFIED | C15, C16 |
| evidence | The slides argue every card should have a place and that data needs interpretation | EXPERIENCE | C16 |
| fantasy and promise | Improvise a unique combat engine that can climb a lethal tower | OPINION | - |
| curiosity and stakes | Can this awkward new card be the missing link, and is the dangerous route worth its reward? | OPINION | - |
| first image | A hand of cards facing a visibly threatening enemy, with a branching route ahead | OPINION | - |
| loop and twist | Fight and choose rewards, but the evolving deck changes the future decision space, not only the numbers | OPINION | - |
| shareable moment | A seemingly weak deck becomes a surprising synergy, or greed for an upgrade ruins a promising run | OPINION | - |
| smallest version | One character, a compact synergistic card pool, contrasting enemies, a route decision and a boss | OPINION | - |
| transfer | The acquisition decision should change how the player thinks in the next encounter. More collectible objects alone do not do that | OPINION | - |

### Case 9 Hades (GP1:186-197)

| row | content | tag | source IDs |
| --- | --- | --- | --- |
| evidence | Supergiant describes repeated escape attempts, changing builds and a continuing story. FAQ updated 2025-07-16 reports more than 50 publications naming it their 2020 Game of the Year | VERIFIED | C17 |
| evidence | The studio describes narrative, accessibility and Early Access as explicit aims | EXPERIENCE | C17 |
| fantasy and promise | A rebellious immortal fights out of the family business of death | OPINION | - |
| curiosity and stakes | Can I finally escape, and what will the household say about this attempt? | OPINION | - |
| first image | An intense escape attempt ends; the hero arrives home to a personally invested antagonist | OPINION | - |
| loop and twist | Action-roguelite runs become episodes in a persistent interpersonal story | OPINION | - |
| shareable moment | A surprising divine-power combination, or a character reply that acknowledges what just happened | OPINION | - |
| smallest version | One weapon, a short route, a boss and a home character whose replies change over several failures | OPINION | - |
| transfer | Attach a second, compatible reward to retrying. Do not just add unrelated dialogue between otherwise identical runs | OPINION | - |

### Case 10 Untitled Goose Game (GP1:199-210)

| row | content | tag | source IDs |
| --- | --- | --- | --- |
| evidence | Official premise centres a troublesome goose in a village. It won the 2020 GDCA Game of the Year | VERIFIED | C18, C20 |
| evidence | Developer interview: manual honking, eye contact and being shooed away are elements that made comic stealth fit the role | EXPERIENCE | C19 |
| fantasy and promise | Become a petty, unstoppable nuisance in a tidy world | OPINION | - |
| curiosity and stakes | What will stealing this ordinary object provoke, and can I get away with it? | OPINION | - |
| first image | A goose proudly carries a stolen key while its owner chases it | OPINION | - |
| loop and twist | Stealth-puzzle manipulation with no lethal punishment, framed as low-stakes animal transgression | OPINION | - |
| shareable moment | A timed honk, a theft, a stare and the human's reaction form one complete little joke | OPINION | - |
| smallest version | A goose, an expressive human, a tiny garden with manipulable objects, responsive chase and recovery | OPINION | - |
| transfer | A character fantasy can set verbs, feedback, tone and failure rules together. A funny mascot pasted on generic tasks cannot | OPINION | - |

### Case 11 Kerbal Space Program (GP1:212-223)

| row | content | tag | source IDs |
| --- | --- | --- | --- |
| evidence | Official description links spacecraft construction to aerodynamic and orbital physics. A 2023-02-24 release from the publisher's parent reports over five million worldwide units for the original game, not the sequel | VERIFIED | C21, C22 |
| fantasy and promise | Run a scrappy space program and get your own improbable machine to orbit | OPINION | - |
| curiosity and stakes | Will this design actually fly, and can I get the crew home? | OPINION | - |
| first image | An overbuilt homemade rocket wobbling on the pad, then the same craft against planetary curvature | OPINION | - |
| loop and twist | Construct, test, diagnose, rebuild; credible physical limits make creativity a hypothesis with visible consequences | OPINION | - |
| shareable moment | A spectacular but legible engineering failure, a miraculous recovery, or a first stable orbit | OPINION | - |
| smallest version | One planet and a launchpad, a small useful part set, and enough flight/orbit/reentry fidelity to test a real design choice | OPINION | - |
| transfer | Make the cause of failure readable and iteration attractive. A failure the player can explain and fix beats a random explosion | OPINION | - |

### Case 12 Outer Wilds (GP1:225-236)

| row | content | tag | source IDs |
| --- | --- | --- | --- |
| evidence | Mobius presents it as a time-loop solar-system mystery and records its 2020 BAFTA Best Game award | VERIFIED | C23, C25 |
| evidence | Development posts describe revising exploration around curiosity and testing the clue network through paper and text demakes | EXPERIENCE | C24 |
| fantasy and promise | A campfire astronaut-archaeologist finding out why a beautiful, dangerous world repeats | OPINION | - |
| curiosity and stakes | What happened here, and can I reach the answer before the environment changes? | OPINION | - |
| first image | A small handmade spacecraft above a fragile planet whose surface visibly changes | OPINION | - |
| loop and twist | Explore, observe, connect clues, revisit; understanding changes the available actions in a resetting world | OPINION | - |
| shareable moment | A discovery that makes a once-impossible place suddenly understandable. Do not spoil the answer in promotion | OPINION | - |
| smallest version | Linked locations, an environmental timer, and a revelation that re-reads an earlier obstacle. Test the mystery on paper before simulating a cosmos | OPINION | - |
| transfer | An unanswered question should point to an actionable investigation. Mystery with no direction can feel like aimless wandering | OPINION | - |

### Case 13 Grow a Garden (GP1:240-242)

| row | content | tag | source IDs |
| --- | --- | --- | --- |
| evidence | Roblox's 2025-06-24 infrastructure article reports 21.6 million simultaneous users. The paper says this shows reach, not a cause or a retention rate | VERIFIED | R19, R24 |
| evidence | Creator listing describes planting, harvesting, growth while offline, and showing finds to friends | VERIFIED | R24 |
| fantasy and promise | Cultivate a garden that becomes visibly yours | OPINION | - |
| curiosity and stakes | What will grow, and what unusual result can be shown? | OPINION | - |
| first image | A player beside a conspicuous harvest in a personal plot | OPINION | - |
| loop and twist | Plant, grow, harvest, improve, with change continuing between visits | OPINION | - |
| shareable moment | Show an unusual find to another player | OPINION | - |
| smallest version | A readable planting-to-harvest cycle, meaningful variation, a place to display it | OPINION | - |
| transfer | Keep the action-to-result promise clear. Do not assume waiting by itself creates value | OPINION | - |

### Case 14 Steal a Brainrot (GP1:244-246)

| row | content | tag | source IDs |
| --- | --- | --- | --- |
| evidence | Roblox reports more than 25 million concurrent users in September 2025. The paper: peak event concurrency is not ordinary-day retention | VERIFIED | R20, R25 |
| evidence | Creator listing describes buying, stealing, income generation and rebirth | VERIFIED | R25 |
| fantasy and promise | Acquire a conspicuous collection while risking it in social conflict | OPINION | - |
| curiosity and stakes | Can I take the prize and protect my own? | OPINION | - |
| first image | A player carries a contested object while its owner chases | OPINION | - |
| loop and twist | Collector progression gains a player-driven theft decision | OPINION | - |
| shareable moment | A successful heist or a reversal | OPINION | - |
| smallest version | Acquisition, visible ownership, theft, defence and recovery in a compact social space | OPINION | - |
| transfer | Make a contested object legible, but prototype newcomer protection and comeback chances together with the theft rule, not afterward | OPINION | - |

### Case 15 99 Nights in the Forest (GP1:248-250)

| row | content | tag | source IDs |
| --- | --- | --- | --- |
| evidence | Roblox's September 2026 podcast listing reports a three-month build and a story of reaching one million concurrent players. A creator account, not a production estimate for this studio | EXPERIENCE | R21 |
| evidence | The listing and the 2026 award description establish camp-building, gathering, rescue and survival | VERIFIED | R29, R30 |
| fantasy and promise | Keep a fragile camp alive with friends while something watches from the forest | OPINION | - |
| curiosity and stakes | What comes after dark, and can my preparation withstand it? | OPINION | - |
| first image | A lit camp surrounded by an unreadable dark treeline | OPINION | - |
| loop and twist | Prepare, survive, recover and extend the group's capability toward a named horizon | OPINION | - |
| shareable moment | A rescue during an escalating night | OPINION | - |
| smallest version | Camp preparation, a readable shared threat and recovery | OPINION | - |
| transfer | Keep the contrast between preparation and threat. Test cooperation without assuming open chat | OPINION | - |

## 9. Idea scoring rubric (GP1:265-275)

Scale (OPINION, GP1:266). It is ordinal. It states confidence and defects. Four ratings only:

| rating | meaning |
| --- | --- |
| FAIL | An observed contradiction or an unmet requirement |
| UNKNOWN | Evidence is missing |
| PLAUSIBLE | Coherent reasoning, but no relevant player observation |
| OBSERVED | A scoped observation supports it. This is not proof of general market success |

Rules for use (GP1:266): do not assign hidden weights. Do not combine policy compliance and creative appeal into one score. (Elsewhere the paper says: no fake-precision total, GP1:486 outside this extract.)

Criteria: 8 (count verified against GP1:267-275: Fantasy, Distinctiveness, Hook delivery, Agency and repeatability, Feasibility, Taste fit, Social and safety fit, Evidence quality).

| # | criterion | what must be stated | evidence that can improve the rating | reason to reject or investigate |
| --- | --- | --- | --- | --- |
| RB1 | Fantasy | The player role and the consequential verb | Players say, in their own words, what they want to do | The pitch is only a genre label or a list of references |
| RB2 | Distinctiveness | The mechanism, fantasy, relationship or audience meaning that the twist changes | Comparison with named alternatives; an independent concept review | No clear reason the intended audience would value the new fantasy or twist |
| RB3 | Hook delivery | The action the title and first image promise | A playable encounter produces that action with no scripted deception | Marketing shows an action the loop does not support |
| RB4 | Agency and repeatability | Which choices change outcomes, and what changes on repetition | Observed choices, retries, strategies and reasons to return | The intended agency, expression, anticipation, comfort or social value is absent or unsupported |
| RB5 | Feasibility | The cheapest build that keeps the decisive action | Probes of target-device and network risk; art production estimates | The small version removes the reason the concept is interesting |
| RB6 | Taste fit | The owner's relevant preferences and deliberate novelty | Explicit owner reasoning tied to this concept | An inferred preference is treated as a permanent veto |
| RB7 | Social and safety fit | How players affect each other and how abuse is handled | Tests with the intended party and stranger set-ups | Targeted harassment, exploitation or prohibited content is required; or agreed competition lacks intended counterplay and recovery |
| RB8 | Evidence quality | Source, date, sample, scope and the remaining unknowns | Independent player observations; reproducible results | Popularity, an AI score or a thumbnail preference is called proof of fun |

Rule table under the rubric (GP1:277-282):

| rule | number | tag | source and date |
| --- | --- | --- | --- |
| Separate measured model results from the proposed game workflow | Named model and task only | VERIFIED | A01-A13, 2025-2026 |
| Separate generation from selection and retest locally | GPT-5.4 paths 27/56 to 38/56 | VERIFIED | A08, 2026-05-27 |
| Treat famous ideation counts as scoped history | More than 2,000 ideas, not prototypes | EXPERIENCE | D02, 2023-10-17 |
| Analyse different concepts without claiming causal success | 18 cases in the paper (15 in this file) | OPINION | C01-C25 and the Roblox case sources |
| Do not invent an optimal funnel or a weighted total | Configurable N | OPINION | author synthesis 2026-10-21 (no source ID) |

## 10. Section 2: the hook and the promise (GP1:284-327)

### 10.1 Definitions and method

| id | statement | tag | source IDs | GP1 |
| --- | --- | --- | --- | --- |
| H1 | Riot's incubation account separates the wanted player outcome from a thesis about an audience or genre opportunity and the innovation meant to serve it. That makes a concept more testable than a genre adjective | EXPERIENCE | P01 | 285 |
| H2 | Write the fantasy as an enacted role: who the player becomes, what they do, what can change, why the outcome matters | OPINION | none | 287 |
| H3 | Write the dramatic promise separately: the surprising situation, conflict or consequence that makes trying the game appealing | OPINION | none | 287 |
| H4 | A theme supplies context. A hook supplies a reason to act | OPINION | none | 287 |
| H5 | A one-line fantasy need not list every system, but it must not promise a different game | OPINION | none | 287 |
| H6 | Design a signature moment as a causal sequence: visible setup, player decision, intelligible consequence, emotional payoff | OPINION | none | 289 |
| H7 | Give the animation, VFX, sound and camera leads the gameplay event and the information priority. Then let them find the expressive treatment | OPINION | none | 289 |
| H8 | A shareable moment can be a betrayal, a clever build, a reversal, a discovery or a comic reaction. It need not be costly spectacle. Keep the ordinary inputs and conditions that make it possible | OPINION | none | 289 |
| H9 | House House reports that trailer viewers inferred reactive music before that system existed, and the team built it later. Marketing can reveal an attractive promise and also create an expectation the build must meet. It is not proof that invented trailer behaviour is an acceptable test shortcut | EXPERIENCE | C19 | 291 |
| H10 | Published promises start from different anchors: House House names a mischievous role, Kerbal Space Program names building and flying a spacecraft, Mobius names exploring a repeating solar-system mystery. These are current public descriptions, not rebuilt internal launch pitches | VERIFIED | C18, C21, C23 | 293 |

### 10.2 Testing the title image and the playable promise

| step | what to do | tag | GP1 |
| --- | --- | --- | --- |
| TS1 | Test interpretation before preference. Show a title or concept image with no coaching. Ask what role, action and consequence the participant expects. Record misunderstandings and competing readings | OPINION | 296 |
| TS2 | A preference question can compare appeal. It cannot show understanding, eventual play or retention | OPINION | 296 |
| TS3 | Use comparable variants. Report audience, exposure method, actual sample, instructions and uncertainty. No universal viewing time or response threshold was set by this research | OPINION | 296 |
| TS4 | Then test promise delivery in a playable sequence: do players do the advertised action by themselves, notice its consequence, and find a reason to continue? | OPINION | 298 |
| TS5 | Record the actual time and path. Do not swap in a generic target for the game's intended pacing | OPINION | 298 |
| TS6 | Separate five causes, which need different fixes: weak hook, unclear controls, delayed delivery, absent payoff, shallow repetition | OPINION | 298 |
| TS7 | Read acquisition and post-entry behaviour together. High click rate plus strong first-play bounce fits a promise mismatch, but loading, device performance, audience targeting or a confusing opening can cause it too. Diagnose before rewriting the game | OPINION | 308 |
| TS8 | A thumbnail test that changes who is acquired is not a clean gameplay experiment. Do not claim a causal Roblox click-rate-to-retention effect size when none is supplied | OPINION | 308 |

### 10.3 Roblox discovery facts used by this section (all VERIFIED)

| id | fact (my words) | number with unit and scope | source IDs | GP1 |
| --- | --- | --- | --- | --- |
| RF1 | The 2026-06-15 announcement widens the Recommended For You evaluation window from seven days to 28 days. It splits the former qualified-play-through signal into more granular measures. Roblox says over-weighting short-term engagement had favoured exciting thumbnails without enough lasting value. No per-game causal lift and no public ranking weights are given | 7 days to 28 days (evaluation window) | R07 | 300 |
| RF2 | Current documentation names play-through rate, first-play bounce, play days and playtime as leading signals | none | R08, R09 | 302 |
| RF3 | These ranking signals use users organically acquired from Recommended For You. The FAQ leaves out engagement, retention and spend of ad-first cohorts, even for their later Home returns | none | R08, R09 | 302 |
| RF4 | Benchmarks do not directly decide recommendations | none | R08, R09 | 302 |
| RF5 | Thumbnail personalisation documentation reports an average +8.5% qualified play-through rate, with some games at +50%. It gives no sample size, baseline, confidence interval or date. The figures are relative changes, not percentage points, not a guarantee | +8.5% average; +50% for some games (relative qPTR change) | R10 | 304 |
| RF6 | Thumbnail personalisation needs at least two active thumbnails. It still defines qPTR in its thumbnail analytics, which does not undo June's ranking change. A video must represent actual gameplay | at least 2 active thumbnails | R10 | 304 |
| RF7 | Publishing guidance recommends accurate names and a first description sentence that explains the game. It sets no universal title length, no emoji requirement and no hit formula | none | R11 | 306 |

### 10.4 Hook pass or fail check (GP1:310-321)

Rule (OPINION): PASS only when the named evidence exists; otherwise FAIL with a reason. A missing test is marked FAIL FOR READINESS, which is not proof that the game itself is bad. 10 items.

| id | check item | tag |
| --- | --- | --- |
| HC01 | The title and first image show a concrete action or curiosity, with no need to explain the pitch | OPINION |
| HC02 | The one-line promise says what the player does and why the consequence matters | OPINION |
| HC03 | The signature moment can be reached through ordinary play, not only through a trailer camera or developer command | OPINION |
| HC04 | The opening playable sequence teaches the action needed to deliver the promise | OPINION |
| HC05 | The repeat loop changes a decision, a relationship, a challenge or an expression. It does not just repeat the advertisement | OPINION |
| HC06 | Title, thumbnail and prototype were tested on the same target audience, or the audience difference is reported | OPINION |
| HC07 | Acquisition, first-play bounce, qualified engagement and returning cohorts are evaluated separately | OPINION |
| HC08 | The minimum build still supports the fantasy, including its critical visual, audio or social dependency | OPINION |
| HC09 | The owner can name the intended tradeoff and the unresolved risk before approving production | OPINION |
| HC10 | Rights, content maturity and current platform-policy questions are resolved, or are explicitly blocking release | OPINION |

Rule table under the hook section (GP1:323-327):

| rule | number | tag | source and date |
| --- | --- | --- | --- |
| Separate interpretation, preference and actual play | No universal test cut-off | OPINION | author synthesis 2026-10-21 (no source ID) |
| Use current recommendation definitions | 28-day windows in the current announcement | VERIFIED | R07, 2026-06-15 |
| Report acquisition and downstream behaviour separately | Metric definitions are not universal targets | VERIFIED | R07-R11, current at 2026-10-21 |
| Show signature moments through ordinary gameplay | No validated moment quota | OPINION | C19, undated, accessed 2026-10-21 |

## 11. Source table (every ID cited above)

Registry page: GP1:535-982. Titles are the registry's, with its stripped punctuation shown as " - ". "Scope note" is the registry's `Scope:` line, paraphrased; "none" means the registry gives no scope line for that entry (all R-entries).

| id | title; author or issuer | date (registry) | registry tag | URL | scope note |
| --- | --- | --- | --- | --- | --- |
| A01 | Old Ideas - Novel Problems - The Instability of LLM Based Novelty Evaluation; Noy Sternlicht et al. | 2026-10-01 first posted; v 2026-10-14 | VERIFIED measured study | https://arxiv.org/html/2610.02022v2 | Low-novelty labels partly assumed; narrow research domain; no game-ideation outcome check |
| A02 | Evaluating LLM Creativity through Long Tail Performance; Yichen Wang et al. | 2026-10-09 | VERIFIED measured study | https://arxiv.org/html/2610.12998v1 | Intervention result is not a frontier-model estimate; quality and originality proxies incomplete |
| A03 | IdeaScientist - Orchestrating Agents for Grounded Scientific Ideation; Jiarui Liu et al. | 2026-10-02 first posted; v 2026-10-09 | VERIFIED measured study | https://arxiv.org/html/2610.04074v2 | Main judging by Qwen3.6-27B; proposals not executed; model-memory contamination not removed by the retrieval cutoff |
| A04 | Breaking Homogeneity - Diversifying Persona Sets for Creative LLM Outputs; Sang Bin Moon et al. | 2026-09-24 | VERIFIED measured study | https://arxiv.org/html/2609.30492v1 | One generation backbone; largely automated judging; not a commercial outcome test |
| A05 | Human diversity fuels collective creativity that large language models cannot simulate or sustain; Mengchen Dong, Hiromu Yakura | 2026-07-29 | VERIFIED measured study | https://arxiv.org/pdf/2607.26899 | Simulation not preregistered; metaphor domain; diversity is not quality |
| A06 | Aggregate vs Personalized Judges in Business Idea Evaluation - Evidence from Expert Disagreement; Wataru Hirota et al. | 2026-07-02 / 2026-07-07 | VERIFIED measured study | https://aclanthology.org/2026.acl-industry.61.pdf | Alignment sometimes worsens; no game-player validation; matching preference is not forecasting market success |
| A07 | AGC Bench - Measuring Artificial General Creativity; Roger Beaty et al. | 2026-07-01 | VERIFIED measured study | https://arxiv.org/html/2607.01152v1 | Different cohorts for two manipulations; mixed scoring; no game-market outcome check |
| A08 | Beyond One Path - Evaluating and Enhancing Divergent Thinking in Interactive LLM Agents; Jihyeong Park et al. | 2026-05-27 | VERIFIED measured study | https://arxiv.org/html/2605.28465v1 | Small human-authored scenario set; predefined success paths; LLM-judged action properties; originality can fall while goal discovery rises |
| A09 | Sparking Scientific Creativity via LLM Driven Interdisciplinary Inspiration; Priyanka Kargupta et al. | 2026-03-12 | VERIFIED measured study | https://arxiv.org/html/2603.12226v1 | Novelty gains are not uniform usefulness gains; LLM preference evaluation; retrospective data; no game evaluation |
| A10 | Examining and Addressing Barriers to Diversity in LLM Generated Ideas; Yuting Deng, Melanie Brucks, Olivier Toubia | 2026-02-23 | VERIFIED measured study | https://arxiv.org/html/2602.20408v1 | Same model generates and categorises; one domain; measures portfolio coverage, not commercial quality |
| A11 | LiteraryTaste - A Preference Dataset for Creative Writing Personalization; John Joon Young Chung et al. | 2025-11-12 | VERIFIED measured study | https://arxiv.org/html/2511.09310v1 | Fine-tuned encoder result, not prompting-only accuracy; text tastes are not gameplay preferences; sample count is not an onboarding requirement |
| A12 | Verbalized Sampling - How to Mitigate Mode Collapse and Unlock LLM Diversity; Jiayi Zhang et al. | 2025-10-01 first posted; v 2026-07-15 | VERIFIED measured study | https://arxiv.org/html/2510.01171v4 | Older-model evidence despite 2026 revision; quality drops in some conditions; probability verbalisation does not certify calibration; no universal best candidate count; human study mostly single-annotator items |
| A13 | The Ideation Execution Gap - Execution Outcomes of LLM Generated versus Human Research Ideas; Chenglei Si, Tatsunori Hashimoto, Diyi Yang | ICLR 2026 (no day) | VERIFIED measured study | https://arxiv.org/html/2506.20803v1 | Old generator; NLP domain; human execution choices mediate outcomes; not a present-model ceiling |
| C01 | Iwata Asks - Splatoon - 3 Got to be Squids; Nintendo | Undated; accessed 2026-10-21 | EXPERIENCE | https://www.nintendo.com/en-gb/Iwata-Asks/Iwata-Asks-Splatoon/Splatoon/3-Got-to-be-Squids/3-Got-to-be-Squids-1021369.html | Publication day not visible; interview is about the original Wii U game, not sequels |
| C02 | Iwata Asks - Splatoon - 4 Gaining Momentum; Nintendo | Undated; accessed 2026-10-21 | EXPERIENCE | https://www.nintendo.com/en-gb/Iwata-Asks/Iwata-Asks-Splatoon/Splatoon/4-Gaining-Momentum/4-Gaining-Momentum-1021371.html | Undated text; does not show the hook caused sales |
| C03 | Top Selling Title Sales Units - Wii U Software; Nintendo Investor Relations | 2026-03-31 | VERIFIED | https://www.nintendo.co.jp/ir/en/finance/software/wiiu.html | Date is the data as-of date, not a shown publication day; units are not unique users or revenue |
| C04 | Thinking With Portals - Creating Valve's New IP; Kim Swift / Portal creators (Game Developer reprint) | 2008-11-04 (orig. January 2008 magazine) | EXPERIENCE | https://www.gamedeveloper.com/design/thinking-with-portals-creating-valve-s-new-ip | HTML article read; magazine PDF not available; creator retrospective, not proof |
| C05 | 8th Annual Game Developers Choice Awards - 2008 Finalists and Winners; GDCA | 2008 | VERIFIED | https://gamechoiceawards.com/archive-gdca-2008/ | Award year 2008 honours games of 2007; not a sales metric |
| C06 | What is Minecraft - Discover the World of Minecraft; Mojang | Undated; accessed 2026-10-21 | VERIFIED | https://www.minecraft.net/en-us/about-minecraft | Current page, not the original 2009 pitch |
| C07 | Exclusive - Behind The Scenes Of Minecraft; Markus Persson excerpt, Game Developer | 2011-02-17 | EXPERIENCE | https://www.gamedeveloper.com/game-platforms/exclusive-behind-the-scenes-of-i-minecraft-i- | Only the creator-attributed excerpt used; his explanation is retrospective interpretation, not controlled analysis |
| C08 | Minecraft 15th Anniversary; Mojang | Undated; accessed 2026-10-21 | VERIFIED | https://www.minecraft.net/en-us/15th-anniversary | Page celebrates the 2024 anniversary; 300 million is placed in 2023, not 2024 sales |
| C09 | Stardew Valley - Press; ConcernedApe | Undated; accessed 2026-10-21 | VERIFIED | https://www.stardewvalley.net/press/ | Page has two release days (Feb 22 vs Feb 26, 2016): do not cite the release-day field. Sales are dated December 2024, not a 2026 total |
| C10 | Press Kit - Among Us; Innersloth | Undated; accessed 2026-10-21 | VERIFIED | https://www.innersloth.com/press-kit-among-us/ | Almost 500 million MAU is a studio-republished metric, not paying users, concurrent users or copies; do not mix original and updated product details |
| C11 | Vampire Survivors - Steam store description; poncle | Undated; accessed 2026-10-21 | VERIFIED | https://store.steampowered.com/app/1794680/Vampire_Survivors/ | Current promotional text; does not document initial intent, cost or commercial cause |
| C12 | BAFTA announces the winners of the 2023 BAFTA Games Awards; BAFTA | 2023-03-30 | VERIFIED | https://www.bafta.org/media-centre/press-releases/bafta-announces-the-winners-of-the-2023-bafta-games-awards/ | Awards are critical recognition, not sales or player counts |
| C13 | The Balatro Timeline; LocalThunk | 2025-03-06 | EXPERIENCE | https://localthunk.com/blog/balatro-timeline-3aarh | Author notes memory is imperfect; 2025 recollection of 2021-2024 work; demo or prototype counts must not be generalised |
| C14 | Balatro Deals a Full House of Success; Playstack | 2025-01-21 | VERIFIED | https://www.playstack.com/news/balatro-5-million-copies-sold/ | No platform breakdown or revenue; not a current lifetime figure |
| C15 | Slay the Spire press kit; Mega Crit | Undated; accessed 2026-10-21 | VERIFIED | https://www.megacrit.com/press-kits/slay-the-spire/ | Current feature counts not necessarily launch counts; 2017-11-15 is Early Access, not version 1.0 |
| C16 | Slay the Spire - Metrics Driven Design and Balance; Anthony Giovannetti, GDC 2019 | 2019 (year precision) | VERIFIED | https://media.gdcvault.com/gdc2019/presentations/Giovannetti_Anthony_SlayTheSpire.pdf | 22-page slides read; figures are presentation-era; no regional/platform split |
| C17 | Hades FAQ; Supergiant Games | 2018-12-07; updated 2025-07-16 | VERIFIED | https://www.supergiantgames.com/blog/hades-faq/ | Use 2025-07-16 as the update date; studio-reported accolades, not sales; narrative effect not isolated |
| C18 | Untitled Goose Game official website; House House / Panic | Undated; accessed 2026-10-21 | VERIFIED | https://untitled.goose.game/ | Current site, not proof of the original pitch wording or date |
| C19 | Panic Podcast Episode 1 - Untitled Goose Game - transcript; Panic with House House | Undated (page shows an invalid date); accessed 2026-10-21 | EXPERIENCE | https://podcast.panic.com/episodes/s01e01/transcript/ | Transcript read, audio not; timing and influence are participant recollections |
| C20 | 20th Annual Game Developers Choice Awards - 2020 Finalists and Winners; GDCA | 2020 | VERIFIED | https://gamechoiceawards.com/archive-gdca-2020/ | Site navigation mentions a 2027 event: use the explicit 2020 archive heading |
| C21 | Kerbal Space Program official website | Undated; accessed 2026-10-21 | VERIFIED | https://www.kerbalspaceprogram.com/?lang=en | Site also mentions the sequel; the case is about the original game; site access is not evidence of healthy support |
| C22 | Kerbal Space Program 2 Launches in Early Access Today; Private Division / Take-Two Interactive | 2023-02-24 | VERIFIED | https://ir.take2games.com/node/29461/pdf | The sales figure is for the original game, not KSP 2; sequel roadmap promises not used as facts |
| C23 | Outer Wilds official game page; Mobius Digital | Undated; accessed 2026-10-21 | VERIFIED | https://www.mobiusdigitalgames.com/outer-wilds.html | Current page with a retrospective award statement; not the original pitch; no sales metric |
| C24 | Demaking Outer Wilds; Alex Beachum / Mobius Digital | 2015-07-30 | EXPERIENCE | https://www.mobiusdigitalgames.com/news/demaking-outer-wilds | Narrative-test evidence only; no claim the suggested minimum teaching version shipped |
| C25 | The Intentionality of Wandering; Mobius Digital interview with Alex Beachum | 2016-08-18 | EXPERIENCE | https://www.mobiusdigitalgames.com/news/the-intentionality-of-wandering | Design rationale is documented; commercial effect is not |
| D02 | Ask the Developer Vol 11 - Super Mario Bros Wonder - Chapter 1; Nintendo | 2023-10-17 | EXPERIENCE; VERIFIED reported count | https://www.nintendo.com/en-gb/News/2023/October/Ask-the-Developer-Vol-11-Super-Mario-Bros-Wonder-Chapter-1-2460393.html | Nintendo-hosted recollection; counts as reported, not audited |
| L01 | Games; US Copyright Office | Undated; accessed 2026-10-21 | VERIFIED official guidance | https://www.copyright.gov/register/tx-games.html | US guidance only; not global clearance, trademark advice or Roblox permission |
| P01 | Incubation - Exploration With a Plan; John-David Perry / Riot Games | 2020-06-18 | EXPERIENCE | https://www.riotgames.com/en/r-and-d-office/incubation-exploration-with-a-plan | Full article read; reported process, not causal comparison |
| P02 | Prototype - Building a Game's Substance; Tom Cadwell / Riot Games | 2020-06-18 | EXPERIENCE | https://www.riotgames.com/en/r-and-d-office/prototype-building-a-games-substance | Any claim of "proof" is the author's wording, not statistical validation |
| P03 | Engineering in Riot R&D; Baris Yaman / Riot Games | 2021-02-23 | EXPERIENCE | https://www.riotgames.com/en/r-and-d-office/engineering-in-riot-r-d | The fresh code environment is Riot's practice, not universal advice |
| P04 | Collaborative Creative in R&D; Andy Lang / Riot Games | 2021-05-21 | EXPERIENCE | https://www.riotgames.com/en/r-and-d-office/collaborative-creative-in-r-d | Do not turn its typical staffing into a universal minimum |
| P06 | Valve's Design Process for Creating Half-Life 2; David Speyrer, Brian Jacobson / Valve | 2006 (GDC listing); 2007 (slide copyright) | VERIFIED artifact content | https://cdn.akamai.steamstatic.com/apps/valve/2006/GDC2006_HL2DesignProcess.pdf | 28-page deck read; reports studio experience, not a controlled study |
| P12 | Ready to Make History - A Look into Venture's Development; Daryl Tan, Miranda Moyer / Blizzard | 2024-04-17 | EXPERIENCE | https://news.blizzard.com/en-us/article/24072104/ready-to-make-history-a-look-into-venture-s-development | Official News mirror read (metadata date 2024-04-17T18:00:00Z); original URL returned 403 |
| P16 | Into the Breach Design Postmortem; Matthew Davis / Subset Games | 2019 (GDC) | VERIFIED artifact content | https://media.gdcvault.com/gdc2019/presentations/Into%20the%20Breach%20Postmortem%20Final.pdf | 49-page deck read; constraint choices are project-specific; efficacy is reported experience |
| P19 | Making Your Game Easy to Tune - Programming and Tech; Masahiro Sakurai | 2022-12-06 | OPINION | https://www.youtube.com/watch?v=nGaajB8m5Q0 | Only indexed title, author, date and description checked; full video/transcript not reviewed; no claims about spreadsheet or implementation internals |
| P20 | Amnesia Fortnight; Double Fine Productions | n.d. (retrieved 2026-10-21) | EXPERIENCE | https://www.doublefine.com/games/amnesia-fortnight | Official hub read; recent site entries do not change what older events show |
| R07 | Optimizing Discovery - How Great Games Reach Millions of Players on Roblox; Roblox | 2026-06-15 | VERIFIED | https://about.roblox.com/newsroom/2026/06/optimizing-discovery-great-games-reach-millions-players-roblox | none |
| R08 | Discovery - current ranking signals and content quality restrictions; Roblox | Undated live docs; accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/discovery | none |
| R09 | Discovery FAQ; Roblox | Undated live docs; accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/discovery-faq | none |
| R10 | Thumbnails - personalization, testing result and authentic video; Roblox | Undated live docs; accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/production/publishing/thumbnails | none |
| R11 | Publish games and places - metadata best practices; Roblox | Undated live docs; accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/production/publishing/publish-games-and-places | none |
| R18 | Community Standards - repetitive content and intellectual property; Roblox | Current standards; accessed 2026-10-21 | VERIFIED | https://about.roblox.com/community-standards | none |
| R19 | The Infrastructure Supporting Record Breaking Experiences; Roblox | 2025-06-24 | VERIFIED | https://about.roblox.com/newsroom/2025/06/roblox-infrastructure-supporting-record-breaking-games | none |
| R20 | The 2025 Roblox Replay - Decoded Through Search and Style; Roblox | 2025-12-16 | VERIFIED | https://about.roblox.com/newsroom/2025/12/roblox-replay-decoded-search-style | none |
| R21 | Made on Roblox episode 1 - creators of 99 Nights in the Forest; Roblox | Listing accessed 2026-10-21; episode announced for September 2026 | EXPERIENCE | https://about.roblox.com/podcast | none |
| R24 | Grow a Garden - official creator game listing; Roblox | Live listing accessed 2026-10-21 | VERIFIED | https://www.roblox.com/games/126884695634066/Grow-a-Garden | none |
| R25 | Steal a Brainrot - official creator game listing; Roblox | Live listing accessed 2026-10-21 | VERIFIED | https://www.roblox.com/games/109983668079237/Steal-a-Brainrot | none |
| R29 | 99 Nights in the Forest - official creator game listing; Roblox | Live listing accessed 2026-10-21 | VERIFIED | https://www.roblox.com/games/79546208627805/99-Nights-in-the-Forest | none |
| R30 | 2026 Roblox Innovation Awards; Roblox | 2026-09-12 | VERIFIED | https://about.roblox.com/newsroom/2026/09/2026-roblox-innovation-awards | none |
| U01 | User supplied research brief; studio owner | Provided 2026-10-21 | OPINION (studio operating instruction) | the two research prompts supplied by the owner (no URL) | The prompts set the requested scope, the final three pitches and the owner's decision rights |

## 12. Claims to fact-check

Every number and Roblox fact in this extract. Fact-checking is a separate ticket (J003); nothing here was checked on the web. "GP1" = paper line.

| # | claim (as the paper states it) | GP1 | source IDs |
| --- | --- | --- | --- |
| F01 | 88 category combinations (default pool), 210 (ordinary persona), 164 (entrepreneur persona), 206 (human pool); GPT-4o-2024-11-20; fitness products | 26 | A10 |
| F02 | 99 human or simulated participants per comparison, ten ideas each | 26 | A10 |
| F03 | Verbalized Sampling July 2026 version; diversity gains 1.6-2.1 times direct prompting | 28 | A12 |
| F04 | 52.6 percentage-point swing in GPT-5.4 pairwise accuracy; judges listed (GPT-5.1/5.2/5.4; Claude Sonnet 4.5/Opus 4.5/4.6); October 2026 | 33 | A01 |
| F05 | 237 prompts; four named small models; 1.5x temperature gives +10.7% novelty and -15.4% quality; 9 October 2026 | 35 | A02 |
| F06 | 277 held-out problems; Claude-4.8-Opus 77.7 vs 68.7; GPT-5.4 71.9 vs 69.5; gaps 9.0 and 2.4; 50-paper human comparison; version 9 October 2026 | 37 | A03 |
| F07 | Gemma-4-31B-it: diversity +78.8%, originality +26.1%, holistic creativity +13.9%, validity 98.5%; 24 September 2026 | 39 | A04 |
| F08 | 644 writers, 351 evaluators; GPT-4o-2024-08-06; simulation with Claude Sonnet 4.6, Qwen3.5-27b; 29 July 2026 | 41 | A05 |
| F09 | 18 models, five tasks, dz=1.40, 99.4% validity, 2,700 generations; 1 July 2026 | 43 | A07 |
| F10 | Ten authored scenarios, 56 paths; GPT-5.4 27/56 to 38/56; Sonnet 4.6 30/56 to 41/56; originality 2.764 to 2.616; 27 May 2026 | 45, 279 | A08 |
| F11 | Qwen3-14B; 400 instances; win rate 83.25 vs 68.00; usefulness 65.75 vs 70.25; 12 March 2026 | 47 | A09 |
| F12 | A06: gpt-5-mini-2025-08-07; alpha 0.189 to 0.404 (need validity); -0.028 to -0.119 (competitive advantage) | 66 | A06 |
| F13 | A11: 100 pairwise choices x 60 people; ModernBERT-large; 75.8% at 90 examples vs 67.7% | 68 | A11 |
| F14 | A13: ICLR 2026; 43 expert researchers, over 100 hours each (GP1:515, outside the range) | 515, 612 | A13 |
| F15 | Nintendo Wonder: more than 2,000 sticky-note ideas; D02 dated 2023-10-17 | 61, 280 | D02, P20 |
| F16 | Splatoon: 4.95 million original Wii U units life-to-date at 2026-03-31, with bundles and downloads | 84 | C03 |
| F17 | Portal: rough first room in week one; dryness after 15-30 minutes; GOTY, Innovation, Best Design at 2008 GDCA | 97 | C04, C05 |
| F18 | Minecraft: 300 million copies in 2023; Persson postmortem 2011 | 110 | C07, C08 |
| F19 | Stardew: four years solo; over 41 million copies as of December 2024 | 123 | C09 |
| F20 | Among Us: released 2018 by a three-person team; summer-2020 breakout; almost 500 million MAU, November 2020 | 136 | C10 |
| F21 | Vampire Survivors: BAFTA Best Game and Game Design on 2023-03-30 | 149 | C11, C12 |
| F22 | Balatro: first played Slay the Spire May 2023; over five million units announced 2025-01-21 | 162 | C13, C14 |
| F23 | Slay the Spire: over 1.5 million copies in GDC 2019 slides | 175 | C15, C16 |
| F24 | Hades: FAQ updated 2025-07-16; more than 50 publications named it 2020 GOTY | 188 | C17 |
| F25 | Untitled Goose Game: 2020 GDCA Game of the Year | 201 | C18, C20 |
| F26 | Kerbal Space Program: over five million worldwide units (original game), release dated 2023-02-24 | 214 | C21, C22 |
| F27 | Outer Wilds: 2020 BAFTA Best Game | 227 | C23, C25 |
| F28 | Grow a Garden: 21.6 million simultaneous users, article dated 2025-06-24 | 241 | R19, R24 |
| F29 | Steal a Brainrot: more than 25 million concurrent users in September 2025 | 245 | R20, R25 |
| F30 | 99 Nights in the Forest: September 2026 listing; three-month build; one million concurrent players; 2026 award | 249 | R21, R29, R30 |
| F31 | Recommended For You evaluation window widened from seven to 28 days on 2026-06-15; qualified play-through signal split into granular measures | 300, 325 | R07 |
| F32 | Leading signals: play-through rate, first-play bounce, play days, playtime; organically acquired users only; ad-first cohorts excluded; benchmarks do not directly decide recommendations | 302 | R08, R09 |
| F33 | Thumbnail personalisation: average +8.5% qPTR, some games +50%; at least two active thumbnails; video must show real gameplay | 304 | R10 |
| F34 | Publishing guidance: accurate names; first description sentence explains the game | 306 | R11 |
| F35 | US Copyright Office separates game idea and method of play from protectable expression; Roblox prohibits unauthorised IP use | 75 | L01, R18 |
| F36 | Roster size: 18 cases in the paper (15 here); rubric: 8 criteria (counted in GP1:267-275); hook check: 10 items (counted in GP1:312-321) | 79, 281, 267-275, 312-321 | none (counts of paper content) |

## 13. Contradictions and weak spots

Observations only; nothing was changed in the notes above to fix them.

| id | place | observation |
| --- | --- | --- |
| W01 | S02, S09, S10 tags | Tags describe the evidence type, but these three are instructions. S02 is a scoping rule tagged VERIFIED; S09 and S10 are rules tagged EXPERIENCE |
| W02 | S03, S05 vs sources | S03 cites A04 and A10, which do not test game mechanics (the paper itself says distinct meanings are not yet distinct enjoyable mechanics, GP1:39). S05 cites A01 (distrust of novelty scores) and A08 (path discovery); neither tests keeping uncertain concepts alive |
| W03 | S07, S11 vs the case roster | Both cite C01-C25, which are sources for cases 1-12. Cases 13-15 cite R-IDs. The paper also says the roster shows possibilities, not causal laws (GP1:80) |
| W04 | S04 and E08 | S04 is tagged VERIFIED but rests on one small task (ten scenarios, 56 paths) with LLM-judged properties. The same study records falling originality for Sonnet 4.6 |
| W05 | A13 | The summary cites A01-A13 (GP1:3), but A13 has no description or number in GP1:1-328. Its numbers appear only at GP1:515 (outside the range) and in the registry |
| W06 | "Historical model" labels | The paper tags some results as historical/older/old (A02, A05 human part, A09, A10, A11, A12, A13) but not A01, A03, A04, A06, A07, A08. It never says which models are current ("2026 publication does not make a model current", GP1:49). A06 uses a 2025-dated model name |
| W07 | A10 numbers | "Category combinations", "default pool" and "99 human or simulated participants per comparison" are not defined. The paper gives four counts and does not say which comparison matters |
| W08 | A09 numbers | Win rates and usefulness scores are given with no unit (percent is not stated). A03 scores give no scale. A12's "1.6-2.1 times" names no metric. A11's "90 examples" is not tied to the 100 choices per person |
| W09 | A03 | Compares to an "SDK" baseline that the paper does not describe. The backbone name "Claude-4.8-Opus" is as written in the paper |
| W10 | A05 | Text calls the study preregistered; the registry says the simulation was not preregistered. Both can be true, but the combined sentence is easy to misread |
| W11 | A01, A02, A04, A07, A12 | No baseline values for A01's 52.6-point swing, no quality number for A12's quality loss, A07 gives dz=1.40 with no scale reference. Percentages in A02/A04 are relative proxy-metric changes |
| W12 | Human methods table | Rows carry no source IDs. The tag cells (EXPERIENCE/VERIFIED/OPINION) are given, but which paper supports M2 and M7 is only implicit (A09 and A08 by context). D02 and P20 appear only in the note below the table |
| W13 | Rule table, "Treat famous ideation counts as scoped history" | Row says "More than 2,000 ideas"; the text says "sticky-note ideas" (GP1:61). D02's registry tag is "EXPERIENCE; VERIFIED reported count" while the row is tagged EXPERIENCE only. The registry excerpt for D02 holds no number |
| W14 | Case tags vs registry tags | C10 is VERIFIED in the registry, but the Among Us team size and release year are tagged EXPERIENCE (GP1:136). C16 is VERIFIED in the registry, but its argument is tagged EXPERIENCE (GP1:175). C25 is EXPERIENCE in the registry but is cited inside a VERIFIED sentence for Outer Wilds (GP1:227) |
| W15 | Among Us | "November 2020" for the MAU figure is not in the C10 registry entry (undated press kit). "Summer-2020 breakout" is a date claim with no registry number |
| W16 | Outer Wilds | The 2020 BAFTA is sourced to C23 (a "retrospective award statement") and C25 (a 2016 interview, which cannot record a 2020 award) |
| W17 | Goose Game, Portal | The registry excerpts for C20 and C05 do not show the awards. The paper relies on the archive headings |
| W18 | Case 13 | R19 (registry excerpt: "21.6 million users playing simultaneously") is not shown in the registry to name Grow a Garden. The attribution rests on the paper's text |
| W19 | Case 14 | The paper says "September 2025"; the registry date of R20 is 2025-12-16 and its excerpt carries no month. The paper's phrase "peak event concurrency" is not explained |
| W20 | Case 15 | The "three-month build" and "one million concurrent" come from a podcast listing announced for September 2026 (EXPERIENCE). The registry date is the access date. R30's excerpt names a category ("Best Survival Game") rather than the game |
| W21 | RF4 | Paper: benchmarks "do not directly determine" recommendations. The registry excerpt for R09 says benchmarks "do not impact" the algorithm. The paper's wording is softer |
| W22 | RF5 and RF6 vs RF1 | R10 reports +8.5% qPTR and still defines qPTR, while R07 splits that signal. The paper notes the tension and says the June change stands. No sample, baseline or interval for +8.5% or +50% |
| W23 | Section 2 numbers | RF2 lists four leading signals; RF1 says qPTR was split into granular measures. The paper does not map one to the other |
| W24 | Rubric | Called ordinal, but no order is defined between FAIL and UNKNOWN. No pass line, no roll-up rule, and OBSERVED has no minimum sample or scope. Criterion RB7 includes prohibited content, while the same paragraph says not to combine policy compliance and creative appeal into one score. The rubric has no criterion for trend evidence or for "proven loop" evidence, although T8 treats a proven loop with a new theme as a strong concept |
| W25 | Hook rule table | "No validated moment quota" is tied to C19, which is a recollection in a transcript with an invalid page date. Last row's date is "undated, accessed 2026-10-21", an access date used as a source date |
| W26 | Registry note vs scope notes | The registry note says every URL was inspected or verified (GP1:537), but scope notes say P19's full video was not reviewed, C19's audio was not watched, and the C04 magazine PDF was unavailable |
| W27 | Dates | Registry access dates and the research cutoff are 2026-10-21. These notes are dated 2026-10-20 by order of the ticket |
| W28 | Rule table "Do not invent an optimal funnel" | Uses "Configurable N", but N is defined only in section 7 (GP1:481-488), outside this extract |
