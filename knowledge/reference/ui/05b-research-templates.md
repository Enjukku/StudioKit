---
type: reference
scope: universal
status: active
updated: 2026-10-20
source: "owner-supplied research paper 'Game_UI_UX_Research_AI_Designer.txt' (ChatGPT, research date 2026-10-21), lines 1-440, J002"
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-20

# UX research, part A (paper lines 1-440): rules, numbers, templates, gaps (continued)

First part (source card, conventions, earlier sections): [[reference/ui/05a-research-rules]]. Citation rules are stated there.

## 4. Reusable templates and schemas

The paper proposes all of these as OPINION (adaptations), unless stated. They are handoff structures, not discovered studio templates (RP:368).

### T01 Decision record per screen (RP:254) OPINION [U03; U05-U07]

| field | content |
| --- | --- |
| goal | the player's current goal |
| info needed | what the player needs to know before choosing |
| actions | the choices available |
| consequence | what each action does |
| evidence it registered | how the player sees the action worked |
| recovery | how to go back, cancel, retry or undo |

Rule: reject a component that has no role here.

### T02 Attention inventory (RP:256) OPINION

| per visible element | note |
| --- | --- |
| priority | semantic importance |
| persistence | how long it stays |
| contrast | against its real background |
| size | rendered size |
| spatial isolation | space around it |
| motion | amount and type |
| sound | whether it plays one |

Review with a grayscale capture, a reduced-size capture and a normal moving capture. Salience must match priority.

### T03 HUD information contract (RP:258) OPINION

| class | rule |
| --- | --- |
| actionable now | stays discoverable while the action is possible |
| useful for planning | may sit in a stable secondary region |
| inspectable on demand | lives in a deliberate detail view |

### T04 Screen state and attention contract (RP:264-271) OPINION

| question | specification field | review evidence |
| --- | --- | --- |
| What is the current player decision | goal and next meaningful action | unprompted task attempt |
| What must remain visible | essential state, priority, persistence | busy gameplay recording |
| What can wait | on-demand detail and its access route | comparison and inspection task |
| What wins when signals conflict | capacity, replacement and overflow policy | maximum simultaneous status case |
| How is a change understood | trigger, acknowledgment, pending and result states | recorded transition and final state |
| How does the player recover | back, cancel, retry or undo destination | failure and interruption route |

### T05 Onboarding competence fields (RP:292) OPINION

Per intended lesson record: the observable player action; the environmental cue; the interface cue; the feedback; the recovery if the action is missed.

### T06 First-session plan (RP:294) OPINION

Name: first meaningful goal; first successful action; first reward; first voluntary repeat; first optional system introduction. Order depends on the game's loop. No universal minute for the shop (timing UNSPECIFIED, RP:307).

### T07 Onboarding funnel and abandonment points (RP:296-298) OPINION

| item | content |
| --- | --- |
| Funnel (7) | first controllable moment; first core action attempted; first successful action; unprompted repeat; first meaningful reward; free-play choice; defined return |
| Abandonment points (7) | entering the world; understanding the immediate goal; finding the control; performing the action; interpreting feedback; collecting a reward; choosing the next activity |
| Record | exposure; exits; active time; errors; assistance; technical interruptions |
| Diagnose apart | tutorial skip; crash; misunderstood instruction |
| No evidence for | a universal shop minute; an acceptable drop-off percentage |

### T08 Offer contract (RP:319) OPINION [U23-U25; R15-R16; R21-R22]

Fields: received item or entitlement; quantity; duration if any; price and currency; eligibility; whether the outcome is random; purchase limits; what happens after purchase. Preview and commit are separate. A card that hides ownership state, real cost or duration is incomplete.

### T09 Purchase state machine (RP:321, 329) OPINION

| state | note from the paper |
| --- | --- |
| inspect | preview of the offer (and, if random, odds detail) |
| review | price and terms |
| commit | the player's deliberate choice; block accidental repeat commit |
| pending | an understandable waiting state |
| confirmed | only now may a celebration run |
| failed | must never be masked by a celebration; must not imply an award that is not owned |
| recovered | the route back after failure or interruption |

Each state has a distinct visual meaning. Roblox adds: closing the prompt is not proof of delivery (R22, VERIFIED, RP:327). The paper's Roblox-side wording lists the states as preview, inspect odds, review price, commit, pending, delivery, recovery (RP:329).

### T10 Paid-random disclosure rules (RP:325, 329, 343) VERIFIED (R14), placement rule OPINION

| rule | detail |
| --- | --- |
| scope | Robux and indirectly purchased currencies, keys or tickets |
| show before purchase | all possible final outcomes and real numeric percentage odds |
| include | player-specific remaining outcomes and paid modifiers where they apply |
| totals | the real distribution totals 100%; rounded display allowed with a disclaimer (documented exception) |
| odds control | descriptive wording, not only an unlabeled info icon |
| restricted users | an eligible alternative, or a blocked paid-random path |
| placement | disclosure before commitment, not inside the reveal (OPINION) |

### T11 Ad rules as of 2026-10-21 (RP:333-337) VERIFIED (R17-R19; P04), design response OPINION

| item | rule |
| --- | --- |
| personalized ads | prohibited under age 18 (June 2026 Advertising Standards) |
| rewards for ad engagement | prohibited as an incentive for under-13 engagement |
| Rewarded Video | 13+ |
| non-rewarded age-appropriate formats | not under a blanket under-13 ban; the 2026 announcement permits specified all-age formats from 4 May (P04 effective 2026-05-04); integration docs include audiences aged 12 or younger |
| integrations | registered, moderated assets; conspicuous labels; campaign and user eligibility still control availability |
| known conflict | an Ad System Abuse example still lists under-13 users as ineligible without a format qualification (RP:335) |
| design response (OPINION) | require current format-specific eligibility; get policy-owner clarification for unresolved designs; do not invent an age gate or bypass platform decisions; reserve persistent or repeated disclosure space; design a fallback; keep essential progress independent of ad delivery |
| dates | R17 updated 2026-06-05 (RP:345) |

### T12 Compact style specification (RP:358-366) OPINION

| system | required decision | evidence to inspect |
| --- | --- | --- |
| shape language | action, selection, passive panel, warning, ornament roles | components in active and inactive states |
| color | semantic roles, contrast pairs, redundant non-color cues | real backgrounds and state combinations |
| type | display vs utility roles, glyph coverage, text scaling | small device and long locale strings |
| icons | meaning, silhouette, label requirement, smallest display role | recognition in context at real size |
| depth and materials | lighting, bevel, shadow, texture rules | consistency across a component family |
| layout | decision order, grouping, spacing, responsive variants | task route at each supported input |
| motion | information beat, repeat behavior, reduced alternative | normal and reduced-motion recordings |

Per row keep the source-supported principle and mark project values unresolved until tested (RP:368).

### T13 Asset handoff list (RP:376) OPINION

Editable sources; expected display sizes; alpha treatment; nine-slice guides; safe ornament zones; localized text dependencies; a tested export sample. Test the imported asset on the real background and phone before mass production. Changeable text, prices and quantities stay outside baked art.

### T14 Hypothesis record (RP:203) OPINION [U08; U10]

Fields: observed player failure; likely mechanism; alternative design; primary measure; guardrail; result that would disprove the hypothesis.

### T15 Reward and rarity sequence states (RP:435) OPINION [M09; M16-M17; R14]

Order (proposed, not a measured timeline): accepted opening; confirmed outcome; anticipation; rarity signal; legible identity and quantity; ownership settlement; return to action. A skip or repeat shortcut ends at the same confirmed result. Paid-random disclosure comes before purchase.

## 5. Case lessons (RP:50-63, 65-176)

All lessons are tagged OPINION in the paper's table. The "evidence base" column lists the tags the paper puts on the facts behind them.

| game (studio) | what to learn | what not to copy | evidence base | ids | RP |
| --- | --- | --- | --- | --- | --- |
| Brawl Stars (Supercell) | separate touch actions; readable battlefield; critical state by more than hue | exact controls without the same mechanics; hue-only identity | EXPERIENCE (C01, C02), OPINION (C03 reading); screenshot undated | C01-C03 | RP:52, 65-73 |
| Clash Royale (Supercell) | stable object identity; next goal visible; modes grouped by task | piling up categories and reward containers without clear differences; crowded monetization | VERIFIED (June 2025 changes) with EXPERIENCE rationale; EXPERIENCE (May 2026); OPINION (C07 reading, no card-hand claims) | C05-C07 | RP:53, 75-84 |
| Candy Crush Saga (King) | test icon meaning; group events by state; show claimable state where players look | interruptions or pressure justified only by monetization | EXPERIENCE + inspected artifact; no effect sizes; monetization fell while reception improved | C04 | RP:54, 86-91 |
| Monument Valley II (ustwo games) | visually functional scene before ornament; restrained palette | sparse UI as a rule for complex games; the impossible-architecture motif | EXPERIENCE (GDC 2018); OPINION (slide reading) | C08 | RP:55, 94-101 |
| Splatoon 3 (Nintendo) | collection, social identity and useful waiting; stable info frame | thematic navigation that removes fast direct exits | EXPERIENCE (C10, C11); OPINION (screens); C09 is the original game | C09-C11 | RP:56, 103-114 |
| Persona 5 (Atlus) | expressive outer framing with disciplined inner alignment; each gesture has a job | unreadable small display type; copied assets or letterforms | EXPERIENCE (session remit); OPINION (slide reading) | C12-C14 | RP:57, 116-123 |
| League of Legends (Riot) | shared materials and motion urgency across states; replaceable decorative layer | assuming web-client timing is a Roblox standard | EXPERIENCE (M01, M02); VERIFIED (font download, rights not established); OPINION (editorial composite, not a screenshot) | M01-M02; M20 | RP:58, 125-132 |
| Hearthstone (Blizzard) | physical effects that explain rule relationships; calm board, atmosphere at edges | motion that implies the wrong strategy or damage rule | EXPERIENCE (M03-M04, M21); no durations; OPINION (slide reading) | M03-M04; M21 | RP:59, 134-141 |
| Destiny 2 (Bungie) | status priority; stable grouping; input-sensitive spatial effects | controller parallax copied unchanged to mouse; channel counts as universal limits | VERIFIED (April 2024 account); EXPERIENCE (deferred channel, mouse tests) | U05; M05-M06 | RP:60, 143-151 |
| VALORANT (Riot) | high-contrast front end; trustworthy confirmation; persistent efficient navigation | removing efficient routes for visual minimalism | EXPERIENCE (Oct 2022 redesign); VERIFIED (Patch 5.10 restore) | U06-U07; M07 | RP:61, 153-161 |
| Fortnite (Epic) | test icons; group actions by player decision; redundant state cues; semantic color (red kept for urgent damage) | mistaking success for safe or intentional purchase UX; a historical (mostly Save the World) layout as current | EXPERIENCE (U02-U03, U26); VERIFIED (FTC order U23 as the purchase counterexample) | U02-U03; U23; U26 | RP:62, 163-170 |
| The Last of Us Part II (Naughty Dog) | discoverable configuration: presets plus fine control; remap, hold/toggle, narration, large HUD scaling, contrast, navigation cues | treating a large option count as proof of accessibility; the game's dramatic tone | VERIFIED (60+ settings, 3 presets); EXPERIENCE (preset motive); OPINION (menu reading) | U04 | RP:63, 172-176 |

## 6. Motion: principles and the numbers the paper calls real

### 6.1 Principles (RP:393-401), tags as in RA-94 to RA-100

1. Motion explains rules, state and consequence (H10). Test the rule the player infers.
2. Acknowledge immediately; anticipation may not withhold acknowledgment.
3. Staging marks the one information beat.
4. Overshoot, squash/stretch, follow-through are optional, and their numbers are UNSPECIFIED.
5. Separate cursor or focus target from scenic motion; tune or disable scenic motion by input and preference.
6. Idle and secondary motion need cancel and priority rules.
7. Reduced motion keeps state; it must not delete the only cue.
8. Provide a static fallback for low-spec clients (League experience, no Roblox cost claim).

### 6.2 Published numbers and their exact scope

| number | what it is | tag | scope the paper gives | allowed as a game default? | RP |
| --- | --- | --- | --- | --- | --- |
| 200 ms | Riot ready-check video fade-in | VERIFIED code example | component fade only; from, to, easing, delay UNSPECIFIED | No | RP:407; record 01 at RP:443 (beyond this file's range, read only to resolve the pointer) [M01] |
| 300 ms | Riot ready-check video fade-out | VERIFIED code example | component fade only; from, to, easing, delay UNSPECIFIED | No | RP:407; record 02 at RP:451 [M01] |
| 50 ms | illustrative timeline offset in a scheduling explanation | EXPERIENCE | explanation of scheduling, not a shipped token | No | RP:408 [M02] |
| about 2.8 s (approx 2,800 ms) | Supercell startup logo; shown once daily | EXPERIENCE | approximate observation; not an ideal celebration time | No | RP:409 [C02] |
| 20 ms | Carbon v10 table stagger; adjust the sequence within 500 ms | VERIFIED | archived non-game guidance; not a game preset | No | RP:410 [M12] |
| 70, 110, 150, 240, 400, 700 ms | Carbon v10 duration scale | VERIFIED specification | non-game enterprise-design ingredients; no game action is assigned one | No | RP:416 [M11] |
| 90-120 ms | Carbon microinteraction checklist | VERIFIED source distinction | not identical to the token scale | No | RP:427 [M11; M19] |
| 40 ms one way, 80 ms round trip | VALORANT network example | VERIFIED scope | confirmation latency, not hitmarker animation life | No (not an animation number at all) | RP:412 [M07] |
| 3 taps | Clash Royale Lucky Drops (March 2024) | VERIFIED historical feature | count of taps only; no ms or easing | No | RP:433 [M16] |

Carbon v10 curves [M11, RP:418-426], cubic Bezier control points, VERIFIED non-game ingredients:

| curve | control points |
| --- | --- |
| Productive standard | (0.2, 0, 0.38, 0.9) |
| Productive entrance | (0, 0, 0.38, 0.9) |
| Productive exit | (0.2, 0, 1, 0.9) |
| Expressive standard | (0.4, 0.14, 0.3, 1) |
| Expressive entrance | (0, 0, 0.3, 1) |
| Expressive exit | (0.4, 0.14, 1, 1) |

### 6.3 Plain statement on defaults

None of the numbers in 6.2 or the six curves is a game preset, and none is a Roblox default. The paper says so for Carbon ("not evidence of game-optimal values", RP:416) and for Riot (component fades only, RP:407). A skill may show them as "published ingredients" with scope. It may not use them as the timing of a Roblox reward, button, shop or HUD animation. The paper also says Carbon discourages bounce and stretch as part of its aesthetic, and Material introduced spring-based schemes in 2025, so neither settles playful overshoot or scale (RP:427). Any timing a designer needs must come from project testing and be marked PROPOSAL.

## 7. Conflicts and cautions the paper itself flags

| # | caution | tag | what to do (paper) | RP |
| --- | --- | --- | --- | --- |
| K01 | Ad policy conflict: an Ad System Abuse example lists under-13 users as ineligible with no format qualification, while the age-group, format and integration provisions say non-rewarded formats are not under a blanket ban. Neither proves eligibility for every ad or child | VERIFIED conflict, OPINION resolution | require current format-specific eligibility and policy-owner clarification; no invented age gate | RP:333-337 |
| K02 | Candy Crush: a qualitatively better win flow came with worse monetization; pop-ups returned; worst case of 11 interruptions between levels | EXPERIENCE | measure outcomes separately; do not copy pressure screens, badge overload or interruption volume | RP:89, 91, 197 |
| K03 | VALORANT: visual cleanup removed one-click navigation; Patch 5.10 restored it. Looks and task efficiency can diverge | VERIFIED | keep persistent efficient navigation | RP:157, 159 |
| K04 | Tutorials: playtime and levels rose in Foldit but return was not significantly better (p=.408); in Hello Worlds return was lower with contextual tutorials (17.96% vs 21.60%, p<.001) | VERIFIED | no universal tutorial uplift; do not call playtime retention | RP:191 |
| K05 | Fortnite is a UX case and a purchase counterexample; the FTC order concerned unwanted purchases and dark patterns | VERIFIED + OPINION | do not treat success as safe purchase UX | RP:46, 62, 313 |
| K06 | Epic's refund window is conditional (24 hours, not used or equipped, exclusions, Return Tickets separate) | EXPERIENCE | do not promise an unconditional refund | RP:315 |
| K07 | Touch-size sources use different units and scopes; Apple has a 44 pt baseline in other button guidance as well as the 44/28 game split; XAG targets exceed app baselines | VERIFIED | do not average; document the rubric | RP:220, 225 |
| K08 | R01 is a 2025 figure from a 10-K filed 2026-02-11, not 2026; phone and tablet are not split | VERIFIED | use it as planning context only | RP:216 |
| K09 | Carbon vs playful motion: Carbon discourages bounce and stretch; its 90-120 ms checklist differs from its token scale; Material now has spring schemes | VERIFIED | neither source sets game overshoot or scale | RP:427 |
| K10 | Published motion numbers cover single components, not whole sequences (Riot fades); VALORANT 40/80 ms is network time | VERIFIED scope | scope each number to its own animation | RP:407, 412 |
| K11 | Screenshots are undated or promotional (Brawl Stars), crop out parts (Clash Royale card hand), or are an editorial composite (League) | OPINION | no claims about reach, target size, accessibility, current production UI or exact styling | RP:68, 78, 131 |
| K12 | Destiny: channel capacities are not universal; the right-side channel was deferred; counterscroll hid data | VERIFIED + EXPERIENCE | do not export slot counts | RP:147, 149 |
| K13 | Historical Fortnite (mostly Save the World) is not the current Battle Royale UI; small unquantified tests | EXPERIENCE | do not infer type family, tap target or layout | RP:165, 167 |
| K14 | TLOU II: option count is not proof of accessibility; one menu is not whole-game conformance; dim warnings need measured contrast | VERIFIED + OPINION | measure contrast | RP:175 |
| K15 | Riot fonts (BeaufortForLoL, Spiegel) are downloadable, but per-component roles and reuse rights are not established | VERIFIED | do not copy fonts | RP:132 |
| K16 | Roblox safe areas: no fixed universal inset; percentage sizing is not enough | VERIFIED | use inset APIs, test | RP:229, 246 |
| K17 | Image guidance (512 max, below 256 small) is guidance, not an upload cap; importer acceptance of a GIF is not animation | VERIFIED | test the actual import | RP:372, 374 |
| K18 | Reported studio gains (L4D about 40% fewer deaths, startup 35 s to 5-6 s, gadget use up) are pre/post or observational, no controls or sample sizes | EXPERIENCE | do not use them as effect sizes or targets | RP:165, 193, 195 |
| K19 | Tags are per sentence. A case section mixes EXPERIENCE, VERIFIED and OPINION; a matrix row can carry one tag for a mixed claim (e.g. the "4 mobile cases" count is VERIFIED corpus count while the case choice is OPINION) | n/a | keep the tag of the sentence you cite | RP:38, 46, 185 |

## 8. Gaps: what the paper leaves UNSPECIFIED or unsupported (designer will need these)

Fill each from project testing and mark PROPOSAL; do not borrow a number from section 6.2.

| # | gap | paper wording | RP |
| --- | --- | --- | --- |
| G01 | Duration, delay, easing for any Roblox button, panel, toast, reward, shop or HUD motion | all absent endpoints, timing, easing and delays UNSPECIFIED | RP:439 |
| G02 | Overshoot, squash/stretch, scale-pop numbers | UNSPECIFIED | RP:397, 439 |
| G03 | Stage timing for a reward or pack reveal (charge, release, reveal, summary) | no per-stage timing; no ms or easing for drops | RP:431, 433 |
| G04 | Stagger value for game lists | only Carbon table stagger 20 ms (non-game) | RP:410 |
| G05 | Hearthstone effect durations | none published | RP:136 |
| G06 | Roblox-specific minimum touch target in any unit | only Apple pt, Android dp, Xbox mm are given; not proven Roblox thresholds | RP:220-225 |
| G07 | Minimum rendered text size and contrast ratio | rendered-text requirements are in paper section 9 (outside this file); this file gives none; TLOU dim warnings need measured contrast | RP:223, 175 |
| G08 | Roblox numeric inset values; topbar height | no fixed universal inset; use CoreUISafeInsets / DeviceSafeInsets | RP:229 |
| G09 | Phone vs tablet share on Roblox; 2026 platform split | not separated; 2025 only | RP:216 |
| G10 | Shop introduction minute; acceptable first-minute drop-off | no evidence; task experiment needed | RP:298, 307 |
| G11 | HUD slot count; buff capacity | no universal target | RP:149, 282 |
| G12 | Universal sample size for user testing | none | RP:203, 212 |
| G13 | Fonts, type sizes, palette codes, shadow values for any reference game | not published or not inferred | RP:129, 151, 159, 368 |
| G14 | Color-blind accessibility or touch accuracy of Brawl Stars UI; card-hand target sizes of Clash Royale | not established | RP:68, 78 |
| G15 | Effect of icons, grouping or redesign on retention; conversion lifts | no effect sizes; no universal ROI | RP:89, 165, 197 |
| G16 | Ad disclosure label size, placement and wording | not given; reserve persistent or repeated space | RP:337 |
| G17 | Roblox image sizes per UI role beyond "at most 512x512 unless large" and "small often below 256x256" | guidance only | RP:372 |
| G18 | Reduced-motion alternative per component | principle only; each motion record must define one | RP:366, 401 |
| G19 | Number of acceptable interruptions or pop-ups per session | only the worst case (11 between levels) | RP:89 |
| G20 | Rule for how long idle motion may run | "should not compete indefinitely" | RP:401 |
| G21 | Unresolved ad eligibility for specific formats and ages | requires policy-owner clarification | RP:337 |
| G22 | Meaning of source ids C13, U12, U13, U17, U18, U21, R12, R13 | not described in RP:1-440 | RP:16, 30, 32 |
