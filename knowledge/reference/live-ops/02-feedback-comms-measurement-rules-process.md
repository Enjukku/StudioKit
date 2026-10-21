---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: "J014-T02, live-ops-designer-research.txt lines 248-536"
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-21

# Live-ops paper part 2: player feedback, communication, measuring an update, long-term health, Roblox rules, the agent's process, templates, do-not-do table, open questions (lines 248-536)

Paraphrased notes. The paper (LP) stays outside git. Every row cites `LP:<line>`. Nothing here is fact-checked: claims are the paper's, listed in section 10 for the fact-check pass. The paper's research cutoff is 2026-10-21. Several of its Roblox sources are undated live pages (read once, on 2026-10-21) or dated mid-2026 or later, so none can be confirmed from memory: check them live. The owner's rule for the paper: strong evidence, not gospel; check what matters (update rhythms, event effects, Roblox rules); drop what cannot be backed up. The paper's own limits sit next to the claims they limit and are collected in section 11. Extraction only: no web access was used.

## 0. How to read

| Key | Meaning |
| --- | --- |
| LP:n | Line n of `live-ops-designer-research.txt`. One paragraph = one line. This note covers LP:248-536. The source register is LP:537-749; only ids cited in lines 248-536 are resolved here (section 9). Register entries are cited by their first line. |
| Tag | The paper's own mark, copied unchanged. VERIFIED = documented platform fact or guidance, read by the paper in the cited source. EXPERIENCE = a studio's or vendor's reported practice or reading. OPINION = the paper's own proposal or synthesis; dated 2026-10-21, "originates in this paper" (LP:539). "none" = framing text the paper does not tag. Templates and the process tables carry the tag in their heading (OPINION). |
| Paragraph tag | The paper tags a paragraph with a mark at the start of each sentence group. When a VERIFIED group is followed by an OPINION group in the same line, the rows split them. A sentence sitting inside a VERIFIED group but written as the paper's inference is a row of Kind LIMIT and is flagged in X-33. |
| Kind (my label) | RULE = official rule, limit, age threshold or eligibility. MECH = documented platform capability or behavior. GUIDE = official recommendation, not a mandate. CASE = reported practice or outcome of a named studio. PROC = the paper's proposed procedure. DEF = a definition the paper proposes. TPL = a template element (field, column, check). LIMIT = a caveat. FRAME = framing. The paper uses only Tag. |
| Src | The paper's source id (R = Roblox documentation or official post, G = game studio or conference), resolved in section 9. Flags: [L] = undated live page, "checked 2026-10-21" is only the day it was read, access is not publication, live check needed. [PC] = source dated after 2026-06-01, live check needed. ix = the paper had only indexed official excerpts. abs = conference abstract only. |
| Row IDs | FB feedback prose; FT feedback template; CM communication; PN patch-notes template; ME measuring; FR failure-response table; LH long-term health; RR Roblox rules (section 5.1); RC Roblox rules and capabilities stated outside section 10 (5.3); RP the paper's procedure around the rules; ST process step; PR process prose; UB update-brief field; HO hand-off receiver; PV post-update review field; DN do-not-do row; OQ open question; N number; FC claim to check; X contradiction or limit. Written with a hyphen (FB-01). |
| Terms | CCU = concurrent users. DAU = daily active users. ARPU = average revenue per user (the paper uses the abbreviation without expanding it). KPI = key performance indicator. ITT = intention-to-treat (the paper uses the words, LP:350). RDC26 = Roblox Developers Conference 2026 (the paper's abbreviation). L = the paper's inactivity-window parameter (ME-04). |
| Priority (section 10) | P1 = Roblox rule or capability, age threshold, measurement method, any number. P2 = case date or schedule, and official guidance that states no rule, capability or number. P3 = framing. |
| Rule of use | OPINION rows are proposed checks, never Roblox policy. Never write "Roblox requires X" from an OPINION or PROC row. A studio's case is a mechanism or a practice, never a benchmark. The paper's "Evidence" cells in the do-not-do table keep their combined tags (for example "VERIFIED / OPINION") and are not split. |

## 1. Player feedback: collection, sorting, representation and closure (LP:248-285)

### 1.1 Evidence base and collection paths

| ID | LP | Kind | Content | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| FB-01 | 250 | GUIDE | Roblox testing guidance warns that community feedback can be biased and presents in-experience surveys as a way to widen participation. | VERIFIED | R13 [L] |
| FB-02 | 250 | CASE | Riot describes using focus groups, surveys and conversations across Discord and forums when it investigates player preferences. | EXPERIENCE | G28 |
| FB-03 | 250 | CASE | The 2022 GDC abstract "Feedback Fundamentals" concerns using community feedback before and after launch. The paper did not review the full presentation. | EXPERIENCE | G27 abs |
| FB-04 | 252 | PROC | Use several collection paths, because each reaches a different population. | OPINION | - |
| FB-05 | 252 | PROC | In-game prompts: reach current players near a relevant moment; miss players who already left. | OPINION | - |
| FB-06 | 252 | PROC | Discord: shows detailed discussion and very engaged members; not representative of everyone. | OPINION | - |
| FB-07 | 252 | PROC | Comments, ratings, reviews: can show expectations and trust; the author's experience, campaigns and platform context may be unclear. | OPINION | - |
| FB-08 | 252 | PROC | Support reports: show severe failures; filtered by who is willing and able to contact support. | OPINION | - |
| FB-09 | 252 | PROC | Behavioral data: reaches silent players; does not give their reasons without interpretation. | OPINION | - |

### 1.2 Asking, moderation, tagging, counting, minorities

| ID | LP | Kind | Content | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| FB-10 | 254 | PROC | Ask at a meaningful moment, with a small optional prompt that does not interrupt essential play. | OPINION | - |
| FB-11 | 254 | PROC | First ask what the player tried to do and what happened; only then (if at all) ask for a rating or a preferred solution. Avoid a leading question such as "How much did you love the new event?". | OPINION | - |
| FB-12 | 254 | PROC | Randomize who gets a prompt, or otherwise document it. Record eligibility, exposure and response counts. | OPINION | - |
| FB-13 | 254 | LIMIT | Surveying only players who completed an event systematically leaves out the players whose failure matters most. | OPINION | - |
| FB-14 | 254 | PROC | Offer neutral choices, and free text where moderation can support it. | OPINION | - |
| FB-15 | 256 | PROC | Keep community moderation and product research separate. Remove abuse under community rules; do not label legitimate criticism as abuse to improve sentiment. | OPINION | - |
| FB-16 | 256 | PROC | Send safety incidents, exploit reports and purchase or data-loss issues straight to the responsible owner; they must not wait to become a frequent theme. | OPINION | - |
| FB-17 | 256 | PROC | When closing the loop, do not repeat exploit steps or personal information in public. | OPINION | - |
| FB-18 | 258 | PROC | The AI first keeps the source excerpt and its context, then applies a stable taxonomy of eleven fields: area/system; player goal; observed symptom; suspected cause; requested solution; sentiment; severity; cohort; device/build; reproducibility; occurrence date. | OPINION | - |
| FB-19 | 258 | PROC | Separate "I cannot find the event entrance" from "give us more rewards", even if both are negative. | OPINION | - |
| FB-20 | 258 | PROC | Allow several tags per item, without counting one author twice in an aggregate theme. | OPINION | - |
| FB-21 | 258 | PROC | Keep contradictory sub-themes visible (example: some want a faster economy, others value scarcity). | OPINION | - |
| FB-22 | 260 | DEF | Count distinct authors per theme inside a defined source and time window. Keep message volume as a separate intensity signal. | OPINION | - |
| FB-23 | 260 | PROC | De-duplicate cross-posts where legitimate identity information allows it; otherwise report possible overlap. | OPINION | - |
| FB-24 | 260 | PROC | Never use a model's estimated count when a deterministic count is possible. | OPINION | - |
| FB-25 | 260 | DEF | Report theme authors divided by eligible sampled authors or respondents, as fits the source. Do not report theme messages divided by all DAU. | OPINION | - |
| FB-26 | 260 | LIMIT | A Discord poll estimates the views of the voters who took part, not of the whole game population. | OPINION | - |
| FB-27 | 260 | LIMIT | Weighting is defensible only with a known sampling model and analyst oversight. | OPINION | - |
| FB-28 | 262 | LIMIT | Loud minorities are neither automatically representative nor automatically wrong; detailed reports may expose a real exploit or an advanced-system problem. | OPINION | - |
| FB-29 | 262 | PROC | Use severity and reproducibility together with prevalence. | OPINION | - |
| FB-30 | 262 | LIMIT | Silent cohorts need behavior checks and targeted research; silence is not satisfaction. | OPINION | - |
| FB-31 | 262 | PROC | Ask whether the same friction shows up among new players, non-payers, mobile users, returning players and veterans. | OPINION | - |
| FB-32 | 262 | PROC | Do not infer sensitive attributes from language, usernames or spending. | OPINION | - |

### 1.3 Player feedback sorting template (LP:264-276, OPINION)

Header block (five fields):

| ID | LP | Field | What goes in it | Tag |
| --- | --- | --- | --- | --- |
| FT-01 | 266 | Collection window / game version | The period covered and the build. | OPINION |
| FT-02 | 267 | Source and sampling method | Where the feedback came from and how it was sampled. | OPINION |
| FT-03 | 268 | Eligible / exposed / responding population | Counts, definitions, and which fields are unavailable. | OPINION |
| FT-04 | 269 | Deduplication rule | Dedupe of authors within a source; limits of cross-source overlap. | OPINION |
| FT-05 | 270 | Taxonomy / codebook version and reviewer | Version of the codebook and who reviewed. | OPINION |

Theme table (eight columns; the paper shows one empty example row, LP:274):

| ID | LP | Column | Instruction in the cell | Tag |
| --- | --- | --- | --- | --- |
| FT-06 | 272, 274 | Theme ID | Identifier of the theme. | OPINION |
| FT-07 | 272, 274 | Player goal / symptom | Describe the problem separately from the solution the player asked for. | OPINION |
| FT-08 | 272, 274 | Evidence excerpts and source dates | Short faithful quote; link for context; no personal data. | OPINION |
| FT-09 | 272, 274 | Unique authors / denominator | A count; a denominator specific to the source; unknown overlap stated. | OPINION |
| FT-10 | 272, 274 | Cohort and severity | Observed, not inferred. | OPINION |
| FT-11 | 272, 274 | Behavioral corroboration | An analyst check, or "unknown". | OPINION |
| FT-12 | 272, 274 | Candidate response | One of: fix, research, explain, defer. | OPINION |
| FT-13 | 272, 274 | Status / owner / closure | Owner; reason; the follow-up to players. | OPINION |

Quality checks under the table (seven, LP:276):

| ID | LP | Check | Tag |
| --- | --- | --- | --- |
| FT-14 | 276 | Inspect raw examples from every important theme. | OPINION |
| FT-15 | 276 | Review ambiguous or contradictory assignments. | OPINION |
| FT-16 | 276 | Verify counts outside the language model. | OPINION |
| FT-17 | 276 | Keep a sample of excluded material, with the reasons for exclusion. | OPINION |
| FT-18 | 276 | Tell new themes apart from repeated discussion. | OPINION |
| FT-19 | 276 | Keep evidence that contradicts the preferred proposal. | OPINION |
| FT-20 | 276 | Report uncertainty instead of forcing each statement into a confident category. | OPINION |

### 1.4 Closing the loop

| ID | LP | Kind | Content | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| FB-33 | 278 | PROC | Give one consistent account with five parts: what players reported; what the studio verified; what changed; what is still unresolved; when the next status update is expected. | OPINION | - |
| FB-34 | 278 | LIMIT | "You asked, we did" fits only when the evidence supports that link. | OPINION | - |
| FB-35 | 278 | PROC | When declining a request, explain the design trade-off without blaming the audience. | OPINION | - |
| FB-36 | 278 | PROC | After the change, use feedback to check that the original problem was solved. Positive comments on an announcement do not show that shipped behavior improved. | OPINION | - |

The four summary rows at LP:282-285 are in the number register (N-01 to N-04).

## 2. Communication: promise, explain, orient, close the loop (LP:287-336)

### 2.1 Promise ledger, channel limits, notifications

| ID | LP | Kind | Content | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| CM-01 | 289 | PROC | Marketing and live ops share one promise ledger. Per claim record: approved feature; available audience; actual start and end time; reward conditions; exclusions; build readiness; fallback wording. | OPINION | - |
| CM-02 | 289 | PROC | A teaser must not run ahead of implementation evidence. If a feature slips, update every affected surface in the same way. | OPINION | - |
| CM-03 | 289 | PROC | Never leave an expired event label or an obsolete reward promise in the title, icon or description. | OPINION | - |
| CM-04 | 291 | MECH | Roblox experience events support opt-in reminders and attribution of entries to the event. | VERIFIED | R07 [L] |
| CM-05 | 291 | RULE | An experience can have at most 10 ongoing or upcoming events. | VERIFIED | R07 [L] |
| CM-06 | 291 | RULE | Update announcements allow 60 characters. | VERIFIED | R07 [L] |
| CM-07 | 291 | RULE | An update announcement can be sent once every 3 days. | VERIFIED | R07 [L] |
| CM-08 | 291 | LIMIT | These are channel constraints, not a recommendation to fill every slot or send at every chance. Send only when the recipient has a real reason to return. | OPINION | R07 [L] |
| CM-09 | 293 | RULE | Personalized experience notifications are a separate, opted-in feature for eligible users aged 13 and over. | VERIFIED | R08 [L] |
| CM-10 | 293 | RULE | Such notifications should relate to the user's own activity. Games must not require users to opt in. | VERIFIED | R08 [L] |
| CM-11 | 293 | PROC | Use an event or update announcement for broad news. Use a personalized notification only for a truthful, relevant, player-specific event. | OPINION | R08 [L] |
| CM-12 | 293 | PROC | Do not dress a generic sale as "your friend needs you". Do not create urgency when nothing expires. | OPINION | R08 [L] |

### 2.2 Sequence, roadmap, update tags

| ID | LP | Kind | Content | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| CM-13 | 295 | PROC | Sequence: announce the player benefit and timing once the work is credible; explain entry and eligibility at release; publish exact changes and known issues; give reminders near real deadlines; report the result or the next correction. | OPINION | - |
| CM-14 | 295 | PROC | Use the game's own UI to orient returning players. | OPINION | - |
| CM-15 | 295 | PROC | A Discord announcement must not be the only explanation of a Roblox feature, given the current social-link eligibility limits. | OPINION | R16 [L] |
| CM-16 | 297 | DEF | Public roadmap labels: "now" = approved and being delivered; "next" = prioritized but still subject to readiness; "exploring" = no promise. | OPINION | - |
| CM-17 | 297 | LIMIT | These labels are the paper's own convention, not a Roblox standard. | OPINION | - |
| CM-18 | 297 | PROC | Put dates only on work with credible dependencies and approved capacity. Show why a priority changed. The roadmap is a trust instrument, not a list of every idea the AI produced. | OPINION | - |
| CM-19 | 299 | MECH | Roblox's discovery documentation describes recommendation signals as player behavior, and names algorithm, seasonality, competition and game updates as possible drivers of change. | VERIFIED | R12 [L] |
| CM-20 | 299 | LIMIT | The official sources reviewed give no evidence that adding "[UPDATE]" guarantees a recommendation boost. A truthful tag may signal freshness to a person. | OPINION | R12 [L] |
| CM-21 | 299 | PROC | Title experiments must judge real audience behavior and keep the game's identity. Do not change title, icon, acquisition spend and onboarding all at once and then credit the patch alone. | OPINION | R12 [L] |

### 2.3 Patch notes template (LP:301-329, OPINION)

| ID | LP | Field | What goes in it |
| --- | --- | --- | --- |
| PN-01 | 303 | Title line | Update name; version; release timestamp with time zone. |
| PN-02 | 304 | Player-facing summary | What is better or newly possible. |
| PN-03 | 305 | Who can play / how to enter | Requirements; location; supported audience. |
| PN-04 | 306 | Event dates | Start; end of gameplay; a separate reward-claim deadline. |
| PN-05 | 308-309 | New content | Each addition: what, where it is, meaningful limits. |
| PN-06 | 311-314 | Balance and progression | Three entries: old value to new value, using verified shipped values; why it changed, which situations it touches, uncertainty where relevant; currency and reward migration, purchase effects, and the path for returning players. |
| PN-07 | 316-317 | Quality-of-life and fixes | The player-visible problem that was resolved; avoid unsupported claims such as "all lag fixed". |
| PN-08 | 319-320 | Known issues | Scope; workaround if safe; when the next status message comes; no invented fix date. |
| PN-09 | 322-323 | From your feedback | Theme, then verified problem, then the change or the decision to defer. |
| PN-10 | 325-326 | What to expect next | The approved next step or investigation; separate commitment from exploration. |
| PN-11 | 328-329 | Feedback route | In-game reporting and permitted community channels; no personal information published. |

The four summary rows at LP:333-336 are in the number register (N-05 to N-08).

## 3. Measuring an update: causal discipline and failure response (LP:338-374)

### 3.1 Roles, definitions

| ID | LP | Kind | Content | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| ME-01 | 340 | PROC | The analyst owns metric definitions, data quality, experimental analysis and uncertainty. The live-ops designer owns the decision hypothesis and reads the result together with the analyst. | OPINION | - |
| ME-02 | 340 | PROC | Before release agree eight items: target population; exposure or assignment definition; primary outcome; guardrails; baseline; comparison design; evaluation window; decision rule. | OPINION | - |
| ME-03 | 340 | PROC | The metric must fit the mechanism. A returner event is judged on qualified reactivation and later play, not only total DAU. | OPINION | - |
| ME-04 | 342 | DEF | Reactivation: for an inactivity window L, eligible lapsed players are those whose last qualifying activity was before a stated cutoff. | OPINION | - |
| ME-05 | 342 | DEF | Reactivation rate = eligible lapsed players who return in the measured window, divided by all eligible lapsed players in the defined reachable or assigned population. | OPINION | - |
| ME-06 | 342 | LIMIT | State whether the denominator is all lapsed accounts, contacted accounts, notification recipients or experiment assignments; these answer different questions. | OPINION | - |
| ME-07 | 342 | LIMIT | L is a parameter chosen from the game's own behavior, not a universal number the paper supplies. | OPINION | - |
| ME-08 | 344 | DEF | A retention definition needs six choices: exact-day or rolling return; first-ever cohort or event-entry cohort; calendar day or elapsed time; what counts as qualifying activity; time zone; how incomplete windows are treated. | OPINION | - |
| ME-09 | 344 | LIMIT | D1, D7 and D30 name observation intervals; they are not target rates. | OPINION | - |
| ME-10 | 344 | PROC | Do not report a mature D7 for cohorts that have not had the chance to reach it. | OPINION | - |
| ME-11 | 344 | PROC | Segment new, continuing and reactivated players. Do not average a changing acquisition mix into an apparent product improvement. | OPINION | - |

### 3.2 Event analytics, experiments, causal design

| ID | LP | Kind | Content | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| ME-12 | 346 | MECH | Roblox's event-analytics announcement supports comparing up to 3 past events, with context of 7 days before and 7 or 14 days after the event. | VERIFIED | R10 ix |
| ME-13 | 346 | LIMIT | These chart windows do not create a control group. (Written inside the VERIFIED group; it is the paper's inference: X-33.) | VERIFIED (as written) | R10 ix |
| ME-14 | 346 | PROC | Use the chart to find patterns and raise questions. | OPINION | - |
| ME-15 | 346 | LIMIT | Before/after changes can come from eight other causes: holidays; school schedules; acquisition spend; creator coverage; outages; algorithm changes; competing launches; regression to the mean. | OPINION | - |
| ME-16 | 346 | LIMIT | An event scheduled after a bad week can look successful even if it changed nothing. | OPINION | - |
| ME-17 | 348 | MECH | Roblox native experiments run 14-60 days and support up to 2 variants plus a control. | VERIFIED | R09 [L] |
| ME-18 | 348 | MECH | Metrics update every 24 hours; playtime, payer conversion and ARPU also update every 5 minutes during the first 24 hours. | VERIFIED | R09 [L] |
| ME-19 | 348 | PROC | Randomize at a unit that fits the design. | OPINION | - |
| ME-20 | 348 | LIMIT | Player-level assignment can contaminate results when the treatment changes a shared economy, server behavior or social group; the analyst must handle the interference or use another design. | OPINION | - |
| ME-21 | 348 | LIMIT | A global holiday event may have no clean simultaneous control; keep that limit visible. | OPINION | - |
| ME-22 | 350 | PROC | For the primary causal claim prefer intention-to-treat comparisons of assigned populations. | OPINION | - |
| ME-23 | 350 | LIMIT | Comparing players who chose to take part with those who did not mixes motivation with treatment. Track real exposure separately, for diagnosis. | OPINION | - |
| ME-24 | 350 | PROC | Do not drop unsuccessful participants after seeing results. Do not stop a test repeatedly at a favorable moment. Do not change the main metric after release. Do not read a non-significant result as proof of no effect. | OPINION | - |
| ME-25 | 350 | PROC | Report effect sizes and uncertainty suited to the method; the paper invents no universal confidence threshold. | OPINION | - |
| ME-26 | 352 | PROC | If traffic is too low to detect an economically meaningful effect, do not run an underpowered test just to get a green dashboard. Alternatives (five): instrumentation checks; usability research; bounded rollout; longer observation where defensible; a clearly labeled observational comparison. | OPINION | - |
| ME-27 | 352 | LIMIT | Pooling repeated similar events needs comparable populations and interventions. A historical control cannot fully remove unmeasured changes. | OPINION | - |

### 3.3 Revenue

| ID | LP | Kind | Content | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| ME-28 | 354 | PROC | Separate five revenue measures: payer conversion; spend per payer; revenue per active user; total receipts; purchase categories. | OPINION | - |
| ME-29 | 354 | PROC | Check whether new spend replaces existing spend, pulls forward a purchase that would have happened later, or rests on a few unusually large purchases. | OPINION | - |
| ME-30 | 354 | PROC | Where reliable cost data exists, judge net contribution after production, marketing and operating costs. | OPINION | - |
| ME-31 | 354 | LIMIT | Do not convert Robux to cash with a guessed exchange rate. Do not compare revenue between games without matching currency and period. | OPINION | - |

### 3.4 Failure-response table (LP:356-363)

Columns in the paper: observation; diagnostic questions; decision direction. The header carries the tag OPINION for the second and third columns.

| ID | LP | Observation | Diagnostic questions | Decision direction | Tag |
| --- | --- | --- | --- | --- | --- |
| FR-01 | 358 | DAU rises, later return does not | New arrivals or lapsed players? Were they qualified? Did the core game disappoint? | Improve the landing and core experience before repeating promotion. | OPINION |
| FR-02 | 359 | Revenue rises while retention or fairness worsens | Is spending concentrated? Did urgency or power advantages cause harm? | Review monetization and guardrails; do not declare an unconditional win. | OPINION |
| FR-03 | 360 | Event participation is low | Did eligible players see and understand the entrance? Is the activity accessible? | Repair discoverability and access before rejecting the whole theme. | OPINION |
| FR-04 | 361 | Participation is high, completion collapses | Where does progress stall: requirement, bug, skill, time, or reward relevance? | Fix the specific bottleneck; avoid blanket reward inflation. | OPINION |
| FR-05 | 362 | Event metrics improve, core queues decline | Did the event move existing play rather than add durable value? | Adjust scheduling, integration or queue structure. | OPINION |
| FR-06 | 363 | Metrics move but the data is inconsistent | Version mismatch, missing telemetry, assignment errors, delayed cohorts? | Resolve evidence quality; classify the result as unknown meanwhile. | OPINION |

### 3.5 When an update fails; the closing decision

| ID | LP | Kind | Content | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| ME-32 | 365 | PROC | First stop ongoing harm, using approved authority. | OPINION | - |
| ME-33 | 365 | PROC | Keep the logs and the exact deployed version. | OPINION | - |
| ME-34 | 365 | PROC | Disabling the problem feature can be safer than reverting the whole build. | OPINION | - |
| ME-35 | 365 | LIMIT | A code rollback does not automatically reverse persistent currency, traded items, purchases or progression; restoring can erase legitimate gains. | OPINION | - |
| ME-36 | 365 | PROC | Builders and progression design define the state-safe response before launch. | OPINION | - |
| ME-37 | 365 | PROC | Communicate the known scope; correct entitlements by supported means; do not promise refunds the studio cannot issue. | OPINION | - |
| ME-38 | 365, 374 | RULE | Roblox says experience creators cannot provide Robux or monetary refunds through the platform. (Sentence sits in an OPINION paragraph; the summary row LP:374 marks it VERIFIED: X-33.) | OPINION (paragraph) / VERIFIED (LP:374) | R22 [L] |
| ME-39 | 367 | PROC | End with a decision: repeat when mechanism and operating cost support it; revise when a specific fixable bottleneck is found; retire when value is too low or harm unacceptable; investigate when evidence is inconclusive. | OPINION | - |
| ME-40 | 367 | PROC | Record what would change that decision. | OPINION | - |
| ME-41 | 367 | PROC | Compare expected with actual effort as well as outcomes, so the next plan uses real production evidence. | OPINION | - |

The four summary rows at LP:371-374 are in the number register (N-09 to N-12).

## 4. Long-term health: economy, power, catch-up, burnout (LP:376-399)

| ID | LP | Kind | Content | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| LH-01 | 378 | GUIDE | Roblox's economy guidance links sources, sinks and the value of rewards, and warns that unusually generous event earnings can affect later spending. | VERIFIED | R06 [L] |
| LH-02 | 378 | LIMIT | The guidance's numerical fishing example is illustrative, not a measured live-game result (the register calls it explicitly fictitious). | VERIFIED | R06 [L] |
| LH-03 | 378 | PROC | The agent must tell teaching examples from empirical benchmarks, and never treat an invented example as a published revenue experiment. | OPINION | R06 [L] |
| LH-04 | 380 | PROC | Keep an economy ledger with eight items: currency issuance; currency removal; balances by cohort; inventories; acquisition rates; purchase prices; relevant trading prices; time to reach important goals. | OPINION | - |
| LH-05 | 380 | DEF | Expected event-reward issuance depends on five things: eligible participation; attempts; completion or award probabilities; repeat limits; modifiers. Report assumptions and ranges. | OPINION | - |
| LH-06 | 380 | PROC | Abuse scenarios include alternate accounts, automation, trading and compounding reward bonuses. | OPINION | - |
| LH-07 | 380 | LIMIT | A per-player cap does not necessarily bound total supply when identities can multiply. | OPINION | - |
| LH-08 | 382 | LIMIT | A larger currency balance is not inflation by itself; inflation concerns purchasing power and prices. A fixed-price shop can instead suffer less scarcity, shorter progression or exhausted demand. | OPINION | - |
| LH-09 | 382 | PROC | Inspect what players can buy, what they still want, how long earning takes and whether supply is concentrated. | OPINION | - |
| LH-10 | 382 | PROC | Trading economies need extra care: scarce inventory, arbitrage, and how event supply relates to old assets. | OPINION | - |
| LH-11 | 382 | PROC | The right response may be better goals or optional desirable sinks, not raising every price. | OPINION | - |
| LH-12 | 384 | PROC | Protect the meaning of existing progress. Prefer new strategic choices, expression and situational utility over pure power increases that make old content obsolete. | OPINION | - |
| LH-13 | 384 | PROC | If power must grow, progression design states how four things adapt: encounter difficulty; competitive matchmaking; returning-player access; prior purchases. | OPINION | - |
| LH-14 | 384 | PROC | Compare effective power in relevant contexts, not only item rarity. | OPINION | - |
| LH-15 | 384 | PROC | Do not offer a paid competitive advantage as the fix for a difficulty spike the update itself created. | OPINION | - |
| LH-16 | 386 | PROC | Audience needs. New players: a concise path to the main appeal. Veterans: mastery, identity, meaningful goals, respect for prior effort. Returning players: an explanation of changes, a clear next objective, restored basic competence, access to relevant social play. | OPINION | - |
| LH-17 | 386 | PROC | Catch-up removes obsolete friction but keeps valued achievements; progression need not become identical for everyone. | OPINION | - |
| LH-18 | 386 | PROC | Tools: optional recaps; guided loadouts; simplified prerequisites; earnable catch-up. Use them where they solve measured barriers. | OPINION | - |
| LH-19 | 386 | PROC | Do not dump every missed tutorial and system unlock on the first return. | OPINION | - |
| LH-20 | 388 | CASE | Overwatch's 2026 announcement explicitly includes returning-player orientation. | VERIFIED | G17 |
| LH-21 | 388 | CASE | Clash Royale's 2026 progression change explains how King Tower level is preserved. | EXPERIENCE | G24 |
| LH-22 | 388 | LIMIT | These show that migration and orientation matter, but neither source gives a portable Roblox retention lift for catch-up. Test the new entry path on the real returner cohort. | OPINION | G17, G24 |
| LH-23 | 390 | DEF | Burnout can show as: falling voluntary participation; abandoned stacked obligations; avoiding long claim routines; feedback about pressure. These are diagnostic signals, not a psychological diagnosis from telemetry. | OPINION | - |
| LH-24 | 390 | PROC | Reduce simultaneous chores; allow breaks and late entry; make optional play truly optional; watch whether rewards crowd out enjoyable play. | OPINION | - |
| LH-25 | 390 | PROC | Do not raise raw session length by making tasks slower or navigation more tedious. | OPINION | - |
| LH-26 | 392 | CASE | Adopt Me's schedule change ties production pressure to team wellbeing. | EXPERIENCE | G01 |
| LH-27 | 392 | DEF | For an AI studio, burnout also covers human review overload, endless exception handling, accumulated defects and a growing maintenance surface. | OPINION | - |
| LH-28 | 392 | LIMIT | Generating more plans can overload the owner faster than generating code adds capacity. | OPINION | - |
| LH-29 | 392 | PROC | Track five things next to content output: support load; escaped defects; rework; on-call coverage; estimate accuracy. | OPINION | - |
| LH-30 | 392 | PROC | A reusable event framework should make each release cheaper to run; if every event adds its own infrastructure, that benefit is not achieved. | OPINION | - |

The four summary rows at LP:396-399 are in the number register (N-13 to N-16).

## 5. Roblox rules: events, offers, random items, younger players (LP:401-429)

Highest-priority fact-check rows. Every row here has an FC row (section 10). Age thresholds are exactly as the paper states them; the paper never says whose age counts where noted.

### 5.1 Rules stated in section 10 of the paper

| ID | LP | Rule (paraphrase) | Applies to | Age threshold | Src and date | Tag | Register key line backs it? | FC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RR-01 | 405 | "Paid random items" cover direct purchases and indirect mechanisms involving currency that can be bought with Robux. | Paid random items | none stated | R14, undated; checked 2026-10-21 [L] | VERIFIED | no (key line covers only the 100% sum) | FC-28 |
| RR-02 | 405, 425 | All final outcomes and their numerical probabilities must be disclosed; the probabilities total exactly 100%. | Paid random items | none stated | R14 [L] | VERIFIED | yes | FC-29 |
| RR-03 | 405 | Changed odds, including relevant boosts or changed sets of eligible outcomes, must be shown accurately. | Paid random items | none stated | R14 [L] | VERIFIED | no | FC-30 |
| RR-04 | 405 | PolicyService restrictions include `ArePaidRandomItemsRestricted` and `IsPaidItemTradingAllowed`. (Wording "include": the list may not be complete.) | Paid random items; paid-item trading (code check) | none stated | R14 [L] | VERIFIED | no | FC-31 |
| RR-05 | 405, 425 | An official clarification dated 2026-05-26 reinforces compliance expectations for paid random items. | Paid random items | none stated | R15, 2026-05-26, ix | VERIFIED | yes (the line is about "more explicit" expectations, not their content) | FC-32 |
| RR-06 | 409, 426 | Experience and community social-link guidance: links are for age-checked users 16 and older. The paper does not say whether that age is the viewer's, the poster's or the community owner's (X-32). | Social links on experiences and communities (the paper says this is separate from profile-link guidance) | 16+, age-checked | R16, undated; checked 2026-10-21 [L] | VERIFIED | no | FC-33 |
| RR-07 | 409, 426 | Up to 3 links are permitted. | Experience and community social links | n/a | R16 [L] | VERIFIED | no | FC-34 |
| RR-08 | 409 | Links must not be shared directly inside experiences. | Social links; in-experience text | n/a | R16 [L] | VERIFIED | yes | FC-35 |
| RR-09 | 293, 411, 427 | Personalized experience notifications are a separate, opted-in feature with its own eligible age threshold. | Personalized experience notifications | 13+ (eligible users) | R08, undated; checked 2026-10-21 [L] | VERIFIED | no | FC-08 |
| RR-10 | 293, 411 | Compulsory opt-in is prohibited: games must not require users to turn notifications on. | Notifications | n/a | R08 [L] | VERIFIED | yes | FC-10 |
| RR-11 | 411, 419 | Deceptive pressure is prohibited in notifications; LP:419 words it as a "documented notification ban on false time pressure". | Notifications | n/a | R08 [L] | VERIFIED | no | FC-11 |
| RR-12 | 293 | Personalized notifications should relate to the user's activity. | Notifications | n/a | R08 [L] | VERIFIED | no | FC-09 |
| RR-13 | 413 | Creators must describe experience content through Roblox's maturity questionnaire. | Maturity of every experience | none stated | R17, undated; checked 2026-10-21 [L] | VERIFIED | partly (key line names the questionnaire only) | FC-36 |
| RR-14 | 415 | Ad integrations: check user eligibility and add the required advertising labels and disclosures. | Ads, sponsorship, brand integrations | threshold not stated | R18, undated; checked 2026-10-21 [L] | VERIFIED | yes | FC-37 |
| RR-15 | 417 | Community Standards restrict commercial use of sensitive real-world events. | All content, including holiday and trend events | none stated | R19, "live policy; date not established"; checked 2026-10-21 [L] | VERIFIED | no (key line is a heading) | FC-38 |
| RR-16 | 419, 429 | NO RULE CLAIMED. The sources the paper reviewed do not establish a blanket ban on truthful limited-time offers. The paper's ban on false time pressure is a notification rule, not a quote of an offer policy. | Limited-time offers | n/a | none; "review synthesis, 2026-10-21" | OPINION | n/a | FC-39 |
| RR-17 | 528 | Roblox's season-pass guidance and its notification prohibitions address different contexts. The paper says scarcity can support a seasonal identity while pressure can harm trust. | Season pass | n/a | R05, undated; checked 2026-10-21 [L] | OPINION (open-question paragraph) | no (key line gives a one-month starting point; the paper states no number) | FC-40 |

### 5.2 The paper's procedure around the rules (OPINION)

| ID | LP | Kind | Content | Tag |
| --- | --- | --- | --- | --- |
| RP-01 | 403 | PROC | Treat policy validation as a release gate with a named owner and current official source links. Past compliance is not enough once audience, reward mechanism, promotion channel or content changes. | OPINION |
| RP-02 | 403 | LIMIT | The section reports guidance checked at the research cutoff. It does not replace checking later revisions or applicable local requirements. | OPINION |
| RP-03 | 407 | PROC | Audit the whole chain Robux, then currency/key/ticket, then random reward, including bundles and paid probability modifiers. A "free" spin received through a paid bundle cannot be judged from the spin button alone. | OPINION |
| RP-04 | 407 | LIMIT | Do not assume a pity mechanic makes a random purchase deterministic or exempt. | OPINION |
| RP-05 | 407 | PROC | Builders implement current eligibility checks plus a permitted alternative or a restriction. The agent must not infer jurisdiction or age from appearance or language. | OPINION |
| RP-06 | 409 | PROC | The link rule is not a reason to move feedback off-platform. Give an in-game route to the audience that cannot reach community links. | OPINION |
| RP-07 | 409 | PROC | Keep experience/community guidance apart from profile-link guidance and from the external service's own eligibility rules. | OPINION |
| RP-08 | 411 | LIMIT | Do not carry either age threshold (13+, 16+) over to every Roblox feature. | OPINION |
| RP-09 | 411 | PROC | Put channel-specific eligibility in the communication brief and check it again when implementation starts. | OPINION |
| RP-10 | 411 | PROC | The agent must not design ways around age, privacy or regional controls. | OPINION |
| RP-11 | 413 | PROC | Reassess maturity when a seasonal update adds materially different horror, violence, gambling-like presentation or other relevant content. A holiday theme is no exemption. | OPINION |
| RP-12 | 413 | PROC | Validate reach and publishing eligibility in the real account before announcing that all players can join. | OPINION |
| RP-13 | 413 | LIMIT | Do not promise age-audience access only because the previous version had it. | OPINION |
| RP-14 | 415 | LIMIT | A brand collaboration may need work beyond ordinary event publication. | OPINION |
| RP-15 | 415 | PROC | Get rights to characters, music and other assets before committing to a licensed theme. Trend popularity and the existence of user-uploaded assets do not give permission. If rights or review time are uncertain, use an original theme. | OPINION |
| RP-16 | 417 | PROC | Screen holiday and trend ideas for sensitive real-world events before creative production. A real-world tragedy must not become a monetized urgency mechanic or a quick engagement chance. | OPINION |
| RP-17 | 419 | PROC | For limited-time offers record six items: real availability window; price; contents; eligibility; repeatability; handling after expiry. | OPINION |
| RP-18 | 419 | LIMIT | Do not present the notification ban on false time pressure as a quote of a universal offer policy. | OPINION |
| RP-19 | 419 | PROC | The studio's own standard rejects fake scarcity, hidden costs and manipulative pressure, especially for younger audiences. This is the studio's standard, not a platform rule. | OPINION |
| RP-20 | 421 | PROC | Event launch checklist, eleven items: approved content and audience; truthful dates and prices; correct reward and odds display; current policy eligibility; allowed communications; required ad disclosures; asset rights; safe data collection; accurate expiry and conversion behavior; tested entitlement handling; a named incident responder. | OPINION |
| RP-21 | 421 | PROC | Failure of a mandatory requirement blocks release. | OPINION |
| RP-22 | 421 | LIMIT | An owner preference does not override platform rules (see X-37 for the clash with the kit's "the owner always wins"). | OPINION |

The five summary rows at LP:425-429 are in the number register (N-17 to N-21).

### 5.3 Roblox rules and capabilities stated outside section 10 (cross-list for the fact-check)

| ID | Surface or feature | What the paper states | Age | Row | FC | Src |
| --- | --- | --- | --- | --- | --- | --- |
| RC-01 | Events | Opt-in reminders and event-linked entry attribution. | n/a | CM-04 | FC-04 | R07 [L] |
| RC-02 | Events | At most 10 ongoing or upcoming events. | n/a | CM-05 | FC-05 | R07 [L] |
| RC-03 | Events (update announcements) | 60 characters; once every 3 days. | n/a | CM-06, CM-07 | FC-06, FC-07 | R07 [L] |
| RC-04 | Event analytics | Compare up to 3 past events; 7 days before; 7 or 14 days after. | n/a | ME-12 | FC-14 | R10 ix |
| RC-05 | Experiments | 14-60 days; up to 2 variants plus control; 24 h and 5 min update cycles. | n/a | ME-17, ME-18 | FC-16 to FC-18 | R09 [L] |
| RC-06 | Experience configs | Change configured values without publishing a new version. | n/a | PR-05 | FC-41 | R21 [L] |
| RC-07 | Refunds | Creators cannot give Robux or monetary refunds through the platform. | n/a | ME-38 | FC-19 | R22 [L] |
| RC-08 | Economy guidance | Sources, sinks, reward value; generous event earnings can change later spending. | n/a | LH-01 | FC-24 | R06 [L] |
| RC-09 | Discovery | Behavior-based signals; algorithm, seasonality, competition, game updates as drivers; no documented "[UPDATE]" lift. | n/a | CM-19, CM-20 | FC-12, FC-13 | R12 [L] |
| RC-10 | Update cadence guidance | Weekly cadence ideal (R04); every two weeks to one month (R02); content cadence builds on existing systems (R01); events influence several KPIs (R03). The paper states no numbers for these in LP:248-536 apart from "fewer than three weeks" (OQ-02). | n/a | OQ-02, OQ-04, DN-02 | FC-43, FC-48, FC-49 | R01-R04 [L] |
| RC-11 | Feedback and testing | Community feedback may be biased; in-experience surveys broaden participation. | n/a | FB-01 | FC-01 | R13 [L] |
| RC-12 | Roadmap announcement | RDC26 lists an "Observability Platform" for "Late 2026"; a roadmap statement, not confirmed delivery. | n/a | N-25, DN-16 | FC-42 | R20 [PC] ix |

## 6. Operating process for the AI live-ops designer (LP:431-518)

### 6.1 Rhythm

| ID | LP | Kind | Content | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| PR-01 | 433 | FRAME | The weekly cycle is an internal decision rhythm, not a duty to publish weekly. | OPINION | - |
| PR-02 | 433 | PROC | Urgent incidents interrupt the cycle through pre-agreed authority. Long-running experiments and seasonal work keep their own timelines. | OPINION | - |
| PR-03 | 433 | PROC | The agent gives the owner concise decision artifacts backed by a detailed evidence ledger, not every raw comment and chart. | OPINION | - |

### 6.2 Step-by-step method and gates (LP:435-450, OPINION). Twelve steps, each with an action, a required output and a gate.

| ID | LP | Step | Action | Required output | Gate before proceeding |
| --- | --- | --- | --- | --- | --- |
| ST-01 | 439 | Intake | Read analyst results, feedback themes, the trend report, release state and builder capacity. | A versioned evidence packet with a cutoff date. | Missing inputs are stated; no invented studio data. |
| ST-02 | 440 | Validate | Check metric definitions, cohort maturity, instrumentation, dates, sampling and source authority. | Data-quality and uncertainty notes. | The apparent change is not a logging or population artifact. |
| ST-03 | 441 | Protect | Find ongoing instability, exploits, failed entitlements or serious player harm. | An incident or mitigation request to the authorized owner. | Urgent harm is not buried under feature ranking. |
| ST-04 | 442 | Diagnose | Find the constraint; separate symptoms from causes. | A problem statement and alternative explanations. | Evidence supports the problem; causal uncertainty stays visible. |
| ST-05 | 443 | Generate alternatives | Consider five kinds: improve, add, simplify or remove, communicate, investigate. | Bounded options tied to the same player objective. | Every option fits the core game and has a mechanism. |
| ST-06 | 444 | Estimate | Ask builders, progression design and marketing for costs and dependencies. | Impact and effort ranges, economy effects, delivery risks. | No unverified build date, assumed license or invented lift. |
| ST-07 | 445 | Rank | Compare evidence, reach, reversibility, cost and strategic fit. | A ranked plan, a cheaper alternative and the deferred ideas. | Counter-evidence and opportunity cost are visible. |
| ST-08 | 446 | Decide | Present the trade-off and ask the owner to choose. | A recorded decision, scope and authority. | Approval is concrete; no silent commitment. |
| ST-09 | 447 | Handoff | Write the chosen update brief and role-specific acceptance criteria. | Contracts for design, progression, build, marketing and analysis. | The owners accept scope, estimates and dependencies. |
| ST-10 | 448 | Verify | Review implementation, economy scenarios, usability, policy and measurement readiness. | A release-readiness record and a rollback or disable plan. | Required checks pass; promised behavior matches shipped behavior. |
| ST-11 | 449 | Release and monitor | Roll out under the approved plan; watch technical and behavioral health. | An incident log and an initial operational assessment. | Stop conditions are enforced; early activity is not called mature retention. |
| ST-12 | 450 | Evaluate and learn | The analyst reports outcomes and uncertainty; the designer recommends the next action. | A repeat, revise, retire or investigate decision, and updated knowledge. | No causal overclaim; actual cost and counter-evidence are kept. |

### 6.3 Chosen update brief and hand-off contract (LP:452-472, OPINION)

Brief fields (seven):

| ID | LP | Field | Contents named by the paper |
| --- | --- | --- | --- |
| UB-01 | 454 | Identity | Decision ID; title; version; owner approval; responsible lead. |
| UB-02 | 455 | Player problem | Cohort; evidence; baseline; source dates; uncertainty. |
| UB-03 | 456 | Objective | Primary behavior or outcome; why it matters now. |
| UB-04 | 457 | Hypothesis | Change, then mechanism, then outcome; plausible alternatives. |
| UB-05 | 458 | Scope | Must deliver; optional only if capacity remains; explicitly excluded. |
| UB-06 | 459 | Player journey | Entry; first meaningful action; repeat activity; completion; next core-game action. |
| UB-07 | 460 | New / returning / veteran paths | Access; comprehension; progression; preserved identity. |

What each receiver gets (six):

| ID | LP | Receiver | Receives | Paper's constraint |
| --- | --- | --- | --- | --- |
| HO-01 | 462 | Game designer | Player promise; core-loop fit; activity constraints; interaction acceptance criteria; edge cases; the question the update must answer. | The live-ops agent must not hand over an unvalidated feature list as finished game design. |
| HO-02 | 464 | Progression designer | Target effort distribution; reward purpose; currency and item flows; existing ownership; catch-up needs; expiry and migration rules; monetization constraints. | That designer validates amounts and incentives. The live-ops agent must not invent a currency multiplier to make the event look exciting. |
| HO-03 | 466 | Builders | Approved scope; dependencies; required interfaces; device and performance limits; persistence and entitlement behavior; exposure identification; safe-disable requirements; acceptance criteria. | Builders return feasibility, effort range, lead time and implementation risks before a date is committed. |
| HO-04 | 468 | Marketing | Approved player benefit; audience; exact dates; eligibility; truthful reward terms; available assets; channel restrictions; claim substantiation; fallback wording. | No teaser may promise unfinished optional scope as guaranteed content. |
| HO-05 | 470 | Analyst | Hypothesis; cohort and assignment or exposure definitions; primary outcome; guardrails; comparison design; observation windows; decision criteria. | An analytical contract, not an invented logging implementation. The analyst confirms the question can really be answered. |
| HO-06 | 472 | Release owner | Launch checklist; sign-offs; incident contacts; stop conditions; safe rollback or disable behavior; communication plan; post-release review dates. | Separate reversible configuration from irreversible player-state changes. |

### 6.4 Live configuration

| ID | LP | Kind | Content | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| PR-05 | 474 | MECH | Roblox configs support changing configured values without publishing a new game version. | VERIFIED | R21 [L] |
| PR-06 | 474 | LIMIT | A configuration switch helps only if builders implement and test the wanted behavior. | OPINION | R21 [L] |
| PR-07 | 474 | LIMIT | It does not automatically undo persistent rewards, repair migrations or act as a general rollback. | OPINION | R21 [L] |
| PR-08 | 474 | PROC | Keep the config version and exposure evidence, so the analyst knows which rules players actually experienced. | OPINION | R21 [L] |

### 6.5 Post-update review template (LP:476-490, OPINION). Thirteen fields.

| ID | LP | Field | Contents named by the paper |
| --- | --- | --- | --- |
| PV-01 | 478 | Decision ID / actual release version and timestamps | - |
| PV-02 | 479 | Original hypothesis and approved success criteria | - |
| PV-03 | 480 | What actually shipped / deviations / incidents | - |
| PV-04 | 481 | Assigned and exposed populations / exclusions / data quality | - |
| PV-05 | 482 | Primary result and uncertainty / guardrail results | - |
| PV-06 | 483 | New, continuing and reactivated cohort results | - |
| PV-07 | 484 | Revenue composition and post-event displacement | - |
| PV-08 | 485 | Feedback changes and unresolved themes | - |
| PV-09 | 486 | Actual active effort, elapsed time, support cost and estimate error | - |
| PV-10 | 487 | Best explanation / credible alternatives / limits to causal attribution | - |
| PV-11 | 488 | Decision | One of: repeat, revise, retire, investigate. |
| PV-12 | 489 | What becomes a reusable rule, and with what evidence mark | - |
| PV-13 | 490 | Owner decision and next review trigger | - |

### 6.6 Do-not-do table (LP:492-511). Sixteen rows.

The "Evidence" column is the paper's, with combined tags kept as written. Dates are as printed in the paper.

| ID | LP | Shortcut to avoid | Detection or replacement | Evidence (as written) | Src |
| --- | --- | --- | --- | --- | --- |
| DN-01 | 496 | Chase every request | Require a player problem, distinct-author counts, cohort context and a behavioral check. | OPINION; feedback bias documented in R13, checked 2026-10-21 | R13 [L] |
| DN-02 | 497 | Add a new system to every update | Ask whether existing mechanics can meet the need; count future maintenance. | OPINION; cadence/expansion distinction in R01-R02, checked 2026-10-21 | R01, R02 [L] |
| DN-03 | 498 | Copy an unrelated viral event | Require core-game fit, audience overlap, trend lifetime and asset rights. | OPINION; Brawl production/attention caution in G10, 2026-03-07 | G10 |
| DN-04 | 499 | Ignore an existing drop-off while adding distant endgame content | Compare affected cohorts, reachability and the binding constraint. | OPINION; this paper, 2026-10-21 | - |
| DN-05 | 500 | Promise a date before builders estimate | Require accepted scope, dependencies, testing and support coverage. | OPINION; Adopt Me wellbeing experience G01, 2020-04-30 | G01 |
| DN-06 | 501 | Claim a retention lift from peak concurrency or views | Check metric, denominator, cohort maturity and counterfactual. | OPINION; measurement distinctions illustrated by G05 and G10 | G05, G10 |
| DN-07 | 502 | Declare success from the launch spike | Check later cohorts and post-event behavior. | OPINION; Brawl's normalized result G10, 2026-03-07 | G10 |
| DN-08 | 503 | Nerf every newly popular strategy | Verify power, counterplay and discovery time. | EXPERIENCE / OPINION; G07, 2026-08-25 | G07 [PC] |
| DN-09 | 504 | Reward social actions without testing actual behavior | Inspect spam, avoidance, abuse and harm to recipients. | EXPERIENCE / OPINION; R11, 2026-08-24 | R11 [PC] |
| DN-10 | 505 | Inflate event rewards without economy review | Simulate aggregate issuance and later demand. | VERIFIED / OPINION; R06, checked 2026-10-21 | R06 [L] |
| DN-11 | 506 | Use false scarcity or compulsory notifications | Validate real deadlines, choice and truthful messages. | VERIFIED / OPINION; R08, checked 2026-10-21 | R08 [L] |
| DN-12 | 507 | Hide random outcomes behind currency or boosts | Audit the complete paid transaction and the current odds. | VERIFIED; R14-R15, checked 2026-10-21 / 2026-05-26 | R14 [L], R15 ix |
| DN-13 | 508 | Send younger players to Discord by default | Use current link eligibility and in-game feedback alternatives. | VERIFIED / OPINION; R16, checked 2026-10-21 | R16 [L] |
| DN-14 | 509 | Roll back persistent state blindly | Keep valid entitlements; test migration and compensation separately. | OPINION; refund limits R22, checked 2026-10-21 | R22 [L] |
| DN-15 | 510 | Replace unknown effort or effects with AI confidence | Keep explicit unknowns; ask for estimates or run a bounded test. | OPINION; this paper, 2026-10-21 | - |
| DN-16 | 511 | Treat an announced platform feature as already available | Confirm current docs and account availability; separate roadmap dates from delivery. | VERIFIED / OPINION; RDC26 announcement R20, 2026-09-11 | R20 [PC] ix |

The four summary rows at LP:515-518 are in the number register (N-22 to N-25).

## 7. Open questions, disagreements and research limits (LP:520-535)

These must survive into the skills. The paper says they are not gaps to fill with a plausible-sounding number (OQ-00). All bullets are tagged OPINION by the heading line.

| ID | LP | Kind | Content (paraphrase, full) | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| OQ-00 | 522 | FRAME | The uncertainties below must remain in the trained agent's knowledge and must not be filled with a plausible-sounding number. | OPINION | - |
| OQ-01 | 524 | LIMIT | Exact causal retention, revenue and returning-player lifts for most studied updates are not publicly established by the sources reviewed. Public release notes show design intent and schedules more often than counterfactual results. Ask for studio-owned measurements; do not borrow another game's success claim. | OPINION | - |
| OQ-02 | 525 | LIMIT | Development time per update is largely undisclosed. Roblox's "fewer than three weeks" guidance is a recommendation. Brawl's "equivalent to 3 Brawlers" statement is relative effort. Neither is a transferable person-day estimate for a small AI studio. (No source id is given at this line for either figure: X-35.) | OPINION | none cited here |
| OQ-03 | 526 | LIMIT | This evidence set shows no universal Roblox retention target, update cadence, optimal event length, acceptable currency multiplier or guaranteed revenue improvement. Genre, maturity, cohort, acquisition mix and team capacity matter. | OPINION | - |
| OQ-04 | 527 | LIMIT | Weekly-cadence advice, more flexible content guidance, Adopt Me's wellbeing-driven change and Minecraft's smaller drops point in different directions. The operational answer is capacity and player fit, not an average of the schedules treated as a best practice. | OPINION | R01-R04 [L], G01, G21 |
| OQ-05 | 528 | LIMIT | Scarcity can support a seasonal identity, while pressure can harm trust. Roblox's season-pass guidance and its notification prohibitions address different contexts. The paper's wider ethical standard is explicitly OPINION and not a platform-wide prohibition. | OPINION | R05 [L], R08 [L] |
| OQ-06 | 529 | LIMIT | The Adopt Me year-end post dated 2023-12-28 reports 56 weekly updates but carries a conflicting "In 2024" heading. It was not used as a precise 2023 update-count benchmark. | OPINION | G03 |
| OQ-07 | 530 | LIMIT | Read social-link guidance by surface: experience/community links and personalized notifications do not share one eligibility threshold. A future policy change means re-checking the primary pages, not repeating this paper. | OPINION | R08 [L], R16 [L] |
| OQ-08 | 531 | LIMIT | The RDC26 official announcement was used for a narrow, dated roadmap claim. The 2026 session talks could not be reviewed from reliable accessible transcripts or video; no numerical lesson is attributed to an unreviewed talk. The August 2026 Roblox/Uplift case study and current docs give accessible contemporary evidence but do not replace the missing talk review. | OPINION | R11 [PC], R20 [PC] |
| OQ-09 | 532 | LIMIT | GDC evidence is limited to official session abstracts (Destiny and feedback practice). Full recordings and slides were not reviewed. No unsupported slide statistic or speaker quote is presented. | OPINION | G25 abs, G27 abs |
| OQ-10 | 533 | LIMIT | Deadlock was searched, but no accessible, dated primary account of its schedule change was found, so it is left out of the ten longitudinal cases. Secondary reports of its cadence are not promoted to verified Valve evidence. A future revision should add verified Valve posts and separate early-development iteration from mature live operation. | OPINION | - |
| OQ-11 | 534 | LIMIT | Hearthstone, Clash Royale and Destiny add to the ten-case comparison. Their dated announcements show operating choices; they do not show that each announced change shipped unchanged or produced a measured improvement. | OPINION | G22-G26 |
| OQ-12 | 535 | LIMIT | No private Creator Hub data, real studio budget, current game funnel, player-feedback corpus or builder-capacity estimate was supplied. The templates are ready to fill; a real ranked production plan would be speculation without those inputs. | OPINION | - |

## 8. Number register

### 8.1 The paper's own summary rows ("Rule | Number | Evidence mark | Source and date")

| ID | LP | Rule | Number or content | Mark (paper) | Source and date (paper) | Scope and limit (from nearby text) |
| --- | --- | --- | --- | --- | --- | --- |
| N-01 | 282 | Community feedback is a selected sample | Representativeness unknown without sampling evidence | VERIFIED | R13, undated; checked 2026-10-21 | FB-01 |
| N-02 | 283 | Triangulate methods | Focus groups, surveys and community conversation; no universal weights | EXPERIENCE | G28, 2024-08-22 | "No universal weights" is the paper's inference (X-42) |
| N-03 | 284 | Count people separately from messages | Exact observed counts; no estimated AI counts | OPINION | This paper, 2026-10-21 | FB-22 to FB-25 |
| N-04 | 285 | Preserve severe low-frequency signals | Frequency is not the only prioritization criterion | OPINION | This paper, 2026-10-21 | FB-28, FB-29 |
| N-05 | 333 | Respect event-listing capacity | At most 10 ongoing or upcoming events | VERIFIED | R07, undated; checked 2026-10-21 | CM-05 |
| N-06 | 334 | Respect update-announcement limits | 60 characters; once every 3 days | VERIFIED | R07, undated; checked 2026-10-21 | CM-06, CM-07 |
| N-07 | 335 | Separate personalized notifications from broadcast updates | Eligible 13+; opt-in | VERIFIED | R08, undated; checked 2026-10-21 | CM-09 |
| N-08 | 336 | Treat an update title tag as communication, not a ranking guarantee | No guaranteed lift documented | OPINION | R12 plus synthesis; checked 2026-10-21 | CM-20 |
| N-09 | 371 | Use event comparisons for diagnosis | Up to 3 events; 7 days before; 7 or 14 days after | VERIFIED | R10, 2025-10-21 | ME-12; chart only, no control (ME-13) |
| N-10 | 372 | Respect native experiment duration and structure | 14-60 days; up to 2 variants plus control | VERIFIED | R09, undated; checked 2026-10-21 | ME-17 |
| N-11 | 373 | Do not confuse cohort labels with targets | D1/D7/D30 are windows; target rates are game-specific | OPINION | This paper, 2026-10-21 | ME-09 |
| N-12 | 374 | Do not promise unsupported refunds | Creator-issued Robux or monetary refunds unavailable through the platform | VERIFIED | R22, undated; checked 2026-10-21 | ME-38 |
| N-13 | 396 | Model reward flows and later demand | No universal safe currency multiplier | VERIFIED / OPINION | R06, undated; checked 2026-10-21 | A statement of absence, tagged with both marks (X-42) |
| N-14 | 397 | Preserve progress and explain migration | King Tower level preserved or increased in the described change | EXPERIENCE | G24, 2026-05-13 | LP:388 says "preservation" only (X-34) |
| N-15 | 398 | Give returners orientation | Quantified retention effect not disclosed | VERIFIED | G17, 2026-02-04 | LH-20, LH-22 |
| N-16 | 399 | Track total operating cost, not content count | Studio-specific effort and support measurements required | OPINION | This paper, 2026-10-21 | LH-29 |
| N-17 | 425 | Disclose final paid-random outcomes accurately | Probabilities total exactly 100% | VERIFIED | R14, undated, checked 2026-10-21; R15, 2026-05-26 | RR-02, RR-05 |
| N-18 | 426 | Use current experience/community link rules | Age-checked 16+; up to 3 links | VERIFIED | R16, undated; checked 2026-10-21 | RR-06, RR-07 |
| N-19 | 427 | Keep notification eligibility separate | Eligible 13+ and opt-in | VERIFIED | R08, undated; checked 2026-10-21 | RR-09, RR-10 |
| N-20 | 428 | Recheck content maturity and advertising constraints | No universal exemption for events | VERIFIED / OPINION | R17-R18, undated; checked 2026-10-21 | RR-13, RR-14; the "no exemption" part is OPINION (RP-11) |
| N-21 | 429 | Distinguish platform prohibition from studio ethical standard | No universal limited-time-offer ban established here | OPINION | Review synthesis, 2026-10-21 | RR-16 |
| N-22 | 515 | Review evidence weekly without requiring a weekly release | Weekly is the proposed internal decision rhythm | OPINION | This paper, 2026-10-21 | PR-01 |
| N-23 | 516 | Preserve decision authority and handoff acceptance | A named owner per deliverable; no universal staffing count | OPINION | "User mandate; operationalized 2026-10-21" (paper's wording) | HO-01 to HO-06 |
| N-24 | 517 | Use live configuration only for tested behavior | No-publish config changes supported; state reversal not implied | VERIFIED / OPINION | R21, undated; checked 2026-10-21 | PR-05 to PR-07 |
| N-25 | 518 | Keep announcements separate from availability | RDC26 described Observability Platform for "Late 2026" | VERIFIED | R20, 2026-09-11 | DN-16; roadmap only (X-41) |

### 8.2 Numbers that appear only in prose (or add detail to a summary row)

| ID | LP | Number | Scope | Paper's limit | Tag | Src, date |
| --- | --- | --- | --- | --- | --- | --- |
| N-26 | 250 | GDC 2022 (day not established) | Feedback Fundamentals abstract | Abstract only | EXPERIENCE | G27 |
| N-27 | 348 | Metrics update every 24 hours; playtime, payer conversion and ARPU also every 5 minutes in the first 24 hours | Roblox native experiments | - | VERIFIED | R09 [L] |
| N-28 | 346 | "7 or 14 days after": the paper does not say when 7 and when 14 applies | Event analytics windows | Chart windows give no control group | VERIFIED | R10 |
| N-29 | 342, 344 | No number supplied for L, for D1/D7/D30 target rates, or for a confidence threshold (LP:350) | Reactivation and retention | Game-specific; no threshold invented | OPINION | - |
| N-30 | 405 | 2026-05-26 | Official clarification on paid random items | Indexed excerpt | VERIFIED | R15 |
| N-31 | 388 | 2026 (Overwatch announcement 2026-02-04; Clash Royale change 2026-05-13) | Returner orientation; progression migration | No portable lift | VERIFIED / EXPERIENCE | G17; G24 |
| N-32 | 392, 500 | 2020-04-30 | Adopt Me flexible schedule | Historical; wellbeing reading | EXPERIENCE | G01 |
| N-33 | 525 | "Fewer than three weeks"; "equivalent to 3 Brawlers" | Roblox guidance; Brawl effort | Not person-day estimates; no source id at this line | OPINION | none cited here |
| N-34 | 529 | 56 weekly updates; post dated 2023-12-28; conflicting "In 2024" heading | Adopt Me year-end post | Not used as a benchmark | OPINION | G03 |
| N-35 | 533 | "Ten longitudinal cases" | The paper's case set (defined before LP:248) | Deadlock excluded | OPINION | - |
| N-36 | 498, 502 | 2026-03-07 | Brawl Stars 2025 review | No controlled attribution (register LP:669) | OPINION / EXPERIENCE | G10 |
| N-37 | 503, 504 | 2026-08-25 (G07); 2026-08-24 (R11) | League patch 26.17; Roblox/Uplift case study | R11: no controlled lift disclosed (register LP:583) | EXPERIENCE / OPINION | G07 [PC]; R11 [PC] |
| N-38 | 518 | "Late 2026"; 2026-09-11 | RDC26 Observability Platform | Roadmap, not delivery | VERIFIED | R20 [PC] |
| N-39 | none stated | No universal safe currency multiplier; no universal retention target; no optimal event length; no cadence benchmark; no guaranteed revenue gain | The paper's evidence set | Mark unknown | OPINION | LP:396, 526 |

### 8.3 Structure counts (so a skill writer can check it kept every part)

| Item | Count | LP |
| --- | --- | --- |
| Feedback taxonomy fields | 11 | 258 |
| Feedback template: header fields / theme columns / quality checks | 5 / 8 / 7 | 266-276 |
| Closing-the-loop parts | 5 | 278 |
| Promise-ledger fields | 7 | 289 |
| Patch-notes template: title and header lines / sections | 4 / 7 | 303-329 |
| Pre-release agreements (measurement) | 8 | 340 |
| Retention-definition choices | 6 | 344 |
| Confounds listed for before/after charts | 8 | 346 |
| Failure-response rows | 6 | 358-363 |
| Economy-ledger items | 8 | 380 |
| Event launch checklist items | 11 | 421 |
| Process steps | 12 | 439-450 |
| Update-brief fields / receivers | 7 / 6 | 454-472 |
| Post-update review fields | 13 | 478-490 |
| Do-not-do rows | 16 | 496-511 |
| Open-question bullets | 12 | 524-535 |

## 9. Source ids used in lines 248-536 (resolved from LP:537-749)

Quotes are the register's own key lines (15 words or fewer), attributed to the register. "[L]" = undated live page: live check. "[PC]" = dated after 2026-06-01: live check. The register preface (LP:539) says all sources were checked on 2026-10-21, are primary or official, and that a quotation is a locating excerpt only.

| ID | Source | Date and limits (register) | Flag | URL | Cited at LP | Reg. LP | Key line (register) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R01 | Roblox, LiveOps essentials | undated live document; checked 2026-10-21. VERIFIED guidance, not measured effect. | [L] | https://create.roblox.com/docs/production/game-design/liveops-essentials | 497, 527 | 543 | "Content Cadence releases exclusively build on existing systems" |
| R02 | Roblox, Content updates | undated live document; checked 2026-10-21. VERIFIED guidance. | [L] | https://create.roblox.com/docs/production/game-design/content-updates | 497, 527 | 547 | "many games release content cadence updates every two weeks to one month." |
| R03 | Roblox, LiveOps planning | undated live document; checked 2026-10-21. VERIFIED guidance. | [L] | https://create.roblox.com/docs/production/game-design/liveops-planning | 527 | 551 | "events typically influence several KPIs simultaneously." |
| R04 | Roblox, Monetization | undated live document; checked 2026-10-21. VERIFIED recommendation, not a platform mandate. | [L] | https://create.roblox.com/docs/production/monetization | 527 | 555 | "A weekly cadence for updates is ideal" |
| R05 | Roblox, Season pass design | undated live document; checked 2026-10-21. VERIFIED design recommendations. | [L] | https://create.roblox.com/docs/production/game-design/season-pass-design | 528 | 559 | "one month is considered a good starting point" |
| R06 | Roblox, Balance virtual economies | undated live document; checked 2026-10-21. VERIFIED guidance; its Feline Fishing Fun example is explicitly fictitious. | [L] | https://create.roblox.com/docs/production/game-design/balance-virtual-economies | 378, 396, 505 | 563 | "Resource planning involves balancing how virtual resources are created and how they're spent." |
| R07 | Roblox, Experience events | undated live document; checked 2026-10-21. VERIFIED current feature constraints. | [L] | https://create.roblox.com/docs/production/promotion/experience-events | 291, 333, 334 | 567 | "you can only announce an update once every three days." |
| R08 | Roblox, Experience notifications | undated live document; checked 2026-10-21. VERIFIED current eligibility and use restrictions. | [L] | https://create.roblox.com/docs/production/promotion/experience-notifications | 293, 335, 411, 427, 506, 528, 530 | 571 | "Games should not require users to turn on notifications" |
| R09 | Roblox, Experiments | undated live document; checked 2026-10-21. VERIFIED platform capability and limits. | [L] | https://create.roblox.com/docs/production/experiments | 348, 372 | 575 | "Experiments run for between 14-60 days." |
| R10 | Roblox DevForum, "Analytics: Understand the success of your Experience Events" | 2025-10-21. VERIFIED announcement, reviewed through indexed official excerpts; full thread access was limited. | ix | https://devforum.roblox.com/t/analytics-understand-the-success-of-your-experience-events/4019126 | 346, 371 | 579 | "compare up to three of your past events on the same chart" |
| R11 | Roblox / Jim Meenan, "Optimize Testing and Live Updates with Roblox's Analytics and Experimentation Platform" | 2026-08-24. VERIFIED platform account; EXPERIENCE for Uplift's production lessons. No controlled lift disclosed for the cited cases. | [PC] | https://about.roblox.com/newsroom/2026/08/optimize-testing-live-updates-roblox-analytics-experimentation-platform | 504, 531 | 583 | "We used analytics and experiments to test our trading hub" |
| R12 | Roblox, Discovery | undated live document; checked 2026-10-21. VERIFIED description of discovery signals and diagnostic factors. | [L] | https://create.roblox.com/docs/discovery | 299, 336 | 587 | "Every signal reflects user behavior after they discover your game." |
| R13 | Roblox, Beta testing experiences | undated live document; checked 2026-10-21. VERIFIED guidance on feedback collection and bias. | [L] | https://create.roblox.com/docs/education/developer/beta-testing-experiences | 250, 282, 496 | 591 | "Feedback may be biased." |
| R14 | Roblox, Paid random items | undated live document; checked 2026-10-21. VERIFIED policy requirements. | [L] | https://create.roblox.com/docs/production/monetization/paid-random-items | 405, 425, 507 | 595 | "the probability percentages of all final outcomes must sum to exactly 100%." |
| R15 | Roblox DevForum, "Clarifying requirements for paid random items" | 2026-05-26. VERIFIED official clarification; indexed official excerpt. | ix | https://devforum.roblox.com/t/clarifying-requirements-for-paid-random-items/4654622 | 405, 425, 507 | 599 | "making compliance expectations more explicit for creators" |
| R16 | Roblox Support, "Social Media Links for Experiences & Communities" | undated current support page; checked 2026-10-21. VERIFIED surface-specific eligibility; the register says not to substitute older group/profile guidance. | [L] | https://en.help.roblox.com/hc/en-us/articles/360000910966-Social-Media-Links-for-Experiences-Communities | 295, 409, 426, 508, 530 | 603 | "Links are not permitted to be shared directly within Experiences." |
| R17 | Roblox, Content maturity | undated live document; checked 2026-10-21. VERIFIED maturity questionnaire guidance. | [L] | https://create.roblox.com/docs/production/promotion/content-maturity | 413, 428 | 607 | "Maturity & Compliance questionnaire" |
| R18 | Roblox, Ad integrations | undated live document; checked 2026-10-21. VERIFIED sponsorship/advertising eligibility and disclosure guidance. | [L] | https://create.roblox.com/docs/production/promotion/ad-integrations | 415, 428 | 611 | "You must check user eligibility and add the required ad labeling and disclosure." |
| R19 | Roblox Community Standards | live policy; publication or revision date not established in the reviewed text; checked 2026-10-21. VERIFIED policy, used narrowly for sensitive real-world events. | [L] | https://about.roblox.com/community-standards | 417 | 615 | "Sensitive Real-World Events" |
| R20 | Roblox DevForum, "RDC26: What We Announced" | 2026-09-11. VERIFIED official announcement; indexed excerpt only. A roadmap statement, not a reviewed talk and not confirmed delivery. | [PC], ix | https://devforum.roblox.com/t/rdc26-what-we-announced/4865880/1 | 511, 518, 531 | 619 | "Observability Platform (Late 2026)" |
| R21 | Roblox, Experience configs | undated live document; checked 2026-10-21. VERIFIED platform capability. | [L] | https://create.roblox.com/docs/production/configs | 474, 517 | 623 | "Configs do nothing unless you use them within your code." |
| R22 | Roblox Support, "Contacting an Experience's Creators for Help" | undated current support page; checked 2026-10-21. VERIFIED creator refund limitation. | [L] | https://en.help.roblox.com/hc/en-us/articles/6566665691924-Contacting-an-Experience-s-Creators-for-Help | 365, 374, 509 | 627 | "Creators cannot provide Robux refunds or monetary refunds from purchases via the Roblox platform." |
| G01 | Adopt Me / Uplift, "Adopt Me moves to a flexible update schedule from weekly Friday update" | 2020-04-30. EXPERIENCE for production/wellbeing interpretation; historical schedule. | - | https://www.playadopt.me/news/adopt-me-moves-to-a-flexible-update-schedule-from-weekly-friday-update-adopt-me-on-roblox | 392, 500, 527 | 633 | "the main being the wellbeing of our Team" |
| G03 | Adopt Me / Uplift, "Happy New Year!" | 2023-12-28. VERIFIED source inconsistency, not a trusted year-specific count benchmark. | - | https://www.playadopt.me/news/happy-new-year | 529 | 641 | "In 2024, we:" |
| G05 | Fortnite official account, record-day announcement | 2023-11-05; the measurement refers to the preceding day. VERIFIED first-party aggregate measurement, not independently audited causal evidence. Official indexed post. | - | https://x.com/Fortnite/status/1721210643888660633 | 501 | 649 | "over 44.7 MILLION players jumping in" |
| G07 | Riot Games, League of Legends Patch 26.17 Notes | 2026-08-25. VERIFIED patch statement; EXPERIENCE for the design rationale. | [PC] | https://www.leagueoflegends.com/en-gb/news/game-updates/league-of-legends-patch-26-17-notes/ | 503 | 657 | "we don't want to be making adjustments so frequently" |
| G10 | Supercell / Frank Keienburg, "2025 in Review: Frank's Blog Post" (Brawl Stars) | 2026-03-07. EXPERIENCE with first-party measured observations; no controlled attribution supplied for the cited changes. | - | https://supercell.com/en/games/brawlstars/blog/community/2025-in-review-franks-blog-post/ | 498, 501, 502 | 669 | "revenue and monthly active players dropping by around 20%" |
| G17 | Blizzard, Overwatch Spotlight / Reign of Talon announcement | 2026-02-04. VERIFIED announced annual narrative and returner support; no retention lift supplied. | - | https://overwatch.blizzard.com/en-us/news/24246206/ | 388, 398 | 697 | "a narrative arc with a set beginning, middle, and end" |
| G21 | Mojang, "The future of Minecraft's development" | 2024-09-08. EXPERIENCE on operating model and feedback; VERIFIED announced change. | - | https://www.minecraft.net/en-us/article/the-future-of-minecrafts-development | 527 | 709 | "These game drops will vary in size" |
| G22 | Blizzard, Hearthstone expansions and adventures | undated live catalog; 2026 entries checked 2026-10-21. VERIFIED catalog dates, not development-time data. | [L] | https://playhearthstone.com/en-us/expansions-adventures/ | 534 (range) | 713 | "March 2026" |
| G23 | Blizzard, "Take a First Look at Hearthstone's New Class Sets" | 2026-04-27. VERIFIED planned structure; no outcome inferred. | - | https://hearthstone.blizzard.com/en-gb/news/24267730 | 534 (range) | 717 | "Four Class Sets are released at a time, with three waves planned throughout the year." |
| G24 | Supercell, "New Collection Levels and Mastery Changes" (Clash Royale) | 2026-05-13. EXPERIENCE for simplification rationale; VERIFIED migration announcement. | - | https://supercell.com/en/games/clashroyale/blog/news/new-collection-levels-and-mastery-changes/ | 388, 397, 534 | 721 | "We want progression to be simple, clear, and rewarding." |
| G25 | GDC / Justin Truman, "From Box Products to Live Service: How Destiny 2 Transformed Bungie" | GDC 2022; exact session day not established. EXPERIENCE; official abstract only. | abs | https://gdcvault.com/play/1027599/From-Box-Products-to-Live | 532, 534 (range) | 725 | "prioritization, organization, and decision-making" |
| G26 | Bungie, "The Edge of Fate and Year of Prophecy Reveal Recap" | 2025-05-06. VERIFIED dated roadmap; execution and results not inferred. | - | https://www.bungie.net/7/en/News/Article/year_of_prophecy_reveal_recap | 534 (range) | 729 | "two paid expansions and two major updates available to all" |
| G27 | GDC / Emma Bridle and Savannah Harrison, "Give Your Players a Seat at the Table: Feedback Fundamentals" | GDC 2022; exact session day not established. EXPERIENCE; official abstract only. | abs | https://gdcvault.com/play/1027615/Give-Your-Players-a-Seat | 250, 532 | 733 | "from small community council to a growing GaaS playerbase" |
| G28 | Riot Games, "/dev: Skin Thematics and Champion Fantasies" | 2024-08-22. EXPERIENCE on player research and allocation of design effort. | - | https://www.leagueoflegends.com/en-ph/news/dev/dev-skin-thematics-and-champion-fantasies/ | 250, 283 | 737 | "using focus groups and sending surveys" |

Register ids not cited in lines 248-536 (for example G02, G04, G06, G08, G09, G11-G16, G19, G20, G29, G30) are not resolved here.

## 10. Claims for the fact-check

Priority: P1 = Roblox rule or capability, age threshold, measurement method, any number. P2 = case date or schedule, and official guidance that states no rule, capability or number. P3 = framing. Fact-check against the source at the id, not against the paper. Live column: [L] re-read the undated live page; [PC] source dated after 2026-06-01; ix / abs = the paper saw only an excerpt or abstract. Key line = whether the register's one key line backs the claim (full / part / none): the key lines are short, so most claims need the full source. Rows for OPINION measurement methods (FC-20 to FC-23) are included because the owner asked to check measurement and event effects; they test method soundness, not a Roblox fact. All Roblox rows in section 5.1 map to FC rows (column "FC" there): FC-08 to FC-11 (notifications), FC-28 to FC-40.

| ID | Claim (paraphrase, with scope) | LP | Row | Tag | Src | Pri | Live | Key line | Why it matters |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FC-01 | Roblox testing guidance says community feedback may be biased and presents in-experience surveys as a way to broaden participation. | 250, 282 | FB-01 | VERIFIED | R13 | P2 | [L] | part (bias only) | Basis for the feedback-sample caveat. |
| FC-02 | Riot (dev post, 2024-08-22) describes focus groups, surveys and Discord/forum conversation as ways to learn player preferences. | 250, 283 | FB-02 | EXPERIENCE | G28 | P3 | - | full | Practice, not result; no weights given. |
| FC-03 | GDC 2022 "Feedback Fundamentals" abstract covers community feedback before and after launch. | 250, 532 | FB-03 | EXPERIENCE | G27 | P3 | abs | part | Abstract only. |
| FC-04 | Roblox experience events support opt-in reminders and event-linked entry attribution. | 291 | CM-04 | VERIFIED | R07 | P1 | [L] | none | Capability the event plan can use. |
| FC-05 | An experience can have at most 10 ongoing or upcoming events. | 291, 333 | CM-05 | VERIFIED | R07 | P1 | [L] | none | Count limit. |
| FC-06 | Update announcements allow 60 characters. | 291, 334 | CM-06 | VERIFIED | R07 | P1 | [L] | none | Message-length limit. |
| FC-07 | An update announcement can be sent once every 3 days. | 291, 334 | CM-07 | VERIFIED | R07 | P1 | [L] | full | Sending ceiling (paper: not a cadence, CM-08). |
| FC-08 | Personalized experience notifications are a separate, opted-in feature for eligible users 13 and over (also LP:411, 427). | 293, 411, 427 | RR-09, CM-09 | VERIFIED | R08 | P1 | [L] | none | Age threshold; do not extend to other surfaces. |
| FC-09 | Personalized notifications should relate to the user's activity. | 293 | RR-12 | VERIFIED | R08 | P1 | [L] | none | Guidance wording ("should"); rule strength unknown. |
| FC-10 | Games must not require users to turn notifications on (compulsory opt-in prohibited). | 293, 411 | RR-10 | VERIFIED | R08 | P1 | [L] | full | Hard prohibition. |
| FC-11 | Notifications prohibit deceptive pressure; LP:419 calls this a documented ban on false time pressure. | 411, 419 | RR-11 | VERIFIED | R08 | P1 | [L] | none | Wording differs between LP:411 and LP:419 (X-30); do not stretch to offers. |
| FC-12 | Roblox's discovery doc describes signals as player behavior and lists algorithm, seasonality, competition and game updates as possible drivers of change. | 299 | CM-19 | VERIFIED | R12 | P1 | [L] | part | Basis for "update effect is not isolated". |
| FC-13 | No official source the paper reviewed documents that an "[UPDATE]" title tag guarantees a recommendation boost (a negative claim). | 299, 336 | CM-20 | OPINION | R12 | P1 | [L] | none | Title-tag advice; confirm nothing in Roblox docs says otherwise. |
| FC-14 | Event analytics lets creators compare up to 3 past events, with 7 days before and 7 or 14 days after. | 346, 371 | ME-12 | VERIFIED | R10 | P1 | ix | part (3 events only) | Window numbers; when 7 vs 14 applies is unstated (N-28). |
| FC-15 | The event-chart windows give no control group (the paper's inference inside the VERIFIED group). | 346 | ME-13 | VERIFIED (as written) | R10 | P1 | ix | none | Measurement method; check it is not contradicted by the feature's design. |
| FC-16 | Native experiments run for 14-60 days. | 348, 372 | ME-17 | VERIFIED | R09 | P1 | [L] | full | Duration bounds. |
| FC-17 | Native experiments support up to 2 variants plus a control. | 348, 372 | ME-17 | VERIFIED | R09 | P1 | [L] | none | Structure limit. |
| FC-18 | Experiment metrics update every 24 hours; playtime, payer conversion and ARPU also every 5 minutes in the first 24 hours. | 348 | ME-18 | VERIFIED | R09 | P1 | [L] | none | Timing numbers; metric names must match. |
| FC-19 | Experience creators cannot give Robux or monetary refunds through the platform. | 365, 374 | ME-38 | OPINION (para) / VERIFIED (LP:374) | R22 | P1 | [L] | full | Governs incident wording; tag conflict X-33. |
| FC-20 | Method: reactivation rate = returning eligible lapsed players / all eligible lapsed players in the stated reachable or assigned population; L is game-specific. | 342 | ME-04 to ME-07 | OPINION | - | P1 | - | n/a | Definition to be used by the analyst. |
| FC-21 | Method: D1/D7/D30 name observation intervals, not target rates; do not report mature D7 for immature cohorts. | 344, 373 | ME-08 to ME-10 | OPINION | - | P1 | - | n/a | Check against Roblox's own retention definitions. |
| FC-22 | Method: player-level assignment can be contaminated when the treatment changes a shared economy, server or social group; a global event may lack a simultaneous control. | 348 | ME-20, ME-21 | OPINION | - | P1 | - | n/a | Event-effect design. |
| FC-23 | Method: prefer intention-to-treat for the primary causal claim; no early stopping at a favorable moment; no universal confidence threshold. | 350 | ME-22 to ME-25 | OPINION | - | P1 | - | n/a | Event-effect design. |
| FC-24 | Roblox economy guidance links sources, sinks and reward value, and warns that very generous event earnings can affect later spending; its fishing example is fictitious. | 378, 396 | LH-01, LH-02 | VERIFIED | R06 | P2 | [L] | part (balancing only) | No numeric benchmark may come from it. |
| FC-25 | Overwatch's 2026-02-04 announcement includes returning-player orientation; no retention lift supplied. | 388, 398 | LH-20 | VERIFIED | G17 | P2 | - | part (narrative arc only) | Case date; not a Roblox lift. |
| FC-26 | Clash Royale's 2026-05-13 change preserves King Tower level (LP:397 says "preserved or increased"). | 388, 397 | LH-21 | EXPERIENCE | G24 | P2 | - | none | Wording differs between LP:388 and LP:397 (X-34). |
| FC-27 | Adopt Me's 2020-04-30 move from weekly Friday updates to a flexible schedule was tied to team wellbeing. | 392, 500 | LH-26, DN-05 | EXPERIENCE | G01 | P2 | - | full | Case used against fixed weekly cadence. |
| FC-28 | Paid random items include direct purchases and indirect mechanisms through currency that can be bought with Robux. | 405 | RR-01 | VERIFIED | R14 | P1 | [L] | none | Scope of the rule; headline compliance item. |
| FC-29 | All final outcomes and their numerical probabilities must be disclosed; probabilities total exactly 100%. | 405, 425 | RR-02 | VERIFIED | R14 | P1 | [L] | full | Exact disclosure rule. |
| FC-30 | Changed odds, including boosts and changed eligible outcomes, must be shown accurately. | 405 | RR-03 | VERIFIED | R14 | P1 | [L] | none | Applies to boosts and rotating pools. |
| FC-31 | PolicyService restrictions include ArePaidRandomItemsRestricted and IsPaidItemTradingAllowed. | 405 | RR-04 | VERIFIED | R14 | P1 | [L] | none | Exact API names and meaning; code will use them. |
| FC-32 | An official clarification dated 2026-05-26 reinforces compliance expectations for paid random items. | 405, 425 | RR-05 | VERIFIED | R15 | P1 | ix | part | What the clarification adds is not stated in LP. |
| FC-33 | Experience and community social-link guidance: links are for age-checked users 16 and older. | 409, 426 | RR-06 | VERIFIED | R16 | P1 | [L] | none | Age threshold; whose age is unstated (X-32). |
| FC-34 | Up to 3 links are permitted on experiences and communities. | 409, 426 | RR-07 | VERIFIED | R16 | P1 | [L] | none | Count limit; surface-specific. |
| FC-35 | Links must not be shared directly within experiences. | 409 | RR-08 | VERIFIED | R16 | P1 | [L] | full | Affects in-game feedback and community prompts. |
| FC-36 | Creators must describe experience content through Roblox's maturity questionnaire. | 413 | RR-13 | VERIFIED | R17 | P1 | [L] | part | Seasonal content may change the answers. |
| FC-37 | Ad integrations require a user-eligibility check and the required ad labels and disclosures. | 415 | RR-14 | VERIFIED | R18 | P1 | [L] | full | Brand and sponsored events. |
| FC-38 | Community Standards restrict commercial use of sensitive real-world events. | 417 | RR-15 | VERIFIED | R19 | P1 | [L] | none | Holiday and trend screening; page date unknown. |
| FC-39 | No Roblox rule banning truthful limited-time offers was found by the paper (a negative claim); the false-time-pressure ban is a notification rule. | 419, 429 | RR-16 | OPINION | none | P1 | - | n/a | Check Roblox monetization and advertising policies for any urgency or scarcity rule before the skill says "allowed". |
| FC-40 | Roblox's season-pass guidance treats a different context from the notification prohibitions; scarcity can support seasonal identity. | 528 | RR-17 | OPINION | R05, R08 | P1 | [L] | part (one-month start only) | Season-pass rule or only a design recommendation? |
| FC-41 | Roblox configs let creators change configured values without publishing a new version. | 474, 517 | PR-05 | VERIFIED | R21 | P1 | [L] | part (needs code use) | Basis for safe-disable design. |
| FC-42 | RDC26 listed an "Observability Platform" for "Late 2026"; a roadmap statement only. | 518, 511 | DN-16, N-25 | VERIFIED | R20 | P1 | [PC], ix | full | Window ends soon; may have shipped or slipped. |
| FC-43 | Roblox guidance distinguishes cadence updates that build on existing systems (R01) and says many games release cadence updates every two weeks to one month (R02). | 497, 527 | DN-02, OQ-04 | OPINION (evidence cited) | R01, R02 | P1 | [L] | full | Update rhythm: the owner asked for a check. |
| FC-44 | Brawl Stars 2025 review (2026-03-07) holds a caution about production and attention that the paper uses against copying viral events. | 498 | DN-03 | OPINION | G10 | P2 | - | none | Pairing unverifiable here (X-36). |
| FC-45 | G05 (Fortnite, 2023-11-05 record day) and G10 illustrate the difference between peak counts or a launch spike and later retention (normalized result). | 501, 502 | DN-06, DN-07 | OPINION | G05, G10 | P2 | - | none | Case use only; no benchmark. |
| FC-46 | League patch 26.17 notes (2026-08-25) say the studio does not want to adjust so frequently; the paper uses it against reflex nerfs. | 503 | DN-08 | EXPERIENCE / OPINION | G07 | P2 | [PC] | part | Post-cutoff source. |
| FC-47 | The Roblox/Uplift case study (2026-08-24) is the paper's evidence for testing social-action rewards; no controlled lift disclosed. | 504 | DN-09 | EXPERIENCE / OPINION | R11 | P2 | [PC] | part (trading hub only) | Pairing with "social actions" unverified (X-36). |
| FC-48 | Roblox guidance of "fewer than three weeks" per update, and a Brawl statement of "equivalent to 3 Brawlers" as effort. | 525 | OQ-02 | OPINION | none cited | P1 | - | n/a | Numbers without a source id here (X-35); update-rhythm claim. |
| FC-49 | Cadence directions differ across sources: weekly "ideal" (R04), two weeks to one month (R02), Adopt Me's flexible schedule (G01), Minecraft's variably sized drops (G21). | 527 | OQ-04 | OPINION | R01-R04, G01, G21 | P1 | [L] | part | Update rhythms; paper's resolution is capacity and fit. |
| FC-50 | Adopt Me year-end post dated 2023-12-28 reports 56 weekly updates but carries a conflicting "In 2024" heading. | 529 | OQ-06 | OPINION | G03 | P1 | - | part (heading only) | Number and date inconsistency. |
| FC-51 | Hearthstone (catalog dates, Class Sets structure of 2026-04-27), Clash Royale and Destiny (2025-05-06 roadmap) announcements show operating choices without proven results. | 534 | OQ-11 | OPINION | G22-G26 | P2 | [L] (G22) | part | Case dates and schedules. |
| FC-52 | GDC evidence on Destiny and feedback practice is limited to abstracts. | 532 | OQ-09 | OPINION | G25, G27 | P3 | abs | part | Limit of the evidence. |
| FC-53 | No accessible dated primary account of Deadlock's schedule change was found, so it is excluded from the ten cases. | 533 | OQ-10 | OPINION | none | P3 | - | n/a | A negative claim; a future revision may add Valve posts. |

## 11. Contradictions and limits

### 11.1 Limits the paper itself states

| ID | LP | Limit | Handling for skills |
| --- | --- | --- | --- |
| X-01 | 522 | The open questions must stay in the trained agent and must not be filled with a plausible number. | Carry OQ-01 to OQ-12 into the live-ops skill as stated limits. |
| X-02 | 524 | Causal retention, revenue and returner lifts of most studied updates are not public. | Never borrow another game's lift; ask for studio-owned data. |
| X-03 | 525 | Update development time is largely undisclosed; guidance and statements are not person-day estimates. | Do not turn "fewer than three weeks" or "3 Brawlers" into an effort figure. |
| X-04 | 526 | No universal retention target, cadence, event length, currency multiplier or revenue gain. | State as unknown; the owner and game data decide. |
| X-05 | 527 | Cadence sources disagree (weekly "ideal", every two weeks to one month, flexible schedule, smaller drops). | Resolve by capacity and player fit; never average. |
| X-06 | 528 | Scarcity vs pressure: Roblox season-pass guidance and notification bans cover different contexts; the wider ethic is OPINION. | Label the studio standard as a studio standard (RP-19). |
| X-07 | 529 | G03 holds a conflicting heading; no 2023 count benchmark. | Do not quote 56 as a benchmark. |
| X-08 | 530 | Link and notification thresholds differ by surface. | Per-surface eligibility in each brief (RP-08, RP-09). |
| X-09 | 531 | RDC26 talks not reviewed; only a roadmap line used. | Cite the announcement only, as roadmap. |
| X-10 | 532 | GDC evidence is abstracts only. | No slide statistics or speaker quotes. |
| X-11 | 533 | Deadlock excluded; secondary cadence reports not promoted. | Do not use Deadlock cadence. |
| X-12 | 534 | Supplementary cases show choices, not shipped results. | Cases are mechanisms. |
| X-13 | 535 | No studio data supplied; a real plan would be speculation. | Templates only; fill with owner data. |
| X-14 | 403 | The rules section reports guidance at the cutoff; later revisions and local requirements are not covered. | Re-check every rule at design time and at review. |
| X-15 | 419 | No blanket ban on truthful limited-time offers established; the notification ban is not an offer policy. | Do not write "Roblox bans limited-time offers" or "allows" without a check (FC-39). |
| X-16 | 378 | The fishing example is illustrative. | No benchmark from it. |
| X-17 | 346 | Event-chart windows are not a control group; before/after confounded. | Use the chart for questions only. |
| X-18 | 388 | Neither G17 nor G24 gives a portable retention lift. | Test catch-up on the real returner cohort. |
| X-19 | 299 | No evidence that "[UPDATE]" guarantees a boost. | Treat the tag as communication. |
| X-20 | 291 | Event and announcement limits are channel constraints, not cadence advice. | Never fill every slot. |
| X-21 | 297 | Roadmap labels are the paper's convention. | Do not call them a Roblox standard. |
| X-22 | 342, 344 | L, D1/D7/D30 and thresholds are not universal numbers. | Parameters chosen per game. |
| X-23 | 250 | G27 is an abstract; the full talk was not reviewed. | Do not paraphrase beyond the abstract. |
| X-24 | 583 (register) | R11 discloses no controlled lift for the cited cases. | Do not quote a lift from R11. |
| X-25 | 433 | The weekly cycle is an internal rhythm, not a publishing duty. | Do not read "weekly" as a release cadence (X-38). |
| X-26 | 474 | A config switch is not a rollback of persistent state. | Test the disable path. |
| X-27 | 365 | Rollback may erase legitimate gains; the studio cannot promise refunds. | State-safe response defined before launch. |
| X-28 | 516 | No universal staffing count. | Name an owner per deliverable. |

### 11.2 Gaps and tensions found by the extractor (not stated by the paper)

| ID | LP | Item | Handling for skills |
| --- | --- | --- | --- |
| X-29 | 405-417 | Most register key lines are one short phrase. For many Roblox claims the key line backs only part of the sentence (see "Key line" in section 10). Examples: R07 key line covers only the 3-day rule; R09 only 14-60 days; R10 only "up to three events"; R14 only the 100% sum; R16 only "no direct sharing"; R17 only the questionnaire name; R19 only a heading; R21 only "do nothing unless used in code". | Re-read the full page for each part; do not treat the key line as proof of the sentence. |
| X-30 | 293, 411, 419 | The paper describes R08 in three ways: "should relate to activity, must not require opt-in" (293); "prohibit compulsory opt-in and deceptive pressure" (411); "documented notification ban on false time pressure" (419). Only the opt-in line is in the register key line. | Check the exact wording of "deceptive pressure" and "false time pressure" before using either. |
| X-31 | 411, 508 | Two age thresholds appear (13+ for notifications, 16+ for social links), and the do-not-do row speaks of "younger players" without an age. The paper does not define "younger". | Name the exact surface and threshold in every brief (RP-08); never write "younger players" as a rule. |
| X-32 | 409, 426 | "Age-checked users 16 and older": the paper does not say whether the age rule is for the viewer, the poster or the community owner. | Do not state who must be 16+ until R16 is read. |
| X-33 | 346, 365, 374 | Tag tensions: LP:346 puts an inference ("no control group") inside a VERIFIED group. LP:365 states the refund limit inside an OPINION paragraph while LP:374 marks it VERIFIED. | Keep both tags as written; fact-check the refund rule as VERIFIED only after reading R22. |
| X-34 | 388, 397, 721 | G24: LP:388 tags it EXPERIENCE and says King Tower level is "preserved"; LP:397 says "preserved or increased". The register calls G24 "EXPERIENCE for simplification rationale; VERIFIED migration announcement". The key line (simple, clear, rewarding) does not mention King Tower. | Read G24 before quoting either wording. |
| X-35 | 525, 533 | The numbers "fewer than three weeks" and "3 Brawlers", and the phrase "ten longitudinal cases", have no source id and are not explained inside LP:248-536 (they belong to the first half of the paper). | Take the source from the first-half note before using them. |
| X-36 | 498, 501, 502, 504 | The do-not-do table pairs claims with sources whose content is not described in lines 248-536: G10 "production/attention caution"; G05 and G10 "measurement distinctions"; R11 for reward-for-social-actions testing. The register key lines for G05 (44.7 million players), G10 (revenue and MAU about 20% down) and R11 (trading hub) do not show these pairings. | Verify each pairing at the source; treat the row as OPINION only until then. |
| X-37 | 421 | The paper says an owner preference does not override platform rules. The kit's AGENTS.md says the owner in chat wins on anything. | The skill should state: the owner decides studio choices; no one can waive a Roblox rule; the agent flags the conflict (needs-decision). |
| X-38 | 433, 527 | R04 calls weekly update cadence ideal; the paper's weekly rhythm is for decisions, not publishing. | Keep the two separate in the skill. |
| X-39 | 346 | R10 is dated 2025-10-21, exactly one year before the cutoff, and was read through excerpts; the paper gives "7 or 14 days after" without saying when each applies. | Re-read the thread; do not state which window applies. |
| X-40 | 417 | R19 has no date; the key line is only a section heading. | Locate the exact policy text before citing it. |
| X-41 | 518 | "Late 2026" is already close at the cutoff date (2026-10-21). | Check whether the feature shipped or slipped before telling the owner. |
| X-42 | 283, 396 | Summary rows tag a negative or inferential claim with a source's mark: N-02 "no universal weights" under EXPERIENCE; N-13 "no universal safe currency multiplier" under VERIFIED / OPINION. | Treat the absence statements as the paper's own. |
| X-43 | 427, 293 | The 13+ threshold is described as "eligible 13+ users" and "eligible age threshold"; the paper does not define "eligible" (for example regional or account conditions). | Read R08 for conditions. |
| X-44 | 402-429 | The §10 table row at LP:428 mixes marks ("VERIFIED / OPINION"): the existence of maturity and ad rules is VERIFIED; "no universal exemption for events" is OPINION. | Split the two when quoting. |
| X-45 | 527, 543-555 | The Roblox cadence sources in the register give different rhythms: "weekly ideal" (R04), "every two weeks to one month" (R02), and a season-pass starting point of one month (R05). These are for different things (updates, content, seasons). | Do not merge into one Roblox cadence number. |

## 12. Line coverage (check C1)

Every non-blank line from 248 to 536 is covered. Blank lines (no text): 249, 251, 253, 255, 257, 259, 261, 263, 265, 271, 275, 277, 279, 286, 288, 290, 292, 294, 296, 298, 300, 302, 307, 310, 315, 318, 321, 324, 327, 330, 337, 339, 341, 343, 345, 347, 349, 351, 353, 355, 364, 366, 368, 375, 377, 379, 381, 383, 385, 387, 389, 391, 393, 400, 402, 404, 406, 408, 410, 412, 414, 416, 418, 420, 422, 430, 432, 434, 436, 451, 453, 461, 463, 465, 467, 469, 471, 473, 475, 477, 491, 493, 512, 519, 521, 523, 536.

| LP | Content | Where it went |
| --- | --- | --- |
| 248 | Heading, section 6 | heading only |
| 250 | Evidence base (R13, G28, G27) | FB-01 to FB-03 |
| 252 | Collection paths | FB-04 to FB-09 |
| 254 | How to ask | FB-10 to FB-14 |
| 256 | Moderation vs research | FB-15 to FB-17 |
| 258 | Taxonomy | FB-18 to FB-21 |
| 260 | Counting | FB-22 to FB-27 |
| 262 | Loud and silent | FB-28 to FB-32 |
| 264 | Heading, feedback sorting template | section 1.3 |
| 266-270 | Template header fields | FT-01 to FT-05 |
| 272-274 | Template table header, separator and example row | FT-06 to FT-13 (273 separator: markup only) |
| 276 | Quality checks | FT-14 to FT-20 |
| 278 | Closing the loop | FB-33 to FB-36 |
| 280-281 | Summary table header and separator | header only; rows in N-01 to N-04 |
| 282-285 | Summary rows | N-01 to N-04 |
| 287 | Heading, section 7 | heading only |
| 289 | Promise ledger | CM-01 to CM-03 |
| 291 | Event and announcement limits | CM-04 to CM-08 |
| 293 | Personalized notifications | CM-09 to CM-12 |
| 295 | Communication sequence | CM-13 to CM-15 |
| 297 | Roadmap | CM-16 to CM-18 |
| 299 | Discovery signals; update tag | CM-19 to CM-21 |
| 301 | Heading, patch-notes template | section 2.3 |
| 303-306 | Template title and header lines | PN-01 to PN-04 |
| 308-309 | New content | PN-05 |
| 311-314 | Balance and progression | PN-06 |
| 316-317 | Quality-of-life and fixes | PN-07 |
| 319-320 | Known issues | PN-08 |
| 322-323 | From your feedback | PN-09 |
| 325-326 | What to expect next | PN-10 |
| 328-329 | Feedback route | PN-11 |
| 331-332 | Summary table header and separator | header only; rows in N-05 to N-08 |
| 333-336 | Summary rows | N-05 to N-08 |
| 338 | Heading, section 8 | heading only |
| 340 | Roles; pre-release agreements | ME-01 to ME-03 |
| 342 | Reactivation | ME-04 to ME-07 |
| 344 | Retention | ME-08 to ME-11 |
| 346 | Event analytics | ME-12 to ME-16 |
| 348 | Native experiments | ME-17 to ME-21 |
| 350 | Causal discipline | ME-22 to ME-25 |
| 352 | Low traffic | ME-26, ME-27 |
| 354 | Revenue | ME-28 to ME-31 |
| 356-357 | Failure-response table header and separator | header only |
| 358-363 | Failure-response rows | FR-01 to FR-06 |
| 365 | When an update fails | ME-32 to ME-38 |
| 367 | Decision | ME-39 to ME-41 |
| 369-370 | Summary table header and separator | header only; rows in N-09 to N-12 |
| 371-374 | Summary rows | N-09 to N-12 |
| 376 | Heading, section 9 | heading only |
| 378 | Economy guidance | LH-01 to LH-03 |
| 380 | Economy ledger | LH-04 to LH-07 |
| 382 | Inflation | LH-08 to LH-11 |
| 384 | Power | LH-12 to LH-15 |
| 386 | Catch-up | LH-16 to LH-19 |
| 388 | Overwatch, Clash Royale | LH-20 to LH-22 |
| 390 | Burnout | LH-23 to LH-25 |
| 392 | Adopt Me; AI-studio burnout | LH-26 to LH-30 |
| 394-395 | Summary table header and separator | header only; rows in N-13 to N-16 |
| 396-399 | Summary rows | N-13 to N-16 |
| 401 | Heading, section 10 | heading only |
| 403 | Policy as release gate | RP-01, RP-02 |
| 405 | Paid random items | RR-01 to RR-05 |
| 407 | Transaction chain | RP-03 to RP-05 |
| 409 | Social links | RR-06 to RR-08; RP-06, RP-07 |
| 411 | Notification eligibility | RR-09 to RR-11; RP-08 to RP-10 |
| 413 | Maturity | RR-13; RP-11 to RP-13 |
| 415 | Ad integrations | RR-14; RP-14, RP-15 |
| 417 | Sensitive real-world events | RR-15; RP-16 |
| 419 | Limited-time offers | RR-16; RP-17 to RP-19 |
| 421 | Event launch checklist | RP-20 to RP-22 |
| 423-424 | Summary table header and separator | header only; rows in N-17 to N-21 |
| 425-429 | Summary rows | N-17 to N-21 |
| 431 | Heading, section 11 | heading only |
| 433 | Weekly rhythm | PR-01 to PR-03 |
| 435 | Heading, step method | section 6.2 |
| 437-438 | Step table header and separator | header only |
| 439-450 | Twelve steps | ST-01 to ST-12 |
| 452 | Heading, update brief | section 6.3 |
| 454-460 | Brief fields | UB-01 to UB-07 |
| 462 | Game designer receives | HO-01 |
| 464 | Progression designer receives | HO-02 |
| 466 | Builders receive | HO-03 |
| 468 | Marketing receives | HO-04 |
| 470 | Analyst receives | HO-05 |
| 472 | Release owner receives | HO-06 |
| 474 | Live configuration | PR-05 to PR-08 |
| 476 | Heading, post-update review | section 6.5 |
| 478-490 | Review fields | PV-01 to PV-13 |
| 492 | Heading, do-not-do | section 6.6 |
| 494-495 | Do-not-do table header and separator | header only |
| 496-511 | Sixteen rows | DN-01 to DN-16 |
| 513-514 | Summary table header and separator | header only; rows in N-22 to N-25 |
| 515-518 | Summary rows | N-22 to N-25 |
| 520 | Heading, open questions | section 7 |
| 522 | Framing | OQ-00 |
| 524-535 | Twelve bullets | OQ-01 to OQ-12 |
