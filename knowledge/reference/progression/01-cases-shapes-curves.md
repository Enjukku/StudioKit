---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: "J011-T01, Progression_Designer_Research_2026.txt lines 1-230"
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-21

# Progression paper part 1: rules, benefits, 12 cases, shapes and timeline, curve library (lines 1-230)

Paraphrased notes. The paper (PP) stays outside git. Every row cites `PP:<line>`. Nothing here is fact-checked: claims are the paper's, listed in section 8 for the fact-check pass. The paper's research cut-off is 2026-10-21 (PP:5). The paper ran no player study and played or instrumented no full game (PP:160). Case numbers are the paper's (Case 1-12); source ids are the paper's (C01-C11); they do not match one to one (index in 4.0).

## 0. How to read

| Key | Meaning |
| --- | --- |
| PP:n | line n of `Progression_Designer_Research_2026.txt`. One paragraph = one line. Source register = PP:728-1310. PP:335-381 (outside range) is used only as a lookup for source limits and is marked "lookup". |
| Tag | VERIFIED (the source publishes the stated rule or number, or a study measures the stated association within its population; not independently reproduced, not causal, not proof of transfer to Roblox: PP:15). EXPERIENCE (a studio or designer's account of intent, practice or interpretation). OPINION (the paper's own proposal, synthesis, model choice or predicted feeling; source id O00, dated 2026-10-21, "not an external empirical source": PP:730). Tags are the paper's, not mine. In the curve section the paper uses VERIFIED for its own derived arithmetic (PP:208, 210); see Z04. |
| Src | paper source id, resolved in section 9 with its date. "undated, accessed D" = no publication date; access is not publication (PP:19). |
| Row IDs | IN preamble, R rule, B benefit paragraph, K case row (K5.V = Case 5 VERIFIED, .E EXPERIENCE, .O OPINION), Q design question, VC vocabulary, S shape paragraph, FT timeline checkpoint, PL plateau, ST shapes rule row, CD curve preamble or derivation, CV curve, CT curve rule row, HC hand check, CL claim, X limit stated by the paper, Z possible issue. |
| (extractor) | Anything I added: a standard definition, a hand calculation, a cross-reference. Not paper text. |
| Formulas | Plain text. `*` multiply, `^` power, `sqrt()` square root, `log_r(x)` log base r, `sum`, `prod`. Variables are defined in the row or in 6.0. |

Coverage map

| Paper part | Where here |
| --- | --- |
| Title, scope, evidence key, derived-value policy PP:1-19 | section 1 |
| Fifteen rules PP:21-51 | section 2 |
| 1 What makes progression worth pursuing PP:53-63 | section 3 |
| Twelve cases, contrasts, design-question table, unknowns, rule table PP:65-166 | section 4 |
| 2 Shapes and player timelines, vocabulary, timeline template, plateau PP:168-204 | section 5 |
| 3 Curve library and per-level vs cumulative PP:206-228 | section 6 |

## 1. Paper preamble (PP:1-19)

| ID | PP | Content (paraphrase) | Tag | Src |
| --- | --- | --- | --- | --- |
| IN1 | 1, 3, 5 | Title "Progression Design for AI Agents in a Roblox Studio"; subtitle: evidence-grounded mathematics and practical design decisions; research cut-off 21 October 2026. | OPINION (framing) | O00, 2026-10-21 |
| IN2 | 7 | Purpose: train a progression designer to turn the game designer's intended player experience into inspectable mathematical models, playable progression and versioned engineering data. The studio owner stays creative director and approves experience, tradeoffs and release. The agent recommends and verifies; it does not read creative approval into a successful calculation. | OPINION | O00 |
| IN3 | 9 | Main conclusion: progression is not one growth curve. It is the interaction of changing player capabilities, costs, rewards, available choices and the time to reach a meaningful state. A smooth curve can still hold a discrete combat breakpoint or an unappealing action repeated too long. Keep three things separate: the numerical model, the player-path assumptions, the intended feeling. The model shows what follows under its assumptions; a source or playtest must show how people respond. | OPINION | O00 |
| IN4 | 11 | Scope: industry progression design applied to a studio that ships Roblox games. Industry sources give system examples and design reasoning. Roblox sources are used only for platform analytics, monetization and player-policy facts, not as the standard of progression craft. Historical game numbers are attributed to their original versions or teaching examples, not presented as current live values. | OPINION | O00 |
| IN5 | 15 | VERIFIED = the source publishes the rule or number, or a study measures the association or effect within its described population and method. It does not mean a studio number was independently reproduced, that an observational association is causal, or that a result transfers to every Roblox genre. EXPERIENCE = a studio or designer's account of intent, practice, experience or interpretation. OPINION = this paper's procedure, synthesis, model choice or unvalidated prediction of feeling. Claims with different evidence are kept apart, not promoted. | OPINION (definitions) | O00 |
| IN6 | 17 | Exact derived values are calculations, not newly observed game facts, and keep the inputs and assumptions that make them valid. The two worked examples use published inputs. No earning rate is invented to make a calendar timeline. When a source does not publish seconds per action or XP per second, the timeline stays symbolic and names the missing measurement. Fractions and powers are kept, not silently rounded. Formula coefficients that are variables are not suggested balance constants. (The two worked examples are outside this range.) | OPINION | O00 |
| IN7 | 19 | Source ids resolve to a dated bibliography. Each source has one short key quotation; the body paraphrases. O00 = the paper's own recommendations, dated 2026-10-21, not an external empirical source. Sources without a reliable publication date are marked undated with an access date, not given an invented year. | OPINION | O00 |

## 2. The fifteen rules (PP:21-51)

| ID | PP | Tag | Rule (paraphrase) | Src, date |
| --- | --- | --- | --- | --- |
| R01 | 23 | OPINION | Start from the experience the owner approved, then choose the mathematics that implements it. | O00, 2026-10-21 |
| R02 | 25 | VERIFIED | A published rule is evidence of that rule in its stated version only. It is not proof the rule was enjoyed or that it is balanced today. | C03, October 2024; C08, 2024-01-05 |
| R03 | 27 | OPINION | Specify what becomes possible after a milestone, not only which stored number rises. | O00, 2026-10-21 |
| R04 | 29 | OPINION | Keep the cost curve separate from the earning process before predicting time to a goal. | O00, 2026-10-21 |
| R05 | 31 | OPINION | Use exact values, units and index origins. Keep missing earning rates symbolic. | O00, 2026-10-21 |
| R06 | 33 | EXPERIENCE | An optional endless resource sink and an introductory reward track solve different design problems. | C02, 2016-10-21; C10, 2025-08-22 |
| R07 | 35 | OPINION | Compare upgrade effects against discrete outcomes and against reference content that did not change. | O00, 2026-10-21 |
| R08 | 37 | OPINION | Define what a reset loses, what it keeps and what the next run looks like before choosing a prestige exponent. | O00, 2026-10-21 |
| R09 | 39 | EXPERIENCE | Reward spacing can need correction even when the system pays a large total. | C05, 2020-12-07 |
| R10 | 41 | VERIFIED | Reward research does not support a blanket claim that all extrinsic rewards always help or always harm motivation. | H02, 1999 (1999-11); H03, 2001 (spring) |
| R11 | 43 | OPINION | Track currency created, destroyed and transferred as separate flows. Do not infer inflation from one wallet total. | O00, 2026-10-21 |
| R12 | 45 | OPINION | Analyze player paths and cohorts. Do not turn the efficient simulated path into a population forecast. | O00, 2026-10-21 |
| R13 | 47 | OPINION | Export engineering data from the reviewed model, with an immutable version and provenance. | O00, 2026-10-21 |
| R14 | 49 | OPINION | Treat arithmetic verification, observed play and policy compliance as three separate gates. | O00, 2026-10-21 |
| R15 | 51 | OPINION | Give the owner consequences and uncertainties. An agent's recommendation never becomes automatic creative approval. | O00, 2026-10-21 |

Tag count (extractor): 11 OPINION, 2 VERIFIED (R02, R10), 2 EXPERIENCE (R06, R09). R10's two sources are described in the paper (outside this range, lookup PP:343-351) as competing meta-analyses; see X18.

## 3. What makes progression worth pursuing (PP:53-63)

All five paragraphs are OPINION. The cited H and W ids are the paper's basis, not proof (limits of the H sources in section 9).

| ID | PP | Tag | Content (paraphrase) | Src, date |
| --- | --- | --- | --- | --- |
| B1 | 55 | OPINION (synthesis, 21 October 2026) | A progression event should say what changes for the player, not merely the stored number. Six possible benefits: capability, choice, understanding, expressive ownership, access, recognizable accomplishment. A bigger damage number can matter if a familiar enemy now dies in fewer attacks; it is only numerical if enemy scaling cancels it before the player can feel a difference. Treat that as a hypothesis to test, not a claim that every equal-scaling system is bad. | H01, 2006; H04, 2017-06-01; H06, 2007-07-19 (repost 2021-03-13); H07, 2005-05-15 (page update 2014-03-28); H08 = M04, 2010-07-14 |
| B2 | 57 | OPINION (21 October 2026) | Separate "learning a mechanic" from "unlocking a mechanic". Hand engineering both the unlock condition and a situation that makes the unlock useful. Three illustrations: an incremental generator brings a production trade-off; an RPG ability opens a build interaction; an action-game movement ability opens a route. These are proposed applications of a learning lens, not findings from experiments on those three genres. | H06, 2007-07-19; H07, 2005-05-15 |
| B3 | 59 | OPINION (21 October 2026) | An early win should give clear causality: I acted, the result changed, I know a next action. Do not equate low difficulty with incompetence, or high difficulty with depth. A relaxing player may value easy competence; an expert may value a hard optional goal. Offer challenge choice and observe the intended audience instead of forcing one curve on all. | H01, 2006; H05, 2015 |
| B4 | 61 | OPINION (21 October 2026) | Audit an "empty level" by asking what the player can now notice or do differently. A cosmetic celebration is not empty by nature, but twenty indistinguishable celebrations are not twenty shown new experiences. Keep a reward ledger per event: functional change, presentation, next use, optional or not. A milestone may deliberately acknowledge accumulated effort without adding a mechanic. | H04, 2017-06-01; H06, 2007-07-19 |
| B5 | 63 | OPINION (21 October 2026) | Define grind for the project as: repeated activity the target audience reports as low-value relative to the time it demands. Repetition alone is not enough: practice, planning, familiar play and social activity can be chosen pleasures. Tell apart a comprehension problem, a skill problem, a resource bottleneck and an unavoidable wait before prescribing more rewards. More earnings do not fix an unreadable objective. | H01, 2006; H06, 2007-07-19; H08 = M04, 2010-07-14 |

## 4. Twelve versioned game cases (PP:65-166)

### 4.0 Case index (extractor assembly from the case headings and bodies)

| Case | PP (heading, body) | Game, topic | Source | Source date | Version scope the paper states |
| --- | --- | --- | --- | --- | --- |
| 1 | 67, 69 | AdVenture Capitalist, lifetime-based prestige | C01 | 2017-01-12 original; 2017-02-01 syndication (PP:69) | published historical model |
| 2 | 71, 73 | Cookie Clicker, stronger prestige compression | C01 | same | published historical model |
| 3 | 75, 77 | Realm Grinder, best-run pressure | C01 | same | published historical model |
| 4 | 79, 81-83 | Factorio, optional infinite sink after finite goals | C02 | 2016-10-21 | Wube 2016 development example, not every 2026 technology |
| 5 | 85, 87-91 | Diablo IV, character journey vs account progression | C03 | October 2024 season launch (no day) | October 2024 overhaul |
| 6 | 93, 95-99 | World of Warcraft, Warbands | C04 | 2024-04-17 | preview, not a claim every detail stayed |
| 7 | 101, 103-107 | Hearthstone, reward interval | C05 | 2020-12-07 | December 2020 correction |
| 8 | 109, 111-115 | Clash Royale, endgame resources and staged caps | C06 + C07 | 2023-06-18; 2023-11-30 | June 2023 design; caps announced in November (year per C07 date) |
| 9 | 117, 119-123 | League of Legends, champion mastery | C08 | 2024-01-05 | January 2024 proposal, not final or current rules |
| 10 | 125, 127-131 | Teamfight Tactics, levels as thresholds | C09 | 2023-11-20 | patch 13.23 |
| 11 | 133, 135-139 | Overwatch 2, Progression 2.0 | C10 | 2025-08-22 | published plan; exact minutes per level not published |
| 12 | 141, 143-145 | Super Mario Bros. Wonder | C11 | 2023-09-08 | Nintendo announcement; platformer analogue, not a persistent XP economy |

Case 1-3 share C01. Case 8 uses C06 and C07. No case uses M-ids or H-ids.

### 4.1 Cases 1-3: idle-game prestige formulas (C01)

Variable meanings are the paper's: p = total prestige (a count; the paper names no unit), cL = lifetime earnings, cM = maximum earnings (the leading "c" is not explained in the paper; see Z11). Domain stated by the paper: none. (extractor) the roots need a nonnegative argument, so cL, cM >= 0.

| ID | PP | Tag | Content | Src, date |
| --- | --- | --- | --- | --- |
| K1.V | 69 | VERIFIED, published historical model | Pecorella gives total prestige p = 150 * sqrt(cL / 10^15), cL = lifetime earnings. Repeating the same run can add prestige, but progressively less. | C01, 2017-01-12 original; 2017-02-01 syndication |
| K1.O | 69 | OPINION | Suits forgiving resets. Test whether repeat farming pushes out discovery. | C01 (inference), O00 |
| K2.V | 73 | VERIFIED, published historical model | p = (cL / 10^12)^(1/3). Doubling total prestige needs 8 times the total lifetime earnings. | C01, same dates |
| K2.O | 73 | OPINION | Compresses explosive ordinary income, but only works if the journey between resets supplies meaningful changes. | C01 (inference), O00 |
| K3.V | 77 | VERIFIED, published historical model | p = (sqrt(1 + 8 * cM / 10^12) - 1) / 2, based on maximum earnings cM. An identical maximum gives no additional prestige. | C01, same dates |
| K3.O | 77 | OPINION | Pushes the player to extend the frontier, but needs an understandable escape from a stalled build. | C01 (inference), O00 |

Paper's own EXPERIENCE for these three: none in the case text (the register tags C01 "VERIFIED published historical formulas; EXPERIENCE analysis": PP:736). Hand checks in section 7.

### 4.2 Case 4: Factorio optional infinite sink (C02)

| ID | PP | Tag | Content | Src, date |
| --- | --- | --- | --- | --- |
| K4.V | 81 | VERIFIED | Wube's 2016 design: worker-robot-speed research at level 6 and above uses count_formula = 1000 * 2^(l - 6), l = research level (integer, 6 or more). Level 6 costs 1,000 (the paper gives no unit beyond the count); each later level doubles. A published development example, not a claim about every 2026 research technology. | C02, 2016-10-21 |
| K4.E | 81 | EXPERIENCE | The developers call infinite research an optional resource sink for very large factories, with diminishing reward relative to cost. | C02, 2016-10-21 |
| K4.O | 83 | OPINION | In a Roblox tycoon, put this curve after the finite feature-unlock journey. Let throughput optimization feed a voluntary prestige project; do not make exponentially priced improvements the gate to ordinary content. Positive: a purpose for surplus. Risk: expansion turns into repetitive waiting. Design hypotheses, not a retention result. | Inference from C02, 2016-10-21 |

### 4.3 Case 5: Diablo IV (C03)

| ID | PP | Tag | Content | Src, date |
| --- | --- | --- | --- | --- |
| K5.V | 87 | VERIFIED | The October 2024 overhaul set character levels to 1-60; Paragon starts at 60; level-earned Paragon points rose from 200 to 300; Paragon is shared within the same realm and mode partition. The Pit unlocks at 60; Pit tiers 20/35/50/65 unlock Torment I/II/III/IV. | C03, October 2024 season launch |
| K5.E | 89 | EXPERIENCE | Blizzard says repeated World Tier III / Sacred-item progression caused stat bloat and that it wanted new characters to reach endgame sooner. It also reports feedback that scaling could make players feel weak. Developer-reported observations, not controlled measurements. | C03 |
| K5.O | 91 | OPINION | Separate first-character teaching, alternate-character catch-up and optional challenge escalation. A player-chosen difficulty staircase can keep a visible power spike without secretly raising every enemy at that moment. Risk: too many overlapping tracks; show what each track unlocks. | Inference from C03 |

### 4.4 Case 6: World of Warcraft Warbands (C04)

| ID | PP | Tag | Content | Src, date |
| --- | --- | --- | --- | --- |
| K6.V | 95 | VERIFIED | The Warbands preview specified shared new reputation/Renown and a maximum-based conversion: existing Renown 5 and Renown 10 both become 10, not 15. Planned quest model: reputation is awarded on a Warband's first completion, a different currency on repeat completions. A preview, not a claim that every detail stayed unchanged. | C04, 2024-04-17 |
| K6.E | 97 | EXPERIENCE | Blizzard explains that front-loaded campaign reputation would unfairly favor many alts if simply summed. Stated goal: easier character switching with no loss of long-term efficiency, while keeping important character-specific progress. | C04 |
| K6.O | 99 | OPINION | In a class-based Roblox RPG, write down which progress is max-merged, summed or kept per character before adding account catch-up. Shared unlocks can remove redundant chores; summing one-time introductory rewards can create an unintended best-practice of farming alts. | Inference from C04 |

### 4.5 Case 7: Hearthstone rewards track (C05)

| ID | PP | Tag | Content | Src, date |
| --- | --- | --- | --- | --- |
| K7.V | 103 | VERIFIED | The December 2020 correction removed 37,000 XP from the track ("nearly 20%" in the paper's wording; who gave that figure is not stated, see Z06); cut the ranked weekly requirement from 7 wins to 5; expanded the bonus-level endpoint from 150 to 350, with 50 gold per level from level 51 onward. | C05, 2020-12-07 |
| K7.E | 105 | EXPERIENCE | Blizzard admitted its first implementation missed its reward goals and reported player complaints about long gaps between bonus rewards. It also stopped relying on future event XP when setting the ordinary track cadence. | C05 |
| K7.O | 107 | OPINION | Audit reward spacing apart from total seasonal payout. Splitting a payout into smaller visible milestones can fix dead stretches, without assuming more levels means a more generous track. Do not balance the normal route around speculative events. | Inference from C05 |

### 4.6 Case 8: Clash Royale (C06, C07)

| ID | PP | Tag | Content | Src, date |
| --- | --- | --- | --- | --- |
| K8.V1 | 111 | VERIFIED | The June 2023 design priced each level-14-to-15 upgrade at 50,000 Elite Wild Cards, with no other requirement. | C06, 2023-06-18 |
| K8.V2 | 111 | VERIFIED | Supercell announced, in November, ranked caps starting December 4 of 11/12/12/13/13/14/14/15/15/15 across leagues 1-10, and cumulative seasonal Elite Wild Card rewards reaching 50,000 at league 10, up from 25,000. The listed rewards are cumulative totals, not amounts to add together. (Year of "December 4" not stated in the paper; see Z05.) | C07, 2023-11-30 |
| K8.E | 113 | EXPERIENCE | Supercell said the stepped caps were meant to avoid an abrupt rise of card levels in battles. | C07 |
| K8.O | 115 | OPINION | A cap shapes where accumulated account power enters competition. Raising the top reward while changing the cap is a useful example of supply-and-demand coordination, but it does not prove fair matchmaking or a fixed time-to-max for ordinary players. | Inference from C06-C07 |

### 4.7 Case 9: League of Legends champion mastery (C08)

| ID | PP | Tag | Content | Src, date |
| --- | --- | --- | --- | --- |
| K9.V | 119 | VERIFIED | Riot's January 2024 proposal made mastery uncapped and combined score with Marks: none for levels 1-4, one per level at 5-9, two per level at 10 and above. It proposed four per-split milestones, then a repeating milestone. Explicitly the proposal version, not the final or current rules. | C08, 2024-01-05 |
| K9.E | 121 | EXPERIENCE | Riot wanted mastery to show accomplishment as well as play, and argued an infinite track alone can feel like grind; shorter-term milestones were the answer. | C08 |
| K9.O | 123 | OPINION | A Roblox shooter or combat game can split a lasting dedication identity from a short-term skill challenge, and keep both apart from combat-stat power. Risk: requirements that pull players off team objectives just to earn grades. | Inference from C08 |

### 4.8 Case 10: Teamfight Tactics patch 13.23 (C09)

| ID | PP | Tag | Content | Src, date |
| --- | --- | --- | --- | --- |
| K10.V1 | 127 | VERIFIED | Patch 13.23 made level 10 generally available. XP needed for 5>6, 6>7, 7>8, 8>9, 9>10 became 20/36/48/80/84. Published total XP to maximum changed from 228 to 288. | C09, 2023-11-20 |
| K10.V2 | 127 | VERIFIED | Shop odds for the five cost tiers: level 8 became 18/25/36/18/3 percent; level 9 became 10/20/25/35/10 percent. | C09, 2023-11-20 |
| K10.E | 129 | EXPERIENCE | Riot framed the change as giving each level a clearer composition identity. | C09 |
| K10.O | 131 | OPINION | Spending to level and spending to improve the current build can compete as choices instead of forming a compulsory upgrade queue. A new level should change feasible decisions. Risk: a dominant rush strategy if the unlocked odds beat every alternative. Do not copy these match-economy numbers into a persistent simulator. | Inference from C09 |

### 4.9 Case 11: Overwatch 2 Progression 2.0 (C10)

| ID | PP | Tag | Content | Src, date |
| --- | --- | --- | --- | --- |
| K11.V | 135 | VERIFIED | The published plan awards Ascended borders every 20 hero levels, the visual sequence reaching a milestone at 60. Earlier levels are easier; the curve flattens at level 20 to a standard amount of play time. Progress earned before gets rewards retroactively. The article does not publish exact minutes per level. | C10, 2025-08-22 |
| K11.E | 137 | EXPERIENCE | Blizzard says the earlier hero-based system was needlessly complex and did not resonate as intended. The redesign stresses legibility and easy-to-reach cosmetic rewards. | C10 |
| K11.O | 139 | OPINION | Use fast cosmetic onboarding, then an understandable long-term recognition track, without making veteran account age a combat advantage. Retroactive credit respects existing investment. A constant rate or a prestigious border does not guarantee the player still enjoys the matches. | Inference from C10 |

### 4.10 Case 12: Super Mario Bros. Wonder (C11)

| ID | PP | Tag | Content | Src, date |
| --- | --- | --- | --- | --- |
| K12.V | 143 | VERIFIED | Nintendo's announcement describes six worlds around the Petal Isles, seven areas in total, and badges earned during progress. Examples change wall climbing, underwater movement, jumping or grappling; an Invisibility badge deliberately adds challenge. Local co-op groups use the same badge. The paper calls this a platformer/obby analogue, not a persistent XP economy. | C11, 2023-09-08 |
| K12.O | 145 | OPINION | In an obby, a worthwhile unlock can change route choice or movement expression instead of adding another speed percentage. Let an assist and an optional constraint coexist. Risk: mandatory movement upgrades that invalidate older obstacles, or a cosmetic-style progression promise that misleads. The source gives no badge-unlock timeline or completion-time benchmark. | Inference from C11 |

No EXPERIENCE row for Case 12 in the paper.

### 4.11 Contrasts, design questions, unknowns, rule table

| ID | PP | Tag | Content | Src, date |
| --- | --- | --- | --- | --- |
| KX1 | 149 | OPINION | The sources do not disagree about one universal formula; they serve different progression jobs. Factorio's optional exponential sink contrasts with Overwatch's flattened cosmetic dedication track. WoW removes repeated account chores, while the idle cases repeat a run on purpose. TFT makes progression a match-level investment choice; Diablo separates a lasting character journey from challenge unlocks. Read them as context-dependent alternatives, not proof one studio is right. | C01-C11, dates above |

Design question to case (PP:151-158). The right column is OPINION throughout.

| ID | PP | Design question | Evidence-backed case | Transfer hypothesis (OPINION) |
| --- | --- | --- | --- | --- |
| Q1 | 152 | Must reset runs beat the previous best? | Realm Grinder versus AdCap/Cookie Clicker [C01] | Choose the behavior on purpose, not just a root exponent. |
| Q2 | 153 | Where should exponential costs live? | Factorio [C02] | Prefer voluntary surplus sinks over basic-content gates. |
| Q3 | 154 | What survives a fresh character? | Diablo/WoW [C03-C04] | Keep accomplishment and define how progress aggregates. |
| Q4 | 155 | Why does a generous track still feel empty? | Hearthstone [C05] | Measure gaps between usable rewards, not total gold alone. |
| Q5 | 156 | Where does account power affect ranked play? | Clash Royale [C06-C07] | Coordinate upgrade resource supply and tier caps. |
| Q6 | 157 | What does a level actually mean? | LoL/TFT/Overwatch [C08-C10] | Tell apart skill, options, dedication and combat strength. |
| Q7 | 158 | Must an unlock be a numerical upgrade? | Mario Wonder [C11] | Add movement verbs and voluntary challenge choices. |

| ID | PP | Content | Tag | Src, date |
| --- | --- | --- | --- | --- |
| U1 | 160 | Unknowns. The review claims no verified enjoyment uplift, no churn effect size and no universal minutes to first prestige. No full game was played or instrumented. The chosen official sources are public rules, development accounts and patch announcements; they cannot show causality or population-wide satisfaction. Some rules are historical proposals. | OPINION (methodological limit) | review limitation, 2026-10-21 |

Rule table PP:162-166 (columns as the paper: Rule / Formula or number / Evidence mark / Source and date)

| ID | PP | Rule | "Formula or number" cell | Tag | Src, date |
| --- | --- | --- | --- | --- | --- |
| KT1 | 163 | Name the benefit of the milestone | Capability, choice, understanding, access or accomplishment (five items; B1 lists six, see Z01) | OPINION | O00, 2026-10-21 |
| KT2 | 164 | Distinguish game rules from player response | Published configuration is not a satisfaction measure | OPINION | O00, 2026-10-21 |
| KT3 | 165 | Compare only the stated game versions | Historical preview versus released rule versus current claim | OPINION | O00, 2026-10-21 |
| KT4 | 166 | Let genre change the job of progression | Options, mastery, account convenience and surplus sinks differ | OPINION | O00, 2026-10-21 |

## 5. Shapes and player timelines (PP:168-204)

### 5.1 Shape and vocabulary

All OPINION, source O00, 2026-10-21 (PP:174 says the definitions are the paper's operational ones, not standard industry terms).

| ID | PP | Item | Definition (paraphrase) |
| --- | --- | --- | --- |
| S1 | 170 | Progression shape | A relationship between state, action and consequence, not the look of a plotted line. For review, name the state being changed (owned generators, unlocked verbs, character level, competitive options, cosmetic recognition, mastery). Then name the distance to the next meaningful change in actions, required resources and measured time. These distances can move in opposite directions. |
| VC1 | 174 | Fast start | The player can reach a meaningful next state with little prior investment on the stated starting path. It does not need every later cost to be small. |
| VC2 | 174 | Slowdown | Required effort rises relative to the player's capacity. |
| VC3 | 174 | Soft wall | Still reachable through the available earning process, but expensive relative to the intended route. |
| VC4 | 174 | Hard wall | Needs a separate condition (a key, a content unlock, a prerequisite) that repeating the current action cannot satisfy. |
| VC5 | 176 | Spike | A discontinuity in useful capability: an extra attack removed from a kill sequence, a new route made feasible, a production multiplier unlocked. |
| VC6 | 176 | Plateau | Holds an important result roughly constant while other things change. It can make room to learn a skill or can hide a lack of content. |
| VC7 | 176 | Reset | Deliberately removes some state while keeping other state. |
| VC8 | 176 | Catch-up | Reduces the repeated cost of reaching a capability already earned, or an intended entry point. |
| VC9 | 176 | Record-keeping rule | For a reset or catch-up, record exactly what is removed, kept, merged and newly granted. |

### 5.2 Placing changes, spikes, and timeline cautions

| ID | PP | Tag | Content | Src, date |
| --- | --- | --- | --- | --- |
| S2 | 180 | OPINION synthesis | The cases give alternatives, not a shared schedule. Overwatch's recognition redesign flattens after an introductory part; Factorio's optional research grows dearer forever; Hearthstone's correction fixes spacing between useful rewards; WoW's account design fixes repeated character work. None is evidence that a simulator should prestige on day one or an RPG should unlock its whole kit in session one. | C02, 2016-10-21; C04, 2024-04-17; C05, 2020-12-07; C10, 2025-08-22 |
| S3 | 182 | OPINION | For each planned spike, compare before and after against the same encounter or earning opportunity. If the enemy is upgraded at the moment the weapon is, the nominal stat spike may not change the experience. If both cost and income rise, compute their ratio rather than inferring speed from larger income alone. These are review requirements, not a ban on enemy scaling. | O00, 2026-10-21 |
| S4 | 184 | OPINION | The timeline template uses the requested checkpoint labels as planning intervals, not as measured completion-time targets. The owner can reject or move any checkpoint. Before presenting it as a forecast, enter the real reachable state, available play time and measured time distribution. A player's first calendar week is not a fixed amount of active play. | O00, 2026-10-21 |
| S5 | 186 | OPINION, author-proposed template dated 2026-10-21 | The checkpoints come from the requested brief. They are not evidence that every player should reach a level in a minute, day, week or month. Define "day/week/month" as calendar age or as active play before assigning any target. The feelings are candidates for the creative director, not findings from player research. Methodological basis cited: W02 (2019), W04 (2010-08-25). | W02, 2019 (GDC event year; exact date not established); W04, 2010-08-25 |

### 5.3 Feeling timeline template (PP:188-193; columns as the paper)

All rows OPINION (S5). "Evidence to gather" is not a preset target.

| ID | PP | Brief checkpoint | Candidate target feeling | Design question | Evidence to gather |
| --- | --- | --- | --- | --- | --- |
| FT1 | 189 | First minute | "I understand what my action changed." | Is the first meaningful action legible and consequential? | Action completion, feedback recognition, player explanation |
| FT2 | 190 | First session | "I made a choice and can name my next goal." | Did progression reveal agency rather than only a larger counter? | Chosen route, first upgrade/unlock, next-goal recall, time distributions |
| FT3 | 191 | First day | "Returning gives me a new possibility." | What changes on return without punishing absence? | State on return, new choices, offline reward interpretation |
| FT4 | 192 | First week | "My build or approach expresses a preference." | Is there meaningful specialization, mastery or a new problem? | Route diversity, viable alternatives, bottleneck traces |
| FT5 | 193 | First month | "I still have goals, or a satisfying completion." | Is there depth, an optional reset, social purpose or a clean ending? | Long-term paths, completion quality, repetition complaints, reset uptake |

Feeling wording in quotation marks is the paper's own (each is under 15 words).

### 5.4 Plateau rule and shapes rule table

| ID | PP | Tag | Content | Src, date |
| --- | --- | --- | --- | --- |
| PL1 | 197 | OPINION | A plateau proposal must name the new thing the player learns, chooses or optimizes while the numeric track slows, state the exit condition and why it serves the intended experience. If the only reason is that the economy must last longer, show the owner alternatives: more varied goals, a different content gate, an optional challenge, or a shorter total progression. Do not hide a content shortfall behind a coefficient. | O00, 2026-10-21 |
| ST1 | 200 | OPINION | State what the curve advances. Cell: state before -> action -> state after. | O00, 2026-10-21 |
| ST2 | 201 | OPINION | Separate resource walls from prerequisite walls. Cell: affordability condition versus unlock predicate. | O00, 2026-10-21 |
| ST3 | 202 | OPINION | Do not assign universal calendar targets. Cell: calendar interval is not active play duration. | O00, 2026-10-21 |
| ST4 | 203 | OPINION | Compare power against unchanged content. Cell: result before and after the same encounter. | O00, 2026-10-21 |
| ST5 | 204 | OPINION | Explain the purpose of a plateau. Cell: learning goal and explicit exit condition. | O00, 2026-10-21 |

## 6. Mathematical toolkit and curve library (PP:206-228)

### 6.0 Preamble rows

| ID | PP | Tag | Content | Src, date |
| --- | --- | --- | --- | --- |
| CD1 | 208 | OPINION framing | The numbers are historical published examples and exact derivations, not 2026 Roblox tuning recommendations. Here EXPERIENCE marks the author's report or model; VERIFIED marks arithmetic that is true given explicit inputs (not proof of fun); OPINION marks recommended workflow and predicted feel. No unsourced numeric gameplay target is introduced. Missing attack cadence, XP rate, offline policy and prestige parameters remain variables. All sources accessed 2026-10-21. | O00, 2026-10-21 |
| CD2 | 210 | VERIFIED definitions; OPINION applications | Definitions and derivations use a nonnegative integer progression index n. Coefficients are symbolic design inputs, not proposed numbers. Evaluating at n = 0, 1, 2 is mathematical sampling, not a prescription for how many levels to have. Original practitioner context: M01 (2016-10-04) and M04 (2010-07-14). Applications and intended feelings are OPINION. | M01, 2016-10-04; M04, 2010-07-14; O00, 2026-10-21 |

Variable convention for the table (PP:210, extractor wording): n = progression index, integer >= 0. f(n) or F(n) = the modeled quantity at index n (cost, requirement, output). The paper gives no unit for f; the unit is whatever the designer models. a, b, b1, b2, r, p, alpha, h, K, K_i, m_i = coefficients or parameters; their stated domains are in the Domain column; "not stated" means the paper gives none.

### 6.1 Curve table (PP:212-221; nine curves)

Sample values are the paper's, exact, at n = 0, 1, 2. Intended feel and best-use are OPINION (O00, 2026-10-21). Formula and sample arithmetic are VERIFIED math by the paper's own labeling (PP:210; see Z04). Hand checks of every sample are in section 7.

| ID | PP | Curve | Formula | Domain (as stated) | Intended feel (OPINION) | Best-use hypothesis (OPINION) | f(0); f(1); f(2) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CV1 | 213 | Affine / linear | f(n) = a + b*n | a, b >= 0 | Readable equal increments | Early deterministic unlock prices | a; a+b; a+2b |
| CV2 | 214 | Polynomial | f(n) = a + b*n^p | a, b >= 0; p > 1 | Increasing absolute steps | Growth without a fixed percentage inflation | a; a+b; a+b*2^p |
| CV3 | 215 | Triangular cumulative | F(n) = b*n*(n+1)/2; incremental cost = b*n | b: not stated | Increasing marginal effort | Linear per-purchase cost; quadratic cumulative cost | 0; b; 3b |
| CV4 | 216 | Exponential | f(n) = a*r^n | a > 0; r > 1 | Constant proportional growth | Escalating prices, compared against income | a; a*r; a*r^2 |
| CV5 | 217 | Logarithmic | f(n) = a + b*log_r(1+n) | b >= 0; r > 1; a: not stated | Diminishing marginal progress | Compressed progress displays or transformations | a; a + b*log_r(2); a + b*log_r(3) |
| CV6 | 218 | Fractional power | f(n) = a + b*n^alpha | 0 < alpha < 1; a, b: not stated | Soft compression without a hard cap | A possible prestige transform | a; a+b; a + b*2^alpha |
| CV7 | 219 | Saturating | f(n) = a + b*n/(h+n) | h > 0; a, b: not stated | Approaching a limit | A capped progression alternative | a; a + b/(h+1); a + 2b/(h+2) |
| CV8 | 220 | Continuous piecewise | f(n) = a + b1*n for n <= K; f(n) = a + b1*K + b2*(n-K) for n > K | K, b1, b2, a: not stated | Deliberate pacing bands | Change slope at approved band boundaries | Paper: "Depends on K". (extractor) see below |
| CV9 | 221 | Milestone step | f(n) = base(n) * prod_i ( m_i ^ [n >= K_i] ) | base(n), m_i, K_i: not stated; bracket [n >= K_i] not defined by the paper | Deliberate power spikes | Count-based or unlock-based milestone boosts | Paper: "Evaluate against actual K_i". (extractor) see below |

(extractor) Derivations for CV8 and CV9, from the paper's formulas only, not paper text:
- CV8, f(0) = a for every K >= 0 (first branch). If K >= 2: f(1) = a + b1, f(2) = a + 2*b1. If K = 1: f(1) = a + b1, f(2) = a + b1 + b2. If K = 0: f(1) = a + b2, f(2) = a + 2*b2. The two branches agree at n = K (both a + b1*K), so the curve is continuous, as the name says.
- CV9, with the bracket read as 1 when n >= K_i and 0 otherwise (a standard Iverson bracket; the paper does not define it): f(n) = base(n) multiplied by the product of m_i over all i with K_i <= n. At n = 0, 1, 2 the product includes only milestones with K_i <= 0, 1, 2.
- (extractor) Link, not stated by the paper: CV6 with alpha = 1/2 has the shape of the Case 1 formula and with alpha = 1/3 the shape of the Case 2 formula; Case 3's formula is the inverse of CV3 (see HC03).

### 6.2 Per-level versus cumulative (PP:223)

| ID | PP | Tag | Content | Src, date |
| --- | --- | --- | --- | --- |
| CD3 | 223 | VERIFIED derivation | Do not mix a per-level requirement e_l with cumulative XP X_l. If level 1 starts at 0 XP, then X_l = sum over j = 1..(l-1) of e_j. (extractor reading: e_j is the XP needed to go from level j to j+1; the paper does not define e_j beyond "per-level requirement".) | Derived here, 2026-10-21; example M04, 2010-07-14 |
| CD4 | 223 | VERIFIED derivation | A constant e_j gives linear cumulative XP; a linear e_j gives quadratic cumulative XP. | same |
| CD5 | 223 | VERIFIED derivation (conditional) | An XP curve is not automatically a time curve. With a fixed q XP per second, time = X / q. With varying acquisition q(t), solve the integral of q(t) dt (from 0 to t) = X. No q is inferred from the requirement curve. | same |

Rule table PP:225-228 (Rule / Formula or number / Evidence mark / Source and date)

| ID | PP | Rule | Formula or number | Tag | Src, date |
| --- | --- | --- | --- | --- | --- |
| CT1 | 226 | State whether a table is incremental or cumulative | X_l = sum e_j | VERIFIED derivation | M04, 2010-07-14; derivation 2026-10-21 |
| CT2 | 227 | Separate curve shape from intended feeling | Feeling is a testable hypothesis, not a coefficient | OPINION | this paper, 2026-10-21 |
| CT3 | 228 | Preserve thresholds when fitting curves | Piecewise formulas retain boundary K | VERIFIED derivation / OPINION application | this paper, 2026-10-21 |

## 7. Hand arithmetic checks (extractor; paper inputs only)

I checked what can be checked from the paper's own numbers. A pass here means internally consistent, not true to the source.

| ID | Check | Inputs (PP) | Result |
| --- | --- | --- | --- |
| HC01 | Factorio: 1000*2^(l-6) at l = 6, 7, 8 | 81 | 1,000; 2,000; 4,000. Level 6 = 1,000 and doubling both hold. |
| HC02 | Cookie Clicker: doubling p needs 8x lifetime earnings | 73 | With p = (x/10^12)^(1/3): p(8x) = 2*p(x). Holds. |
| HC03 | Realm Grinder formula is the inverse of the triangular number relation | 77, 215 | Solve y = p(p+1)/2 with y = cM/10^12: p = (sqrt(1+8y) - 1)/2. Matches the paper's formula. Same cM gives same p, so no extra prestige. Holds. |
| HC04 | AdCap: repeating an identical run adds less | 69 | Total p after two identical runs = 150*sqrt(2*x/10^15) = sqrt(2) * (first-run total); the second run adds (sqrt(2) - 1) of the first, about 0.41 times it, less than 1. Holds. Doubling p would need 4x earnings (not stated in the paper). |
| HC05 | TFT shop odds sum to 100 | 127 | Level 8: 18+25+36+18+3 = 100. Level 9: 10+20+25+35+10 = 100. Holds. |
| HC06 | TFT XP: sum of the five listed requirements | 127 | 20+36+48+80+84 = 268, not 288. Gap 288 - 268 = 20 must come from earlier levels, which the paper does not list. Not checkable here (Z02). |
| HC07 | Clash caps: ten values for ten leagues, non-decreasing | 111 | 11/12/12/13/13/14/14/15/15/15 = 10 values, never fall. Holds. |
| HC08 | Clash: 50,000 appears twice | 111 | 14>15 upgrade cost = 50,000; league-10 cumulative seasonal reward = 50,000. The paper draws no link; no claim made. |
| HC09 | Curve samples CV1-CV7 at n = 0, 1, 2 | 213-219 | All match direct substitution (n=0 gives a, a, 0, a, a+b*log_r(1)=a, a, a). Triangular: F(1) = b, F(2) = 3b, F(n) - F(n-1) = b*n. |
| HC10 | CV8 continuity at n = K | 220 | Both branches give a + b1*K. Holds. |
| HC11 | Cumulative from per-level: constant and linear e_j | 223 | e_j = c: X_l = c*(l-1), linear. e_j = c*j: X_l = c*(l-1)*l/2, quadratic. Holds. (This matches CV3 with b = c.) |
| HC12 | Hearthstone: 37,000 XP as "nearly 20%" | 103 | Implies a pre-correction track total a little above 185,000 XP. The paper gives no total; cannot confirm. |

## 8. Claims to fact-check (a)

Every VERIFIED or EXPERIENCE claim in lines 1-230 that carries a number, formula, version or date. "PP" is the paper line. Tag is the paper's. Src date is from the register (section 9). Fact-check confirms the claim matches the source and the source date is right.

| # | Claim (paraphrase, numbers exact) | PP | Src | Src date | Tag |
| --- | --- | --- | --- | --- | --- |
| CL01 | AdCap total prestige p = 150 * sqrt(cL / 10^15), cL = lifetime earnings | 69 | C01 | 2017-01-12 (+2017-02-01 syndication) | VERIFIED |
| CL02 | AdCap: repeating the same run still adds prestige, progressively less | 69 | C01 | same | VERIFIED |
| CL03 | Cookie Clicker p = (cL / 10^12)^(1/3); doubling p needs 8x lifetime earnings | 73 | C01 | same | VERIFIED |
| CL04 | Realm Grinder p = (sqrt(1 + 8*cM/10^12) - 1)/2, from maximum earnings; identical maximum gives no extra prestige | 77 | C01 | same | VERIFIED |
| CL05 | Factorio worker-robot-speed research level 6+ : count_formula = 1000 * 2^(l-6); level 6 costs 1,000; each level doubles; a 2016 development example | 81 | C02 | 2016-10-21 | VERIFIED |
| CL06 | Factorio developers describe infinite research as an optional sink for huge factories with diminishing reward vs cost | 81 | C02 | 2016-10-21 | EXPERIENCE |
| CL07 | Diablo IV October 2024: character levels 1-60; Paragon begins at 60 | 87 | C03 | October 2024 | VERIFIED |
| CL08 | Diablo IV October 2024: level-earned Paragon points raised from 200 to 300 | 87 | C03 | October 2024 | VERIFIED |
| CL09 | Diablo IV: Paragon shared within the same realm and mode partition | 87 | C03 | October 2024 | VERIFIED |
| CL10 | Diablo IV: Pit unlocks at 60; Pit tiers 20/35/50/65 unlock Torment I/II/III/IV | 87 | C03 | October 2024 | VERIFIED |
| CL11 | Diablo IV: Blizzard says World Tier III / Sacred-item progression caused stat bloat, wanted new characters to reach endgame sooner, and reports feedback that scaling could make players feel weak | 89 | C03 | October 2024 | EXPERIENCE |
| CL12 | WoW Warbands preview: shared new reputation/Renown; existing Renown 5 and Renown 10 become 10, not 15 | 95 | C04 | 2024-04-17 | VERIFIED |
| CL13 | WoW Warbands preview: reputation on a Warband's first quest completion, a different currency on repeats | 95 | C04 | 2024-04-17 | VERIFIED |
| CL14 | WoW: Blizzard says front-loaded campaign reputation would favor many alts if summed; goal is easier character switching without lost long-term efficiency | 97 | C04 | 2024-04-17 | EXPERIENCE |
| CL15 | Hearthstone Dec 2020: 37,000 XP removed ("nearly 20%"); weekly ranked requirement 7 wins -> 5; bonus-level endpoint 150 -> 350; 50 gold per level from 51 onward | 103 | C05 | 2020-12-07 | VERIFIED |
| CL16 | Hearthstone: Blizzard said the first implementation missed goals; players complained of long gaps between bonus rewards; ordinary cadence no longer depends on future event XP | 105 | C05 | 2020-12-07 | EXPERIENCE |
| CL17 | Clash Royale June 2023: each level 14->15 upgrade costs 50,000 Elite Wild Cards, no other requirement | 111 | C06 | 2023-06-18 | VERIFIED |
| CL18 | Clash Royale: caps from December 4 of 11/12/12/13/13/14/14/15/15/15 across leagues 1-10 | 111 | C07 | 2023-11-30 | VERIFIED |
| CL19 | Clash Royale: cumulative seasonal Elite Wild Card rewards reach 50,000 at league 10, up from 25,000; listed rewards are cumulative totals | 111 | C07 | 2023-11-30 | VERIFIED |
| CL20 | Clash Royale: Supercell said stepped caps avoid an abrupt card-level increase in battles | 113 | C07 | 2023-11-30 | EXPERIENCE |
| CL21 | LoL mastery January 2024 proposal: uncapped mastery; Marks none at levels 1-4, one per level at 5-9, two per level at 10+ | 119 | C08 | 2024-01-05 | VERIFIED |
| CL22 | LoL proposal: four per-split milestones, then a repeating milestone; proposal version, not final | 119 | C08 | 2024-01-05 | VERIFIED |
| CL23 | LoL: Riot wanted mastery to show accomplishment; said an infinite track alone can feel like grind; shorter milestones as response | 121 | C08 | 2024-01-05 | EXPERIENCE |
| CL24 | TFT patch 13.23: level 10 generally available; XP for 5>6, 6>7, 7>8, 8>9, 9>10 = 20/36/48/80/84 | 127 | C09 | 2023-11-20 | VERIFIED |
| CL25 | TFT patch 13.23: published total XP to maximum 228 -> 288 | 127 | C09 | 2023-11-20 | VERIFIED |
| CL26 | TFT patch 13.23: level 8 shop odds 18/25/36/18/3 percent; level 9 10/20/25/35/10 percent | 127 | C09 | 2023-11-20 | VERIFIED |
| CL27 | TFT: Riot framed the change as a clearer composition identity per level | 129 | C09 | 2023-11-20 | EXPERIENCE |
| CL28 | Overwatch 2 Progression 2.0: Ascended borders every 20 hero levels; visual sequence reaches a milestone at 60 | 135 | C10 | 2025-08-22 | VERIFIED |
| CL29 | Overwatch 2: earlier levels easier; curve flattens at level 20 to a standard amount of play time; prior progress rewarded retroactively; exact minutes per level not published | 135 | C10 | 2025-08-22 | VERIFIED |
| CL30 | Overwatch 2: Blizzard says the earlier hero-based system was unnecessarily complex and did not resonate; redesign stresses legibility and accessible cosmetics | 137 | C10 | 2025-08-22 | EXPERIENCE |
| CL31 | Mario Wonder: six worlds around the Petal Isles, seven areas in total; badges earned during progress; examples (wall climbing, underwater movement, jumping, grappling); Invisibility adds challenge; co-op groups share the badge | 143 | C11 | 2023-09-08 | VERIFIED |
| CL32 | Rule 2: a published rule is evidence of that rule in its stated version only (cites C03 October 2024 and C08 2024-01-05) | 25 | C03, C08 | October 2024; 2024-01-05 | VERIFIED |
| CL33 | Rule 6: optional endless sink and introductory reward track solve different problems (cites C02 and C10) | 33 | C02, C10 | 2016-10-21; 2025-08-22 | EXPERIENCE |
| CL34 | Rule 9: reward spacing can need correction despite a large aggregate payout (cites C05) | 39 | C05 | 2020-12-07 | EXPERIENCE |
| CL35 | Rule 10: reward research gives no support to "all rewards help" or "all rewards harm" (cites H02 1999 and H03 2001) | 41 | H02, H03 | 1999-11; 2001 spring | VERIFIED |
| CL36 | Curve library: the nine formulas and their n = 0, 1, 2 sample values (section 6.1) are correct as math | 213-221 | O00 (M01 2016-10-04, M04 2010-07-14 for context) | 2026-10-21 | VERIFIED (paper's derivation) |
| CL37 | Per-level vs cumulative: X_l = sum_{j=1}^{l-1} e_j; constant e_j gives linear X, linear e_j gives quadratic X; time = X/q for fixed q, integral of q(t) dt = X otherwise | 223, 226 | M04 (context), O00 | 2010-07-14; 2026-10-21 | VERIFIED derivation |
| CL38 | M01 is dated 2016-10-04 and M04 2010-07-14 as "original practitioner context" for the curve toolkit | 210 | M01, M04 | 2016-10-04; 2010-07-14 | VERIFIED (paper's dating) |

OPINION rows that lean on a cited source (fact-check optional: does the source plausibly support the use?):

| # | OPINION row | PP | Src leaned on |
| --- | --- | --- | --- |
| OL1 | Six benefits of a progression event | 55 | H01, H04, H06, H07, H08 (= M04) |
| OL2 | Learning vs unlocking a mechanic | 57 | H06, H07 |
| OL3 | Early win and challenge choice | 59 | H01, H05 |
| OL4 | Empty-level audit | 61 | H04, H06 |
| OL5 | Grind definition | 63 | H01, H06, H08 (= M04) |
| OL6 | Timeline template method | 186 | W02, W04 |
| OL7 | Cross-case synthesis of what each case shows | 180 | C02, C04, C05, C10 |

## 9. Source table (b): every source id cited in lines 1-230

Register lines are PP:728-1014 and PP:1216-1262. "Evidence type" is the register's wording. No web access was used; URLs are copied from the register. Quotation text is at the register line given (not reproduced here).

| Id | Title | Author / org | Date (register) | Evidence type | URL (date provenance URL) | PP register line |
| --- | --- | --- | --- | --- | --- | --- |
| O00 | Original recommendations and mathematical analysis prepared for this paper | the paper | 2026-10-21 | not an external empirical source | none | 730 |
| C01 (= M02) | The Math of Idle Games, Part III | Anthony Pecorella / Kongregate | 2017-01-12; author republication 2021-07-30 (in-text PP:69 also says 2017-02-01 syndication) | VERIFIED published historical formulas; EXPERIENCE analysis | https://www.kongregate.com/en/pages/the-math-of-idle-games-part-iii (provenance: https://www.sirpinski.com/the-math-of-idle-games-part-iii/) | 732 |
| C02 | Friday Facts #161 - Infinite Research and Blueprint Library | Tomas and kovarex / Wube | 2016-10-21 | VERIFIED published development formula; EXPERIENCE intent | https://www.factorio.com/blog/post/fff-161 | 746 |
| C03 | Conquer Colossal Foes in Season of Hatred Rising | Blizzard Entertainment | October 2024 season launch; accessed 2026-10-21 | VERIFIED announced rules; EXPERIENCE developer observations | https://news.blizzard.com/en-gb/article/24140803/conquer-colossal-foes-in-season-of-hatred-rising | 758 |
| C04 | The War Within: Warbands Preview | Blizzard Entertainment | 2024-04-17 | VERIFIED preview specification; EXPERIENCE rationale | https://news.blizzard.com/en-us/article/24061008/the-war-within-warbands-preview (provenance: https://us.forums.blizzard.com/en/wow/t/the-war-within-warbands-preview/1832312) | 770 |
| C05 | Rewards Track Update Coming Soon | Ben Lee / Blizzard Entertainment | 2020-12-07 | VERIFIED announced corrections; EXPERIENCE player-feedback account | https://hearthstone.blizzard.com/en-gb/news/23585675/rewards-track-update-coming-soon | 784 |
| C06 | Card Evolution | Supercell | 2023-06-18 | VERIFIED announced upgrade cost | https://supercell.com/en/games/clashroyale/blog/release-notes/card-evolution-2/ | 796 |
| C07 | Changes Coming to Path of Legends | Supercell | 2023-11-30 | VERIFIED announced caps/rewards; EXPERIENCE intent | https://supercell.com/en/games/clashroyale/blog/news/changes-coming-to-path-of-legends/ | 808 |
| C08 | /dev: Updating Champion Mastery | Evan "Riot Revenancer" Humphreys / Riot Games (register prints the nickname without quotes) | 2024-01-05 | VERIFIED proposal; EXPERIENCE design intent | https://www.leagueoflegends.com/en-us/news/dev/dev-updating-champion-mastery/ | 820 |
| C09 | Teamfight Tactics patch 13.23 notes | Riot Prism / Riot Games | 2023-11-20 | VERIFIED patch numbers; EXPERIENCE designer interpretation | https://teamfighttactics.leagueoflegends.com/en-gb/news/game-updates/teamfight-tactics-patch-13-23-notes/ | 832 |
| C10 | Weekly Recall: Gaining Progress | Blizzard Entertainment | 2025-08-22 | VERIFIED progression specification; EXPERIENCE feedback account | https://news.blizzard.com/en-us/article/24224138/weekly-recall-gaining-progress (provenance: https://eu.forums.blizzard.com/en/overwatch/t/weekly-recall-gaining-progress/38036) | 844 |
| C11 | Experience the unexpected in Super Mario Bros. Wonder gameplay presentation | Nintendo | 2023-09-08 | VERIFIED announced mechanics | https://www.nintendo.com/au/news-and-articles/experience-the-unexpected-in-super-mario-bros-wonder-gameplay-presentation/ | 858 |
| M01 | The Math of Idle Games, Part I | Anthony Pecorella | 2016-10-04; author republication 2021-07-30 | EXPERIENCE for game model; VERIFIED for explicitly derived arithmetic | https://www.kongregate.com/en/pages/the-math-of-idle-games-part-i (provenance: https://www.sirpinski.com/the-math-of-idle-games-part-i/) | 870 |
| M04 (= H08) | Level 2: Numeric Relationships | Ian Schreiber (Game Balance Concepts) | 2010-07-14 | EXPERIENCE for reported game rules; VERIFIED for derivations | https://gamebalanceconcepts.wordpress.com/2010/07/14/level-2-numeric-relationships/ | 896 |
| H01 | The Motivational Pull of Video Games | Ryan, Rigby and Przybylski | 2006 | VERIFIED | https://selfdeterminationtheory.org/SDT/documents/2006_RyanRigbyPrzybylski_MandE.pdf | 936 |
| H02 | A meta-analytic review of experiments examining the effects of extrinsic rewards on intrinsic motivation | Deci, Koestner and Ryan | 1999-11 | VERIFIED | https://pubmed.ncbi.nlm.nih.gov/10589297/ | 946 |
| H03 | Pervasive negative effects of rewards on intrinsic motivation: The myth continues | Cameron, Banko and Pierce | 2001 spring | VERIFIED | https://pmc.ncbi.nlm.nih.gov/articles/PMC2731358/ | 956 |
| H04 | Towards understanding the effects of individual gamification elements on intrinsic motivation and performance | Mekler et al. | 2017-06-01 | VERIFIED | https://research.aalto.fi/en/publications/towards-understanding-the-effects-of-individual-gamification-elem/ | 966 |
| H05 | The challenge-skill balance and antecedents of flow: A meta-analytic investigation | Fong, Zaleski and Leach | 2015 journal issue; DOI first published 2014 | VERIFIED | https://www.tandfonline.com/doi/abs/10.1080/17439760.2014.967799?journalCode=rpos20&src=recsys | 976 |
| H06 | The Chemistry of Game Design | Daniel Cook | 2007-07-19 original; 2021-03-13 author repost | EXPERIENCE | https://lostgarden.com/2021/03/13/the-chemistry-of-game-design-2/ | 986 |
| H07 | Geek Fun Isn't Frivolous | Raph Koster | 2005-05-15 original; 2014-03-28 page update | EXPERIENCE | https://www.raphkoster.com/games/essays/geek-fun-isnt-frivolous/ | 996 |
| W02 | Beyond Spreadsheets: Building a Metagame Simulator for Balance and Prototyping | David Morris, Spryfox (GDC Vault session overview) | 2019 (GDC event year; exact session date not established) | EXPERIENCE | https://gdcvault.com/play/1026489/Beyond-Spreadsheets-Building-a-Metagame | 1228 |
| W04 | Level 8: Metrics and Statistics | Ian Schreiber, Game Balance Concepts | 2010-08-25 | EXPERIENCE | https://gamebalanceconcepts.wordpress.com/2010/08/25/level-8-metrics-and-statistics/ | 1252 |

Register ids not cited in lines 1-230, so not in this table: H09, M03, M05, M06, W01, W03, W05-W08 (M02 is only an alias of C01; H08 only an alias of M04).

Paper's own limit notes on the H sources (lookup, outside range; paraphrased; the paper says these in its section 6):

| Id | Lookup PP | Limit the paper states |
| --- | --- | --- |
| H01 | 337-339 | Associations between perceived autonomy/competence and enjoyment; samples of 89, 50 and 58 undergraduates (Studies 1-3) and 730 online-community members aged 16-44 (Study 4). Largely correlational; not an experiment showing a progression tree causes retention. |
| H02 | 343-345 | Meta-analysis of 128 experiments; expected tangible rewards reduced free-choice intrinsic motivation, positive feedback raised it; mostly controlled tasks, not commercial games. |
| H03 | 349-351 | Competing meta-analysis rejecting a pervasive negative-reward conclusion; the paper calls the disagreement with H02 "important" and says neither supports "all help" or "all harm". |
| H04 | 355-357 | Points, levels and leaderboards raised annotation quantity without significant gains in intrinsic motivation or competence; image-annotation task, not entertainment gameplay; sample not stated. |
| H05 | 361-363 | Meta-analysis of 28 studies: moderate challenge-skill/flow link; associations only, no universally optimal difficulty ratio; only the abstract was verified. |
| H06 | 367-369 | Designer framework, not a controlled study; do not repeat its neuroscience as established evidence. |
| H07 | 373-375 | Designer op-ed; not proof that all enjoyment is learning; do not drop comfort, socializing, expression. |
| H08 / M04 | 379-381 | Educational worked examples, not measured player experience or a present-day balance audit of the example game. |

## 10. Contradictions and limits the paper states (c)

| ID | PP | Item | Handling for the skill writer |
| --- | --- | --- | --- |
| X01 | 11, 15 | VERIFIED means "the source says so", not reproduced, not causal, not proven for Roblox. Historical numbers belong to their versions. | Keep the version next to every number. |
| X02 | 9 | A model shows results under its assumptions; only a source or playtest shows how people respond. | Never present a model output as a feeling. |
| X03 | 17, 208 | No earning rate is invented; timelines stay symbolic; coefficients are not balance constants. | Variables stay variables. |
| X04 | 55 | The "equal scaling cancels the number" idea is a hypothesis, not a claim that all equal-scaling systems are bad. | Mark as hypothesis. |
| X05 | 57 | Learning-vs-unlocking examples are proposed applications, not experimental findings. | Mark as proposal. |
| X06 | 59, 61, 63 | Easy is not incompetent, hard is not deep; a cosmetic celebration is not empty by nature; repetition alone is not grind. | Judge by audience and function. |
| X07 | 69-77 | Cases 1-3 are historical published models, not current game values. | Version-tag. |
| X08 | 81 | Factorio formula is a 2016 development example, not every 2026 technology. | Version-tag. |
| X09 | 89 | Diablo observations are developer-reported, not controlled measurements. | Label as EXPERIENCE. |
| X10 | 95 | WoW Warbands is a preview; not every detail stayed. | Label as preview. |
| X11 | 115 | Clash Royale coordination does not prove fair matchmaking or a fixed time-to-max. | No time-to-max claim. |
| X12 | 119 | LoL mastery is the January 2024 proposal, not final or current rules. | Label as proposal. |
| X13 | 131 | TFT match-economy numbers must not be copied into a persistent simulator. | Do not transfer the numbers. |
| X14 | 135 | Overwatch minutes per level are not published. | No minutes figure. |
| X15 | 143, 145 | Mario Wonder is an analogue, not a persistent XP economy; no unlock timeline or completion-time benchmark. | No timeline claim. |
| X16 | 149 | The cases do not conflict on one formula; they serve different jobs. | Do not rank studios. |
| X17 | 160 | No verified enjoyment uplift, churn effect size or universal minutes-to-first-prestige; official sources cannot show causality. | State this limit in the skill. |
| X18 | 41; lookup 351 | Rule 10 cites H02 and H03; the paper's own later note (outside range) calls their disagreement important. Inside the range the two are cited together without saying they disagree. | Say both exist; claim neither "all help" nor "all harm". |
| X19 | 174 | The vocabulary (fast start ... catch-up) is the paper's operational wording, not industry standard terms. | Define in the skill; do not call it standard. |
| X20 | 184, 186 | Timeline checkpoints are planning intervals, not completion-time targets; calendar age is not active play; feelings are candidates, not research results. | Keep targets blank until measured. |
| X21 | 210 | n = 0, 1, 2 sampling is not a level-count prescription. | Do not read sample values as design values. |
| X22 | 208 | Curve numbers are historical examples, not 2026 Roblox tuning. | No default constants. |

## 11. Possible issues (extractor), not fixed (d)

| ID | PP | Item | Why it looks off |
| --- | --- | --- | --- |
| Z01 | 55 vs 163 | Benefits count: PP:55 lists six (capability, choice, understanding, expressive ownership, access, recognizable accomplishment); the rule table at PP:163 lists five (capability, choice, understanding, access, accomplishment) and omits "expressive ownership". | (extractor) possible issue. Unclear whether the table shortens the list or the list grew. |
| Z02 | 127 | TFT: the five listed XP requirements sum to 268 (20+36+48+80+84); published totals are 228 -> 288. 288 - 268 = 20 would have to come from requirements before level 5, which the paper does not list; the old per-level values (needed to see 228) are also not listed. | (extractor) possible issue. Not checkable from the paper alone; fact-check against C09. |
| Z03 | 69 vs 734 | C01 later date: PP:69 says "2017-02-01 syndication"; the register (PP:734) says "author republication 2021-07-30" and gives the sirpinski.com provenance. Two different later dates for the same source, not reconciled. | (extractor) possible issue. May be two different re-posts; the register does not name the syndication host or date source. |
| Z04 | 15 vs 208, 210, 223 | VERIFIED is defined (PP:15) as a source publishing the rule/number or a study measuring an effect. PP:208 and 223 also use VERIFIED for the paper's own arithmetic, with the paper (O00) as the only source. Also R02 (PP:25) and R10 (PP:41) are tagged VERIFIED though they read as method statements, and R06/R09 are tagged EXPERIENCE though they read as prescriptions. | (extractor) possible issue. Tag meaning shifts; skill text should not turn paper-derived math into "source-verified". |
| Z05 | 111 | Clash Royale "December 4" has no year, and the phrase "announced December 4 ranked caps" does not say whether Dec 4 is the effective date or the announcement date. I read it as effective date, year 2023 from the C07 date 2023-11-30 and the "In November" wording. | (extractor) possible issue. Fact-check against C07. |
| Z06 | 103 | Hearthstone: "nearly 20%" is not attributed (Blizzard, or the paper's own calculation) and no pre-correction total is given. "50 gold per level from 51 onward" does not say whether levels past 50 are the bonus levels. | (extractor) possible issue. Fact-check against C05. |
| Z07 | 87 | Diablo IV: "level-earned Paragon points raised from 200 to 300" could be a points cap or a level cap; the paper's wording is kept here. | (extractor) possible issue. Fact-check against C03; the lead flagged 200 -> 300 as a key figure. |
| Z08 | 119 | LoL: "four per-split milestones, then a repeating milestone" is unexplained (what a milestone grants, what a split is). Marks per level are given only for levels 1-4, 5-9 and 10+. | (extractor) possible issue. Fact-check against C08. |
| Z09 | 135 | Overwatch: "every 20 hero levels" (borders), "milestone at 60" (which milestone is not said) and "flattens at 20" are three separate numbers; the paper does not say how the border cadence and the flattening relate. | (extractor) possible issue. Fact-check against C10. |
| Z10 | 143 | Mario Wonder: "six worlds around the Petal Isles, seven areas in total" may mean six worlds plus the Petal Isles hub; the paper does not say. | (extractor) possible issue. Low risk; check C11. |
| Z11 | 69, 73, 77 | Prestige symbols: cL (lifetime earnings) and cM (maximum earnings) are used as single symbols; the "c" prefix is never explained, and no domain or unit for p, cL, cM is given. | (extractor) possible issue. Defined here as the paper defines them; do not rename. |
| Z12 | 215-221 | Curve domains incomplete: no domain for b in CV3; a in CV5; a and b in CV6 and CV7; any parameter in CV8; base(n), m_i, K_i in CV9. CV9's bracket [n >= K_i] is undefined. CV3 uses capital F, others use f. CV8 and CV9 sample cells are not values ("Depends on K"; "Evaluate against actual K_i"). | (extractor) possible issue. Check C2: samples for CV8 and CV9 exist only as my conditional derivations (section 6.1). |
| Z13 | 210 vs 223 | Index origins differ: curves use n >= 0; the XP derivation starts at level 1 (X_1 = 0); Factorio counts l from 6 with exponent l - 6; TFT names transitions as 5>6 etc. The paper's own R05 says to state index origins. | (extractor) possible issue. Always carry the origin when quoting a formula. |
| Z14 | 65-145 | Case numbers (1-12) and source ids (C01-C11) differ: Case 4 = C02, Case 5 = C03 ... Case 12 = C11, with Cases 1-3 all C01 and Case 8 using C06 + C07. | (extractor) possible issue (confusion risk only). Use the 4.0 index. |
| Z15 | 17 | The "two worked examples" are outside this range and cannot be located from lines 1-230. | (extractor) not checkable here. |
