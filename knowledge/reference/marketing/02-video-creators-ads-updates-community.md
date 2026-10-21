---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: "J012-T02, Roblox_Marketing_Agent_Research_2026.txt lines 117-263"
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-21

# Marketing paper part 2: short videos and trailers, creators and offers, Roblox ads and accounting, updates/events/notifications, community and the Roblox privacy conflict (lines 117-263)

Paraphrased notes. The paper (MP) stays outside git; its research cutoff is 2026-10-21. Every row cites `MP:<line>`. Nothing here is fact-checked yet: claims are the paper's, and section 8 lists what a fact-checker must open live. The paper's own limits ("not a forecast", "not a rate card", "attribution is not incrementality") sit next to the claim they limit and are collected again in section 9. Lines 1-15 (evidence method) are summarized in the key table below. Part 1 of the paper (lines 16-116) is not covered here.

## 0. How to read

| Key | Meaning |
| --- | --- |
| MP:n | Line n of `Roblox_Marketing_Agent_Research_2026.txt`. One paragraph = one line. Source register = MP:529-1164 (only cited entries are resolved here, section 7). |
| Tag | The paper's own tag, kept exactly as the paper marks the statement (MP:11). VERIFIED = an official rule, documented product behavior or directly documented measurement. It does NOT mean the paper's author audited Roblox's algorithm, ran a campaign or tested an account. EXPERIENCE = a developer, publisher, platform or vendor's reported outcome or interpretation. OPINION = a proposed studio procedure or reasoned application, not established causality. Combined marks the paper uses are kept (for example "OPINION / EVIDENCE GAP", "VERIFIED advice", "VERIFIED announcement"). |
| synth | The paper's own dated OPINION synthesis (2026-10-21). It has no source id. The sources it cites "explain the constraint or example, not proof that the recommendation will work" (MP:13). Basis ids are written in brackets, for example `synth [S01, S06]`. |
| Src | The paper's source id, resolved in section 7 with date, URL and a short register quote. "undated live" = living documentation with no publication date; the paper only read it on 2026-10-21. Access is not publication (MP:11). |
| Row IDs | SV short video/trailer, CR creator/sponsorship, AD ads/accounting, UP updates/events/notifications, CM community, N number, FC claim to check, X contradiction or limit. Row ids use a hyphen (SV-01). The paper's own source ids N04 and N10 (Brawl Stars blog, Steamworks trailers) have no hyphen and appear only in Src columns and section 7. |
| Central rule (MP:7) | Optimize the whole promise-to-play journey, not isolated impressions, views or clicks. The owner stays creative director and decision-maker. The agent proposes creative work and measurement plans. Research is NOT authorization to publish, contact creators, buy advertising or make contractual commitments. |
| Editorial method (MP:13) | A source's concrete rule and its commercial-success claim can carry different marks. A platform-reported randomized study stays platform-reported evidence when its full method is unavailable. A case can show a mechanism without showing expected return for another game. |
| Rule of use | Treat every OPINION row as a proposed check of the studio, never as a platform rule. Never write "YouTube requires X" or "Roblox requires X" from an OPINION row. Never turn a case number into a forecast, a budget or a benchmark. |
| Cutoff flag | Used in sections 7 and 8. "post-cutoff" = source dated (or updated) after 2026-06-01. "undated live" = living page, content may differ from what the paper read. "pre" = dated on or before 2026-06-01. |

## 1. Short videos and trailers (MP:117-153)

### 1.1 What the platforms document (MP:119-131)

| ID | MP | Lesson | Tag | Src |
| --- | --- | --- | --- | --- |
| SV-01 | 119 | YouTube says Shorts recommendations consider whether viewers choose to watch, whether they stay, average view duration, average percentage viewed, likes and post-watch surveys. Personalization and competing content also matter. YouTube publishes no universal winning percentage and no mandatory format. | VERIFIED | S01 (undated live) |
| SV-02 | 119 | TikTok describes recommendations from watch/skip behavior, likes, shares, comments, sounds, hashtags and viewer context. For most users, interactions including watch time weigh more than other factors, but the weights can change. | VERIFIED | S07 (undated live) |
| SV-03 | 119 | Limit: neither source establishes a Roblox-specific viral formula. | VERIFIED | S01, S07 |
| SV-04 | 121 | TikTok's June 2025 performance-ad guidance advises stating the proposition within 3 seconds, setting the hook within 6 seconds, and using contextual captions/text. Limit: this is paid-advertising guidance, not proof that organic videos fail after a precise threshold. | VERIFIED | S06 (updated 2025-06) |
| SV-05 | 121 | The often-repeated "90% of ad recall within six seconds" claim comes from older advertising research (studies 2021-2022). It is not a 2026 experiment on Roblox clips. | VERIFIED | S22 (undated; studies 2021-2022) |
| SV-06 | 125 | YouTube Shorts can run up to 3 minutes. That maximum is not evidence of an ideal length. YouTube advises matching length to the content and using both absolute and relative watch-time signals. | VERIFIED | S03, S02 (both undated live) |
| SV-07 | 129 | TikTok recommends its Commercial Music Library for promotion. Its general music licenses outside that library do not cover commercial use. Other protected music needs the right rights. | VERIFIED | S08 (undated live) |

### 1.2 The paper's craft procedure (MP:123, 127, 131)

| ID | MP | Lesson | Tag | Src |
| --- | --- | --- | --- | --- |
| SV-08 | 123 | Treat the first 3 seconds as a production review checkpoint, not an algorithm boundary. Show a legible player action and its surprising consequence before explaining lore. | OPINION | synth 2026-10-21 [S01, S06] |
| SV-09 | 123 | Hook candidates the paper names: a clever combat reversal, a surprising machine chain, a cooperative rescue, a genuinely rare transformation, a player-created build. Reject a hook whose payoff is not available in the current build. Cut loading, walking to the action and generic logo openings unless they serve a deliberate narrative purpose. Limit: craft judgment, not a measured success rate. | OPINION | synth [S01, S06] |
| SV-10 | 127 | Use the shortest edit that makes the action understandable and earns its payoff. Compare a compact payoff clip against a longer explanatory cut. Do not declare a universal 15-, 30- or 60-second optimum. | OPINION | synth [S02, S03] |
| SV-11 | 127 | Render a vertical version that keeps gameplay readable. Check text against the real controls of the destination app. Review once muted and once with sound. Captions explain the decision or consequence and must not cover the reticle, resource counter or target. No universal caption speed is given; TikTok's ad recommendation is not a child-reading standard. | OPINION | synth [S06] |
| SV-12 | 131 | Keep a clean gameplay/sound-effects master, a caption-free master, and each platform edit. Record music license, allowed platforms, paid-media rights, territory and expiry separately. Do not assume a trending track, or one platform's music library, clears cross-platform ads. Keep authentic game sounds when they explain the action. | OPINION | synth [S08] |

### 1.3 Posting times and frequency (MP:133-137)

| ID | MP | Lesson | Tag | Src |
| --- | --- | --- | --- | --- |
| SV-13 | 135 | YouTube says no minimum cadence is needed for Shorts to perform well, and publish time is not known to affect long-term video performance. Audience-active times can help initial viewing and matter for Live/Premiere scheduling. Its schedule advice still recommends consistency and sustainability. The paper reads these as statements about different outcomes, not opposing algorithm rules. | VERIFIED | S01, S02, S21 (all undated live) |
| SV-14 | 137 | Pick a cadence the capture/editor pipeline can sustain. Report output and learning, not a made-up daily quota. Pick times from the channel's observed audience geography/activity and release logistics. | OPINION | synth [S01, S02, S21] |
| SV-15 | 137 | The reviewed primary sources contain no substantiated universal posting hour or posts-per-day target for Roblox on TikTok or Reels. Do not import generic SEO "best time" tables as facts. | OPINION | synth (evidence limit) |

### 1.4 Instagram tools and limits (MP:139-145)

| ID | MP | Lesson | Tag | Src |
| --- | --- | --- | --- | --- |
| SV-16 | 141 | Trial Reels show content to non-followers first; the creator can then share it more widely. Meta described an optional auto-share decision that uses views in the first 72 hours. Limit: a product capability, not a controlled A/B test. | VERIFIED | S10 (2024-12-10; updated 2025-06-26) |
| SV-17 | 143 | Meta reported that after trying Trial Reels, 40% of creators posted more often, and among that subgroup 80% saw more non-follower reach. Limit: do not turn the conditional 80% into 80% of all creators, a predicted reach lift, or Roblox-specific causality. | EXPERIENCE | S11 (2025-06-12; updated 2025-06-26) |
| SV-18 | 145 | Meta's Edits app supports editing and watermark-free export, and exposes feedback such as skip rate that can affect distribution. | VERIFIED | S12 (2025-04; updated 2025-12-17) |
| SV-19 | 145 | Use these features as diagnostics, not guarantees. Check the account's current metric labels before copying any formula. The paper could not read the current Instagram Help insight page reliably, so it does not present the 2023 watch-time denominator as verified current in 2026. | OPINION | synth [S12] |

### 1.5 Steam trailer craft, non-Roblox (MP:147)

| ID | MP | Lesson | Tag | Src |
| --- | --- | --- | --- | --- |
| SV-20 | 147 | Valve recommends player-perspective gameplay early in a Steam trailer and checking that the trailer is understandable without sound. Steam's six-second microtrailer is generated from six one-second extracts. Limit: not a Roblox specification. | VERIFIED | N10 (undated live) |
| SV-21 | 147 | Transfer visible playable proof and sound-off clarity. Do not transfer Steam's exact product mechanics. | OPINION | synth [N10] |

## 2. Creators, sponsorships and offers (MP:155-178)

| ID | MP | Lesson | Tag | Src |
| --- | --- | --- | --- | --- |
| CR-01 | 157 | Buy an identifiable audience and a deliverable, not a follower count. The brief names: the real game promise, target language/region/platform, the creator's relevant recent content, deliverables, dates, disclosure wording, permitted edits, usage rights, paid-amplification rights, approval boundaries and measurement access. | OPINION | synth 2026-10-21 [P06-P09] |
| CR-02 | 157 | Ask for observed median views on comparable recent videos and for audience geography, not a single best post. Say plainly that honest reactions are welcome and paid praise is not required. | OPINION | synth [P06-P09] |
| CR-03 | 159 | FTC guidance (2023, read 2026-10-21) requires clear disclosure of unexpected material connections and truthful endorsements. Platform disclosure tools are not automatically sufficient. For video, the guidance favors disclosure inside the video, visual and audible. Brands and intermediaries must train and monitor their endorsers. Limit: U.S. guidance, not assurance of compliance elsewhere. | VERIFIED | P06 (2023 revision) |
| CR-04 | 161 | YouTube (2026-09-03) introduced refreshed branded-content disclosures and age/geographic controls and announced automated detection. The creator stays responsible. Sponsored content must be declared in the paid-promotion setting. | VERIFIED | P07 (2026-09-03), P08 (undated live) |
| CR-05 | 161 | TikTok requires commercial-content disclosure both for one's own business and for compensated third-party promotion, with labels that distinguish the cases. Tagging a brand partner can also grant advertising authorization, so disclosure and reuse rights must not be confused. | VERIFIED | P09 (undated live) |
| CR-06 | 163 | If the creator is a minor: require a properly authorized adult/representative and a jurisdiction-specific review of contracting, compensation, privacy and safeguarding before any agreement. Do not assume account eligibility proves contractual capacity. Do not ask creators to collect children's contact information. Do not invent a universal legal minimum creator age. | OPINION | synth [P06-P09] |
| CR-07 | 165 | Evidence gap: the source set established no defensible universal Roblox creator fee, CPM, cost per acquired player or guaranteed conversion rate. Get written quotes for each campaign. Separate creator production fee, licensing/reuse, paid amplification, agency fees and any performance component. Limit: an unpublished quote is not a market benchmark. | OPINION / EVIDENCE GAP | synth (evidence limit) |
| CR-08 | 167 | Give each creator a distinct link or campaign parameter. Record clicks, attributed joins, first-session outcomes and mature retention. Link sharing, manual searchers, existing-player overlap and simultaneous updates all limit attribution. Ask for aggregate reports, not children's personal data. Trial a bounded deliverable before a larger commitment. The owner approves spend and external communications. | OPINION | synth [P01, P06-P09] |
| CR-09 | 169 | Non-Roblox case: TikTok reports that creator-led paid creative for Clash Royale raised CTR by 107% and six-second view-through rate by 65%. Budget, sample, campaign dates and allocation are undisclosed. Limit: figures concern paid creative, not Roblox organic acquisition or expected returns. | EXPERIENCE | S19 (undated live) |
| CR-10 | 171 | YouTube requires a branded-content declaration and clear disclosures. Branded-content videos are removed from YouTube Kids. A child-friendly creator is not a workaround for that restriction. | VERIFIED | S13 (undated live) |
| CR-11 | 171 | Meta supports partnership ads for eligible creator content. Access and price are separate questions. | VERIFIED | S20 (2024-02) |
| CR-12 | 173 | Case, Petrex "Catch the Drop": 51 public videos from 32 channels, posted 10-30 April 2026, with 79,587 combined views and 2,534 likes observed on 7 October 2026. The case separately reports 2M+ game visits and a 92% like ratio. Limit: the public-video sample is a floor, not unique reach or attributable campaign acquisition; creator costs were not disclosed. | EXPERIENCE | C06 (2026; measured 2026-10-07) |
| CR-13 | 173 | Keep three things apart: deliverables, public counts, and game totals. | OPINION | synth [C06] |

## 3. Roblox ads and sponsored placements (MP:180-220)

### 3.1 Ads Manager settings, row by row (MP:184-193)

The paper marks the whole table VERIFIED (P01, living documentation, accessed 2026-10-21). It can change; check the live page. Units of the audience minimums are not stated in the paper.

| ID | MP | Setting | Documented behavior (paraphrase, numbers exact) | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| AD-01 | 187 | Access / payment | Advertiser age 13+ with a verified email. Payment cards require 18+. Minimum conversion is 1 ad credit, and a conversion is irreversible. | VERIFIED | P01 |
| AD-02 | 188 | Placement | Home and search, assigned automatically. | VERIFIED | P01 |
| AD-03 | 189 | Audiences | Four options. All. New: never / absent 180+ days (paper's wording). Recent: last 30 days (paper's wording), minimum 10,000. Lapsed: 30-180 days, minimum 20,000. | VERIFIED | P01 |
| AD-04 | 190 | Targeting | Location, age, gender, genre and device, subject to audience eligibility. | VERIFIED | P01 |
| AD-05 | 191 | Creatives | Up to 10 thumbnails, 16:9, documented as evenly distributed. | VERIFIED | P01 |
| AD-06 | 192 | Reporting | Post-click processing can take 48 hours. | VERIFIED | P01 |
| AD-07 | 193 | Attribution | First-time users: 30 days. Last played less than 7 days ago: the clicked session only. Absent 7-29 days: 7 days. Absent 30+ days: 30 days. | VERIFIED | P01 |

### 3.2 Bidding, objectives, and what the paper tells the agent to do (MP:195-197)

| ID | MP | Lesson | Tag | Src |
| --- | --- | --- | --- | --- |
| AD-08 | 195 | Staff reply of 2025-04-09: the new Ads Manager uses fractional automated bidding instead of asking creators to set a manual bid. Competitive demand can delay serving. | VERIFIED | P02 (2025-04-09) |
| AD-09 | 195 | 2026-05-07: Earnings was introduced together with revised attribution and user-reporting segments. | VERIFIED | P03 (2026-05-07) |
| AD-10 | 195 | 2026-06-16: Engagement launched to help reach highly engaged players, tied to Kids/Select eligibility. (The register quote calls it a "beta"; see X-37.) | VERIFIED | P04 (2026-06-16, post-cutoff) |
| AD-11 | 195 | 2026-10-02: Earnings access expanded to nearly 30,000 games. Eligibility is determined in the interface. | VERIFIED | P05 (2026-10-02, post-cutoff) |
| AD-12 | 197 | Use Plays for a bounded acquisition test. Use Earnings when the objective is monetization and the account is eligible. Use Engagement only for its specific audience-reach purpose. Do not buy Engagement traffic and judge it as the cheapest general acquisition campaign. Do not reuse manual CPP-bid tutorials from before 2025 as current setup steps. | OPINION | synth 2026-10-21 [P01-P05] |
| AD-13 | 197 | The reviewed sources do not establish a universal minimum daily spend, a maximum account spend, or a current fixed Robux-to-credit exchange ratio. Verify the purchase preview and the campaign UI before approval. Never silently substitute an old 285-Robux rule. | OPINION | synth [P01-P05] |

### 3.3 What the published numbers establish, and the two-ledger accounting (MP:199-209)

| ID | MP | Lesson | Tag | Src |
| --- | --- | --- | --- | --- |
| AD-14 | 201 | Roblox-reported randomized studies, 21 campaigns: all produced incremental plays. Median lift was 14% for incremental play sessions and 10% for D7 retained users. Limit: reported study medians, not a forecast. | EXPERIENCE | P05 (2026-10-02, post-cutoff) |
| AD-15 | 201 | Ink Game reported USD $250/day and a 277% return in the Earnings spotlight. Limit: neither figure is a launch budget, a typical creator payout, a universal CPI, or independently audited proof the studio will profit. The spotlight does not publish enough cost accounting to infer net profit. | EXPERIENCE | P05 |
| AD-16 | 203 | ROAS reporting now includes Creator Rewards, Immersive Ads and Rewarded Video earnings, and converts earnings to USD with applicable rate differences. Estimated ROAS is a forecast while earnings accrue. | VERIFIED | P05 |
| AD-17 | 205 | Keep two ledgers: platform-attributed ROAS, and studio incremental contribution. The second = estimated incremental net receipts minus advertising, creator production/licensing, campaign assets and incremental operating costs. | OPINION | synth 2026-10-21 [P01, P05, P16] |
| AD-18 | 205 | Do not compare gross player Robux spending with a USD media bill. Do not convert all receipts at the premium U.S. adult rate. Report both cash spend and the opportunity cost of reinvested earned Robux, without counting that cost twice. | OPINION | synth [P01, P05, P16] |
| AD-19 | 207 | DevEx standard rate for eligible Earned Robux after 2025-09-05 10:00 PT is USD $0.0038; balances from before that date use $0.0035. The eligible U.S. 18+ rate is $0.0054 from 2026-06-08. Limit: conditional DevEx rates, not retail Robux purchase prices and not a guaranteed cash-out approval. (The paper gives the dollar figures only; the per-Robux unit is implied by the DevEx context.) | VERIFIED | P16 (undated live; rates effective 2025-09-05 and 2026-06-08) |
| AD-20 | 209 | In the weekly report, separate new, recent and resurrected users. Show spend, observed joins, denominator, cohort maturity and retention. Record concurrent game changes, organic featuring, seasonality, creator posts and outages. Use a randomized holdout if one is available to estimate incrementality. A before/after increase alone cannot allocate causality. Do not add several channels' attributed revenues as if they were necessarily disjoint. | OPINION | synth 2026-10-21 [P01, P05] |

### 3.4 Disagreements and rollout ambiguity (MP:211-215)

| ID | MP | Lesson | Tag | Src |
| --- | --- | --- | --- | --- |
| AD-21 | 213 | P01 (current setup doc) says creatives are evenly distributed. The older P10 announcement (2025-08-05) promised engagement-based creative optimization. | VERIFIED | P01 versus P10 (2025-08-05) |
| AD-22 | 213 | Treat delivery logic as unresolved when interpreting experiments. This is not proof that every creative comparison is randomized. | OPINION | synth [P01, P10] |
| AD-23 | 215 | P05's October announcement says Sponsored Tile video support is coming "in coming weeks"; the current setup doc describes thumbnails. | VERIFIED | P05 versus P01 |
| AD-24 | 215 | Confirm video support in the specific account. Do not present an announcement as universal availability. Allow for moderation contingency; do not promise same-day approval. | OPINION | synth [P01, P05] |

## 4. Updates, events and return messages (MP:222-237)

| ID | MP | Lesson | Tag | Src |
| --- | --- | --- | --- | --- |
| UP-01 | 224 | Creator Hub, Engagement, Events & Updates supports up to ten ongoing/upcoming events. | VERIFIED | D13 (undated live) |
| UP-02 | 224 | Trending Events eligibility needs a public, active event that started within seven days and has at least 1,000 RSVPs. Its sort uses game DAU. (Paper's table: "eligibility, not guaranteed reach".) | VERIFIED | D13 |
| UP-03 | 224 | Update announcements remain a distinct, old-form workflow during the consolidation: 60 characters maximum, once per three days, delivered to opted-in players. Reports show views, visit rate and unfollow rate. | VERIFIED | D13 |
| UP-04 | 224 | Current off-platform featuring documentation says submit at least seven days ahead. Selection is not automatic. | VERIFIED | D13 |
| UP-05 | 226 | The original Off-Platform Featuring announcement (2025-12-10, initial pilot) required 14 days' notice, listed App Store, Google Play and Roblox channels, and asked for either 1920×1080 plus 1080×1920 finished art, or a 4000×4000 layered PSD. | VERIFIED | D14 (2025-12-10) |
| UP-06 | 226 | This conflicts with the current seven-day documentation. Use current docs for the documented minimum, reserve 14 days as an optional planning buffer, and verify the live submission form. Do not present the old pilot's three-to-five selected holiday events as current capacity. Do not promise featuring from eligibility alone. | OPINION | synth [D13, D14] |
| UP-07 | 228 | Personalized experience notifications serve opted-in users aged 13+. A user can receive one per day per experience. Aggregate user throttles and spam prevention can still block delivery. | VERIFIED | D15 (undated live) |
| UP-08 | 228 | The dashboard needs 100 aggregate impressions for summary performance and 100 per notification for itemized stats. CTR = clicks / impressions. Dismiss and turn-off rates also use impressions. | VERIFIED | D15 |
| UP-09 | 228 | The opted-in total can include under-13 users who are eligible for update notices but not for personalized experience notifications. New notification strings are recommended for variants. Category can segment analytics. These are not the same channel or cadence as the three-day update announcements. | VERIFIED | D15 |
| UP-10 | 230 | Tie each message to a real, accessible reason to return. Keep opt-out signals next to visits. A tool's sending ceiling is not a recommended content cadence. | OPINION | synth [D13-D15] |
| UP-11 | 230 | Record event ID, actual build availability, scheduled time zone, assets, approval state, audience, intended destination and measurement period. Check the event-specific spawn path before promotion. Measure notification reach from impressions, not from requests sent or from everyone opted in. | OPINION | synth [D13-D15] |

## 5. Community and player participation (MP:239-262)

| ID | MP | Lesson | Tag | Src |
| --- | --- | --- | --- | --- |
| CM-01 | 241 | Discord's current minimum age is at least 13 and can be as high as 16 by country. | VERIFIED | S14 (updated 2026-09-22, post-cutoff) |
| CM-02 | 241 | Discord's September 2026 update groups users as adult, teen or unconfirmed. Teen protections include routing non-friend DMs to requests and restricting adult content and settings. Other server members cannot see an account's age group. Do not mistake membership or Roblox account linking for proof of adulthood. | VERIFIED | S14, S16 (2026-09-22, post-cutoff) |
| CM-03 | 243 | AutoMod is available to all Discord servers and can filter/block risky content. Custom keyword rules support multiple languages. The common flagged-word lists and the spam-content filter are English-only in the current FAQ. | VERIFIED | S15 (updated 2026-06-15, post-cutoff) |
| CM-04 | 245 | Launch with limited posting surfaces, clear rules, a named human escalation path, AutoMod tested in the community's languages, anti-scam guidance and an incident log. | OPINION | synth 2026-10-21 [S14-S16] |
| CM-05 | 245 | Do not require Discord membership for essential support, patch information or age-appropriate rewards. Offer the same essentials in-game and through permitted Roblox surfaces. Collect structured bug/category feedback without asking for birthdays, IDs, school details or personal contacts. Keep moderation decisions separate from marketing popularity. Staff must not solicit private conversations with minors as a growth tactic. | OPINION | synth [S14-S16] |
| CM-06 | 249 | Discord's launch of 2026-05-28 (updated 2026-06-02) advertises Social SDK integrations for major Roblox games: account-linked access, Rich Presence and invites. It stresses authorization and revocation. | VERIFIED | S17 (2026-05-28; updated 2026-06-02) |
| CM-07 | 251 | Roblox staff's notice of 2026-06-02 prohibits cross-platform user profiling/tracking, unauthorized sharing, and circumvention of Roblox privacy settings. It warns against tools that publicly export live statuses, friend lists or play history, and separates compliant authentication and private/internal tools from those. User IDs and usernames count as protected user information in this notice. | VERIFIED | S18 (2026-06-02, post-cutoff) |
| CM-08 | 253 | The two sources differ materially in emphasis. Vendor authorization does not make every feature Roblox-compliant. The agent must not ship cross-platform presence, user matching or moderation-data synchronization only because a successful studio appears in a vendor launch. Require a current Roblox-policy and privacy review of each data flow, not just an OAuth consent screen. No SDK implementation is authorized by the paper. | OPINION | synth 2026-10-21 [S17, S18] |
| CM-09 | 255 | Medal reports clips created/shared of: Untitled Boxing Game 147K/28K, War Tycoon 319K/181K, BloxStrike 449K/213K. No time window, unique-creator count, spend or downstream retention is given. Medal's Sol's RNG page labels its activation figures as estimates, not completed growth. | EXPERIENCE | C04, C05 (both undated vendor pages) |
| CM-10 | 255 | Highlight sharing is an activity measure until acquisition and player quality are measured separately. | OPINION | synth [C04, C05] |
| CM-11 | 257 | Non-Roblox example: Brawl Stars' Thumbs Up For Brawl combined an in-game action, shared progress, milestone rewards and positive social submissions. The 10 billion pin uses was an announced target, not measured participation. | VERIFIED | N04 (2024-06-10) |
| CM-12 | 257 | Borrow a playable shared activity. Do not borrow the target, and do not assume the same giveaway mechanics are permitted. | OPINION | synth [N04] |

## 6. Number register (MP:117-263)

### 6.1 The paper's own "Rule / Number / Evidence mark / Source and date" rows (MP:149-153, 175-178, 217-220, 232-237, 259-262)

Rule column paraphrased. Evidence mark and source date kept as the paper writes them.

| ID | MP | Rule (paraphrase) | Number | Tag (paper's mark) | Src and date (paper's) |
| --- | --- | --- | --- | --- | --- |
| N-01 | 150 | Paid-ad guidance is not an organic algorithm boundary | Proposition within 3 seconds; hook within 6 | VERIFIED advice | S06 updated Jun 2025 |
| N-02 | 151 | Shorts maximum is not an optimum | Up to 3 minutes | VERIFIED | S03 accessed 21 Oct 2026 |
| N-03 | 152 | No invented universal posting quota | No minimum Shorts cadence | VERIFIED | S01 accessed 21 Oct 2026 |
| N-04 | 153 | Trial distribution is not randomized assignment | Optional auto-share uses first 72 hours | VERIFIED | S10 updated 26 Jun 2025 |
| N-05 | 176 | Ask for a campaign-specific quote | No reliable universal rate established | OPINION evidence limit | Review cutoff 21 Oct 2026 |
| N-06 | 177 | Preserve paid non-Roblox scope | CTR +107%; six-second VTR +65% | EXPERIENCE | S19 undated, accessed 21 Oct 2026 |
| N-07 | 178 | Disclose material relationships | No exemption because content is child-friendly | VERIFIED | P06 2023; S13 accessed 21 Oct 2026 |
| N-08 | 218 | Reported study medians are not forecasts | 14% play-session lift; 10% D7 retained-user lift | EXPERIENCE | P05 2 Oct 2026 |
| N-09 | 219 | Treat attributed earnings and incremental profit separately | No universal profitable CPP | OPINION | Studio accounting proposal 21 Oct 2026 |
| N-10 | 220 | Verify rollout in the account | Video support announced as forthcoming | VERIFIED announcement | P05 2 Oct 2026 |
| N-11 | 233 | Event capacity | 10 upcoming/ongoing | VERIFIED | D13 / accessed 2026-10-21 |
| N-12 | 234 | Trending Events criteria | at most 7 days since start; at least 1,000 RSVPs; public | VERIFIED eligibility, not guaranteed reach | D13 |
| N-13 | 235 | Update announcement ceiling | 60 characters; once per 3 days | VERIFIED | D13 |
| N-14 | 236 | Personalized notification ceiling | 1 per user per game per day; 13+ | VERIFIED | D15 |
| N-15 | 237 | Featuring notice conflict | Live docs 7 days; original post 14 | VERIFIED disagreement | D13/D14 |
| N-16 | 260 | Do not infer adulthood from community membership | Discord at least 13, up to 16 by country | VERIFIED | S14 22 Sep 2026 |
| N-17 | 261 | Review language coverage of moderation | Built-in wordlists and spam filter English-only | VERIFIED | S15 15 Jun 2026 |
| N-18 | 262 | Vendor integration is not platform-policy clearance | Per-data-flow review needed | OPINION from documented tension | S17 updated 2 Jun 2026; S18 2 Jun 2026 |

### 6.2 Other numbers that appear in the prose

Ads Manager settings numbers (13+, 18+, 1 ad credit, 10,000, 20,000, 30-180 days, 180+ days, 10 thumbnails, 16:9, 48 hours, the four attribution windows) are carried in full scope in AD-01 to AD-07. They are not repeated here.

| ID | MP | Value | Scope and limit (paper) | Tag | Src, date |
| --- | --- | --- | --- | --- | --- |
| N-19 | 121 | 90% of ad recall within six seconds | Older advertising research (studies 2021-2022). Not a 2026 experiment on Roblox clips. | VERIFIED | S22 (undated live) |
| N-20 | 127 | 15-, 30-, 60-second lengths | Named only to say there is no universal optimum among them. | OPINION | synth [S02, S03] |
| N-21 | 143 | 40% of creators posted more often; 80% of that subgroup saw more non-follower reach | Meta-reported, Trial Reels. The 80% is conditional on the 40% subgroup. Not a predicted lift. Not Roblox-specific. | EXPERIENCE | S11, 2025-06-12 |
| N-22 | 145 | 2023 watch-time denominator | Not presented as verified current in 2026; the Instagram Help page could not be read reliably. | OPINION | synth [S12] |
| N-23 | 147 | Six-second microtrailer from six one-second extracts | Steam product mechanic. Not a Roblox spec. | VERIFIED | N10 (undated live) |
| N-24 | 169 | CTR +107%; six-second VTR +65% (detail of N-06) | Clash Royale, creator-led paid creative, reported by TikTok. Budget, sample, dates, allocation undisclosed. Not Roblox organic. | EXPERIENCE | S19 (undated live) |
| N-25 | 173 | 51 public videos; 32 channels; posted 10-30 April 2026; 79,587 combined views; 2,534 likes observed 7 October | Catch the Drop. Public-video sample is a floor, not unique reach or attributable acquisition. Creator costs not disclosed. | EXPERIENCE | C06 (2026; measured 2026-10-07) |
| N-26 | 173 | 2M+ game visits; 92% like ratio | Catch the Drop. Reported separately from the public-video counts in N-25. Game totals are not campaign-attributable. | EXPERIENCE | C06 |
| N-27 | 195 | Nearly 30,000 games | Earnings access expansion, announced 2026-10-02. Eligibility decided in the interface. | VERIFIED | P05 (2026-10-02) |
| N-28 | 197 | 285 Robux | An old exchange rule. The paper says: never silently substitute it; no current fixed Robux-to-credit ratio is established by the reviewed sources. | OPINION | synth [P01-P05] |
| N-29 | 201 | 21 campaigns, all with incremental plays | Roblox-reported randomized studies. Not a forecast. | EXPERIENCE | P05 (2026-10-02) |
| N-30 | 201 | USD $250/day; 277% return | Ink Game, Earnings spotlight. Not a launch budget, typical payout, universal CPI or audited proof; no net-profit inference. | EXPERIENCE | P05 |
| N-31 | 207 | USD $0.0038 | DevEx standard rate, eligible Earned Robux after 2025-09-05 10:00 PT. Conditional rate, not a retail price. | VERIFIED | P16 |
| N-32 | 207 | USD $0.0035 | DevEx rate for earlier balances. | VERIFIED | P16 |
| N-33 | 207 | USD $0.0054 | DevEx rate, eligible U.S. 18+, from 2026-06-08. Do not apply to all receipts. | VERIFIED | P16 |
| N-34 | 226 | 14 days; 1920×1080 plus 1080×1920 or 4000×4000 layered PSD | Original 2025-12-10 pilot announcement. Conflicts with current 7-day documentation. | VERIFIED | D14 (2025-12-10) |
| N-35 | 226 | three-to-five selected holiday events | The old pilot's selection size. Not current capacity. | OPINION | synth [D14] |
| N-36 | 228 | 100 aggregate impressions; 100 per notification | Dashboard thresholds for summary and itemized stats. | VERIFIED | D15 |
| N-37 | 255 | Boxing Game 147K/28K; War Tycoon 319K/181K; BloxStrike 449K/213K | Medal, clips created/shared. No window, unique creators, spend or retention. Sol's RNG figures are labeled estimates. | EXPERIENCE | C04, C05 |
| N-38 | 257 | 10 billion pin uses | Brawl Stars announced target. Not measured participation. | VERIFIED | N04 (2024-06-10) |

## 7. Source ids used in lines 117-263 (resolved from MP:529-1164)

Quotes are the register's own, 15 words or fewer (some register quotes were cut to fit and are marked "cut"). "acc" = accessed by the paper (2026-10-21 for every entry). "Used for" gives the paper's tag when it cites the source. Cutoff flag: see section 0.

| ID | Source | Date and limits | URL | MP (register) | Used for (tag) | Key quote (register, attributed) | Cutoff flag |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C04 | Medal, "Medal for Roblox Developers - Grow Your Game" | undated vendor page; acc | https://medal.tv/developer/roblox | 869-875 | EXPERIENCE | "Incentivize players to clip and post their best moments in your game" | undated live |
| C05 | Medal x Sol's RNG partnership page | undated vendor page; acc | https://medal.tv/developer/roblox/solsrng | 877-883 | EXPERIENCE | "Estimated growth with a single activation" | undated live |
| C06 | Petrex, "Catch the Drop Roblox Case Study" | 2026; acc (paper text: measurements 2026-10-07) | https://petrex.io/work/samsung-galaxy-store | 885-891 | EXPERIENCE | "traffic attributable to individual campaigns requires separate reporting" | post-cutoff (measured 2026-10-07) |
| D13 | Roblox Creator Docs, "Experience events and updates" | undated live; acc | https://create.roblox.com/docs/production/promotion/experience-events | 629-635 | VERIFIED | "you can publish a maximum of 10 ongoing or upcoming events" | undated live |
| D14 | Roblox DevForum, "Introducing Off-Platform Featuring for Creator Events" | 2025-12-10 | https://devforum.roblox.com/t/introducing-off-platform-featuring-for-creator-events/4142230 | 637-643 | VERIFIED | "must be submitted at least 14 days prior to the event start date" (cut) | pre |
| D15 | Roblox Creator Docs, "Experience notifications" | undated live; acc | https://create.roblox.com/docs/production/promotion/experience-notifications | 645-651 | VERIFIED | "delivery of notifications is not guaranteed" | undated live |
| N04 | Supercell, "Thumbs Up For Brawl Community Event!" | 2024-06-10 | https://supercell.com/en/games/brawlstars/blog/community/thumbs-up-for-brawl-community-event/ | 1093-1099 | VERIFIED | "it adds to the tracker bar and you get rewards" (cut) | pre |
| N10 | Steamworks, "Trailers" | undated live; acc | https://partner.steamgames.com/doc/store/trailer | 1141-1147 | VERIFIED | "the first trailer you list on your store page is primarily gameplay" | undated live |
| P01 | Roblox Creator Docs, "Ads Manager" | undated living; acc | https://create.roblox.com/docs/production/promotion/ads-manager | 693-699 | VERIFIED | "The payment method cannot be changed after a campaign is published." | undated live |
| P02 | Roblox DevForum, "Leveling Up Ads Manager With New Features", staff reply 151 | 2025-04-09 | https://devforum.roblox.com/t/leveling-up-ads-manager-with-new-features/3587640/151 | 701-707 | VERIFIED | "there's no need to set a manual bid" | pre |
| P03 | Roblox DevForum, "Ads Manager Updates: Maximize Earnings, Attribution Updates, New Tile in Beta, Other Updates" | 2026-05-07 | https://devforum.roblox.com/t/ads-manager-updates-maximize-earnings-attribution-updates-new-tile-in-beta-other-updates/4623762/1 | 709-715 | VERIFIED | "we have updated our attribution logic" | pre |
| P04 | Roblox DevForum, "Roblox Kids and Select Global Launch: Upcoming Updates to Eligibility, Ads Manager, and Expedited Review" | 2026-06-16 | https://devforum.roblox.com/t/roblox-kids-and-select-global-launch-upcoming-updates-to-eligibility-ads-manager-and-expedited-review/4685717 | 717-723 | VERIFIED | "A new Engagement Objective beta in Creator Ads Manager" | post-cutoff |
| P05 | Roblox DevForum, "Ads Manager RDC Recap: Earnings, ROAS Reporting, & Incrementality" | 2026-10-02 | https://devforum.roblox.com/t/ads-manager-rdc-recap-earnings-roas-reporting-incrementality/4909790/1 | 725-731 | EXPERIENCE (21-campaign studies, Ink Game); VERIFIED (Earnings access, ROAS reporting, video-support announcement) | "All 21 campaigns brought incremental plays." | post-cutoff |
| P06 | FTC, "FTC's Endorsement Guides: What People Are Asking" | 2023 revision | https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking | 733-739 | VERIFIED | "rests with the influencer and the brand" (cut; register quote is longer) | pre |
| P07 | YouTube Help blog, "Giving you tools to easily disclose paid partnerships with new controls & automated disclosures" | 2026-09-03 | https://support.google.com/youtube/blog/458476782/giving-you-tools-to-easily-disclose-paid-partnerships-with-new-controls-automated-disclosures | 741-747 | VERIFIED | "Granular age & geographic controls for branded content" | post-cutoff |
| P08 | YouTube Help, "Add branded content restrictions & disclosure labels" | undated living; acc | https://support.google.com/youtube/answer/154235 | 749-755 | VERIFIED | "selecting the paid promotion button in your video details" | undated live |
| P09 | TikTok Support, "Promoting a brand, product, or service" | undated living; acc | https://support.tiktok.com/en/business-and-creator/creator-and-business-accounts/promoting-a-brand-product-or-service | 757-763 | VERIFIED | "you must turn on the content disclosure setting" | undated live |
| P10 | Roblox DevForum, "Ads Manager Updates: Acquire New Users, Continuous Campaigns and More" | 2025-08-05 | https://devforum.roblox.com/t/ads-manager-updates-acquire-new-users-continuous-campaigns-and-more/3862159 | 765-771 | VERIFIED | "Ad thumbnails will soon automatically optimize based on user engagement" | pre |
| P16 | Roblox Help, "Developer Exchange - Help and Information Page" | undated living guidance; acc; rate effective dates 2025-09-05 and 2026-06-08 | https://en.help.roblox.com/hc/en-us/articles/13061189551124-Developer-Exchange-Help-and-Information-Page | 813-819 | VERIFIED | "This rate is effective as of June 8, 2026" | undated live; holds a post-cutoff effective date (2026-06-08) |
| S01 | YouTube Help, "Search and discovery tips: Shorts" | undated; acc | https://support.google.com/youtube/answer/11914225?hl=en | 893-899 | VERIFIED | "There is no minimum posting cadence required for your videos to perform well." | undated live |
| S02 | YouTube Help, "YouTube performance FAQ & Troubleshooting" | undated; acc | https://support.google.com/youtube/answer/141805?hl=en | 901-907 | VERIFIED | "Publish time is not known to impact a video's long-term performance." | undated live |
| S03 | YouTube Help, "Get started creating YouTube Shorts" | undated; change effective 2025-03-31; acc | https://support.google.com/youtube/answer/10059070?hl=en | 909-915 | VERIFIED | "no minimum watch time requirement" | undated live |
| S06 | TikTok for Business, "Creative best practices for performance ads" | updated 2025-06; acc | https://ads.tiktok.com/resources/help/article/creative-best-practices?lang=en | 933-939 | VERIFIED | "Introduce your content proposition in the first 3 seconds for better recall and awareness." | pre |
| S07 | TikTok Support, "How TikTok recommends content" | undated; acc | https://support.tiktok.com/en/using-tiktok/exploring-videos/how-tiktok-recommends-content | 941-947 | VERIFIED | "How important each factor is can change over time." | undated live |
| S08 | TikTok Support, "Commercial use of music on TikTok" | undated; acc | https://support.tiktok.com/en/business-and-creator/creator-and-business-accounts/commercial-use-of-music-on-tiktok | 949-955 | VERIFIED | "don't cover the commercial use of music in content" (cut) | undated live |
| S10 | Meta, "Test Content With Non-Followers Using Trial Reels" | 2024-12-10; updated 2025-06-26 | https://about.fb.com/news/2024/12/trial-reels-try-content-non-followers-first-see-what-perfoms-best/ | 965-971 | VERIFIED | "Trial reels will be shown to non-followers first." | pre |
| S11 | Meta, "Inspiring Creativity That Brings People Together" | 2025-06-12; updated 2025-06-26 | https://about.fb.com/news/2025/06/inspiring-creativity-that-brings-people-together/ | 973-979 | EXPERIENCE | "40% of creators started posting reels more often" | pre |
| S12 | Meta, "Introducing Edits: A Streamlined Video Creation App" | 2025-04; updated 2025-12-17 | https://about.fb.com/news/2025/04/introducing-edits-streamlined-video-creation-app/ | 981-987 | VERIFIED | "export and post wherever you want with no added watermarks" | pre |
| S13 | YouTube Help, "YouTube Branded Content Policies" | undated; acc | https://support.google.com/youtube/answer/17596007?hl=en | 989-995 | VERIFIED | "you are ultimately responsible for ensuring your disclosure is clear and prominent." | undated live |
| S14 | Discord Support, "Why is Discord asking for my birthday?" | updated 2026-09-22 | https://support.discord.com/hc/en-us/articles/360040724612-Why-is-Discord-asking-for-my-birthday | 997-1003 | VERIFIED | "you must be at least 13 to use Discord" | post-cutoff |
| S15 | Discord Support, "AutoMod FAQ" | updated 2026-06-15 | https://support.discord.com/hc/en-us/articles/4421269296535-AutoMod-FAQ | 1005-1011 | VERIFIED | "AutoMod is currently available for all servers." | post-cutoff |
| S16 | Discord blog, "Safer for Teens, Same Discord for Adults" | 2026-09-22 | https://discord.com/blog/safer-for-teens-same-discord-for-adults | 1013-1019 | VERIFIED | "isn't shown on your profile or visible to other members in a server" (cut) | post-cutoff |
| S17 | Discord blog, "Official Discord Integrations for Steal a Brainrot, Grow a Garden, Brookhaven RP, and more" | 2026-05-28; updated 2026-06-02 | https://discord.com/blog/official-discord-integrations-for-steal-a-brainrot-grow-a-garden-brookhaven-rp-and-more | 1021-1027 | VERIFIED | "Users can deauthorize the experience at any time" | published pre, updated post-cutoff |
| S18 | Roblox DevForum, "A Reminder About User Privacy and Third-Party Integrations" | 2026-06-02 | https://devforum.roblox.com/t/a-reminder-about-user-privacy-and-third-party-integrations/4665118 | 1029-1035 | VERIFIED | "Creators may not track Roblox users across third-party platforms or services" | post-cutoff |
| S19 | TikTok for Business, "Learn How Clash Royale Drove Engagement with TikTok-Native Content" | undated; acc | https://ads.tiktok.com/business/en-US/inspiration/supercell-clash-royale-tiktok-one | 1037-1043 | EXPERIENCE | "Past performance does not guarantee or predict future performance." | undated live |
| S20 | Meta, "Making it Easier for Brands and Creators to Collaborate on Instagram" | 2024-02 | https://about.fb.com/news/2024/02/creator-marketplace-for-brands-and-creators-to-collaborate-on-instagram/ | 1045-1051 | VERIFIED | "Advertisers can boost organic Instagram content as partnership ads" | pre |
| S21 | YouTube Help, "Upload schedule tips: Shorts" | undated; acc | https://support.google.com/youtube/answer/13616979?hl=en | 1053-1059 | VERIFIED | "A consistent, sustainable release schedule is critical" | undated live |
| S22 | TikTok for Business, "Creative Best Practices for TikTok Ads" | undated; underlying studies 2021-2022; acc | https://ads.tiktok.com/business/en-US/blog/creative-best-practices-top-performing-ads | 1061-1067 | VERIFIED | "90% of ad recall impact is captured within the first six seconds" | undated live (studies 2021-2022) |

## 8. Claims for the fact-check

Priority: P1 = Roblox platform facts (Ads Manager settings, audiences, attribution windows, ad policy, age rules, events/announcement/notification limits, DevEx rates, ad integration prices). P2 = YouTube, TikTok, Instagram, Discord, FTC, Steam facts. P3 = case results. Check against the source at the id, not against the paper. Lines 117-263 hold no ad-integration prices and no Roblox ad-policy text (those sources P11-P13 are cited only outside this part). "Cutoff flag" as in section 0; check living pages for change since 2026-10-21.

### 8.1 P1: Roblox platform facts

| ID | Pri | Claim to check (paraphrase) | MP | Src | Src date | Cutoff flag | Why it matters |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FC-01 | P1 | Ads Manager access: advertiser age 13+, verified email; payment cards 18+; minimum conversion 1 ad credit; conversion irreversible. | 187 | P01 | undated live | undated live | Age gate and an irreversible money step go into any approval request. |
| FC-02 | P1 | Audiences: All; New = never / absent 180+ days; Recent = last 30 days, minimum 10,000; Lapsed = 30-180 days, minimum 20,000. Check the unit of the minimums and the exact wording of "never" and "last 30 days". | 189 | P01 | undated live | undated live | Decides which campaigns can run at all and how "resurrected" users are counted (AD-20). |
| FC-03 | P1 | Attribution windows: first-time users 30 days; last played under 7 days = clicked session only; absent 7-29 days = 7 days; absent 30+ days = 30 days. P03 (2026-05-07) says attribution logic was updated; confirm the table matches it. | 193 | P01, P03 | undated live; 2026-05-07 | undated live; pre | Every ROAS and join number depends on these windows. |
| FC-04 | P1 | Placement is automatic on Home and search (no manual placement). | 188 | P01 | undated live | undated live | Sets what the agent can promise about where an ad shows. |
| FC-05 | P1 | Targeting options: location, age, gender, genre, device, subject to audience eligibility. | 190 | P01 | undated live | undated live | Targeting by age touches ad-policy rules (see sources P12, outside this part). |
| FC-06 | P1 | Creatives: up to 10 thumbnails, 16:9, evenly distributed. | 191 | P01 | undated live | undated live | Even distribution vs engagement optimization changes how creative tests are read (FC-14). |
| FC-07 | P1 | Reporting: post-click processing can take 48 hours. | 192 | P01 | undated live | undated live | Sets the earliest honest read time for a campaign. |
| FC-08 | P1 | New Ads Manager uses fractional automated bidding; no manual bid; competitive demand can delay serving. Check which part comes from the staff reply and which from other docs. | 195 | P02 | 2025-04-09 | pre | Prevents old CPP-bid tutorials from being used (AD-12). |
| FC-09 | P1 | Earnings was introduced with revised attribution and user-reporting segments. | 195 | P03 | 2026-05-07 | pre | Date and scope of the Earnings objective and the new segments. |
| FC-10 | P1 | Engagement objective: "launched" (paper) versus "beta" (register quote); purpose is reaching highly engaged players for Kids/Select eligibility. | 195, 197 | P04 | 2026-06-16 | post-cutoff | Status (beta or live) and purpose decide whether the agent may propose it. |
| FC-11 | P1 | Earnings access expanded to nearly 30,000 games; eligibility is decided in the interface. | 195 | P05 | 2026-10-02 | post-cutoff | Tells whether this studio's game can use Earnings; do not promise it. |
| FC-12 | P1 | ROAS reporting includes Creator Rewards, Immersive Ads and Rewarded Video earnings; earnings converted to USD with rate differences; estimated ROAS is a forecast while earnings accrue. | 203 | P05 | 2026-10-02 | post-cutoff | Basis of the two-ledger accounting (AD-17). |
| FC-13 | P1 | Sponsored Tile video support announced as arriving "in coming weeks"; the current setup document still describes thumbnails. Check whether video is live now. | 215 | P05, P01 | 2026-10-02; undated live | post-cutoff | Stops an announcement from being sold as availability (AD-24). |
| FC-14 | P1 | Creative delivery: P01 says even distribution; P10 promised engagement-based optimization of ad thumbnails. Check which is current. | 213 | P01, P10 | undated live; 2025-08-05 | undated live; pre | Decides whether an A/B creative comparison is valid. |
| FC-15 | P1 | No universal minimum daily spend, maximum account spend or fixed Robux-to-credit ratio exists in the docs; the old "285 Robux" rule must not be used. Check the live purchase preview and docs for any of these now. | 197 | P01-P05 | mixed | mixed | If a fixed ratio or minimum exists now, AD-13 is wrong. |
| FC-16 | P1 | DevEx standard rate for eligible Earned Robux after 2025-09-05 10:00 PT is USD $0.0038; earlier balances $0.0035. | 207 | P16 | undated live; effective 2025-09-05 | undated live | Money conversion in the incremental ledger. |
| FC-17 | P1 | Eligible U.S. 18+ DevEx rate is USD $0.0054 from 2026-06-08. Check eligibility conditions. | 207 | P16 | undated live; effective 2026-06-08 | undated live; effective date post-cutoff | The paper warns not to apply the premium rate to all receipts. |
| FC-18 | P1 | Events: Creator Hub, Engagement, Events & Updates; up to ten ongoing/upcoming events. | 224, 233 | D13 | undated live | undated live | Capacity limit for any event calendar. |
| FC-19 | P1 | Trending Events: public active event, started within 7 days, at least 1,000 RSVPs; sort uses game DAU. | 224, 234 | D13 | undated live | undated live | Eligibility rules; the paper says eligibility is not guaranteed reach. |
| FC-20 | P1 | Update announcements: 60 characters maximum; once per 3 days; delivered to opted-in players; reports show views, visit rate, unfollow rate; old-form workflow during consolidation. | 224, 235 | D13 | undated live | undated live | Hard text and cadence ceiling for update messages. |
| FC-21 | P1 | Off-platform featuring: current docs say submit at least 7 days ahead; selection not automatic; original post said 14 days. Check the live submission form. | 224, 226, 237 | D13, D14 | undated live; 2025-12-10 | undated live; pre | The paper plans a 14-day buffer because the two sources disagree. |
| FC-22 | P1 | Off-platform featuring pilot: channels App Store, Google Play, Roblox; art 1920×1080 plus 1080×1920, or 4000×4000 layered PSD. | 226 | D14 | 2025-12-10 | pre | Art spec for event submissions, if still current. |
| FC-23 | P1 | The old pilot selected three to five holiday events (the register quote does not show this). Check the number in D14 and that it is not current capacity. | 226 | D14 | 2025-12-10 | pre | Prevents a promise based on an old pilot size. |
| FC-24 | P1 | Personalized experience notifications: opted-in users aged 13+; one per user per day per experience; aggregate throttles and spam prevention can still block delivery. | 228, 236 | D15 | undated live | undated live | Hard ceiling and age gate for return messages. |
| FC-25 | P1 | Notification dashboard needs 100 aggregate impressions for summary and 100 per notification for itemized stats; CTR = clicks / impressions; dismiss and turn-off rates use impressions. | 228 | D15 | undated live | undated live | Decides when the agent may read a test result. |
| FC-26 | P1 | Opted-in total can include under-13 users eligible for update notices but not personalized notifications; new strings recommended for variants; category segments analytics. | 228 | D15 | undated live | undated live | Stops a wrong reach estimate and wrong variant setup. |
| FC-27 | P1 | Roblox staff notice of 2026-06-02: bans cross-platform user profiling/tracking, unauthorized sharing and circumvention of privacy settings; warns about public export of live statuses, friend lists, play history; user IDs and usernames are protected information; compliant authentication and private/internal tools are distinguished. | 251 | S18 | 2026-06-02 | post-cutoff | Controls what the agent may do with any Discord or SDK link (CM-08). |

### 8.2 P2: YouTube, TikTok, Instagram, Discord, FTC, Steam

| ID | Pri | Claim to check (paraphrase) | MP | Src | Src date | Cutoff flag | Why it matters |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FC-28 | P2 | YouTube Shorts recommendation signals (choose to watch, stay, average view duration, average percentage viewed, likes, post-watch surveys); no universal winning percentage or mandatory format. | 119 | S01 | undated live | undated live | Basis for not giving a duration target. |
| FC-29 | P2 | TikTok recommendation factors (watch/skip, likes, shares, comments, sounds, hashtags, context); for most users, watch time weighs more; weights can change. | 119 | S07 | undated live | undated live | Basis for the "no formula" stance. |
| FC-30 | P2 | TikTok June 2025 performance-ad guidance: proposition in first 3 seconds, hook within 6, contextual captions. The register quote shows only the 3-second statement; check the 6-second and caption statements. | 121 | S06 | 2025-06 | pre | The only numeric hook guidance in the part. |
| FC-31 | P2 | The 90% ad-recall-in-six-seconds claim is on a TikTok ads page and rests on 2021-2022 studies. | 121 | S22 | undated live; studies 2021-2022 | undated live | Prevents this old claim from being used as a 2026 Roblox fact. |
| FC-32 | P2 | Shorts can be up to 3 minutes; YouTube advises matching length to content and using absolute plus relative watch time. The S03 register quote covers a different statement (no minimum watch time); check the 3-minute limit on the page. | 125, 151 | S03, S02 | undated live; change effective 2025-03-31 | undated live | Maximum length affects edit plans. |
| FC-33 | P2 | TikTok recommends its Commercial Music Library for promotion; licenses outside it do not cover commercial use. | 129 | S08 | undated live | undated live | Music clearance rule for paid and creator content. |
| FC-34 | P2 | YouTube: no minimum cadence; publish time not known to affect long-term performance; audience-active times matter for Live/Premiere; consistency recommended. | 135, 152 | S01, S02, S21 | undated live | undated live | Basis for "no invented quota". |
| FC-35 | P2 | Trial Reels go to non-followers first; optional auto-share decision uses views in the first 72 hours. The register quote shows only the non-follower part; check the 72-hour statement. | 141, 153 | S10 | 2024-12-10; updated 2025-06-26 | pre | Number 72 hours is a product detail. |
| FC-36 | P2 | Meta: 40% of creators posted more after trying Trial Reels; 80% of that subgroup saw more non-follower reach. | 143 | S11 | 2025-06-12; updated 2025-06-26 | pre | Easy to misread the conditional 80% (N-21). |
| FC-37 | P2 | Edits app: editing, watermark-free export, feedback such as skip rate that can affect distribution. Check the "can affect distribution" statement. | 145 | S12 | 2025-04; updated 2025-12-17 | pre | Basis for using it as a diagnostic only. |
| FC-38 | P2 | Instagram's current insight labels (the 2023 watch-time denominator). The paper could not read the page; no source id. Check the live Instagram Help insights page. | 145 | none (paper limit) | n/a | n/a | Avoids copying an unverified formula. |
| FC-39 | P2 | Steam: first trailer mostly gameplay; player-perspective gameplay early; check without sound; six-second microtrailer from six one-second extracts. The register quote covers only the first-trailer statement. | 147 | N10 | undated live | undated live | Non-Roblox craft source; check each detail. |
| FC-40 | P2 | FTC (2023 guidance): disclose unexpected material connections; platform tools not automatically sufficient; disclosure inside video, visual and audible; brands train and monitor endorsers. | 159 | P06 | 2023 revision | pre | Legal basis of creator briefs; U.S. only. |
| FC-41 | P2 | YouTube (2026-09-03): refreshed branded-content disclosures, age/geographic controls, automated detection; sponsored content declared in paid-promotion setting. | 161 | P07, P08 | 2026-09-03; undated live | post-cutoff; undated live | New feature set after the model cutoff. |
| FC-42 | P2 | TikTok: commercial-content disclosure for own business and compensated third-party promotion, with distinct labels; tagging a brand partner can grant ad authorization. The register quote shows only the disclosure-setting statement. | 161 | P09 | undated live | undated live | Disclosure and reuse rights are separate. |
| FC-43 | P2 | YouTube: branded-content declaration required; branded-content videos are removed from YouTube Kids. The register quote shows only the disclosure-responsibility statement. | 171, 178 | S13 | undated live | undated live | Blocks the "child-friendly creator" workaround. |
| FC-44 | P2 | Meta supports partnership ads for eligible creator content. | 171 | S20 | 2024-02 | pre | Separates reuse rights from price and access. |
| FC-45 | P2 | Discord: minimum age at least 13, up to 16 by country; September 2026 adult/teen/unconfirmed groups; teen protections (non-friend DMs to requests; limits on adult content/settings); age group not visible to other server members. | 241, 260 | S14, S16 | 2026-09-22 | post-cutoff | Community plan cannot assume adult members. |
| FC-46 | P2 | AutoMod available to all servers; custom keywords support multiple languages; common flagged-word lists and spam filter English-only. | 243, 261 | S15 | updated 2026-06-15 | post-cutoff | Moderation coverage gap for non-English communities. |
| FC-47 | P2 | Discord 2026-05-28 launch (updated 2026-06-02): Social SDK integrations for major Roblox games with account-linked access, Rich Presence and invites; authorization and revocation stressed. | 249 | S17 | 2026-05-28; updated 2026-06-02 | updated post-cutoff | One side of the Roblox/Discord conflict (X-30). |

### 8.3 P3: case results

| ID | Pri | Claim to check (paraphrase) | MP | Src | Src date | Cutoff flag | Why it matters |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FC-48 | P3 | Roblox-reported randomized studies: 21 campaigns, all with incremental plays; median lift 14% (play sessions) and 10% (D7 retained users). Check the exact metric names and "median". | 201, 218 | P05 | 2026-10-02 | post-cutoff | Highest-weight result number; easy to misquote as a forecast. |
| FC-49 | P3 | Ink Game: USD $250/day and 277% return in the Earnings spotlight. | 201 | P05 | 2026-10-02 | post-cutoff | Large return figure with no cost accounting. |
| FC-50 | P3 | Clash Royale: creator-led paid creative lifted CTR 107% and six-second VTR 65%; budget, sample and dates undisclosed. | 169, 177 | S19 | undated live | undated live | Non-Roblox paid creative; check the metric names. |
| FC-51 | P3 | Catch the Drop: 51 videos, 32 channels, posted 10-30 April 2026, 79,587 views, 2,534 likes on 7 October; 2M+ visits; 92% like ratio. The URL slug ("samsung-galaxy-store") does not match the case title; confirm the page. | 173 | C06 | 2026; measured 2026-10-07 | post-cutoff | Many exact numbers; page identity unclear from the URL. |
| FC-52 | P3 | Medal clip counts (created/shared): Untitled Boxing Game 147K/28K, War Tycoon 319K/181K, BloxStrike 449K/213K; Sol's RNG figures labeled estimates. Check which number is "created" and which "shared". | 255 | C04, C05 | undated live | undated live | Vendor-reported; no window or retention. |
| FC-53 | P3 | Brawl Stars: 10 billion pin uses was an announced target; rewards tied to shared progress. | 257 | N04 | 2024-06-10 | pre | Non-Roblox; target is not a result. |

## 9. Contradictions and limits

### 9.1 Where the paper says its sources qualify each other

| ID | MP | Item | Handling for skills |
| --- | --- | --- | --- |
| X-01 | 121, 150 | TikTok's 3-second / 6-second advice is for paid performance ads, not an organic algorithm boundary. | Use 3 seconds as an internal review checkpoint only (SV-08). Never say "the algorithm cuts off at 3 seconds". |
| X-02 | 121 | The "90% recall in 6 seconds" claim comes from older ad research (2021-2022), not a 2026 Roblox test. | Do not quote it as a current Roblox fact. |
| X-03 | 125, 151 | YouTube's 3-minute Shorts maximum is not an ideal length. | Compare edit lengths on the real clip. |
| X-04 | 135 | YouTube's "no minimum cadence" and "publish time not known to matter" versus "consistency is recommended" are about different outcomes, not rival rules. | Give a sustainable cadence, no quota (SV-14). |
| X-05 | 137 | No substantiated universal Roblox posting hour or posts-per-day number exists in the reviewed primary sources. | Do not cite generic best-time tables. |
| X-06 | 141, 153 | Trial Reels is a product capability. It is not a randomized A/B test. | Do not read Trial Reels results as an experiment. |
| X-07 | 143 | The 80% figure applies only to the 40% subgroup. | Never say "80% of creators". |
| X-08 | 145 | Instagram's current insight page could not be read. The 2023 watch-time denominator is not verified for 2026. | Read the account's own metric labels first. |
| X-09 | 147 | The Steam trailer rules and the six-second microtrailer are not Roblox specifications. | Transfer playable proof and sound-off clarity only. |
| X-10 | 159 | FTC guidance is U.S. guidance, not assurance elsewhere. Platform disclosure tools are not automatically enough. | Add jurisdiction review; disclose inside the video. |
| X-11 | 161 | Disclosure (a platform label) and reuse/advertising authorization (for example, tagging a brand partner on TikTok) are different things. | Keep them as separate lines in the brief. |
| X-12 | 163 | No universal legal minimum creator age; account eligibility does not prove contractual capacity. | Adult/representative plus jurisdiction review; do not invent a minimum age. |
| X-13 | 165, 176 | No defensible universal Roblox creator fee, CPM, cost per acquired player or conversion rate; an unpublished quote is not a benchmark. | Ask for a written quote per campaign; never state a market rate. |
| X-14 | 167 | Link sharing, manual searchers, existing-player overlap and simultaneous updates all limit creator attribution. | Distinct links, bounded trial, aggregate reports. |
| X-15 | 169, 177 | The Clash Royale numbers are non-Roblox, paid creative, with budget, sample, dates and allocation undisclosed. | Do not use as a Roblox forecast. |
| X-16 | 173 | Catch the Drop public-video counts are a floor, not unique reach or attributable acquisition. Creator costs were not disclosed. | Keep deliverables, public counts and game totals apart (CR-13). |
| X-17 | 197 | No universal minimum daily spend, maximum account spend or current Robux-to-credit ratio was established. Pre-2025 manual CPP-bid tutorials are out of date. | Read the live purchase preview; never use "285 Robux". |
| X-18 | 201, 218 | Study medians (14%, 10%) are Roblox-reported results, not forecasts. Ink Game's $250/day and 277% are not a budget, payout, CPI or audited profit proof. | Quote with scope; never use as a plan. |
| X-19 | 203 | Estimated ROAS is a forecast while earnings accrue. | Wait for cohort maturity before judging (AD-20). |
| X-20 | 205, 219 | Platform-attributed ROAS and studio incremental contribution are different ledgers. No universal profitable CPP. Gross Robux spending is not comparable to a USD media bill. | Keep two ledgers (AD-17). |
| X-21 | 207 | DevEx rates are conditional and are not retail Robux prices or guaranteed cash-out approval. | Do not use the premium U.S. 18+ rate for all receipts. |
| X-22 | 209 | Attribution is not incrementality. A before/after rise cannot allocate causality. Several channels' attributed revenues may overlap. | Use a randomized holdout when available. |
| X-23 | 213 | P01 (even distribution) versus P10 (engagement-based optimization): delivery logic is unresolved. | Do not assume creative comparisons are randomized. |
| X-24 | 215, 220 | The October announcement of Sponsored Tile video versus the current thumbnails-only setup doc. An announcement is not universal availability. | Confirm in the specific account; allow for moderation time. |
| X-25 | 226, 237 | Off-platform featuring: current docs say 7 days; the original announcement said 14. The old pilot's three-to-five selected events is not current capacity. | Use 7 as the documented minimum; plan a 14-day buffer; no promise from eligibility. |
| X-26 | 228 | Update announcements (60 characters, once per 3 days) and personalized notifications (1 per day, 13+) are different channels. The opted-in total can include users who cannot get personalized notifications. | Never merge their limits; measure reach from impressions. |
| X-27 | 230 | A tool's sending ceiling is not a recommended content cadence. | Tie each message to a real reason to return. |
| X-28 | 241 | Community membership or Roblox account linking does not prove adulthood. Discord's age group is hidden from other members. | No adult-only content or rewards based on membership. |
| X-29 | 243, 261 | Discord AutoMod built-in wordlists and the spam filter are English-only. | Test in the community's languages. |
| X-30 | 249-253, 262 | Discord's vendor launch (S17) and Roblox's privacy notice (S18) differ materially. OAuth consent is not Roblox-policy clearance. No SDK implementation is authorized by the paper. | Per-data-flow Roblox policy and privacy review; the owner decides. |
| X-31 | 255 | Medal clip counts have no time window, unique creators, spend or retention. Sol's RNG figures are estimates. | Highlight sharing is activity, not acquisition. |
| X-32 | 257 | 10 billion pin uses was a target, not measured participation. | Borrow the activity, not the target. |

### 9.2 Extractor notes: gaps between the paper's text and its register (not the paper's own limits)

These come from reading the register quote against the sentence it backs. A short register quote usually anchors one part of a source, not every claim. The fact-checker opens the URL.

| ID | MP | Note | Handling |
| --- | --- | --- | --- |
| X-33 | 125, 151 | S03's register quote (no minimum watch time) does not show the 3-minute Shorts maximum the paper cites it for. | Check FC-32 on the page. |
| X-34 | 121, 150 | S06's register quote shows the 3-second statement only; the 6-second hook and caption statements are not in the quote. | Check FC-30. |
| X-35 | 141 | S10's register quote shows "non-followers first" only; the 72-hour auto-share detail is not in the quote. | Check FC-35. |
| X-36 | 171, 178 | S13's register quote is about disclosure responsibility; the YouTube Kids removal is not in the quote. | Check FC-43. |
| X-37 | 195 | P04 is described as "launched" in the paper, but the register quote calls the Engagement objective a "beta". | Check FC-10; report which status the live page shows. |
| X-38 | 224-228 | D13, D14 and D15 register quotes anchor only one fact each (10 events; 14 days; delivery not guaranteed). Most limits in section 4 (7 days, 1,000 RSVPs, 60 characters, 100 impressions) are not in the quotes. | Check FC-18 to FC-26 on the live pages. |
| X-39 | 207 | P16's register quote shows only the 2026-06-08 effective date; the dollar rates and the 2025-09-05 10:00 PT time are not in the quote. | Check FC-16, FC-17. |
| X-40 | 173 | C06's URL slug names a different case ("samsung-galaxy-store") than the case title. | Confirm the page content in FC-51. |
| X-41 | 119, 135 | Several source ids (S01, S02, S03, S07, S08, S13, S19, S21, S22) are undated living pages. Their content on a later date may differ. | Re-read before quoting; keep "acc 2026-10-21". |

## 10. Coverage map (check C1)

Every paragraph and table row of MP:117-263 maps to at least one row. Heading lines and table header lines carry no claim of their own. No line was skipped.

| MP lines | Covered by |
| --- | --- |
| 117 (heading) | structure only |
| 119 | SV-01, SV-02, SV-03 |
| 121 | SV-04, SV-05, N-19 |
| 123 | SV-08, SV-09 |
| 125 | SV-06 |
| 127 | SV-10, SV-11, N-20 |
| 129 | SV-07 |
| 131 | SV-12 |
| 133, 139 (headings) | structure only (sections 1.3, 1.4) |
| 135 | SV-13 |
| 137 | SV-14, SV-15 |
| 141 | SV-16 |
| 143 | SV-17, N-21 |
| 145 | SV-18, SV-19, N-22 |
| 147 | SV-20, SV-21, N-23 |
| 149-153 | N-01 to N-04 |
| 155 (heading) | structure only |
| 157 | CR-01, CR-02 |
| 159 | CR-03 |
| 161 | CR-04, CR-05 |
| 163 | CR-06 |
| 165 | CR-07 |
| 167 | CR-08 |
| 169 | CR-09, N-24 |
| 171 | CR-10, CR-11 |
| 173 | CR-12, CR-13, N-25, N-26 |
| 175-178 | N-05 to N-07 |
| 180, 182, 199, 211 (headings) | structure only (sections 3.1 to 3.4) |
| 184-193 | AD-01 to AD-07 |
| 195 | AD-08 to AD-11, N-27 |
| 197 | AD-12, AD-13, N-28 |
| 201 | AD-14, AD-15, N-29, N-30 |
| 203 | AD-16 |
| 205 | AD-17, AD-18 |
| 207 | AD-19, N-31 to N-33 |
| 209 | AD-20 |
| 213 | AD-21, AD-22 |
| 215 | AD-23, AD-24 |
| 217-220 | N-08 to N-10 |
| 222, 239, 247 (headings) | structure only |
| 224 | UP-01 to UP-04 |
| 226 | UP-05, UP-06, N-34, N-35 |
| 228 | UP-07 to UP-09, N-36 |
| 230 | UP-10, UP-11 |
| 232-237 | N-11 to N-15 |
| 241 | CM-01, CM-02 |
| 243 | CM-03 |
| 245 | CM-04, CM-05 |
| 249 | CM-06 |
| 251 | CM-07 |
| 253 | CM-08 |
| 255 | CM-09, CM-10, N-37 |
| 257 | CM-11, CM-12, N-38 |
| 259-262 | N-16 to N-18 |
| 1-15 (evidence method) | section 0 (Central rule, Editorial method, Tag) |

Counts: SV 21, CR 13, AD 24, UP 11, CM 12, N 38, FC 53, X 41, sources 38.
