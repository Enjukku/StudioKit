> Author: researcher (vfx-gap-research workflow) · claude-sonnet-5-5 · default · 2026-10-12

# Gap run: telegraph lead times, danger-zone visuals, reaction-time literature, low-health effects

Scope note: most named sources (WoW, FFXIV, Destiny 2, Elden Ring, Monster Hunter, Hades II, Returnal, Apex, Valorant) gave NO first-hand telegraph number. Searches returned fan wikis, forums and listicles. Nothing was invented. Result: one peer-reviewed simple-reaction-time anchor, one spec for flash/pulse limits, several qualitative studio statements, and a long "still open" list with tests.

## 1. Search count used

15/15 WebSearch (the last two returned only snippets). WebFetch calls: 21 (3 returned nothing usable: Bungie accessibility page, hal.science PDF (access denied), biae.clemson.edu (host not found)).

## 2. Sources read

| id | title | author/studio | year | tier | URL | pre-2020? | what it gave |
| --- | --- | --- | --- | --- | --- | --- | --- |
| G01 | Factors influencing the latency of simple reaction time | Woods, Wyma, Yund, Herron, Reed; Frontiers in Human Neuroscience 9:131 | 2015 | study (peer-reviewed) | https://pmc.ncbi.nlm.nih.gov/articles/PMC4374455/ | yes (2015); no newer one opened | Visual SRT means, age slope, SD, response window (last 15,791 chars not read) |
| G02 | Understanding SC 2.3.1: Three Flashes or Below Threshold | W3C WCAG 2.2 | 2.2 (2023) | spec | https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html | no | Max 3 flashes/s, area, luminance, red-flash definition |
| G03 | Avoid flickering images and repetitive patterns | Game Accessibility Guidelines (consortium of game accessibility practitioners) | live 2026 | C (named community standard, no author) | https://gameaccessibilityguidelines.com/avoid-flickering-images-and-repetitive-patterns/ | no | Game-specific flicker limits; red transitions flagged; offer disable option |
| G04 | Ensure no essential information is conveyed by a fixed colour alone | Game Accessibility Guidelines | live 2026 | C | https://gameaccessibilityguidelines.com/ensure-no-essential-information-is-conveyed-by-a-fixed-colour-alone/ | no | 8-10% of males red/green difficulty; colour plus symbol/shape; orange vs blue for two teams |
| G05 | The VFX Artist's Guide to Area of Effect | VFX Apprentice (no byline; page date shown "Sep 25, 2026", may be a modified date) | 2026? | C (no named artist) | https://www.vfxapprentice.com/blog/area-of-effect-aoe-in-games | no | Perspective and decal advice, indicator vs hitbox sizing, one 2 s example |
| G06 | Area of Effect (AoE marker page) | FFXIV Console Games Wiki (community) | live | D | https://ffxiv.consolegameswiki.com/wiki/AoE_marker | no | Orange default; red variants snapshot later; snapshot at telegraph disappearance |
| G07 | Designing for Difficulty: Readability in ARPGs | Alex Kubodera, Game Developer | 2022-04-19 | B (blogger) | https://www.gamedeveloper.com/game-platforms/designing-for-difficulty-readability-in-arpgs | no | Readability = telegraphing + expectations; Sekiro warning symbol plus sound as a crutch; no numbers |
| G08 | A third-person, action, roguelike, bullet-hell arcade thriller: The making of Returnal | Holly Green, Game Developer, reporting Harry Krueger (Housemarque) GDC 2022 | 2022-04-07 | B | https://www.gamedeveloper.com/marketing/a-third-person-action-roguelike-bullet-hell-arcade-thriller-the-making-of-returnal | no | No readability method; only 60 fps target and "simple and consistent" 3D visuals |
| G09 | Clarity in League | bananaband1t, Riot Games | 2021-03-12 | A | https://www.leagueoflegends.com/en-us/news/dev/clarity-in-league/ | no | Audio cue ahead of time (Zoe Q), audio wind-up (Taric), big ground circle can imply more dodgeability than real; hitbox must match effect |
| G10 | Spell indicator | League of Legends Wiki (community) | live | D | https://wiki.leagueoflegends.com/en-us/Spell_indicator | no | Indicator type list; only colour named is blue for range. Silent on fill/outline |
| G11 | Square Enix Q&A: How Omega Became a Boss in FFXIV | Matt Hilton, PlayStation.Blog (Yoshida/Nabeshima) | 2018-11-13 | B | https://blog.playstation.com/2018/11/13/square-enix-qa-how-omega-became-a-boss-in-final-fantasy-xiv/ | yes (2018) | Overlapping mechanics hectic; no telegraph numbers |
| G12 | The Color-Word Stroop Task Does Not Differentiate Cognitive Inhibition Ability Among Esports Gamers | Toth, Kowal, Campbell; Frontiers in Psychology 10:2852 | 2019 | study | https://www.frontiersin.org/articles/10.3389/fpsyg.2019.02852/full | yes (2019) | 4-key colour-box RT, 727-865 ms by group (NOT simple RT; see GAP 2) |
| G13 | Mental chronometry | Wikipedia (cites Kosinski 2008) | live | D | https://en.wikipedia.org/wiki/Mental_chronometry | no | Lead only: simple RT about 190 ms visual, 160 ms auditory; Hick formula |
| G14 | Tips from a combat designer: The art of boss design | Mike Birkhead, Game Developer (AltDevBlog) | 2012 | B | https://www.gamedeveloper.com/design/tips-from-a-combat-designer-the-art-of-boss-design | yes | No numbers |
| G15 | Design Tool: Signs & Feedback | Nicolas Kraj, GDKeys | 2020-03-16 | C | https://gdkeys.com/design-tool-signs-feedback/ | no | No numbers; green poison AOE example only |
| G16 | A behind the scenes look at the effects in Hades | Arti Sergeev, 80 Level (artist Josh Barnett) | 2020-10-08 | B | https://80.lv/articles/a-behind-the-scenes-look-at-the-effects-in-hades/ | no | Nothing on telegraphs |
| G17 | The Impact of Dark Souls on Boss Design | Josh Bycer, Game Developer | 2021-07-19 | B | https://www.gamedeveloper.com/design/the-impact-of-dark-souls-on-boss-design | no | Nothing on telegraphs |
| G18 | Search snippets only (NOT opened pages): SULFUR low-health mod, Minecraft feedback post, Steam threads, Icy Veins on WoW Midnight boss timeline, Bungie accessibility post, Olive Press esports RT | various | various | D | see section 6 | | Leads only; not cited as evidence except where marked "snippet" |

Pages that failed: hal.science Liu et al. CHI 2020 (Anubis access denied), Bungie accessibility post (page text empty), biae.clemson.edu Kosinski (host not found), Game Developer "Enemy Attacks and Telegraphing" second open (returned only boilerplate; already read in the first run as S10 there).

## 3. Gap-by-gap results

### GAP: Named-game telegraph lead times (WoW, FFXIV, Destiny 2, Elden Ring, Monster Hunter, Hades II, Returnal, Apex, Valorant)
Status: STILL OPEN (no tier A/B number found for any of them)

| finding | numbers | evidence level | source ids |
| --- | --- | --- | --- |
| [V: confirmed vs G06 - orange default, late display, snapshot at disappearance, red resolves later, 10 s LoS cast, chevrons/pulsing] FFXIV default ground AoE is bright orange; many high-end AoEs show the telegraph only right before the hit, so players read cast name or boss animation. Damage "snapshots" when the telegraph disappears, not when the hit animation ends. Some duties use red AoEs that resolve later after the telegraph vanishes. The page lists no lead time in seconds (only a 10 s cast for old line-of-sight AoEs, which have no telegraph) | no lead time found; 10 s cast (LoS) | tier D fan wiki, lead only | G06 |
| FFXIV Omega rework: the team added animations and effects but made no statement on telegraph timing; overlapping mechanics were called hectic | no number found | industry practice (Square Enix/PlayStation.Blog, 2018) [V: corrected - article is a Q&A by Matt Hilton (Square Enix community director) with Yoshito Nabeshima; no telegraph discussion; "hectic" confirmed. "Yoshida" in G11 row not confirmed] | G11 |
| Returnal (Housemarque GDC 2022 as reported): the report names no readability technique or number [V: corrected - "readability is a goal" removed: not in the article; it states simple, consistent visual messaging and a 60 fps target] | 60 fps target only | industry practice (secondhand report) | G08 |
| Riot: audio cue ahead of time and audio wind-up are used to warn; a large ground circle can imply more dodgeability than the real threat gives; hitbox must match the effect | no number found | industry practice (Riot, 2021) | G09 |
| Sekiro: a dedicated warning symbol plus sound marks perilous attacks, used as a crutch when patterns are hard to read [V: corrected - symbol (danger kanji) plus sound confirmed, marks attacks needing a specific counter; the "crutch" framing was not found in the article, drop it] | no number found | industry practice (blogger report, 2022) | G07 |
| Elden Ring, Monster Hunter, Hades II, Destiny 2, WoW cast bars, Apex, Valorant: no usable first-hand or tier B/C source found. Search results gave forum threads and listicles. A forum post claimed a parry delay of about 4 frames; unverified, tier D, not used | none | none | n/a |

### GAP: Riot "truthful indicators" examples
Status: PARTLY FILLED (the principle is confirmed; the phrase "truthful indicators" itself was not found in any page opened)

| finding | numbers | evidence level | source ids |
| --- | --- | --- | --- |
| Riot treats indicator accuracy as a clarity rule: hitboxes that do not line up with effects frustrate players; a big ground circle can overpromise dodgeability (the article's example is Arcane Comet, "not a champion ability"); Pool Party Renekton hitbox never changes while the model moves [V: confirmed, with correction - the big-circle example is Arcane Comet; Renekton is cited for distracting cosmetic animation] | no number found | industry practice (Riot 2021) | G09 |
| First-run file already holds Riot 2022 and 2020 statements (hitbox correctness ranked first) | see p3-scene.md V-06, V-09, V-25 | industry practice | (p3 S01, S05) |
| Third-party guide: player indicators slightly smaller than true hitbox, enemy indicators slightly larger. Not a Riot statement, no named artist [V: corrected - the guide calls this a "fun fact" about SOME games (descriptive, not a recommendation); no byline confirmed; page date Sep 25, 2026 as shown] | "slightly" (no value) | tier C only; needs second source | G05 |

### GAP: Minimum warning (ms) vs reaction-time literature
Status: PARTLY FILLED (simple visual RT is solid; choice RT and telegraph-specific data are not)

| finding | numbers | evidence level | source ids |
| --- | --- | --- | --- |
| Visual simple RT, bull's-eye target, Experiment 1 | mean 230.8 ms (N=1469); hardware-corrected 213 ms; SD 26.8 ms; youngest group 217.9 ms, oldest 239.1 ms; age slope 0.55 ms/year [V: confirmed - all values re-read in G01; text elsewhere gives youngest as 217.8, rounding only. "Bull's-eye target" not re-checked] | study | G01 |
| Experiment 2 | mean 237.8 ms (N=189); corrected about 220 ms; SD 27.8 ms; slope 0.45 ms/year [V: confirmed] | study | G01 |
| Historical Galton visual SRTs and prior-study range | Galton 181-189 ms (studies 1884-1893, ages 18-60); earlier studies 233 to nearly 400 ms [V: corrected - Galton range confirmed and dated 1884-1893 (so pre-2020 by far); the 233-400 ms range was in the unread tail or not located, so that part is V: unverified] | study (as reported in G01) | G01 |
| Response window used in the study | 110-1000 ms; minimum observed SRT not reported [V: confirmed for window; "not reported" not checked in the unread last 15,791 chars] | study | G01 |
| Mental chronometry summary: visual simple RT about 190 ms, auditory about 160 ms (Kosinski 2008); Hick: RT = a + b*log2(n+1) | 190 ms / 160 ms [V: confirmed - Wikipedia states these and cites Kosinski 2008, Clemson literature review; original still unopened] | tier D lead (Wikipedia citing Kosinski, original not opened). Pre-2020. Newer confirmation: G01 gives higher means (231 ms) for a lab visual task | G13 |
| Choice RT with 4 alternatives in a keyboard colour task (not a game dodge): mean 727-865 ms by group in the control condition; elite CS:GO players 727 ms, non-gamers 865 ms. The paper calls it a "simple choice reaction time condition" (colour-word box task, 4 keys inferred from key bindings; response is to ink colour) [V: corrected - label checked: not plain "simple RT"; values 727.02/748.67/785.38/864.50 ms and group order confirmed, authors Toth, Kowal, Campbell, Front. Psychol. 10:2852, Dec 2019] | 727.02 / 748.67 / 785.38 / 864.50 ms | study (2019; pre-2020) | G12 |
| Games rule of thumb already in first run: 0.25 s reaction floor, anticipation = reaction + trigger + buffer | 0.25 s | industry practice (GDKeys 2020) | p2 S09 |
| Inference for our telegraph floor: lab SRT is about 0.23 s for a stimulus-known, single-response case. A telegraph in a game also needs detection of which attack, a choice of direction, motor time for a phone tap or stick move, and render latency. So the S09 0.25 s is a hard minimum for the very simplest case, not a target | derived from 0.23 s + extras; no measured value for the extras | inference | G01, p2 S09 |
| Esports study (Bickmann et al., IJER 2021, Vienna Test System): pro/non-pro esports players and non-pro athletes did NOT differ in simple visual/acoustic/choice RT. ms values not read | no number found | study, snippet only (abstract not opened) [V: unverified - Bickmann 2021 not opened, no URL given] | G18 |

### GAP: Danger-zone colour and fill conventions
Status: PARTLY FILLED (conventions confirmed qualitatively; no hex, opacity or fill-timer numbers from a named source)

| finding | numbers | evidence level | source ids |
| --- | --- | --- | --- |
| FFXIV: bright orange for standard AoE, red used in some duties with later resolve, chevrons and pulsating rings for homing and radial types | no number found | tier D fan wiki | G06 |
| Third-person ground circles stretch into ovals; fixes named: camera-facing elements or thick vertical border rings; terrain-conforming shaders so the zone stays visible on stairs and slopes | no number found | tier C only; needs second source | G05 |
| Clearly defined outline matters more as number of targets grows; bright, saturated colours contrasting with the environment | no number found | tier C only | G05 |
| Fill-up countdown: no source read specifies a fill-based timer. One guide describes a vortex pulling particles inward as a countdown and a cast that "gradually solidifies" with brighter light toward completion (idea, not a measured rule) | one 2 s example only [V: confirmed - hypothetical swirling vortex giving "exactly two seconds"; "gradually solidifies" not re-checked: V: unverified] | tier C only | G05 |
| Colour must not be the only signal: use a back-up shape, symbol or pattern; red often looks darker to colourblind players; orange vs blue works for two teams | 8-10% of males with red/green difficulty [V: confirmed vs G04] | industry practice (GAG community standard) | G04 |
| Red transitions are flagged as seizure triggers (red flash definition: R/(R+G+B) at least 0.8 for one transition) | see GAP low-health | spec | G02, G03 |
| LoL indicators: types (circle, cone, line, ring, concentric) exist; only blue for range is named. Fill vs outline not stated | none | tier D | G10 |
| Hades: no source read describes its telegraph colour or fill | none | none | G16 |

### GAP: Low-health screen effects and vignette pulse rates
Status: PARTLY FILLED (an upper bound on pulse rate from spec; no studio pulse-rate number found)

| finding | numbers | evidence level | source ids |
| --- | --- | --- | --- |
| Upper bound on any repeated flash or pulse: no more than 3 general flashes and no more than 3 red flashes in any one-second period, OR flash area at most 0.006 steradians (25% of any 10-degree visual field; 341x256 px on a 1024x768 screen; 87,296 CSS px) | max 3 per second; 0.10 relative-luminance change for a general flash when darker state below 0.80 [V: confirmed vs G02 incl. 0.006 sr, 341x256 px, 87,296 CSS px, red ratio 0.8. Note: "25% of any 10-degree field" - area is a fraction of a small field, not 25% of the screen; the "(25% ...)" wording is correct but do not equate it with GAG's 25% of screen] | spec | G02 |
| Game-specific limits: more than 3 flashes per second over 25% or more of the screen; flashing sequences over 5 s; avoid flicker where possible; give a warning and an option to disable | 3/s, 25% screen, 5 s [V: confirmed vs G03; the page says "investigate providing" a disable option, softer than "offer"] | industry practice (GAG community) | G03 |
| A low-health vignette that fades in and out is a red-edge overlay, which falls under the red-flash rule if it pulses red fast and big. Inference: keep pulse at or below about 2 Hz (one cycle = one opposing pair = one flash) and mind area. 2 Hz is OUR safety margin under the 3/s cap, not a studio number | inference: under 3/s | inference | G02, G03 |
| Typical tuning in community examples: soft red vignette at 35% health, stronger critical at 15%, pulse on by default, adjustable opacity, thickness and pulse speed (one mod). A Minecraft player post proposes reddening edges with a louder heartbeat as health drops | 35% / 15% thresholds [V: unverified - snippet only, page not opened here] | tier D (mod page and forum, snippet only) | G18 |
| Accessibility: a player request to disable red low-health overlays, comparing them to head bob and screen shake | no number | tier D snippet | G18 |

## 4. Quotes used

| quote | who | source |
| --- | --- | --- |
| "an audio cue ahead of time" | Riot, Clarity in League, 2021 (as returned by fetch) | G09 [V: confirmed - exact wording "bright, saturated, and has an audio cue ahead of time", about Zoe's Q] |
| "hitboxes don't line up with their effects" | Riot, Clarity in League, 2021 (as returned by fetch) | G09 [V: confirmed - from "particularly when hitboxes don't line up with their effects"; apostrophe style differs only] |

## 5. Conflicts with first-run files

| first-run row | conflict | resolution |
| --- | --- | --- |
| p2-p12 section 4 "Reaction time": snippet "averages over 0.3 s; up to 3 s for novices" (tier D, not opened) | G01 measures visual simple RT at about 0.23 s mean (0.213 s corrected). Different task (known stimulus, single response) vs game telegraph (unknown attack, choice) | Consistent: 0.23 s is the lab floor; game-level 0.3 s+ needs a game source. Keep 0.25 s as a floor, not a target |
| p2-p12 S09 row "0.25 s reaction rule of thumb" | G01 supports it in magnitude (mean 231 ms, SD 27 ms, so about 16% of young adults are slower than 0.26 s if normal; inference, not measured) | No change; add G01 as study-level support |
| p3 V-06 / V-25 (indicator matches hitbox) | G05 says enemy indicators are drawn slightly larger than the hitbox and player indicators slightly smaller. Riot says indicator must match hitbox | Conflict between a tier C guide and Riot practice. Prefer Riot (match). Treat "slightly larger" as an untested option, tag tier C |

## 6. Still open and how we can test it ourselves

| question | status | test |
| --- | --- | --- |
| Lead time (ms) per attack class in WoW, FFXIV, Destiny 2, Elden Ring, MH, Hades II, Apex, Valorant | no tier A/B/C number found | Record 60 fps gameplay of 3 to 5 named attacks per game, count frames from first visual change to damage frame; label as our measurement. Report tier D for any wiki frame data |
| Minimum telegraph for our game on phone | no game-specific study found | Build a dodge-the-blast harness in Studio: vary telegraph 400, 600, 800, 1200 ms; metric = hit rate, on a 30 fps phone and a PC; start from 0.23 s lab floor plus 0.25 s buffer |
| Choice RT with n alternatives for a phone tap | no ms values for games found | Same harness with 1, 2, 4 safe zones; fit a + b*log2(n+1) |
| Danger colour hex, opacity, fill style | no named-source value found | A/B red vs orange, outline-only vs fill+outline, on 3 stage palettes; metric: time to spot the zone and misreads; add a shape/pattern backup per G04 |
| Fill-up timer vs pulse-only vs sound-only | no source | Same harness; measure early/late dodges |
| Low-health pulse rate and vignette size | spec cap only (3/s; 25% screen) | Test 0.5, 1, 1.5, 2 Hz with opacity under 40%; measure player comfort and flash-area under WCAG formula; ship a "reduce screen effects" toggle |
| Primary sources not reached: Bungie accessibility post (empty page), Liu et al. CHI 2020 (blocked), Kosinski 2008 (host down), Bickmann 2021 full text, Housemarque GDC 2022 slides, Blizzard Midnight design posts, Riot technology blog | unread | Try GDC Vault with a login, DOI links, and archive.org mirrors next run |

## Verification log

Checker: adversarial fact-check pass, 2026-10-12, WebFetch re-open of G01-G13 (G14-G17 not re-opened). No claim was proved false enough to delete.

| item | result |
| --- | --- |
| G01 numbers (means, N, SD, corrected values, slopes, window, Galton) | confirmed; "233 to nearly 400 ms" prior range not located (unverified); last 15,791 chars of G01 still unread |
| G12 label | corrected: paper says "simple choice reaction time condition"; 4-key task; values confirmed |
| G05 indicator sizing | corrected: a "fun fact" about some games, not a recommendation; the Conflicts row 3 wording "says enemy indicators are drawn slightly larger" should be read as descriptive. Resolution (prefer Riot) stands |
| G09 big-circle example | corrected: it is Arcane Comet (not a champion ability) |
| G08 Returnal "readability is a goal" | removed: not in the article |
| G07 Sekiro "crutch" | removed: not in the article |
| G11 | corrected: author Matt Hilton interviewing Nabeshima; no "Yoshida" confirmed |
| G02 / G03 / G04 / G06 / G13 numbers | confirmed |
| G18 snippet items (35%/15%, Bickmann) | unverified, tier D / snippet |
| Tier labels | G09 tier A is a developer-published post by a Riot designer (fair as A for Riot practice). G07 "B (blogger)" - the page itself labels the author "Blogger"; B is generous |
| FILLED status check | No gap is marked FILLED. All PARTLY FILLED statuses stand. The lower-case "Riot truthful indicators" status stands: principle partly supported, phrase absent |
| 2 Hz margin | stays labelled inference. Note GAG's 25%-of-screen and WCAG's 25%-of-a-10-degree-field are different area rules |
