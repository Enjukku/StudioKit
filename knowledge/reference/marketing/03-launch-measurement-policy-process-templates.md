---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: "J012-T03, Roblox_Marketing_Agent_Research_2026.txt lines 264-527"
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-21

# Marketing agent paper part 3: launch planning and non-Roblox cases, measurement, policy and rights, release gate, 13-step process, AI failure patterns, six operational templates, do-not list, open questions (lines 264-527)

Paraphrased notes. The paper (MP) stays outside git. Every row cites `MP:<line>`. Evidence sections are paraphrased. The six templates (section 6) are the owner's own text and are restated closely, as tables. Nothing here is fact-checked yet: claims are the paper's, listed in section 11 for the fact-check pass. The paper's research cutoff is 2026-10-21. Many platform facts are dated after 2026-06-01 and may be newer than a model's own knowledge: recheck them live (section 10 flags them).

## 0. How to read

| Key | Meaning |
| --- | --- |
| MP:n | line n of `Roblox_Marketing_Agent_Research_2026.txt`. One paragraph = one line. Source register = MP:529-1164 (only cited entries resolved here, section 10). |
| Tag | The paper's own tag, copied exactly. VERIFIED = an official rule, documented product behavior or directly documented measurement. It does not mean the author audited Roblox's algorithm, ran a campaign or tested an account (MP:11). EXPERIENCE = a developer, publisher, platform or vendor's reported outcome or interpretation (MP:11). OPINION = a proposed studio procedure or a reasoned application, not established causality (MP:11). |
| Mixed paragraphs | Many paragraphs open with VERIFIED or EXPERIENCE and end with an OPINION sentence. Rows are split on the paper's inline marks. When a sentence has no mark of its own, the Tag cell says "unmarked" and gives the paragraph mark. A VERIFIED paragraph may hold an unmarked advice sentence: treat that sentence as the paper's advice (MP:13). |
| Editorial method (MP:13) | A source's concrete rule and its commercial-success claim can carry different marks. A randomized study reported by a platform stays platform-reported when its method is not available. A case can show a mechanism without showing expected return for another game. Every OPINION is original synthesis as of 2026-10-21; its cited source explains the constraint or example, it does not prove the recommendation works. |
| Register rule (MP:531, 11) | Company and vendor outcome reports remain EXPERIENCE even when the host page is official. Undated living docs are dated by access (2026-10-21), never given an invented publication date. |
| Authority (MP:7, 398) | The owner is creative director and decision-maker. The agent proposes creative work and measurement plans. The paper grants no permission to publish, contact creators, buy advertising, make contractual commitments, spend, or collect player information. Central recommendation (MP:7): optimize the whole promise-to-play journey, not isolated impressions, views or clicks. |
| STD | Source label for rows with no external source: "Studio operating design, 21 October 2026" (MP:392-394, 398) or "OPINION, editorial method" (MP:13). Not an external study. |
| Src | The paper's source id, resolved in section 10 with date, URL and a short quote. "live" = undated living doc accessed 2026-10-21. |
| Cutoff flag | post-cutoff = the source is dated after 2026-06-01. live = undated, wording may change, recheck. pre-cutoff = dated 2026-06-01 or earlier. |
| Row IDs | Hyphenated. LA launch and non-Roblox cases, ME measurement, PO policy/ethics/rights, RG release gate, PR process step, AF AI failure pattern, TP template field or item (TP-TITLE, TP-THUMB, TP-BRIEF, TP-VIDEO, TP-LAUNCH, TP-REPORT), DN do-not, OQ open question, N number, FC claim to check, X contradiction or limit. Number rows "N-nn" are not the paper's source ids "N01-N12" (Squad Busters, Mario Kart, Arcane, Steam). |
| Rule of use | A VERIFIED row is a fact-check target, not a current fact. An OPINION row is a studio procedure: a skill must label it as such and never present it as a Roblox or platform rule. No row grants permission to spend, publish or contact anyone. |
| Terms not expanded here | PTR, qPTR, RFY, CPTV, CPP, CCU, DAU, DevEx, LaunchData, bounce, PolicyService. The paper does not define them in lines 264-527. Do not expand them from outside memory in a skill. Take the live dashboard or doc definition (see ME-18, X-24). |

## 1. Launch planning and non-Roblox cases (MP:264-287)

"Paper's limit" is the paper's own caveat, kept next to the claim.

| ID | MP | Lesson (paraphrase) | Paper's limit | Tag | Src, date |
| --- | --- | --- | --- | --- | --- |
| LA-01 | 266 | A launch is a coordinated product state, not a posting date. Marketing starts when the designer can demonstrate the hook. It works with the trend scout on audience language without copying protected expression. It gets the art director's visual references before generating campaign material. The analyst defines what can be measured before promotion starts. The owner decides whether the build and the campaign are ready together. | - | OPINION | STD |
| LA-02 | 268 | Grow a Garden (Jandel's account): the partnership began at about 500 CCU and 10,000-20,000 DAU, then weekly updates followed. His approximate recollection: roughly 100,000 CCU within two weeks and one million in about a month. He also reported 12 million TikTok followers. | Retrospective, approximate recollection. | EXPERIENCE | C02, interview 2025-09-07, updated 2025-09-08 |
| LA-03 | 268 | Read LA-02 as an exceptional survivor case, not a controlled cadence study and not a TikTok-to-player funnel. The first numbers count concurrent or daily players, not retained acquisition attributable to a post. | The paper's own limit on LA-02. | OPINION | C02 (motive), STD |
| LA-04 | 270 | Gabby's Dollhouse Official (The Gang's report): 7M+ visits in its first 45 days. The movie activation across several games: 71M+ sessions, 24M+ unique players, 9.3M+ in-game trailer views, 15M+ hours played. Combined impact includes 28M+ YouTube views. The game also served as a set for DreamWorks video production. | Company-reported; "+" means "more than". | EXPERIENCE | C03, undated, acc 2026-10-21 |
| LA-05 | 270 | Borrow the idea of filmable real gameplay plus coordinated audience access. The counts and phases in LA-04 are different measures and not one conversion funnel. Licensed IP and a movie campaign limit transfer to an unknown original game. | The paper's own limit on LA-04. | OPINION | C03 (motive), STD |
| LA-06 | 274 | Squad Busters (Supercell, non-Roblox) launched with a celebrity ensemble and creator counterparts to explain its squad premise. | - | VERIFIED | N01, 2024-05-29 |
| LA-07 | 274 | Supercell reported 40 million preregistrations, then more than US$100 million gross revenue in the first seven months of 2024. | The paper's bracket lists N01, N02, N03 without saying which holds the revenue figure (see FC-40). | EXPERIENCE | N01 (2024-05-29), N02 (2025-02-11) |
| LA-08 | 274 | The team later announced the end of active development, after it could not solve durable core problems. | Unmarked sentence inside the EXPERIENCE paragraph. MP:285 calls N03 a "VERIFIED announcement". | unmarked (paragraph mark EXPERIENCE; MP:285 says VERIFIED announcement) | N03, 2025-10-30 |
| LA-09 | 274 | Awareness, early revenue and lasting product success are three different outcomes. Borrow the single intelligible premise, not the celebrity budget or the preregistration target. | - | OPINION | N01-N03 (motive), STD |
| LA-10 | 276 | Mario Kart World Direct recap (Nintendo, non-Roblox): first introduced the interconnected world, then showed what it means for game modes. | - | VERIFIED | N07, 2025-04-17 |
| LA-11 | 276 | Nintendo reported 5.63 million units for April-June 2025, including hardware-bundled copies. | Includes bundles. | EXPERIENCE | N08, 2025-08-01 |
| LA-12 | 276 | The transferable craft is progressive demonstration: difference, then action, then consequence. The sales figure is not the Direct's conversion rate and not a Roblox demand benchmark. | - | OPINION | N07, N08 (motive), STD |
| LA-13 | 278 | Riot's Arcane season-two calendar coordinated screenings, themed physical experiences and fan gatherings across regions. The published calendar shows campaign structure only: not incremental League acquisition and not campaign ROI. | Limit sits in the same sentence pair. | VERIFIED | N09, 2024-10-10 |
| LA-14 | 278 | A small team can coordinate an original character, place and visual vocabulary across the assets it owns, without borrowing Riot's protected designs or global production scale. | - | OPINION | N09 (motive), STD |
| LA-15 | 280 | Steam Next Fest (non-Roblox) has platform-specific requirements: a released demo, categories and tags, preview checks. Press coverage is not guaranteed. | - | VERIFIED | N11, live |
| LA-16 | 280 | Transfer the advance preparation and the playable demonstration. Do not transfer Steam's festival mechanics or wishlists into Roblox. | - | OPINION | N11 (motive), STD |
| LA-17 | 282 | A cinematic awareness ad and a gameplay-first evaluation asset do not contradict each other: they answer different questions. Make destination-specific assets around the same truthful promise. | - | OPINION | STD |
| LA-18 | 282 | The later timeline (TP-LAUNCH) covers four weeks before and four weeks after launch, with decision gates, and without invented daily posting or spending targets. | - | OPINION | STD |

## 2. Measurement and analyst interpretation (MP:289-312)

| ID | MP | Lesson (paraphrase) | Paper's limit | Tag | Src, date |
| --- | --- | --- | --- | --- | --- |
| ME-01 | 291 | Roblox changed how it records impressions, clicks and plays for Home, Search and Charts, so fewer are lost when apps close or crash. Effective the same day. | - | VERIFIED | D16, 2026-10-12 |
| ME-02 | 291 | After the change, counts can rise while PTR dips slightly, because more impressions are recovered than plays. Historical data is unchanged. | - | VERIFIED | D16, 2026-10-12 |
| ME-03 | 291 | Roblox describes the change as measurement infrastructure, not a change to RFY recommendations, with minimal expected effect on relative ranking or benchmarks. | Roblox's description, not an audit. | VERIFIED | D16, 2026-10-12 |
| ME-04 | 291 | Mark 2026-10-12 in every campaign review that spans it. A before/after rise across that date does not prove a new title or thumbnail worked. | - | OPINION | D16 (motive), STD |
| ME-05 | 293 | Acquisition separates new from returning users. Sources named: Home recommendations, Continue, Search, Charts, sponsored/search/portal ads, teleports, and unattributed "Other". | - | VERIFIED | D17, live (acc 2026-10-21) |
| ME-06 | 293 | New-user conversion counts new users who played after an impression. | - | VERIFIED | D17, live |
| ME-07 | 293 | D7 retention here means a return on the eighth day after the end of the first session. | Definition is specific to this dashboard. | VERIFIED | D17, live |
| ME-08 | 293 | Seven-day playtime = cumulative playtime divided by new users in that cohort. | - | VERIFIED | D17, live |
| ME-09 | 293 | Thirty-day payer conversion and revenue per user need their full observation windows. Revenue excludes subscriptions, engagement payouts and immersive ads. | - | VERIFIED | D17, live |
| ME-10 | 293 | A four-day campaign cannot yet show its mature D7 or 30-day value. Report immature cohorts as pending. Do not mix ad and organic populations. | Four days is the paper's example length. | OPINION | D17 (motive), STD |
| ME-11 | 295 | Share links are tracked campaign links. The docs say there is no limit on links per game. | - | VERIFIED | D18, live |
| ME-12 | 295 | Creating links for a group needs the Manage share links permission and the group account. Custom LaunchData is optional. | The paper's wording "group creation" is short; read as creating links for a group-owned game (see X-27). | VERIFIED | D18, live |
| ME-13 | 295 | Use a separate link for each creator, channel and creative, and keep its campaign key. | - | OPINION | D18 (motive), STD |
| ME-14 | 295 | A share link gives channel attribution, not proof of incremental lift: some visitors might have joined anyway. Never infer off-platform revenue from video views alone. | - | OPINION | D18 (motive), STD |
| ME-15 | 297 | Open Cloud added four APIs: Analytics Query, Events/Updates, Experiments, Thumbnail Personalization. Analytics queries run asynchronously and need polling. | Announcement date 2026-08-24. | VERIFIED | D19, 2026-08-24 |
| ME-16 | 297 | The thumbnail endpoint family is labeled Experimental. Creating a configuration deactivates the previous one and starts its own statistics. Updating an active configuration swaps its images and keeps its identifier and existing statistics. | - | VERIFIED | D20, live |
| ME-17 | 297 | The agent must log create and update as two distinct operations, keep configuration history, and verify the real approved state. Do not call every new API stable. Do not promise native MCP availability because an announcement said it was coming. | - | OPINION | D19, D20 (motive), STD |
| ME-18 | 299 | Minimum weekly report, fields: build, creative and configuration IDs; acquisition source; cohort start and maturity; impressions plus precisely defined PTR/qPTR; bounce; play days and playtime windows; creator-share-link results; notification opt-outs; known reporting breaks; concurrent changes; one proposed next decision with what would disconfirm it. | Basis named by the paper: D02, D03, D07, D16-D20. Full template: TP-REPORT. | OPINION | D02, D03, D07, D16, D17, D18, D19, D20 (basis), STD |
| ME-19 | 299 | Show absolute counts beside rates. With low volume, adaptive allocation or missing breakdowns, say "inconclusive", never "winner". Keep qualitative comprehension findings apart from measured conversion. | - | OPINION | STD |
| ME-20 | 301 | YouTube Shorts public views changed on 2025-03-31 to count starts and replays, with no minimum watch duration. | - | VERIFIED | S03, change effective 2025-03-31 |
| ME-21 | 301 | TeamYouTube announced on 2026-08-17 that the first-frame public-view standard would extend globally to all formats on 24 August, and confirmed the rollout on 27 August. The original engaged-view metric remains available. | The paper writes "24 August" and "27 August" without a year; the register gives 2026-08-17 and 2026-08-27. | VERIFIED | S04, 2026-08-17, rollout 2026-08-27 |
| ME-22 | 303 | YouTube's current docs define average view duration from engaged views and their watch time, not all public starts. Stayed-to-watch reflects viewing past the first Shorts seconds. Thumbnail CTR concerns registered thumbnail impressions. These are different events with different denominators. | - | VERIFIED | S05, live |
| ME-23 | 305 | Every weekly report should hold: platform; format; organic, paid or creator distribution; date range; video duration; metric definition and version; public views; engaged views where available; unique reach where available; watched-versus-skipped or retention curve; average view duration; average percentage viewed; shares and saves; profile or destination clicks; attributable game arrivals; new-player quality; spend; production cost. | Full template: TP-REPORT. | OPINION (2026-10-21) | STD |
| ME-24 | 305 | Mark unavailable fields "unavailable". Never divide incompatible metrics to invent a conversion rate. Show creator fee, production labor and ad spend separately before computing a fully loaded acquisition cost. Causal incrementality needs a suitable experiment, not a matching timestamp. | - | OPINION (2026-10-21) | STD |
| ME-25 | 307 | Treat patterns as hypotheses. Poor initial hold: inspect the opening. Good hold but weak destination action: inspect game fit and the call to action. More clicks but poor in-game retention: suspect promise mismatch or onboarding friction. These are investigation routes, not diagnoses proven by correlation. | - | OPINION (2026-10-21) | STD |
| ME-26 | 307 | Do not buy views or manufacture engagement to improve a report. | - | OPINION (2026-10-21) | STD |

## 3. Rules, ethics, younger audiences, ad integrations, rights (MP:314-330, 350, 352-355)

MP:316 (heading) says advertising is not the same as monetization. MP:326 (heading) says trend inspiration is not rights clearance.

| ID | MP | Lesson (paraphrase) | Paper's limit | Tag | Src, date |
| --- | --- | --- | --- | --- | --- |
| PO-01 | 318 | Since the policy effective 2026-05-04 (update 2026-06-17), age-appropriate integrations, Homepage formats and Billboards are available to all age groups, including under-13 users. | - | VERIFIED | P11, policy 2026-05-04, update 2026-06-17 |
| PO-02 | 318 | Ads may not be personalized for users under 18. | - | VERIFIED | P12, updated 2026-10-09 |
| PO-03 | 318 | Rewarded Video remains 13+. Rewards must be predetermined, opt-in and delivered promptly. Watching may not be a progression gate. | - | VERIFIED | P12, 2026-10-09 |
| PO-04 | 318 | Ads for under-18 audiences may not directly urge children to buy, nor pressure adults to buy for them. | - | VERIFIED | P12, 2026-10-09 |
| PO-05 | 318 | Required: clear disclosure, truthful claims, non-infringing assets. Prohibited: misleading free-Robux offers and fake system controls. | - | VERIFIED | P12, 2026-10-09 |
| PO-06 | 318 | The latest P12 revision changes Portal restrictions and several restricted product categories. Do not apply a blanket old 13+ rule to every format. | The "do not apply" clause is advice inside a VERIFIED paragraph. | VERIFIED (last clause unmarked advice) | P12, 2026-10-09 |
| PO-07 | 320 | Paid branded content and specified off-platform promotion, including promotion of the studio's own merchandise, can count as ad integrations. Obligations: register campaigns, submit assets, build eligibility and disclosure controls. | - | VERIFIED | P13, live |
| PO-08 | 320 | `AdService:GetCampaignEligibilityAsync` decides whether campaign assets may be shown. Region and age restrictions can apply. | - | VERIFIED | P13, live |
| PO-09 | 320 | One rejected asset can invalidate the whole campaign. Adding assets to an active campaign limits serving to 18+ while they are in review. | - | VERIFIED | P13, live |
| PO-10 | 320 | Whole-game ads need a persistent bottom-right HUD label and an "Ad" disclosure in the thumbnail's bottom-left. Roblox recommends submitting at least five days ahead. | "recommends" = a recommendation, not a stated rule. | VERIFIED | P13, live |
| PO-11 | 322 | Integration revenue-share pricing starts 2027-01-01. It is not a general 2026 game-acquisition charge. | Platform integration charge from 2027-01-01. | VERIFIED | P11 (announcement 2026-06-17); P13 (live) |
| PO-12 | 322 | Published CPTV for the first 28 days, in USD: $1.50 U.S.; $0.75 Tier 1; $0.20 Tier 2; $0.05 Tier 3. Later visits: $0.10 per thousand. | Platform integration charge from 2027-01-01, not an influencer fee. The paper does not define CPTV or "per thousand" here (see X-24, X-26). | VERIFIED | P11 (2026-06-17); P13 (live) |
| PO-13 | 322 | A qualified visit is a session that engages with branded assets, not necessarily a unique person. Influencer arrangements outside the integration are excluded. | - | VERIFIED | P11, P13 |
| PO-14 | 322 | Recheck the 2027 schedule before contracting. These are platform integration charges, not a recommended influencer fee and not a Sponsored Tile CPP. | - | OPINION | STD |
| PO-15 | 324 | Paid-random-item rules apply to purchases made with Robux or Robux-acquired currency. They require the actual numerical odds and eligibility handling. | - | VERIFIED | P14, live |
| PO-16 | 324 | Roblox requires PolicyService integration for restricted features and recommends avoiding urgent or pushy messages to minors. | "recommends" for the messaging part. | VERIFIED | P15, live |
| PO-17 | 324 | Keep three separate approval checks: (1) ad exposure and disclosure, (2) paid-random-item purchase rules, (3) earnings and DevEx eligibility. Passing one does not show the others pass. | - | OPINION | STD |
| PO-18 | 328 | U.S. Copyright Office guidance: copyright does not protect a game idea, title or play method as such; expressive artwork or text can be protected. | US only. | VERIFIED | P17, live |
| PO-19 | 328 | USPTO guidance: trademark confusion depends on how similar the marks are and how related the goods or services are, not only on exact spelling. | US only. | VERIFIED | P18, live |
| PO-20 | 328 | A trending meme, franchise character, song or competitor thumbnail is not automatically licensed for commercial advertising. Keep evidence of asset ownership, licenses and scope. Send ambiguous adaptations to qualified legal review. Changing a few pixels, or using an AI-made imitation, is not clearance. | - | OPINION | P17, P18 (motive), STD |
| PO-21 | 330 | Roblox lists misleading or mismatched metadata among discoverability concerns. | - | VERIFIED | P19, live |
| PO-22 | 330 | Make title, icon, thumbnail, trailer and first playable session promise the same achievable thing. Keep a proof sheet: each marketed feature, the build where it works, where players meet it, the authentic capture. Do not market a future feature as live. Do not imply official sponsorship without permission. | - | OPINION | P19 (motive), STD |
| PO-23 | 350 | Steam's base capsule rules exclude review scores, awards and promotional calls to action. This is a Steam rule, not a Roblox icon specification. | The register quote shows only the review-score rule (see FC-31). | VERIFIED | N12, live |
| PO-24 | 350 | Recheck the real destination's rules. Do not import a familiar platform's restrictions wholesale. | - | OPINION | N12 (motive), STD |

## 4. Small-studio release gate (MP:332-348)

The owner approves all seven items before publication or spend. Basis named by the paper: P01-P19 (synthesis). The paper does not specify evidence per item.

| ID | MP | Gate item (paraphrase) | See | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| RG-00 | 334 | Before any publication or spend, the owner approves the seven items below. | AF-08, DN-11 | OPINION (2026-10-21) | P01-P19 (synthesis), STD |
| RG-01 | 336 | The right product, format, objective and audience are named, and jurisdiction is reviewed. No assumption rests on a blanket age rule. | PO-02, PO-06 | OPINION | STD |
| RG-02 | 338 | The promise is checked against the build. A rights register exists. Disclosures are accessible. | PO-20, PO-22 | OPINION | STD |
| RG-03 | 340 | Creator deliverables, pay, rights, adult representation where needed, and who monitors are all agreed. | TP-REPORT-10 | OPINION | STD |
| RG-04 | 342 | The campaign has a total loss ceiling, a duration, a currency and a funding source. Auto-reload is explicitly off unless separately authorized. | DN-06, DN-11 | OPINION | STD |
| RG-05 | 344 | For integrations: registration, moderation and runtime eligibility are in place, with fallback behavior for ineligible users. | PO-07 to PO-10 | OPINION | STD |
| RG-06 | 346 | Tracking identity, cohort maturity and net-receipts accounting are set. Labels separate forecast, attributed and incremental results. | ME-10, ME-14 | OPINION | STD |
| RG-07 | 348 | A pause owner and an escalation route exist for spending anomalies, moderation failure, misleading content or player harm. | TP-REPORT-00 | OPINION | STD |

## 5. The 13-step process, AI failure patterns, campaign record (MP:357-394)

The workflow is proposed, not an industry standard and not permission to act externally. Its output is an approval package whose claims trace to the build, sources and measurements (MP:359).

| ID | MP | Step (paraphrase) | With | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| PR-00 | 359 | The process is a proposed studio workflow. Its output is an approval package traceable to the build, sources and measurements. It does not authorize external actions. | - | OPINION | STD |
| PR-01 | 361 | Define the audience and fantasy with the designer: what the player does, what makes it distinctive, what payoff the current build shows. Record features not yet live and keep them out of present-tense promises. | designer | OPINION | STD |
| PR-02 | 363 | Ask the trend scout for audience interests and language. Separate a rising subject from a right to use a franchise, character, song, logo or likeness. Record source, date and uncertainty of each trend claim. | trend scout | OPINION | STD |
| PR-03 | 365 | Ask the analyst to define the decision: acquisition surface, outcome, denominator, eligible cohort, observation window. Define in advance what counts as misleading traffic or poor-fit acquisition. | analyst | OPINION | STD |
| PR-04 | 367 | Build the message hierarchy: plain-language promise, supporting proof, title candidates, first-sentence page description, and a reason to play now that is really available. Reject interchangeable genre slogans. | - | OPINION | STD |
| PR-05 | 369 | Get the art lock from the art director. Use approved characters, silhouettes, palette, environment and logo. Write separate icon and thumbnail briefs. Keep one game identity across variants. | art director | OPINION | STD |
| PR-06 | 371 | Make and revise images through the studio's ChatGPT image pipeline; outputs are candidates. Check against approved references: hands, object count, typography, character identity, geometry, scale, fake interfaces, invented rewards. Never label generated key art as gameplay capture. | art pipeline | OPINION | STD |
| PR-07 | 373 | Capture proof in the real build. Record version, scene, permissions and any staging. Prepare a native Roblox preview under its own rules, and separate social edits for each platform. An entertaining edit must still be true to the game. | - | OPINION | STD |
| PR-08 | 375 | Assemble the page and channel kit: approved title, description, icon, thumbnails, native preview, short-video plans, update announcement, event proposal, creator brief. Check each destination's current requirements; one export does not fit all. | - | OPINION | STD |
| PR-09 | 377 | Prepare policy and rights review: commercial disclosure requirements, audience restrictions, licenses, campaign eligibility. Send unclear rights, minor-contracting or jurisdiction questions to qualified review instead of guessing. | qualified reviewer | OPINION | STD |
| PR-10 | 379 | Present the owner's decision package: recommended assets, rejected alternatives and why, budget options without commitment, measurement limits, a rollback path for the marketing assets. Publication, outreach and spending need real authorization. | owner | OPINION | STD |
| PR-11 | 381 | After authorization, check the live state against the approved set: asset IDs, text, timestamps, account configuration, links. An accepted upload is not proof of approval, visibility or delivery to every eligible player. | owner (authorized) | OPINION | STD |
| PR-12 | 383 | Read results with the analyst. Keep raw counts and exact metric labels. Segment paid and organic. Wait for cohort maturity. Report inconclusive results as inconclusive. Tell experimental evidence apart from adaptive allocation, before/after comparisons and vendor testimonials. | analyst | OPINION | STD |
| PR-13 | 385 | Propose the next bounded revision. Diagnose which failed: comprehension, audience fit, destination friction, game quality, measurement or policy. More impressions do not fix a misleading promise or an unplayable first session. | - | OPINION | STD |
| PR-14 | 389 | Keep one campaign record: approved brief, current policy checks, source register, asset versions, rights, capture provenance, measurement dictionary, owner decisions, live timestamps, results, next action. It beats keeping only the winning prompt because another agent can then explain what was promised, what changed and why. | - | OPINION | STD |

AI failure patterns and their rejection tests (MP:387, OPINION):

| ID | MP | Failure pattern | Rejection test | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| AF-01 | 387 | Generic titles | Unfamiliar-reader explanation check | OPINION | STD |
| AF-02 | 387 | Cluttered images | Small-size preview and text-hidden preview | OPINION | STD |
| AF-03 | 387 | Unsupported spectacle | Build-proof check | OPINION | STD |
| AF-04 | 387 | Wrong tone | Audience and art-direction review | OPINION | STD |
| AF-05 | 387 | Fake statistics | Source verification | OPINION | STD |
| AF-06 | 387 | A polished imitation without a license | Rights review | OPINION | STD |
| AF-07 | 387 | A confident "winner" without a valid denominator | Analyst review | OPINION | STD |
| AF-08 | 387 | A campaign plan that silently authorizes spending | Owner-approval gate | OPINION | STD |

## 6. Operational templates (MP:396-481)

All six are OPINION, "Studio operating design, 21 October 2026" (MP:398). They are proposed work products, not platform requirements and not empirically optimal schedules. The owner approves creative direction, budgets, publication and external commitments. The marketing agent prepares evidence and drafts. These tables restate the owner's own text closely. Tag on every row: OPINION. Src on every row: STD.

### 6.1 Title pass or fail checklist (MP:400-414)

| ID | MP | Pass or fail item | Required evidence |
| --- | --- | --- | --- |
| TP-TITLE-00 | 402 | Rule of use: apply every item to the proposed title and its paired creative. A failed item blocks release of that candidate until it is corrected or the owner explicitly resolves it. A pass means "fit for evaluation", not proven commercial effectiveness. | - |
| TP-TITLE-01 | 405 | The title names a recognizable fantasy or action, not only a genre label. | A plain-language description of what the player does in the released build. |
| TP-TITLE-02 | 406 | Every promise is playable in the advertised version. | A capture or build reference showing the promised action. |
| TP-TITLE-03 | 407 | Curiosity is resolved in gameplay, not by a misleading visual. | A short explanation of the reveal and when a new player reaches it. |
| TP-TITLE-04 | 408 | The title and the image communicate the same game. | A comparison of title, icon, thumbnail and first playable objective. |
| TP-TITLE-05 | 409 | Distinctiveness does not depend on copying another game's name. | A similarity review and a documented independent naming rationale. |
| TP-TITLE-06 | 410 | Any brand, character or licensed term has cleared rights. | Permission or license scope, territory and expiry, recorded by the owner. |
| TP-TITLE-07 | 411 | The title is readable on the actual destination surface. | Captures of the candidate in the current mobile and desktop interface. |
| TP-TITLE-08 | 412 | Any update tag names a real current change. | A release identifier, and the removal or refresh condition. |
| TP-TITLE-09 | 413 | Localization keeps the meaning and creates no unintended claim. | A review of the complete title and paired image in each intended language. |
| TP-TITLE-10 | 414 | The proposed test has an identifiable unit and outcome. | The analyst's specification, the eligibility window, and unchanged comparison conditions. |

### 6.2 Thumbnail and icon pass or fail checklist (MP:416-432)

| ID | MP | Pass or fail item | Required evidence |
| --- | --- | --- | --- |
| TP-THUMB-00 | 418 | Rule of use: evaluate thumbnail and icon separately. A composition that survives a wide crop need not survive a square crop. Inspect on the actual current product surface, not only the high-resolution export. | - |
| TP-THUMB-01 | 421 | The central action is identifiable at display size. | A small-size preview beside the intended title. |
| TP-THUMB-02 | 422 | The subject stays understandable without reading tiny text. | A text-hidden preview. |
| TP-THUMB-03 | 423 | The focal subject and the background do not merge. | A grayscale and low-contrast inspection. |
| TP-THUMB-04 | 424 | The promised object, reward or event exists in the game. | A build capture and an item or feature reference. |
| TP-THUMB-05 | 425 | The emotional expression supports the real player fantasy. | Art director approval of tone and audience fit. |
| TP-THUMB-06 | 426 | Interface imagery does not pose as a Roblox reward, purchase or system control. | A policy and interface review. |
| TP-THUMB-07 | 427 | No number, price, reward or status label is invented by image generation. | A manual comparison with the approved brief and the game configuration. |
| TP-THUMB-08 | 428 | Crop, overlays and safe areas keep the subject on each target surface. | Separate destination previews. |
| TP-THUMB-09 | 429 | Protected characters, logos, fonts, music references and likenesses are cleared. | A rights record, not an assumption based on a popular trend. |
| TP-THUMB-10 | 430 | The image is distinct from current and competitor creatives. | A comparison sheet with candidate identifiers. |
| TP-THUMB-11 | 431 | Each candidate tests one coherent creative hypothesis. | One written explanation of the intended change in player expectation. |
| TP-THUMB-12 | 432 | The asset is traceable and reversible. | The original brief, the generation or edit history, owner approval, and the previous live asset. |

### 6.3 Thumbnail and icon image brief (MP:434-444)

Copy these fields into the studio art pipeline. The marketing agent owns the message, the art director owns visual coherence, the owner approves the selected concept (MP:436). Do not ask the image model to invent an unapproved feature just to raise click appeal (MP:436). Each field takes the content shown in brackets in the paper.

| ID | MP | Field | Content the field must hold |
| --- | --- | --- | --- |
| TP-BRIEF-00 | 436 | Rule of use | Fields go into the art pipeline. Owner roles as above. No invented features for click appeal. |
| TP-BRIEF-01 | 438 | Game and build | Name, version, release state. |
| TP-BRIEF-02 | 438 | Destination | Icon or thumbnail; the current required format; exact export dimensions verified in the destination. |
| TP-BRIEF-03 | 438 | Audience and locale | Intended audience, language, policy constraints. |
| TP-BRIEF-04 | 438 | Player fantasy | The experience the player will actually have. |
| TP-BRIEF-05 | 438 | Single message | What the viewer should understand before reading a description. |
| TP-BRIEF-06 | 440 | Truth reference | Gameplay captures, object references, approved art. |
| TP-BRIEF-07 | 440 | Hero subject | Identity, silhouette, expression, pose, scale. |
| TP-BRIEF-08 | 440 | Playable action | What is happening and why it matters. |
| TP-BRIEF-09 | 440 | Environment | Enough context to identify the setting without hiding the action. |
| TP-BRIEF-10 | 440 | Composition | Focal hierarchy, camera, foreground and background. |
| TP-BRIEF-11 | 440 | Contrast and palette | Approved art direction, and separation from the surrounding interface. |
| TP-BRIEF-12 | 442 | Text | None, or exact approved wording that is added and checked in the art pipeline. |
| TP-BRIEF-13 | 442 | Exclusions | Unreleased rewards, fake controls, fake currency, misleading scale, unauthorized characters or logos, excessive detail. |
| TP-BRIEF-14 | 442 | Crop variants | Destination-specific previews. |
| TP-BRIEF-15 | 442 | Accessibility checks | Small-size readability, contrast, reliance on color alone. |
| TP-BRIEF-16 | 442 | Rights references | Source and permission record for each external asset. |
| TP-BRIEF-17 | 444 | Test hypothesis | Which expectation changes, and why that may improve qualified acquisition. |
| TP-BRIEF-18 | 444 | Comparison | The current candidate and the stable conditions. |
| TP-BRIEF-19 | 444 | Primary outcome | Exact metric name and denominator. |
| TP-BRIEF-20 | 444 | Guardrails | Post-acquisition engagement, audience fit, policy. |
| TP-BRIEF-21 | 444 | Approval | Art director recommendation, owner decision. |
| TP-BRIEF-22 | 444 | Archive | Brief ID, asset ID, version, publish date, reason for replacement. |

### 6.4 Short video plan (MP:446-454)

The "first 3 seconds" is a requested planning field, not a universal performance threshold. Duration, pacing, posting time and frequency stay hypotheses unless a cited platform rule sets a limit or this game's own data shows a result (MP:448).

| ID | MP | Field | Content the field must hold |
| --- | --- | --- | --- |
| TP-VIDEO-00 | 448 | Rule of use | As the paragraph above. |
| TP-VIDEO-01 | 450 | Hook | One truthful tension, surprise, achievement or social interaction. |
| TP-VIDEO-02 | 450 | Audience promise | Why the intended viewer would want to play, not only watch. |
| TP-VIDEO-03 | 450 | Platform and placement | Shorts, TikTok, Reels or another verified destination. |
| TP-VIDEO-04 | 450 | Objective | Awareness, qualified visits, plays, return visits or creator interest. |
| TP-VIDEO-05 | 450 | Build and capture provenance | Version; real play or clearly disclosed staging; permissions. |
| TP-VIDEO-06 | 452 | First 3 seconds | The exact opening image, action, on-screen words and audio cue. |
| TP-VIDEO-07 | 452 | Shot list | For each shot: time range, gameplay action, camera, information added, transition, caption. |
| TP-VIDEO-08 | 452 | Payoff | The actual game event that answers the opening. |
| TP-VIDEO-09 | 452 | Captions | Exact wording, readable placement, localization and accessibility review. |
| TP-VIDEO-10 | 452 | Sound | Dialogue, game audio, music rights, sound-off interpretation. |
| TP-VIDEO-11 | 452 | Length | Candidate duration and the reason for it, not an invented optimum. |
| TP-VIDEO-12 | 454 | Call to action | Accurate game identity and the permitted route to play. |
| TP-VIDEO-13 | 454 | Destination | Approved landing surface and tracking method. |
| TP-VIDEO-14 | 454 | Disclosure | Sponsor or material-connection label when it applies. |
| TP-VIDEO-15 | 454 | Thumbnail or cover | An honest, representative frame. |
| TP-VIDEO-16 | 454 | Variants | One coherent creative difference per comparison that is to be interpreted. |
| TP-VIDEO-17 | 454 | Measurement | Platform-specific view definition; watch or engaged-view metric; attribution window; plays; downstream quality. |
| TP-VIDEO-18 | 454 | Stop or revise | Owner-approved conditions based on policy, negative feedback, cost or acquisition quality. |

### 6.5 Launch timeline, four weeks before to four weeks after (MP:456-469)

This is the user-requested planning window. It is not evidence that a game needs this much preparation, that a launch will get recommendation traffic, or that every listed channel should be used. Advance a stage only when its required decision is ready. A delayed game must not be marketed with a false launch promise (MP:458).

| ID | MP | Window | Marketing work product | Owner and analyst decision |
| --- | --- | --- | --- | --- |
| TP-LAUNCH-00 | 458 | Rule of use | As the paragraph above. | - |
| TP-LAUNCH-01 | 461 | Four weeks before | Hook statement, playable proof, audience hypothesis, rights inventory, source and policy check. | Approve the fantasy being sold; name what is still unproven. |
| TP-LAUNCH-02 | 462 | Three weeks before | Title candidates, separate icon and thumbnail concepts, page draft, capture plan. | Select coherent candidates; reject promises the build does not hold. |
| TP-LAUNCH-03 | 463 | Two weeks before | Capture real gameplay, draft short videos, creator shortlist and offer terms, moderation plan. | Decide whether any external campaign is appropriate; approve no spend implicitly. |
| TP-LAUNCH-04 | 464 | One week before | Approved launch kit, verified destinations, event or announcement drafts, measurement dictionary. | Confirm instrumentation, attribution limits, support readiness and release contingency. |
| TP-LAUNCH-05 | 465 | Launch day | Publish only approved assets through authorized workflows; record exact versions and times. | Compare acquisition quality and technical health against the agreed evaluation plan. |
| TP-LAUNCH-06 | 466 | First week after | Channel and cohort report, player misunderstanding review, creative corrections. | Fix broken promises or onboarding mismatch before treating more impressions as the answer. |
| TP-LAUNCH-07 | 467 | Second week after | An interpretable creative test where the available traffic supports one; creator and community review. | Separate content performance from game retention; approve any changed budget. |
| TP-LAUNCH-08 | 468 | Third week after | Update kit tied to a real playable change; returning-player message. | Check that the update gives a new reason to return and can be understood without hype. |
| TP-LAUNCH-09 | 469 | Fourth week after | Consolidated acquisition and retention assessment, rights and asset archive, next-cycle proposal. | Continue, revise or stop channels based on measured quality, uncertainty and opportunity cost. |

### 6.6 Weekly marketing report for the analyst and owner (MP:471-481)

Weekly is the requested reporting cadence, not a proven optimal publishing or testing frequency. Urgent policy, spend-control or misleading-creative issues go out at once through the studio's agreed approval process, not in the weekly report (MP:473).

| ID | MP | Field | Content the field must hold |
| --- | --- | --- | --- |
| TP-REPORT-00 | 473 | Rule of use | As the paragraph above. |
| TP-REPORT-01 | 475 | Report period and data cut | Start, end, timezone, extraction time. |
| TP-REPORT-02 | 475 | Live build and creative versions | Version IDs and change timestamps. |
| TP-REPORT-03 | 475 | Decision requested | The specific choice, owner and deadline. |
| TP-REPORT-04 | 475 | Executive result | What changed, how strong the evidence is, what is still uncertain. |
| TP-REPORT-05 | 477 | Metric dictionary | Exact dashboard label; numerator; denominator; eligibility; surface; paid or organic status; cohort; attribution window; reporting delay. |
| TP-REPORT-06 | 477 | Acquisition table | Impressions; clicks if defined; plays; qualified plays if defined; unique users where available; spend and currency. |
| TP-REPORT-07 | 477 | Quality table | Post-acquisition retention with cohort definition; engagement; bounce if defined; satisfaction; technical health. Rule: do not turn unavailable values into zero. |
| TP-REPORT-08 | 479 | Creative test record | Hypothesis; candidates; allocation method; exposure period; eligible population; primary outcome; guardrails; observed counts; uncertainty; decision. |
| TP-REPORT-09 | 479 | Cross-channel record | Platform-native views and engaged views; outbound activity if measurable; Roblox acquisition source; the attribution limitation. |
| TP-REPORT-10 | 479 | Creator record | Deliverables; disclosure compliance; cost; tracking method; measured outcomes; unmeasured spillover. |
| TP-REPORT-11 | 481 | Interpretation | Causal evidence, association, self-report, or insufficient data. |
| TP-REPORT-12 | 481 | Changes in measurement | Dashboard definition, attribution or recording changes that break comparability. |
| TP-REPORT-13 | 481 | Cost assessment | Cost per defined outcome; revenue definition; attribution uncertainty. Rule: no invented return on ad spend. |
| TP-REPORT-14 | 481 | Next action | Keep, revise, pause or investigate; rationale; owner approval; reversibility. |
| TP-REPORT-15 | 481 | Missing evidence | What to instrument; what access is needed; what observation would change the recommendation. |

## 7. Do not do (MP:483-505)

| ID | MP | Prohibition (paraphrase) | Tag | Src, date |
| --- | --- | --- | --- | --- |
| DN-01 | 485 | Do not assume a default-only thumbnail qualifies a game for Home recommendation impressions. | VERIFIED | D01, 2026-10-19 |
| DN-02 | 487 | Do not call adaptive thumbnail allocation, sequential social posts or a before/after rename a randomized A/B experiment. | OPINION | D08 (2024-11-13, update 2025-02-13); S10 (2024-12-10, update 2025-06-26); STD 2026-10-21 |
| DN-03 | 489 | Do not call a high observed CTR a success while hiding poor post-click player quality. | OPINION | STD, 2026-10-21 |
| DN-04 | 491 | Do not reuse a voiced social trailer as a native Roblox preview without checking the native content rules. | VERIFIED | D07, live |
| DN-05 | 493 | Do not hide sponsorship. Do not assume a platform label discharges every disclosure duty. | VERIFIED | P06 (2023 guidance); P07 (2026-09-03) |
| DN-06 | 495 | Do not invent creator fees, ad-credit conversion rates, cost-per-player targets or a guaranteed profitable budget. Get current quotes and account terms. | OPINION | Research limits and studio procedure, 2026-10-21 |
| DN-07 | 497 | Do not personalize ads to under-18 users. Do not make rewarded video a mandatory progression gate. | VERIFIED | P12, 2026-10-09 |
| DN-08 | 499 | Do not treat a licensed studio case as permission to use the same character, franchise, music or logo. | OPINION | P17, P18 (live); studio rights procedure, 2026-10-21 |
| DN-09 | 501 | Do not export Roblox presence or user information across platforms just because a third-party vendor offers a connection. | VERIFIED | S18, 2026-06-02 |
| DN-10 | 503 | Do not use views, sessions and unique players as interchangeable. Do not count projected activation figures as completed results. | OPINION | C03, C04, C05 (live); studio reporting procedure, 2026-10-21 |
| DN-11 | 505 | Do not quietly turn a draft launch plan into ad spend, creator outreach, publication or a contract. | OPINION | Owner approval workflow, 2026-10-21 |

## 8. Disagreements and open questions (MP:507-527)

Two disagreements first (MP:509, 511), then ten evidence gaps (MP:513-525). The paper says gaps become investigation plans, never invented benchmarks (MP:513). Rows OQ-03 to OQ-12 are table rows that carry the section mark OPINION (MP:513).

| ID | MP | What the paper says is unresolved | What to do (paper) | Tag | Src, date |
| --- | --- | --- | --- | --- | --- |
| OQ-01 | 509 | Current thumbnail analytics still document qPTR, while the June RFY ranking announcement uses PTR and bounce. A July staff reply acknowledged the mismatch. | Keep both labels and their definitions until the live dashboard or export confirms a migration. Do not relabel old rates under a new name. | VERIFIED (the mismatch); OPINION (the handling) | D02 (2026-06-15); D07 (live); D10 (2026-07-20) |
| OQ-02 | 511 | Current event docs give a seven-day featuring submission lead time. The original pilot said 14 days. | Check the live form and account behavior. Use a conservative contingency and do not present it as a platform rule. | VERIFIED (the two figures); OPINION (the handling) | D13 (live); D14 (2025-12-10) |
| OQ-03 | 511 | Ads docs describe even creative delivery. An older announcement described engagement-based optimization. | Check live account behavior. | VERIFIED (the two descriptions); OPINION (the handling) | P01 (live); P10 (2025-08-05) |
| OQ-04 | 516 | Best title length or wording: controlled Roblox uplift by word count, emoji or update tag is unknown. | Run comprehension checks first. Then judge carefully logged package changes with source-specific cohorts and stated causal limits. | OPINION | STD |
| OQ-05 | 517 | Winning icon composition: the universal effect of faces, emotion, contrast or a visual formula is unknown. | Test truthful alternatives at the real display size. Keep icon changes apart from thumbnail personalization. | OPINION | STD |
| OQ-06 | 518 | Best short-video length and cadence: no controlled 2026 Roblox-specific optimum across TikTok, Shorts and Reels. | Log candidate length, audience, opening, source and downstream quality. Do not generalize a small sample from one channel. | OPINION | STD |
| OQ-07 | 519 | Creator economics: no public rate card, and no stable conversion from followers or views to retained Roblox users. | Get campaign-specific quotes and aggregate audience evidence. Define attribution and rights before contracting. | OPINION | STD |
| OQ-08 | 520 | Incremental ad value: unknown whether attributed players and earnings would have come without the campaign. | Use a suitable holdout when one exists. Otherwise report attribution as attribution and list simultaneous changes. | OPINION | STD |
| OQ-09 | 521 | Native preview encoding limits: current authoritative duration, file-size and codec limits were not established. | Check the live upload interface before export and keep its current specification. Do not reuse an unverified old limit. | OPINION | STD |
| OQ-10 | 522 | Instagram metric definitions: some current Help definitions could not be verified reliably. | Read the account's current Insights definitions before computing cross-platform rates. | OPINION | STD |
| OQ-11 | 523 | Brand campaign transfer: unknown whether a licensed-IP or major-studio campaign predicts an original small game's result. | Treat the example as a mechanism. Test the studio's own audience and product. Do not copy protected expression. | OPINION | STD |
| OQ-12 | 524 | Low-traffic creative learning: unknown whether available exposure supports a meaningful comparison. | Ask the analyst to quantify uncertainty. Keep an inconclusive result rather than invent a winner. | OPINION | STD |
| OQ-13 | 525 | Current account eligibility: unknown whether a newly announced ad format or optimization is enabled for this game. | Verify the actual account before proposing a launch commitment or budget. | OPINION | STD |
| OQ-14 | 527 | Closing statement: the paper recommends an evidence-producing workflow, not a guarantee of discovery. A useful agent explains the promise, proves it is playable, separates live platform mechanics from announcements, and says when evidence does not justify a larger commitment. | - | OPINION | STD |

## 9. Number register (MP:264-527)

Part A holds the paper's four "Rule | Number | Evidence mark | Source and date" summary tables (MP:284-287, 309-312, 352-355, 391-394). Rule labels are lightly reworded; the Number, mark and source cells keep the paper's text. Part B holds every other number or date in the part, with scope and limit.

### 9.A Summary-table rows

| ID | MP | Rule (reworded) | Number | Evidence mark (paper) | Source and date (paper) |
| --- | --- | --- | --- | --- | --- |
| N-01 | 285 | Launch milestones are distinct outcomes | 40 million preregistrations; later development ended | EXPERIENCE and VERIFIED announcement | N01 29 May 2024; N03 30 Oct 2025 |
| N-02 | 286 | Keep the denominator behind sales | 5.63 million units includes bundles | EXPERIENCE | N08 1 Aug 2025 |
| N-03 | 287 | Use the requested planning window without calling it optimal | Four weeks before and four after | OPINION | User requested template; 21 Oct 2026 |
| N-04 | 310 | Mark the measurement discontinuity | 2026-10-12 | VERIFIED | D16 / 2026-10-12 |
| N-05 | 311 | Match cohort maturity | 7-day and 30-day metrics | VERIFIED | D17 / accessed 2026-10-21 |
| N-06 | 312 | API availability is not stability | Thumbnail endpoints Experimental | VERIFIED | D20 / accessed 2026-10-21 |
| N-07 | 353 | Tell exposure from personalization | Rewarded Video 13+; no under-18 personalization | VERIFIED | P12 9 Oct 2026 |
| N-08 | 354 | Future integration charges are not the current ad CPP | Published start 1 Jan 2027 | VERIFIED future schedule | P11 17 Jun 2026; P13 accessed 21 Oct 2026 |
| N-09 | 355 | Trends are not rights clearance | No automatic permission | OPINION informed by legal guidance | P17-P18 accessed 21 Oct 2026 |
| N-10 | 392 | Use a traceable approval package | No automatic spend or publication | OPINION | Studio operating design 21 Oct 2026 |
| N-11 | 393 | Keep generated key art apart from gameplay proof | Distinct asset provenance | OPINION | Studio operating design 21 Oct 2026 |
| N-12 | 394 | Reject unsupported certainty | Unknown remains unknown until measured | OPINION | Studio operating design 21 Oct 2026 |

### 9.B Other numbers and dates, with scope

| ID | Value | Scope (who, what it counts) | MP | Limit (paper) | Tag | Src, date |
| --- | --- | --- | --- | --- | --- | --- |
| N-13 | about 500 CCU; 10,000-20,000 DAU | Grow a Garden at the start of the partnership, Jandel's account | 268 | Concurrent or daily players, not retained acquisition attributable to a post | EXPERIENCE | C02, 2025-09-07 (upd 2025-09-08) |
| N-14 | roughly 100,000 CCU in two weeks; roughly 1 million in about a month | Grow a Garden, Jandel's approximate recollection | 268 | Retrospective; not a controlled cadence study | EXPERIENCE | C02 |
| N-15 | 12 million TikTok followers | Reported by Jandel | 268 | Not a TikTok-to-player funnel | EXPERIENCE | C02 |
| N-16 | weekly updates | Cadence reported after the partnership began | 268 | Not a controlled cadence study | EXPERIENCE | C02 |
| N-17 | 7M+ visits; first 45 days | Gabby's Dollhouse Official, The Gang's report | 270 | Licensed IP; different phase from N-18 | EXPERIENCE | C03, live |
| N-18 | 71M+ sessions; 24M+ unique players; 9.3M+ in-game trailer views; 15M+ hours played | Movie activation across several games, The Gang's report | 270 | Different counts and phases; not one funnel | EXPERIENCE | C03, live |
| N-19 | 28M+ YouTube views | Combined impact, The Gang's report | 270 | Same | EXPERIENCE | C03, live |
| N-20 | 40 million preregistrations | Squad Busters, as reported | 274 | Awareness is not lasting success | EXPERIENCE | N01, 2024-05-29 |
| N-21 | more than US$100 million gross revenue; first seven months in 2024 | Squad Busters, as reported | 274 | Source for this figure not named (FC-40) | EXPERIENCE | N01-N03 bracket; N02 (2025-02-11) |
| N-22 | 5.63 million units; April-June 2025 | Mario Kart World, Nintendo, includes hardware-bundled copies | 276 | Not the Direct's conversion rate; not a Roblox benchmark | EXPERIENCE | N08, 2025-08-01 |
| N-23 | 2026-10-12, effective that day | Roblox recording change for Home/Search/Charts impressions, clicks, plays; history unchanged | 291 | Annotate every review spanning it | VERIFIED | D16 |
| N-24 | eighth day after first session ended | D7 retention as D17 defines it | 293 | Dashboard-specific | VERIFIED | D17, live |
| N-25 | cumulative playtime / new users in cohort | Seven-day playtime as D17 defines it | 293 | - | VERIFIED | D17, live |
| N-26 | 30-day payer conversion and revenue/user; revenue excludes subscriptions, engagement payouts, immersive ads | D17 definitions | 293 | Need full 30-day windows | VERIFIED | D17, live |
| N-27 | four-day campaign | Paper's example of an immature cohort | 293 | Cannot show mature D7 or 30-day value | OPINION | D17 (motive), STD |
| N-28 | no limit on share links per game | Roblox share links | 295 | Channel attribution only, not incremental lift | VERIFIED | D18, live |
| N-29 | 2026-08-24 | Open Cloud added Analytics Query, Events/Updates, Experiments, Thumbnail Personalization APIs | 297 | Analytics queries are asynchronous | VERIFIED | D19, 2026-08-24 |
| N-30 | 2025-03-31 | YouTube Shorts public views start counting starts/replays, no minimum watch duration | 301 | - | VERIFIED | S03 |
| N-31 | 2026-08-17 announcement; 24 August extension to all formats; 27 August rollout confirmed (year omitted in paper) | YouTube first-frame public-view standard | 301 | Engaged-view metric remains available | VERIFIED | S04 |
| N-32 | 2026-05-04 effective; 2026-06-17 update | Roblox advertising policy P11 | 318 | - | VERIFIED | P11 |
| N-33 | under-13 | Age-appropriate integrations, Homepage formats, Billboards available to all age groups | 318 | - | VERIFIED | P11 |
| N-34 | under-18; updated 2026-10-09 | Ads may not be personalized | 318 | - | VERIFIED | P12 |
| N-35 | 13+ | Rewarded Video | 318 | Do not apply 13+ to every format | VERIFIED | P12 |
| N-36 | 18+ | Serving limit while new assets on an active campaign are reviewed | 320 | - | VERIFIED | P13, live |
| N-37 | at least five days ahead | Roblox's recommended submission lead for integration assets | 320 | A recommendation | VERIFIED | P13, live |
| N-38 | 2027-01-01 | Start of integration revenue-share pricing | 322 | Not a general 2026 acquisition charge | VERIFIED | P11 (2026-06-17); P13 |
| N-39 | first 28 days: US $1.50; Tier 1 $0.75; Tier 2 $0.20; Tier 3 $0.05 (USD) | Published CPTV for integrations | 322 | Platform integration charge, not an influencer fee or Sponsored Tile CPP | VERIFIED | P11; P13 |
| N-40 | $0.10 per thousand | CPTV for visits after the first 28 days | 322 | Same | VERIFIED | P11; P13 |
| N-41 | 2026-10-19 | Custom thumbnail required for Home recommendation eligibility | 485 | - | VERIFIED | D01 |
| N-42 | first 3 seconds | Short-video plan field | 448 | Planning field, not a performance threshold | OPINION | STD |
| N-43 | 7 days (current docs) vs 14 days (original pilot) | Featuring submission lead time for events | 511 | Verify the live form | VERIFIED | D13 (live); D14 (2025-12-10) |
| N-44 | June 2026 and July 2026 | RFY ranking announcement (PTR) and staff reply on the mismatch | 509 | Preserve both labels | VERIFIED | D02 (2026-06-15); D10 (2026-07-20) |
| N-45 | 2023; 2026-09-03; 2026-06-02 | FTC guidance P06; YouTube paid-partnership controls P07; Roblox privacy reminder S18 | 493, 501 | - | VERIFIED | P06; P07; S18 |
| N-46 | four weeks before and four after; weekly | Requested planning window and reporting cadence | 282, 458, 473 | Not optimal, not proven | OPINION | STD |
| N-47 | 13 steps; 7 gate items; 3 separate approval checks; 8 failure patterns | Counts of the paper's own lists (MP:324, 334-348, 359-385, 387) | 324, 334, 359, 387 | Structure only | OPINION | STD |

## 10. Source ids used in lines 264-527 (resolved from MP:529-1164)

Key quotes are the register's own, 15 words or fewer, attributed to the named source. P01-P19 are all listed because MP:334 cites the whole range; C04 because MP:503 cites C03-C05. "Used in" shows where the paper uses the source (row IDs) and the paper's mark. "acc" = accessed by the paper. A quote marked "shortened" is cut from a longer register quote to stay under 15 words.

| ID | Source (publisher, title) | Date and limits (register) | Cutoff flag | MP register | Used in (mark) | URL | Key quote (register) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| D01 | Roblox DevForum, "Homepage Recommendation Eligibility Now Requires a Custom Thumbnail" | 2026-10-19; acc 2026-10-21 | post-cutoff | 533-539 | DN-01 (VERIFIED) | https://devforum.roblox.com/t/homepage-recommendation-eligibility-now-requires-a-custom-thumbnail/4945086 | "Games with only a default thumbnail are not eligible for homepage recommendations." |
| D02 | Roblox DevForum, "Recommended For You Algorithm Improvements That Better Value Long-Term Retention" | 2026-06-15; acc 2026-10-21 | post-cutoff | 541-547 | ME-18 (basis), OQ-01 (VERIFIED) | https://devforum.roblox.com/t/recommended-for-you-algorithm-improvements-that-better-value-long-term-retention/4684575 | "We've updated the Recommended For You algorithm signals from 7 days to 28 days" |
| D03 | Roblox Creator Docs, "Discovery" | undated live; acc 2026-10-21 | live | 549-555 | ME-18 (basis) | https://create.roblox.com/docs/discovery | "Every signal reflects user behavior after they discover your game." |
| D07 | Roblox Creator Docs, "Thumbnails" | undated live; acc 2026-10-21 | live | 581-587 | ME-18 (basis), DN-04 (VERIFIED), OQ-01 (VERIFIED) | https://create.roblox.com/docs/production/publishing/thumbnails | "Thumbnail personalization only starts when you activate 2 or more thumbnails." |
| D08 | Roblox DevForum, "Live now: Personalize your thumbnails to attract more users" | 2024-11-13; update 2025-02-13; acc 2026-10-21 | pre-cutoff | 589-595 | DN-02 (OPINION) | https://devforum.roblox.com/t/live-now-personalize-your-thumbnails-to-attract-more-users/3257233 | "Personalization uses multi-arm bandit (instead of A/B testing)" |
| D10 | Roblox DevForum, "QPTR is displaying incorrectly/inaccurately", reply 6 | 2026-07-20; acc 2026-10-21 | post-cutoff | 605-611 | OQ-01 (VERIFIED) | https://devforum.roblox.com/t/qptr-is-displaying-incorrectlyinaccurately/4690988/6 | "the thumbnail personalization is not fully aligned with the algo now" |
| D13 | Roblox Creator Docs, "Experience events and updates" | undated live; acc 2026-10-21 | live | 629-635 | OQ-02 (VERIFIED) | https://create.roblox.com/docs/production/promotion/experience-events | "you can publish a maximum of 10 ongoing or upcoming events" |
| D14 | Roblox DevForum, "Introducing Off-Platform Featuring for Creator Events" | 2025-12-10; acc 2026-10-21 | pre-cutoff | 637-643 | OQ-02 (VERIFIED) | https://devforum.roblox.com/t/introducing-off-platform-featuring-for-creator-events/4142230 | "The event must be submitted at least 14 days prior to the event start date" |
| D16 | Roblox DevForum, "Improved Discovery Measurement in Creator Analytics" | 2026-10-12; acc 2026-10-21 | post-cutoff | 653-659 | ME-01 to ME-04, N-04 (VERIFIED) | https://devforum.roblox.com/t/improved-discovery-measurement-in-creator-analytics/4930122 | "Your historical data will not change." |
| D17 | Roblox Creator Docs, "Acquisition" | undated live; acc 2026-10-21 | live | 661-667 | ME-05 to ME-10, N-05 (VERIFIED) | https://create.roblox.com/docs/production/analytics/acquisition | "Acquisition measures where new and returning users are coming from and how well they convert." |
| D18 | Roblox Creator Docs, "Share links" | undated live; acc 2026-10-21 | live | 669-675 | ME-11 to ME-14 (VERIFIED) | https://create.roblox.com/docs/production/promotion/share-links | "There is no limit to how many share links you can create per game" |
| D19 | Roblox DevForum, "New OpenCloud APIs for Analytics, Events, Experiments, and Thumbnail Personalization" | 2026-08-24; acc 2026-10-21 | post-cutoff | 677-683 | ME-15, ME-17 (VERIFIED) | https://devforum.roblox.com/t/new-opencloud-apis-for-analytics-events-experiments-and-thumbnail-personalization/4828676/1 | "Analytics queries run asynchronously due to their size." |
| D20 | Roblox Creator Docs, "Thumbnail Personalization Open Cloud reference" | undated live; acc 2026-10-21 | live | 685-691 | ME-16, N-06 (VERIFIED) | https://create.roblox.com/docs/cloud/reference/features/thumbnail-personalization | "the new configuration starts its own statistics" |
| P01 | Roblox Creator Docs, "Ads Manager" | undated live; acc 2026-10-21 | live | 693-699 | OQ-03 (VERIFIED); within P01-P19 (RG-00) | https://create.roblox.com/docs/production/promotion/ads-manager | "The payment method cannot be changed after a campaign is published." |
| P02 | Roblox DevForum, "Leveling Up Ads Manager With New Features", staff reply 151 | 2025-04-09; acc 2026-10-21 | pre-cutoff | 701-707 | within P01-P19 (RG-00) | https://devforum.roblox.com/t/leveling-up-ads-manager-with-new-features/3587640/151 | "there's no need to set a manual bid" |
| P03 | Roblox DevForum, "Ads Manager Updates: Maximize Earnings, Attribution Updates, New Tile in Beta, Other Updates" | 2026-05-07; acc 2026-10-21 | pre-cutoff | 709-715 | within P01-P19 (RG-00) | https://devforum.roblox.com/t/ads-manager-updates-maximize-earnings-attribution-updates-new-tile-in-beta-other-updates/4623762/1 | "we have updated our attribution logic" |
| P04 | Roblox DevForum, "Roblox Kids and Select Global Launch: Upcoming Updates to Eligibility, Ads Manager, and Expedited Review" | 2026-06-16; acc 2026-10-21 | post-cutoff | 717-723 | within P01-P19 (RG-00) | https://devforum.roblox.com/t/roblox-kids-and-select-global-launch-upcoming-updates-to-eligibility-ads-manager-and-expedited-review/4685717 | "A new Engagement Objective beta in Creator Ads Manager" |
| P05 | Roblox DevForum, "Ads Manager RDC Recap: Earnings, ROAS Reporting, & Incrementality" | 2026-10-02; acc 2026-10-21 | post-cutoff | 725-731 | within P01-P19 (RG-00) | https://devforum.roblox.com/t/ads-manager-rdc-recap-earnings-roas-reporting-incrementality/4909790/1 | "All 21 campaigns brought incremental plays." |
| P06 | FTC, "FTC's Endorsement Guides: What People Are Asking" | 2023 revision; acc 2026-10-21 | pre-cutoff | 733-739 | DN-05 (VERIFIED) | https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking | "clearly and conspicuously disclosing a material connection rests with the influencer and the brand" (shortened) |
| P07 | YouTube Help blog, "Giving you tools to easily disclose paid partnerships with new controls & automated disclosures" | 2026-09-03; acc 2026-10-21 | post-cutoff | 741-747 | DN-05 (VERIFIED) | https://support.google.com/youtube/blog/458476782/giving-you-tools-to-easily-disclose-paid-partnerships-with-new-controls-automated-disclosures | "Granular age & geographic controls for branded content" |
| P08 | YouTube Help, "Add branded content restrictions & disclosure labels" | undated live; acc 2026-10-21 | live | 749-755 | within P01-P19 (RG-00) | https://support.google.com/youtube/answer/154235 | "selecting the paid promotion button in your video details" |
| P09 | TikTok Support, "Promoting a brand, product, or service" | undated live; acc 2026-10-21 | live | 757-763 | within P01-P19 (RG-00) | https://support.tiktok.com/en/business-and-creator/creator-and-business-accounts/promoting-a-brand-product-or-service | "you must turn on the content disclosure setting" |
| P10 | Roblox DevForum, "Ads Manager Updates: Acquire New Users, Continuous Campaigns and More" | 2025-08-05; acc 2026-10-21 | pre-cutoff | 765-771 | OQ-03 (VERIFIED) | https://devforum.roblox.com/t/ads-manager-updates-acquire-new-users-continuous-campaigns-and-more/3862159 | "Ad thumbnails will soon automatically optimize based on user engagement" |
| P11 | Roblox DevForum, "New Advertising Policies & Standards" | policy effective 2026-05-04; revenue-share update 2026-06-17; acc 2026-10-21 | mixed: policy pre-cutoff; update 2026-06-17 post-cutoff | 773-779 | PO-01, PO-11 to PO-13, N-08 (VERIFIED) | https://devforum.roblox.com/t/new-advertising-policies-standards/4527365/1 | "The rates for 2027 are as follows" |
| P12 | Roblox Help, "Advertising Standards" | updated 2026-10-09; acc 2026-10-21 | post-cutoff | 781-787 | PO-02 to PO-06, DN-07, N-07 (VERIFIED) | https://en.help.roblox.com/hc/en-us/articles/13722260778260-Advertising-Standards | "Ads may not be personalized for users under the age of 18." |
| P13 | Roblox Creator Docs, "Ad integrations" | undated live; acc 2026-10-21 | live | 789-795 | PO-07 to PO-13, N-08 (VERIFIED) | https://create.roblox.com/docs/production/promotion/ad-integrations | "Starting January 1, 2027" |
| P14 | Roblox Creator Docs, "Paid random items policy guidelines" | undated live; acc 2026-10-21 | live | 797-803 | PO-15 (VERIFIED) | https://create.roblox.com/docs/production/monetization/paid-random-items | "the actual numerical odds of what they may receive" |
| P15 | Roblox Help, "Promoting Items to Younger Audiences" | undated live; acc 2026-10-21 | live | 805-811 | PO-16 (VERIFIED) | https://en.help.roblox.com/hc/en-us/articles/47965190783892-Promoting-Items-to-Younger-Audiences | "Avoid using pushy or urgent messages when interacting with minors." |
| P16 | Roblox Help, "Developer Exchange - Help and Information Page" | undated live; acc 2026-10-21; rate effective dates 2025-09-05 and 2026-06-08 | live; rate date 2026-06-08 post-cutoff | 813-819 | within P01-P19 (RG-00); PO-17 names "DevEx eligibility" without an id | https://en.help.roblox.com/hc/en-us/articles/13061189551124-Developer-Exchange-Help-and-Information-Page | "This rate is effective as of June 8, 2026" |
| P17 | U.S. Copyright Office, "Games" | undated official guidance; acc 2026-10-21 | live | 821-827 | PO-18, N-09 (VERIFIED) | https://www.copyright.gov/register/tx-games.html | "The idea for a game is not protected by copyright." |
| P18 | USPTO, "Likelihood of confusion" | undated official guidance; acc 2026-10-21 | live | 829-835 | PO-19, N-09 (VERIFIED) | https://www.uspto.gov/trademarks/search/likelihood-confusion | "confusingly similar" |
| P19 | Roblox Creator Docs, "Discovery FAQ" | undated live; acc 2026-10-21 | live | 837-843 | PO-21 (VERIFIED) | https://create.roblox.com/docs/discovery-faq | "Misleading or mismatched metadata and content" |
| C02 | GamesBeat, "How Grow a Garden took off on Roblox", Janzen 'Jandel' Madsen interview | 2025-09-07; updated 2025-09-08; acc 2026-10-21 | pre-cutoff | 853-859 | LA-02, LA-03 (EXPERIENCE) | https://gamesbeat.com/janzen-madsen-interview/ | "We implemented a live service. We started weekly updates." |
| C03 | The Gang, "Gabby's Dollhouse Official on Roblox" case study | undated case study; acc 2026-10-21 | live | 861-867 | LA-04, LA-05, DN-10 (EXPERIENCE) | https://www.thegang.io/case-studies/gabbys-dollhouse-case-study | "DreamWorks could now film YouTube content directly inside the Roblox environment." |
| C04 | Medal, "Medal for Roblox Developers - Grow Your Game" (vendor page) | undated vendor page; acc 2026-10-21 | live | 869-875 | DN-10 (range C03-C05; OPINION) | https://medal.tv/developer/roblox | "Incentivize players to clip and post their best moments in your game" |
| C05 | Medal, "Medal x Sol's RNG - Partnership" (vendor page) | undated vendor page; acc 2026-10-21 | live | 877-883 | DN-10 (OPINION) | https://medal.tv/developer/roblox/solsrng | "Estimated growth with a single activation" |
| S03 | YouTube Help, "Get started creating YouTube Shorts" | undated; change effective 2025-03-31; acc 2026-10-21 | pre-cutoff (change) | 909-915 | ME-20, N-30 (VERIFIED) | https://support.google.com/youtube/answer/10059070?hl=en | "no minimum watch time requirement" |
| S04 | YouTube Community (TeamYouTube), "An update to how we count public views across YouTube" | 2026-08-17; rollout confirmed 2026-08-27; acc 2026-10-21 | post-cutoff | 917-923 | ME-21, N-31 (VERIFIED) | https://support.google.com/youtube/thread/433409976?hl=en | "This standard will now apply globally across all formats." |
| S05 | YouTube Help, "Understand your YouTube video reach" | undated; acc 2026-10-21 | live | 925-931 | ME-22 (VERIFIED) | https://support.google.com/youtube/answer/9314355?hl=en | "This is calculated from engaged views and their corresponding watch time." |
| S10 | Meta, "Test Content With Non-Followers Using Trial Reels" | 2024-12-10; updated 2025-06-26; acc 2026-10-21 | pre-cutoff | 965-971 | DN-02 (OPINION) | https://about.fb.com/news/2024/12/trial-reels-try-content-non-followers-first-see-what-perfoms-best/ | "Trial reels will be shown to non-followers first." |
| S18 | Roblox DevForum, "A Reminder About User Privacy and Third-Party Integrations" | 2026-06-02; acc 2026-10-21 | post-cutoff | 1029-1035 | DN-09 (VERIFIED) | https://devforum.roblox.com/t/a-reminder-about-user-privacy-and-third-party-integrations/4665118 | "Creators may not track Roblox users across third-party platforms or services" |
| N01 | Supercell-issued Squad Busters global-launch announcement (PR Newswire) | 2024-05-29; acc 2026-10-21 | pre-cutoff | 1069-1075 | LA-06, LA-07, N-01 | https://www.prnewswire.com/news-releases/chris-hemsworth-christina-ricci-ken-jeong-will-arnett-and-aulii-cravalho-squad-up-with-supercell-for-global-game-launch-302157916.html | "the game has achieved 40 million pre-registrations" |
| N02 | Supercell, "In for the Forever Game" | 2025-02-11; acc 2026-10-21 | pre-cutoff | 1077-1083 | LA-07 (bracket) | https://supercell.com/en/news/forever-game/ | "has not yet scaled up to the game team's (or Supercell's) aspirations" |
| N03 | Supercell, "Squad Busters Development is Ending, Final Update in December 2025" | 2025-10-30; acc 2026-10-21 | pre-cutoff | 1085-1091 | LA-08, N-01 | https://supercell.com/en/news/squad-development-ending/ | "we were not able to find a lasting solution to its core problems" |
| N07 | Nintendo, "Mario Kart World Direct revs up new details" | 2025-04-17; acc 2026-10-21 | pre-cutoff | 1117-1123 | LA-10 (VERIFIED) | https://www.nintendo.com/us/whatsnew/mario-kart-world-direct-revs-up-new-details-on-the-biggest-mario-kart-ever-coming-to-nintendo-switch-2-at-launch/ | "an interconnected world where you can drive virtually anywhere" |
| N08 | Nintendo, "Consolidated Financial Highlights, Three Months Ended June 30, 2025" | 2025-08-01; acc 2026-10-21 | pre-cutoff | 1125-1131 | LA-11, N-02 (EXPERIENCE) | https://www.nintendo.co.jp/ir/pdf/2025/250801e.pdf | "sales of 5.63 million units, including units bundled with the hardware" |
| N09 | Arcane, "Watch, Play, Experience: Celebrating Arcane Season 2 Across The Globe" | 2024-10-10; acc 2026-10-21 | pre-cutoff | 1133-1139 | LA-13 (VERIFIED) | https://www.arcane.com/en-us/news/announcements/watch-play-experience-heres-how-were-celebrating-arcane-season-2-across-the-globe/ | "Event access ranges from ticketed to free" |
| N11 | Steamworks, "Steam Next Fest" | undated; acc 2026-10-21 | live | 1149-1155 | LA-15 (VERIFIED) | https://partner.steamgames.com/doc/marketing/upcoming_events/nextfest | "Only games with released demos will be eligible to appear." |
| N12 | Steamworks, "Graphical Asset Rules" | undated; acc 2026-10-21 | live | 1157-1163 | PO-23 (VERIFIED) | https://partner.steamgames.com/doc/store/assets/rules | "No review scores of any kind, including Steam reviews or external news sources" |

The register intro (MP:531) says quotes are short anchors, not a substitute for reading the source. Several paper details are not visible in the one register quote (see X-17).

## 11. Claims for the fact-check

Fact-check against the source at the id, not against the paper. Priority: P1 = Roblox platform facts (highest harm if wrong: policy, money, measurement); P2 = non-Roblox platform rules and US guidance (YouTube, Steam, FTC, Meta, copyright, trademark); P3 = case results. "Flag" = cutoff flag from section 10.

| ID | Pri | Claim (paraphrase) | MP | Src | Src date | Flag | Why it matters |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FC-01 | P1 | Roblox changed recording of Home/Search/Charts impressions, clicks and plays on 2026-10-12 to reduce loss on app close or crash. Counts can rise while PTR dips slightly. History unchanged. Roblox calls it infrastructure, not an RFY change, with minimal ranking effect. | 291 | D16 | 2026-10-12 | post-cutoff | The "annotate 2026-10-12" rule (ME-04) and every before/after review rest on it. Check each sub-claim. |
| FC-02 | P1 | A custom thumbnail is required for Home recommendation eligibility. Effective 2026-10-19. A default-only thumbnail is not eligible. | 485 | D01 | 2026-10-19 | post-cutoff | Blocks the whole TP-THUMB flow and DN-01. Check the date and the exact scope ("homepage recommendations"). |
| FC-03 | P1 | D17 definitions: sources list (Home recommendations, Continue, Search, Charts, sponsored/search/portal ads, teleports, Other); new-user conversion = new users who played after an impression; D7 = return on the eighth day after first session ended; seven-day playtime = cumulative playtime / new users; 30-day payer conversion and revenue/user need 30-day windows; revenue excludes subscriptions, engagement payouts, immersive ads. | 293 | D17 | live | live | Wrong definition = wrong cohort maturity rules (N-05) and wrong report fields. |
| FC-04 | P1 | Share links: tracked campaign links; no limit per game; group creation needs Manage share links permission and the group account; custom LaunchData optional. | 295 | D18 | live | live | Basis for distinct link per creator (ME-13). Check what "group creation" means (X-27). |
| FC-05 | P1 | Open Cloud added Analytics Query, Events/Updates, Experiments and Thumbnail Personalization APIs; analytics queries are asynchronous and need polling. The paper also says an announcement said native MCP availability was "coming" (not a promise to rely on). | 297 | D19 | 2026-08-24 | post-cutoff | Agent tooling plan depends on which APIs exist. Check the MCP "coming" statement is in the post. |
| FC-06 | P1 | Thumbnail endpoints are labeled Experimental. Creating a configuration deactivates the previous one and starts new statistics. Updating an active configuration replaces images but keeps its identifier and statistics. | 297, 312 | D20 | live | live | Drives the two distinct logged operations (ME-17). Status label may change. |
| FC-07 | P1 | Age-appropriate integrations, Homepage formats and Billboards available to all age groups including under-13. Policy effective 2026-05-04, update 2026-06-17. | 318 | P11 | 2026-05-04 / 2026-06-17 | post-cutoff (update) | Decides which ad formats an under-13 audience may see (RG-01). |
| FC-08 | P1 | Ads may not be personalized for users under 18. Ads for under-18 may not directly urge children to buy or pressure adults to buy for them. Required: clear disclosure, truthful claims, non-infringing assets. Prohibited: misleading free-Robux offers, fake system controls. | 318, 497 | P12 | 2026-10-09 | post-cutoff | Hard policy; breach can lead to rejected or removed ads. |
| FC-09 | P1 | Rewarded Video remains 13+; rewards predetermined, opt-in, promptly delivered; watching cannot gate progression. Latest revision changes Portal restrictions and several restricted product categories. | 318, 353, 497 | P12 | 2026-10-09 | post-cutoff | Paper warns against a blanket 13+ rule. Check what changed in the latest revision. |
| FC-10 | P1 | Ad integrations: paid branded content and specified off-platform promotion (including own merchandise) can count; register campaigns, submit assets, build eligibility and disclosure controls. | 320 | P13 | live | live | Scope of RG-05. Check the "own merchandise" example. |
| FC-11 | P1 | `AdService:GetCampaignEligibilityAsync` decides whether assets may be shown; region and age limits can apply; a rejected asset can invalidate the whole campaign; adding assets to an active campaign limits serving to 18+ during review. | 320 | P13 | live | live | Exact API name and the 18+ rule affect fallback behavior (RG-05). |
| FC-12 | P1 | Whole-game ads need a persistent bottom-right HUD label and an "Ad" disclosure at the thumbnail's bottom-left. Roblox recommends submitting at least five days ahead. | 320 | P13 | live | live | Positions and the five-day figure go into TP-THUMB and TP-LAUNCH. Check "recommends" vs "requires". |
| FC-13 | P1 | Integration revenue-share pricing starts 2027-01-01. Published CPTV, first 28 days, USD: $1.50 U.S.; $0.75 Tier 1; $0.20 Tier 2; $0.05 Tier 3. Later visits $0.10 per thousand. A qualified visit = a session engaging with branded assets. Influencer deals outside the integration are excluded. | 322, 354 | P11, P13 | 2026-06-17; live | post-cutoff | Money. Check the unit of "$0.10 per thousand" (X-26), tier definitions and that these are not influencer fees. |
| FC-14 | P1 | Paid-random-item rules cover purchases using Robux or Robux-acquired currency; actual numerical odds and eligibility handling required. | 324 | P14 | live | live | Separate approval check PO-17(2). |
| FC-15 | P1 | Roblox requires PolicyService integration for restricted features and recommends avoiding urgent, pushy messages to minors. | 324 | P15 | live | live | Check which part is required and which only recommended. |
| FC-16 | P1 | Roblox lists misleading or mismatched metadata among discoverability concerns. | 330 | P19 | live | live | Basis for the promise-match proof sheet (PO-22). |
| FC-17 | P1 | Native Roblox preview has its own content rules, so a voiced social trailer cannot be reused unchecked. | 491 | D07 | live | live | The register quote for D07 is about activating 2 or more thumbnails, not preview rules. Find the preview rule in the page. |
| FC-18 | P1 | Thumbnail analytics still document qPTR; the June RFY announcement uses PTR and bounce; a July staff reply acknowledged the mismatch. | 509 | D02, D07, D10 | 2026-06-15; live; 2026-07-20 | post-cutoff | Metric label rule (OQ-01). D07's register quote does not mention qPTR. |
| FC-19 | P1 | Current event docs say a seven-day featuring submission lead time; the original pilot said 14 days. | 511 | D13, D14 | live; 2025-12-10 | live | The D13 register quote is about a 10-event maximum, and D14 shows 14 days. Find "seven days" in D13. |
| FC-20 | P1 | Ads docs describe even creative delivery; an older announcement described engagement-based optimization. | 511 | P01, P10 | live; 2025-08-05 | live | Decides whether creative tests in Ads Manager are interpretable. The P01 register quote is about payment method. |
| FC-21 | P1 | Creators may not track Roblox users across third-party platforms or services; do not export presence or user data because a vendor offers a connection. | 501 | S18 | 2026-06-02 | post-cutoff | Limits Discord and creator-tool integrations. |
| FC-22 | P1 | Thumbnail personalization uses a multi-arm bandit, not A/B testing (so adaptive allocation is not a randomized experiment). | 487 | D08 | 2024-11-13 (upd 2025-02-13) | pre-cutoff | Basis for DN-02. Check it is still the current method. |
| FC-23 | P1 | Native preview duration, file-size and codec limits: the paper did not establish them. | 521 | live upload interface | n/a | live | Unknown. Read the live interface before export. |
| FC-24 | P1 | Whether a newly announced ad format or optimization is enabled for this account is unknown. | 525 | live account | n/a | live | Unknown. Check the real account before any budget proposal. |
| FC-25 | P1 | Earnings and DevEx eligibility is a third, separate approval check. | 324 | P16 (named only by range) | live; rate date 2026-06-08 | live | The paper names DevEx but cites no id here. Low risk; check only if a skill states DevEx rules. |
| FC-26 | P2 | YouTube Shorts public views count starts and replays since 2025-03-31, with no minimum watch duration. | 301 | S03 | 2025-03-31 | pre-cutoff | Report fields (ME-23). |
| FC-27 | P2 | TeamYouTube: first-frame public-view standard extends to all formats on 24 August (2026), rollout confirmed 27 August; engaged-view metric remains available. | 301 | S04 | 2026-08-17 / 2026-08-27 | post-cutoff | The paper omits the year for 24 and 27 August. Check year and the "remains available" claim. |
| FC-28 | P2 | YouTube average view duration is built on engaged views and their watch time; stayed-to-watch reflects viewing past the first Shorts seconds; thumbnail CTR uses registered thumbnail impressions. | 303 | S05 | live | live | Basis for "different events, different denominators" (ME-22, ME-24). Check "stayed-to-watch" wording. |
| FC-29 | P2 | US Copyright Office: copyright does not protect a game idea, title or play method as such; expressive artwork or text can be protected. | 328 | P17 | live | live | US only. Basis for PO-20. |
| FC-30 | P2 | USPTO: trademark confusion depends on mark similarity and related goods or services, not exact spelling alone. | 328 | P18 | live | live | US only. Basis for TP-TITLE-05. |
| FC-31 | P2 | Steam base capsule rules exclude review scores, awards and promotional calls to action. | 350 | N12 | live | live | The register quote shows only review scores. Check "awards" and "calls to action". |
| FC-32 | P2 | Steam Next Fest requires a released demo, categories/tags and preview checks; press coverage is not guaranteed. | 280 | N11 | live | live | The register quote shows only the demo rule. |
| FC-33 | P2 | FTC guidance: responsibility for clear disclosure of a material connection rests with the influencer and the brand. | 493 | P06 | 2023 | pre-cutoff | Basis for DN-05 and the creator brief. |
| FC-34 | P2 | YouTube paid-partnership controls and automated disclosures (age and geographic controls for branded content). | 493 | P07 | 2026-09-03 | post-cutoff | A platform label may not discharge every disclosure duty (DN-05). |
| FC-35 | P2 | Meta Trial Reels show content to non-followers first. | 487 | S10 | 2024-12-10 (upd 2025-06-26) | pre-cutoff | Used only in DN-02 (sequential social posts are not a randomized test). Check what the paper means by "sequential". |
| FC-36 | P2 | Some current Instagram Help metric definitions could not be verified reliably. | 522 | live account Insights | n/a | live | Unknown. Read the account's Insights definitions. |
| FC-37 | P3 | Grow a Garden: partnership start about 500 CCU / 10,000-20,000 DAU; about 100,000 CCU in two weeks; about 1 million in a month; 12 million TikTok followers; weekly updates. | 268 | C02 | 2025-09-07 (upd 2025-09-08) | pre-cutoff | Approximate recollection. Check the word "partnership" (X-23). |
| FC-38 | P3 | Gabby's Dollhouse Official: 7M+ visits in 45 days; movie activation 71M+ sessions, 24M+ unique players, 9.3M+ trailer views, 15M+ hours; 28M+ YouTube views combined; DreamWorks used the game as a set. | 270 | C03 | undated | live | Exact figures; check which are "combined impact". |
| FC-39 | P3 | Squad Busters used a celebrity ensemble and reported 40 million preregistrations. | 274, 285 | N01 | 2024-05-29 | pre-cutoff | Check the "creator counterparts" part too. |
| FC-40 | P3 | Squad Busters: more than US$100 million gross revenue in the first seven months of 2024; development later ended. | 274, 285 | N01, N02, N03 | 2024-05-29; 2025-02-11; 2025-10-30 | pre-cutoff | The register quotes do not hold the $100M figure. Find which source states it. |
| FC-41 | P3 | Mario Kart World Direct recap introduced an interconnected world, then showed effects on game modes. | 276 | N07 | 2025-04-17 | pre-cutoff | Mechanism claim only. |
| FC-42 | P3 | Nintendo: 5.63 million units for April-June 2025, including hardware-bundled copies. | 276, 286 | N08 | 2025-08-01 | pre-cutoff | Exact figure and the "including bundled" scope. |
| FC-43 | P3 | Arcane season-two calendar: screenings, themed physical experiences, fan gatherings across regions; access from ticketed to free. | 278 | N09 | 2024-10-10 | pre-cutoff | Structure claim only. |
| FC-44 | P3 | Medal vendor pages (clip incentives; "estimated growth with a single activation") are the source of the "projected activation figures" warning. | 503 | C04, C05 | live | live | Vendor claims stay EXPERIENCE (MP:531). Check that the paper's "projected" label matches the page. |

## 12. Contradictions and limits

### 12.1 Where the paper says its sources disagree or mismatch (MP:509, 511)

| ID | MP | Item | Handling for skills |
| --- | --- | --- | --- |
| X-01 | 509 | qPTR vs PTR plus bounce: thumbnail analytics docs and the June RFY announcement use different labels (D02, D07, D10). | Keep both labels and definitions. Never relabel old rates. See OQ-01. |
| X-02 | 511 | Event featuring lead time: current docs say seven days, the original pilot said 14 (D13, D14). | Check the live form. Use a conservative contingency and say it is a contingency, not a platform rule. See OQ-02. |
| X-03 | 511 | Ads delivery: docs say even creative delivery; an older announcement said engagement-based optimization (P01, P10). | Check live account behavior before reading an ad creative test. See OQ-03. |

### 12.2 Limits the paper puts on its own evidence

| ID | MP | Limit | Handling for skills |
| --- | --- | --- | --- |
| X-04 | 268 | Grow a Garden is an exceptional survivor case with an approximate retrospective account. It is not a cadence study or a TikTok funnel. The early numbers are CCU and DAU, not retained acquisition. | Use as a mechanism story only. Never quote it as a benchmark. |
| X-05 | 270 | Gabby's Dollhouse numbers cover different counts and phases (visits, sessions, unique players, views, hours). Licensed IP and a movie campaign limit transfer. | Never add or chain these into a funnel. See DN-10. |
| X-06 | 274 | Squad Busters shows that awareness, early revenue and lasting success differ. Preregistration and celebrity budget do not transfer. | Use for the single-premise lesson only. |
| X-07 | 276 | The 5.63 million figure includes hardware bundles. It is not a Direct conversion rate or a Roblox benchmark. | Keep the denominator with the number (N-02). |
| X-08 | 278 | Arcane's published calendar shows structure, not incremental acquisition or ROI. | Cite as a structure example only. |
| X-09 | 280 | Steam Next Fest rules and wishlists do not transfer to Roblox. | Transfer preparation and the playable demo only. |
| X-10 | 287, 458 | The four-before, four-after window is a requested planning window, not an optimum, and not proof a launch gets recommendation traffic. | Present as a template, with decision gates, not as a schedule target. |
| X-11 | 291 | D16 is measurement infrastructure. A rise across 2026-10-12 is not evidence a creative worked. | Annotate; do not attribute (ME-04). |
| X-12 | 293 | A young cohort cannot show mature D7 or 30-day value. | Report as pending (ME-10). |
| X-13 | 295 | Share links give channel attribution, not incremental lift. Video views alone give no off-platform revenue. | Label "attributed", never "incremental" (RG-06). |
| X-14 | 297 | An API being available does not make it stable. An announcement that something is coming is not availability. | Log operations and state the status label (ME-17). |
| X-15 | 301-305 | YouTube view counts, engaged views, average view duration and thumbnail CTR are different events with different denominators. The count definition changed on 2025-03-31 and again from 2026-08-24. | Keep the metric version in every report (ME-23). |
| X-16 | 322 | CPTV prices are platform integration charges from 2027-01-01. They are not a recommended influencer fee and not a Sponsored Tile CPP. | Never use them to budget an influencer or an ad tile (DN-06). |
| X-17 | 531 | Quotes in the register are short anchors. Some paper claims are not visible in the one register quote: the P13 five-day figure, the D13 seven-day figure, the D07 preview rule, the N12 awards and calls-to-action rule, the P01 even-delivery claim. (Extractor's note.) | Fact-checker must read the full source page for these (FC-12, FC-17, FC-19, FC-20, FC-31). |
| X-18 | 531 | Company and vendor outcome reports stay EXPERIENCE even when hosted on an official page. | Keep EXPERIENCE on all case figures (LA, N-13 to N-22). |
| X-19 | 274 | The $100M gross revenue figure and "first seven months" sit in a paragraph that cites N01, N02 and N03 without naming the source of each figure. N02's register quote is about falling short of aspirations. (Extractor's note.) | Treat the figure as company-reported and unlocated until FC-40 is checked. |
| X-20 | 274, 285 | LA-08 (development ended) is unmarked in MP:274 (inside an EXPERIENCE paragraph). MP:285 calls N03 a "VERIFIED announcement". (Extractor's note.) | Tag it as the announcement fact; the interpretation stays OPINION. |
| X-21 | 318 | The P12 paragraph is marked VERIFIED, but its last sentence ("do not apply a blanket old 13+ rule") is advice. (Extractor's note.) | Treat the advice as the paper's, the rule changes as Roblox's. |
| X-22 | 13, 7 | OPINION rows are original synthesis; their cited sources show the constraint or example, not that the recommendation works. Research is not authorization to publish, contact creators, buy ads or contract. | Never promote an OPINION row to a platform rule. |
| X-23 | 268 | The paper writes "the partnership" starting at about 500 CCU without saying whose partnership. (Extractor's note.) | Quote as "Jandel's account" and check C02 (FC-37). |
| X-24 | 264-527 | Terms used but not defined in this part: PTR, qPTR, RFY, CPTV, CPP, CCU, DAU, DevEx, LaunchData, bounce, PolicyService. (Extractor's note.) | Take definitions from the live dashboard or doc. Do not guess. |
| X-25 | 301 | "24 August" and "27 August" have no year in the paper; the register gives 2026-08-17 and 2026-08-27 for S04. (Extractor's note.) | Write the full date in any skill. |
| X-26 | 322 | "$0.10 per thousand" is not tied to a unit (per thousand visits is likely but the paper does not say). (Extractor's note.) | Check P11 and P13 before stating the unit. |
| X-27 | 295 | "Group creation needs Manage share links permission and the group account" is short; it is read here as creating links for a group-owned game. (Extractor's note.) | Check D18 wording (FC-04). |
| X-28 | 503 | The warning about "projected activation figures" cites C03-C05, but C04 and C05 are Medal vendor pages, not results. (Extractor's note.) | Treat vendor estimates as projections, case-study counts as reported results. |
| X-29 | 527 | The paper recommends an evidence-producing workflow, not a guarantee of discovery. | Never promise reach, rank or revenue. |

### 12.3 Unknown or not established by the paper (MP:516-525)

| ID | MP | Not established | Handling for skills |
| --- | --- | --- | --- |
| X-30 | 516 | Best title length or wording; controlled Roblox uplift by word count, emoji or update tag. | No title-length rule. Comprehension check first (OQ-04). |
| X-31 | 517 | Winning icon composition; universal effect of faces, emotion or contrast. | No formula. Test truthful alternatives (OQ-05). |
| X-32 | 518, 448 | Best short-video length and cadence; the "first 3 seconds" field is a planning field, not a threshold. | No length or cadence target (OQ-06, N-42). |
| X-33 | 519 | Creator rate card; follower-to-retained-player conversion. | No invented fees (OQ-07, DN-06). |
| X-34 | 520 | Incremental ad value without a holdout. | Report attribution as attribution (OQ-08). |
| X-35 | 521-525 | Native preview limits, Instagram metric definitions, brand-campaign transfer, low-traffic learning, current account eligibility. | Check live; keep inconclusive results (OQ-09 to OQ-13). |
