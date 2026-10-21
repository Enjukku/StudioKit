---
type: reference
scope: universal
status: active
updated: 2026-10-20
source: "owner-supplied research paper 'Game_UI_UX_Research_AI_Designer.txt' (ChatGPT, research date 2026-10-21), lines 437-1112, J002"
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-20

# UX research part B: motion records, accessibility, localization, measuring, process, sources (continued)

First part (source card, conventions, earlier sections): [[reference/ui/06a-research-motion-a11y]]. Citation rules are stated there.

## 5. The AI-designer process (paper section 12, RP:823-937)

RP:825 [OPINION]: a proposed operating method grounded in case evidence, not a claim that one studio uses this checklist. Evidence gaps stay explicit requirements; never invent a value just to finish a spec [P01; U08; U10; M01-M07]. The 9 steps (matrix RP:934, OPINION).

| step | Do this (RP line) | Deliverable the step must produce | Ids |
|---|---|---|---|
| 1 | Define the player moment (827). Use the what / how / why questions to find missing understanding | Moment record: goal, prior knowledge, game state, input, locale, accessibility settings, consequence of failure | U03 |
| 2 | Build an evidence ledger (829). Separate a measured outcome from a design intention or visual interpretation | Ledger: per claim, evidence tag, source/date, unit, scope, uncertainty | U01; U08 |
| 3 | Map the decision and its states (831). Keep common task routes | State list: entry, normal, empty, maximum content, loading, pending, error, insufficient resources, eligibility, success, recovery | U05-U07; R14-R16; R22 |
| 4 | Wireframe before materials (833). Order info by player importance, compare plausible structures, use realistic content | Wireframes (several structures, real content) + a written reason the chosen one serves the decision | P01; U06 |
| 5 | Apply a visual grammar (835). Keep identity strong without assuming ornament aids understanding | Role definitions: shape, color, type, icon, material, layout | C04; C08; C12-C14; P01 |
| 6 | Storyboard information and motion (837). Mark input acknowledgment, confirmed result, information visibility, input availability and decoration end as separate beats | Storyboard with those beats + cancel, repeat and reduced-motion behavior | M01-M07; U17 |
| 7 | Write the implementation contract (839). Unknown numeric fields stay UNSPECIFIED | Spec: sizes and coordinate conventions, state meanings, assets, text behavior, focus map, all motion fields (see 1a), acceptance tests | R02-R07; U12-U16; M01-M02 |
| 8 | Review the real artifact (841). Exercise dense, long-string, enlarged-text, reduced-motion and failure states | Target-size screenshots and recordings from actual devices; review notes | R12-R13; U12-U21 |
| 9 | Test and revise (843). Mix targeted observation with suitable metrics | Test results with disconfirming results, trade-offs and regression tests kept; approved project values versioned and not relabeled as studio facts | U01; U08; U10; C04 |

Approval and gating rules in this section (all OPINION unless marked):
- A reviewer records PASS, FAIL or UNVERIFIED with the supporting capture or test. UNVERIFIED is not PASS (RP:879).
- The checklist's qualitative pass conditions are proposed review criteria, not published effect sizes; other numbers keep their source rubric (RP:879).
- Check 14: all required motion fields must be resolved before release; this paper's own library is not release-ready (RP:896).
- Check 13: every empirical timing/easing/scale claim needs provenance (RP:895).
- Check 21: threshold for first-session learning is declared before the test (RP:903).
- Evidence matrix (RP:932-937): evidence-preserving workflow (9 steps, OPINION); outcome states PASS/FAIL/UNVERIFIED (OPINION); no fabricated empirical parameter (OPINION); resolve policy and project gaps before release, no assumed all-ages eligibility (VERIFIED, R17-R19; P04, 2026).

### 5a. "Do not do" list (RP:845-875)

| # | Do not | Why (tag, id) | RP |
|---|---|---|---|
| 1 | Infer a rule from a flourish | Hearthstone collision animation suggested the wrong damage rule [EXPERIENCE M04] | 847 |
| 2 | Remove a task shortcut for a cleaner layout | VALORANT restored removed one-click destinations [VERIFIED U07] | 849 |
| 3 | Treat designer icon preference as player meaning | See contextual icon tests in section 1 [EXPERIENCE C04; U02] | 851 |
| 4 | Add more equal-priority status effects than the HUD can explain | Destiny overflow supports explicit priority rules [OPINION adaptation of U05] | 853 |
| 5 | Turn qualitative directions into invented percentages | Candy Crush account publishes no effect sizes [VERIFIED source limit C04] | 855 |
| 6 | Equate longer sessions or more box openings with better UX | Tutorial return and playtime diverged; loot-box interaction did not prove welfare [VERIFIED U01; M18] | 857 |
| 7 | Use promotional screenshots as current production specs | Brawl and Clash images are undated snapshots [VERIFIED artifact limit C03; C07] | 859 |
| 8 | Claim a complete studio motion preset from one fade constant | See records 01 and 02 [VERIFIED M01] | 861 |
| 9 | Make repeated spectacle mandatory without a task reason | Hearthstone batch reveal gives a faster review path [OPINION adaptation of M09] | 863 |
| 10 | Signal purchase success when the prompt merely closes | Confirmed delivery differs from dialog completion [VERIFIED R22] | 865 |
| 11 | Hide odds behind an unlabeled info icon | Roblox requires descriptive pre-purchase access to paid-random outcomes and odds [VERIFIED R14] | 867 |
| 12 | Apply old blanket ad age rules | 2026 format-specific rules supersede that; ambiguity remains documented [VERIFIED R17-R19; P04] | 869 |
| 13 | Use color, sound or animation as the only critical cue | Additional channels and motion alternatives required by the selected guidance [VERIFIED U17-U19] | 871 |
| 14 | Shrink every long translation to fit a fixed English box | Reflow and real-script testing are the supported approach [VERIFIED U21] | 873 |
| 15 | Treat emulator memory or a universal tween count as a phone benchmark | Roblox requires real-device profiling; cost depends on workload [VERIFIED R08; R12] | 875 |

### 5b. Numeric review checklist (22 checks, RP:881-904)

Record PASS / FAIL / UNVERIFIED with the capture or test for each.

| # | Check | Pass condition | Tag and scope |
|---|---|---|---|
| 01 | Context | device, build, input, locale and scale fields all present | OPINION evidence requirement |
| 02 | Text size | meet the selected rendered-glyph baseline of section 2 | VERIFIED U12; do not substitute nominal font size |
| 03 | Text enlargement | 200% supported with no lost content or function | VERIFIED U12 |
| 04 | Contrast | 4.5:1 standard; 3:1 applicable large; 7:1 high-contrast mode | VERIFIED U13; weakest background and correct large threshold |
| 05 | Touch | declared physical/dp/pt rubric met; no conflicting overlapping hit areas | VERIFIED P02-P03/U14 baseline; OPINION overlap criterion |
| 06 | Safe areas | no required control hidden by cutouts or Roblox chrome | OPINION adaptation of R02 |
| 07 | Digital navigation | all required actions reachable on supported digital inputs | OPINION gate based on U15 |
| 08 | Focus | unambiguous active target; no focus escape behind an active modal | OPINION gate based on U16 |
| 09 | State semantics | selected / owned / equipped / pending / success states distinguishable | OPINION gate based on M07; R22 |
| 10 | Busy HUD | no essential signal displaced by lower-priority effects | OPINION gate based on U05 |
| 11 | Critical cues | no critical fact communicated only by color | VERIFIED U18 principle; OPINION review rule |
| 12 | Captions | essential opening and audio events have accessible equivalents | OPINION gate based on U19 |
| 13 | Motion provenance | every empirical timing/easing/scale claim has provenance | OPINION evidence gate |
| 14 | Motion completeness | all required implementation fields resolved before release | OPINION gate; this research library is not release-ready |
| 15 | Reduced motion | essential meanings preserved in the reduced variant | OPINION gate based on U17; R13 |
| 16 | Temporal safety | qualified temporal analysis done; a still image is not enough | VERIFIED U20; no simple flash-count shortcut |
| 17 | Localization | essential prices, conditions and distinguishing labels unclipped | OPINION gate based on U21; R14-R16 |
| 18 | Paid randomness | actual distribution totals 100%; allowed display rounding explained | VERIFIED R14 |
| 19 | Price and grant | displayed price matches charge; ownership confirmed | OPINION gate based on R16; R22 |
| 20 | Advertising | no U13 rewarded-ad path; current format eligibility verified | VERIFIED R17-R19; P04 (check: see section 7, "U13" ambiguity) |
| 21 | First-session learning | unprompted core action tested; threshold declared before the test | OPINION test based on U01-U03 |
| 22 | Real-device performance | performance claims backed by actual device measurements | OPINION gate based on R08; R12 |

### 5c. Failure modes to screen in AI-generated work (RP:906-908) [OPINION]

Generic panels unrelated to the game, excessive text, weak grouping, tiny controls, wrong apparent scale, flat state feedback, uncontrolled simultaneous animation. These are review hypotheses, not measured prevalence claims. Diagnose each as one of: style-role mismatch, failed comprehension, insufficient target geometry, hidden urgency, absent acknowledgment, motion/performance failure. Never replace a concrete diagnosis with "looks AI generated" [C04; C08; P01; U05-U07; U12-U17].

---

## 6. Source register (RP:939-1111)

Paper rule (RP:941): live pages checked 2026-10-21. "Undated" means no reliable publication date; an access date is not a publication date. Reliability scale used here: HIGH = official Roblox or platform doc/policy; ENG = official non-Roblox doc, high only within its stated scope; EXP = studio talk, interview, portfolio or case account (experience, not proof); STUDY = peer-reviewed or conference study; BLOG = practitioner blog. Reliability is the extractor's judgement from the paper's type labels; key lines omitted.

### 6a. Case studies (C)

| id | Publisher / author | Title (short) | Date | Type | Reliability note | RP |
|---|---|---|---|---|---|---|
| C01 | Antti Summala / Supercell | Designing Two Tasty Cores (Brawl Stars), GDC 2019 | 2019 | talk abstract (full talk not viewed) | EXP; abstract only | 943 |
| C02 | Supercell | How Titan Made Brawl Stars Toilet Break-Friendly | 2026-07-10 | firsthand company engineering account | EXP | 945 |
| C03 | Supercell | Brawl Stars game page | undated, accessed 2026-10-21 | official promo screenshot and text | undated snapshot; not a production spec | 947 |
| C04 | Matheus Knebel | Candy Crush Saga UX-overhaul (2019-20) | not stated; mentions 2023 plans; accessed 2026-10-21 | practitioner portfolio | EXP; no effect sizes | 949 |
| C05 | Supercell | Clash Royale June Update 2025 | 2025-06-28 | official release notes | HIGH for what shipped | 951 |
| C06 | Supercell | Clash Royale Collection Levels & Mastery Changes | 2026-05-13 | official announcement | HIGH for what shipped | 953 |
| C07 | Supercell | Clash Royale game page | undated, accessed 2026-10-21 | official promo screenshot and text | undated snapshot; not a production spec | 955 |
| C08 | David Fernández Huerta / ustwo games | The Art of Monument Valley II, GDC 2018 | 2018 | talk slides and notes (PDF pages 115, 125, 193-194 relevant) | EXP | 957 |
| C09 | Nintendo | Iwata Asks: Splatoon 4. Gaining Momentum | 2015 (day not shown) | first-party developer interview | EXP | 959 |
| C10 | Nintendo | Ask the Developer Vol. 7: Splatoon 3 Part 2 | 2022-09-07 | translated developer interview | EXP | 961 |
| C11 | Nintendo | Ask the Developer Vol. 7: Splatoon 3 Part 3 | 2022-09-07 | translated developer interview | EXP | 963 |
| C12 | Masayoshi Suto, Kazuhisa Wada / Atlus | Persona UI creative methods, CEDEC+KYUSHU 2017 (Japanese) | 2017-10-28 | session abstract | EXP; abstract only | 965 |
| C13 | CEDEC | CEDEC Awards winners | 2019 | official award record | award record only | 967 |
| C14 | Atlus slides via Famitsu | Atlus CEDEC+KYUSHU 2017 slides, published by Famitsu | 2017-11-13 | primary slides embedded in secondary coverage; only visible slide text relied on | EXP; not the reporter's paraphrase | 969 |

### 6b. Roblox and platform sources (R)

| id | Publisher | Title (short) | Date | Type | Reliability note | RP |
|---|---|---|---|---|---|---|
| R01 | Roblox | 2025 Form 10-K (Our Users p.9; metric definition pp.5-6) | filed 2026-02-11; period 2025-01-01 to 2025-12-31 | regulatory filing | HIGH; latest annual split is 2025, mobile aggregated | 971 |
| R02 | Roblox | ScreenInsets | undated, accessed 2026-10-21 | official doc | HIGH | 973 |
| R03 | Roblox | Position and size UI objects | undated, accessed 2026-10-21 | official doc | HIGH | 975 |
| R04 | Roblox | Size modifiers and constraints | undated, accessed 2026-10-21 | official doc | HIGH | 977 |
| R05 | Roblox | UI 9-slice design | undated, accessed 2026-10-21 | official doc | HIGH | 979 |
| R06 | Roblox | Text & image labels | undated, accessed 2026-10-21 | official doc | HIGH | 981 |
| R07 | Roblox | Improve performance: asset memory usage | undated, accessed 2026-10-21 | official doc | HIGH | 983 |
| R08 | Roblox | MicroProfiler tag reference | undated, accessed 2026-10-21 | official doc | HIGH | 985 |
| R09 | Roblox | UI appearance modifiers: stroke thickness | undated, accessed 2026-10-21 | official doc | HIGH | 987 |
| R10 | Roblox | Viewport frames | undated, accessed 2026-10-21 | official doc | HIGH | 989 |
| R11 | Roblox | Particle emitters | undated, accessed 2026-10-21 | official doc | HIGH | 991 |
| R12 | Roblox | Design for performance | undated, accessed 2026-10-21 | official doc | HIGH | 993 |
| R13 | Roblox | Accessibility guidelines | undated, accessed 2026-10-21 | official doc | HIGH | 995 |
| R14 | Roblox | Paid random items policy guidelines | undated, accessed 2026-10-21 | official policy | HIGH | 997 |
| R15 | Roblox | Monetization: presenting products and global audiences | undated, accessed 2026-10-21 | official policy/doc | HIGH | 999 |
| R16 | Roblox | Regional pricing | undated, accessed 2026-10-21 | official doc | HIGH | 1001 |
| R17 | Roblox | Advertising Standards | last updated 2026-06-05; new sections announced 2026-03-20, effective 2026-05-04 | official policy | HIGH; conflicts with P04 on under-13 (section 7) | 1003 |
| R18 | Roblox | Ad integrations | undated, accessed 2026-10-21 | official doc | HIGH | 1005 |
| R19 | Roblox | Immersive ads | undated, accessed 2026-10-21 | official doc | HIGH | 1007 |
| R20 | Roblox | Importer | undated, accessed 2026-10-21 | official doc | HIGH | 1009 |
| R21 | Roblox | Subscriptions | undated, accessed 2026-10-21 | official doc | HIGH | 1011 |
| R22 | Roblox | Developer Products | undated, accessed 2026-10-21 | official doc | HIGH | 1013 |

### 6c. Research, guidance and press (U)

| id | Publisher / author | Title (short) | Date | Type | Reliability note | RP |
|---|---|---|---|---|---|---|
| U01 | Erik Andersen et al. | Impact of Tutorials on Games of Varying Complexity, CHI 2012 | 2012-05-05 to 05-10 | study | STUDY | 1015 |
| U02 | Celia Hodent | Understanding the Success of Fortnite (UX and psychology) | 2019-07-22; updated 2020-06-20 | blog analysis | BLOG / EXP | 1017 |
| U03 | Celia Hodent | The Gamer's Brain Part 2: onboarding, GDC 2016 | 2016-03-22; updated 2020-06-01 | talk write-up | EXP | 1019 |
| U04 | Matthew Dunnerstick / Naughty Dog | TLOU Part II accessibility features detailed | 2020-06-09 | studio blog | EXP | 1021 |
| U05 | Destiny 2 team / Bungie UI and UX | This Week in Destiny (Updating the HUD) | 2024-04-11 | studio news | EXP | 1023 |
| U06 | Riot Games | Preview the future of VALORANT's interface | 2022-10-10 | studio news | EXP | 1025 |
| U07 | Jo-Ellen Aragon / Riot | VALORANT Patch Notes 5.10 | 2022-11-15 | official patch notes | HIGH for what shipped | 1027 |
| U08 | Mike Ambinder / Valve | Data to Drive Decision-Making, Steam Dev Days 2014 | 2014 | talk slides | EXP | 1029 |
| U09 | Giancarlo Varanini / Ubisoft | How Ubisoft Is Putting the Spotlight on Accessibility | 2018-05-17 | company article | EXP; reported adoption only | 1031 |
| U10 | Youssef Maguid / David Tisserand | Future of Accessibility at Ubisoft | 2022-03-16 | interview | EXP | 1033 |
| U11 | Microsoft | Xbox Accessibility Guidelines V3.2 | version 2023-06-08; accessed 2026-10-21 | official guideline | ENG; not a checklist or certification | 1035 |
| U12 | Microsoft | XAG 101: Text display | updated 2026-03-04 | official guideline | ENG | 1037 |
| U13 | Microsoft | XAG 102: Contrast | updated 2026-03-04 | official guideline | ENG | 1039 |
| U14 | Microsoft | XAG 107: Input | updated 2026-03-04 | official guideline | ENG | 1041 |
| U15 | Microsoft | XAG 112: UI navigation | updated 2026-03-04 | official guideline | ENG | 1043 |
| U16 | Microsoft | XAG 113: UI focus handling | updated 2026-03-04 | official guideline | ENG | 1045 |
| U17 | Microsoft | XAG 117: Visual distractions and motion settings | updated 2026-03-04 | official guideline | ENG | 1047 |
| U18 | Microsoft | XAG 103: Additional channels for cues | updated 2026-03-04 | official guideline | ENG | 1049 |
| U19 | Microsoft | XAG 104: Subtitles and captions | updated 2026-03-04 | official guideline | ENG | 1051 |
| U20 | Microsoft | XAG 118: Photosensitivity | updated 2026-03-04 | official guideline | ENG | 1053 |
| U21 | W3C Internationalization | Text size in translation | undated, accessed 2026-10-21 | standards-body article | ENG | 1055 |
| U22 | Game Accessibility Guidelines | Use simple clear language | undated, accessed 2026-10-21 | guideline page | ENG; no reading-grade target | 1057 |
| U23 | FTC | Order requiring Epic Games to pay $245 million (Fortnite unwanted charges) | 2023-03-14 | regulator press release | HIGH for the order; case timeline is a second source | 1059 |
| U24 | Epic Games | Epic FTC settlement and moving beyond industry practices | 2022-12-19; update 2023-09-19 | company statement | EXP | 1061 |
| U25 | Epic Games Support | Cancel or refund Fortnite Item Shop purchases (page cites a 24-hour cancel window) | undated; checked 2026-10-21 | support page | company policy page | 1063 |
| U26 | Celia Hodent / Ars Technica | 10 things you might not have noticed in Fortnite | 2018-09-13 | firsthand video interview | EXP | 1065 |

### 6d. Motion and mechanics sources (M) and platform patterns (P)

M10 and M14 are absent from the paper's register and are not cited in lines 437-1112 (numbering gap).

| id | Publisher / author | Title (short) | Date | Type | Reliability note | RP |
|---|---|---|---|---|---|---|
| M01 | Riot, Jules Glegg | Under the hood of the League Client's Hextech UI | 2017-02-14 | studio engineering report; code example VERIFIED, rationale EXPERIENCE | code numbers VERIFIED for that client only | 1067 |
| M02 | Riot, Richard Ye | Animation in the League of Legends Client | 2018-02-27 | studio engineering | EXP | 1069 |
| M03 | Blizzard, Hadidjah Chamberlin | Developer Insights: The Art Behind THE SCIENCE | 2018-10-26 | studio artist account | EXP | 1071 |
| M04 | Blizzard, Peter Whalen | Hearthside Chat: Karazhan's Chess Event | 2016-10-07 | studio design account | EXP | 1073 |
| M05 | David Candland | Motion Comps | n.d.; accessed 2026-10-21 | UI director portfolio | EXP | 1075 |
| M06 | Madeleine Shopoff | UI/UX Technical Designer: Destiny / Destiny 2 | n.d.; accessed 2026-10-21 | implementer portfolio | EXP | 1077 |
| M07 | Riot, Kevin Lee | The State of Hit Registration | 2020-08-06 | studio engineering | EXP | 1079 |
| M08 | Blizzard | Overwatch 2 PvP beta patch notes | April 2022 (initial beta notes) | patch notes, historical behavior | VERIFIED historical | 1081 |
| M09 | Blizzard | Introducing Mass Pack Opening (Hearthstone) | 2023-09-06 | feature announcement | EXP / historical behavior | 1083 |
| M11 | IBM Carbon v10 | Motion: Overview | footer updated 2025-08-19; accessed 2026-10-21 | archived design-system spec, non-game | VERIFIED for scope; non-game | 1085 |
| M12 | IBM Carbon v10 | Motion: Choreography | footer updated 2025-08-19; accessed 2026-10-21 | archived design-system guidance, non-game | VERIFIED for scope; non-game | 1087 |
| M13 | Epic Games | Optimization Guidelines for UMG | n.d.; accessed 2026-10-21 | engine doc (Unreal, not Roblox) | VERIFIED; not Roblox | 1089 |
| M15 | Epic Games | Project World Location to Widget Position | n.d.; accessed 2026-10-21 | API doc (Unreal, not Roblox) | VERIFIED; not a Roblox recipe | 1091 |
| M16 | Supercell | Clash Royale Game Update: Lucky Drops (three taps to open) | 2024-03-18 | historical feature doc | VERIFIED historical | 1093 |
| M17 | Supercell | How to get all the Angelic and Demonic Drops (Brawl Stars) | 2024-11-07, later dated announcements | seasonal feature doc | VERIFIED | 1095 |
| M18 | Dominic Kao | Infinite Loot Box, IEEE Trans. on Games 12(2) 219-224 | early 2019; issue June 2020 | peer-reviewed study | STUDY; platform not a shipped recipe | 1097 |
| M19 | Google | Material Design 3 Motion physics system | May 2025 change; accessed 2026-10-21 | non-game design-system description | VERIFIED for scope; non-game | 1099 |
| M20 | Riot | League of Legends Downloads | n.d.; accessed 2026-10-21 | official asset availability | VERIFIED | 1101 |
| M21 | Brian Schwab (formerly Blizzard) | Designers Are from Saturn, Programmers Are from Uranus, GDC 2014 | 2014; day not verified | talk slides | EXP | 1103 |
| P01 | Riot Games | Complementary Visual Design in Spirit Blossom | 2020-07-21 | studio article | EXP | 1105 |
| P02 | Apple | Game controls (Human Interface Guidelines) | undated, accessed 2026-10-21 | platform guideline | ENG | 1107 |
| P03 | Google Android Accessibility Help | Touch target size | undated, accessed 2026-10-21 | platform guidance | ENG | 1109 |
| P04 | Roblox staff | New Advertising Policies and Standards (DevForum) | 2026-03-20; all-age change effective 2026-05-04; updated 2026-06-17 | staff announcement | HIGH (staff post); conflicts with R17 example (section 7) | 1111 |

---

## 7. Conflicts, cautions and UNSPECIFIED gaps

### 7a. Conflicts and checks flagged by the paper

| item | detail | RP |
|---|---|---|
| Ads: under-13 eligibility vs all-age formats | The unqualified under-13 ineligibility example (R17-R19) is not resolved against current all-age nonrewarded format provisions (P04). Runtime eligibility check is still needed. Do not assume all-ages eligibility | 924, 937, 869 |
| XAG large-text definitions differ from web | Large thresholds differ by platform and from web definitions | 746 |
| Ready-check constants are narrow | 200 ms / 300 ms apply to one video fade pair in 2017; not a preset | 861, 720 |
| Non-game motion tokens | 70-700 ms tokens and a 20 ms stagger example come from IBM Carbon (M11-M12, non-game). Not a value for any game record | 523, 722 |
| Promo screenshots | C03 and C07 are undated snapshots; do not use as production specs | 859 |
| Epic UMG docs | M13 and M15 are Unreal documents; M15 is not a Roblox recipe | 697 |
| Subtitle adoption | 60% / 70% PC is adoption, not prevalence, causation or quality | 752 |
| Study scope | M18 is a study platform; more openings do not equal welfare | 790, 857 |

### 7b. UNSPECIFIED gaps (paper's "open questions", all tagged VERIFIED evidence limit, RP:910-928)

1. 2026 phone-versus-tablet share of Roblox play, and the device mix of the target game. Latest annual split is 2025 and aggregates mobile [R01].
2. Studio-wide timings, easing, scale endpoints and overshoot for button, tab, toast, number-pop, reward, rarity and level-up effects in the named games [M01-M09; M11-M13; M15-M19].
3. Exact reveal-stage timing for HoYoverse wishes and the cited Supercell and Hearthstone reveals [M09; M16-M17].
4. A universal acceptable first-session drop-off rate, shop-introduction minute, tutorial length or reading-grade threshold [U01-U03; U22].
5. Transferable retention, conversion or trust gains from the cited UI redesigns; reports omit methods, denominators, effect sizes [C04; U05-U08].
6. Universal phone cost in ms or memory per tween, gradient, stroke pulse, sprite sheet, viewport preview or screen-layer particle [R07-R12].
7. Policy owner's resolution of the under-13 ineligibility example vs all-age nonrewarded formats [R17-R19; P04].
8. Best project-specific balance of expressive motion, repeated-task speed, comfort and delight for young players; needs observed comprehension, repeated-use and accessibility tests [M03-M09; M18; U17].
9. Optimal fixed text-expansion allowance or universal icon vocabulary for every supported language [U02; U21-U22].

### 7c. Extractor `check` flags (nothing changed in the source facts above)

| flag | issue |
|---|---|
| "U13" in checklist item 20 (RP:902) | Reads "No U13 rewarded-ad path". In this paper U13 is also the source id for XAG 102 (contrast). In context it probably means an under-13 player; confirm before the skill uses it. |
| Record 25 duration (RP:683) | "≈2,800 ms" is a paper conversion of ≈2.8 s tagged EXPERIENCE under C02. The C02 key line in the register (RP:945) is about loading time and does not show the 2.8 s figure; the figure's origin is in the first half or the source page. |
| Particle emitter numbers (RP:712) | 100 particles/s mobile vs 400 otherwise are cited as R08-R11 as a group; the exact source is not named. |
| Touch rubric (RP:887) | Check 05 requires a "declared physical/dp/pt rubric" from P02-P03/U14; no touch-target number appears in lines 437-1112. Numbers, if any, live in the first half; UNSPECIFIED here. |
| Mobile text DPI (RP:739) | 18 px at 100 DPI etc. are XAG values; the paper gives no mapping to Roblox pixels or scale; do not convert without a source. |
| Evidence-matrix tables (RP:719) | Several matrix tables have four columns but a three-column separator row. Formatting only; content read as four columns. |
| Section 11 phrasing (RP:812) | "Require the UI designer to state ..." is a paper recommendation (OPINION), treated here as a rule from data, not as an instruction to this agent. |
| Source numbering gaps | M10 and M14 are not in the register and not cited in this slice. |
