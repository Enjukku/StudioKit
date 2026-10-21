---
type: reference
scope: universal
status: active
updated: 2026-10-20
source: "owner-supplied research paper 'Game_UI_UX_Research_AI_Designer.txt' (ChatGPT, research date 2026-10-21), lines 1-440, J002"
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-20

# UX research, part A (paper lines 1-440): rules, numbers, templates, gaps

Reading rule for a skill that uses this file: keep the tag next to every claim. A row tagged OPINION or EXPERIENCE is never a rule of the platform and never a measured result. UNSPECIFIED means "the paper has no value"; it is not zero and not a default. Cite as `RP:<line>` plus the paper's own ids, e.g. `RP:220 [P02]`.

## 1. Source card

| field | value |
| --- | --- |
| What it is | "Game UI and UX Research for an AI Designer": industry craft for playful, mobile-first games with Roblox platform constraints (RP:1-4) |
| Author | ChatGPT (owner-supplied); an AI-written synthesis that cites named, dated sources |
| Research date | current to 21 October 2026 (RP:4) |
| This file covers | RP:1-440: 15 headline rules, tag meanings, sections 1-8 up to (not including) motion record "01 Ready check acceptance entrance". Part B covers the rest and the source register |
| Trust note | The tags are the paper's own. Keep the tag with the claim. The paper says a tag verifies the stated finding or rule, not universal effectiveness (RP:38) |
| Not covered by the paper | Luau or engine implementation (RP:40). It is a designer's reference |
| Why the tags matter | A screenshot reading is OPINION even when the screenshot is authentic: it cannot show intention, timing or a retention effect (RP:40) |

Tag meanings (RP:38), reproduced in my words:

| tag | meaning | do not read it as |
| --- | --- | --- |
| VERIFIED | A published measurement, inspectable artifact, official feature, policy or guideline | Proof that the thing works for every game |
| EXPERIENCE | A firsthand studio or practitioner account; public methods are limited | A controlled study |
| OPINION | The paper's own interpretation or proposed adaptation | An observed outcome |
| UNSPECIFIED | A missing parameter | Zero, or a default, or a secret studio preset |

Source ids as they are used inside RP:1-440 (the dated register is in part B; role below is read from how the text uses the id; an id not described in RP:1-440 is marked "not described here"):

| id | role in RP:1-440 |
| --- | --- |
| C01 | Supercell, Antti Summala, Brawl Stars design account (EXPERIENCE) |
| C02 | Supercell 2026 account (dated 2026-07-10): Android startup time, startup logo, Brawl Stars loading |
| C03 | Brawl Stars landscape phone screenshot (undated, promotional) |
| C04 | Matheus Knebel, Candy Crush overhaul account 2019-20 |
| C05 | Clash Royale June 2025 patch notes |
| C06 | Clash Royale May 2026 Collection Levels note |
| C07 | Clash Royale portrait promotional screenshot |
| C08 | Monument Valley II, David Fernandez Huerta, GDC 2018 slides |
| C09 | Original Splatoon interview (squid silhouette) |
| C10 | Splatoon 3 Nintendo interview and screenshots |
| C11 | Splatoon 3 lobby (test range, ghosts) |
| C12 | Persona 5 official 2017 session description (Suto, Wada) |
| C13 | not described here (only in ranges "C12-C14", "C01-C14") |
| C14 | Atlus CEDEC slide photographs |
| U01 | Andersen et al., tutorial experiment, CHI 2012 |
| U02, U03 | Celia Hodent, Fortnite icon testing and HUD grouping (U03 = GDC 2016 per RP:306) |
| U04 | Naughty Dog, The Last of Us Part II accessibility (2020-06-09) |
| U05 | Bungie Destiny HUD account (2024-04-11) |
| U06, U07 | Riot VALORANT front-end redesign (Oct 2022); Patch 5.10 navigation restore (2022-11-15) |
| U08 | Valve, Mike Ambinder (Steam Dev Days 2014) |
| U10 | Ubisoft, QC vs user research and accessibility (2022-03-16) |
| U12, U13 | not described here (cited with U14 for text and hit area, RP:16, RP:225) |
| U14 | Xbox Accessibility Guideline on target size (updated 2026-03-04) |
| U15, U16 | XAG 112 and XAG 113 (RP:235) |
| U17 | cited for reduced motion (RP:397, RP:401); not described here |
| U18, U21 | not described here (U21 = translations per headline 14) |
| U23 | FTC order against Epic (2023-03-14 per matrix) |
| U24, U25 | Epic response; Epic support on cancellation |
| U26 | Hodent on health-bar colors (RP:170) |
| M01 | Riot 2017: ready-check code examples |
| M02 | Riot 2018: League client motion; 50 ms illustrative offset |
| M03, M04 | Blizzard Hearthstone: Magnetic, Karazhan chess |
| M05 | David Candland, Destiny mouse and parallax tests |
| M06 | Shopoff, Destiny lore scroll and charge states |
| M07 | VALORANT netcode and hit confirmation (40 ms / 80 ms) |
| M09 | Hearthstone 2023 mass pack opening |
| M11 | Carbon v10 motion (durations, curves) |
| M12 | Carbon v10 table stagger |
| M16, M17 | Clash Royale Lucky Drops (Mar 2024); Brawl Stars Angelic/Demonic Drops (Nov 2024) |
| M19 | Material motion (spring schemes 2025) |
| M20 | Riot font download page (BeaufortForLoL, Spiegel) |
| M21 | Brian Schwab, Hearthstone GDC slides |
| P01 | Riot Spirit Blossom visual-design account (2020-07-21) |
| P02 | Apple game-controls guidance |
| P03 | Android touch-target guidance |
| P04 | Roblox Advertising Standards provisions (effective 2026-05-04) |
| R01 | Roblox 2025 Form 10-K (filed 2026-02-11) |
| R02-R04 | Roblox safe areas, core UI, size and aspect constraints |
| R05 | Roblox nine-slice |
| R06, R07 | Roblox image resolution and memory; asset reuse and sprite sheets |
| R12, R13 | not described here (headline 14: desktop memory emulation; headline 13: reduced motion) |
| R14 | Roblox paid random item rules (odds disclosure) |
| R15, R16 | Roblox honest purchase / pricing rules |
| R17-R19 | Roblox Advertising Standards and ad announcements (R17 updated 2026-06-05) |
| R20 | Roblox importer (image / GIF) |
| R21, R22 | Roblox subscriptions; purchase prompt and delivery |

## 2. The 15 headline rules (RP:6-34)

| # | rule (my words) | tag | source ids | RP | check |
| --- | --- | --- | --- | --- | --- |
| H01 | Use the newest platform-mix evidence: mobile 83%, desktop 14%, console 3% for 2025. It is not a 2026 measurement | VERIFIED | R01 | RP:6 | |
| H02 | Borrow each reference game's design logic. Do not borrow its artwork, layout density, business model or reputation | OPINION | C01-C14; U02-U07; M01-M06 | RP:8 | |
| H03 | Put the player's immediate decisions before decoration. A good-looking redesign can still remove useful navigation | EXPERIENCE | U06-U07 | RP:10 | |
| H04 | Do not treat tutorial completion, playtime, progress, return rate, retention, spending and trust as the same thing | VERIFIED | U01 | RP:12 | |
| H05 | Test what an icon means before polishing it. Designer taste is not comprehension evidence | EXPERIENCE | C04; U02 | RP:14 | |
| H06 | Measure real hit areas and rendered text. Points, dp, pixels and millimeters are different units | VERIFIED | P02-P03; U12-U14 | RP:16 | |
| H07 | Give a busy HUD explicit priority, capacity, replacement and overflow rules | OPINION | U05 | RP:18 | |
| H08 | Keep prices, outcomes and consent readable before purchase. Never celebrate ownership that is not confirmed | VERIFIED | R14-R16; R22; U23 | RP:20 | |
| H09 | Use current, format-specific ad eligibility. Under-13 rewarded-ad engagement stays prohibited | VERIFIED | R17-R19; P04 | RP:22 | |
| H10 | Let motion explain rules, state and consequence. Motion must not suggest a different mechanic | EXPERIENCE | M03-M04; M07 | RP:24 | |
| H11 | Scope a published timing to the exact animation it measures, not to a whole reward sequence | VERIFIED | M01 | RP:26 | |
| H12 | Treat missing timing, easing, scale and overshoot values as UNSPECIFIED. They are not secret studio presets | OPINION | M01-M09; M11-M13; M15-M19 | RP:28 | |
| H13 | Keep meaning when motion is reduced. Add non-color cues, focus navigation and configurable presentation | VERIFIED | U15-U20; R13 | RP:30 | |
| H14 | Test real translations and the smallest real devices. Fixed source-language boxes and desktop memory emulation are not enough | VERIFIED | U21; R12 | RP:32 | |
| H15 | Approve a UI by task evidence, state-complete specs and recordings, not by how a screenshot looks | OPINION | U08; U10; M07 | RP:34 | |

## 3. Rules per section

Number units stay as the paper gives them. Do not convert or average. "check" flags a possible paper problem; I did not fix any.

### Paper section 1: what great game UI looks like (RP:44-187)

| id | rule (one line) | tag | numbers with units | paper ids | RP | check |
| --- | --- | --- | --- | --- | --- | --- |
| RA-01 | Treat the 12-case set as teaching examples, not a ranking | OPINION | 12 full cases, 4 mobile (Brawl Stars, Clash Royale, Candy Crush Saga, Monument Valley II); at least 5 deliberately colorful or stylized | C01-C14; U02-U07; U23 | RP:42, 46, 184-185 | Matrix marks the "4 mobile cases" as VERIFIED corpus count |
| RA-02 | Do not read commercial scale as proof of ethical purchase design; use Fortnite as both a UX case and a purchase counterexample | OPINION | none | U02-U07; U23 | RP:46 | |
| RA-03 | Treat every screenshot reading as OPINION; a screenshot cannot prove intention, timing or retention | OPINION | none | all visual readings | RP:40 | |
| RA-04 | Separate navigation, aim and special-action shapes; leave the middle of the screen for the game | OPINION | Brawl Stars: movement lower left, aim lower right, skull button separate | C01-C03 | RP:68, 73 | Screenshot is undated and promotional (RP:68) |
| RA-05 | Show critical state by text or shape as well as hue | OPINION | none | C03 | RP:73 | The screenshot does not prove color-blind accessibility or touch accuracy (RP:68) |
| RA-06 | Test thumb occlusion, input learning and cold-start time on the least capable target phone | OPINION | none | C01-C03 | RP:73 | |
| RA-07 | Keep one stable object identity across collection, battle and rewards | OPINION | none | C05-C07 | RP:84 | |
| RA-08 | Show the next meaningful goal, not an unexplained aggregate (XP total) | OPINION | none | C06 | RP:82, 84 | Clash Royale May 2026 note is an intended benefit, not a measured gain |
| RA-09 | Group modes by the player's task, not by the team that built them | OPINION | none | C05 | RP:80, 84 | |
| RA-10 | Make reward containers differ in contents before adding more looks | OPINION | none | C05 | RP:80, 84 | |
| RA-11 | State the meaning an icon must carry before giving a style reference; test it unlabeled, then in context | OPINION | Candy Crush test: calendar matched Events better than the designers' trophy | C04 | RP:89, 91 | EXPERIENCE account, not a replicated experiment |
| RA-12 | Keep explicit labels for unfamiliar categories | OPINION | none | C04 | RP:91 | |
| RA-13 | Show a claimable state where the player already looks; do not add another modal | OPINION | gold Events state = claimable rewards | C04 | RP:89, 91 | |
| RA-14 | Track shop visits, purchase rate, task completion, frustration and unintended purchase as separate measures | OPINION | worst example: 11 interruptions between levels (not an average) | C04 | RP:89, 91 | Knebel reports no effect sizes |
| RA-15 | For a young audience, take extra care that a reward claim cannot be mistaken for a purchase | OPINION | none | C04 | RP:91 | |
| RA-16 | Build a visually functional prototype before decorating | OPINION | none | C08 | RP:97, 101 | Production method, not a usability effect size |
| RA-17 | Choose a restrained scene palette; mark actionable objects with local hue, value, silhouette and motion; never rely on decorative color alone | OPINION | none | C08 | RP:97-101 | Colors "caused success" is not shown (RP:99) |
| RA-18 | Do not copy sparse UI as a universal rule; competitive or inventory-heavy games may need more visible information | OPINION | none | C08 | RP:55, 101 | |
| RA-19 | Give an expressive collection a stable information frame; make waiting useful with optional practice or social presence | OPINION | none | C10-C11 | RP:106-114 | No queue-abandonment effect size (RP:110) |
| RA-20 | Derive a mascot icon from a meaningful shape, not a mascot beside an unrelated arrow | OPINION | none | C09 | RP:112, 114 | Attribute to the original Splatoon, not Splatoon 3 (RP:112) |
| RA-21 | Do not force navigation through a 3D world when a quick menu is more accessible; keep direct Back and Exit | OPINION | none | C10 | RP:56, 114 | |
| RA-22 | Write a visual thesis; give each expressive gesture one job: identity, grouping, selection, transition or feedback | OPINION | none | C12-C14 | RP:119-123 | |
| RA-23 | Keep utility text steadier than display lettering; keep row alignment and repeated input hints inside energetic framing | OPINION | none | C14 | RP:121, 123 | |
| RA-24 | On mobile, simplify expressive geometry, enlarge readable content and offer reduced motion; do not copy letterforms or assets | OPINION | none | C12-C14 | RP:123 | A screenshot cannot show a transition is fast or comfortable |
| RA-25 | Keep a decorative layer replaceable without losing the accepted, pending or ready state | OPINION | none | M01-M02 | RP:129 | |
| RA-26 | Do not assume League web-client timing is a Roblox standard | OPINION | none | M01-M02 | RP:58 | |
| RA-27 | Test the rule players infer from an animation, not only its appeal; a material must not change the perceived action | OPINION | none | M03-M04 | RP:138 | |
| RA-28 | Let persistent effects stay visible without taking over attention (Hearthstone Magnetic clarifies valid targets without recommending attachment) | EXPERIENCE | no durations published | M03-M04 | RP:136 | |
| RA-29 | Use stable spatial grouping and timer-first compact status rows; shape or line placement supplements green/red color | OPINION (facts VERIFIED) | over 2,000 possible buffs/debuffs; 4 old-channel entries; new critical and weapon channels, up to 2 modifiers each; April 2024 | U05 | RP:145, 149-151 | Capacities are not universal HUD limits (RP:149) |
| RA-30 | Do not give every buff equal emphasis; use priority and stable location | OPINION | none | U05 | RP:151 | Type family and color codes UNSPECIFIED |
| RA-31 | Do not copy controller parallax unchanged to mouse; keep scenic motion tunable per input | EXPERIENCE | none quantified | U05; M05-M06 | RP:60, 147 | A counterscroll concept hid data (RP:147) |
| RA-32 | Keep restrained geometry, a clear action hierarchy and persistent efficient navigation; art must not hide where to act | OPINION | Patch 5.10 restored one-click nav to Home, Battlepass, Agents, Career, Collection, Store | U06-U07 | RP:155-161 | Redesign was front end, not in-match HUD (RP:155) |
| RA-33 | Group actions by the decisions players make; test icons with players | EXPERIENCE | no sample size or uplift; trap icon misread as ammunition or trees | U02-U03 | RP:165, 167 | Mostly Save the World, historical (RP:165) |
| RA-34 | Reserve red for urgent damage; use ammo-type subicons, input prompts and visible material counts as semantic choices | EXPERIENCE | none | U26 | RP:170 | Not a universal palette |
| RA-35 | Offer presets plus fine control; reach useful settings before the barrier they solve | VERIFIED (facts), OPINION (transfer) | more than 60 settings; 3 presets (vision, hearing, motor) | U04; U15 | RP:173-176, 187 | Option count alone does not prove accessibility; dim warnings need measured contrast (RP:175) |
| RA-36 | Interacting settings hurt discoverability, so presets were added | EXPERIENCE | none | U04 | RP:174 | |

### Paper section 2: why UX matters (RP:189-212)

| id | rule | tag | numbers with units | ids | RP | check |
| --- | --- | --- | --- | --- | --- | --- |
| RA-37 | Do not relabel playtime as retention. Tutorial results differ by game and outcome | VERIFIED | over 45,000 new players; 8 conditions; 3 games; Foldit contextual vs none: 660 vs 510 s, 7 vs 4 levels (29% and 75%, p<.001); return 19.16% vs 20.50%, p=.408 (not significant); Hello Worlds return 17.96% (contextual) vs 21.60% (none), p<.001; 2012 | U01 | RP:191, 209 | Hello Worlds return is lower with the tutorial. "Return" means reload or restart, not D1 or D7 (RP:191) |
| RA-38 | Treat a game design as a hypothesis; observe and instrument | EXPERIENCE | Left 4 Dead: approx 40% fewer deaths on No Mercy The Apartments after better teammate cues | U08 | RP:193, 210 | No sampling or controls shown; CS GO playtime example stayed confounded |
| RA-39 | Count access time as part of the session | EXPERIENCE | Android startup roughly 35 s down to 5 or 6 s after Brawl Stars loading work; dated 2026-07-10 | C02 | RP:195, 211 | Observational; not an animation target; not a retention cause |
| RA-40 | Keep task success, learning, session behavior, return, spending and trust as separate outcomes | OPINION | none | C04; U01; U08 | RP:197 | No universal ROI or conversion lift |
| RA-41 | For a new game, name the mechanism and collect the missing outcome; do not borrow another game's revenue as proof | OPINION | none | C04; U01; U08 | RP:197 | |
| RA-42 | Separate QA ("it works") from user research ("it fits the intent"); design accessibility from concept; larger default menu type is one example | EXPERIENCE | Ubisoft 2022-03-16 | U10 | RP:201, 212 | |
| RA-43 | Use a hypothesis record (template T14); observe before explaining; use telemetry for scale and observation for reasons | OPINION | no universal sample size | U08; U10 | RP:203 | |

### Paper section 3: devices and input (RP:214-246)

| id | rule | tag | numbers with units | ids | RP | check |
| --- | --- | --- | --- | --- | --- | --- |
| RA-44 | Plan mobile-first from the dated mix. It does not split phone and tablet and is not a 2026 figure, playtime share, revenue share, session count or unique people | VERIFIED | Mobile 83%, Desktop 14%, Console 3% (average daily active users, 2025); Form 10-K filed 2026-02-11 | R01 | RP:216, 243 | Platform-assignment method not given by the chart |
| RA-45 | Apple: frequent controls at least 44x44 pt; less-important controls (menus) at least 28x28 pt. Keep frequent controls near the thumb; keep movement and camera input areas and system boundaries clear | VERIFIED | 44x44 pt; 28x28 pt | P02 | RP:220, 244 | Other Apple button guidance uses a broader 44 pt baseline. Do not call 44 pt a universal hard minimum |
| RA-46 | Android: touch target at least 48x48 dp with at least 8 dp separation; a visible 24x24 dp icon may sit in a bigger target | VERIFIED | 48x48 dp; 8 dp gap; 24x24 dp icon; approx 9 mm physical | P03 | RP:221, 244 | Android units; not Roblox outcome thresholds |
| RA-47 | Xbox game guidance: phone targets 15x15 mm and tablet targets 24x24 mm, with customizable size, position and spacing | VERIFIED | 15x15 mm phone; 24x24 mm tablet; at 100 DPI 59x59 px and 94x94 px; updated 2026-03-04 | U14 | RP:223, 245 | Millimeters are not points or dp. Arithmetic (15 mm and 24 mm at 100 DPI) matches the paper's px values |
| RA-48 | Pick one rubric, write it down, test on real hardware. Hit region is not icon size; a font property is not the measured glyph. Never average Apple, Android and Xbox numbers | OPINION | none | P02-P03; U12-U14 | RP:225 | The paper says XAG targets are more demanding than the app baselines because scope, unit and player needs differ |
| RA-49 | Default Roblox movement and jump controls sit in the lower corners. CoreUISafeInsets protects interactive content from cutouts and Roblox core UI; DeviceSafeInsets protects cutouts only; neither supports non-interactive edge-to-edge backgrounds | VERIFIED | none | R02-R04 | RP:229 | |
| RA-50 | A fixed historical topbar height is not a safe-area contract; percentage sizing alone does not guarantee usable content; min/max size and aspect constraints exist | VERIFIED | no fixed universal inset | R02-R04 | RP:229, 246 | |
| RA-51 | Specify functional bounds and decorative bounds separately; keep task hierarchy across phone, tablet, PC, console; adapt placement, density, focus and prompts to input; test controls during movement and aiming | OPINION | none | R02-R04; P02; U14-U16 | RP:231 | Proposed, not measured on Roblox |
| RA-52 | Give hover-only information a touch and controller equivalent | OPINION | none | R02-R04; U14-U16 | RP:231 | |
| RA-53 | UI routes work with keyboard and controller digital input; select, back and tab behave consistently; there is an accessible route from launch to accessibility settings (XAG 112) | VERIFIED | XAG 112 | U15 | RP:235 | |
| RA-54 | Show a visible focus indicator; a modal takes focus and holds it, so the obscured screen cannot be selected (XAG 113) | VERIFIED | XAG 113 | U16 | RP:235 | |
| RA-55 | For each screen, specify initial focus, traversal, wrapping, dismissal and restored focus; test launch-to-play-and-exit without a pointer; on mixed input keep logical selection and keep controller prompts when the mouse moves; log unresolved behavior as a decision | OPINION | none | U15-U16 | RP:237 | |

### Paper section 4: hierarchy and clarity (RP:248-282)

| id | rule | tag | numbers | ids | RP | check |
| --- | --- | --- | --- | --- | --- | --- |
| RA-56 | Do not assume fewer elements always means clearer UI (Fortnite undifferentiated groups; Destiny modifiers over capacity; VALORANT navigation removed) | EXPERIENCE | none | U03; U05-U07 | RP:250 | |
| RA-57 | Describe each screen as a player decision using the decision record (template T01). Reject a component with no role in it. Keep a decorative item only with an explicit narrative role that does not compete | OPINION | none | U03; U05-U07 | RP:254 | |
| RA-58 | Build the attention inventory (T02) before polishing. Priority is semantic; salience is what the render does. A health warning quieter than a shop sparkle fails | OPINION | none | U03; U05-U07 | RP:256 | |
| RA-59 | Review three captures: grayscale, reduced size, normal moving | OPINION | none | U03; U05-U07 | RP:256 | |
| RA-60 | Split HUD information into actionable now, useful for planning, inspectable on demand (T03). Do not remove information the player needs just to be minimal | OPINION | none | U03; U05-U07 | RP:258 | |
| RA-61 | Complete the screen state and attention contract (T04) and validate it with the task, not taste | OPINION | no universal HUD slot count | U03; U05-U08 | RP:262-273 | |
| RA-62 | Distinguish selected, equipped, owned and claimed; give a disabled control a discoverable reason; in comparisons align values and units and keep current-item context | OPINION | none | U03; U05-U08 | RP:273 | |
| RA-63 | Rank by semantic urgency before display slots | VERIFIED (fact) | old Destiny channel capacity 4 | U05 | RP:279 | |
| RA-64 | Test common routes for regressions | VERIFIED | one-click access restored (Patch 5.10, 2022-11-15) | U07 | RP:280 | |
| RA-65 | Group by the action the player understands | EXPERIENCE | no published uplift (GDC 2016) | U03 | RP:281 | |

### Paper section 5: first session and onboarding (RP:284-307)

| id | rule | tag | numbers | ids | RP | check |
| --- | --- | --- | --- | --- | --- | --- |
| RA-66 | Do not assume a tutorial teaches more; effects differ by game and outcome | VERIFIED | 3 games; 8 conditions (CHI 2012) | U01 | RP:286, 304 | |
| RA-67 | Explain each element in three parts: what it is, how to use it, why it matters. Protect attention while teaching (a fort-damage message was missed during combat) | EXPERIENCE | none | U03 | RP:288, 306 | |
| RA-68 | Alpha difficulty or death during onboarding correlated with lower retention; the direction of cause is unknown | EXPERIENCE | no first-minute drop-off benchmark | U03 | RP:288, 306 | Correlation only |
| RA-69 | Plan onboarding as a list of demonstrated competences (T05). A finished dialogue panel is not proof of learning | OPINION | none | U01-U03; U08 | RP:292 | |
| RA-70 | Name five first-session milestones (T06). Do not copy a universal minute mark for the shop; test shop timing | OPINION | shop timing UNSPECIFIED | U01-U03; U08 | RP:294, 307 | |
| RA-71 | Record abandonment at semantic transitions (T07); split technical failure from comprehension failure; follow a numeric anomaly with targeted observation | OPINION | none | U01-U03; U08 | RP:296 | |
| RA-72 | Use the 7-step funnel (T07) and record exposure, exits, active time, errors, assistance, technical interruptions. A skip, a crash and a misread instruction each need their own diagnosis | OPINION | no acceptable drop-off percentage | U01-U03; U08 | RP:298 | |
| RA-73 | Require an unprompted repeat before counting a lesson learned; do not equate "Next" with learning | OPINION | proposed test | U01-U03; U08 | RP:305 | |

### Paper section 6: shops and monetization UI (RP:309-346)

| id | rule | tag | numbers with units | ids | RP | check |
| --- | --- | --- | --- | --- | --- | --- |
| RA-74 | Test purchase comprehension separately from commercial performance | OPINION | none | C04 | RP:311 | |
| RA-75 | Require affirmative consent and avoid dark patterns; the FTC order is a regulatory action, not a trust study | VERIFIED | FTC order finalized March 2023 (2023-03-14 in matrix): $245 million for refunds; separate $275 million children's-privacy settlement is not part of it | U23 | RP:313, 344 | |
| RA-76 | Epic's changes (hold-to-purchase, cancellation, refund, payment saving) are a company account, not proof of full remediation. Do not promise an unconditional refund | EXPERIENCE | V Bucks Item Shop cancellation: within 24 hours if the item is not used or equipped; exclusions apply; Return Tickets are a separate route | U24-U25 | RP:315 | The 24-hour rule is Epic support, not a Roblox rule |
| RA-77 | Treat an offer as a contract (T08); separate preview from commit; an item card that hides ownership, real cost or duration is incomplete | OPINION | none | U23-U25; R15-R16; R21-R22 | RP:319 | |
| RA-78 | Run purchase as a state machine (T09); disable accidental repeat commit while keeping a clear waiting state; celebrate only after confirmation | OPINION | none | U23-U25; R15-R16; R21-R22 | RP:321 | |
| RA-79 | For paid randomness show all possible final outcomes and real numeric percentage odds before purchase (T10) | VERIFIED | distribution totals 100%; documented rounding exception with disclaimer | R14 | RP:325, 343 | |
| RA-80 | Use descriptive wording for the odds-detail control, not only an unlabeled info icon; restricted users need an eligible alternative or a blocked paid-random path | VERIFIED | none | R14 | RP:325 | |
| RA-81 | Be honest and deliberate: no fake perpetual discounts, false scarcity or misleading countdowns; show current product information because regional pricing can differ from art; subscriptions need clear price, duration, benefits; a closed prompt does not prove delivery | VERIFIED | subscriptions renew monthly | R15-R16; R21-R22 | RP:327, 346 | |
| RA-82 | Put paid-random disclosure before commitment, not in the reveal; a rare-looking frame is not an explanation of odds; prices and changing terms are content, not baked art | OPINION | none | R14-R16; R21-R22 | RP:329 | |
| RA-83 | Apply ad rules as of the date (T11); reserve disclosure space; design fallbacks; keep essential progress independent of ad delivery | VERIFIED (rules) / OPINION (design response) | see T11 | R17-R19; P04 | RP:333-337, 345 | The paper flags a source conflict, see section 8 of this file |

### Paper section 7: visual style and image-based UI (RP:348-385)

| id | rule | tag | numbers with units | ids | RP | check |
| --- | --- | --- | --- | --- | --- | --- |
| RA-84 | Start with a visual thesis and functional hierarchy, then define shape and material roles, then approve a small component family; do not imitate a source's surface | OPINION | none | P01; C08; C12-C14 | RP:350, 352 | The Riot account is an intended treatment, not a rule that UI must look physical |
| RA-85 | A playful style does not need every surface equally textured, saturated or animated | OPINION | none | P01; C08; C12-C14 | RP:352 | |
| RA-86 | Use the 7-row style spec (T12); mark project values unresolved until tested; do not infer font families, palette codes or shadow values from screenshots | OPINION | none | P01; C04; C08; U12-U18 | RP:356-368 | Not a discovered studio template (RP:368) |
| RA-87 | Derive material from the game world and task; no universal bevel or gradient value | EXPERIENCE | none | P01 (2020-07-21) | RP:382 | |
| RA-88 | Use nine-slice: corners kept, edges stretch along their axis, center stretches | VERIFIED | 9 regions | R05 | RP:372, 383 | |
| RA-89 | Texture memory follows pixel count: 1024x1024 uses 4x the graphics memory of 512x512. Ask for no more resolution than needed: generally at most 512x512 unless a large screen area is covered; small images are often below 256x256 | VERIFIED | 1024x1024 = 4x 512x512; 512x512 general maximum; small < 256x256 | R05-R07 | RP:372, 384 | Guidance, not a universal upload cap |
| RA-90 | Reuse the same asset ID to avoid duplicate uploads; removing alpha or disk compression does not promise equal runtime-memory saving | VERIFIED | none | R07; R20 | RP:374 | |
| RA-91 | Sprite sheets group small images, but their full dimensions and unused area still cost memory | VERIFIED | none | R07; R20 | RP:374 | |
| RA-92 | Import acceptance of a GIF is not proof it plays as an animated GUI image | VERIFIED | none | R20 | RP:374 | |
| RA-93 | Hand off the asset list (T13); test the imported asset on the real background and a phone before mass production; keep changeable text, prices and quantities out of baked art | OPINION | none | P01; R05-R07; R20 | RP:376, 385 | Blender icon family camera, lighting, silhouette are project choices, not Roblox rules |

### Paper section 8: UI motion, principles part (RP:387-436)

| id | rule | tag | numbers with units | ids | RP | check |
| --- | --- | --- | --- | --- | --- | --- |
| RA-94 | Public evidence is strongest about motion meaning, sequence and production limits; weaker about full timing recipes | EXPERIENCE | none | M03-M07 | RP:389 | |
| RA-95 | Use timelines for complex cross-element transitions; provide a static fallback for low-spec clients (historical League client, not a Roblox cost guarantee) | EXPERIENCE | none | M02 | RP:393 | |
| RA-96 | Size a celebration to the mechanical consequence and the competing tasks | EXPERIENCE | none | M03-M04 | RP:395 | |
| RA-97 | Anticipation prepares attention but must not withhold basic acknowledgment; staging marks the key information beat; overshoot, squash/stretch, follow-through are optional with UNSPECIFIED numbers; keep labels readable and interaction stable | OPINION | numbers UNSPECIFIED | M01-M04; U17 | RP:397 | "Playful" does not give false timing authority |
| RA-98 | Give secondary and idle motion cancel and priority rules; idle motion must not compete forever with the task | OPINION | none | M05-M06; U17 | RP:397, 401 | |
| RA-99 | Keep the cursor or focus target separate from scenic motion; tune or disable scenic motion by input and preference; reduced motion keeps state and never removes the only cue | OPINION | none | M05-M06; U17 | RP:401 | |
| RA-100 | Destiny: parallax can overpower at high cursor speed; distance- and gamepad-sensitive scroll and peripheral-readable charge states exist; no numeric curves were published | EXPERIENCE | none | M05-M06 | RP:399 | |
| RA-101 | Use local-action events and confirmed-hit events separately (VALORANT) | VERIFIED scope | 40 ms one way, 80 ms round trip = confirmation latency, not hitmarker animation life | M07 | RP:412 | Riot separated correct simulation from misleading presentation |
| RA-102 | Reward sequence: write separate states (T15). A skip or repeat shortcut must reach the same confirmed result; an animation must not imply force or tap speed changes odds unless it does | OPINION | listed order is proposed, not a studio timeline | M09; M16-M17; R14 | RP:435 | |
| RA-103 | Hearthstone 2023 mass opening: charge over the stack, release into the opening area, reveal highlights one by one or together, end with a summary. No per-stage timing | EXPERIENCE | none | M09 | RP:431 | |
| RA-104 | Clash Royale Lucky Drops (March 2024) = three taps with chances to improve rarity. Brawl Stars Angelic/Demonic Drops (November 2024) = hold-to-open, longer opening signals a better reward. No ms, no easing; not current specs | VERIFIED historical feature | 3 taps | M16-M17 | RP:433 | |
| RA-105 | The 25 motion records are a calibration-ready library, not 25 presets; approve every unknown field through project testing first | OPINION | 25 records; all absent values UNSPECIFIED | records in part B | RP:439 | Records start at RP:441 (part B) |

Continued in [[reference/ui/05b-research-templates]].
