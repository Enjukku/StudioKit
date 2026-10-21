---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: "J013-T03, Roblox_Analyst_Research_2026.txt + case sources checked 2026-10-21"
supersedes: []
---
> Author: researcher · claude-sonnet-5-5 · high · 2026-10-21

# Analyst practice: diagnosis, economy, feedback, event planning, reporting (notes and case fact-check)

AP = the owner's paper `Roblox_Analyst_Research_2026.txt` (outside git; line numbers below refer to it; never paste it). PR-id = row id in this note. Tags are the paper's own: V = VERIFIED, E = EXPERIENCE, O = OPINION. Platform facts (R-sources) and statistics (S-sources) are checked by two other agents and are marked "not checked here". OPINION rows are procedure proposals: noted, not fact-checked.

## 1. How I checked

All reads on 2026-10-21. No verdict comes from memory. Quotes are 15 words or fewer, attributed.

| Tag | What | Note |
| --- | --- | --- |
| AP | `Roblox_Analyst_Research_2026.txt` lines 1-32, 91-97, 145-237, 344-441, 443-472, 493-513, 585-655, 747-795 (I register). I also read 474-491 and grep'd every I1-I12 cite (AP:251, 480-482, 628-631 hold extra cites) | Paraphrased only. |
| skill | `.agents/skills/analytics/SKILL.md` (T-01..T-12, lines 31-42; plan file line 11; three questions line 22) | Used only to split analysis from logging code in the event notes. |
| format | `knowledge/reference/marketing/fact-check-roblox-discovery.md` | Format model only. |
| live-extract | WebFetch of each I-source URL in the AP register. WebFetch returns a small-model extract of the page, not the raw page. Where the only evidence is an extract the row says "extract". | I1 read live and in full detail (two reads). |
| PDF problem | I4 (Valve slides) and I6 (Halo paper) are PDFs. WebFetch could not read the PDF text (compressed streams; both the AP URL and two mirrors). The Read tool needs `pdftoppm`, which is not installed. No shell was available. | For I4 I used a GDC 2009 report on Game Watch (Japanese, extract translated by the fetch tool) and a press piece with an Ambinder quote. For I6 I used the Microsoft Research publication page (extract). Both are second-hand, so the rows say so. |
| search | WebSearch used only to find pages. A search summary is never evidence in a row. | |

Evidence sources read (all 2026-10-21):

| Id | URL read | What I got |
| --- | --- | --- |
| I1 | https://www.growthbook.io/podcast/episode/1-36 | Episode page with summary and full transcript (extract). Date 2026-09-01. |
| I2 | https://pmc.ncbi.nlm.nih.gov/articles/PMC4941432/ | Full paper on PMC (extract): abstract, treatments, results. |
| I3 | https://www.riotgames.com/en/work-with-us/disciplines/insights/get-data-informed-on-the-insights-blog | Blog page (extract). Date on page 2015-11-16. |
| I4 | https://cdn.cloudflare.steamstatic.com/apps/valve/2009/GDC2009_ValvesApproachToPlaytesting.pdf ; https://www.gdcvault.com/play/1566/Valve-s-Approach-to-Playtesting ; https://game.watch.impress.co.jp/docs/news/080132.html ; https://gmtk.substack.com/p/valves-secret-weapon | Slides unreadable. GDC Vault page: speaker, GDC 2009, no abstract, no day. Game Watch report and press piece used for content. |
| I5 | https://toronto.ubisoft.com/people-of-ubisoft-toronto-meet-elise-bisson-user-research-craft-lead/ | Profile page (extract). Date 2023-03-23. |
| I6 | https://www.microsoft.com/en-us/research/publication/mastering-the-art-of-war-how-patterns-of-gameplay-influence-skill-in-halo/ ; paper PDF (unreadable) | Publication page (extract): CHI 2013, April 2013. |
| I7 | https://partner.steamgames.com/doc/store/reviews | Doc page (extract). No revision date shown. |
| I8 | https://gdcvault.com/play/1025985/Did-You-Have-Fun-Analytics | Abstract page (extract). GDC 2019, no exact date. |
| I9 | https://www.gdcvault.com/play/1026091/Research-Methods-to-Improve-Live | Abstract page (extract). GDC 2019 microtalk. |
| I10 | https://robertochaves.portfolio.site/candy-crush | Portfolio page (extract). No date. |
| I11 | https://www.zynga.com/blog/zynga-completes-acquisition-of-mobile-growth-platform-storemaven/ | Press release (extract). Date 2022-09-12. |
| I12 | https://www.gdcvault.com/play/1023268/Evaluating-Game-Experiments-A-More | Abstract page (extract). GDC 2016, no exact date. Not in my line range (cited at AP:251); added because it is an I-source. |

## 2. Notes

Row = PR-id | AP:line | tag | paraphrase. "Plat" = platform fact or statistic, not checked here. "Case" = see section 3.

### 2.1 The 15 rules (AP summary)

| PR-id | AP:line | tag | paraphrase |
| --- | --- | --- | --- |
| PR-R01 | 18 | V (plat) | Read D1 retention and session time first, then sustained return, then money. Roblox gives this order (R1). |
| PR-R02 | 19 | V (plat) | Compare cohorts of the same age that have all been observed. D7 and D30 mean nothing before their return day has passed (R3). |
| PR-R03 | 20 | O | Every metric needs five things before reading it: denominator, unit, time window, population, definition version (R12, S1). |
| PR-R04 | 21 | V (plat) | Roblox peer benchmarks move. The displayed band is the 50th to 90th percentile. It is not a target (R2). |
| PR-R05 | 22 | O | Treat fixed 2026 genre-and-age targets as unknown unless a dated, comparable dataset backs them (R2). |
| PR-R06 | 23 | E | Mix behavior data, surveys and watched play. Riot and Valve use complementary methods (I3, I4). Case. |
| PR-R07 | 24 | O | A funnel shows where to look. It does not show why someone left (R9, I4). |
| PR-R08 | 25 | V (stat) | Size an experiment for the effect and the spread. No universal player count exists (S1). |
| PR-R09 | 26 | V (stat) | Check sample ratio mismatch before picking a winner (S2, R11). |
| PR-R10 | 27 | V (plat) | Early harm checks stop bad tests. They do not crown early winners (R11). |
| PR-R11 | 28 | V (stat) | A significant result does not show size, importance or truth (S5). |
| PR-R12 | 29 | O | Judge money together with retention, progression, trust and purchase delivery (I1, I2, R15). Case. |
| PR-R13 | 30 | V (plat) | Mark 2026-10-12 as a discovery measurement break. Old data was not rewritten (R18). |
| PR-R14 | 31 | O | Count feedback contributors and sampling gaps, not only comments. Silence is not approval (I3, I5, I7). Case. |
| PR-R15 | 32 | O | Give one finding, its evidence and uncertainty, and one next action with an owner and a success condition (I5, S5). |

### 2.2 What to watch first (new vs live game)

| PR-id | AP:line | tag | paraphrase |
| --- | --- | --- | --- |
| PR-W01 | 93 | O | New game order: (1) players can join and performance is usable; (2) the first session delivers the advertised activity; (3) players understand and finish the core loop; (4) D1; (5) progression and D7. Log purchase delivery and economy integrity from day one, even if there is too little data to infer anything yet. Heavy ad spend before the first session works only buys more evidence of the same fault (R1). |
| PR-W02 | 95 | O | Live game: watch service health and logging all the time. Then: comparable retention cohorts, mix of active players, content use, economy stocks and flows, how many people pay, revenue quality. Keep three groups apart: new, continuously active, returning after a lapse. A spike of returning players does not show better onboarding. |
| PR-W03 | 97 | O | Read the low tail of FPS and the high tail of memory per device class. A platform average can improve because weak devices stopped returning. Compare like devices and the same release. Link technical faults to join success and goal completion when data allows. Never call an unexplained disconnect a crash. Never read a missing last event as a voluntary exit. |
| PR-W04 | 99-104 | V/O | Table rows: respect return-day horizons (V, R3); optimize early experience first: D1 and mean session time (V, R1); keep the unit of the experiment consistent: player, party or server as assigned (O, S1); read performance as P10/P50/P90 where supported (V, R7, R13). Plat. |

### 2.3 Diagnosis

| PR-id | AP:line | tag | paraphrase |
| --- | --- | --- | --- |
| PR-D01 | 149 | O | Split "players are leaving" into one measurable symptom: fewer arrivals, more join failures, shorter sessions, fewer repeat sessions, lower return-day retention, stalled progression, or loss of established players. Each needs a different search. Lower peak CCU can sit beside flat retention. Falling average session length can come from many new players, not a worse game. |
| PR-D02 | 151 | O | Find the first credible break in time. Then compare steady segments: acquisition cohort, source, platform/OS, version, country/language, prior tenure, prior progression. Use only dimensions the metric really has. Segment counts must add up to the total. Explain "Unknown" and "Other". Do not claim a platform-by-source effect from two separate one-way charts. A rate re-weighted to fixed baseline segment weights can show a mix change if strata fit and data suffice. Label it an adjustment. |
| PR-D03a | 157 | O | Hypothesis: acquisition promise mismatch. Prediction: early exits that depend on source after a campaign or creative change. Disconfirm: the same exits in unaffected sources. Collaborator: marketing agent. |
| PR-D03b | 158 | O | Hypothesis: loading or device regression. Prediction: join failures and FPS or memory change concentrated in one version or device. Disconfirm: matched-device performance is stable, and the task failure can be reproduced elsewhere. Collaborator: engineering and game designer. |
| PR-D03c | 159 | O | Hypothesis: players cannot find the next action. Prediction: eligible players stall before an obvious action; playtesters are confused. Disconfirm: players understand it but cannot afford it. Collaborator: game designer. |
| PR-D03d | 160 | O | Hypothesis: progression wall. Prediction: more attempts, time or shortfall at the same milestone. Disconfirm: progression works but players have no wish to return. Collaborator: progression designer. |
| PR-D03e | 161 | O | Hypothesis: content used up. Prediction: finishers among advanced players return less. Disconfirm: early-stage cohorts fall just as much. Collaborator: live-ops designer. |
| PR-D03f | 162 | O | Hypothesis: economy or offer frustration. Prediction: shortfall or purchase/delivery failures plus matching feedback. Disconfirm: the complaint comes from an unrepresentative group and affected behavior is unchanged. Collaborator: progression or game designer. |
| PR-D03g | 163 | O | Hypothesis: the measurement changed. Prediction: the break lines up with a schema or pipeline change, and other independent measures disagree. Disconfirm: the break persists in independent verified data. Collaborator: analyst and engineering. |
| PR-D04 | 153 | O | Build the competing-explanations table before choosing a story (rows D03a-g). Each row needs a prediction, a test that would disprove it, and a named collaborator. |
| PR-D05 | 167 | O | Funnel report fields per step: eligible entrants, completers, conditional completion, overall completion, time to complete, repeated attempts, unresolved observations. The biggest percent drop can hit fewer people than a smaller early drop. Rank by players affected, severity, strength of evidence, fix cost. Not by drop percent alone. |
| PR-D06 | 169 | O | Keep five states apart: shown, eligible, attempted, succeeded, reward delivered. Judge a shop by more than its buyers and a boss by more than its wins. Name alternate paths and optional steps. For repeatable activities use attempt funnels for usability and player-level outcomes for retention. If valid orders vary, a strict line funnel can call normal play abandonment. |
| PR-D07 | 171 | O | Time-to-milestone must keep people who did not finish. Finishers only select skilled players and make a hard feature look fast. Use a fixed follow-up window. Report the finished fraction beside the timing. Use survival methods only if raw data and censoring assumptions exist. Not reached by the cut-off does not mean never. |
| PR-D08 | 175 | V/O | Survival and hazard methods exist for cut-off game-time data (S8, stat, not checked here). Define the end event first (finish a level, end a session, become inactive). Cut-off by end of data differs from telemetry lost in a crash. A routine curve does not fix missingness that depends on the outcome. |
| PR-D09 | 177, 193 | E | Riot: uses surveys, behavior analytics and lab observation. Yasuo example: 36 percent win rate at release, above 50% after about 35 games. Lesson offered: split a new weapon or hard mechanic by prior experience so learning is not mistaken for bad balance (I3). Case C15-C19. |
| PR-D10 | 179 | E | Valve: designs are hypotheses, playtests are experiments. Slides discuss observer bias, think-aloud problems, averages hiding extremes. Offered lessons: let players chase a goal without coaching; record actions before asking why; keep comprehension tests apart from timed tests (I4). Case C20-C24. |
| PR-D11 | 181 | E | Ubisoft research lead: test the gap between what the design meant and what players feel. Designers keep the design call. The analyst should say "players misread the upgrade requirement", not replace a system (I5). Case C25-C27. |
| PR-D12 | 183, 194 | V | Halo study: seven months of behavior from over 3 million players, plus a 70-person survey, used together (I6). Case C28-C31. |
| PR-D13 | 185 | O | Recruit playtesters from the affected audience (new players, the right devices), not only staff, Discord regulars or big spenders. Watch confusion to form a mechanism guess. Check how common it is separately. A few repeat observations can justify a cheap usability fix without a prevalence claim. |
| PR-D14 | 189 | O | Causal language ladder: "occurred" = descriptive change. "associated with" = adjusted observational link. "consistent with" = proposed mechanism. "caused an estimated change in this tested population" = only after a valid experiment or defensible causal design. Predicting churn does not tell you what prevents it. A feature used by loyal players may mark loyalty, not cause it. |
| PR-D15 | 193-196 | E/V/O | Table rows: check learning before nerf or buff (E, I3); mix behavior and explanations (V, I6); count failures and unfinished journeys, no universal drop-off threshold (O); funnels locate, they do not explain (O, R9). |

### 2.4 Economy

| PR-id | AP:line | tag | paraphrase |
| --- | --- | --- | --- |
| PR-E01 | 200 | V/O | Roblox Economy view shows sources, sinks, average wallet after instrumentation. Monetization view shows revenue, paying users, daily conversion, ARPPU, ARPDAU (R8, R5; plat). Study virtual currency apart from Robux revenue. Neither equals cash profit or DevEx. |
| PR-E02 | 206 | O | Accounting identity for one currency and a fixed wallet set: closing stock = opening stock + minted sources - destroyed sinks + net transfers across the boundary + explicit adjustments. Player-to-player transfers cancel across the whole population. Marketplace fees can be sinks. A currency exchange needs both sides logged. Refunds, admin grants, resets, expiry and exploit reversals need their own categories. A change in the wallet set must be reconciled separately. |
| PR-E03 | 208 | O | Review: sources and sinks per active player and per unit of active play time; wallet distribution by tenure and progression; affordability of the next meaningful purchase; sink participation. Average balance can rise because rich veterans are a bigger share, saving is intended, a good sink vanished, or items were duplicated. Positive net flow is not automatically inflation. New players and content can need a bigger supply. |
| PR-E04 | 210 | O | Inflation test, traded economy: a same-quality basket of market prices rising with currency supply, trade volume and buying power. Exclude quality changes and thin-market manipulation. Fixed-price shop: prices cannot show market inflation. Look at how fast rewards buy upgrades, full inventory, skipped content, lost scarcity. Name the mechanism before using the word inflation. |
| PR-E05 | 212 | O | Progression economy review questions: Can an eligible non-payer afford the next intended step? How many active minutes and attempts does it need? Do players spend on intended sinks, hoard for an event, or stall? Which currency binds? Do new rewards displace old ones? What happens after the first prestige or rebirth? Give the progression designer one bottleneck and one experiment, not "add sinks". |

### 2.5 Purchase and payers

| PR-id | AP:line | tag | paraphrase |
| --- | --- | --- | --- |
| PR-P01 | 216 | O | Purchase trace: eligibility, offer shown, value understood, prompt, confirmed purchase, benefit delivered, later use and return. Keep cancel, failure, too little currency, policy block and delivery error apart where visible. A prompt is not a purchase. A client acknowledgement is not settlement. |
| PR-P02 | 218 | O | Split first-time and repeat payers by status measured before the treatment. Report: payer count, purchase frequency, basket value, product mix, concentration, revenue per eligible user. ARPPU can rise by losing small spenders. Higher conversion with lower ARPPU can still raise revenue. Do not judge a price test among buyers only: treatment can change who buys. |
| PR-P03 | 220, 234 | V | King pricing field experiment: over 14 million consumers, discounts of 9-70% on large purchases, little revenue change, shifts mostly among existing buyers (I2). Offered use: test total revenue, first-payer recruitment, stockpiling, later spend, retention. An old study shows a mechanism, not a Roblox elasticity. Case C09-C14. |
| PR-P04 | 222, 235 | V (plat) | Roblox price-optimization guidance: usually 60,000 transactions in the prior 30 days; managed tests apply prices only on positive incremental revenue; automatic tests at least every 90 days (R14). Not checked here. The paper adds: this is not a player count for an experiment. Check account eligibility, running tests, regional prices, discounts first (O). |

### 2.6 Fair monetization constraints

| PR-id | AP:line | tag | paraphrase |
| --- | --- | --- | --- |
| PR-F01 | 226, 236 | V (plat) | Paid random outcomes include Robux-funded currency and odds modifiers. Real outcomes and numeric odds must be shown. Odds total 100% (rounding disclosure rule applies). Per-player paid-random-item and paid-trading limits apply (R15). Not checked here. |
| PR-F02 | 228 | O | Treat eligibility and policy as design limits, never as test variables. Propose clear offers, honest prices and benefits, reliable delivery, a workable non-paying path, and watch regret, frustration, and return. No pressure aimed at vulnerable players. A revenue gain does not excuse deception. Retention and satisfaction guardrails are studio choices above the documented minimum. |
| PR-F03 | 230 | E/O | Supercell interview (Sept 2026): retention, trust, telling players about tests in advance, make-up events for fairness (I1). Offered use: in a shared world, unequal rewards can touch friendships, competition, trading even in a random UI test. A private shop-layout test and a server-wide currency test need different designs. Case C01-C08. |
| PR-F04 | 234-237 | V/O | Table rows: do not assume deeper discounts raise revenue (V, I2); check price-test feasibility (V, R14); audit real outcome probabilities (V, R15); separate stock growth from inflation, no universal source-to-sink target (O). |

### 2.7 Feedback as data

| PR-id | AP:line | tag | paraphrase |
| --- | --- | --- | --- |
| PR-FB01 | 346 | V/O | Audience > Feedback: CSV export, ratings, device or platform context, comments. Coverage starts 2025-02-01 for votes and 2025-03-17 for comments. Ratings can change. Filtered comments do not show (R16, plat). Analyze the window you have, not a life-time census. The shown platform may not be the device used all through play. |
| PR-FB02 | 348 | O | Source filters differ: in-game responses are filtered by who is exposed and who stays; Roblox ratings by who reviews; Discord by community members; social posts include onlookers and copied complaints. Use authorized data only. Keep personal identifiers to a minimum. Remove reposts and repeat contributors where legitimately possible. If identity cannot be resolved, report comment counts, not unique players. |
| PR-FB03 | 352 | O | Codebook (versioned): topic, feature/stage, sentiment, report type (bug, comprehension, difficulty, fairness, preference, request), severity, evidence span, confidence, unknown/other. A comment may carry several themes, so theme shares need not add to 100%. Keep raw wording and source id in a protected audit trail. Summaries point back to exact examples. Keep a request ("double rewards") apart from the need ("progress feels stalled"). |
| PR-FB04 | 354 | O | Human-label validation: people first label a varied sample (languages, devices, positive/negative/neutral, rare severe problems). Compare model labels to the human ones. Review disagreements. Revise the codebook before bulk work. Audit precision and recall per theme where labels allow, not one overall accuracy. Record doubt for sarcasm, slang, short comments, translation. The model must not invent an unstated reason for quitting. |
| PR-FB05 | 356 | O | Report a theme as contributors mentioning it / contributors in this source and window. Also report source participation against eligible players if known. Compare who responded with the player population. Weighting fixes known mix gaps, not unknown nonresponse. A big opt-in sample can be biased. Silence is not satisfaction. |
| PR-FB06 | 360 | E/O | Steam reviews doc: reviews are one channel and should not dominate development (I7). Activision GDC abstract: in-game fun surveys tied to disconnects, maps, performance, turned into experiments (I8; see correction C35). Offered use: tie a complaint about a wave to eligibility, attempt, failure and device evidence. Agreement raises confidence. A severe repeatable bug can deserve action with few reports. Case C32-C37. |
| PR-FB07 | 362 | E/O | GDC retention session: diaries, surveys, analytics, in-house tests across early and long play (I9). Offered use: diaries or follow-up interviews for gaps between sessions that logs cannot explain (unclear goal, social availability, boredom, other interests). No leading prompts. Case C38-C39. |
| PR-FB08 | 364 | V/O | Roblox AI reports: analytics reports for games with 1000+ DAU, feedback reports with 20+ comments; the docs warn they can be wrong (R17, plat). Treat generated themes as leads, not independent proof of another model's reading of the same comments. |
| PR-FB09 | 368-371 | V/O | Table rows: respect coverage dates (V, R16); eligibility for a report is not representativeness (V, R17); report contributors and denominators, no universal representative comment count (O); validate machine coding against evidence spans, no invented accuracy bar (O). |

### 2.8 Event planning (what a new feature should log)

| PR-id | AP:line | tag | paraphrase |
| --- | --- | --- | --- |
| PR-EV01 | 375 | O | Log decisions, not every action. Start from the player benefit and the decision the data must support. List the competing explanations that would need different actions. Choose the fewest observations that tell them apart. |
| PR-EV02 | 377 | O | Event contract: 16 fields (listed in section 4.3). A change in meaning needs a version boundary and a note on comparability. |
| PR-EV03 | 379 | O | Names: stable, outcome-style (feature_entered, reward_granted). Changing item or map ids go in controlled properties, not in new event names. Keep exposure apart from selection and success apart from delivery. "feature_used" cannot tell an invisible button from a failed try from a success. No raw chat, free text, fine movement or every attack unless a defined decision needs it and collection is appropriate. |
| PR-EV04 | 381-393 | O | Example (tower-defense progression feature), seven decision questions, each with observation, context and reason: (1) Did eligible players discover it? eligibility and real chance to see it; feature version, prior progression, assignment if tested. (2) Can players start? entry try and accept/fail; failure reason, resource state. (3) Is the first wave understandable? attempt start, meaningful checkpoint, end result; map or tier, attempt id, party, loadout category. (4) Is progression too slow? milestone reached, time/attempt/resource summaries; stage, active-play exposure. (5) Was the reward delivered? authoritative grant result; reward category, currency and balance meaning. (6) Does the feature improve the game? later return and total play; eligible cohort, follow-up, assignment. (7) Does it hurt performance or trust? version-linked technical and feedback outcomes; device/OS, exposure, source coverage. AP marks all rows as proposed meanings, not claims about real schemas. |
| PR-EV05 | 395 | O | DROPPED from this note: a sentence about one specific game genre's first-loop checkpoints (game-specific). The general rule stays: add opportunity and failure reasons where they separate fixes; do not add an event per fragment. See section 6. |
| PR-EV06 | 399 | O | Acceptance before ship: walk the successful, canceled, retried, interrupted and returning-player journeys. Totals must reconcile with an independent authoritative record where one exists. Check missing properties and impossible order. Both test arms must offer equal measurement. Say what happens when a session ends without a final event. Do not claim a reliable quit reason if none exists. |
| PR-EV07 | 401 | O | Keep authoritative money and progression accounting apart from sampled diagnostic telemetry. If sampled, record the inclusion rule and never read a sample as a full count. Retire measurements that no longer serve a decision, but keep the definition and history needed to read old analyses. Too much logging adds confusion. Too little leaves no denominator or mechanism. Event count is not maturity. |
| PR-EV08 | 403, 409 | E | King practitioner account: prototype, interview, iterate, remote tests, then live A/B for the Mystery Machine (I10). Offered order: find likely confusion cheaply, plan measurement for what remains unknown, then test live outcomes. Do not spend test traffic to learn that a button is unreadable. Case C40-C43. |
| PR-EV09 | 407-410 | O/E | Table rows: every observation needs a decision, no universal event count (O); separate opportunity, action, result, delivery (O, R9); validate prototypes before live tuning, one-week sprint reported, not required (E, I10); version meaning and record missing data (O, R18). |

### 2.9 Reporting

| PR-id | AP:line | tag | paraphrase |
| --- | --- | --- | --- |
| PR-RP01 | 414 | O | Headline shape: for [players], [outcome] changed [amount] during [window]; [evidence] supports [reading] while [uncertainty] remains; recommend [one action] because [value and risk]. If the cause is unknown say where the loss happens and that the reason is not found. |
| PR-RP02 | 416 | O | Keep three certainties apart: of the measurement, of the cause, of the value of acting. A cheap, reversible fix can go ahead on weak causal proof. A costly redesign needs more. Do not relabel a judgment call as a proven cause. "High confidence" needs stated grounds, not an AI-made percent. |
| PR-RP03 | 418-424 | O | Recipient table (see section 4.5). |
| PR-RP04 | 426 | E/O | Zynga public account ties creative testing, growth experiments and measurement (I11). Offered use: judge the players a creative brings, not clicks. Analyst owns evidence, marketing owns execution. The announcement gives no Zynga retention targets. Case C44-C46 (correction: it describes the acquired product). |
| PR-RP05 | 430 | O | Charts that earn space: cohort heatmap for same-age return; time series with release and measurement notes for timing; aligned small multiples for device or source; count-and-rate funnel bars for where loss occurs; distributions or cumulative curves for session or progression spread; source/sink flow plus wallet distribution for economy; effect-with-interval plot for experiments. Show denominators, units, date windows, maturity, missing data. Keep raw points visible when smoothing. Overlapping rolling windows are not independent confirmations. |
| PR-RP06 | 432 | O | Charts to avoid: dual axes that suggest false links; averages alone for skewed data; cumulative curves that hide a stalled daily rate; cut axes that inflate small gaps without notice. Flow or Sankey only when flows reconcile. Caption = finding plus limit, not axis labels. |
| PR-RP07 | 434 | V/O | Creator Hub custom dashboards combine charts, tables, summary cards (R21, plat). Save a small owner view and a diagnostic view. Widget count is not success. No made-up charts without game data. |
| PR-RP08 | 438-441 | O/E/V | Table rows: lead with one finding and one action (O); make uncertainty assessable: denominators, window, interval where valid (O, S5); analyst diagnoses, designer chooses the fix (E, I5); reuse a shared metric view (V, R21). |

### 2.10 Process (12 steps) with gates

| PR-id | AP:line | tag | step: required work -> gate before moving on |
| --- | --- | --- | --- |
| PR-PC01 | 449 | O | Frame: turn the request into outcome, population, window, decision -> a different answer would change an action. |
| PR-PC02 | 450 | O | Inventory: confirm dashboards and API metrics, raw data, permissions, definitions -> no promised analysis needs a field that does not exist. |
| PR-PC03 | 451 | O | Freeze: keep extraction, query, build/config, timezone, cohort and accounting definitions -> another analyst can reproduce the input. |
| PR-PC04 | 452 | O | Validate: check completeness, duplicates, joins, missing data, maturity, impossible values, reconciliation -> the measure fits the question. |
| PR-PC05 | 453 | O | Describe: size, affected count, spread, uncertainty -> rates have the right denominators and units. |
| PR-PC06 | 454 | O | Localize: split by plausible pre-treatment segments and time; check composition -> segment evidence adds up to the overall change. |
| PR-PC07 | 455 | O | Hypothesize: list competing mechanisms and predictions; look for disproof -> no single convenient story assumed. |
| PR-PC08 | 456 | O | Triangulate: playtests and feedback from the affected population -> qualitative evidence is not shown as prevalence. |
| PR-PC09 | 457 | O | Identify: pick an experiment, a credible quasi-experiment, or a plainly descriptive comparison -> causal wording matches the strength of design. |
| PR-PC10 | 458 | O | Evaluate: compare useful effect, uncertainty, guardrails, build cost -> invalid or inconclusive is an allowed result. |
| PR-PC11 | 459 | O | Report: one finding, evidence, uncertainty, one action, owner, review condition -> the director can decide without decoding stats words. |
| PR-PC12 | 460 | O | Learn: record the prediction, the decision, the rollout result, the revised belief -> failed and null results are kept. |

### 2.11 AI-specific controls

| PR-id | AP:line | tag | paraphrase |
| --- | --- | --- | --- |
| PR-AI01 | 464 | O | Never compute a business result by fluent text. Use deterministic queries and calculations and keep their outputs. Every reported number resolves to a source cell, query result or stated formula. Keep measured, calculated, estimated and opinion values apart. Keep full precision inside; use a stated display-rounding rule in reports. |
| PR-AI02 | 466 | O | Check the grain before every join (a purchase joined to many event rows multiplies revenue). Audit row counts and unique keys before and after. Keep absent, zero, cut-off, filtered, not-yet-final apart. Know if each metric is a sum, mean, ratio of sums, mean of ratios, percentile or distinct count. Do not pool experiment results by averaging arm lifts. |
| PR-AI03 | 468 | O | Leakage: a churn model may use only features known before prediction time; subgroup splits for causal reading use pre-treatment traits. Exclude bots and exploits by an auditable rule set made before seeing preferred outcomes. Show sensitivity when exclusions matter. Do not trim big spenders to reach significance. Do not hide one extreme payer inside a plain mean. |
| PR-AI04 | 470 | O | Every newly searched segment is exploratory unless planned in advance. Keep a log of questions tried, not only the significant charts. AI summaries, benchmark claims and auto-proposed reasons need source-level checks. Without raw data do not invent intervals, power or sample sizes from aggregates. |
| PR-AI05 | 472, 490 | E/O | Supercell 2026: fewer than 100 A/B tests per quarter; worry about consistency as AI lets more staff analyze (I1). Offered use: a standard review contract, not a quota. The target is an auditable decision. Case C05-C06. |

### 2.12 Appendix A (diagnosis checklist) - rows in section 4.1

| PR-id | AP:line | tag | paraphrase |
| --- | --- | --- | --- |
| PR-A01..A13 | 497-511 | O | The 13 steps with PASS and FAIL actions are copied as a list in section 4.1. |
| PR-A14 | 513 | O | Severe verified technical defect: recommend repair now and keep the evidence. Do not wait for a cohort to mature. Uncertain and costly problem: recommend the most decision-relevant missing measurement or test. "Investigate everything" is not a recommendation. |

### 2.13 Appendix D (weekly report) - fields in section 4.2

| PR-id | AP:line | tag | paraphrase |
| --- | --- | --- | --- |
| PR-AD01 | 587 | O | Keep the decision report short. Put queries and detailed segments in an audit attachment. Do not force a causal story every week. A quiet week can still show an important uncertainty. |
| PR-AD02 | 589-613 | O | Fields are listed in section 4.2. |

### 2.14 Appendix E (do-not-do list)

| PR-id | AP:line | tag | paraphrase |
| --- | --- | --- | --- |
| PR-AE01 | 619 | O | Do not invent a Roblox genre benchmark or reuse another platform's number. Fetch the game's own current comparison; say that public data is missing (R2). |
| PR-AE02 | 620 | V | Do not compare immature D7/D30 with mature cohorts (R3). |
| PR-AE03 | 621 | V | Do not call a pipeline change a behavior change. Note measurement versions, mainly 2026-10-12 (R18). |
| PR-AE04 | 622 | V | Do not say a p-value is the chance the hypothesis is false. Report effect, uncertainty, design validity (S5). |
| PR-AE05 | 623 | O | Do not stop at the first good-looking p-value. Use the set horizon or valid sequential inference (S1, S3). |
| PR-AE06 | 624 | E | Do not ignore sample ratio mismatch or fix it by handy exclusions. Find the missing or enrolled population first (S2). |
| PR-AE07 | 625 | V | No early-harm alert is not proof of safety or an early win. EHD is a harm screen with enrollment and metric limits (R11). |
| PR-AE08 | 626 | O | Do not compare buyers, finishers or event joiners as if chosen at random. Keep the eligible population. |
| PR-AE09 | 627 | V | Do not report only the favorable metrics, segments or tests. Keep the declared primary outcome and full history (S5). |
| PR-AE10 | 628 | O | Do not infer causes of quitting from last events or model sentiment alone. Watch affected players and test competing explanations (I3, I4). |
| PR-AE11 | 629 | O | Do not equate more play time with more enjoyment. Waiting, confusion and incentives raise time. Measure experience too (I4, I8). Support check: C37. |
| PR-AE12 | 630 | O | Do not read more currency as inflation or higher ARPPU as better monetization. Reconcile stocks, prices, population, payer mix (R8, R5). |
| PR-AE13 | 631 | O | Do not generalize loud comments to all players. State coverage; look for silent, new and lapsed players (I3, I5, I7). |
| PR-AE14 | 632 | V | Do not quote AI feedback summaries as observed facts. Check original comments and numbers (R17). |
| PR-AE15 | 633 | O | Do not give a menu of unrelated fixes with no priority. Make one recommendation tied to evidence and a decision condition. |

### 2.15 Appendix F (open questions and limits)

| PR-id | AP:line | tag | paraphrase |
| --- | --- | --- | --- |
| PR-AF01 | 637 | O | No sourced 2026 public matrix of weak/average/good per genre and age. Retrieve each game's own benchmark values, pool and snapshots. A research gap is not proof that no private dataset exists. |
| PR-AF02 | 639 | O | Native experiment internals (estimator, intervals, sequential rules, multiple tests, late-enrolled retention) are not fully public. Verify docs or ask support before reproducing scorecards. Do not reverse-engineer intervals from rounded screenshots. |
| PR-AF03 | 641 | V/O | Acquisition 30-day revenue view leaves out subscriptions, engagement payouts, immersive ads (R6, plat). The acquisition page says "8th day (D8)" for a 7-day idea while the retention page says D7 is the eighth day (R3). Treat as a label clash. Call first-play day zero and check the field that comes back. |
| PR-AF04 | 643 | O | Aggregated API data does not give raw longitudinal records, custom joins or user-level survey links. List real data and permissions before promising survival models, causal adjustment or first-purchase analysis. Aggregate-only analysis may be all that is possible. |
| PR-AF05 | 645 | V/O | Standard and performance endpoints keep different history (28 days for performance, 1468 for many standard metrics; R13, plat). Archive allowed aggregates on a schedule that fits the comparison horizon. Check each metric. |
| PR-AF06 | 647 | O | Player-level random splits can answer the wrong question where trading, queues, parties or global rewards link players. Needs per-game design. No universal threshold. |
| PR-AF07 | 649 | O | Case precision is limited. Roblox creator reports lack data to rebuild intervals or unit of uplift. Supercell and named practitioners are first-hand accounts, not audited benchmarks. The King pricing result is old and context-specific. (Checked: C01-C14.) |
| PR-AF08 | 651 | O | The paper used the RDC 2026 post and the public GDC abstracts and slides. It did not watch full recordings. An abstract supports only what it says. (Checked: C35, C36, C38, C39, C47, C48.) |
| PR-AF09 | 653 | O | Low-traffic games: precise small-effect tests may not be possible. Valid routes: fix directly seen severe faults, improve measurement, or test a larger design change. A convincing story is not sample information. |
| PR-AF10 | 655 | O | Data the studio must supply: universe and place ids, genres and launch dates, current authorized dashboards or API responses, release and campaign calendar, economy catalog and accounting rules, event dictionary, experiment history, feedback access, and the director's current decision. |

### 2.16 Event planning: analysis vs logging code (against the analytics skill)

The analytics skill owns the logging code and limits. The analyst notes own the decision and the observation. Skill line numbers are `.agents/skills/analytics/SKILL.md`.

| AP contract field (AP:377) | Owner | Skill link |
| --- | --- | --- |
| semantic name | analysis picks the meaning | skill picks the method and name slot: funnel, economy or custom event (T-04, line 34); 100 custom names max (T-05, line 35) |
| exact trigger | analysis states it | skill: fire on the server after the action succeeded (T-01, T-03, lines 31, 33) |
| eligible population | analysis | skill: put segment fields on funnel step 1 (T-08, line 38) |
| unit (player, session, attempt) | analysis | skill: repeating flows get a new run GUID (T-04, line 34) |
| success/failure meaning | analysis | see tension in section 6 (T-03 logs success, AP also wants tries and failure reasons) |
| time basis | analysis | not in the skill; ask engineering |
| required properties and supported dimensions | analysis chooses what must be known | skill limits it: 3 custom fields, bucketed values, 8,000 combinations (T-05, T-06, lines 35-36) |
| currency or amount units | logging | skill: LogEconomyEvent, amount always positive, 10 currencies, 20 transaction types, 100 SKUs (T-04, T-05) |
| deduplication meaning | analysis defines | skill: save a flag for one-time steps (T-07, line 37) |
| version | analysis | skill: append steps, never renumber (T-08); where the version lives is open (one of three custom fields?) |
| sampling plan | analysis | skill: never per frame or per hit; aggregate (T-07); rate limit 120 + 20 x CCU per minute (T-05) |
| privacy purpose | analysis plus policy | skill rule: no typed text or personal data in fields (line 46); `platform-policy` |
| retention policy | analysis | platform fixed: events roll off 90 days after last data (T-05, line 35). So the analyst must archive aggregates (PR-AF05) |
| owner | analysis | skill: a row in `knowledge/design/telemetry.md` (line 11) |
| report or decision it enables | analysis | skill rule: no event without a plan row naming the question (line 47) |

## 3. Fact-check table (every I-cited claim)

Read 2026-10-21. "extract" = WebFetch returned a small-model extract of the page; that is the only evidence for the row unless another source is named. Verdicts: confirmed / corrected / unverified-kept-with-label / dropped.

| PR-id | claim (paraphrase) | AP:line | checked against (URL, date read, what the page supports) | verdict | corrected text or reason |
| --- | --- | --- | --- | --- | --- |
| C01 (I1; PR-F03) | I1 is a GrowthBook podcast interview with Shan Huang of Supercell, dated 2026-09-01 | 749-751 | https://www.growthbook.io/podcast/episode/1-36 read 2026-10-21 (extract). Page: "The Experimentation Edge" S1 E36; Huang is a data scientist on Supercell's central experimentation team; dated 2026-09-01; summary plus full transcript | confirmed | Host is a vendor (GrowthBook); the interview is a guest account. |
| C02 (I1; PR-F03) | Interview stresses retention | 230 | same page (extract). Transcript: retention is "our let's say North Star metrics most of the time" | confirmed | "Most of the time" is a limit: it is the main metric, not the only one. |
| C03 (I1; PR-F03, PR-R12) | Interview stresses player trust | 230 | same page, second read (extract). The word trust is in the page title, URL and host's words. The guest speaks of transparency and fairness and of players resting assured | corrected | Write: "stresses transparency to players and fair treatment" and keep "trust" as the host's and title's frame, not the guest's word. |
| C04 (I1; PR-F03) | Experiments are explained to players in advance; make-up events preserve fairness | 230 | same page (extract). Community managers tell players upfront that testing is coming; players who do not get the better experience "will always have a make-up event later on" | confirmed | The page does not say what a make-up event contains. Do not add detail. |
| C05 (I1; PR-AI05) | Fewer than 100 A/B tests a quarter | 472, 490 | same page (extract). Transcript: "less than a hundred AB test per quarter" for the whole company: four or five big games and a few small ones, about 10 to 20 per game | confirmed | Scope: company-wide, not per game. Not stated whether store or user-acquisition experiments are inside it. Do not use as a quota or a norm. |
| C06 (I1; PR-AI05) | Growing concern about consistency as AI opens analysis to more staff | 472 | same page, second read (extract). Guest says almost anyone can now run and read experiments with AI and asks how to keep AI analysis quality consistent | confirmed | A stated question and worry, not a measured problem. |
| C07 (I1) | Quote that a better game experience brings business results naturally | 750 | same page (extract). A pull quote matches; transcript has one variant ("comes") | confirmed | Quote as the guest's belief, not a finding. |
| C08 (I1, I10; PR-AI05) | Supercell shows "comparatively limited test cadence" next to a King practitioner's "extensive testing" | 482 (outside my range; found by grep) | I1 page: <100 per quarter company-wide. I10 page: one feature's process only (see C43) | corrected | "Comparatively limited" is the paper's reading. The King page gives no cadence, so the contrast has no support. Drop "extensive testing"; keep Supercell's number with its scope. |
| C09 (I2; PR-P03) | King experiment had more than 14 million consumers | 220, 234 | https://pmc.ncbi.nlm.nih.gov/articles/PMC4941432/ read 2026-10-21 (extract of the full paper). Abstract: "more than 14 million consumers" | confirmed | Study: Levitt, List, Neckermann, Nelson. PNAS 113(27), 2016-07-05. |
| C10 (I2; PR-P03) | Discounts of 9-70% on large purchases | 220, 234 | same page (extract). Abstract: price cuts of 9% to 70% for large purchases. Body: four arms, top discounts 9%, 23%, 55%, 73%; prices varied only for buys of 100 or more gold bars; the game is not named in the paper | confirmed | Keep "9-70%" as the abstract states it. Add scope: large virtual-currency bundles only; deepest arm was 73% in the body. |
| C11 (I2; PR-P03) | Revenue changed little | 220 | same page (extract). Abstract: "remarkably little impact on revenue." Body: revenue per user within 1% in three arms; the deepest-discount arm was about 10% lower over 12 weeks (extract numbers) | corrected | Write: "little change in three arms; the deepest-discount arm earned about 10% less (extract; verify in full paper before quoting the number)." |
| C12 (I2; PR-P03) | Purchases shifted among existing buyers, not new buyers | 220 | same page (extract). Abstract: virtually no rise in the number of buyers; all changes came from people who already bought. Body (extract): share of buyers about 0.026 in all arms | confirmed | The study also reports some sign of habit formation after prices returned (extract), and that infrequent buyers reacted more. |
| C13 (I2; PR-P03) | Offered tests: stockpiling, first-payer recruitment, later spend, retention | 220 | same page (extract). Paper reports buyers of big bundles used goods fast and did not store them; authors say it is hard to know how far results travel | confirmed (as OPINION) | The study did not find stockpiling. Keep stockpiling as a thing to check on Roblox, not as a finding. The paper's own warning on limits can support the AP caution. |
| C14 (I2) | Date and DOI: PNAS 2016-07-05, 10.1073/pnas.1510501113 | 753 | same page (extract). Date and DOI match | confirmed | |
| C15 (I3; PR-D09, PR-R06) | Riot uses surveys, analytics and lab observation | 177 | https://www.riotgames.com/en/work-with-us/disciplines/insights/get-data-informed-on-the-insights-blog read 2026-10-21 (extract). Names three tools: surveys (what players say), analytics (what they do), lab studies (watch in person) | confirmed | The page is a studio recruiting and blog page. It is a practice statement, not a study. |
| C16 (I3; PR-D09, PR-D15) | Yasuo showed a 36 percent win rate at release | 177, 193 | same page (extract). "limped onto Summoner's Rift with a 36 percent win rate" at launch with patch 3.15, Dec 2013 | confirmed | The page does not say whether 36% covers first games or the whole launch period, or give a sample size. Say "36 percent at release (sample not stated)". |
| C17 (I3; PR-D09) | Win rate passed 50% after about 35 games | 177, 193 | same page (extract). Win rate "did actually climb past the 50% point" at about 35 games with the champion; the figure at that point is not given; a chart is shown but its values are not in text | confirmed | Keep "something like 35 games" as approximate. |
| C18 (I3; PR-D09) | The learning curve "changed the balancing interpretation" | 177 | same page (extract). Page shows win rate by games played; says Riot tuned the champion back with minor nerfs by patch 4.2 | unverified-kept-with-label | The page shows the learning curve. It does not say it changed Riot's balance decision. Label as the paper's reading. One champion at one time: not a rule. |
| C19 (I3) | Date 2015-11-16 | 757 | same page (extract). Date matches | confirmed | |
| C20 (I4; PR-D10, PR-R06) | Valve treats designs as hypotheses and playtests as experiments | 179 | https://gmtk.substack.com/p/valves-secret-weapon (extract: Ambinder quote that designs are hypotheses and playtests are experiments); https://game.watch.impress.co.jp/docs/news/080132.html (extract of a GDC 2009 report); the slide PDF could not be read | confirmed (second-hand) | Slides not read by me. Two secondary sources agree. |
| C21 (I4; PR-D10) | Slides discuss observer bias | 179 | Game Watch report (extract): the observer's presence affects how people play; lab sessions are artificial | confirmed (second-hand) | Content from a report, not the slide text. |
| C22 (I4; PR-D10) | Slides discuss think-aloud as a distraction | 179 | Game Watch report (extract): talking aloud can get in the way of play and what people say can be imprecise; useful for why players act | confirmed (second-hand) | Say "can interfere and can be imprecise", not "is bad". |
| C23 (I4; PR-D10) | Slides discuss averages hiding extremes | 179 | Game Watch report (extract): statistics can hide extreme data and lose nuance; use them to add to other methods | confirmed (second-hand) | |
| C24 (I4) | GDC 2009, exact day not established | 761 | https://www.gdcvault.com/play/1566/Valve-s-Approach-to-Playtesting (extract): speaker Mike Ambinder, GDC 2009, no day, no abstract | confirmed | Keep "2009". The AP's applied lessons (no coaching; actions before reasons; comprehension apart from timing) are OPINION, not Valve's words. |
| C25 (I5; PR-D11) | Ubisoft's research lead describes testing the gap between design intention and player experience | 181, 766 | https://toronto.ubisoft.com/people-of-ubisoft-toronto-meet-elise-bisson-user-research-craft-lead/ read 2026-10-21 (extract). Quote: "identify when there's a gap between the design intention and the player's experience." | confirmed | Title on page: User Research Craft Lead, Ubisoft Toronto. |
| C26 (I5; PR-D11, PR-RP08) | Designers keep design responsibility | 181, 440 | same page (extract). She says researchers "don't (and shouldn't) tell designers how to make their games" | confirmed | Researchers pass findings to teams who choose the fix. |
| C27 (I5) | Date 2023-03-23 | 765 | same page (extract). Date matches | confirmed | A profile interview, not a method paper. |
| C28 (I6; PR-D12) | Seven months of behavior from over 3 million players | 183, 194 | https://www.microsoft.com/en-us/research/publication/mastering-the-art-of-war-how-patterns-of-gameplay-influence-skill-in-halo/ read 2026-10-21 (extract): skill ratings (TrueSkill) from Halo multiplayer matches, seven months, over three million players. The paper PDF could not be read | confirmed (second-hand) | The study is about skill change in multiplayer play, not retention. |
| C29 (I6; PR-D12) | 70-person survey | 183, 770 | same page (extract): a survey of 70 participants compared self-perception with game data | confirmed (second-hand) | |
| C30 (I6; PR-D12) | The two methods let the authors compare observed patterns with players' own explanations; big behavior data did not remove the need for qualitative reading | 183 | same page (extract): the survey compares players' self-perceptions with data | corrected | First half is supported. The second half ("did not remove the need") is the paper's inference; say so. Keep the claim narrow: a small survey (70) was used to check and explain data from millions. |
| C31 (I6) | Date April 2013, CHI | 769 | same page (extract): CHI 2013, April 2013 | confirmed | Exact day not stated (AP says the same). |
| C32 (I7; PR-FB06, PR-R14) | Steam says reviews are one feedback channel | 360, 774 | https://partner.steamgames.com/doc/store/reviews read 2026-10-21 (extract). "Reviews should be used as one channel for feedback" | confirmed | Official Steamworks doc advice, not a study. |
| C33 (I7; PR-FB06) | Steam cautions against letting reviews dominate development | 360 | same page (extract): do not let reviews "dominate or distract efforts away from the product"; also advises capping time spent reading | confirmed | The AP's wider rule (count contributors, silence is not approval) is the paper's OPINION and is not on the Steam page. |
| C34 (I7) | Page undated | 773 | same page: no revision date visible in the extract | confirmed | |
| C35 (I8; PR-FB06) | Activision abstract describes linking in-game fun surveys with disconnects, maps, performance, then forming experiments | 360 | https://gdcvault.com/play/1025985/Did-You-Have-Fun-Analytics read 2026-10-21 (extract). Abstract: surveys used to predict what drives fun; disconnecting, certain maps, player and team performance are named as examples; the talk will show how to turn such insight into design experiments | corrected | Write: "the abstract says surveys were used to predict what makes a match fun, naming disconnects, maps and performance as examples; it promises a method for turning insight into experiments. It does not say experiments were run or what they found." |
| C36 (I8) | GDC 2019, day not established | 777 | same page (extract): GDC 2019, no date | confirmed | Abstract only; full talk not seen. |
| C37 (I8, I4; PR-AE11) | I4 and I8 support "more play time is not more enjoyment" | 629 | I4 evidence: C20-C23 (no play-time point seen). I8 abstract: fun is the key measure (extract); no claim about time | unverified-kept-with-label | Neither page says play time misleads. The rule stays as the paper's OPINION. Cite I8 only for "measure fun by asking players". |
| C38 (I9; PR-FB07) | GDC session: diaries, surveys, analytics, in-house playtests across early and long play | 362, 782 | https://www.gdcvault.com/play/1026091/Research-Methods-to-Improve-Live read 2026-10-21 (extract). Session "Research Methods to Improve Live Game Retention, D1 to D100"; GDC 2019 microtalk; methods named: player diaries, analytics, surveys, in-house playtests; day 1 to day 100 and beyond | confirmed | Day not stated. |
| C39 (I9; PR-FB07) | The session is one source ("the GDC retention-research session") | 362 | same page (extract). Five speakers: Sebastian Long (Player Research), two from Glu Mobile, one from Sony PlayStation, one from Scopely | corrected | Write: "a microtalk with five speakers from several companies; each topic is short." It is not one studio's practice. Diaries were described for live content engagement in a console sports game (extract); no numbers given. |
| C40 (I10; PR-EV08) | King practitioner: prototyping, interviews, iteration, remote tests, then a live A/B test | 403, 785 | https://robertochaves.portfolio.site/candy-crush read 2026-10-21 (extract). Steps match: design sprint, prototypes (three groups), interviews, iteration, online remote play tests, one version A/B tested live | confirmed | One feature's process on one portfolio page. |
| C41 (I10; PR-EV08) | "King's practitioner account"; feature is the Mystery Machine | 403 | same page (extract). Author says he consulted for King on three occasions; the feature belongs to Candy Crush Soda | corrected | Write: "a consultant's portfolio account of one feature in Candy Crush Soda". Not an employee statement, not company policy. |
| C42 (I10; PR-EV09) | One-week sprint reported | 409 | same page (extract): "we did a one week Design Sprint" | confirmed | The week is the design sprint only, not the whole cycle through live test. |
| C43 (I10; PR-EV08, C08) | A King practitioner describes extensive testing (used against Supercell) | 482 | same page (extract): one feature's process; no counts, no cadence | dropped | No support for "extensive". Remove the claim. |
| C44 (I11; PR-RP04) | Zynga announcement dated 2022-09-12 | 789 | https://www.zynga.com/blog/zynga-completes-acquisition-of-mobile-growth-platform-storemaven/ read 2026-10-21 (extract): dated 2022-09-12 | confirmed | |
| C45 (I11; PR-RP04) | Zynga's public account links creative optimization, growth experiments and performance measurement | 426 | same page (extract). The release says Storemaven helped game developers "optimize their creatives, conduct growth experiments, and measure performance" | corrected | Write: "a Zynga press release about buying a growth-tool company says that company's tools serve creative testing, growth experiments and measurement." It describes the product bought, not Zynga's own proven practice. Case type: vendor and acquisition announcement. |
| C46 (I11; PR-RP04) | The announcement gives no Zynga retention targets | 426 | same page (extract): no retention targets, benchmarks or internal data | confirmed | |
| C47 (I12; PR-extra at AP:251) | Dhawan abstract frames evaluation around metric distributions and highly engaged players | 251, 793-795 | https://www.gdcvault.com/play/1023268/Evaluating-Game-Experiments-A-More read 2026-10-21 (extract). Quote: "it is essential to understand the distributions of key metrics for players." Method "takes into account the actions of the most engaged players" | confirmed | GDC 2016, no day. Outside my line range; included for completeness. |
| C48 (I12) | The abstract names no estimator and no numeric gain | 251 | same page (extract): says only that it can "significantly improve the accuracy" of results; no figures or method | confirmed | The AP caution is right. Do not quote any accuracy gain. |

## 4. Procedures ready to lift

### 4.1 Diagnosis checklist: "players are leaving" (AP:495-513)

Run in order. PASS = the check is supported by evidence. FAIL = stop that inference and do the FAIL action. A pass on one step does not certify the whole analysis. Keep the query, output and analyst judgment for each row.

| Step | AP:line | PASS condition | FAIL action |
| --- | --- | --- | --- |
| 1 Define the loss | 499 | Named outcome, population, dates, baseline, numerator, denominator | Replace "leaving" with a measurable question |
| 2 Verify measurement | 500 | Stable definitions, extraction status, logging coverage and version; totals reconcile | Repair or bound the measurement problem before claiming behavior changed |
| 3 Check maturity | 501 | Compared cohorts have equal completed follow-up | Wait, compare mature cohorts, or label early indicators separately |
| 4 Check reliability | 502 | Counts and uncertainty support the claimed change; no unexplained missing segment | Report insufficient evidence; get the missing data |
| 5 Check acquisition composition | 503 | Source and new/returning mix considered; retained counts shown beside rates | Recompute within comparable populations; do not blame onboarding yet |
| 6 Check technical experience | 504 | Join outcomes, crash counts, FPS and memory tails, version and device examined | Investigate affected devices and builds; separate technical from voluntary exits |
| 7 Locate the break | 505 | Eligible funnel denominators, incomplete attempts, elapsed and active time examined | Name the missing measurement or inspect sessions and playtests |
| 8 Check progression | 506 | Time, attempts, affordability and completion fractions assessed, non-completers included | Test difficulty, clarity, resource shortfall, content exhaustion separately |
| 9 Check economy and purchase | 507 | Supply and sinks, offer eligibility, delivery, progression fairness examined where relevant | Reconcile currency and purchase flows before reading spend |
| 10 Seek competing explanations | 508 | Several plausible mechanisms with disproving predictions recorded | Make alternatives before choosing a recommendation |
| 11 Triangulate | 509 | Behavior agrees with observation and feedback, or the gaps are explained | Recruit the affected audience; look into the conflicting evidence |
| 12 Bound causality | 510 | Wording fits the design; observational alternatives still visible | Downgrade "caused" to "associated", or design a valid intervention |
| 13 Make one decision | 511 | One action with owner, target population, expected mechanism, success measure, review date | Return one next measurement or test, not a bundle of guesses |

Two rules attached (AP:513): a verified severe technical defect = repair now, keep evidence, do not wait for a cohort. Uncertain and costly = recommend the most decision-relevant missing measurement or test. "Investigate everything" is not usable.

### 4.2 Weekly report fields (AP:587-613)

Rule: decision report is short; queries and segment detail go in an audit attachment; no forced causal story (AP:587).

1. Game | reporting dates and timezone | data finalized through (AP:589)
2. ONE MAIN FINDING: one plain sentence on player behavior, with population and comparison (AP:590)
3. EVIDENCE: counts, rate or amount, comparable baseline, meaningful uncertainty (AP:591)
4. HOW SURE: High / moderate / low, with reasons from design, data quality, precision; no made-up probability (AP:592)
5. ONE RECOMMENDATION: action + owner + target players + success measure + review date (AP:593)
6. Measures table, columns "current value and denominator | comparable baseline | interpretation" (AP:595-604), eight rows:
   - New players and acquisition mix. Interpretation: did the audience change?
   - First-session core-loop completion: eligible N and completed N. Interpretation: where are new players blocked?
   - Mature D1 / D7 / D30 cohorts: separate cohort dates and counts; equal follow-up. Interpretation: do players return?
   - Session time and visits per player: aligned population. Interpretation: longer visits or more visits?
   - Progression milestone and affordability: completion fraction and timing. Interpretation: clarity, challenge, resource wall or exhaustion?
   - Payer conversion / ARPPU / ARPDAU: revenue basis and period. Interpretation: more buyers, more purchases, or more spend per buyer?
   - Currency stock and net flows: currency, population, adjustments. Interpretation: meaningful scarcity and sink use?
   - Performance: affected device and version, count and tail; matched population. Interpretation: who has a poor technical experience?
7. Updates and tests: what shipped; valid result or still immature; next decision date (AP:606)
8. Player voice: theme, unique contributors or comments, channel, counterexamples, behavior match (AP:607)
9. Chart: one chart that answers the main question; raw N; labeled units; uncertainty or cohort maturity (AP:608)
10. Owner decision needed: a specific decision, or "none this week" (AP:609)
11. Limits: missing data, traffic shifts, measurement breaks, open alternatives (AP:610)
12. Links: data, plan, query, codebook, prior decision (AP:611)
13. Routing note: see 4.5 (AP:613)

Not in my line range, but tied to this report: the four verdict sentences for experiments (AP:580-583) belong to the experiment note.

### 4.3 Event contract fields (AP:375-379, 399-401)

Before listing events, write the decision, the competing explanations and the fewest observations that tell them apart (AP:375). Then each event has these 16 fields (AP:377):

1. semantic name
2. exact trigger
3. eligible population
4. unit
5. success or failure meaning
6. time basis
7. required properties
8. supported dimensions
9. currency and amount units, where relevant
10. deduplication meaning
11. version
12. sampling plan
13. privacy purpose
14. retention policy
15. owner
16. report or decision it enables

Naming (AP:379): stable and outcome-style (feature_entered, reward_granted). Changing ids go in controlled properties. Exposure apart from selection. Success apart from delivery. No raw chat or free text. No fine movement or every attack unless a defined decision needs it.
Versioning (AP:377): a change in meaning needs a version boundary and a comparability note.
Observation stages (AP:408): opportunity, action, result, delivery.
Acceptance before ship (AP:399): walk successful, canceled, retried, interrupted, returning-player journeys; reconcile totals with an independent authoritative record; check missing properties and impossible order; both test arms measured equally; define what happens with no terminal event; claim no quit reason without evidence.
Sampling and accounting (AP:401): authoritative money and progression accounting apart from sampled diagnostics; record the inclusion rule for a sample; never read a sample as a count.
Retirement (AP:401): remove a measurement when no decision uses it; keep its definition and history.
Split of work: fields above are analysis. Writing the call, bucketing, limits and the telemetry module are logging (see 2.16).

### 4.4 Feedback codebook fields and checks (AP:352-356)

Codebook (versioned), one row per coded comment or response (AP:352):
1. topic
2. feature or stage
3. sentiment
4. report type: bug, comprehension, difficulty, fairness, preference, request
5. severity
6. evidence span
7. confidence
8. unknown or other

Rules: several themes per comment allowed (shares need not total 100%); raw wording and source id kept in a protected audit trail; summaries point to exact examples; request kept apart from need.
Validation (AP:354): humans label a varied sample (languages, devices, positive/negative/neutral, rare severe problems) -> compare model labels -> review disagreements -> revise the codebook -> only then bulk coding. Audit precision and recall per theme. Record doubt for sarcasm, slang, short comments, translation. No invented reasons for quitting.
Denominators (AP:356): theme rate = contributors mentioning the theme / contributors in this source and window. Also source participation versus eligible players, respondent mix versus player mix. Weighting fixes known mix gaps only. Silence is not satisfaction.
Source filters (AP:348): in-game = exposure and survival filter; Roblox ratings = reviewer filter; Discord = community participants; social = onlookers and copied complaints. Authorized data only; minimal identifiers; deduplicate where legitimate; else report comment counts.
Triangulation (AP:360-364): connect each complaint to eligibility, attempt, failure and device evidence; a severe repeatable bug can justify action with few reports; diaries or interviews for gaps logs cannot explain, with no leading prompts; AI-generated themes are leads, not proof.

### 4.5 Recipient routing table (AP:418-424, 613)

| Recipient | Needs from the finding | Boundary | AP:line |
| --- | --- | --- | --- |
| Creative director | Main change, business and player impact, uncertainty, one decision | Do not hide trade-offs behind a combined score | 420 |
| Game designer | The affected journey and the likely comprehension or gameplay mechanism | Diagnosis supports design; it does not dictate a full redesign | 421 |
| Progression designer | Time, attempt or affordability bottleneck and the affected cohort | No global pacing change from survivors alone | 422 |
| Marketing agent | Source quality, promise match, value of mature cohorts | Attribution is not automatically incrementality | 423 |
| Live-ops designer | Event reach, use, displacement, return after the event | A launch spike is not lasting engagement | 424 |

Routing note in the weekly report (AP:613): game designer = comprehension and challenge; progression designer = pace and resources; marketing agent = acquisition promise and quality; live-ops designer = timing, content, return; creative director = priority and trade-off.
Ownership (AP:426, 440): analyst owns evidence; marketing owns its execution; designer chooses the fix.

## 5. Gaps for a non-expert owner

Short sentences, one idea each. Terms are the paper's words; the plain version is mine (inference, not checked against a style tool).

| AP:line | Paper wording | Plain version |
| --- | --- | --- |
| 20, 38 | "denominator, unit, time window, population, definition version" | "Say what we counted. Say out of whom. Say which days. Say which players. Say which version of the rule." |
| 151 | "marginal charts", "standardized to fixed baseline segment weights" | "Two separate charts cannot show a joint effect. We re-count with the same player mix as before, so a change in mix does not trick us." |
| 167 | "conditional completion", "overall completion" | "Of those who reached this step, how many finished it. Of all who started, how many finished it." |
| 171 | "retain non-completers", "survivors", "censoring" | "Count players who did not finish, too. If we count only finishers, a hard feature looks easy. 'Not yet' is not 'never'." |
| 189 | "causal language ladder", "identification" | "We say 'it happened' for what we saw. We say 'linked to' when we compared groups. We say 'caused' only after a fair test." |
| 216, 626 | "fulfillment", "treatment can change who becomes a buyer" | "Did the player get what they paid for? A change can make different people buy. So compare all eligible players, not only buyers." |
| 206 | "accounting identity", "boundary", "adjustments" | "Start stock + coins made - coins removed + coins that crossed in or out + fixes = end stock. Every coin must have a home." |
| 210 | "quality-consistent basket" | "Track the price of the same items over time. If the items changed, the price change means nothing." |
| 348 | "exposure/survival filter" | "Only players who saw the survey and stayed long enough could answer it." |
| 354 | "precision and recall per theme" | "How often a tag was right. How many real cases it caught. Check both for each theme." |
| 356 | "contributors / contributors in this source and window" | "How many people raised it, out of how many people we heard from, in this place and these days." |
| 356 | "nonresponse mechanisms" | "We do not know why quiet players are quiet. Do not guess that they are happy." |
| 377 | "deduplication meaning", "time basis" | "When two events count as one. Which clock the time comes from." |
| 379 | "exposure vs selection vs success vs delivery" | "Saw it. Chose it. Did it work. Got the reward. Four different events." |
| 416 | "certainty about measurement / cause / expected value of action" | "Are the numbers right? Do we know why? Is acting worth the risk? Three separate answers." |
| 423 | "attribution is not incrementality" | "A source that gets credit for a player may not have caused that player to come." |
| 432 | "dual-axis", "truncated axes" | "Do not draw two lines with two scales on one chart. Do not cut the axis so a tiny gap looks big." |
| 447-460 | "Identify", "Localize", "Triangulate" | "Pick how we will know the cause. Find where it happens. Check with a second kind of evidence." |
| 464-466 | "grain", "leakage" | "Check what one row stands for before joining tables. Do not use facts from after the event to explain it." |
| 470 | "exploratory unless prespecified" | "If we hunt through many splits, a good-looking one may be chance. Mark it 'a lead' until we test it again." |
| 592 | "How sure: High / moderate / low" | Keep the three words. Add one line of reasons: how clean the data is, how big the sample is, whether we ran a fair test. |
| 426 | "attribution", "creative" | "Which ad, thumbnail or video brought which players, and whether those players stayed." |

## 6. Disagreements and dropped claims

| # | Item | AP:line | Reason | Action |
| --- | --- | --- | --- | --- |
| 1 | Zynga I11 is a description of the purchased product, not Zynga's own practice | 426 | C45. A press release on buying a tool company. | Corrected. Say "vendor and acquisition announcement." |
| 2 | Activision I8 abstract says insights can be turned into experiments; AP says findings formed experiments | 360 | C35. The abstract promises a method; no experiment is described. | Corrected. |
| 3 | King practitioner I10 is a consultant for Candy Crush Soda; "extensive testing" has no support | 403, 482 | C41, C43. | Corrected / dropped. |
| 4 | "Player trust" is the host and title's word, not Supercell's guest's | 230 | C03. | Corrected. |
| 5 | "Fewer than 100 tests a quarter" is company-wide, about 10 to 20 per game | 472, 490 | C05. | Add scope. A "comparatively limited cadence" reading (482) is the paper's inference. |
| 6 | King revenue "changed little" hides a deepest-arm drop of about 10% | 220 | C11 (extract numbers). | Corrected; verify in full paper before quoting the number. |
| 7 | Riot "learning curve changed the balancing interpretation" | 177 | C18. Page shows the curve and a later nerf; no statement on the decision. | unverified-kept-with-label. Do not turn into a rule. |
| 8 | I4 and I8 cited for "play time is not enjoyment" | 629 | C37. Neither source says it. | Keep the rule as OPINION; change the cite. |
| 9 | Halo "need for qualitative interpretation" | 183 | C30. Paper's inference; the survey was small (70). | Corrected: narrow claim. |
| 10 | AP:395 names a specific game's checkpoints | 395 | Game-specific content must not enter a universal note. | Dropped (PR-EV05). The general rule is kept in PR-EV04. |
| 11 | Tension with analytics skill T-03 ("log the success, not the attempt", skill line 33) versus AP:388 and AP:399 (entry tries, failure reasons, canceled and retried journeys) | 388, 399 | AP wants failures and tries as data; the skill says log after success. These fit if a try and its server-decided failure are logged as their own step or custom event, after the server decides. | needs-decision for the analytics skill owner: add a line to T-03 saying failures decided by the server are loggable. |
| 12 | AP event contract wants many properties per event; skill allows 3 custom fields, 8,000 combinations (T-05, T-06) | 377 | Contract fields like version, dimension list and context do not all fit three fields. | The analyst must rank fields by decision value and bucket values; a spare field can carry the version. Skill owner may confirm. |
| 13 | AP:645 vs analytics skill T-05: Roblox drops events 90 days after last data | 377 (retention policy), 645 | "Retention policy" cannot be set by the studio for platform events. | The contract's retention field = "archive aggregates on this schedule". |
| 14 | Tags: I7 is a Roblox-neutral official doc but tagged EXPERIENCE | 773 | Tag convention only. | Left as is. |
| 15 | I4 and I6 PDFs unread | 179, 183 | Tool limit (see section 1). | The claims are labeled "second-hand". A person with a PDF reader can confirm quickly. |

Counts for this note. Section 2: 125 rows (15 rules, 4 watch, 21 diagnosis incl. 7 hypothesis rows, 5 economy, 4 purchase, 4 fair, 9 feedback, 9 events, 8 reporting, 12 process steps, 5 AI controls, 2 appendix-A, 2 appendix-D, 15 appendix-E, 10 appendix-F) plus a 15-row analysis-vs-logging table. Section 3: 48 rows. Confirmed 37 (7 of them second-hand: C20-C23, C28, C29, C31; C13 is confirmed as an OPINION). Corrected 8 (C03, C08, C11, C30, C35, C39, C41, C45). Unverified-kept-with-label 2 (C18, C37). Dropped 1 (C43). Section 2 also drops one sentence (PR-EV05, game-specific).
