---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: "J014-T01, live-ops-designer-research.txt lines 1-247"
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-21

# Live-ops paper part 1: mandate and evidence contract, 15 rules, durable games and ten studied games, update rhythm and production economics, content types, events and event design template, deciding what comes next and ranked update plan template (lines 1-247)

Paraphrased notes. The paper (LP) stays outside git. Every row cites `LP:<line>`. Nothing here is fact-checked: claims are the paper's, listed in section 10 for the fact-check pass. The paper's research cutoff is 2026-10-21. Several of its sources are dated mid-2026 or later (R11, G07, G14, G15, G19, G20), and many Roblox rules come from undated live documents read on the cutoff day, so none can be confirmed from memory: check them live. The paper is strong evidence, not gospel: its own limits sit next to the claims they limit and are collected in section 11. Extraction only: no web access was used. The paper's later parts (LP:248 onward: feedback, experiments, analytics and so on) are not in this note.

## 0. How to read

| Key | Meaning |
| --- | --- |
| LP:n | line n of `live-ops-designer-research.txt`. One paragraph, table row or template field = one line. Source register = LP:537-749 (only entries cited in lines 1-247 are resolved here, section 9). |
| Tag | The paper's own mark, copied unchanged. VERIFIED = an official source establishes a platform capability, rule, release date, schedule or a specifically reported measurement; an official announcement verifies what was announced, not that an intervention caused growth (LP:11). EXPERIENCE = a developer's account, interpretation, production lesson or explanation of results; useful, but not a controlled experiment (LP:12). OPINION = the paper's proposed operating rules, hypotheses, templates and analytical deductions; recommendations, not measured facts (LP:13). "none" = a definition or framing line the paper does not tag. |
| Mixed-tag lines | Inside OPINION templates the field names and instructions inherit OPINION (LP:15). Where one line carries several tags, each row copies the tag of its own sentence. Where a table cell has no tag of its own (event-type column, section 3.2) the row says so. |
| Kind (my label) | RULE = official rule, limit or eligibility. MECH = documented platform behavior. CASE = reported outcome or schedule of a named game. PROC = the paper's proposed procedure or advice. LIMIT = a caveat the paper states. FRAME = framing, definition or role text. The paper itself uses only Tag. |
| Src | The paper's source id, resolved in section 9 with date and URL. R = Roblox documents and posts (R01-R22 in the register). G = game studios and conference evidence (G01-G30). "undated; checked 2026-10-21" = a live document that shows no reliable date (LP:15); it was read that day, not published that day. |
| Row IDs | MD mandate, EC evidence contract, RU rule, DU durable-games principle, CS studied game, EB evidence behind patterns, RH rhythm, CT content type, EVT event, ET event-template field, DN decision step, UP ranked-plan template part, N number, FC claim to check, X contradiction or limit. Written with a hyphen (RU-01). Source ids (G01) and row ids (CS-01) never overlap. |
| Terms | KPI = key performance indicator. MAU = monthly active users. DAU = daily active users. CCU = concurrent users. QoL = quality of life. QA = quality assurance. "Content cadence" = releases that build only on existing systems (register quote for R01), as opposed to an expansion. |
| Post-cutoff | Source dated after 2026-06-01 (the studio's flag). Undated live documents are marked "live-read": read on 2026-10-21 by the paper, they may have changed since. "indexed" = the paper read only indexed official text or excerpts (register note). |
| Priority (section 10) | P1 = a Roblox rule or capability; any cadence claim; any event or update effect (including side effects); any number or percentage. P2 = a case date or schedule with no other number. P3 = framing, or a qualitative case statement. |
| Rule of use | OPINION rows are proposed checks, never Roblox policy. Never write "Roblox requires X" from an OPINION row. A case result is one game's report, never a benchmark. Tags do not carry over between papers: this paper counts a first-party reported measurement as VERIFIED (LP:11), which another paper in this kit may not (X-23). |

## 1. Mandate and evidence contract (LP:1-17)

| ID | LP | Kind | Content | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| MD-01 | 1, 3 | FRAME | Paper: training an AI live-ops designer for a small Roblox studio. Research cutoff 2026-10-21. Audience: an AI agent advising a studio owner / creative director after launch. | none | - |
| MD-02 | 7 | FRAME | Role: the live-ops designer owns the argument for what the game does next. It combines the analyst's results, player feedback and the trend scout's findings into alternatives, explains the trade-offs, asks the owner to decide and writes an executable handoff. | OPINION | - |
| MD-03 | 7 | LIMIT | The designer must not silently become the creative director, invent the analyst's conclusions, or commit builders and marketing to unapproved work. The owner chooses. | OPINION | - |
| MD-04 | 7 | FRAME | Split of work: game design specifies play; progression design specifies rewards and economy; builders estimate and implement; marketing communicates; the analyst evaluates outcomes. | OPINION | - |
| EC-01 | 11 | FRAME | VERIFIED = an official source establishes a platform capability, rule, release date, schedule or specifically reported measurement. An official announcement proves what was announced, not that an action caused growth. | none | - |
| EC-02 | 12 | FRAME | EXPERIENCE = a developer's account, interpretation, production lesson or explanation of results. First-party experience is useful but not a controlled experiment. | none | - |
| EC-03 | 13 | FRAME | OPINION = this paper's proposed operating rules, hypotheses, templates and deductions. Recommendations for the agent, not externally measured facts. | none | - |
| EC-04 | 15 | FRAME | Every paragraph or table row with a substantive claim carries a label. Inside explicitly labeled OPINION templates, field names and instructions inherit the label. | none | - |
| EC-05 | 15 | FRAME | Source ids resolve to a dated register that gives a short exact quote and a URL. | none | - |
| EC-06 | 15 | LIMIT | "Undated; checked 2026-10-21" means a live document showed no reliable publication or update date. It does not mean it was published on the research date. | none | - |
| EC-07 | 15 | LIMIT | Historical examples stay dated examples, not promises about current game schedules. Approximate figures keep the source's qualifier. Unknown does not mean zero. | none | - |
| EC-08 | 17 | PROC | Keep evidence as an auditable record with ten fields: claim, source, date, population, time window, metric definition, intervention, comparison, uncertainty, decision relevance. Never turn visits into unique players, peak concurrency into retention, event attendance into returning-player rate, gross spend into studio profit, or a release interval into development time. | OPINION | - |

## 2. The fifteen rules (LP:19-35)

Rule n sits at LP:20+n. A VERIFIED mark covers the platform or source fact, not an outcome. Detail for each rule is in the section named in the last column.

| ID | LP | Rule in my words | Tag | Src | Detail in |
| --- | --- | --- | --- | --- | --- |
| RU-01 | 21 | Optimize the durable value of returning to the core game. The owner approves the update, its scope and the accepted trade-offs. | OPINION | - | DU-01, DN-01 |
| RU-02 | 22 | Roblox cadence guidance depends on context: monetization guidance calls weekly ideal; content guidance says many games ship every two weeks to one month. | VERIFIED | R02, R04 | RH-01, RH-02, FC-01, FC-02 |
| RU-03 | 23 | Adopt Me changed its weekly schedule after 56 consecutive weeks, citing team wellbeing. A calendar promise can outgrow production capacity. | EXPERIENCE | G01 | CS-01, EB-01, FC-13 |
| RU-04 | 24 | Fix a verified blocker in the existing game before paying for attention to more content players cannot enjoy. | OPINION | - | DN-01 |
| RU-05 | 25 | A documented Adopt Me festival ran 4 weeks with weekly additions. An event can hold several beats without several new systems. | VERIFIED | G02 | EB-02, EVT-05, FC-14 |
| RU-06 | 26 | Fortnite's November 2023 record reported over 44.7 million players and 102 million hours. Neither figure is a return rate. | VERIFIED | G05 | EB-08, EB-09, FC-17 |
| RU-07 | 27 | Brawl Stars reported that a highly visible collaboration coincided with falling revenue and MAU. Attention is not evidence of healthy retention. | EXPERIENCE | G10 | EB-16, FC-26 |
| RU-08 | 28 | Count distinct feedback authors inside each sampling channel. Never describe Discord message share as the percentage of all players who agree. | OPINION | - | outside this note (feedback part, LP:248+) |
| RU-09 | 29 | Roblox's event-impact comparison is observational. Its native experiments give randomization and run for 14-60 days. | VERIFIED | R09, R10 | FC-04, FC-05, X-15 |
| RU-10 | 30 | Fix the target cohort, primary outcome, guardrails, comparison and decision window before shipping. | OPINION | - | ET-17, ET-18, DN-03 |
| RU-11 | 31 | Roblox paid-random-item rules cover indirect Robux purchases and require final-outcome probabilities to total exactly 100%. | VERIFIED | R14 | FC-10 |
| RU-12 | 32 | Current experience / community social-link guidance uses age-checked 16+ eligibility; personalized experience notifications use 13+ eligibility. They are different features. | VERIFIED | R08, R16 | FC-11, FC-12 |
| RU-13 | 33 | Give returning players an understandable next action and a viable route back. Do not make absence an accumulating punishment. | OPINION | - | EVT-03, CT-04 |
| RU-14 | 34 | Reserve implementation, QA, moderation, support and rollback capacity before promising an external date. | OPINION | - | RH-13 |
| RU-15 | 35 | After release choose repeat, revise, retire or investigate. "Insufficient evidence" is a valid conclusion; do not invent a win. | OPINION | - | ET-23 |

## 3. What great live operations are, and the ten studied games (LP:37-96)

### 3.1 Principles (LP:39-41)

| ID | LP | Kind | Content | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| DU-01 | 39 | FRAME | Great live operations keep a renewable relationship between player and game. Players need a reason to return, an understandable way to take part, a satisfying arrival, and confidence that their investment still counts. Novelty brings attention; reliable play, fair progression, social ties and a credible future turn it into continued play. The update is a means to that relationship, not the product metric. | OPINION | - |
| DU-02 | 41 | PROC | Games fade when: novelty hides a weak core loop; acquisition sends players into unresolved friction; new content is out of reach for most; progression is exhausting; complexity makes returning costly. Other causes: competition, seasonal demand, discovery changes, technical regressions. Never diagnose "not enough content" from a falling DAU chart alone. | OPINION | - |
| DU-03 | 41 | LIMIT | A mature game need not maximize release frequency. A stable competitive meta, a creative sandbox or a social collection can hold value between large releases. | OPINION | - |

### 3.2 Ten studied games (LP:45-58)

| ID | LP | Kind | Content | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| CS-00 | 45 | LIMIT | The "rhythm" and "event" columns are described as source-grounded; the "learn" and "do not copy" columns are the paper's recommendations. The ten cases were chosen for useful operating patterns, not as a causal ranking of the industry's best games. Public evidence is especially thin for exact update-induced retention, returning-player percentages and person-days per release. | OPINION | - |

Columns below: rhythm evidence is as tagged by the paper inside the cell. The event-type cell has no tag or source of its own (see X-21, FC-42). "Learn" and "Do not copy" are OPINION (header, LP:47).

| ID | LP | Game | Rhythm evidence and date (paper's tags) | Event types / operating pattern (no own tag) | Learn [OPINION] | Do not copy [OPINION] | Src |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CS-01 | 49 | Adopt Me | EXPERIENCE: weekly run changed after 56 weeks, in 2020. VERIFIED: 4-week festival in 2025. | Collection additions, themed minigames, event currency, weekly festival beats | Reuse the collection fantasy; test technical and social side effects | A permanent weekly obligation; rewards that encourage unwanted social behavior | G01, G02 |
| CS-02 | 50 | Roblox BedWars | VERIFIED: the public experience description advertises Friday updates; checked 2026-10-21. | Competitive modes; a visible weekly appointment | Make the next reason to play understandable and predictable | Assuming the public cadence reveals team size, update cost or retention lift | G04 |
| CS-03 | 51 | Fortnite | VERIFIED: OG began 2023-11-03 and refreshed historical content during the month. | Nostalgia, changing loot / map eras, seasonal spectacle | Reactivation can start from familiar identity and shared memories | Celebrity / IP budgets, infrastructure scale or peak attendance as a retention target | G06 |
| CS-04 | 52 | League of Legends | VERIFIED: the 2026 schedule includes October 7 and October 21; generally fortnightly with exceptions. Arena balances on alternating odd-numbered patches. | Balance, thematic seasons, event progression | Keep competitive trust while giving strategies time to develop | Balancing everything every time; copying a large team's content load | G07, G30 |
| CS-05 | 53 | Teamfight Tactics | VERIFIED: shift to 3 sets per year. EXPERIENCE: a 2025 retrospective describes the cost of abbreviated testing. | New sets, traits, units, seasonal rediscovery | Renew the strategic possibility space; protect testing time | Treating a new set as a cheap reskin; treating a collaboration date as permission to skip QA | G08, G09 |
| CS-06 | 54 | Brawl Stars | VERIFIED: monthly passes beginning on the first Thursday; a 2026 review reports outcomes and production trade-offs. | Brawlers, modes, collaborations, ranked refreshes, passes | Judge novelty, progression and competitive health together | An overpowered promotional character; marketing reach as proof of product success | G10, G11 |
| CS-07 | 55 | Genshin Impact | VERIFIED: a historical version notice specifies 6 weeks; 2026 version notices give dated release evidence. | New exploration / story content, characters, time-limited events | Pair a durable world with bounded reasons to revisit | Assuming a small studio can match its production throughput or monetization context | G13, G14, G15 |
| CS-08 | 56 | Overwatch | VERIFIED: a 2022 plan specified 9-week seasons; the 2026 plan connects seasons 1-6 into an annual story. | Heroes, modes, seasonal narrative, returning-player orientation | Give updates a coherent direction and explain what changed | Treating the historical interval as a verified permanent 2026 contract | G16, G17 |
| CS-09 | 57 | Dota 2 | VERIFIED: the dated update feed shows irregular large changes and smaller follow-ups; 2026 event fixes adjust rewards and usability. | Gameplay refreshes, events, reward corrections | Protect the underlying match experience; repair event friction | Demanding an identical monthly content package regardless of readiness | G19, G20 |
| CS-10 | 58 | Minecraft | EXPERIENCE: Mojang announced several free drops of varying size instead of a single annual summer update. | Sandbox additions, test builds, community-informed refinements | Smaller coherent releases can coexist with longer-term work | Adding disconnected mechanics only to fill a calendar | G21 |

Extractor grouping by what kind of cadence evidence each case gives (my label; not in the paper; the paper does not compare these as one scale):

| Evidence type | Games | Note |
| --- | --- | --- |
| Roblox-native games | CS-01 Adopt Me, CS-02 BedWars | Only these two (plus the Uplift case study, EB-03) are Roblox evidence; the other eight are not Roblox games (X-25). |
| Fixed public appointment | CS-02 BedWars (Friday), CS-04 LoL (fortnightly, with exceptions), CS-06 Brawl Stars (first Thursday monthly) | Each states a date rule. LoL schedule is subject to change (G30). |
| Interval given for a past plan | CS-01 Adopt Me (weekly, ended after 56), CS-07 Genshin (6 weeks, 2022), CS-08 Overwatch (9 weeks, 2022) | Historical intervals; the paper says not to treat them as current contracts (EB-24). |
| Structure per year | CS-05 TFT (3 sets per year), CS-08 Overwatch 2026 (annual arc, seasons 1-6) | Annual packaging rather than a fixed interval. |
| Variable or irregular | CS-09 Dota 2 (irregular), CS-10 Minecraft (varying-size drops) | Cadence follows readiness. |
| Event-structured window | CS-01 festival (4 weeks), CS-03 Fortnite OG (a month of phases) | Event length is a design choice, no optimum (EVT-06). |
| Date arithmetic (mine, not the paper's) | LoL 2026-10-07 to 2026-10-21 = 14 days; Genshin 2026-08-12 to 2026-09-23 = 42 days = 6 weeks | The paper says release evidence is not development duration (EB-21); G15 has no independent publication timestamp. |

### 3.3 Evidence behind the patterns (LP:60-88)

| ID | LP | Kind | Content | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| EB-01 | 62 | CASE | Adopt Me's 2020 schedule change explicitly tied production rhythm to team wellbeing. | EXPERIENCE | G01 |
| EB-02 | 62 | CASE | The 2025 Cherry Blossom Festival ran April 4 to May 2, with weekly additions. | VERIFIED | G02 |
| EB-03 | 62 | CASE | In Roblox's August 2026 case study, Uplift described tests of trading-hub server size and matchmaking. A friend-related currency incentive led to spam friend requests and avoidance of private servers; a summer decorative-fish change caused performance problems. Neither gives a controlled retention lift. | EXPERIENCE | R11 |
| EB-04 | 64 | PROC | For a small collection game: separate the reusable festival structure from its weekly reward and content beats, and test the social behavior a reward actually induces. A "social" feature can make play less social. A visually minor addition can become the main reason an update fails on weak devices. | OPINION | - |
| EB-05 | 66 | CASE | BedWars' official experience listing gives a concrete weekly Friday promise. It does not disclose staffing, testing time, revenue effect or the share of players who return because of it. | VERIFIED | G04 |
| EB-06 | 66 | PROC | Copy the clarity of the appointment only after measuring your own studio's ability to keep it. Competitive updates also need a stable version and readable change explanations. | OPINION | - |
| EB-07 | 68 | CASE | Epic's OG announcement spread returning historical content across November 2023. | VERIFIED | G06 |
| EB-08 | 68 | CASE | Epic later reported over 44.7 million players and 102 million hours for November 4. | VERIFIED | G05 |
| EB-09 | 68 | LIMIT | These are strong scale observations but weak causal evidence: the counterfactual audience and the share of truly reactivated players are not reported. A Roblox analogue is a recognizable earlier area, mode or collection with better access, not a promise of Fortnite-like growth. | OPINION | - |
| EB-10 | 70 | CASE | Riot's 2026 Arena notes say some balance work happens on alternating patches because excessive adjustment can stop players discovering strategies. | EXPERIENCE | G07 |
| EB-11 | 70 | PROC | Tell a demonstrably oppressive mechanic from ordinary unfamiliarity. Stable discovery time is a design resource. Balance after a trend report should rest on match outcomes and available counters, not on the latest viral complaint. | OPINION | - |
| EB-12 | 72 | CASE | TFT's move to 3 sets per year is a production model for renewing strategic depth. Its Into the Arcane retrospective reports that a shorter test period, tied to the show's timing, worsened balance and bugs. | EXPERIENCE | G08, G09 |
| EB-13 | 72 | PROC | Small studios can borrow the bounded strategic refresh with far fewer assets. They cannot infer the labor needed from the gap between set launches. | OPINION | - |
| EB-14 | 74 | CASE | Riot's earlier TFT retrospective: adding a few champions every couple of weeks changed sentiment and playtime almost not at all; bundling changes into a bigger moment created heavy workload. No exact effect size is given. | EXPERIENCE | G08 |
| EB-15 | 74 | LIMIT | Direct counter-evidence to "more frequent automatically means more engaging". Meaningful novelty and production feasibility both matter. | OPINION | - |
| EB-16 | 76 | CASE | Supercell's March 2026 Brawl review: the Buzz Lightyear work equaled 3 Brawlers, produced videos with 40,000,000+ views, and was followed by revenue and MAU falling "around 20%" from December 2024 to February 2025. The review describes gameplay disruption, not a controlled causal estimate. | EXPERIENCE | G10 |
| EB-17 | 76 | CASE | Ranked first produced mid-trophy playtime 27% above its March 2024 peak, then normalized. | EXPERIENCE | G10 |
| EB-18 | 76 | CASE | A separate February 2026 update described a Mega Quest cadence test: 80% of players on monthly quests, 20% on weekly quests. No outcome was supplied. | VERIFIED | G12 |
| EB-19 | 78 | PROC | Brawl rejects two shortcuts: fame does not show healthy play, and an early gain does not show durability. A Roblox studio should price a temporary feature against what the same effort could improve for good. A small, understandable experiment can beat a big collaboration. | OPINION | - |
| EB-20 | 80 | CASE | HoYoverse explicitly described Version 2.7 as expected to last 6 weeks, in 2022. | VERIFIED | G13 |
| EB-21 | 80 | CASE | 2026 notices identify updates on August 12 and September 23. They are release evidence, not a disclosure of development time or causal retention. | VERIFIED | G14, G15 |
| EB-22 | 80 | PROC | Transferable pattern: durable progression plus temporary invitations. Do not borrow a character-release treadmill without the budget, audience and economy that make it viable. | OPINION | - |
| EB-23 | 82 | CASE | Blizzard's 2026 Overwatch announcement describes a connected annual arc and returner-facing explanations of changes. | VERIFIED | G17 |
| EB-24 | 82 | PROC | A coherent story makes separate patches legible. Returning players need orientation before another mission list. The 9-week season promise is context, not proof that every later season lasted exactly that long. | OPINION | G16 |
| EB-25 | 84 | CASE | Dota's 2026 event corrections include paying Scrap whether the player wins or loses, and clearer reward information. | VERIFIED | G20 |
| EB-26 | 84 | PROC | In a competitive game, reward structures can encourage frustration or selfish play. Reward participation that helps the match, check for abuse, explain reward conditions. A pass existing is no reason to neglect players outside it. | OPINION | - |
| EB-27 | 86 | CASE | Mojang described smaller free drops and changes shaped by community testing, including refinements to new creatures. | EXPERIENCE | G21 |
| EB-28 | 86 | PROC | Incremental releases work when each adds to a coherent game and the studio keeps capacity for deeper changes. Smaller is not inherently better than a big expansion; it moves coordination and attention costs. | OPINION | - |
| EB-29 | 88 | CASE | GDC 2022 abstract of Justin Truman's Destiny talk frames live service as a change in prioritization, organization and decision-making. Only the abstract was reviewed, not the talk. | EXPERIENCE | G25 |
| EB-30 | 88 | PROC | For an AI studio: release planning, incident response and learning must be continuous duties, not steps added after development ends. | OPINION | - |

The table at LP:90-96 is in the number register (N-01 to N-05).

## 4. Update rhythm: cadence, size and production economics (LP:98-127)

| ID | LP | Kind | Content | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| RH-01 | 100 | RULE | Roblox monetization guidance calls weekly updates ideal and monthly updates a minimum. | VERIFIED | R04 |
| RH-02 | 100 | RULE | Roblox content-update guidance describes many games releasing every two weeks to one month, and recommends under three weeks of effort for content-cadence work. | VERIFIED | R02 |
| RH-03 | 100 | RULE | Roblox live-ops essentials separate content cadence on existing systems from expansions that can take many months. | VERIFIED | R01 |
| RH-04 | 100 | LIMIT | These are contextual design recommendations, not platform rules, controlled comparisons or guaranteed discovery boosts. "Monthly minimum" is not a reason to ship an unfinished update each month. | OPINION | - |
| RH-05 | 102 | PROC | Choose rhythm from four constraints, read separately: (1) how fast the target audience uses up meaningful content; (2) how often its natural play routine opens a return chance; (3) how much change the game can absorb without confusion; (4) how reliably the team can build, verify and support it. More builder time does not show players want more tasks. An exhausted endgame cohort does not show new players need another progression system. | OPINION | - |

Candidate rhythm menu (LP:104-110; header marks the table OPINION):

| ID | LP | Rhythm | Suitable scope | Main benefit to test | Main cost to include |
| --- | --- | --- | --- | --- | --- |
| RH-06 | 106 | Weekly | Variants of existing systems, rotating challenges, small reward drops, targeted fixes | Predictable return appointment; fast correction | Repeated QA, communication, support, context switching |
| RH-07 | 107 | Every two weeks | A bounded content package or several related improvements | A more complete, legible change | Still easy to overcommit if every release adds a system |
| RH-08 | 108 | Monthly | A substantial area, coherent feature package or prepared event | More meaningful novelty; clearer marketing | Longer wait before a struggling cohort gets help |
| RH-09 | 109 | Seasonal | A themed umbrella over several releases | Coherent goals; a recognizable return moment | Expiry pressure, catch-up complexity, big integration risk |
| RH-10 | 110 | As needed | Security, data-loss, exploit or severe stability fixes | Stops harm quickly | Must not excuse poorly tested routine releases |

| ID | LP | Kind | Content | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| RH-11 | 112 | PROC | The menu is not a benchmark. Suggested start for a small studio: a stable existing-system content lane, a separately scoped improvement lane, and emergency capacity. Pick the exact cadence only after estimates and consumption evidence exist. One patch may carry content and fixes, but each needs its own hypothesis and evaluation. Do not create parallel lanes if the same constrained builder must do everything in sequence. | OPINION | - |
| RH-12 | 114 | PROC | Ask builders for elapsed lead time and active effort separately. Cover: concept approval, design, art, code, integration, device testing, progression simulation, localization, moderation / eligibility checks, announcement preparation, rollout, support. Reused code cuts some costs, not all. An AI-generated asset still needs integration and verification. Dependencies and review queues can dominate elapsed time. | OPINION | - |
| RH-13 | 116 | PROC | Planning constraint: committed work must fit the capacity left after committed maintenance and release support. Use measured past throughput if there is any; otherwise take an estimate range and label confidence. Do not invent a universal percentage buffer or claim "AI can build this in a day". If estimates exceed the window: cut scope, reuse a validated pattern, move the date, or cancel. Unmeasured parallel agents are not a capacity estimate. | OPINION | - |
| RH-14 | 118 | PROC | Small updates shrink each failure and teach faster, but repeated release overhead can eat the saving. Large updates give an easier return reason and can fix structural problems, but bundle risks and blur attribution. Compare a bundle with its smallest useful alternative. An empty weekly reskin can be worse than a useful monthly change; a large expansion cannot stand in for a broken purchase fix. | OPINION | - |
| RH-15 | 120 | CASE | Minecraft's variable-size drops and Adopt Me's schedule change support flexibility; BedWars' public weekly appointment shows predictability. None of them shows a single optimum. | EXPERIENCE | G01, G04, G21 |
| RH-16 | 120 | PROC | Settle the apparent disagreement by asking what each game's production system and player promise can sustain. Keep a public cadence only when a credible minimum meaningful release stands behind it. | OPINION | - |

The table at LP:122-127 is in the number register (N-06 to N-09).

## 5. Types of live content (LP:129-159)

| ID | LP | Kind | Content | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| CT-00 | 131 | PROC | Pick a content type only after naming the player problem and the behavior wanted. "Add a season" names packaging, not a hypothesis. Revenue can rise because more players arrive, more become payers, payers spend more, or purchases are pulled forward from later; each has different durability and trust effects. No reviewed source gives a portable percentage lift for any content type across Roblox genres. | OPINION | - |

Content-type table (LP:133-142). Columns 2-4 carry the OPINION mark in the header.

| ID | LP | Content type | Hypothesized player job and outcome | What to measure | Failure mode |
| --- | --- | --- | --- | --- | --- |
| CT-01 | 135 | Areas, quests, story | Give progressed players a meaningful next destination; invite lapsed players back | Eligibility, reach, completion, return after completion, development cost | New content exists but most players cannot reach it |
| CT-02 | 136 | Items, pets, characters, equipment | Widen expression, collection or strategic choice | Adoption and continued use, collection goals, spending displacement, balance | Inventory bloat; strictly better purchases; old rewards made worthless |
| CT-03 | 137 | Limited-time modes | Temporary novelty and social play with no commitment to permanence | Participation among eligible players, repeat sessions, displacement of the core mode, queue health | Split matchmaking; an event unrelated to the game's appeal |
| CT-04 | 138 | Seasonal goals and passes | Make progress readable across repeated visits | Start / finish / drop-off by cohort, rewards earned, payer and non-payer health | Homework; missed-day penalties; rewards that need unhealthy play |
| CT-05 | 139 | Collaborations and holiday themes | Create recognition and a shared moment | Qualified acquisition, reactivation, later core play, incremental margin | Licensed spectacle swamps the game, or expires before costs are recovered |
| CT-06 | 140 | Balance changes | Keep competition fair and strategy varied | Outcome distributions by skill and context, pick / use patterns, counterplay, sentiment | Reactive nerfs destroy learning or hide the real problem |
| CT-07 | 141 | Quality of life and accessibility | Remove repeated friction; widen practical access | Task success, abandonment, device performance, support incidence | Low visibility makes a useful fix look like "no content" |
| CT-08 | 142 | Bug, exploit, stability fixes | Restore the intended game and economy | Error / crash rate, failed rewards / purchases, affected cohorts | Shipping new monetization while known damage continues |

| ID | LP | Kind | Content | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| CT-09 | 144 | RULE | Roblox season-pass guidance suggests one month as a starting point, at least a one-week rest between seasons, and ten tiers as an initial design. These are suggestions, not validated completion or revenue targets. | VERIFIED | R05 |
| CT-10 | 144 | PROC | Size a real pass from observed session opportunities and progression rates; model late starters and low-frequency players explicitly. A large tier count can add admin work without adding meaningful play. | OPINION | - |
| CT-11 | 146 | CASE | Blizzard's current Hearthstone expansion page lists March, July and October releases for 2026. Its April 2026 announcement describes Class Sets replacing Mini-Sets: 4 classes per wave, 3 planned waves. | VERIFIED | G22, G23 |
| CT-12 | 146 | PROC | These show packaging being revised. For Roblox: revisit packaging when the old one stops serving players; do not bolt a second pass onto the first just because another game has one. | OPINION | - |
| CT-13 | 148 | CASE | Supercell's May 2026 Clash Royale announcement says progression should be simpler and clearer, and describes changes that keep or raise existing King Tower level. | EXPERIENCE | G24 |
| CT-14 | 148 | PROC | An improvement update can be a major product event. When replacing progression, explain the migration before urging players to invest more in the old system. | OPINION | - |
| CT-15 | 150 | CASE | Bungie's May 2025 roadmap described 2 paid expansions and 2 free major updates. It is a dated plan, not proof of later execution or a fixed 2026 schedule. | VERIFIED | G26 |
| CT-16 | 150 | PROC | Keep substantial paid value apart from the ongoing health work everyone needs. A small Roblox studio should not put basic usability or an exploit fix behind a paid seasonal product. | OPINION | - |
| CT-17 | 152 | PROC | Remove content when its harm exceeds its maintained value: broken queue population, confusing duplicate systems, exploit surface, disproportionate support cost. Before removal check active use, paid entitlements, downstream dependencies and an alternative path for affected players. Retirement is a design and communication project; announcing a removal is not a safe migration. | OPINION | - |

The table at LP:154-159 is in the number register (N-10 to N-13).

## 6. Events (LP:161-210)

| ID | LP | Kind | Content | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| EVT-01 | 163 | MECH | Roblox separates temporary events from permanent updates and notes that an event can move several KPIs at once. | VERIFIED | R03 |
| EVT-02 | 163 | FRAME | Define an event as a temporary player proposition with an entrance, a repeatable activity, a progression / reward structure and a stated end. A decorative lobby is a theme; a shop discount is an offer. Either can support an event; neither alone gives a satisfying reason to return. | OPINION | - |
| EVT-03 | 165 | PROC | Start with the intended audience: active players wanting variety, lapsed players needing a reason, new players needing an accessible start, or friends coordinating. Do not use one completion curve for all four without checking accessibility. A returner event must not demand every system added during the absence. A new-player event must not hide its core activity behind veteran progression. | OPINION | - |
| EVT-04 | 167 | PROC | Set duration from observed play opportunities, content exhaustion and operational coverage. Estimate required effort from reward costs and observed earning rates, keeping the distribution, not only the mean. Model late joiners, low-frequency players, device limits, missed days, skill differences. Completion must be possible through healthy participation; a path that needs near-perfect attendance fails. If the reward cannot fit the audience's routine: lower the requirement, extend the window, or add catch-up. | OPINION | - |
| EVT-05 | 169 | CASE | Adopt Me's cited festival lasted 4 weeks. Epic scheduled Remix: The Finale for November 30, 2024 at 2 PM ET. | VERIFIED | G02, G29 |
| EVT-06 | 169 | PROC | Two event shapes: a multiweek progression window versus a synchronized spectacle. Neither shows an optimal length. A small studio can usually support repeatable activities and scheduled reward beats better than a one-shot, high-concurrency spectacle. If synchronization is essential, plan an encore or an equally accessible route and rehearse the failure case. | OPINION | - |
| EVT-07 | 171 | PROC | Keep an event calendar with: game beat, theme, target cohort, content lock, test window, moderation / approval dependencies, communication dates, staff coverage, event end, reward-claim end, follow-up measurement dates. State time zones and show local player time where possible. Start from the audience's countries and routines, not assumed global holidays. Check school / exam patterns only from suitable aggregate evidence; never infer a child's personal schedule. | OPINION | - |
| EVT-08 | 173 | PROC | A trend qualifies only if: its core appeal fits the game; its useful life outlasts build-and-review lead time; audience overlap is credible; rights are available. "Popular this week" is not enough. Ask the trend scout for first-seen date, growth / decay evidence, relevant audience, source reliability, saturation and rights limits. Reusable mechanics under a broad seasonal theme are often safer than a rushed copy of a copyrighted character. | OPINION | - |
| EVT-09 | 175 | PROC | Ethical urgency = a true ending, clear consequences, a fair way to take part. Disclose which rewards expire, whether currency converts, whether a cosmetic may return, whether purchases speed progress. Avoid fake stock counters, resetting "last chance" timers, hidden requirements, coercive streak loss, and late purchase prompts for rewards the player cannot reasonably finish earning. Scarcity may define a shared moment, but permanent competitiveness must not depend on being present in a narrow window. | OPINION | - |
| EVT-10 | 177 | RULE | Roblox's notification policy specifically forbids deceptive pressure, including false time pressure. Its season-pass guidance discusses exclusivity as an incentive. | VERIFIED | R08, R05 |
| EVT-11 | 177 | LIMIT | Real design tension: a tactic Roblox discusses is not automatically right for younger players. The paper recommends truthful urgency and bounded effort. It does not claim that all limited-time content is banned by Roblox. | OPINION | - |

The table at LP:205-210 is in the number register (N-14 to N-17).

### 6.1 Event design template (LP:179-203), tag OPINION (field names and instructions inherit it, LP:15)

Twenty-three fields, in the paper's order. Each field is a blank to fill; the right column paraphrases the instruction in the brackets.

| ID | LP | Field | What goes in it |
| --- | --- | --- | --- |
| ET-01 | 181 | Event name / decision ID | Name and the decision record id. |
| ET-02 | 182 | Owner approval and version | Who approved, which version. |
| ET-03 | 183 | Player promise | One sentence. |
| ET-04 | 184 | Primary goal and target cohort | The one goal and who it is for. |
| ET-05 | 185 | Evidence | Analyst finding, feedback theme, trend report, with source dates. |
| ET-06 | 186 | Mechanism | Why this activity should change that cohort's behavior. |
| ET-07 | 187 | Core-game fit | Which existing fantasy, action or social relationship it reinforces. |
| ET-08 | 188 | Start / end / claim deadline / time zone | Explicit timestamps; no vague phrases such as "Sunday night". |
| ET-09 | 189 | Length rationale | Observed play opportunities and content-consumption evidence. |
| ET-10 | 190 | Eligibility and entrance | New, active, returning; device, region and policy limits. |
| ET-11 | 191 | Activity loop | Entry, then meaningful action, then feedback, then reward, then an optional next visit. |
| ET-12 | 192 | Calendar beats | What changes, when, and why each beat matters. |
| ET-13 | 193 | Rewards | Deterministic or random; free or paid; functional or cosmetic; tradable or bound. |
| ET-14 | 194 | Effort and catch-up | Observed earning distributions; paths for late starts and missed days. |
| ET-15 | 195 | Economy impact | Expected issuance, sinks, persistent inventory, expiry / conversion rules. |
| ET-16 | 196 | Monetization | Clear price and value; eligibility; odds where applicable; no assumed conversion lift. |
| ET-17 | 197 | Success | Primary metric, denominator, baseline, counterfactual, observation window. |
| ET-18 | 198 | Guardrails | Core retention, stability, fairness, economy, purchase / reward integrity, player pressure. |
| ET-19 | 199 | Production | Builder-approved estimates, reuse, dependencies, QA, support and moderation. |
| ET-20 | 200 | Communication | RSVP / event listing, announcement, in-game explanation, end reminders. |
| ET-21 | 201 | Failure plan | Disable path, safe reward handling, fallback activity, incident owner. |
| ET-22 | 202 | Exit | Cleanup, unclaimed rewards, persistent achievements, statement on future availability. |
| ET-23 | 203 | Decision after event | Repeat, revise, retire or investigate; the analyst's review date. |

## 7. Deciding what comes next: evidence to a ranked update plan (LP:212-246)

| ID | LP | Kind | Content | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| DN-01 | 214 | PROC | Use a decision sequence, not a weighted idea contest. First urgent harm: lost progress, failed purchases, safety problems, broken access, severe instability, exploitable currency issuance. Next the binding product constraint for the studio's current objective. Then the smallest intervention that might remove it. Only then do attractive new systems compete for capacity. | OPINION | - |
| DN-02 | 216 | PROC | "Fix the biggest drop-off first" needs care. Compare number affected, rate, cohort importance, plausibly recoverable share and cost of the fix. A big normal exit after a good session differs from an early failure. A small paid-entitlement failure can outrank a bigger cosmetic complaint. A funnel drop can come from changed instrumentation, a changed incoming audience, or an optional step. Get the analyst's denominator and observed behavior before naming a cause. | OPINION | - |
| DN-03 | 218 | PROC | Write hypotheses in one form: for a cohort, an observed problem blocks a valuable behavior; changing a specific cause should improve a metric through a mechanism, without harming guardrails. Tie each clause to evidence or mark it uncertain. Conditional example (not a diagnosis of any real game): if a verified early device failure drives abandonment, repair it before proposing an endgame event. | OPINION | - |
| DN-04 | 220 | PROC | Compare impact and effort without false precision. Impact = reach, plausible effect size, duration, strategic importance. Effort = all delivery and ongoing costs. Confidence = strength of evidence for the problem and the mechanism, not rhetorical certainty. When reach and effect are both measured, use eligible population times a justified incremental effect, carrying the uncertainty. When effect is unknown write "unknown; test required". Do not turn low / medium / high into invented decimals and rank on that. | OPINION | - |
| DN-05 | 222 | PROC | An impact-versus-effort matrix helps discussion but must not outrank mandatory fixes or dependency limits. Show a best-supported option, a cheaper useful alternative, and a reason to defer. With weak evidence, a small diagnostic or prototype may beat a full feature. Count opportunity cost: which maintenance, onboarding fix or event beat is displaced. Builders supply estimates; progression design supplies economic feasibility; the live-ops agent may assume neither. | OPINION | - |
| DN-06 | 224 | PROC | Add when the unmet need needs a new capability and the old game can absorb it. Improve when an existing system serves the need but access, usability, balance or depth falls short. Remove or consolidate when systems duplicate each other, split play, cost disproportionate upkeep, or undermine the intended experience. Keep valuable identity and entitlements when changing the route. A request for "more rewards" may really mean unclear progress, poorly matched rewards, or a missing social goal. | OPINION | - |

### 7.1 Ranked update plan template (LP:226-239), tag OPINION

| ID | LP | Part | Content |
| --- | --- | --- | --- |
| UP-01 | 228 | Header line (4 fields) | Decision period; studio objective; capacity verified by (who checked it); evidence cutoff. |
| UP-02 | 230 | Table columns (7) | Rank / status; candidate and player problem; evidence and uncertainty; impact and metric; effort / dependencies; accountable owner; decision requested. |
| UP-03 | 232 | Row type 1: urgent (if any) | Rank slot: "urgent if applicable". Problem: the specific harm and affected cohort. Evidence: measurement, reproducibility, source date. Impact: harm stopped, scope. Effort: builder estimate, safe mitigation. Owner: a named role or person. Decision requested: fix or mitigate now under agreed authority. |
| UP-04 | 233 | Row type 2: main candidate | Rank slot: a rank. Problem: a bounded update hypothesis. Evidence: analyst plus feedback plus trend evidence, with unknowns. Impact: reach, effect range only if justified, durable outcome. Effort: active effort, elapsed time, maintenance, risks. Owner: live-ops, design or build lead. Decision requested: approve scope and trade-off. |
| UP-05 | 234 | Row type 3: smaller alternative | Rank slot: a rank. Problem: a smaller alternative. Evidence: what it can and cannot test. Impact: same objective, smaller scope. Effort: verified estimate. Owner: owner. Decision requested: choose it instead, or reserve it. |
| UP-06 | 235 | Row type 4: defer / reject | Rank slot: defer or reject. Problem: the proposal. Evidence: missing evidence or poor fit. Impact: uncertain or conflicting value. Effort: opportunity cost. Owner: review owner. Decision requested: a revisit trigger, or retire it. |
| UP-07 | 237 | Required attachment (8 items) | Confidence rationale; counter-evidence; economic implications; new / returning / veteran impact; measurement plan; rollback feasibility; communication commitments; explicit list of excluded scope. |
| UP-08 | 239 | Owner decision record (8 fields) | Chosen option; changes; rejected alternatives; reasons; budget / capacity; authorized date; success criteria; permitted emergency actions. |
| UP-09 | 239 | Rules around the record | Silence is not approval. If the owner picks an option against the agent's advice, keep the agent's rationale and revise the brief; do not rewrite the evidence to make the choice look inevitable. |

The table at LP:241-246 is in the number register (N-18 to N-21).

## 8. Number register (LP:1-247)

### 8.1 The paper's own summary rows ("Rule | Number | Evidence mark | Source and date")

| ID | LP | Rule | Number | Mark (paper) | Source and date (paper) | Scope and limit (from nearby paper text) |
| --- | --- | --- | --- | --- | --- | --- |
| N-01 | 92 | Separate a sustainable rhythm from an absolute promise | 56 consecutive weekly releases before a schedule change | EXPERIENCE | G01, 2020-04-30 | Adopt Me only; wellbeing was the stated reason (LP:62). Also LP:23, 49. |
| N-02 | 93 | Put several beats inside one coherent event | 4 weeks | VERIFIED | G02, 2025-04-04 | One festival; no optimum (LP:169). Also LP:25, 62 (April 4 to May 2). |
| N-03 | 94 | Do not equate audience scale with retention | Over 44.7 million players; 102 million hours | VERIFIED | G05, 2023-11-05 | Measurement is for the preceding day, November 4 (LP:68; register). Not a return rate. Also LP:26. |
| N-04 | 95 | Separate initial effect from durable effect | 27% initial mid-trophy playtime comparison; later normalization | EXPERIENCE | G10, 2026-03-07 | Brawl Stars Ranked; against its March 2024 peak (LP:76). No controlled attribution. |
| N-05 | 96 | Do not infer build time from release spacing | Comparable person-days unknown | OPINION | Synthesis of G01-G25; 2026-10-21 | Not a register source; range includes G18, which has no register entry (X-22). |
| N-06 | 124 | Read weekly advice in context | Weekly ideal; monthly minimum in monetization guidance | VERIFIED | R04, undated; checked 2026-10-21 | Recommendation, not mandate (LP:100). Also LP:22. |
| N-07 | 125 | Keep routine content bounded | Every two weeks to one month; fewer than three weeks' effort recommended | VERIFIED | R02, undated; checked 2026-10-21 | Recommendation (LP:100). Also LP:22. |
| N-08 | 126 | Separate expansion work from routine cadence | Expansions may take many months; no universal duration | VERIFIED | R01, undated; checked 2026-10-21 | Guidance, not measured effect (register note for R01). |
| N-09 | 127 | Count labor and elapsed time separately | Studio-specific; unknown until estimated or measured | OPINION | This paper, 2026-10-21 | Not a register source. |
| N-10 | 156 | Treat pass size as a starting hypothesis | One month; at least one-week rest; ten initial tiers suggested | VERIFIED | R05, undated; checked 2026-10-21 | Suggestions, not validated targets (LP:144). |
| N-11 | 157 | Packaging can change | 4 classes per wave; 3 planned Class Set waves | VERIFIED | G23, 2026-04-27 | Planned structure, no outcome inferred (register). Wording check: X-16. |
| N-12 | 158 | Separate plans from delivered outcomes | 2 paid expansions and 2 free updates in a dated roadmap | VERIFIED | G26, 2025-05-06 | A plan, not proof of execution (LP:150). |
| N-13 | 159 | Never promise a generic content-type revenue lift | No portable causal percentage established | OPINION | Review synthesis, 2026-10-21 | Not a register source. Mark unknown. |
| N-14 | 207 | Event duration is a design variable | 4-week festival example; no universal optimum | VERIFIED / OPINION | G02, 2025-04-04; synthesis 2026-10-21 | One cell holds both marks; the first half is VERIFIED, "no optimum" is OPINION. |
| N-15 | 208 | Synchronized events need explicit, localizable timing | 2024-11-30, 2 PM ET | VERIFIED | G29, 2024-11-21 | One Fortnite live event; no attendance estimate (register). |
| N-16 | 209 | Do not create false time pressure in notifications | No acceptable deceptive amount | VERIFIED | R08, undated; checked 2026-10-21 | Roblox notification policy; the paper's wider ethic is OPINION (LP:177). |
| N-17 | 210 | Keep a humane completion path | Required effort and catch-up depend on observed cohorts | OPINION | This paper, 2026-10-21 | Not a register source. |
| N-18 | 243 | Prioritize evidenced constraints over fashionable additions | No universal score or effort multiplier | OPINION | This paper, 2026-10-21 | Not a register source. Mark unknown. |
| N-19 | 244 | Investigate incentives, not just feature labels | Friend-reward side effects reported; quantified lift absent | EXPERIENCE | R11, 2026-08-24 | Uplift case study; no controlled lift (LP:62). Post-cutoff. |
| N-20 | 245 | Keep simplicity when changing progression | No causal lift disclosed in the cited announcement | EXPERIENCE | G24, 2026-05-13 | Clash Royale announcement (LP:148). |
| N-21 | 246 | Owner chooses; agent records the trade-off | All committed updates need recorded authority | OPINION | "User mandate; operationalized 2026-10-21" | Not a register source (X-22). |

### 8.2 Numbers that appear only in prose

| ID | LP | Number | Scope | Paper's limit | Tag | Src, date |
| --- | --- | --- | --- | --- | --- | --- |
| N-22 | 3 | Research cutoff 2026-10-21 | The whole paper | - | none | - |
| N-23 | 29 | 14-60 days | Duration of Roblox native experiments (with randomization) | - | VERIFIED | R09, undated; checked 2026-10-21 |
| N-24 | 31 | Exactly 100% | Sum of final-outcome probabilities in paid random items; rule covers indirect Robux purchases | - | VERIFIED | R14, undated; checked 2026-10-21 |
| N-25 | 32 | 16+ (age-checked) and 13+ | 16+ = experience / community social-link eligibility; 13+ = personalized experience notifications | Different features; read each surface | VERIFIED | R16 and R08, undated; checked 2026-10-21 |
| N-26 | 49, 62 | 2020 (schedule change); April 4 to May 2, 2025 (festival) | Adopt Me | Historical dated examples (LP:15) | EXPERIENCE / VERIFIED | G01 2020-04-30; G02 2025-04-04 |
| N-27 | 51, 68 | 2023-11-03 (OG start); "November 4" player-hours day | Fortnite OG | Scale, not return rate | VERIFIED | G06 2023-11-03; G05 2023-11-05 |
| N-28 | 52 | October 7 and October 21, 2026; fortnightly with exceptions; alternating odd-numbered Arena patches | League of Legends | G30: dates can change at any time; schedule is planned | VERIFIED | G30 (displayed 2026-05-26; checked 2026-10-21); G07 2026-08-25 |
| N-29 | 53, 72 | 3 sets per year | TFT | No date for the change given in the paper | VERIFIED (LP:53); EXPERIENCE (LP:72) | G09 2025-03-10; G08 2023-09-11 |
| N-30 | 54 | First Thursday of each month | Brawl Stars passes | Start date of the change not stated | VERIFIED | G11 (page displays 2024-02-07; not the first-update date) |
| N-31 | 55, 80 | 6 weeks (Version 2.7, 2022); 2026-08-12 and 2026-09-23 | Genshin Impact | Release evidence, not development time | VERIFIED | G13 2022-05-19; G14 2026-08-12; G15 2026-09-23 |
| N-32 | 56, 82 | 9-week seasons (2022); seasons 1-6 (2026 annual arc) | Overwatch | Historical interval not a 2026 contract | VERIFIED | G16 2022-06-16; G17 2026-02-04 |
| N-33 | 62 | August 2026 case study | Uplift (Adopt Me studio), trading hub, friend currency, summer fish | No controlled lift | EXPERIENCE | R11 2026-08-24 |
| N-34 | 74 | "A few champions every couple of weeks"; no effect size | TFT mid-set drops | No exact effect size | EXPERIENCE | G08 2023-09-11 |
| N-35 | 76 | Work equal to 3 Brawlers; 40,000,000+ views; around 20% fall in revenue and MAU; December 2024 to February 2025 | Brawl Stars Buzz Lightyear collaboration | Not a controlled causal estimate | EXPERIENCE | G10 2026-03-07 |
| N-36 | 76 | 27% above March 2024 peak, then normalized | Ranked, mid-trophy playtime | Initial only | EXPERIENCE | G10 2026-03-07 |
| N-37 | 76 | 80% monthly / 20% weekly Mega Quest; February 2026 | Brawl Stars cadence test | No outcome supplied | VERIFIED | G12 (Feb 2026 update; page displays 2026-03-31) |
| N-38 | 88 | GDC 2022 | Destiny live-service talk abstract | Abstract only | EXPERIENCE | G25 (exact day not established) |
| N-39 | 100 | Under three weeks' effort | Content-cadence work | Recommendation | VERIFIED | R02 |
| N-40 | 144 | One month; one-week rest; ten tiers | Season pass starting design | Not validated targets | VERIFIED | R05 |
| N-41 | 146 | March, July, October 2026; April 2026; 4 per wave; 3 waves | Hearthstone | Plans, not outcomes | VERIFIED | G22 (live catalog); G23 2026-04-27 |
| N-42 | 148 | May 2026; King Tower level kept or raised | Clash Royale | No causal lift disclosed | EXPERIENCE | G24 2026-05-13 |
| N-43 | 150 | May 2025; 2 + 2 | Destiny roadmap | Dated plan | VERIFIED | G26 2025-05-06 |
| N-44 | 169 | 2024-11-30, 2 PM ET | Fortnite Remix: The Finale | Scheduled time | VERIFIED | G29 2024-11-21 |
| N-45 | 45, 96, 131, 220, 243 | Unknowns the paper marks: update-induced retention, returning-player percentage, person-days per release; portable percentage lift per content type; universal score or effort multiplier | All cases / all Roblox genres | "Unknown does not mean zero" (LP:15) | OPINION | - |

## 9. Source ids used in lines 1-247 (resolved from LP:537-749)

Quotes are the register's own, 15 words or fewer. "Cited at" = lines within 1-247. "Reg." = register line. "Post-cutoff" = dated after 2026-06-01. Register note on all entries (LP:539): sources are official docs, official studio posts or conference abstracts; all checked 2026-10-21; quotes are locating excerpts.

| ID | Source (register title) | Date and limits (register) | Post-cutoff / live | URL | Cited at LP | Reg. | Key quote (register) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R01 | Roblox, LiveOps essentials | Undated live document; checked 2026-10-21. Guidance, not measured effect | live-read | https://create.roblox.com/docs/production/game-design/liveops-essentials | 100, 126 | 543 | "Content Cadence releases exclusively build on existing systems" |
| R02 | Roblox, Content updates | Undated live document; checked 2026-10-21 | live-read | https://create.roblox.com/docs/production/game-design/content-updates | 22, 100, 125 | 547 | "many games release content cadence updates every two weeks to one month." |
| R03 | Roblox, LiveOps planning | Undated live document; checked 2026-10-21 | live-read | https://create.roblox.com/docs/production/game-design/liveops-planning | 163 | 551 | "events typically influence several KPIs simultaneously." |
| R04 | Roblox, Monetization | Undated live document; checked 2026-10-21. Recommendation, not a platform mandate | live-read | https://create.roblox.com/docs/production/monetization | 22, 100, 124 | 555 | "A weekly cadence for updates is ideal" |
| R05 | Roblox, Season pass design | Undated live document; checked 2026-10-21. Design recommendations | live-read | https://create.roblox.com/docs/production/game-design/season-pass-design | 144, 156, 177 | 559 | "one month is considered a good starting point" |
| R08 | Roblox, Experience notifications | Undated live document; checked 2026-10-21. Current eligibility and use restrictions | live-read | https://create.roblox.com/docs/production/promotion/experience-notifications | 32, 177, 209 | 571 | "Games should not require users to turn on notifications" |
| R09 | Roblox, Experiments | Undated live document; checked 2026-10-21. Capability and limits | live-read | https://create.roblox.com/docs/production/experiments | 29 | 575 | "Experiments run for between 14-60 days." |
| R10 | Roblox DevForum, Analytics: Understand the success of your Experience Events | 2025-10-21. Reviewed through indexed official excerpts; full thread access limited | no; indexed | https://devforum.roblox.com/t/analytics-understand-the-success-of-your-experience-events/4019126 | 29 | 579 | "compare up to three of your past events on the same chart" |
| R11 | Roblox / Jim Meenan, Optimize Testing and Live Updates with Roblox's Analytics and Experimentation Platform | 2026-08-24. VERIFIED platform account; EXPERIENCE for Uplift's production lessons; no controlled lift for the cited cases | yes | https://about.roblox.com/newsroom/2026/08/optimize-testing-live-updates-roblox-analytics-experimentation-platform | 62, 244 | 583 | "We used analytics and experiments to test our trading hub" |
| R14 | Roblox, Paid random items | Undated live document; checked 2026-10-21. Policy requirements | live-read | https://create.roblox.com/docs/production/monetization/paid-random-items | 31 | 595 | "the probability percentages of all final outcomes must sum to exactly 100%." |
| R16 | Roblox Support, Social Media Links for Experiences & Communities | Undated current support page; checked 2026-10-21. Surface-specific eligibility; do not substitute older group / profile guidance | live-read | https://en.help.roblox.com/hc/en-us/articles/360000910966-Social-Media-Links-for-Experiences-Communities | 32 | 603 | "Links are not permitted to be shared directly within Experiences." |
| G01 | Adopt Me / Uplift, Adopt Me moves to a flexible update schedule from weekly Friday update | 2020-04-30. EXPERIENCE for the production / wellbeing reading; historical schedule | no | https://www.playadopt.me/news/adopt-me-moves-to-a-flexible-update-schedule-from-weekly-friday-update-adopt-me-on-roblox | 23, 49, 92, 120 | 633 | "the main being the wellbeing of our Team" |
| G02 | Adopt Me / Uplift, Cherry Blossom Festival | 2025-04-04. Event dates and duration | no | https://www.playadopt.me/news/cherry-blossom-festival | 25, 49, 62, 93, 169, 207 | 637 | "will run for 4 weeks" |
| G03 | Adopt Me / Uplift, Happy New Year! | 2023-12-28. Source inconsistency, not a trusted year-specific count benchmark | no | https://www.playadopt.me/news/happy-new-year | 96 (inside the range "G01-G25" only) | 641 | "In 2024, we:" |
| G04 | Easy.gg, BedWars official Roblox experience listing | Undated live listing; checked 2026-10-21. Advertised cadence; no attribution or development-cost data | live-read | https://www.roblox.com/games/6872265039/BedWars | 50, 66, 120 | 645 | "Updates are every FRIDAY" |
| G05 | Fortnite official account, record-day announcement | 2023-11-05; measurement refers to the preceding day. First-party aggregate, not independently audited. Official indexed post | no; indexed | https://x.com/Fortnite/status/1721210643888660633 | 26, 68, 94 | 649 | "over 44.7 MILLION players jumping in" |
| G06 | Epic Games, Fortnite OG: Drop Back into Battle Royale Chapter 1! | 2023-11-03. Release structure and historical content refreshes | no | https://www.fortnite.com/news/fortnite-og-drop-back-into-battle-royale-chapter-1 | 51, 68 | 653 | "each major update will bring a different phase of Battle Royale's past" |
| G07 | Riot Games, League of Legends Patch 26.17 Notes | 2026-08-25. Patch statement VERIFIED; design rationale EXPERIENCE | yes | https://www.leagueoflegends.com/en-gb/news/game-updates/league-of-legends-patch-26-17-notes/ | 52, 70 | 657 | "we don't want to be making adjustments so frequently" |
| G08 | Riot Games / Rodger Caudill with Alex Cole and Mort, Talking Tactics: Reflecting on the end of Mid-sets | 2023-09-11. EXPERIENCE on novelty / workload; VERIFIED announced set cadence | no | https://teamfighttactics.leagueoflegends.com/en-us/news/dev/talking-tactics-reflecting-on-the-end-of-mid-sets/ | 53, 72, 74 | 661 | "the impact was near nonexistent when we looked at player sentiment, playtime, etc." |
| G09 | Riot Games, /dev: TFT Into the Arcane Learnings | 2025-03-10. EXPERIENCE on test-time and quality trade-offs | no | https://teamfighttactics.leagueoflegends.com/en-ph/news/dev/dev-tft-into-the-arcane-learnings/ | 53, 72 | 665 | "three sets a year" |
| G10 | Supercell / Frank Keienburg, 2025 in Review: Frank's Blog Post | 2026-03-07. EXPERIENCE with first-party measured observations; no controlled attribution | no | https://supercell.com/en/games/brawlstars/blog/community/2025-in-review-franks-blog-post/ | 27, 54, 76, 95 | 669 | "revenue and monthly active players dropping by around 20%" |
| G11 | Supercell, #StarrToon Patch Notes | Page displays 2024-02-07 and aggregates earlier notes. Historical transition to monthly passes; do not call the displayed date the first December update date | no | https://supercell.com/en/games/brawlstars/blog/release-notes/starrtoon-patch-notes/ | 54 | 673 | "each new season starting on the first Thursday of each month" |
| G12 | Supercell, Release Notes February 2026 | February 2026 update; aggregated page displays 2026-03-31 and includes later maintenance. Test allocation, not a result | no | https://supercell.com/en/games/brawlstars/blog/release-notes/release-notes-february-2026/ | 76 | 677 | "80% of players will receive Mega Quest's on the standard monthly schedule." |
| G13 | HoYoverse, Version 2.7 Update Notice | 2022-05-19. Historical expected duration; indexed official text (page body not exposed to the reader) | no; indexed | https://genshin.hoyoverse.com/en/news/detail/21052 | 55, 80 | 681 | "the duration of Version 2.7 is expected to be 6 weeks" |
| G14 | HoYoverse, "Everwinter Without Mercy" Version 7.0 Update Details | 2026-08-12. Indexed official text, not a complete reviewed article | yes; indexed | https://genshin.hoyoverse.com/m/en/news/detail/165655 | 55, 80 | 685 | "Below are the details of the Version 7.0 update" |
| G15 | HoYoverse, "A Rekviem for the Underworld" Version 7.1 Update Details | Update maintenance 2026-09-23; independent publication timestamp not established. Indexed official text | yes; indexed | https://genshin.hoyoverse.com/m/en/news/detail/166383 | 55, 80 | 689 | "Update maintenance begins 2026/09/23 06:00 (UTC+8)" |
| G16 | Blizzard, Overwatch 2 Reveal Event Recap | 2022-06-16. Historical plan, not proof of every later season | no | https://overwatch.blizzard.com/en-gb/news/23814218/overwatch-2-reveal-event-recap/ | 56, 82 | 693 | "create and deliver seasonal content every nine weeks" |
| G17 | Blizzard, Overwatch Spotlight / Reign of Talon announcement | 2026-02-04. Announced annual narrative and returner support; no retention lift | no | https://overwatch.blizzard.com/en-us/news/24246206/ | 56, 82 | 697 | "a narrative arc with a set beginning, middle, and end" |
| G19 | Valve, Dota 2 news / update feed | Rolling feed; cited 2026 entries include 2026-03-24, 2026-06-25, 2026-07-30; checked 2026-10-21. Dated examples, not a fixed cadence | yes (entries after 2026-06-01); live-read | https://www.dota2.com/news | 57 | 701 | "7.41e Gameplay Update" |
| G20 | Valve, Dota 2 update entry | 2026-07-01. Event reward and usability corrections | yes | https://www.dota2.com/news/updates/16749/ | 57, 84 | 705 | "Scrap is rewarded regardless of winning or losing." |
| G21 | Mojang, The future of Minecraft's development | 2024-09-08. EXPERIENCE on operating model and feedback; announced change VERIFIED | no | https://www.minecraft.net/en-us/article/the-future-of-minecrafts-development | 58, 86, 120 | 709 | "These game drops will vary in size" |
| G22 | Blizzard, Hearthstone expansions and adventures | Undated live catalog; 2026 entries checked 2026-10-21. Catalog dates, not development time | live-read | https://playhearthstone.com/en-us/expansions-adventures/ | 146 | 713 | "March 2026" |
| G23 | Blizzard, Take a First Look at Hearthstone's New Class Sets | 2026-04-27. Planned structure; no outcome inferred | no | https://hearthstone.blizzard.com/en-gb/news/24267730 | 146, 157 | 717 | "Four Class Sets are released at a time, with three waves planned throughout the year." |
| G24 | Supercell, New Collection Levels and Mastery Changes | 2026-05-13. EXPERIENCE for the simplification rationale; migration announcement VERIFIED | no | https://supercell.com/en/games/clashroyale/blog/news/new-collection-levels-and-mastery-changes/ | 148, 245 | 721 | "We want progression to be simple, clear, and rewarding." |
| G25 | GDC / Justin Truman, From Box Products to Live Service: How Destiny 2 Transformed Bungie | GDC 2022; exact session day not established. EXPERIENCE; official abstract only | no | https://gdcvault.com/play/1027599/From-Box-Products-to-Live | 88 | 725 | "prioritization, organization, and decision-making" |
| G26 | Bungie, The Edge of Fate and Year of Prophecy Reveal Recap | 2025-05-06. Dated roadmap; execution and results not inferred | no | https://www.bungie.net/7/en/News/Article/year_of_prophecy_reveal_recap | 150, 158 | 729 | "two paid expansions and two major updates available to all" |
| G29 | Epic Games, Watch Remix: The Finale Nov. 30 @ 2 PM ET! | 2024-11-21. Scheduled live-event timing; no attendance estimate | no | https://www.fortnite.com/news/get-the-slayer-juice-wrld-outfit-starting-nov-25-and-watch-remix-the-finale-on-nov-30-at-2-pm-et | 169, 208 | 741 | "November 30, 2024, at 2 PM ET" |
| G30 | Riot Support / Isto, Patch Schedule - League of Legends | Date displayed 2026-05-26; 2026 schedule checked 2026-10-21. Planned patch dates, explicitly subject to change | live-read (October dates are after the displayed date) | https://support.riotgames.com/en-us/league-of-legends/gameplay/patch-schedule-league-of-legends | 52 | 745 | "Patch dates can change at any time for any number of reasons." |
| (not in register) | "This paper", "Review synthesis", "Synthesis of G01-G25", "User mandate; operationalized 2026-10-21" | The paper's own synthesis dated 2026-10-21; no register entry | n/a | - | 96, 127, 159, 210, 243, 246 | - | - |

G03 is listed because it sits inside the range "G01-G25" at LP:96 and bears on X-18. Register entries not cited in lines 1-247 are not resolved here (for example R06, R07, R12, R13, R15, R17-R22, G27, G28). G18 has no register entry at all (the register jumps from G17 to G19), though the range "G01-G25" spans it.

## 10. Claims for the fact-check

Priority: P1 = a Roblox rule or capability; any cadence claim; any event or update effect (including side effects); any number or percentage. P2 = a case date or schedule with no other number. P3 = framing or qualitative case statement. Fact-check against the source at the id, not against the paper. "Quote covers" says what the register's short quote backs; anything else still needs a read of the live source. "Post-cutoff" = source dated after 2026-06-01; "live-read" = undated live page, re-read it.

### 10.1 Roblox rules and capabilities

| ID | Claim (paraphrase, with scope) | LP | Tag | Src | Src date | Post-cutoff | Pri | Quote covers / check |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FC-01 | Roblox monetization guidance calls a weekly update cadence ideal and monthly a minimum; it is a recommendation, not a mandate | 22, 100, 124 | VERIFIED | R04 | undated; checked 2026-10-21 | live-read | P1 | Quote covers "weekly is ideal" only. "Monthly minimum" is not in the quote. |
| FC-02 | Roblox content-update guidance: many games ship content-cadence updates every two weeks to one month; recommended effort for such work is under three weeks | 22, 100, 125 | VERIFIED | R02 | undated; checked 2026-10-21 | live-read | P1 | Quote covers "two weeks to one month". The under-three-weeks figure is not in the quote. |
| FC-03 | Roblox live-ops essentials separate content cadence on existing systems from expansions that can take many months; no universal duration | 100, 126 | VERIFIED | R01 | undated; checked 2026-10-21 | live-read | P1 | Quote covers "build on existing systems" only. "Many months" is not in the quote. |
| FC-04 | Roblox native experiments run for 14-60 days and give randomization | 29 | VERIFIED | R09 | undated; checked 2026-10-21 | live-read | P1 | Quote covers 14-60 days. "Randomization" is not in the quote. |
| FC-05 | Roblox offers an event-impact comparison across past events (register: up to three on one chart); the paper calls such comparison observational | 29 | VERIFIED | R10 | 2025-10-21 | no; indexed only | P1 | Quote covers the compare-up-to-three feature. "Observational" is the paper's reading (X-15). Full thread not reviewed by the paper. |
| FC-06 | Roblox distinguishes temporary events from permanent updates, and events typically move several KPIs at once | 163 | VERIFIED | R03 | undated; checked 2026-10-21 | live-read | P1 | Quote covers "several KPIs simultaneously". The temporary-versus-permanent distinction is not in the quote. |
| FC-07 | Roblox season-pass guidance: one month as a starting point, at least one-week rest between seasons, ten tiers initially; suggestions, not validated targets | 144, 156 | VERIFIED | R05 | undated; checked 2026-10-21 | live-read | P1 | Quote covers "one month". Rest period and ten tiers are not in the quote. |
| FC-08 | Roblox season-pass guidance discusses exclusivity as an incentive | 177 | VERIFIED | R05 | undated; checked 2026-10-21 | live-read | P1 | Not in the quote. Read the page for the exact wording. |
| FC-09 | Roblox notification policy forbids deceptive pressure, specifically including false time pressure | 177, 209 | VERIFIED | R08 | undated; checked 2026-10-21 | live-read | P1 | Quote covers "should not require users to turn on notifications" only. Prohibition wording is not in the quote. The paper's wider ethic is OPINION (LP:177). |
| FC-10 | Roblox paid-random-item rules cover indirect Robux purchases and require the probabilities of all final outcomes to sum to exactly 100% | 31 | VERIFIED | R14 | undated; checked 2026-10-21 | live-read | P1 | Quote covers the 100% sum. "Indirect purchases" is not in the quote. |
| FC-11 | Experience / community social-link guidance uses age-checked 16+ eligibility | 32 | VERIFIED | R16 | undated; checked 2026-10-21 | live-read | P1 | Quote covers "links not permitted in experiences" only. The 16+ threshold is not in the quote. |
| FC-12 | Personalized experience notifications use 13+ eligibility | 32 | VERIFIED | R08 | undated; checked 2026-10-21 | live-read | P1 | The 13+ threshold is not in the quote. |

### 10.2 Named games: cadence, schedules, numbers, results

| ID | Claim (paraphrase, with scope) | LP | Tag | Src | Src date | Post-cutoff | Pri | Quote covers / check |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FC-13 | Adopt Me moved from a weekly Friday update to a flexible schedule after 56 consecutive weekly releases (2020); the stated reason was team wellbeing | 23, 49, 62, 92 | EXPERIENCE | G01 | 2020-04-30 | no | P1 | Quote covers wellbeing. The count 56 and "consecutive" are not in the quote; confirm 56 in G01 itself (X-18). |
| FC-14 | Adopt Me's Cherry Blossom Festival ran 4 weeks (April 4 to May 2, 2025) with weekly additions | 25, 49, 62, 93, 169, 207 | VERIFIED | G02 | 2025-04-04 | no | P1 | Quote covers "run for 4 weeks". The date range and "weekly additions" are not in the quote. |
| FC-15 | Uplift (Roblox case study): tests of trading-hub server size and matchmaking; a friend-currency incentive caused spam friend requests and private-server avoidance; a summer decorative-fish change caused performance problems; no controlled lift | 62, 244 | EXPERIENCE | R11 | 2026-08-24 | yes | P1 | Quote covers "tested our trading hub" only. The side effects are not in the quote. Update side effects, so P1. |
| FC-16 | BedWars' official Roblox listing says updates come every Friday | 50, 66 | VERIFIED | G04 | undated; checked 2026-10-21 | live-read | P1 | Quote covers it. Live listing, may have changed. |
| FC-17 | Fortnite reported over 44.7 million players and 102 million hours for November 4, 2023 (post of 2023-11-05) | 26, 68, 94 | VERIFIED | G05 | 2023-11-05 | no; indexed | P1 | Quote covers 44.7 million only. 102 million hours is not in the quote. |
| FC-18 | Fortnite OG began 2023-11-03; each major update in November brought a different phase of Chapter 1 Battle Royale history | 51, 68 | VERIFIED | G06 | 2023-11-03 | no | P2 | Quote covers the phases idea. The start date is the register's source date; confirm it equals the OG launch date. |
| FC-19 | League of Legends patches are generally fortnightly, with exceptions | 52 | VERIFIED | G30 | displayed 2026-05-26; checked 2026-10-21 | live-read | P1 | Quote covers only "dates can change". Which exceptions exist is not stated. |
| FC-20 | The 2026 League patch schedule includes October 7 and October 21 | 52 | VERIFIED | G30 | displayed 2026-05-26; checked 2026-10-21 | live-read | P2 | Dates are not in the quote. Planned dates only; October 21 is the cutoff day. |
| FC-21 | Arena balance work runs on alternating odd-numbered patches because excessive adjustment can stop players discovering strategies | 52, 70 | VERIFIED (LP:52); EXPERIENCE (LP:70) | G07 | 2026-08-25 | yes | P1 | Quote covers the rationale ("don't want adjustments so frequently"). "Alternating odd-numbered" is not in the quote; one patch note may not prove a pattern (X-17). |
| FC-22 | TFT shifted to 3 sets per year | 53, 72 | VERIFIED (LP:53); EXPERIENCE (LP:72) | G08, G09 | 2023-09-11; 2025-03-10 | no | P1 | G09 quote covers "three sets a year". No date for the shift in the paper (X-19). |
| FC-23 | TFT's Into the Arcane retrospective: a shorter test period, tied to the show's timing, worsened balance and bugs | 53, 72 | EXPERIENCE | G09 | 2025-03-10 | no | P1 | Not in the quote. Update-timing effect. |
| FC-24 | TFT's 2023 retrospective: adding a few champions every couple of weeks left sentiment and playtime almost unchanged; bundling into a larger moment created heavy workload; no effect size | 74 | EXPERIENCE | G08 | 2023-09-11 | no | P1 | Quote covers "near nonexistent" impact. "A few champions every couple of weeks" and the workload point are not in the quote. Scope: mid-set drops in one game. |
| FC-25 | Brawl Stars passes: each new season starts on the first Thursday of each month | 54 | VERIFIED | G11 | page displays 2024-02-07 | no | P1 | Quote covers it. Date of the transition is not given (X-20). |
| FC-26 | Brawl Stars review: Buzz Lightyear work equaled 3 Brawlers, videos passed 40,000,000 views, revenue and MAU fell around 20% from December 2024 to February 2025; not a controlled causal estimate | 27, 76 | EXPERIENCE | G10 | 2026-03-07 | no | P1 | Quote covers "around 20%". 3 Brawlers, 40,000,000+ and the period are not in the quote. |
| FC-27 | Brawl Stars Ranked: mid-trophy playtime reached 27% above its March 2024 peak at first, then normalized | 76, 95 | EXPERIENCE | G10 | 2026-03-07 | no | P1 | Not in the quote. |
| FC-28 | Brawl Stars February 2026 update: Mega Quest cadence test with 80% of players on monthly and 20% on weekly quests; no outcome | 76 | VERIFIED | G12 | February 2026; page displays 2026-03-31 | no | P1 | Quote covers the 80%. The 20% weekly arm and "no outcome" are not in the quote. |
| FC-29 | Genshin Impact Version 2.7 was expected to last 6 weeks (notice of 2022) | 55, 80 | VERIFIED | G13 | 2022-05-19 | no; indexed | P1 | Quote covers it. |
| FC-30 | Genshin 2026 notices identify updates on August 12 (Version 7.0) and September 23 (Version 7.1) | 55, 80 | VERIFIED | G14, G15 | 2026-08-12; 2026-09-23 | yes; indexed | P2 | G15 quote covers maintenance start 2026/09/23 06:00 (UTC+8). Whether 2026-08-12 is notice date or update date: check (X-24). |
| FC-31 | Overwatch 2's 2022 plan was seasonal content every nine weeks | 56, 82 | VERIFIED | G16 | 2022-06-16 | no | P1 | Quote covers it. Historical, not a current contract. |
| FC-32 | Overwatch's 2026 announcement connects seasons 1-6 into an annual narrative arc and offers returner-facing explanations | 56, 82 | VERIFIED | G17 | 2026-02-04 | no | P1 | Quote covers the narrative arc. "Seasons 1-6" and returner support are not in the quote. |
| FC-33 | Dota 2's official feed shows dated large updates and smaller follow-ups (register cites 2026-03-24, 2026-06-25, 2026-07-30); "irregular" is the paper's reading | 57 | VERIFIED | G19 | rolling feed; checked 2026-10-21 | yes; live-read | P2 | Quote is an update title only. Pattern claim ("irregular") needs a read of the feed. |
| FC-34 | Dota 2 update of 2026-07-01: Scrap is rewarded whether the player wins or loses; reward information improved | 57, 84 | VERIFIED | G20 | 2026-07-01 | yes | P2 | Quote covers Scrap. "Improved reward information" is not in the quote. |
| FC-35 | Mojang announced several free game drops of varying size instead of one annual summer update, informed by community testing (for example new-creature refinements) | 58, 86 | EXPERIENCE | G21 | 2024-09-08 | no | P1 | Quote covers "vary in size". "Instead of a single annual summer update", "several", and the creature example are not in the quote. |
| FC-36 | Hearthstone's expansion catalog lists March, July and October releases for 2026 | 146 | VERIFIED | G22 | undated; 2026 entries checked 2026-10-21 | live-read | P2 | Quote covers "March 2026" only. |
| FC-37 | Hearthstone April 2026: Class Sets replace Mini-Sets, 4 per release, 3 planned waves | 146, 157 | VERIFIED | G23 | 2026-04-27 | no | P1 | Quote covers "Four Class Sets ... three waves". "Replacing Mini-Sets" is not in the quote. Paper says "4 classes per wave" (X-16). |
| FC-38 | Clash Royale May 2026 announcement: progression should be simpler and clearer; changes keep or raise existing King Tower level | 148, 245 | EXPERIENCE | G24 | 2026-05-13 | no | P3 | Quote covers the simplification aim. King Tower point is not in the quote. No causal lift disclosed. |
| FC-39 | Bungie's May 2025 roadmap: 2 paid expansions and 2 free major updates | 150, 158 | VERIFIED | G26 | 2025-05-06 | no | P1 | Quote covers it. A plan, not delivery. |
| FC-40 | Epic scheduled Remix: The Finale for 2024-11-30 at 2 PM ET (announced 2024-11-21) | 169, 208 | VERIFIED | G29 | 2024-11-21 | no | P2 | Quote covers it. |
| FC-41 | GDC 2022 abstract (Destiny talk) frames live service as a change in prioritization, organization and decision-making | 88 | EXPERIENCE | G25 | GDC 2022 (day unknown) | no | P3 | Quote covers it. Abstract only. |
| FC-42 | The "event types / operating pattern" cells for the ten games (themed minigames, event currency, loot / map eras and so on) are described as source-grounded but name no source per cell | 45, 49-58 | OPINION (table intro) | none per cell | - | - | P3 | Check each cell against the game's G source before use (X-21). |

## 11. Contradictions and limits

### 11.1 Limits the paper itself states

| ID | LP | Limit | Handling for skills |
| --- | --- | --- | --- |
| X-01 | 11 | An official announcement verifies what was announced, not that an intervention caused growth. | Write "X announced / reported", never "X caused". |
| X-02 | 12 | First-party experience is not a controlled experiment. | Label every EXPERIENCE row as one developer's account. |
| X-03 | 13, 45 | OPINION rows, templates and the "learn / do not copy" columns are recommendations, not measured facts. | Never cite them as Roblox rules or as evidence of effect. |
| X-04 | 15 | "Undated; checked 2026-10-21" does not mean published that day. Historical examples are not promises about current schedules. | Treat R01-R05, R08, R09, R14, R16, G04, G22, G30 as needing a live re-read. |
| X-05 | 45 | Cases are picked for operating patterns, not as a causal ranking. Public evidence is thin on update-induced retention, returning-player percentages and person-days per release. | Do not state retention effects of updates as known. |
| X-06 | 26, 68 | Fortnite's 44.7M players / 102M hours are not return rates; scale is strong evidence, causation is weak; the counterfactual is not reported. | Never use as a reactivation benchmark. |
| X-07 | 27, 76 | Brawl: a collaboration coincided with a fall in revenue and MAU; the review describes gameplay disruption, not a controlled estimate. | Say "coincided with", never "caused". |
| X-08 | 62 | The Uplift examples give no controlled retention lift. | Use as side-effect warnings only. |
| X-09 | 66 | BedWars' weekly promise says nothing about staffing, testing time, revenue effect or returning share. | Do not infer cost or lift from a public cadence. |
| X-10 | 74, 76 | No exact effect size for TFT's few-champion drops; no outcome for the Mega Quest test. | Do not quote an effect for either. |
| X-11 | 80, 82, 100, 144, 146, 150, 157, 158 | HoYoverse dates are release evidence, not development time. Historical intervals (6 weeks, 9 weeks) are not current contracts. Roblox cadence and season-pass guidance are recommendations. Hearthstone and Bungie are plans, not proof of delivery. | Keep each number labeled with its source and date; never average the intervals. |
| X-12 | 100, 120, 131, 169, 220 | No single optimum: cadence, event length, content-type lift, score or effort multiplier are all unestablished. "Monthly minimum" does not mean ship an unfinished update. | State as unknown; do not give a target. |
| X-13 | 177 | The paper's urgency ethic is OPINION. It does not claim all limited-time content is banned by Roblox; Roblox discusses exclusivity in season-pass guidance and bans deceptive pressure in notifications. | Quote the two Roblox rules separately; add the ethic as advice only. |
| X-14 | 88 | Only the GDC abstract was reviewed, not the talk. | No slide or talk claims. |

### 11.2 Gaps and tensions found by the extractor (not stated by the paper)

| ID | LP | Item | Handling for skills |
| --- | --- | --- | --- |
| X-15 | 29 | "Observational" for the event-impact comparison is the paper's own reading placed under VERIFIED. | Say "Roblox documents a past-event comparison view; comparisons are not randomized" and verify R10. |
| X-16 | 146, 157 (register 717) | G23 quote says "Four Class Sets are released at a time"; the paper writes "4 classes per wave". "Replacing Mini-Sets" is not in the quote. | Re-read G23 before stating the structure. |
| X-17 | 52, 70 | "Arena balances on alternating odd-numbered patches" cites G07 (one patch note, 26.17) and G30. One note may not establish a pattern. | Verify against several patch notes. |
| X-18 | 23, 49, 92 | The 56-week figure is attached to G01 (2020). The paper's later limits section (LP:529, outside this note) says another Adopt Me post, G03 (2023-12-28), "reports 56 weekly updates" under a conflicting "In 2024" heading. Two sources with the same number invite a mix-up. | Confirm 56 consecutive weeks in G01 itself. |
| X-19 | 53, 72 | TFT "3 sets per year" is VERIFIED at LP:53 and EXPERIENCE at LP:72; the paper gives no date for the change. G08 is dated 2023, G09 2025. | Find the announcement date; keep both tags where the paper keeps them. |
| X-20 | 54 | G11 (Brawl monthly passes): the page displays 2024-02-07 and the register says not to treat that as the first update date. The paper gives no transition date. | Do not date the change. |
| X-21 | 45, 49-58 | The paper calls the rhythm and event descriptions "source-grounded", but the event-type column cites no source per cell and carries no own tag. | Treat the column as unverified until checked (FC-42). |
| X-22 | 96, 127, 159, 210, 243, 246 | Several number-table sources are not register entries: "This paper", "Review synthesis", "Synthesis of G01-G25", "User mandate". G18 does not exist in the register. | Treat as the paper's own synthesis; do not look for a URL. |
| X-23 | 11, 26, 27 | Tag use differs between cases. Epic's own player count (G05) is VERIFIED because LP:11 counts a "specifically reported measurement"; Supercell's own revenue and MAU figures (G10) are EXPERIENCE. BedWars is VERIFIED at LP:50 and 66 but sits in an EXPERIENCE sentence at LP:120. | Keep the tag per row; do not rank case reliability by tag alone. Do not carry this paper's tags into notes from other papers. |
| X-24 | 55, 80 | G14 is dated 2026-08-12 and the paper says the notices "identify updates" on August 12 and September 23. Is August 12 the notice date or the release date? G15 has no independent publication timestamp. The gap August 12 to September 23 is 42 days (my arithmetic), but the paper tells readers not to infer development time from release spacing. | Check both notices; no interval claim. |
| X-25 | 49-58 | Only two of the ten cases (Adopt Me, BedWars) are Roblox games, plus the Uplift case study. The other eight are not Roblox games and run other audiences, teams and economies. | Do not read any non-Roblox interval as Roblox guidance. |
| X-26 | 52, 62, 70, 76, 80, 84 | Post-cutoff sources carry many checks: R11 (2026-08-24), G07 (2026-08-25), G14 (2026-08-12), G15 (2026-09-23), G20 (2026-07-01), G19 (entries 2026-06-25, 2026-07-30). Several are indexed text only (G14, G15, R10, G05, G13). | Re-read these first. |
| X-27 | 22, 100, 120 | Weekly-ideal (R04), Adopt Me ending its weekly run (G01), BedWars' weekly promise (G04), Minecraft's variable drops (G21) and TFT's no-effect from small drops (G08) point different ways. The paper resolves it by studio capacity and player fit (LP:120), not by a number. | Never average them into one cadence. |

### 11.3 What the paper says it did not do (inside lines 1-247)

| ID | LP | Not done or unknown |
| --- | --- | --- |
| X-28 | 45 | Did not rank the ten games causally. |
| X-29 | 96, 127 | Did not find comparable development time per update. |
| X-30 | 131, 159 | Did not find a portable percentage lift per content type. |
| X-31 | 7, 246 | Does not authorize committing builders or marketing; every committed update needs recorded owner authority. |

## 12. Line coverage (check C1)

Every non-blank line from 1 to 247 appears below. Blank lines: 2, 4, 6, 8, 10, 14, 16, 18, 20, 36, 38, 40, 42, 44, 46, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 97, 99, 101, 103, 111, 113, 115, 117, 119, 121, 128, 130, 132, 143, 145, 147, 149, 151, 153, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 204, 211, 213, 215, 217, 219, 221, 223, 225, 227, 229, 236, 238, 240, 247. Table separator lines (markdown dashes): 48, 91, 105, 123, 134, 155, 206, 231, 242.

| LP | Content | Where it went |
| --- | --- | --- |
| 1, 3 | Title; research cutoff and audience | MD-01, N-22 |
| 5 | Heading "Mandate and evidence contract" | heading |
| 7 | Mandate paragraph | MD-02, MD-03, MD-04 |
| 9 | Lead-in "Evidence labels apply throughout:" | lead-in to EC-01 to EC-03 |
| 11, 12, 13 | VERIFIED, EXPERIENCE, OPINION definitions | EC-01, EC-02, EC-03 |
| 15 | How labels, registers and dates are used | EC-04 to EC-07 |
| 17 | Auditable-record rule | EC-08 |
| 19 | Heading "Fifteen rules to retain" | heading |
| 21-35 | Rules 1-15 (rule n = line 20+n) | RU-01 to RU-15 |
| 37 | Heading "1. What great live operations are" | heading |
| 39 | Definition of great live operations | DU-01 |
| 41 | Why games fade; mature games | DU-02, DU-03 |
| 43 | Heading "Ten studied games" | heading |
| 45 | Table lead-in and limits | CS-00, N-45 |
| 47 | Table header row | header (columns used in section 3.2) |
| 49-58 | Table rows, ten games | CS-01 to CS-10 |
| 60 | Heading "Evidence behind the patterns" | heading |
| 62 | Adopt Me, festival, Uplift case | EB-01, EB-02, EB-03 |
| 64 | Lesson for small collection games | EB-04 |
| 66 | BedWars | EB-05, EB-06 |
| 68 | Fortnite OG | EB-07, EB-08, EB-09 |
| 70 | Riot Arena | EB-10, EB-11 |
| 72 | TFT 3 sets per year | EB-12, EB-13 |
| 74 | TFT earlier retrospective | EB-14, EB-15 |
| 76 | Brawl Stars | EB-16, EB-17, EB-18 |
| 78 | Brawl lesson | EB-19 |
| 80 | HoYoverse / Genshin | EB-20, EB-21, EB-22 |
| 82 | Overwatch | EB-23, EB-24 |
| 84 | Dota 2 | EB-25, EB-26 |
| 86 | Minecraft | EB-27, EB-28 |
| 88 | GDC Destiny abstract | EB-29, EB-30 |
| 90 | Table header (Rule / Number / Evidence mark / Source and date) | header |
| 92-96 | Number rows for section 1 | N-01 to N-05 |
| 98 | Heading "2. Update rhythm" | heading |
| 100 | Roblox cadence guidance | RH-01 to RH-04 |
| 102 | Four constraints | RH-05 |
| 104 | Rhythm table header | header |
| 106-110 | Weekly, two-weekly, monthly, seasonal, as needed | RH-06 to RH-10 |
| 112 | Menu not benchmark; lanes | RH-11 |
| 114 | Lead time and effort | RH-12 |
| 116 | Capacity constraint | RH-13 |
| 118 | Small versus large | RH-14 |
| 120 | Flexibility versus predictability | RH-15, RH-16 |
| 122 | Table header | header |
| 124-127 | Number rows for section 2 | N-06 to N-09 |
| 129 | Heading "3. Types of live content" | heading |
| 131 | Choose a type after naming the problem | CT-00 |
| 133 | Content-type table header | header |
| 135-142 | Eight content types | CT-01 to CT-08 |
| 144 | Season pass | CT-09, CT-10, N-40 |
| 146 | Hearthstone | CT-11, CT-12 |
| 148 | Clash Royale | CT-13, CT-14 |
| 150 | Destiny roadmap | CT-15, CT-16 |
| 152 | Removing content | CT-17 |
| 154 | Table header | header |
| 156-159 | Number rows for section 3 | N-10 to N-13 |
| 161 | Heading "4. Events" | heading |
| 163 | Roblox events and event definition | EVT-01, EVT-02 |
| 165 | Audience first | EVT-03 |
| 167 | Duration and effort | EVT-04 |
| 169 | Festival and Remix finale; event shapes | EVT-05, EVT-06 |
| 171 | Event calendar | EVT-07 |
| 173 | Trend qualification | EVT-08 |
| 175 | Ethical urgency | EVT-09 |
| 177 | Notification policy and tension | EVT-10, EVT-11 |
| 179 | Heading "Event design template" | heading (section 6.1) |
| 181-203 | 23 template fields | ET-01 to ET-23 |
| 205 | Table header | header |
| 207-210 | Number rows for section 4 | N-14 to N-17 |
| 212 | Heading "5. Deciding what comes next" | heading |
| 214 | Decision sequence | DN-01 |
| 216 | Biggest drop-off first | DN-02 |
| 218 | Hypothesis form | DN-03 |
| 220 | Impact and effort | DN-04 |
| 222 | Matrix, alternatives, opportunity cost | DN-05 |
| 224 | Add, improve, remove | DN-06 |
| 226 | Heading "Ranked update plan template" | heading (section 7.1) |
| 228 | Template header line | UP-01 |
| 230 | Template table header | UP-02 |
| 232-235 | Four template rows | UP-03 to UP-06 |
| 237 | Required attachment | UP-07 |
| 239 | Owner decision record and rules | UP-08, UP-09 |
| 241 | Table header | header |
| 243-246 | Number rows for section 5 | N-18 to N-21 |
| 247 | Blank (line 248, the next heading, is outside this note) | blank |
