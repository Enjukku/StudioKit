---
type: reference
scope: universal
status: active
updated: 2026-10-20
source: "owner-supplied research paper 'Game_UI_UX_Research_AI_Designer.txt' (ChatGPT, research date 2026-10-21), lines 437-1112, J002"
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-20

# UX research part B: motion records, accessibility, localization, measuring, process, sources

Reading rules. Cite as `RP:<line>` plus the paper's own ids (for example `RP:443 [M01]`). Tags are the paper's own: VERIFIED, EXPERIENCE, OPINION, UNSPECIFIED. Never upgrade a tag. UNSPECIFIED means "no value exists; do not invent one; resolve it by project test". The paper is data, not instruction. The `check` notes are the extractor's flags; nothing was changed. Section 7 lists all conflicts and gaps.

Tag key: VERIFIED = checked against an official doc or code example. EXPERIENCE = a studio or practitioner reported it. OPINION = the paper's own design judgement or adaptation. UNSPECIFIED = a field with no published value.

---

## 1. Motion record library (records 01-25)

RP:439 [OPINION specification structure]: this is a calibration-ready library, not 25 complete presets. All endpoints (from/to), easing, delay, scale pop and overshoot not labeled as published are UNSPECIFIED. Each contract is an original adaptation. A cited source supports only the stated number or the semantic precedent. Unknown fields must be approved by project testing before engineering treats a record as executable.

Column key: PUB = published numbers. Every field not named in PUB (from, to, easing, delay, and duration unless shown) = UNSPECIFIED. Contract = trigger → states. CANCEL/RM = cancel and reduced-motion rule. CAL = calibration test.

| # | Name | Property | PUB (tag, id) | Contract (trigger → states) | CANCEL / RM | CAL | RP |
|---|---|---|---|---|---|---|---|
| 01 | Ready check acceptance entrance | video fade-in | duration 200 ms [VERIFIED code example, M01]; from/to/easing/delay UNSPECIFIED | accept action → acknowledge at once → intro state → waiting/idle. Duplicate accept must not restart the effect | authoritative cancel overrides waiting; static accepted/pending states with equal text | player can tell own accept from whole lobby ready | 441-449 |
| 02 | Ready check video exit | video fade-out | duration 300 ms [VERIFIED code example, M01]; rest UNSPECIFIED | leave the video state; decorative playback must not delay the real state change | cancel stale playback, show correct new state; omit ornamental video | fast accept/cancel/timeout sequences never show an obsolete accepted state | 451-459 |
| 03 | Button acknowledgement | fill/outline emphasis (OPINION) | none; all UNSPECIFIED. Precedent U16/U17 (semantic only) | pointer-down or equivalent → local acknowledgement; action success stays separate | pointer-exit, disabled, focus change restore right visual state; static pressed/focus contrast stays | rapid repeats, touch occlusion, controller activation; no delayed hit-testing | 461-469 |
| 04 | Hover focus fade | opacity of highlight layer (OPINION) | none. Precedent U16/U17 | hover and keyboard/gamepad focus are separate states that may share emphasis; do not depend on hover | interrupt from current look, not via baseline flash; instant contrast change is enough | tab fast across dense items; emphasis never on a previous target | 471-479 |
| 05 | Small panel expansion | panel reveal/translation (OPINION) | none. Precedent U16/U17 | reveal info from its owning control; keep ownership and navigation focus | reversing a request must not queue another full transition; show final layout directly | players identify the opening control and dismiss without hunting | 481-489 |
| 06 | System toast arrival | position/opacity (OPINION) | none. Precedent U16/U17. Dwell time = separate UNSPECIFIED parameter | nonblocking event → concise toast → stable readable state | merge repeated events; keep reviewable history for important outcomes; no travel in RM | recall accuracy during gameplay, not noticeability in an empty menu | 491-499 |
| 07 | Important result expansion | panel reveal (OPINION) | none. Precedent U16/U17 | confirmed milestone → focused result → stable primary next action; no celebration for routine acknowledgements | skip to same final result; decoration never owns the confirmation event | completion time and result comprehension vs a restrained alternative | 501-509 |
| 08 | Background dimming | scrim opacity (OPINION) | none. Precedent U16/U17. No enterprise duration assigned to this game action | a genuine modal sets hierarchy; do not hold focus or input routing until the fade ends | restore prior focus on dismiss; static scrim is the RM equivalent | reversals; does the background change obstruct the task | 511-519 |
| 09 | Inventory reveal stagger | row or tile reveal (OPINION) | none. M12 gives a non-game stagger example (20 ms, see section 7), not this game record | stable navigation first; reveal inventory without hiding selectable info behind a parade | scroll, sort or new query cancels old waves; RM reveals all at once | long lists; last item time-to-interactive; change grouping rather than add delay without limit | 521-529 |
| 10 | Tactile press and return | scale/depth/shadow (proposed) | none. OPINION template [U14; M03] | press → held → release or cancel. Visual compression must not shrink the hit target | release outside restores baseline with no activation; contrast/border change replaces scaling | compare travel and compression against label legibility and pointer accuracy; record only measured/approved values | 531-539 |
| 11 | Focus indicator travel | position/size of focus indicator (proposed) | none. OPINION template [U16] | nav input selects the target at once; an optional visual bridge explains the move | retarget from current look; never queue every focus step; RM snaps to current target | held-stick repeat, wraparound; focus ownership always unambiguous | 541-549 |
| 12 | Tab spatial continuity | panel position/mask (proposed) | none. OPINION template [U15; U07] | sibling tabs move along one consistent spatial relation; hierarchical drill-down uses a distinguishable relation | latest tab wins; keep each tab's scroll where intended; RM = direct content replacement | ask users if they moved sideways in a category or deeper into one | 551-559 |
| 13 | Reversible modal entrance | panel transform/opacity (proposed) | none. OPINION template [U16; U17] | invoke → trap focus only when modal is active → settle → dismiss → restore focus. Arrival and dismissal need not share emphasis | reverse or go from current state, never wait; static panel and scrim | open/close spam, nested confirmation, connection loss, back button | 561-569 |
| 14 | Reward anticipation hold | progress/energy treatment (proposed) | none. EXPERIENCE seed, OPINION contract: Brawl Stars seasonal hold and duration as value signal [M17] | explicit open action → anticipation → reveal of an already valid result; say whether holding is required or only ceremonial | offer a non-hold equivalent and instant reveal where rules allow; keep any granted entitlement | hold-progress comprehension, fatigue over repeated rewards, alternative-input access | 571-579 |
| 15 | Rarity step up reveal | badge/material/color/shape transition (proposed) | none. EXPERIENCE seed, OPINION contract: historical Clash Royale staged rarity-upgrade taps [M16] | acknowledge each stage; show rarity with text/shape as well as color; end on a stable named reward | skip cosmetic stages, not the result; do not present input force or tap speed as an odds lever unless it is a real rule | do players understand what is interaction, presentation and the real random outcome | 581-589 |
| 16 | Batch reward summary | group/reveal transition (proposed) | none. EXPERIENCE seed, OPINION contract: Hearthstone one-by-one or all-at-once reveal leads to a summary [M09] | user picks ceremony or compact reveal; both reach the same complete, inspectable result | skip to summary; store entitlement separately from playback so interruption cannot lose rewards | return after interruption, duplicate-grant prevention, find one new item in a large batch | 591-599 |
| 17 | World to HUD reward transfer | projected position/path and scale (proposed) | none. OPINION template; M15 supports projection only | link pickup location to destination HUD counter, then show authoritative total. Freeze a source point or track it on purpose; do not mix coordinate spaces | static acquisition cue and counter update, no travel; missing/offscreen source falls back to destination-only feedback | camera motion, split-screen, safe areas, DPI scale, aspect ratios, source occlusion | 601-609 |
| 18 | Currency count up | displayed numeric value (proposed) | none. OPINION template [R22] | real balance updates atomically; display may interpolate toward it, with explicit delta and final total | new changes retarget without dropping value; skip shows true final number; RM = direct replace plus delta | very large gains, spend during count-up, negative changes, locale digit widths, screen-reader announcements. No one sound per unit at unbounded rate | 611-619 |
| 19 | Progress fill with milestone | fill extent/value (proposed) | none. OPINION template [C06; M06] | state delta → fill → crossed-milestone cue → new target. Separate real progress from simulated loading | retarget from the real displayed value; show exact new progress and crossed milestones statically | multiple level crossings, reversals, reconnect reconciliation; do users mistake decoration for usable gameplay resources | 621-629 |
| 20 | Confirmed hit marker | reticle overlay (proposed) | none. OPINION template grounded in M07 event distinction | authoritative hit event → legible marker plus matching sound; local firing feedback is a separate event | keep categorical confirmation without shake or expansion; never fake confirmation for a predicted miss | high fire rate, latency variance, head/body difference, target occlusion. Score information accuracy, not only apparent impact | 631-639 |
| 21 | Elimination critical event accent | categorical icon/text/accent (proposed) | none. OPINION template; M08 is audio-semantic evidence | confirmed critical/kill event has a distinct signature that does not steal aim attention or look like an ordinary hit | merge simultaneous events; static symbols/text and optional distinct audio remain | muted audio, peripheral vision, dense fights, ally/enemy, concurrency limits | 641-649 |
| 22 | Floating damage number | world-anchored or projected position/opacity (proposed) | none. OPINION template. No universal lifetime published | damage event makes a readable amount tied to the right target; merge or stack by a documented policy | stable anchored totals, shorter travel or optional suppression; never hide the aim point with a critical-number burst | overlap density, camera pans, target death, repeated damage, real phone performance | 651-659 |
| 23 | Cooldown charge ready cue | fill/pips/ready accent (proposed) | none. OPINION template; Destiny state-communication precedent [M06] | unavailable → charging → available. End matches real ability readiness, not the end of a decorative tween | changed cooldown/charge state cancels obsolete effects; static ready state plus optional sound carries it | peripheral recognition, multiple charges, cooldown modification, pause, server reconciliation | 661-669 |
| 24 | Restrained menu parallax | scenic layer translation/rotation (proposed) | none. EXPERIENCE seed, OPINION contract [M05] | scenic response adds depth while labels, focus and target acquisition stay stable. Separate mouse and stick policies | settle when input stops; RM disables scenic movement entirely | rapid mouse sweeps, edge positions, large screens, comfort feedback, relocating seen info | 671-679 |
| 25 | Frequency capped brand introduction | UNSPECIFIED | duration ≈2,800 ms (paper's conversion of ≈2.8 s) [EXPERIENCE observed duration; OPINION template, C02]; Brawl Stars reports once-daily display; from/to/easing/delay UNSPECIFIED | a brand moment must not repeatedly lengthen a short-session access path to fill a video timeline | launch proceeds when ready; static identity and a clear readiness state replace the animation | time-to-play and repeat-entry behavior, including loading finishing before the presentation | 681-689 |

Record 01 and 02 numbers (200 ms in, 300 ms out) are scoped to the League ready-check video only (RP:720 [VERIFIED, M01, 2017-02-14]). Do not read them as a studio preset (RP:861 [VERIFIED M01]).

### 1a. Exact builder handoff fields (RP:693, 695)

[OPINION] An approved record needs all of these fields; wherever one is UNSPECIFIED the record is incomplete [M01-M07; U17].

| field group | fields |
|---|---|
| Target | element; property and units; coordinate space; transform origin |
| Values | from/to; duration in ms; exact easing or spring parameters; delay/stagger |
| Behavior | trigger; loop/overshoot rules; completion event; input availability; interruption; repeat behavior |
| Markers | sound/VFX markers; reduced-motion variant |
| Proof | performance capture; source/version |

[OPINION] For world-to-HUD transfer, specify source point, destination counter and authoritative quantity separately from the travel effect. For damage, separate attempted action, confirmed hit and confirmed elimination. Define how simultaneous events merge or suppress each other. Align sound and visual effect to the same named semantic event; physical device audio/video latency still needs measurement [M07-M08; M15; R22]. RP:695.

[VERIFIED platform contract] Epic's projection API says whether a world position projects onto the screen and accounts for viewport scaling. It publishes no reward trajectory or timing and is not a Roblox recipe [M15]. RP:697.

### 1b. Recording review method (RP:699)

[OPINION recording method] Save: device, build, input, settings, original resolution, actual frame timebase. Mark: input, first visible response, information reveal, peak, settlement, next available action. Formula (known constant frame rate): elapsed ms = frame intervals × 1000 / frames per second. Variable-frame-rate footage needs timestamps. Do not infer one unique easing curve or full input-to-photon latency from a compressed recording. Review at normal speed, frame steps, muted audio, repeated use, reduced motion [M07; U17; R12].

### 1c. Roblox technique and performance constraints (RP:701-714)

| technique | supported use and risk (tag) | review requirement | id |
|---|---|---|---|
| Position / size / rotation / transparency changes | OPINION application; concurrency and layout work can matter | actual phone profile; no universal tween cost | R08 |
| Gradient sweep or shine | VERIFIED: UI effects can add GuiEffect work | reduce complexity if profiled as hotspot; no fixed ms claim | R08 |
| Stroke pulse | VERIFIED: tweening text-stroke thickness can rerender/store glyph sizes and flicker | prefer a tested alternative for text emphasis | R09 |
| Flipbook or sprite sheet | VERIFIED: texture memory and image-region techniques; world emitter flipbook limits are distinct | budget the whole sheet; do not claim native GUI particles from world docs | R07; R11 |
| Live 3D item preview | VERIFIED: viewport displays 3D content | test real geometry and concurrent previews; cost UNSPECIFIED | R10 |
| Screen-layer particles | OPINION design technique; not a documented native emitter guarantee | measure covered pixels and transparency overlap; static fallback | R11 |

- RP:712 [VERIFIED, R08-R11]: do not tween text UIStroke thickness (glyph variants can be rendered and stored; perf issue or flicker). Profiler guidance names UI amount, complexity, concurrent tweens and repeated layout work as possible costs, not a ranked price table. World ParticleEmitters: 100 particles/second mobile ceiling vs 400 otherwise; this is not a recommended GUI celebration budget. check: which of R08-R11 holds the 100/400 numbers is not stated (R11 key line is about fill-rate).
- RP:714 [VERIFIED, R12]: the device emulator helps aspect-ratio and control review but is not accurate for memory. Profile the live experience on supported phones. No universal frame-time or memory budget per effect is established.

### 1d. Motion evidence matrix (RP:716-724)

| rule | number | tag | source, date |
|---|---|---|---|
| Scope ready-check constants correctly | 200 ms in; 300 ms out | VERIFIED | M01, 2017-02-14 |
| Preserve repeat access to play | around 2.8 s logo; once-daily | EXPERIENCE | C02, 2026-07-10 |
| Keep non-game ingredients separate | 70-700 ms tokens; 20 ms example stagger | VERIFIED source scope | M11-M12, archived page updated 2025-08-19 |
| Complete records before implementation | 25 records; missing fields UNSPECIFIED | OPINION method | this library, 2026-10-21 |
| Profile actual phones | no universal ms per effect | VERIFIED evidence limit | R08-R12, accessed 2026-10-21 |

---

## 2. Accessibility rules (paper section 9, RP:727-767)

Numbers are XAG (Xbox Accessibility Guidelines) context, not an engine font setting or a universal law [U11]. XAG is design/testing best practice, not legal-compliance certification (RP:729). A single screenshot proves one criterion at most.

| id | Rule (imperative) | Tag | Numbers and units | Ids | RP |
|---|---|---|---|---|---|
| RB-01 | Treat XAG numbers as stated context only; do not turn them into an engine font setting or a universal rule. Do not claim compliance from a screenshot | VERIFIED | none | U11 | 729 |
| RB-02 | Console text: measure visible glyph height; at least this size | VERIFIED | 26 px at 1080p; 52 px at 4K | U12 | 737 |
| RB-03 | PC and VR text: measure visible glyph height | VERIFIED | 18 px at 1080p; 36 px at 4K | U12 | 738 |
| RB-04 | Mobile text: scale the minimum with DPI | VERIFIED | 18 px at 100 DPI; 36 at 200 DPI; 72 at 400 DPI | U12 | 739 |
| RB-05 | Support text scaling to 200% of the specified minimum without losing content or function | VERIFIED | 200% | U12 | 740, 903 |
| RB-06 | Measure text height from highest visible ascender to lowest descender; count edge pixels only above 2:1 contrast. Do not substitute nominal font size | VERIFIED | 2:1 (edge-pixel threshold) | U12; U13 | 746, 884 |
| RB-07 | Do not use platform screen magnification as the fix for small text | register key line (no tag given at the claim) | none | U12 | 1037 |
| RB-08 | Standard important text and visuals: contrast against the weakest relevant background | VERIFIED | at least 4.5:1 | U13 | 741 |
| RB-09 | Large text and visuals: contrast; the large threshold differs by platform and differs from web | VERIFIED | at least 3:1. Large = console 52 px at 1080p or 104 px at 4K; PC/VR 36 px or 72 px (1080p / 4K); mobile 36 px at 100 DPI, doubling with DPI | U13 | 742, 746 |
| RB-10 | Inactive text: keep contrast | VERIFIED | at least 3:1 | U13 | 743 |
| RB-11 | High contrast mode elements | VERIFIED | at least 7:1 | U13 | 744 |
| RB-12 | Sample the lowest-contrast part of changing or nonuniform backgrounds | VERIFIED | none | U13 | 746, 1039 |
| RB-13 | Never use color as the only information channel; add other sensory channels for critical cues (XAG 103) | VERIFIED | XAG 103 | U18; U19 | 750 |
| RB-14 | Give subtitles for speech and captions for important non-speech sound; identify speaker or location when unclear; make them available from opening content (XAG 104) | VERIFIED | XAG 104 | U18; U19 | 750 |
| RB-15 | Do not rely on haptics alone; hardware or preference can disable them | VERIFIED | none | U18; U19 | 750 |
| RB-16 | Do not read subtitle-adoption data as disability prevalence, retention effect or subtitle quality. Collection window and denominator not published | EXPERIENCE | 60% of Assassin's Creed Origins players enabled subtitles; 70% on PC | U09 | 752 |
| RB-17 | Do not assume Roblox's larger-text, preferred-background-transparency or reduced-motion preferences fix custom UI. TextScaled text ignores PreferredTextSize; layout constraints can cap growth. Specify and test the resulting variants | VERIFIED | none | R13 | 754 |
| RB-18 | Let players control discretionary moving, blinking, scrolling and auto-updating UI, and problematic camera effects (XAG 117) | VERIFIED | XAG 117 | U17; U20 | 756 |
| RB-19 | Test for photosensitivity over time, including unintended triggers (XAG 118). Criteria involve frequency, area, luminance, red flashes, spatial patterns. A simple under-three-flashes rule is not a safety certification | VERIFIED | XAG 118; "under three flashes" named only as insufficient | U17; U20 | 756 |
| RB-20 | Review the same task with enlarged text, stronger backgrounds, reduced motion, muted audio and supported digital inputs; check info and recovery route stay available. Use actual intended players for comprehension and accessibility; a checklist or color-vision simulation is a screen, not participant evidence | OPINION | none | U10-U20; R13 | 758 |
| RB-21 | Keep accessibility reachable at first launch; no required route may be unreachable | OPINION | no unreachable required route | adaptation of U15; U19 | 766 |
| RB-22 | Do not infer photosensitivity safety from a still image; temporal testing required | VERIFIED | none | U20 (updated 2026-03-04) | 767 |

Matrix rows (RP:762-767) restate: glyph height (U12, updated 2026-03-04); contrast 4.5:1 / 3:1 / 7:1 (U13, updated 2026-03-04); first-launch availability (OPINION, synthesis 2026-10-21); still-versus-temporal (U20, updated 2026-03-04).

---

## 3. Localization rules (paper section 10, RP:769-786)

| id | Rule (imperative) | Tag | Numbers and units | Ids | RP |
|---|---|---|---|---|---|
| RB-23 | Do not reserve a fixed text-expansion percentage. Short strings can grow much more than long passages. The W3C example: English "views" to Italian has a final-length ratio of 3, which is not a 300% addition. Guidance covers reflow, long compounds, taller scripts, forced abbreviations; it guarantees no percentage reserve for all languages | VERIFIED | final-length ratio 3 (example) | U21 | 771, 783 |
| RB-24 | Use concise, straightforward language when complexity is not needed. No universal reading grade, word count or reading-speed target is published for young players; the target stays UNSPECIFIED until the audience and task are tested | VERIFIED | reading grade UNSPECIFIED | U22 | 773, 785 |
| RB-25 | For each text container, specify wrapping, resizing direction, priority, line behavior and whether truncation is allowed | OPINION | none | U21-U22; R14-R16 | 775 |
| RB-26 | Never let a general ellipsis rule hide the distinguishing item name, price, odds, eligibility or material consequence. No hidden payment condition is allowed | OPINION | none | U21; R14-R16 | 775, 784 |
| RB-27 | Test real long translations, tall glyphs, mixed numbers and scripts, and right-to-left layout where supported. Pseudolocalization finds fragile boxes; it does not prove translation quality | OPINION | none | U21-U22; R14-R16 | 775 |
| RB-28 | Keep icon semantics testable; icons do not remove localization. Separate navigation arrows from world-direction, brand and object symbols before mirroring | OPINION | none | C04; U02; U15; U21-U22 | 777 |
| RB-29 | Recheck focus order after a mirrored layout | OPINION | none | U15 | 777 |
| RB-30 | For younger readers, observe comprehension of the action and its consequence; shorter is not automatically clearer | OPINION | none | U22 | 777 |
| RB-31 | Retest semantics and focus across locales; there is no universal icon vocabulary | OPINION | none | C04; U02; U15; U21 | 786 |

---

## 4. Measuring UI (paper section 11, RP:788-821)

| id | Rule (imperative) | Tag | Numbers and units | Ids | RP |
|---|---|---|---|---|---|
| RB-32 | Do not treat the Infinite Loot Box study as a motion recipe. 2×2 visual/audio manipulation; higher audio effects raised the number of boxes opened; other reported variables had no significant effect. More openings do not prove welfare or satisfaction | VERIFIED | 1,235 participants; 2×2 design | M18 | 790, 818 |
| RB-33 | Keep three questions apart: effect on repeated action, on progress, on revenue. No reviewed source gives a portable conversion gain for a button bounce, shine, rarity curve or celebration length. Do not read M18 as a mandate to intensify rewards | OPINION | effect size UNSPECIFIED | M18; U01; C04 | 792, 820 |
| RB-34 | Lock the measurement definitions in the contract table below before collecting data | OPINION | none | derived from cited studies | 796-808 |
| RB-35 | Completion rate = completed eligible users / exposed eligible users, for a defined milestone and window | OPINION | ratio definition | U01; U08; M18 | 808 |
| RB-36 | Report absolute percentage-point change beside relative change, with denominators and uncertainty | OPINION | none | U01; U08; M18 | 808 |
| RB-37 | A same-session reload is not automatically day-one retention | OPINION | none | U01; U08; M18 | 808 |
| RB-38 | Before an A/B test fix: hypothesis, changed feature, primary outcome, guardrails, exposure rule, randomization unit, analysis window. Check concurrent changes and novelty effects. Predefine device/audience segments; do not hunt a favorable subgroup afterward | OPINION | no universal sample size or duration | U01; U08 | 810, 819 |
| RB-39 | Use observation to study mechanism; use randomization to isolate a change where feasible | OPINION | none | U01; U08 | 810 |
| RB-40 | State what a screenshot cannot establish (see evidence-fit list below). A model-simulated user is not participant evidence | OPINION | none | U08; U10-U20; R12; M07 | 812, 821 |
| RB-41 | Do not infer a motion conversion lift from the cited studies | VERIFIED evidence limit | effect size UNSPECIFIED | M01-M09; M11-M13; M15-M19; C04 | 820 |

### 4a. Measurement contract (RP:796-806) [OPINION]

| measure | definition to lock | guardrail or companion |
|---|---|---|
| Task success | observable goal and assistance allowed | error, recovery, comprehension |
| Task time | start/end events and excluded waits | accuracy and frustration |
| Onboarding completion | eligible exposure and semantic milestone | unprompted repeat and return |
| Offer conversion | actual visible offer and completed purchase | accidental purchase, refund, comprehension |
| Retention | cohort, return event, time window, timezone | crashes and acquisition mix |
| Motion response | input acknowledgment versus semantic result | error rate, comfort, performance |
| Accessibility | named criterion and player task | actual participant experience |

### 4b. Evidence fits the question (RP:812) [OPINION]

| evidence type | can support |
|---|---|
| Still image | layout, some contrast, content checks |
| Recording | sequence, visible focus, interruption |
| Actual interaction | hit testing |
| Profiling | performance |
| Participants | comprehension |
| Field data | population behavior |

### 4c. Measuring evidence matrix (RP:816-821)

| rule | number | tag | source, date |
|---|---|---|---|
| Keep repeated interaction distinct from welfare | 1,235 participants; 2×2 | VERIFIED | M18, 2019 online; 2020 issue |
| Preserve denominators and scope | no universal sample size | OPINION | adaptation of U01; U08; synthesis 2026-10-21 |
| Do not infer motion conversion lift | effect size UNSPECIFIED | VERIFIED evidence limit | M01-M09; M11-M13; M15-M19; C04; synthesis 2026-10-21 |
| Match evidence to the question | still vs recording vs task | OPINION | adaptation of U08; U10; M07; synthesis 2026-10-21 |

---

Continued in [[reference/ui/06b-research-process-sources]].
