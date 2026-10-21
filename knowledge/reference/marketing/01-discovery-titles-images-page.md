---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: "J012-T01, Roblox_Marketing_Agent_Research_2026.txt lines 1-115"
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-21

# Marketing paper part 1: evidence method, 15 rules, discovery, titles, icons / thumbnails / personalization, game page and native gameplay video (lines 1-115)

Paraphrased notes. The paper (MP) stays outside git. Every row cites `MP:<line>`. Nothing here is fact-checked: claims are the paper's, listed in section 9 for the fact-check pass. The paper's research cutoff is 2026-10-21. Most of its Roblox sources are dated mid-2026 or later, so none of them can be confirmed from memory: check them live. The paper is strong evidence, not gospel: its own limits sit next to the claims they limit and are collected in section 10. Extraction only: no web access was used.

## 0. How to read

| Key | Meaning |
| --- | --- |
| MP:n | line n of `Roblox_Marketing_Agent_Research_2026.txt`. One paragraph = one line. Source register = MP:529-1164 (only entries cited in lines 1-115 are resolved here, section 8). Register entries are cited by their first line. |
| Tag | The paper's own mark, copied unchanged. VERIFIED = official rule, documented product behavior or directly documented measurement; it does NOT mean the author audited Roblox's algorithm, ran a campaign or tested an account (MP:11). EXPERIENCE = a developer's, publisher's, platform's or vendor's reported outcome or interpretation (MP:11). OPINION = the paper's proposed procedure or reasoned application; not established causality (MP:11). "none" = framing text the paper does not tag. |
| Paragraph tag | The paper tags a whole paragraph with one mark. When a VERIFIED paragraph ends with the paper's own advice, the row keeps VERIFIED and the Kind column says PROC. Do not read such advice as a Roblox rule (X-09). |
| Kind (my label) | RULE = official rule, limit, size or eligibility. MECH = documented platform behavior. CASE = reported outcome of a named game. PROC = the paper's proposed procedure or advice. LIMIT = a caveat the paper states. FRAME = framing. The paper itself uses only Tag. |
| Src | The paper's source id, resolved in section 8 with date and URL. "live" = the paper marks the source as live documentation. "undated, acc 2026-10-21" = the source shows no date; the paper only read it that day. Access is not publication (MP:11). |
| Row IDs | EM evidence method, RU rule, DI discovery, TI title, IM icon / thumbnail / personalization, PG page / video, N number, FC claim to check, X contradiction or limit. Written with a hyphen (RU-01). Source ids N01-N12 in the paper are source entries (non-Roblox cases), not number rows; number rows here are written N-01. |
| Terms | RFY = Recommended For You. PTR = play-through rate (expansion inferred from MP:51; not spelled out in lines 1-115). qPTR = qualified play-through rate; for thumbnails: qualified Home-recommendation plays divided by Home-recommendation impressions (MP:87). CCU = concurrent users. DAU = daily active users. |
| Post-cutoff | Source dated after 2026-06-01 (the studio's flag). Undated live documents are marked "live-read" instead: they were read on 2026-10-21 and may have changed since. |
| Rule of use | The paper's OPINION rows are proposed checks, never Roblox policy. Never write "Roblox requires X" from a PROC or OPINION row. Platform lift numbers are platform-reported results, not forecasts. |

## 1. Evidence method (MP:1-13)

| ID | MP | Kind | Lesson | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| EM-1 | 1, 3, 5 | FRAME | The paper is a 2026 study of marketing Roblox games, built as evidence plus operating procedures for an AI marketing agent. Research cutoff: 2026-10-21. | none | - |
| EM-2 | 7 | FRAME | Purpose: train a Roblox studio's marketing agent to make truthful, distinctive campaigns and judge whether they bring suitable players into the game. Topics: discovery, packaging, gameplay video, creators, advertising, updates, community, measurement. Central recommendation: optimize the whole promise-to-play journey, not isolated impressions, views or clicks. | none | - |
| EM-3 | 7 | FRAME | Authority: the owner stays creative director and decision-maker. The agent proposes creative work and measurement plans. Research is not permission to publish, contact creators, buy advertising or make contractual commitments. | none | - |
| EM-4 | 11 | FRAME | VERIFIED is a narrow mark: official rule, documented product behavior, or a directly documented measurement. It does not mean the author audited Roblox's algorithm, ran the campaign or tested an account. | none | - |
| EM-5 | 11 | FRAME | EXPERIENCE marks an outcome or reading reported by a developer, publisher, platform or vendor. OPINION marks a proposed studio procedure or reasoned application, not established causality. | none | - |
| EM-6 | 11 | FRAME | Each source id resolves to a date, a direct URL and one short quote in the dated register. Undated living documents are dated by access day; no publication date is invented. | none | - |
| EM-7 | 13 | LIMIT | One source can carry two marks: its concrete rule and its commercial success claim can differ. | OPINION | MP editorial method, 2026-10-21 |
| EM-8 | 13 | LIMIT | A randomized study reported by a platform stays "platform-reported evidence" when its full method is not available. | OPINION | MP editorial method, 2026-10-21 |
| EM-9 | 13 | LIMIT | A case can show a useful mechanism without showing the expected return for another game. | OPINION | MP editorial method, 2026-10-21 |
| EM-10 | 13 | LIMIT | OPINION items are the paper's own synthesis as of the cutoff. Their cited sources explain the constraint or the example; they do not prove the recommendation works. | OPINION | MP editorial method, 2026-10-21 |
| EM-11 | 531 | LIMIT | Register preface: dates are split into publication, update and access. A quote is a short anchor, not a substitute for the full source. Ids that share one URL share one quote. Company and vendor outcome reports stay EXPERIENCE even when the host page is official. (Register text, outside lines 1-115, kept because it limits every EXPERIENCE row.) | none | - |

## 2. The fifteen rules (MP:17-45)

Each rule carries the paper's mark and its sources. A VERIFIED mark covers the platform fact in the source, not an outcome. Detail for rules 1-6 is in sections 3-6. Rules 7-15 are only stated here: their body text sits outside lines 1-115 and is not extracted in this note (X-21).

| ID | MP | Rule in my words | Tag | Src | Detail in |
| --- | --- | --- | --- | --- | --- |
| RU-01 | 17 | Have a custom thumbnail ready before relying on Home recommendations. The requirement took effect 2026-10-19. | VERIFIED | D01, 2026-10-19 | DI-01 to DI-03 |
| RU-02 | 19 | Judge RFY with its organic-acquisition cohort and the current behavior windows, not the whole game's mixed traffic. | VERIFIED | D02, 2026-06-15 | DI-04 to DI-06 |
| RU-03 | 21 | Sell a playable fantasy under a distinct name. No controlled optimum for title length was established. | OPINION | D05, acc 2026-10-21; C01-C06 | TI-01 to TI-15 |
| RU-04 | 23 | Thumbnail personalization is adaptive allocation, not a conventional fixed-allocation A/B test. | VERIFIED | D08, 2024-11-13, updated 2025-02-13 | IM-10 to IM-13 |
| RU-05 | 25 | Keep native Roblox gameplay previews apart from voiced social trailers; their rules differ. | VERIFIED | D07, acc 2026-10-21 | IM-09, PG-12 |
| RU-06 | 27 | Treat a spectacular studio case as a source of hypotheses, not a forecast and not a license to copy protected IP. | OPINION | C01-C06; N01-N09 | TI-09 to TI-12, IM-24 |
| RU-07 | 29 | YouTube states no minimum posting cadence for Shorts to perform well. | VERIFIED | S01, acc 2026-10-21 | outside part (X-21, X-22) |
| RU-08 | 31 | A creator quote must name deliverables, rights, disclosures and measurement. Follower count is not a rate card. | OPINION | P06-P09 | outside part |
| RU-09 | 33 | Current Ads Manager accounting and audience windows differ from old manual-bidding tutorials. | VERIFIED | P01, acc 2026-10-21; P02, 2025-04-09 | outside part |
| RU-10 | 35 | Ad eligibility depends on the format. Exposure to under-13 users, personalization for under-18 users and rewarded video are separate questions. | VERIFIED | P11, 2026-06-17; P12, 2026-10-09 | outside part |
| RU-11 | 37 | A sending ceiling is not an optimal cadence for updates or notifications. | OPINION | D13-D15 | outside part |
| RU-12 | 39 | Discord account integration does not override Roblox's ban on tracking users across platforms. | VERIFIED | S17, 2026-05-28, updated 2026-06-02; S18, 2026-06-02 | outside part |
| RU-13 | 41 | Annotate the 2026-10-12 Roblox recording change before reading acquisition trends. | VERIFIED | D16, 2026-10-12 | outside part (X-21) |
| RU-14 | 43 | Report views, clicks, plays, qualified plays, unique users and retention, each with its own denominator and window. | OPINION | D07, D17; S03-S05 | IM-06 (qPTR), IM-17 |
| RU-15 | 45 | The owner approves the promise, final assets, external communications and spend. The agent supplies drafts, evidence and reversible next steps. | OPINION | Studio operating design, 2026-10-21 (paper's own; not in register) | EM-3 |

## 3. How Roblox discovery works, October 2026 (MP:47-62)

### 3.1 Eligibility and RFY signals

| ID | MP | Kind | Lesson | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| DI-01 | 49 | RULE | Since 2026-10-19 a game needs at least one custom thumbnail to qualify for homepage-recommendation impressions. A default-only thumbnail is not enough. | VERIFIED | D01, 2026-10-19, live |
| DI-02 | 49 | LIMIT | Continue stays available to people who played the game before. The thumbnail rule is an eligibility gate, not a promise of impressions. | VERIFIED | D01, 2026-10-19, live |
| DI-03 | 49 | PROC | Paper's action: prepare a truthful 16:9 custom asset before counting on organic Home acquisition. (The 16:9 size itself is stated in MP:87; see IM-03.) | VERIFIED | D01, 2026-10-19, live |
| DI-04 | 51 | MECH | RFY widened its behavior evaluation from 7 days to 28 days, split into Day 1, Days 2-7 and Days 8-28. | VERIFIED | D02, 2026-06-15, live |
| DI-05 | 51 | MECH | As a ranking signal, PTR and first-play bounce rates replaced qualified play-through rate. | VERIFIED | D02, 2026-06-15, live |
| DI-06 | 51 | LIMIT | The announcement scopes these signals to users organically acquired through RFY, not the whole game's audience. | VERIFIED | D02, 2026-06-15, live |
| DI-07 | 53 | MECH | Discovery has two stages: retrieval, then ranking. | VERIFIED | D03, undated, acc 2026-10-21, live |
| DI-08 | 53 | MECH | Ads, search, friends, teleports, notifications and external sources can help a game enter consideration. Their users' engagement does not directly become RFY-ranking cohort engagement. | VERIFIED | D03 |
| DI-09 | 53 | MECH | Highest-priority ranking signals: PTR, first-play bounce, play days per user, playtime per user. | VERIFIED | D03 |
| DI-10 | 53 | MECH | Bounce reporting separates sessions under 60 seconds from sessions of 61-180 seconds. | VERIFIED | D03 |
| DI-11 | 53 | RULE | Counted playtime is capped at 60 minutes per user, per game, per day. | VERIFIED | D03 |
| DI-12 | 53 | MECH | Next-tier signals: intentional co-play days, qualified sessions, spend days, Robux per user. | VERIFIED | D03 |
| DI-13 | 53 | MECH | The emphasis is per-user averages, not totals. | VERIFIED | D03 |
| DI-14 | 53 | LIMIT | Benchmarks are comparison aids, not direct inputs to the algorithm. | VERIFIED | D03 |
| DI-15 | 53 | MECH | Seasonality, competitor performance and platform changes can affect impressions. | VERIFIED | D03 |
| DI-16 | 53 | RULE | Metadata that is misleading, reward-led or too similar to existing games can reduce exposure. | VERIFIED | D03 |
| DI-17 | 53 | MECH | Semantic search supports natural-language intent, not only exact-title matching. | VERIFIED | D03 |

### 3.2 Diagnosis and chart reading

| ID | MP | Kind | Lesson | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| DI-18 | 55 | PROC | Diagnose low distribution in this order: playable audience and moderation, then custom-thumbnail eligibility, then the real acquisition source, then RFY PTR and bounce, then mature return-play windows. | OPINION | basis D01-D03 |
| DI-19 | 55 | LIMIT | Do not promise any of these: a fixed launch-day seed, guaranteed exploration after an update, a CCU threshold that unlocks Home, a universal benchmark. The official sources the paper examined do not establish them. | OPINION | basis D01-D03 |
| DI-20 | 55 | PROC | Treat growth that follows advertising as a hypothesis to measure, not as purchased ranking credit. | OPINION | basis D01-D03 |
| DI-21 | 57 | MECH | Top Playing Now is a real-time, CCU-based Charts sort, released globally on mobile, tablet, desktop and web. | VERIFIED | D04, 2025-03-05, terminology updated 2025-04-29, live |
| DI-22 | 57 | LIMIT | Do not confuse it with personalized RFY, lifetime visits, revenue, or a guaranteed Trending placement. | OPINION | D04 (basis) |
| DI-23 | 57 | PROC | With every competitive screenshot, save the sort, the filter, the retrieval time and the metric. Never infer a title's effectiveness from chart membership alone. | OPINION | D04 (basis) |

## 4. Titles that communicate a playable fantasy (MP:64-81)

| ID | MP | Kind | Lesson | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| TI-01 | 66 | RULE | Roblox advises recognizable names, discourages frequent renaming and repeated words, and recommends cautious decoration. | VERIFIED | D05, undated, acc 2026-10-21, live-read |
| TI-02 | 66 | RULE | Roblox's example allows one or two well-placed emojis. It does not claim a conversion uplift. | VERIFIED | D05 |
| TI-03 | 66 | RULE | The description should explain the game at once and use relevant keywords naturally. Irrelevant repetition can hurt discovery. Genre should match gameplay. | VERIFIED | D05 |
| TI-04 | 68 | PROC | Treat the title as part of a promise system: a clear activity gives comprehension, a distinctive condition gives curiosity, the real game gives the payoff. | OPINION | MP studio procedure, 2026-10-21 |
| TI-05 | 68 | PROC | A "what happens if" title works only when the game answers the question. Stakes must describe a real challenge, not false scarcity or an unavailable reward. | OPINION | MP studio procedure |
| TI-06 | 68 | LIMIT | A dramatic title that sets the wrong expectation can bring visits without good play. | OPINION | MP studio procedure |
| TI-07 | 70 | PROC | The paper's three original candidate titles illustrate mechanisms only: "One Floor Left" (survival constraint, but needs the image and first sentence to name the activity), "Build a Storm Shelter" (names action and threat), "Everyone Controls the Train" (social coordination fantasy). Use one only if the shipped game truly delivers it. | OPINION | MP studio procedure |
| TI-08 | 70 | LIMIT | These examples are not measured winners, not advice to imitate an existing title, and carry no CTR or conversion estimate. | OPINION | MP studio procedure |
| TI-09 | 72 | CASE | Wonder Works reported SpongeBob Tower Defense in the top 15 by Robux spent after 35 days, with nearly 125 million visits and a 40-minute average session. | EXPERIENCE | C01, 2025-03-17 |
| TI-10 | 72 | LIMIT | These are licensed-game outcomes, not a title test. The source does not show the title's incremental contribution or any retention cohort. | EXPERIENCE | C01, 2025-03-17 |
| TI-11 | 74 | CASE | Non-Roblox example: Playstack explains Balatro through a familiar gameplay combination and its Joker-driven progression. | VERIFIED | N05, undated, acc 2026-10-21 |
| TI-12 | 74 | CASE | The publisher later reported more than five million units sold. Neither this nor TI-11 isolates a title effect. | EXPERIENCE | N06, 2025-01-21 |
| TI-13 | 74 | PROC | Borrow the clarity of the explanation, not a claim that short or unusual names cause sales. | OPINION | N05, N06 (basis) |
| TI-14 | 76 | LIMIT | Unknown: a causally optimal Roblox title word count, character count, emoji count, or update-tag uplift. A platform's allowed length is not an optimum. | OPINION | D05, C01-C06 (rule table MP:79) |
| TI-15 | 76 | PROC | To investigate a title: archive old and new text with timestamps, hold other packaging stable where possible, split by acquisition surface, and treat an uncontrolled rename as observational. | OPINION | MP studio procedure |
| TI-16 | 76 | LIMIT | A small player-comprehension exercise can show confusion but cannot give a population CTR estimate. Avoid frequent name changes that make the game hard to recognize. | OPINION | MP studio procedure |

## 5. Icons, thumbnails and native personalization (MP:83-103)

| ID | MP | Kind | Lesson | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| IM-01 | 85 | RULE | Icons are square and at least 512×512. Roblox suggests checking small renderings such as 150×150. Only one icon shows per locale. | VERIFIED | D06, undated, acc 2026-10-21, live-read |
| IM-02 | 85 | RULE | Icons go through moderation. Their job is a recognizable theme, tone and genre, not a miniature feature list. | VERIFIED | D06 |
| IM-03 | 87 | RULE | Thumbnail guidance: 1920×1080 at 16:9. | VERIFIED | D07, undated, acc 2026-10-21, live-read |
| IM-04 | 87 | RULE | Home personalization uses 2-5 active variants, under 3 MB. A single image does not personalize. (Scope of "under 3 MB" per image or per set is not stated: X-05.) | VERIFIED | D07 |
| IM-05 | 87 | RULE | A gallery allows up to ten images or videos. | VERIFIED | D07 |
| IM-06 | 87 | MECH | Thumbnail qPTR = qualified Home-recommendation plays divided by Home-recommendation impressions. | VERIFIED | D07 |
| IM-07 | 87 | RULE | Native videos get three free uploads per month; uploads rejected by policy consume the quota. | VERIFIED | D07 |
| IM-08 | 87 | RULE | Xbox, PlayStation and VR do not support native videos. | VERIFIED | D07 |
| IM-09 | 87 | RULE | A native preview must show representative gameplay. Not allowed: external footage, narration, voice-chat conversations, lyrical music. Sparse factual overlays are allowed. | VERIFIED | D07 |
| IM-10 | 89 | MECH | Roblox calls personalization a multi-armed bandit, not fixed-allocation A/B testing. | VERIFIED | D08, 2024-11-13, update 2025-02-13 |
| IM-11 | 89 | MECH | Traffic starts spread across the active assets, then shifts toward the stronger asset for each audience while some exploration continues. | VERIFIED | D08 |
| IM-12 | 89 | LIMIT | Launch guidance warns that games under 1,000 DAU may get no meaningful results. This is a practical warning, not a hard entry requirement. | VERIFIED | D08 |
| IM-13 | 89 | CASE | Historical launch test: +8.5% average qPTR lift, some outcomes at +50%. These are platform-reported test aggregates, not guaranteed returns for one game and not a present-day baseline. | EXPERIENCE | D08, 2024-11-13, update 2025-02-13 |
| IM-14 | 91 | RULE | Staff advice: avoid restarting within 7 days, keep several distinct concepts, change on substantial content updates. | VERIFIED | D09, 2025-02-13 |
| IM-15 | 91 | CASE | Later staff snapshot: over 8,000 adopting experiences, +12% average relative qPTR lift, some outcomes at +56%. | EXPERIENCE | D09, 2025-02-13 |
| IM-16 | 91 | LIMIT | The launch figures (IM-13) and snapshot figures (IM-15) differ because they are different reported snapshots, not evidence of a universal uplift. The 7-day advice does not guarantee statistical sufficiency and does not mean "publish every 7 days". | EXPERIENCE (figures); VERIFIED paragraph (advice limit) | D09 |
| IM-17 | 93 | MECH | A Roblox metrics reply said thumbnail personalization still reported qPTR while broader analytics moved toward all-play PTR, and that alignment was being worked on. Current thumbnail docs still say qPTR. | VERIFIED | D10, 2026-07-20 |
| IM-18 | 93 | PROC | In every result, keep the actual field name, tooltip, numerator, denominator, cohort and export timestamp. Never relabel qPTR as PTR. Never claim the migration is complete. The July reply shows a known transition, not the October UI for every creator. | OPINION | D10 (basis) |
| IM-19 | 95 | PROC | For a small team's first set, consider distinct concepts for core action, social situation and progression payoff, only where each exists in the game. A manageable production choice, not a measured optimum. | OPINION | basis D06-D10 |
| IM-20 | 95 | PROC | Ask unfamiliar viewers what action they expect, then compare it with the first playable session. An AI's predicted click score is not player evidence. | OPINION | basis D06-D10 |
| IM-21 | 95 | PROC | Keep the full approved set and identify every image by asset ID and version. | OPINION | basis D06-D10 |
| IM-22 | 95 | LIMIT | Allocation and audience shift over time, so a higher raw rate is not automatically a randomized causal effect. Icon swaps and gallery reordering need their own observation design; Home personalization does not show they changed conversion. | OPINION | basis D06-D10 |
| IM-23 | 97 | CASE | Splitting Point CEO Janzen Madsen credited thumbnail personalization with helping a dusty trip find its audience and reported over one billion plays. | EXPERIENCE | C01, 2025-03-17 |
| IM-24 | 97 | LIMIT | A testimonial: no creative exposure, no CTR or qPTR comparison, no retained-player attribution. The billion is not a count of unique people and not a causal estimate. | EXPERIENCE | C01, 2025-03-17 |

## 6. The game page and native gameplay preview (MP:105-115)

| ID | MP | Kind | Lesson | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| PG-01 | 107 | RULE | Existing YouTube embeds on game pages were scheduled for automatic removal starting 2026-09-30. Adding new ones has been disabled since November 2025. | VERIFIED | D11, 2026-09-18, effective 2026-09-30 |
| PG-02 | 107 | RULE | Supported replacement: free direct video upload in Creator Hub (Configure / Configurations, Places, the selected place, Videos), then approval. | VERIFIED | D11 |
| PG-03 | 107 | PROC | Launch checklist change: linking an external trailer is not the same as installing a native preview. | VERIFIED | D11 (paragraph tag) |
| PG-04 | 109 | MECH | Gameplay videos had fully rolled out in Home RFY (announcement 2026-08-31). | VERIFIED | D12, 2026-08-31, full rollout |
| PG-05 | 109 | RULE | The announcement advises showing actual current gameplay within the opening seconds, not a cinematic or promotional trailer. | VERIFIED | D12 |
| PG-06 | 109 | CASE | Roblox reported, for RFY when video was present: Superstar Baseball +30% plays and +31% playtime; Notoriety +41% plays and +39% playtime. Test window 2026-06-07 to 2026-06-26. | EXPERIENCE | D12 (same source), test window 2026-06-07 to 2026-06-26 |
| PG-07 | 109 | LIMIT | These are directional reported tests, not forecast multipliers. Public text gives no sample sizes, no confidence intervals, and not enough detail to reproduce the experiment. | EXPERIENCE | D12 |
| PG-08 | 109 | MECH | A 2026-09-01 reply says video annotations were added to Acquisition, Engagement and Retention; deeper video analytics were still to come at that time. | EXPERIENCE (paragraph tag from the same source) | D12, analytics reply 2026-09-01 |
| PG-09 | 111 | PROC | Page checklist: truthful title / genre / first-sentence summary; readable icon; approved custom Home image; gallery that shows the core action before secondary features; current approved native video; genuine available rewards; a specific event or return reason; device and age eligibility checked. | OPINION | basis D05, D07, D11, D12 |
| PG-10 | 111 | LIMIT | A badge listing is not evidence that its reward improves retention. | OPINION | basis D05, D07, D11, D12 |
| PG-11 | 111 | LIMIT | Do not claim every visitor sees the video, or that a supported preview plays automatically in every placement. | OPINION | basis D05, D07, D11, D12 |
| PG-12 | 111 | PROC | Keep the native Roblox gameplay preview separate from a voiced TikTok or YouTube edit; their content rules differ. | OPINION | basis D05, D07, D11, D12 |

## 7. Number register (MP:1-115)

### 7.1 The paper's own summary rows ("Rule | Number | Evidence mark | Source and date")

| ID | MP | Rule | Number | Mark (paper) | Source and date (paper) | Scope and limit (from nearby paper text) |
| --- | --- | --- | --- | --- | --- | --- |
| N-01 | 60 | Custom thumbnail before Home launch | At least 1 | VERIFIED | D01 / 2026-10-19 | Eligibility gate, not a promise of impressions (MP:49). |
| N-02 | 61 | Diagnose long-term RFY performance | D1, D2-7, D8-28 | VERIFIED | D02 / 2026-06-15 | Windows inside a 28-day evaluation, organic RFY cohort only (MP:51). |
| N-03 | 62 | No paid-ranking guarantee | No verified guaranteed threshold | OPINION, limitation | D03 / accessed 2026-10-21 | Examined official sources do not establish a CCU threshold or launch seed (MP:55). |
| N-04 | 79 | Do not invent an optimal title length | Unknown | OPINION evidence limit | D05 accessed 21 Oct 2026; C01-C06 | Allowed length is not an optimum (MP:76). |
| N-05 | 80 | A named game's growth is not a title experiment | Top 15 by Robux spent after 35 days | EXPERIENCE | C01 17 Mar 2025 | SpongeBob Tower Defense, licensed game, no title test (MP:72). |
| N-06 | 81 | Keep the promise and playable action aligned | No universal uplift supplied | OPINION | Studio procedure 21 Oct 2026 | No CTR or conversion estimate attached (MP:70). |
| N-07 | 100 | Icon master and small preview | 512×512; 150×150 example | VERIFIED | D06 / accessed 2026-10-21 | 512×512 is the minimum for a square icon; 150×150 is a suggested preview size (MP:85). |
| N-08 | 101 | Home active variant range | 2-5; under 3 MB | VERIFIED | D07 / accessed 2026-10-21 | Scope of "under 3 MB" not stated (X-05). |
| N-09 | 102 | Avoid constant restarts | at least 7 days is staff advice, not sufficiency | VERIFIED guidance | D09 / 2025-02-13 | Not a guarantee of statistical sufficiency; not "publish every 7 days" (MP:91). |
| N-10 | 103 | Record metric definition | PTR is not the same as qPTR | VERIFIED transition | D10 / 2026-07-20 | Known transition; do not assert it has finished (MP:93). |
| N-11 | 114 | Replace YouTube game-page embeds | Starting 2026-09-30 | VERIFIED | D11 / 2026-09-18 | Paper words it as "scheduled"; effect not confirmed in the part (X-07). |
| N-12 | 115 | Treat video lifts as cases | +30%/+31%; +41%/+39% plays/playtime | EXPERIENCE; June 7-26 tests | D12 / 2026-08-31 | RFY plays / playtime when video present; directional; no sample sizes (MP:109). |

### 7.2 Numbers that appear only in prose

| ID | MP | Number | Scope | Paper's limit | Tag | Src, date |
| --- | --- | --- | --- | --- | --- | --- |
| N-13 | 5 | Research cutoff 2026-10-21 | The whole paper | - | none | - |
| N-14 | 51 | 7 days to 28 days | RFY behavior evaluation window | Organic RFY users only | VERIFIED | D02, 2026-06-15 |
| N-15 | 53 | 60 s; 61-180 s | Bounce reporting buckets | - | VERIFIED | D03, acc 2026-10-21 |
| N-16 | 53 | 60 minutes per user / game / day | Cap on counted playtime | - | VERIFIED | D03 |
| N-17 | 49, 87 | 16:9; 1920×1080 | Thumbnail format | - | VERIFIED | D01 (16:9 in MP:49), D07 (both in MP:87) |
| N-18 | 85 | 1 icon per locale | Icon display | - | VERIFIED | D06 |
| N-19 | 66 | 1 or 2 emojis | Roblox's naming example | No conversion uplift claimed | VERIFIED | D05 |
| N-20 | 87 | Up to 10 images / videos | Gallery | - | VERIFIED | D07 |
| N-21 | 87 | 3 free uploads / month | Native videos; policy rejections consume quota | - | VERIFIED | D07 |
| N-22 | 89 | Under 1,000 DAU | Launch-guidance warning for personalization | Practical warning, not a hard entry rule | VERIFIED | D08 |
| N-23 | 89 | +8.5% average qPTR lift; some +50% | Historical launch test, platform-reported aggregates | Not guaranteed individual returns; not a present baseline | EXPERIENCE | D08, 2024-11-13 / 2025-02-13 |
| N-24 | 91 | 7 days | Staff advice on restarts | Not a sufficiency guarantee | VERIFIED | D09, 2025-02-13 |
| N-25 | 91 | Over 8,000 experiences; +12% average relative qPTR lift; some +56% | Later staff snapshot | Different snapshot from N-23; no universal uplift | EXPERIENCE | D09, 2025-02-13 |
| N-26 | 72 | Top 15 by Robux spent after 35 days; nearly 125 million visits; 40-minute average session | SpongeBob Tower Defense, reported by Wonder Works | Licensed game; no title effect; no retention cohort | EXPERIENCE | C01, 2025-03-17 |
| N-27 | 74 | More than 5 million units sold | Balatro (non-Roblox), publisher report | No title effect isolated | EXPERIENCE | N06, 2025-01-21 |
| N-28 | 97 | Over 1 billion plays | Splitting Point game, CEO testimonial | Not unique people; not causal | EXPERIENCE | C01, 2025-03-17 |
| N-29 | 107 | 2026-09-30 (removal start); November 2025 (new embeds disabled) | YouTube embeds on game pages | - | VERIFIED | D11, 2026-09-18 |
| N-30 | 109 | +30% plays / +31% playtime (Superstar Baseball); +41% / +39% (Notoriety); window 2026-06-07 to 2026-06-26; announcement 2026-08-31; reply 2026-09-01 | RFY plays and playtime when video was present | Directional; not guarantees; no sample sizes or confidence intervals | EXPERIENCE | D12 |
| N-31 | 17-45 | Dates inside the rule list: 2026-10-19; 2026-06-15; 2024-11-13 (updated 2025-02-13); 2025-04-09; 2026-06-17; 2026-10-09; 2026-05-28 (updated 06-02); 2026-06-02; 2026-10-12 | Source dates for RU-01 to RU-13 | See section 8 | per rule | per rule |
| N-32 | 55, 62 | None established: fixed launch-day seed, post-update exploration guarantee, CCU threshold that unlocks Home, universal benchmark | RFY | Mark unknown | OPINION | basis D01-D03 |
| N-33 | 76, 79 | None established: causal optimum for title word, character or emoji count; update-tag uplift | Roblox titles | Mark unknown | OPINION | D05; C01-C06 |
| N-34 | 70 | None attached: CTR or conversion estimate for the three example titles | Example titles | Mark unknown | OPINION | MP studio procedure |
| N-35 | 109 | None public: sample sizes, confidence intervals, reproducible detail | Video lift tests | Do not forecast | EXPERIENCE | D12 |
| N-36 | 97 | None given: creative exposure, CTR / qPTR comparison, retained-player attribution | Splitting Point testimonial | Do not infer causality | EXPERIENCE | C01 |
| N-37 | 29 | None specified by YouTube: minimum posting cadence for Shorts | YouTube Shorts | Not a statement that cadence is irrelevant (X-22) | VERIFIED | S01 |

## 8. Source ids used in lines 1-115 (resolved from MP:529-1164)

Quotes are the register's own, 15 words or fewer, attributed to the source; a few are shortened to a continuous part of the register quote to stay within the limit. "acc" = accessed by the paper. "Post-cutoff" = dated after 2026-06-01. "Cited at" = lines in 1-115.
| ID | Source | Date and limits | Post-cutoff | URL | Cited at MP | Reg. MP | Key quote (register) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| D01 | Roblox DevForum, "Homepage Recommendation Eligibility Now Requires a Custom Thumbnail" | 2026-10-19; acc 2026-10-21; live | yes | https://devforum.roblox.com/t/homepage-recommendation-eligibility-now-requires-a-custom-thumbnail/4945086 | 17, 49, 55, 60 | 533 | "Games with only a default thumbnail are not eligible for homepage recommendations." |
| D02 | Roblox DevForum, "Recommended For You Algorithm Improvements That Better Value Long-Term Retention" | 2026-06-15; acc 2026-10-21; live | yes | https://devforum.roblox.com/t/recommended-for-you-algorithm-improvements-that-better-value-long-term-retention/4684575 | 19, 51, 55, 61 | 541 | "We've updated the Recommended For You algorithm signals from 7 days to 28 days" |
| D03 | Roblox Creator Docs, "Discovery" | undated live doc; acc 2026-10-21 | live-read | https://create.roblox.com/docs/discovery | 53, 55, 62 | 549 | "Every signal reflects user behavior after they discover your game." |
| D04 | Roblox DevForum, "Introducing Top Playing Now on Charts" | 2025-03-05; terminology updated 2025-04-29; acc 2026-10-21; live | no | https://devforum.roblox.com/t/introducing-top-playing-now-on-charts/3529809 | 57 | 557 | "based on concurrent users (CCU)" |
| D05 | Roblox Creator Docs, "Create and publish games and places" | undated live doc; acc 2026-10-21 | live-read | https://create.roblox.com/docs/production/publishing/publish-games-and-places | 21, 66, 76, 79, 111 | 565 | "Frequent repetition of words or phrases may result in demotion of your game." |
| D06 | Roblox Creator Docs, "Icons" | undated live doc; acc 2026-10-21 | live-read | https://create.roblox.com/docs/production/publishing/experience-icons | 85, 95, 100 | 573 | "you can only display one icon per locale" |
| D07 | Roblox Creator Docs, "Thumbnails" | undated live doc; acc 2026-10-21 | live-read | https://create.roblox.com/docs/production/publishing/thumbnails | 25, 43, 87, 95, 101, 111 | 581 | "Thumbnail personalization only starts when you activate 2 or more thumbnails." |
| D08 | Roblox DevForum, "Live now: Personalize your thumbnails to attract more users" | 2024-11-13; update 2025-02-13; acc 2026-10-21 | no | https://devforum.roblox.com/t/live-now-personalize-your-thumbnails-to-attract-more-users/3257233 | 23, 89, 95 | 589 | "Personalization uses multi-arm bandit (instead of A/B testing)" |
| D09 | Roblox DevForum, "5 Tips From Roblox Staff to Get the Most Out of Thumbnail Personalization" | 2025-02-13; acc 2026-10-21 | no | https://devforum.roblox.com/t/5-tips-from-roblox-staff-to-get-the-most-out-of-thumbnail-personalization/3471689 | 91, 95, 102 | 597 | "Avoid restarting tests within 7 days" |
| D10 | Roblox DevForum, "QPTR is displaying incorrectly/inaccurately", reply 6 | 2026-07-20; acc 2026-10-21 | yes | https://devforum.roblox.com/t/qptr-is-displaying-incorrectlyinaccurately/4690988/6 | 93, 95, 103 | 605 | "the thumbnail personalization is not fully aligned with the algo now" |
| D11 | Roblox DevForum, "YouTube Videos Will Be Removed from Game Detail Pages" | 2026-09-18; effective 2026-09-30; acc 2026-10-21 | yes | https://devforum.roblox.com/t/youtube-videos-will-be-removed-from-game-detail-pages/4879633/1 | 107, 111, 114 | 613 | "The ability to add new YouTube videos has been disabled since November 2025." |
| D12 | Roblox DevForum, "Gameplay Videos on Home: Help Your Games Get Discovered" | 2026-08-31; test window 2026-06-07 to 2026-06-26; analytics reply 2026-09-01; acc 2026-10-21 | yes | https://devforum.roblox.com/t/gameplay-videos-on-home-help-your-games-get-discovered/4842601/1 | 109, 111, 115 | 621 | "Lifts are directional test results, not guarantees of future performance." |
| D13 | Roblox Creator Docs, "Experience events and updates" | undated live doc; acc 2026-10-21 | live-read | https://create.roblox.com/docs/production/promotion/experience-events | 37 | 629 | "you can publish a maximum of 10 ongoing or upcoming events" |
| D14 | Roblox DevForum, "Introducing Off-Platform Featuring for Creator Events" | 2025-12-10; acc 2026-10-21 | no | https://devforum.roblox.com/t/introducing-off-platform-featuring-for-creator-events/4142230 | 37 | 637 | "submitted at least 14 days prior to the event start date" |
| D15 | Roblox Creator Docs, "Experience notifications" | undated live doc; acc 2026-10-21 | live-read | https://create.roblox.com/docs/production/promotion/experience-notifications | 37 | 645 | "delivery of notifications is not guaranteed" |
| D16 | Roblox DevForum, "Improved Discovery Measurement in Creator Analytics" | 2026-10-12; acc 2026-10-21 | yes | https://devforum.roblox.com/t/improved-discovery-measurement-in-creator-analytics/4930122 | 41 | 653 | "Your historical data will not change." |
| D17 | Roblox Creator Docs, "Acquisition" | undated live doc; acc 2026-10-21 | live-read | https://create.roblox.com/docs/production/analytics/acquisition | 43 | 661 | "where new and returning users are coming from and how well they convert" |
| P01 | Roblox Creator Docs, "Ads Manager" | undated living doc; acc 2026-10-21 | live-read | https://create.roblox.com/docs/production/promotion/ads-manager | 33 | 693 | "The payment method cannot be changed after a campaign is published." |
| P02 | Roblox DevForum, "Leveling Up Ads Manager With New Features", staff reply 151 | 2025-04-09; acc 2026-10-21 | no | https://devforum.roblox.com/t/leveling-up-ads-manager-with-new-features/3587640/151 | 33 | 701 | "there's no need to set a manual bid" |
| P06 | FTC, "FTC's Endorsement Guides: What People Are Asking" | 2023 revision; acc 2026-10-21 | no | https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking | 31 | 733 | "a material connection rests with the influencer and the brand" |
| P07 | YouTube Help blog, "Giving you tools to easily disclose paid partnerships with new controls & automated disclosures" | 2026-09-03; acc 2026-10-21 | yes | https://support.google.com/youtube/blog/458476782/giving-you-tools-to-easily-disclose-paid-partnerships-with-new-controls-automated-disclosures | 31 | 741 | "Granular age & geographic controls for branded content" |
| P08 | YouTube Help, "Add branded content restrictions & disclosure labels" | undated living doc; acc 2026-10-21 | live-read | https://support.google.com/youtube/answer/154235 | 31 | 749 | "selecting the paid promotion button in your video details" |
| P09 | TikTok Support, "Promoting a brand, product, or service" | undated living doc; acc 2026-10-21 | live-read | https://support.tiktok.com/en/business-and-creator/creator-and-business-accounts/promoting-a-brand-product-or-service | 31 | 757 | "you must turn on the content disclosure setting" |
| P11 | Roblox DevForum, "New Advertising Policies & Standards" | policy effective 2026-05-04; revenue-share update 2026-06-17; acc 2026-10-21 | partly (update 2026-06-17) | https://devforum.roblox.com/t/new-advertising-policies-standards/4527365/1 | 35 | 773 | "The rates for 2027 are as follows" |
| P12 | Roblox Help, "Advertising Standards" | updated 2026-10-09; acc 2026-10-21 | yes | https://en.help.roblox.com/hc/en-us/articles/13722260778260-Advertising-Standards | 35 | 781 | "Ads may not be personalized for users under the age of 18." |
| C01 | Roblox Newsroom, "Unveiling the Future of Creation With Native 3D Generation, Collaborative Studio Tools, and Economy Expansion" | 2025-03-17; acc 2026-10-21 | no | https://about.roblox.com/newsroom/2025/03/unveiling-future-creation-native-3d-generation-collaborative-studio-tools-economy-expansion | 21, 27, 72, 79, 80, 97 | 845 | "really helped us find our audience" (about automatic thumbnail personalization) |
| C02 | GamesBeat, "How Grow a Garden took off on Roblox", Janzen 'Jandel' Madsen interview | 2025-09-07; updated 2025-09-08; acc 2026-10-21 | no | https://gamesbeat.com/janzen-madsen-interview/ | 21, 27 (range only) | 853 | "We implemented a live service. We started weekly updates." |
| C03 | The Gang, "Gabby's Dollhouse Official on Roblox" case study | undated; acc 2026-10-21 | live-read | https://www.thegang.io/case-studies/gabbys-dollhouse-case-study | 21, 27 (range only) | 861 | "DreamWorks could now film YouTube content directly inside the Roblox environment." |
| C04 | Medal, "Medal for Roblox Developers - Grow Your Game" (vendor page) | undated; acc 2026-10-21 | live-read | https://medal.tv/developer/roblox | 21, 27 (range only) | 869 | "Incentivize players to clip and post their best moments in your game" |
| C05 | Medal, "Medal x Sol's RNG - Partnership" (vendor page) | undated; acc 2026-10-21 | live-read | https://medal.tv/developer/roblox/solsrng | 21, 27 (range only) | 877 | "Estimated growth with a single activation" |
| C06 | Petrex, "Catch the Drop Roblox Case Study" | 2026 (no day); acc 2026-10-21 | unknown (month not given) | https://petrex.io/work/samsung-galaxy-store | 21, 27 (range only) | 885 | "traffic attributable to individual campaigns requires separate reporting" |
| S01 | YouTube Help, "Search and discovery tips: Shorts" | undated; acc 2026-10-21 | live-read | https://support.google.com/youtube/answer/11914225?hl=en | 29 | 893 | "There is no minimum posting cadence required for your videos to perform well." |
| S03 | YouTube Help, "Get started creating YouTube Shorts" | undated; change effective 2025-03-31; acc 2026-10-21 | live-read | https://support.google.com/youtube/answer/10059070?hl=en | 43 (range S03-S05) | 909 | "no minimum watch time requirement" |
| S04 | YouTube Help community, "An update to how we count public views across YouTube" | 2026-08-17; rollout confirmed 2026-08-27; acc 2026-10-21 | yes | https://support.google.com/youtube/thread/433409976?hl=en | 43 (range S03-S05) | 917 | "This standard will now apply globally across all formats." |
| S05 | YouTube Help, "Understand your YouTube video reach" | undated; acc 2026-10-21 | live-read | https://support.google.com/youtube/answer/9314355?hl=en | 43 (range S03-S05) | 925 | "This is calculated from engaged views and their corresponding watch time." |
| S17 | Discord blog, "Official Discord Integrations for Steal a Brainrot, Grow a Garden, Brookhaven RP, and more" | 2026-05-28; updated 2026-06-02; acc 2026-10-21 | partly (update 2026-06-02) | https://discord.com/blog/official-discord-integrations-for-steal-a-brainrot-grow-a-garden-brookhaven-rp-and-more | 39 | 1021 | "Users can deauthorize the experience at any time" |
| S18 | Roblox DevForum, "A Reminder About User Privacy and Third-Party Integrations" | 2026-06-02; acc 2026-10-21 | yes | https://devforum.roblox.com/t/a-reminder-about-user-privacy-and-third-party-integrations/4665118 | 39 | 1029 | "Creators may not track Roblox users across third-party platforms or services" |
| N01 | Supercell-issued Squad Busters global-launch announcement (PR Newswire) | 2024-05-29; acc 2026-10-21 | no | https://www.prnewswire.com/news-releases/chris-hemsworth-christina-ricci-ken-jeong-will-arnett-and-aulii-cravalho-squad-up-with-supercell-for-global-game-launch-302157916.html | 27 (range only) | 1069 | "the game has achieved 40 million pre-registrations" |
| N02 | Supercell, "In for the Forever Game" | 2025-02-11; acc 2026-10-21 | no | https://supercell.com/en/news/forever-game/ | 27 (range only) | 1077 | "has not yet scaled up to the game team's (or Supercell's) aspirations" |
| N03 | Supercell, "Squad Busters Development is Ending, Final Update in December 2025" | 2025-10-30; acc 2026-10-21 | no | https://supercell.com/en/news/squad-development-ending/ | 27 (range only) | 1085 | "we were not able to find a lasting solution to its core problems" |
| N04 | Supercell, "Thumbs Up For Brawl Community Event!" | 2024-06-10; acc 2026-10-21 | no | https://supercell.com/en/games/brawlstars/blog/community/thumbs-up-for-brawl-community-event/ | 27 (range only) | 1093 | "it adds to the tracker bar and you get rewards" |
| N05 | Playstack, Balatro official product page | undated; acc 2026-10-21 | live-read | https://www.playstack.com/games/balatro/ | 27, 74 | 1101 | "The poker roguelike." |
| N06 | Playstack, "Balatro Deals a Full House of Success" | 2025-01-21; acc 2026-10-21 | no | https://www.playstack.com/news/balatro-5-million-copies-sold/ | 27, 74 | 1109 | "over 5 million units sold" |
| N07 | Nintendo, "Mario Kart World Direct revs up new details" | 2025-04-17; acc 2026-10-21 | no | https://www.nintendo.com/us/whatsnew/mario-kart-world-direct-revs-up-new-details-on-the-biggest-mario-kart-ever-coming-to-nintendo-switch-2-at-launch/ | 27 (range only) | 1117 | "an interconnected world where you can drive virtually anywhere" |
| N08 | Nintendo, Consolidated Financial Highlights, three months ended 2025-06-30 | 2025-08-01; acc 2026-10-21 | no | https://www.nintendo.co.jp/ir/pdf/2025/250801e.pdf | 27 (range only) | 1125 | "sales of 5.63 million units, including units bundled with the hardware" |
| N09 | Arcane site, "Watch, Play, Experience: Celebrating Arcane Season 2 Across The Globe" | 2024-10-10; acc 2026-10-21 | no | https://www.arcane.com/en-us/news/announcements/watch-play-experience-heres-how-were-celebrating-arcane-season-2-across-the-globe/ | 27 (range only) | 1133 | "Event access ranges from ticketed to free" |
| MP-OWN | The paper's editorial method (MP:13) and "Studio operating design, 21 October 2026" (MP:45) | 2026-10-21; the paper's own synthesis, not an external study; no register entry | n/a | - | 13, 45, 68-70, 81 | - | - |

Register ids shared by one URL (S09 with P09) are not cited in lines 1-115. Register ids not cited in lines 1-115 are not resolved here (for example D18-D20, P03-P05, P10, P13-P19, S02, S06-S16, S19-S22, N10-N12).

## 9. Claims for the fact-check

Priority: P1 = Roblox discovery facts; click-through, PTR, qPTR and lift numbers; ad costs; platform rules and limits (sizes, counts, dates). P2 = other platform facts (including non-Roblox platforms). P3 = case results. Fact-check against the source at the id, not against the paper. "Post-cutoff" = source dated after 2026-06-01; "live-read" = undated live page, re-read it. Rows for rules 7-15 check only what lines 1-115 state; their details lie outside this note.

| ID | Claim (paraphrase) | MP | Pri | Src | Src date | Post-cutoff | Why it matters |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FC-01 | Since 2026-10-19 a game needs at least one custom (non-default) thumbnail to qualify for homepage-recommendation impressions; Continue unaffected for prior players; it is a gate, not a promise | 17, 49, 60 | P1 | D01 | 2026-10-19 | yes | Two days before the paper's cutoff; may have been revised since; headline launch-checklist item |
| FC-02 | RFY evaluation widened from 7 to 28 days (Day 1, Days 2-7, Days 8-28); PTR and first-play bounce replaced qualified PTR as ranking signals; scoped to organic RFY users | 19, 51, 61 | P1 | D02 | 2026-06-15 | yes | Core of the diagnosis model; scope limit must be checked |
| FC-03 | D03 priority signals: PTR, first-play bounce, play days per user, playtime per user; next tier: intentional co-play days, qualified sessions, spend days, Robux per user; per-user averages, not totals | 53 | P1 | D03 | undated, acc 2026-10-21 | live-read | Signal list feeds the agent's measurement plan |
| FC-04 | Bounce buckets: under 60 s and 61-180 s; counted playtime capped at 60 minutes per user / game / day | 53 | P1 | D03 | undated, acc 2026-10-21 | live-read | Exact numbers; a change would break diagnosis advice |
| FC-05 | D03: retrieval then ranking; ads, search, friends, teleports, notifications, external sources do not directly count as RFY cohort engagement; benchmarks are comparison aids, not inputs | 53 | P1 | D03 | undated, acc 2026-10-21 | live-read | Basis for "advertised growth is a hypothesis" (DI-20) |
| FC-06 | D03: misleading, reward-led or too-similar metadata can reduce exposure; semantic search supports natural-language intent | 53 | P1 | D03 | undated, acc 2026-10-21 | live-read | Limits what a title or description may promise |
| FC-07 | Top Playing Now: real-time CCU-based Charts sort, released globally on mobile, tablet, desktop, web | 57 | P1 | D04 | 2025-03-05; terminology 2025-04-29 | no | Defines what chart screenshots mean |
| FC-08 | Roblox naming advice: recognizable names; avoid frequent renaming and repeated words; one or two well-placed emojis; repeated words may cause demotion | 66 | P1 | D05 | undated, acc 2026-10-21 | live-read | Title and emoji limits; check the exact emoji wording |
| FC-09 | Icon: square, at least 512×512; preview at 150×150 suggested; one icon per locale; moderated | 85, 100 | P1 | D06 | undated, acc 2026-10-21 | live-read | Size and count limits |
| FC-10 | Thumbnail: 1920×1080, 16:9 | 87 | P1 | D07 | undated, acc 2026-10-21 | live-read | Asset spec for the art pipeline |
| FC-11 | Home personalization: 2-5 active variants, under 3 MB; a single image does not personalize (register quote backs only "2 or more") | 87, 101 | P1 | D07 | undated, acc 2026-10-21 | live-read | Upper bound 5 and the scope of 3 MB are not in the register quote |
| FC-12 | Gallery allows up to ten images / videos | 87 | P1 | D07 | undated, acc 2026-10-21 | live-read | Count limit |
| FC-13 | Thumbnail qPTR = qualified Home-recommendation plays / Home-recommendation impressions | 87 | P1 | D07 | undated, acc 2026-10-21 | live-read | Metric definition that must be quoted exactly |
| FC-14 | Native videos: 3 free uploads per month; policy rejections use up quota; Xbox, PlayStation, VR unsupported | 87 | P1 | D07 | undated, acc 2026-10-21 | live-read | Count and platform limits |
| FC-15 | Native preview content rules: representative gameplay; no external footage, narration, voice-chat conversations or lyrical music; sparse factual overlays allowed | 87 | P1 | D07 | undated, acc 2026-10-21 | live-read | Separates native previews from social trailers (rule 5) |
| FC-16 | Personalization is a multi-armed bandit, not fixed A/B; traffic starts spread, shifts toward stronger assets per audience, keeps exploration | 23, 89 | P1 | D08 | 2024-11-13; update 2025-02-13 | no | Prevents wrong "A/B test" claims |
| FC-17 | Launch guidance: under 1,000 DAU may lack meaningful results (a warning, not a hard requirement) | 89 | P1 | D08 | 2024-11-13; update 2025-02-13 | no | Number and hedge both matter |
| FC-18 | Launch test: +8.5% average qPTR lift, some +50% (platform-reported) | 89 | P1 | D08 | 2024-11-13; update 2025-02-13 | no | Lift numbers; check "average" and "some" |
| FC-19 | Staff advice: avoid restarting within 7 days; keep multiple distinct concepts; change on substantial content updates | 91, 102 | P1 | D09 | 2025-02-13 | no | Cadence limit, easily over-read |
| FC-20 | Staff snapshot: over 8,000 adopting experiences; +12% average relative qPTR lift; some +56% | 91 | P1 | D09 | 2025-02-13 | no | Lift numbers; "relative" matters |
| FC-21 | Thumbnail personalization still reports qPTR while broader analytics move to all-play PTR; alignment in progress; docs still say qPTR | 93, 103 | P1 | D10 | 2026-07-20 | yes | Metric naming; migration status may have changed by October |
| FC-22 | YouTube embeds on game pages scheduled for removal from 2026-09-30; new additions disabled since November 2025 | 107, 114 | P1 | D11 | 2026-09-18 | yes | Date has passed; confirm it happened as stated |
| FC-23 | Replacement path: free direct video upload in Creator Hub, Places, selected place, Videos, then approval | 107 | P1 | D11 | 2026-09-18 | yes | Exact menu path |
| FC-24 | Gameplay videos fully rolled out in Home RFY; advice to show actual current gameplay in the opening seconds | 109 | P1 | D12 | 2026-08-31 | yes | Roblox's own creative guidance |
| FC-25 | Video lifts (RFY, video present): Superstar Baseball +30% plays / +31% playtime; Notoriety +41% / +39%; window 2026-06-07 to 2026-06-26; directional, no sample sizes | 109, 115 | P1 | D12 | 2026-08-31 | yes | Lift numbers; never quote as forecast |
| FC-26 | Video annotations added to Acquisition, Engagement and Retention (reply 2026-09-01); deeper video analytics still to come then | 109 | P2 | D12 | 2026-09-01 | yes | Status may have moved since |
| FC-27 | A Roblox recording change on 2026-10-12 must be annotated before reading acquisition trends (what changed is not described in lines 1-115) | 41 | P1 | D16 | 2026-10-12 | yes | Trend breaks; nature of the change unknown here |
| FC-28 | Experience events: a maximum of 10 ongoing or upcoming events (register quote; rule 11 states no number) | 37 | P1 | D13 | undated, acc 2026-10-21 | live-read | Limit used for the sending-ceiling rule |
| FC-29 | Off-platform event featuring: event submitted at least 14 days before start (register quote; rule 11 states no number) | 37 | P1 | D14 | 2025-12-10 | no | Lead-time limit |
| FC-30 | Experience notifications: delivery is not guaranteed | 37 | P1 | D15 | undated, acc 2026-10-21 | live-read | Basis for "ceiling is not a cadence" |
| FC-31 | Ads Manager: current accounting and audience windows differ from old manual-bidding tutorials; no manual bid needed (P02); payment method fixed after publish (P01) | 33 | P1 | P01, P02 | acc 2026-10-21; 2025-04-09 | live-read (P01) | Ad cost and bidding rules; the "windows" detail is outside this part |
| FC-32 | Ad eligibility depends on format; under-13 exposure, under-18 personalization, rewarded video differ; ads may not be personalized for users under 18 | 35 | P1 | P11, P12 | 2026-06-17 update; 2026-10-09 | partly (P11); yes (P12) | Ad policy and age rules |
| FC-33 | Discord integration does not override Roblox's ban on tracking users across third-party platforms; users can deauthorize | 39 | P1 | S17, S18 | 2026-05-28 (updated 06-02); 2026-06-02 | partly (S17); yes (S18) | Privacy / platform rule |
| FC-34 | YouTube specifies no minimum posting cadence for Shorts to perform well | 29 | P2 | S01 | undated, acc 2026-10-21 | live-read | Cadence advice; see X-22 |
| FC-35 | Report-definition sources: S03 no minimum watch time requirement (change effective 2025-03-31); S04 public view-count standard applies globally (2026-08-17, rollout 2026-08-27); S05 reach built from engaged views and watch time; D17 Acquisition definition | 43 | P2 | S03, S04, S05, D17 | see section 8 | S04 yes; others live-read | Rule 14 denominators; details outside this part |
| FC-36 | Disclosure rules: FTC guide (2023 revision), YouTube paid-promotion controls (2026-09-03) and label steps, TikTok content-disclosure setting | 31 | P2 | P06-P09 | 2023; 2026-09-03; undated | P07 yes | Rule 8 creator-quote contents; details outside this part |
| FC-37 | SpongeBob Tower Defense: top 15 by Robux spent after 35 days, nearly 125 million visits, 40-minute average session (Wonder Works). The register quote for C01 is about thumbnail personalization; confirm the page also holds these figures | 72, 80 | P3 | C01 | 2025-03-17 | no | Case numbers; source pairing unconfirmed (X-10) |
| FC-38 | Balatro: explained via familiar gameplay combination and Joker-driven progression (N05); more than five million units sold (N06) | 74 | P3 | N05, N06 | undated; 2025-01-21 | no | Non-Roblox case; claim-to-source pairing by order (X-18) |
| FC-39 | Splitting Point CEO credited thumbnail personalization; over one billion plays | 97 | P3 | C01 | 2025-03-17 | no | Case number; testimonial only |
| FC-40 | Case sources cited only as ranges in rules 3 and 6 (C02-C06, N01-N04, N07-N09): the paper's lines 1-115 state no result from them | 21, 27 | P3 | C02-C06; N01-N04, N07-N09 | see section 8 | C06 unknown | Do not quote results from these ids using this note |

## 10. Contradictions and limits

### 10.1 Limits the paper itself states

| ID | MP | Limit | Handling for skills |
| --- | --- | --- | --- |
| X-01 | 11 | VERIFIED does not mean the author audited Roblox's algorithm, ran a campaign or tested an account. It means documented. | Write "Roblox documents..." not "Roblox's algorithm does...". |
| X-02 | 13 | A platform-reported randomized study stays platform-reported when its method is incomplete. A case shows a mechanism, not expected return elsewhere. | Label lift numbers "platform-reported" every time. |
| X-03 | 49 | The custom-thumbnail rule is an eligibility gate, not a promise of impressions. | Never write "a custom thumbnail brings recommendations". |
| X-04 | 51, 53 | D02 signals apply to organically acquired RFY users, not the whole game. Other sources (ads, search, friends, teleports, notifications, external) can help entry but do not directly feed the RFY cohort. Benchmarks are not direct inputs. | Evaluate RFY on its own cohort. |
| X-05 | 87, 101 | "Under 3 MB" is written next to "2-5 active variants"; the paper does not say whether it is per image or for the set. The register quote for D07 backs "2 or more" only. | Re-read D07 before stating the size or the upper bound. |
| X-06 | 55 | No fixed launch-day seed, guaranteed post-update exploration, CCU unlock threshold or universal benchmark is established. | State as unknown. |
| X-07 | 107, 114 | Paper words the YouTube removal as "scheduled starting 2026-09-30"; by the cutoff the date had passed, and the part does not say it took effect. | Check D11 before telling the owner embeds are gone. |
| X-08 | 76, 79 | No causal optimum for title word count, character count, emoji count or update-tag uplift. Allowed length is not an optimum. A rename not controlled is observational. | Give no title-length target. |
| X-09 | 49, 107 | Inside VERIFIED paragraphs, trailing advice (truthful 16:9 asset; "linking is not equivalent to a native preview") is the paper's own advice under the paragraph tag. | Treat as PROC. |
| X-10 | 72, 97 | C01 is cited for both SpongeBob Tower Defense figures (MP:72) and the Splitting Point testimonial (MP:97); the C01 register quote concerns thumbnail personalization only. SpongeBob figures are licensed-game outcomes with no title effect or retention cohort. | Re-read C01 for both claims; never use SpongeBob as title evidence. |
| X-11 | 89, 91 | Launch (+8.5%, some +50%) and later snapshot (+12% relative, over 8,000 experiences, some +56%) differ because they are different reported snapshots, not a universal uplift. The 7-day advice is not statistical sufficiency. | Never average, merge or forecast from these. |
| X-12 | 93 | PTR and qPTR are different fields; the July 2026 reply shows a transition, not a finished migration, and not every creator's October UI. | Copy the field name, tooltip and cohort verbatim. |
| X-13 | 95 | Higher raw qPTR is not a randomized causal effect (adaptive allocation); icon swaps and gallery reordering are not tested by Home personalization. The "three concepts" idea is a production choice, not an optimum. | Say "observed", not "caused". |
| X-14 | 97 | The testimonial supplies no exposure, no CTR / qPTR comparison, no retention attribution; one billion is not unique people. | Do not use as an uplift estimate. |
| X-15 | 109 | Video lifts: directional reported tests, no sample sizes, no confidence intervals, not reproducible from public text, not forecast multipliers. Pertain to RFY plays / playtime when video was present. | Never quote as expected lift. |
| X-16 | 111 | Do not claim every visitor sees the video, or that it plays in every placement. A badge listing is not evidence of retention. | Avoid "players will see". |
| X-17 | 7 | The research is not authorization to publish, contact creators, buy ads or commit contractually. The owner decides. | Keep every external step behind owner approval. |

### 10.2 Gaps and tensions found by the extractor (not stated by the paper)

| ID | MP | Item | Handling for skills |
| --- | --- | --- | --- |
| X-18 | 74 | Balatro: the sources are listed at the end of the paragraph ("N05, ...; N06, 2025-01-21"). Pairing N05 with the explanation and N06 with the unit count is my reading by order. | Verify when quoting. |
| X-19 | 51, 87, 93 | PTR is never spelled out in lines 1-115. "Qualified play-through rate" (MP:51) and qPTR (MP:87) suggest PTR = play-through rate; the paper defines only qPTR. | Do not define PTR beyond what the live source says. |
| X-20 | 17, 49, 87 | The 16:9 format is attached to D01 in MP:49 but defined by D07 in MP:87. | Cite D07 for sizes. |
| X-21 | 29, 31-43 | Rules 7-15 appear in the rule list only; their body text is outside lines 1-115. The register quote for a rule is not always proof of the rule text (for example P01/P02 quotes cover payment lock and bidding, while rule 9 speaks of accounting and audience windows; D16's quote does not describe the 2026-10-12 change). | Do not build a skill statement from rule lines 29-45 alone. |
| X-22 | 29 | Rule 7 (no minimum cadence) must stay narrow. The register elsewhere lists S21 (MP:1053-1059), whose register quote stresses a consistent, sustainable release schedule; S21 is not cited in lines 1-115. | Quote rule 7 as "no minimum", not "cadence does not matter". |
| X-23 | 21, 27 | Rules 3 and 6 cite whole ranges (C01-C06, N01-N09). Within lines 1-115 only C01, N05 and N06 carry a stated result. | Do not attribute results to the other ids from this note. |
| X-24 | 97 | "A dusty trip" is written in lower case in the paper; the game's name is not confirmed. | Check the exact title before naming it. |
| X-25 | 109 | PG-08 (2026-09-01 reply) sits in an EXPERIENCE-tagged sentence chain that starts with the lifts; it is a status note, not a lift. | Check whether deeper video analytics now exist. |
| X-26 | 53, 85, 87 | Several rules come from undated live docs (D03, D05, D06, D07) read on 2026-10-21; they may have changed since. | Re-read before any hard number reaches an owner. |
| X-27 | 11, 531 | Official hosting does not upgrade vendor or company outcome reports: they stay EXPERIENCE. | Keep tags from the section 5 and 6 rows. |

### 10.3 What the paper says it did not do (MP:7, 11, 13)

| ID | MP | Not done or unknown |
| --- | --- | --- |
| X-28 | 11 | Did not independently audit Roblox's algorithm, run a campaign or test an account. |
| X-29 | 7 | Does not authorize publishing, creator outreach, ad spend or contract commitments. |
| X-30 | 13 | OPINION rows are original synthesis; cited sources do not prove they work. |
| X-31 | 76 | No controlled study of title length, emoji use or rename effects exists in the paper. |
| X-32 | 55, 62 | No verified guaranteed ranking threshold; no paid-ranking guarantee. |

## 11. Line coverage (check C1)

Every line from 1 to 115 that holds text is covered by at least one row. Lines not turned into lesson rows, and why:

| MP | Content | Reason |
| --- | --- | --- |
| 9 | Heading "How to read the evidence" | heading only; its content is line 11 (EM-4 to EM-6) |
| 15 | Heading "Fifteen rules" | heading only |
| 47 | Heading "1 How Roblox discovery works in October 2026" | heading only |
| 64 | Heading "2 Titles that communicate a playable fantasy" | heading only |
| 83 | Heading "3 Icons thumbnails and native personalization" | heading only |
| 105 | Heading "4 The game page and native gameplay preview" | heading only |
| 59, 78, 99, 113 | Table header row "Rule / Number / Evidence mark / Source and date" | header only; data rows are in N-01 to N-12 |

Line-to-row map: 1, 3, 5 EM-1; 7 EM-2, EM-3; 11 EM-4 to EM-6; 13 EM-7 to EM-10; 17-45 RU-01 to RU-15; 49 DI-01 to DI-03; 51 DI-04 to DI-06; 53 DI-07 to DI-17; 55 DI-18 to DI-20; 57 DI-21 to DI-23; 60-62 N-01 to N-03; 66 TI-01 to TI-03; 68 TI-04 to TI-06; 70 TI-07, TI-08; 72 TI-09, TI-10; 74 TI-11 to TI-13; 76 TI-14 to TI-16; 79-81 N-04 to N-06; 85 IM-01, IM-02; 87 IM-03 to IM-09; 89 IM-10 to IM-13; 91 IM-14 to IM-16; 93 IM-17, IM-18; 95 IM-19 to IM-22; 97 IM-23, IM-24; 100-103 N-07 to N-10; 107 PG-01 to PG-03; 109 PG-04 to PG-08; 111 PG-09 to PG-12; 114-115 N-11, N-12. Line 115 is the last row of the part; line 117 (section 5, short videos) is outside it.
