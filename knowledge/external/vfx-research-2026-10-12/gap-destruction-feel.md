> Author: researcher (vfx-gap-research workflow) · claude-sonnet-5-5 · default · 2026-10-12

# Gap fill: destruction feel (LEGO games, Siege, Battlefield, The Finals, Teardown, timing, perceived weight)

First-run file read first: `p4-destruction.md` (sections 5 Gaps, 6 Leads not followed, Verification log). Source ids here use the prefix G so they do not clash with S01-S35 there.

Headline, honest: no maker published a destruction-VFX talk with millisecond timings for crack, hold, fall, dust bloom or settle. The only hard numbers found are: (1) perception studies on weight and fall speed, (2) one forum-sourced miniature frame-rate rule, (3) two Roblox gravity values from the local docs, (4) physics-paper fragment-size exponents, (5) a 2-3 frame flash from a stylized explosion breakdown, (6) a few Teardown and LEGO scale facts. LEGO, Siege, Battlefield and Finals VFX stay mostly open.

## 1. Search count used

15/15 WebSearch calls. About 39 WebFetch calls (many returned little or failed; failures listed under section 2 "Pages that failed").

## 2. Sources read

Tier key as in the brief. "pre" = pre-2020.

| id | title | author/studio | year | tier | URL | pre-2020? | what it gave |
| --- | --- | --- | --- | --- | --- | --- | --- |
| G01 | The detail in Lego Star Wars: The Skywalker Saga is remarkable | Tom Baines, Thumbsticks, interviewing Danny Roberts (lead designer, TT Games) | 2019-06-26 | B | https://www.thumbsticks.com/detail-lego-star-wars-the-skywalker-saga-remarkable/ | pre | Every LEGO object is built by hand from individually modelled pieces, not swapped for approximate bricks when destroyed. Super Star Destroyer: "over 18 million bricks". Jabba's barge: "months to build", destroyed "in about two minutes". No VFX detail. [V: confirmed - quotes, date 2019-06-26, speaker Danny Roberts re-opened] |
| G02 | Skywalker Saga "Building the Galaxy" behind the scenes | thebrickfan (summarising a WB Games / TT Games video) | 2022-03-11 | D | https://www.thebrickfan.com/lego-star-wars-the-skywalker-saga-building-the-galaxy-behind-the-scenes/ | no | Weathering, sky colours, small details. Nothing on destruction. Opened, empty for our need. |
| G03 | Chaos Physics in LEGO Fortnite (session page) | Michael Lentine, Epic Games, GDC | 2024 | A (abstract only) | https://gdcvault.com/play/1034659/Chaos-Physics-in-LEGO-Fortnite | no | Confirms the talk exists (Chaos rigid bodies, destruction, networked physics, low-end platforms). Page has no slides, VFX, debris or numbers. Programming talk, not VFX. |
| G04 | Rendering (Siege) slides | Jalal El Mansouri, Ubisoft Montreal, GDC | 2016 | A | https://archive.org/download/GDC2016Mansouri/GDC2016-Mansouri.pdf | pre | PDF text extracted locally (pdftotext, 82 slides). One art-direction slide on destruction; render numbers only (see gap b). No dust or readability slide. [V: confirmed - re-extracted PDF locally: 10537 / 412 / 64 / 73%, GPU 14 ms, CPU 38 ms, "100s OF DEBRIS", big-went-on slide] |
| G05 | The Art of Destruction in Rainbow Six Siege: an interview with Julien L'Heureux | Ubisoft News | 2016-03-11 | A | https://news.ubisoft.com/en-us/article/4GHX2yepSaKkflLjLAlpwO/the-art-of-destruction-in-rainbow-six-siege-an-interview-with-julien-lheureux | pre | Materials "need to react logically and consistently". No debris, dust or timing. |
| G06 | Siege explosion changes blog (Y5S1) | Ubisoft | 2020 (year from search listing; page date not shown in fetch) | A | https://www.ubisoft.com/en-us/game/rainbow-six/siege/news-updates/1QkezaGoRkDWqcQ6duGvtk | no | Visual and audio cues on explosions; shrapnel holes show damage direction; damage calc runs in "a matter of milliseconds". Nothing on dust, debris or particles. |
| G07 | We spoke to DICE about Battlefield 6 destruction | Press Start (Australia), interview with DICE producer David Sirland | 2025-08-06 | B | https://press-start.com.au/features/2025/08/06/we-spoke-to-dice-about-battlefield-6-destruction-and-community-driven-evolution/ | no | Destruction must be "readable" and "deterministic"; needs "the fluffy part"; cracks and health state shown. No numbers. [V: confirmed - all five quoted phrases found, Sirland, 2025-08-06] |
| G08 | THE FINALS developer diary (World Building) news post | IDC Games | 2026-08-03 | B/D | https://idcgames.com/en/the-finals/news/the-finals-developer-diary-explores-the-creative-process-behind-building-the-games-iconic-arenas-2026-08-03-09-55-13582 | no | Text only: collapses open routes, walls open sightlines. No VFX, smoke, timing. Video not seen. |
| G09 | The Finals interview, Embark on balancing and destruction | mp1st (Stigsson, Tilleby, Grundberg of Embark) | 2023-12-15 | B | https://mp1st.com/news/the-finals-interview-embark-talks-balancing-destruction-and-more | no | Consistency of breaking matters for tactics; team explored "how much should we be able to destroy and how fast". No VFX, no numbers. [V: confirmed - Joakim Stigsson, 2023-12-15; full wording "how much should we be able to destroy and how fast and all that"] |
| G10 | Teardown design notes | Dennis Gustafsson, Tuxedo Labs | 2020-11-05 | A | https://blog.voxagon.se/2020/11/05/teardown-design-notes.html | no | Re-read for VFX: nothing on smoke, fire, dust or timing. Unbreakable walls make the environment "harder to read". Blog index (60 posts) checked: no post on smoke or fire. |
| G11 | Teardown and Voxel-Based Rendering with Dennis Gustafsson (SED1772 transcript) | Software Engineering Daily, host JN, guest Dennis Gustafsson (DG) | 2025-01-02 | A (maker interview) | https://softwareengineeringdaily.com/wp-content/uploads/2024/12/SED1772-Teardown.txt | no | 1 voxel = 10 cm (0:07:02); hundreds of millions of voxels (0:11:43); blown-apart pieces "fly and rotate and behave like actual objects" (0:04:05); in an EARLIER driving game, physics and destruction were "more like a decoration, more like a visual effect" (0:18:29), which he did not want. No smoke, fire, dust or particle talk. [V: corrected - voxel timestamp 0:08:20 -> 0:07:02, decoration timestamp 0:20:40 -> 0:18:29; the decoration remark is about a previous vehicle game, not Teardown's early destruction] |
| G12 | TT Games: behind Star Wars The Skywalker Saga (event page) | Manchester Animation Festival | 2022 | D (listing) | https://www.manchesteranimationfestival.co.uk/archive/2022/events/tt-games-behind-star-wars-the-skywalker-saga/ | no | Speaker list (animation, models, cinematics). No VFX or destruction in the listed topics. |
| G13 | Gravitational Acceleration as a Cue for Absolute Size and Distance | Hecht, Kaiser, Banks, Hart (NASA Ames) | 1994 | study | https://ntrs.nasa.gov/citations/20020006041 | pre | Abstract only. Observers use acceleration and velocity cues for size and distance; accuracy is below what free-fall dynamics would allow; projected size plus motion cues beats size alone. Published version: Hecht, Kaiser, Banks 1996, Perception and Psychophysics 58, 1066-1075 (known only from a search snippet, not opened). [V: unverified - NTRS abstract not re-opened in this check] |
| G14 | Intuitive physics of gravitational motion as shown by perceptual judgment and prediction-motion tasks | Vicovaro, Noventa, Battaglini, Acta Psychologica 194, 51-62 | 2019 | study | https://www.research.unipd.it/retrieve/e14fb26e-7f63-3de1-e053-1705fe0ac030/ActPsy2019.pdf (read as text locally) | pre (2019) | Implied mass changes judged natural fall speed and time-to-contact. Numbers in gap g. [V: confirmed - n=30, F(4,116)=28.27, eta2 0.17, 56.35 vs 51.05, 29.3 ms CI 15.8-42.8, 21 of 30, arrival times, 43 ms air-resistance; read locally from the PDF] |
| G15 | Falling and heaviness | Ujitoko, Kaneko, Yokosaka, Kawabe (NTT), Frontiers in Psychology 14:1042188 | 2023-03-28 | study | https://pmc.ncbi.nlm.nih.gov/articles/PMC10089262/ | no | n=78 analysed. Whether an object falls at all changes felt heaviness; fall speed above zero barely does. Numbers in gap g. [V: confirmed - 128 recruited / 78 analysed, F=4.7 eta_p2 0.058, F=240.0 eta_p2 0.756, gravity levels; post-hoc: only zero-fall differs from the non-zero levels] |
| G16 | Gravity prior in human behaviour: a perceptual or semantic phenomenon? | Gallagher, Torok, Klaas, Ferre, Experimental Brain Research 238 | 2020 | study | https://pmc.ncbi.nlm.nih.gov/articles/PMC7438378/ | no | Downward motion at 1 g is judged faster and more precisely than upward; n=20 analysed. About speed and duration, not mass or size. Little use for us. |
| G17 | MiniatureFormula thread (Cinematography Mailing List) | Jim Sofranko (DP), Geoff Boyle FBKS (DP), Art Adams (DP), Don Canfield | undated | D/C (named DPs, forum thread) | https://cinematography.net/edited-pages/MiniatureFormula.htm | n.d. | Rule: fps = 24 x square root of scale denominator. Worked examples. No derivation cited. [V: confirmed - formula, 166 / 144 fps, "test, test and test" by Sofranko, thread undated] |
| G18 | A Time Scaling: Scaling Laws in SFX Films | Matsuoka, Nakamura, J. Japanese Soc. for Experimental Mechanics 20(4), 229-236 | 2021 | study (abstract only) | https://www.jstage.jst.go.jp/article/jjsem/20/4/20_229/_article | no | Peer-reviewed paper exists on scaling laws plus high-speed photography for miniatures in SFX films (falling object in fluid as the example). Abstract page has no numbers; the PDF was over the fetch size limit (10 MB) and was not read. |
| G19 | Stylized Frag Launcher Explosion (Overwatch inspiration) breakdown | Atif, realtimevfx.com | 2017-06-06 | C | https://realtimevfx.com/t/stylized-frag-launcher-explosion-overwatch-inspiration-breakdown-posted/1894?page=2 | pre | 18 layers in 6 groups; instant flash about 2-3 frames; emitter start offsets differ by about 2-3 frames; exact offsets only in a screenshot I cannot read. Explosion, not collapse. [V: confirmed - quote, 2-3 frames, 18 layers / 6 groups, Atif 2017-06-06] |
| G20 | Generic behaviours in impact fragmentation | Sator, Mechkov, Sausset, arXiv:0709.4150 | 2007 | preprint (no journal info on the page I read) | https://ar5iv.arxiv.org/html/0709.4150 | pre | Fragment size follows a power law; exponent grows with impact energy. Numbers in gap f. [V: confirmed - alpha 0.70, beta 1.00, N=1457, V up to 3 with threshold 1.15, rock 0.65, tau 1 to about 2.5; page shows no journal reference and no submission date (ID 0709 implies Sept 2007)] |
| G21 | Roblox Creator Docs mirror: physics/units.md | Roblox | local mirror | spec | knowledge/external/roblox-creator-docs/physics/units.md (lines 105-125) | no | Default gravity 196.2 studs/s2 = 54.936 m/s2; "realistic" 35 studs/s2 = 9.8 m/s2. resources/beyond-the-dark/building-architecture.md line 59: closest real-world scale of one stud is 28 cm. [V: confirmed - units.md lines 121-127: 196.2 / 54.936 and 35 / 9.8; 28 cm at units.md:39] |

Pages that failed or gave nothing usable (so nothing is cited from them):
- PubMed 8920842 (Hecht 1996): cookie wall. NTRS 20040173123: timeout.
- APS Physics viewpoint v18/184 and Phys. Rev. Lett. 129, 078002: HTTP 403. xboxygen.com Finals article: HTTP 403. thegamer.com Siege debris article: HTTP 404 (same as first run). reachthefinals.com/news: HTTP 404. web.archive.org: blocked by the fetch tool.
- The Pixel Lab "Ground Destruction 3 Bursts" product page (opened): no timings, counts or author; D tier, unused.
- arXiv API queries (two): zero results.

Leads seen only in search snippets, NOT used as findings:
- Villermaux maximum-entropy fragmentation exponents 1.3 / 2.4 / 3.5 for 1D / 2D / 3D (APS Physics viewpoint 2025 per a snippet; page 403). Read it before use.
- "Explosions follow cube-root scaling, not square-root" and "ten times framing rate per three orders of magnitude of charge" (from a search summary of forum and technical pages; none opened).
- "Siege debris is computed on the client side, so each player sees different debris" and "debris stuck in a doorway can block sight" (thegamer.com snippet; page 404).
- Rory Payton self-written profile claims TT Games cutscene effects library for Skywalker Saga (twine.net; unverified, not opened).
- Embark "Dynamism Upgrade" French press: smoke will look "more natural" (snippet from xboxygen; 403).

## 3. Gap-by-gap results

### GAP: (a) LEGO games destruction VFX (TT Games, LEGO Fortnite, LEGO 2K Drive)

Status: STILL OPEN for VFX. Only scale and approach facts found.

| finding | numbers | evidence level | source ids |
| --- | --- | --- | --- |
| TT Games builds each model from individually modelled pieces and does not substitute approximate bricks on break. Implication for us: the break view and the intact view use the same bricks. | Super Star Destroyer: over 18 million bricks. Jabba's barge: months to build, about 2 minutes to destroy in-game. | industry practice (Danny Roberts, TT Games lead designer, 2019). Interview is trade press (B) and pre-launch. | G01 |
| Epic gave a 2024 GDC programming talk on LEGO Fortnite physics and destruction. No VFX content reachable; slides members-only. | no number found | industry practice (talk exists), content not read | G03 |
| No TT Games VFX talk, GDC session or artist breakdown for brick-break, stud pops or pieces was found. The 2022 TT Games festival session lists animation, modelling and cinematics, not VFX. | no number found | none | G12, G02 |
| LEGO 2K Drive: nothing found (one search covered it, no hit). | no number found | none | none |

### GAP: (b) Rainbow Six Siege dust and debris VFX, dust occlusion readability

Status: STILL OPEN for dust and readability. One art-direction line and render numbers found.

| finding | numbers | evidence level | source ids |
| --- | --- | --- | --- |
| The Siege rendering lead states the art direction for destruction in one slide: the player must feel something big happened. | Quote below. | industry practice (Ubisoft Montreal, GDC 2016, pre-2020) | G04 |
| Debris and destructible props are "generally smaller meshes but in great numbers", labelled "100s of debris"; poking holes in walls and floors degrades occlusion efficiency; walls and floors are procedurally generated unique geometry. The team used a material-based draw-call system because early prototypes were graphics-bound on CPU and GPU. | Material-based batching result: 10,537 unbatched draw calls, 412 batched total (vis + gbuffer + decals), 64 batched for shadows, culling efficiency 73%. (Pairing of numbers to labels follows the extracted slide text order; slide image not seen.) | industry practice (render cost, not VFX look) | G04 |
| Frame budget the destruction had to fit: target 60 FPS; GPU 14 ms average in non-combat; CPU max 38 ms linear on consoles; average 5 ms geometry, 5 ms lighting, 4 ms post. | 14 ms, 38 ms, 5 / 5 / 4 ms | industry practice (2016, console era) | G04 |
| 2020 explosion update stresses clear visual and audio cues and shrapnel holes that show where damage came from. This is readability by decals, not by dust. | no VFX number; damage calc "a matter of milliseconds" | industry practice (Ubisoft blog 2020) | G06 |
| Interview with the Realblast physics programmer covers material-consistent reactions only. | no number found | industry practice (2016) | G05 |
| Debris blocking sight and per-client debris: snippet only (page 404). Not a finding. | no number found | none | (lead) |

### GAP: (c) Battlefield 2042 / Battlefield 6 destruction VFX talks or interviews

Status: STILL OPEN for VFX numbers; only design intent found (design-intent items confirmed). [V: corrected - was "PARTLY FILLED"; no VFX evidence fills the gap]. No Battlefield 2042 source found. No GDC 2026 or other BF6 VFX talk surfaced.

| finding | numbers | evidence level | source ids |
| --- | --- | --- | --- |
| DICE producer David Sirland: destruction must be controlled, "readable" and "deterministic", not random; players should not face gameplay changes they cannot predict. | no number found | industry practice (DICE, interview 2025) | G07 |
| Early prototypes used plain boxes and coloured things; the team then found destruction needed the particles, effects and granularity ("the fluffy part"). They upgraded tech to show cracks and health state of a target. | no number found | industry practice (DICE 2025) | G07 |
| Destruction is meant to happen across a whole match; Bad Company 2 endgame had "no cover afterwards" (a lesson against total flattening). | no number found | industry practice (DICE 2025) | G07 |
| EA / Frostbite article (S01 in the first run) already covers seam and surface emitters by material; no new BF6 VFX source beyond it. | see p4 S01 | industry practice | (p4 S01) |

### GAP: (d) The Finals newer Embark talks 2024-2026

Status: STILL OPEN. No 2025 or 2026 Embark VFX talk found; the 2024 GDC talk is members-only and an engineering talk.

| finding | numbers | evidence level | source ids |
| --- | --- | --- | --- |
| No Embark GDC or SIGGRAPH talk on destruction VFX found for 2025-2026. The August 2026 developer diary text names no effects, smoke, dust or timing. | no number found | none | G08 |
| Embark design stance (2023): consistency (it must break the same way in different places) and "how much should we be able to destroy and how fast" were explicit design questions. | no number found | industry practice (Embark staff, 2023) | G09 |
| Smoke "more natural" in the announced Dynamism Upgrade: French press snippet only, page 403. | no number found | none (lead) | (lead) |
| First-run file already holds the Embark patch-note items (S03 to S06). | see p4 | industry practice | (p4) |

### GAP: (e) Teardown VFX (smoke, fire, debris dust) from Gustafsson

Status: STILL OPEN for VFX. Scale facts found; the VFX material may exist only in his social posts.

| finding | numbers | evidence level | source ids |
| --- | --- | --- | --- |
| Gustafsson's blog (60 posts, index read) has no post on smoke, fire or dust. His smoke experiments were shared on social media (pointer from 80 Level, already in p4 as S35). | no number found | industry practice (index of maker blog) | G10 |
| 2025 maker interview covers voxels, lighting, ray tracing, modding; it does not discuss smoke, fire, dust or particles. | no number found | industry practice (Gustafsson, 2025) | G11 |
| Scale and style facts: 1 voxel = 10 cm, aimed at the MagicaVoxel look; hundreds of millions of voxels in a scene. Detached pieces "fly and rotate and behave like actual objects". In an earlier driving game, destruction was "decoration" and he did not want that for Teardown; he wanted destruction that affects gameplay. [V: corrected - not Teardown's own early destruction] | 10 cm per voxel; "hundreds of millions" voxels [V: confirmed] | industry practice (Gustafsson 2025) | G11 |
| Readability: avoid unbreakable walls because they make the environment "harder to read". | no number found | industry practice (Gustafsson 2020) | G10 |
| In-game Smokegun exposes duration, amount, colour, gravity, drag (search snippet of a fan wiki; not opened). | no number found | tier D lead | (lead) |

### GAP: (f) ms or frame timing for collapse phases; debris size distributions

Status: collapse-phase timing STILL OPEN (no named source). Debris size: PARTLY FILLED from physics (not from games).

| finding | numbers | evidence level | source ids |
| --- | --- | --- | --- |
| No named source gives crack, hold, fall, dust bloom or settle timings in ms or frames. Closest: a stylized explosion breakdown says the instant flash lasts about 2-3 frames and emitter start times differ by about 2-3 frames between layers; timing is "critical" because most layers are short-lived. | flash 2-3 frames; layer offsets about 2-3 frames; 18 layers | industry practice (Atif, realtimevfx 2017, tier C, single source, explosion not collapse, pre-2020) | G19 |
| Real fragment sizes from impact follow a power law with exponent that rises with impact energy. In a 2D molecular-dynamics disk (N = 1457), exponent tau = 0.70 ln(V) + 1.00 (both +/- 0.01) for V between 1.15 and 3 (V = impact speed in simulation units). Experiments in the literature span tau of about 1 to 2.5. Rock impact: slope 0.65. | tau about 1 to 2.5; 0.70 and 1.00 fit constants; 0.65 | preprint (2007), physics not games | G20 |
| Inference for our game: if the number of pieces of mass m scales like m to the power minus tau, a higher tau means relatively more small pieces and fewer big ones. A harder hit should therefore produce a bigger share of small pieces. This is a physical prior to test, not a measured player-preference. | no player-preference number found | inference | G20 |
| Game-side debris size mix: Siege slide says "smaller meshes in great numbers" (no ratio); Control and Finals numbers are in p4. No named game source gives a big:medium:small:dust ratio. | no number found | industry practice (qualitative) | G04 |
| Commercial VFX packs list counts (for example 25 burst animations) but no timing or sizes. Unused. | 25 animations | tier D | (Pixel Lab page) |

### GAP: (g) Perceived weight and mass from motion; slow motion and scale (miniatures, Froude)

Status: PARTLY FILLED. Perception studies found with numbers. Miniature rule found only through a forum thread and a paper abstract. No study found that tests "slow motion makes things look big" directly.

| finding | numbers | evidence level | source ids |
| --- | --- | --- | --- |
| People hold a "heavy-fast, light-slow" belief. Virtual 6.5 cm spheres (polystyrene 5 g vs wood 55 g) fell from about 2 m. Low acceleration or velocity was judged natural for the light sphere; high values were judged natural for the heavy sphere. | n=30; 5 acceleration levels 0.5, 0.9, 1.3, 1.7, 2.1 g (g = 9.81 m/s2); constant-velocity levels 2.07, 2.78, 3.31, 3.82, 4.24 m/s; material x magnitude interaction F(4,116)=28.27, p<.001, eta2=0.17; mean naturalness 56.35 (accelerated) vs 51.05 (constant velocity) on 0-100 | study (2019) | G14 |
| Implied mass also shifts time-to-contact: the heavy sphere's estimated time-to-contact was shorter. | 29.3 ms shorter (95% CI 15.8 to 42.8 ms); real air-resistance difference 43 ms; 21 of 30 participants showed it; physical arrival times 946 / 705 / 586 / 513 / 462 ms for the five accelerations | study (2019) | G14 |
| Naive viewers did not clearly prefer 1 g accelerated motion over constant velocity. Fall duration still matters to feel, but the study found the heuristic dominating. | motion pattern effect eta2=0.016 (small); 0.9 g not rated significantly more natural than several other combinations | study (2019) | G14 |
| For felt heaviness of an object a user lifts, whether the object falls on release changes heaviness; how fast it falls (above zero) hardly does. Lifting speed had a far larger effect. | n=78 analysed (128 recruited); gravity 0, 2.45, 4.9, 9.8, 19.6, 39.2 m/s2; falling-speed effect F=4.7, eta_p2=0.058; lifting-speed ratio (0.25, 0.5, 1.0) F=240.0, eta_p2=0.756; "lighter when the falling speed was zero" | study (2023). Note: this is a lifting interaction on screen, not a VFX study. | G15 |
| Observers use both acceleration and velocity to judge absolute size and distance, but less accurately than physics allows; adding projected size and motion cues beats size alone. Newer confirmation of the size claim: none found in this run. | 3 experiments; g about 9.8 m/s2 as the cue | study (1994, pre-2020) | G13 |
| Downward motion at 1 g is judged faster and more precisely than upward. | n=20; PSE 766 ms (down ball) vs about 796-798 ms for other conditions | study (2020) | G16 |
| Miniature filming rule: over-crank by the square root of the scale denominator so gravity-driven motion reads as full size when played at normal speed (so the action looks slowed). | fps = 24 x sqrt(D/d); 1/48 gives about 166 fps; 1/36 gives 144 fps. The thread says "test, test and test" and gives no derivation. | tier D/C forum thread by named DPs, single source; a peer-reviewed paper on the same topic exists (abstract read, numbers not read) | G17, G18 |
| Roblox link (arithmetic from spec values): default gravity is 196.2 studs/s2 against 35 studs/s2 "realistic" for a 0.28 m stud. Ratio 196.2/35 = 5.6, so fall times at default gravity are shorter by sqrt(5.6) = 2.37 than real-scale falls. Example: a 10-stud (2.8 m) free fall takes sqrt(2x10/196.2) = 0.32 s at default and sqrt(2x10/35) = 0.76 s at "realistic". By the miniature rule, default Roblox gravity makes everything read as small / light / toy-scale; slowing time for dust or debris by about 0.4 pushes it toward "big". [V: confirmed arithmetic (5.6, 2.37, 0.32 s, 0.76 s); the "reads small / big" part is inference from a forum rule, no study tests it] | 196.2 vs 35 studs/s2; 2.37; 0.32 s vs 0.76 s | spec (values) plus inference (reading) | G21, G17 |

## 4. Quotes used

| quote | who | source |
| --- | --- | --- |
| "When destruction happens you need to feel that something big went on!" | Ubisoft Montreal (Siege rendering slide, as extracted from the PDF) [V: confirmed, 12 words] | G04 |
| "is built from over 18 million bricks" | Danny Roberts, TT Games | G01 |
| "in about two minutes in the game" | Danny Roberts, TT Games | G01 |
| "readable" and "deterministic" | David Sirland, DICE | G07 |
| "the particles, the effects, the granularity to it" | David Sirland, DICE | G07 |
| "how much should we be able to destroy and how fast" | Joakim Stigsson, Embark | G09 |
| "fly and rotate and behave like actual objects" | Dennis Gustafsson | G11 |
| "more like a decoration, more like a visual effect" | Dennis Gustafsson, about an earlier driving game [V: corrected - context] | G11 |
| "Timing is critical for each component because most layers are short lived." | Atif, realtimevfx | G19 |
| "the best thing to do is test, test and test" | Jim Sofranko, cinematography.net thread | G17 |
| "the participants judged the object to be lighter when the falling speed was zero" | Ujitoko et al. [V: confirmed, abstract] | G15 |

Note: the fetch tool summarises pages with a small model; quotes are as returned. Verify against the page before any outside use.

## 5. Conflicts with first-run files

| first-run file and row | conflict or update |
| --- | --- |
| p4-destruction.md section 5 "Slow fall for weight": "no game source; film side not found in budget" | Film side now found: the miniature over-crank rule (G17, tier D/C) and a paper (G18). Perception side now found (G14, G15). Still no game source. The row stays "test it ourselves" but now has a rule to test. |
| p4-destruction.md section 5 "Scale cues": only the LEGO film rule (S18) that toy-scale effects stay fast | Not a conflict, a pair. S18: effects that should read as toy are fast. G17: effects that should read as big are slowed by sqrt(scale). Both agree: speed carries scale. Our decision: toy bricks or real building. |
| p4-destruction.md section 5 "Ubisoft Siege dust design, DICE collapse VFX talk, Embark VFX talk: none found" | Still none. Added only: Siege art-direction line and render numbers (G04), DICE interview intent (G07). |
| p4-destruction.md section 5 "LEGO games destruction VFX: not found" | Still not found; added scale facts and the Epic talk existing (G01, G03). |
| p4-destruction.md section 5 "Debris size distribution: no number found" | Updated: no game number, but physics-paper exponents (G20). Do not treat physics tau as a game target. |
| p4-destruction.md section 2b "whole-building collapse" row: "no number found" for windup and dissipation | No change. G19 flash 2-3 frames is an explosion number, not a collapse number. |
| p4-destruction.md ledger row "~3 s stand, ~6 s fall (S34)" | Still the only collapse timing. No new source. |

## 6. Still open and how we could test it ourselves

| open item | test |
| --- | --- |
| Collapse phase timing (crack, hold, fall, dust bloom, settle) | Frame-step 3 clips of Teardown / Finals / Battlefield collapse at 60 fps and log each phase in frames (sources: our own captures, label them "measured by us"). Then build 3 phase timings in Studio and have 5+ viewers rate "heavy" 1-7. |
| Does slowing dust or debris make a brick building look bigger? | Same wall break at TimeScale 1.0, 0.6, 0.4 for dust only (Roblox emitter TimeScale 0-1, S33 in p4). Ask: toy or building? Predict from G17/G21 that about 0.4 reads biggest. |
| Fall speed and felt weight for bricks | Roblox Workspace.Gravity at 196.2, 98, 35 studs/s2 for the same debris drop; ask "which pieces feel heavier". G14 predicts a split between light and heavy materials, G15 predicts little speed effect once things fall. |
| Heavy-fast heuristic by material | Give heavy bricks higher fall acceleration and light bricks lower. G14 says heavy material tolerates faster. Test with 5 viewers. |
| Debris size mix by hit strength | Fragment sampler with tau from 1.0 to 2.5 (G20 range) by blast energy; rate "heavy" vs "too fine". Log live bodies and frame time. |
| Siege-style sightline loss from dust | Place a target brick behind a dust cloud; measure time until readable for dust life steps up to the 20 s Roblox cap (p4 S33). |
| LEGO game break feel | Capture Skywalker Saga and LEGO Fortnite breaks at 60 fps; log number of pieces, stud pops, piece lifetime in frames. Label "measured by us". |
| Teardown smoke and fire | Read Gustafsson's social posts on smoke (human with an account) and the Teardown mod API (p4 S23). Not reachable here. |
| Miniature scaling paper numbers | Read the full PDF of G18 (13 MB, over the fetch limit) with local tools after owner approval to download. |
| BF6 and Finals VFX talks | Check GDC Vault 2026 and Embark's YouTube developer diary video for the Dynamism Upgrade when accessible. |

## Verification log

Checked 2026-10-12 by an adversarial fact-check pass (WebFetch re-open plus local PDF text extraction). No WebSearch used.

| result | claims |
| --- | --- |
| confirmed | G01 quotes and numbers; G04 render numbers, frame budget, 12-word quote; G07 five phrases; G09 Stigsson quote; G11 voxel size, "hundreds of millions", "fly and rotate"; G14 all numbers (n=30, F, eta2, means, 29.3 ms CI, 21 of 30, arrival times); G15 all numbers and quote; G17 formula, 166 / 144 fps, quote; G19 quote, 2-3 frames, 18 layers; G20 fit constants, N, ranges; G21 gravity and stud values; Roblox arithmetic (5.6, 2.37, 0.32 s, 0.76 s) |
| corrected | G11 timestamps (0:08:20 -> 0:07:02; 0:20:40 -> 0:18:29). G11 "decoration" remark was about an earlier driving game, not Teardown; fixed in the source row, gap (e) row and quote table. Gap (c) status "PARTLY FILLED" -> STILL OPEN for VFX (design intent only). |
| unverified | G02, G03, G05, G06, G08, G10, G12, G13, G16, G18 not re-opened (G13 NTRS abstract, G16, G18 abstract-only; others only support "nothing found" statements). The 2016 Siege lead pairing of numbers to labels: the layout text supports 10537 unbatched, 412 batched, 64 shadows, 73% culling. G14/G15 are lab studies, not VFX studies; G20 is a physics preprint with no journal reference visible. |
| removed | none; no claim was proved false |
| status checks | (a) STILL OPEN ok. (b) STILL OPEN ok. (c) fixed above. (d) STILL OPEN ok. (e) STILL OPEN ok. (f) STILL OPEN ok for timing; the debris-size physics is preprint-level only. (g) PARTLY FILLED ok; the study cues are about naturalness and time-to-contact of falling spheres and on-screen lifting, not about VFX scale. |
