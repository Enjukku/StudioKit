> Author: researcher (vfx-deep-research workflow) · claude-sonnet-5-5 · default · 2026-10-12

# P4 Film/Anime case studies + P8 Flipbooks

Scope note: WebSearch budget ran out mid-run (limit 200 per turn, shared). Planned reads NOT done: Arcane/Fortiche, Bad Guys SIGGRAPH, Epic SubUV blending, soft-particle docs, GDC Guilty Gear body, Jujutsu Kaisen impact-frame sources. See section 5. Evidence levels: study | preprint | industry practice | spec | inference.

## 1. Sources read (opened and read with WebFetch/Read)

| id | title | author/studio | year | tier | URL | pre-2020? | what it gave us |
|---|---|---|---|---|---|---|---|
| S1 | The Return of Hand-Drawn and Stylized Effects Animation | Ian Failes, VFX Voice | 2022 | B | https://www.vfxvoice.com/the-return-of-hand-drawn-and-stylized-effects-animation/ | no | Spider-Verse explosions = 2D art on Houdini cards, particles/debris on 2s; Bad Guys sprite library + two-tone sims merged; Turning Red poof dissipation by subdividing shapes; Mitchells cards with brush textures; Rift emissive cards [V: confirmed - 2022-09-27; explosions on cards, particles/debris on 2s, "start from scratch with a piece of paper" and "couldn't tell" all in page] |
| S2 | Animation Platforms: Yoshiyama Yu, Tropical Rouge! Pretty Cure, and Sakuga as New Media | Alex Tai, Mechademia 16(2) | 2024 | A (peer-reviewed) | https://gwern.net/doc/anime/2024-tai.pdf | no | Impact frames: split-second, flash, found by frame-stepping; "bank cut" reuse plus added impact frame and effect layer; snappy spacing. READ PDF pages 1-13 (journal pp.121-133) as page images because the text layer was garbled. Pages 14-21 (pp.134-141 and notes) NOT read [V: unverified - PDF text layer garbled on re-open; metadata confirms Tai, Mechademia 16(2), 2024, pp.121-141, but "split second", Cure Flamingo and two-frame claims could not be checked] |
| S3 | Giving Across the Spider-Verse that crucial hand-made quality | Ian Failes, befores & afters (Grochola interview) | 2024 | B | https://beforesandafters.com/2024/01/10/giving-spider-man-across-the-spider-verse-that-crucial-hand-made-quality/ | no | Kismet linework: about 100M lines, about 1000 shots; lines draw on and erase; templates plus hand keyframes. No frame-rate content |
| S4 | Behind the amazing 2DFX in Across the Spider-Verse | Toon Boom (Finizio, Grochola interview) | 2023 | C (vendor interview, named artists) | https://www.toonboom.com/?p=16859 | no | 2D FX frame by frame; first film = 2D libraries on cards, sequel kept library only for rain drips and background fire/smoke; 2D<->3D handoffs; 6 2D FX animators, about 40 FX artists [V: confirmed - 6 2D FX animators, FX dept about 40 (Grochola's dept), 2023; library kept for rain drips, background fire/smoke] |
| S5 | 2D VFX behind Spot | 80 Level | 2023 | B | https://80.lv/articles/2d-vfx-behind-spot-from-spider-man-across-the-spider-verse/ | no | 2D draw-overs composited with linework tools. No timing numbers |
| S6 | "first CG animated movie ... dedicated inking team" | befores & afters | 2023 | B | https://beforesandafters.com/2023/06/28/this-was-the-first-cg-animated-movie-ive-ever-heard-of-that-actually-had-a-dedicated-inking-team/ | no | Variable frame rates 1s/2s/3s up to 6s; StepSets republishes scenes at other rates for FX sims; FX trickier to match [V: confirmed - "on 1s, sometimes 2s or 3s, right up to 6s"; StepSets] |
| S7 | Hobie animated with different frame rates per body part | befores & afters (Alan Hawkins) | 2023 | B | https://beforesandafters.com/2023/06/17/the-across-the-spider-verse-spider-punk-character-hobie-was-animated-with-different-frame-rates-for-different-parts-of-his-own-body-and-accessories/ | no | Jacket 4s, body 3s, some parts 2s, guitar lowest up to 6s; fewer frames "pop" more; do not let him steal the screen [V: confirmed - jacket 4s, body 3s, some parts 2s, guitar "6s sometimes"] |
| S8 | How DreamWorks lent a stylized look to Puss in Boots: The Last Wish | befores & afters (Mark Edwards) | 2023 | B | https://beforesandafters.com/2023/01/11/heres-how-dreamworks-lent-a-whole-new-brand-of-stylized-look-and-feel-to-puss-in-boots-the-last-wish | no | Most of film on ones; action on 2s/4s ("stepped animation"); dust and explosions = volume plus surface passes with hard edge; hand-drawn FX for fire; stamp maps [V: confirmed - "Most of the film is on ones"; action 2s or 4s chosen per shot; scalloping] |
| S9 | Wishing upon a star for Puss in Boots: The Last Wish | VFX Voice | 2023 | B | https://vfxvoice.com/wishing-upon-a-star-for-puss-in-boots-the-last-wish/ | no | "Scalping" volumes into sculpted meshes; textured custom glow replacing Gaussian glow; hand-drawn layer over sims, tools reused from The Bad Guys |
| S10 | Puss in Boots: The Last Wish returns to its fairy tale illustration roots | AWN | 2022 | B | https://www.awn.com/animationworld/puss-boots-last-wish-returns-its-fairy-tale-illustration-roots | no | Painterly edge, illustrated bloom/DOF, detail loosened toward periphery; wolf bar scene as "Goldilocks Zone" test |
| S11 | Spider-Man: Into the Spider-Verse (SideFX community article) | SideFX (Imageworks FX team) | 2019 | C (vendor write-up of makers' work) | https://www.sidefx.com/community/spider-man-into-the-spider-verse/ | YES | Hand-drawn FX library (explosions, muzzle flash, hits, smoke, steam, flame) packed in sprite sheets, UV frame switching on cards; explosions on twos then ones; rigid-body debris on twos; layers at different depths [V: confirmed - posted 2019-01-29; explosions "often animated on 2's - then shifted to 1's"; rigid-body geometry output on 2's] |
| S12 | The LEGO Movie: Construction, Animation and Demolition | Baillet, Heckenberg et al., Animal Logic, SIGGRAPH 2014 talk | 2014 | A | https://animallogic.com/wp-content/uploads/2023/07/The-LEGO-Movie-Construction-Animation-And-Demolition.pdf | YES | Voxel smoke/explosions/water simulated normally then replaced by bricks of matching size and shape; "Brick Blur" smear; 2000+ bricks; per-brick variation. No newer confirmation found [V: confirmed - authors Baillet, Heckenberg, Murphy, Sarsfield, Smith; "over 2000" bricks, "Brick Blur", voxel smoke/explosions/water replaced with bricks of matching size and shape, all in the PDF text; 2014 per ACM metadata] |
| S13 | The Building Blocks Behind The LEGO Movie 2 | Ian Failes, VFX Voice | 2019 | B | https://vfxvoice.com/the-building-blocks-behind-the-lego-movie-2/ | YES | Sweet Mayhem explosions hand-sculpted per frame in LDD, replacement animation, stop-motion feel; dust scattered semi-procedurally (bunches in corners); no motion blur [V: corrected - Theriault quote and 2019 date confirmed, but source says explosions were "hand-sculpted initially with LDD" with "procedural replacement animation like a stop-motion solution"; not purely hand-sculpted brick by brick for every frame] |
| S14 | Interview: Demon Slayer producer Yuma Takahashi | Anime News Network | 2019 | B | https://www.animenewsnetwork.com/feature/2019-08-28/interview-demon-slayer-producer-yuma-takahashi/.149177 | YES | Water breathing almost all hand-drawn, little 3DCG in final composite; CG derived from hand drawings [V: confirmed - "almost all of those water elements are done by hand", little 3DCG] |
| S15 | Godzilla Minus One: Exceeding Expectations with Efficient Effects | nippon.com | 2024 | B- (general press) | http://www.nippon.com/en/japan-topics/g02409/ | no | 35-person VFX team; budget reportedly JPY 100-150M; heavy bass sound heightens destruction; panicked crowd expressions sell scale; analog rocking of planes/boats combined with CG [V: confirmed - 35 VFX staff, JPY 100-150M reported, "heavy bass sound", ~ planes/boats moved by hand] |
| S16 | Dune: Part Two VFX (Paul Lambert) | VFX Voice | 2024 | B | https://vfxvoice.com/?p=13144059 | no | Every explosion digital, practical desert explosions = behaviour reference; "super high explosive" reframing; plate-based as possible; distant explosion in a 35 s shot [V: confirmed - "Every explosion that you see is digital", 35-second all-digital shot, "super high explosive"] |
| S17 | Oppenheimer VFX (Andrew Jackson, DNEG) | VFX Voice, Fall 2023 | 2023 | B | https://vfxvoice.com/?p=13138572 | no | Trinity from practical: pyro, cloud and water tanks, forced-perspective miniatures, high-speed photography for scale; 35mm for extreme high speed; about 150 VFX shots, about 30% in-camera; mostly 2D compositing of photographed elements [V: corrected - 150 shots, ~30% in-camera, 35mm high speed, miniatures confirmed, but the page attributes these figures to VFX producer Mike Chambers (published 2023-10-04); Andrew Jackson attribution not confirmed from this page] |
| S18 | Roblox Creator Docs mirror: effects/particle-emitters.md, ParticleEmitter.yaml, ParticleFlipbookMode and ParticleFlipbookLayout enums | Roblox | local mirror | Spec | knowledge/external/roblox-creator-docs/ (local) | n/a | Flipbook layouts, max 30 fps, modes, random start, blend frames, LightEmission, memory warning [V: confirmed - ParticleEmitter.yaml: FlipbookFramerate max 30 fps; OneShot ignores framerate, uses Lifetime divided by frame count] |
| S19 | Sprite sheet length vs cost? | realtimevfx.com: Keith, Partikel | date not shown (thread id 1595, likely pre-2020) | C | https://realtimevfx.com/t/sprite-sheet-length-vs-cost/1595 | likely YES | Cost is texture size not grid; most sheets 8x8, rarely above 1024; 30 fps needs 30 frames/s; DXT1 RGBA = 2x RGB [V: corrected - thread posts dated 2017-02-02 to 02-04 (Partikel, Keith, digzelot), so pre-2020 = YES; "rarely can push above 1024", RGBA = 2x RGB under DXT1 confirmed] |
| S20 | Increasing flipbook based effects duration | realtimevfx.com: iNeeDzv, BlazejOrlowskiVFX, Limeslushie, windksr | 2024 | C | https://realtimevfx.com/t/increasing-flipbook-based-effects-duration/27592 | no | 9x9 at 2048; channel packing 64 frames per channel = 192; frame stride plus motion vectors; warning on motion-vector memory and shader cost |
| S21 | Flipbooks and Texture Sheets | vfxdoc.readthedocs.io (author not named) | n.d. | D (corroboration only) | https://vfxdoc.readthedocs.io/en/latest/textures/flipbooks/ | unknown | Power-of-two dims, crop frames, edge fix, loop needs longer source |
| S22 | Niagara Flipbook Baker Quick Start | Epic Games docs | UE5, n.d. | Spec | https://dev.epicgames.com/documentation/en-us/unreal-engine/niagara-flipbook-baker-quick-start-guide-in-unreal-engine | no | Defaults 8x8 / 1024 / 128 px tiles / 30 fps; match authoring rate; non-divisible tiles waste pixels [V: confirmed - 8x8, 1024, 128 px, 30 fps; 10x10 at 1024 gives 102 px with 4 px padding; 30 frames at 20 fps = 20 unique] |
| S23 | Texture Sheet Animation module | Unity docs | current | Spec | https://docs.unity3d.com/Manual/PartSysTexSheetAnimModule.html | no | Start Frame randomises phase; Cycles; Single Row + Random Row (variant row per particle) |
| S24 | Flipbook Player block | Unity VFX Graph docs 17.5 | current | Spec | https://docs.unity3d.com/Packages/com.unity.visualeffectgraph@17.5/manual/Block-FlipbookPlayer.html | no | FrameRate vs Cycles mode; Random Full Cycle ends on last frame; Reverse; Clamp Blending |
| S25 | Exploring and Modernizing the VFX Methods of Diablo 3 | Nick Seavert, JangaFX | n.d. | C | https://jangafx.com/insights/diablo-3-vfx-experiments | n.d. | Scrolling-noise alternative to flipbooks (flipbooks "show repeating patterns"); UV scales 0.25/0.5/1/2; alpha composite suits emissive not smoke |
| S26 | GDC Vault: GuiltyGearXrd Art Style (page only) | Junya Motomura, Arc System Works | 2015 | A (abstract only) | https://gdcvault.com/play/1022031/GuiltyGearXrd-s-Art-Style-The | YES | Abstract only, body members-only. No numbers. Not used as evidence |
| S27 | Sub-uv and material tex coords | realtimevfx.com: cEssex, Luos_83, Famosines | n.d. | C | https://realtimevfx.com/t/sub-uv-and-material-tex-coords/30543 | n.d. | Gradients/noise applied after SubUV jump between sub-frames unless matched to sheet tiling; weak |
| S28 | Dynamic Brushstrokes: Sakuga in Anime | nihonnarratives substack | n.d. | D | https://nihonnarratives.substack.com/p/sakuga-animation | n.d. | Lead only: Nakamura smears, Naruto animators "break the rules of physics" on impacts |

Opened but gave nothing usable (not cited as evidence): befores & afters Godzilla six-minute page (video only); befores & afters ActionVFX/Godzilla (paywalled summary: stock smoke, dust and fire elements helped combine the CG creature); Epic Niagara sprite renderer page (empty); Unity soft-particles URL and Wikipedia Impact_frame (404); forums.jangafx.com (shutdown redirect).

Counts: Tier A 2 read (S2, S12) plus 1 abstract-only (S26). Tier B 13 (S1, S3, S5, S6, S7, S8, S9, S10, S13, S14, S15, S16, S17). Tier C 6 (S4, S11, S19, S20, S25, S27). Tier D 2 (S21, S28). Spec 4 (S18, S22, S23, S24). About 27 pages used.

## 2. Findings

### 2a. Field methods (film and anime)

| field | method | what it does to the viewer | how to use it in a game | evidence level | source, tier and year |
|---|---|---|---|---|---|
| timing (punch) + shape | Impact frame: a one-to-few-frame abstract high-contrast drawing (hot red/white outlines on black, converging jagged lines) inserted at the hit | Flash of force, too brief to inspect, rewards frame-stepping | Spawn a large billboard/screen flash at the punch moment for 1-3 frames (about 50-100 ms; inference), 2 colours, radial lines. Only on big hits. Roblox: static single cell (FlipbookFramerate 0), LightEmission 1, Lifetime about 0.05-0.1 s | industry practice for the method; frame count = inference | S2 (A, 2024). Source says "split second", no frame count [V: unverified - Tai text unreadable; 1-3 frame / 50-100 ms is inference as stated] |
| timing (punch) | Reuse a sequence ("bank cut") and add an impact frame plus effect layer for the special version | Same attack feels upgraded when added frames land | Reuse one hit sheet; add impact-frame card and one extra layer for combo/finisher/upgraded hits | study (one animator's case) | S2 (A, 2024). Two frames added to the finisher; no other number [V: unverified - "two frames added" not checkable in garbled Tai PDF] |
| timing | Large spatial distance between poses with high drawing count feels much faster | Snappiness | Large jumps between flipbook positions or short fast debris lifetime, not slow fades | study (author's viewing analysis, not measured) | S2 (A, 2024) |
| timing | Variable frame rate: most film on ones, action on 2s/4s, hand-picked per element | Stepped, hand-made, punchy | FX flipbooks at 12-15 fps with FlipbookBlendFrames=false (24 fps film on 2s = 12 unique/s; 30 fps game on 2s = 15). Keep the peak on a higher rate | industry practice | S8 (B, 2023), S6 (B, 2023), S7 (B, 2023), S11 (C, 2019) [V: confirmed - S6, S7, S8 rates verified; 12-15 fps is inference] |
| timing (punch) | Explosions on twos, shifted to ones for emphasis; rigid-body debris on twos | Stepped look matches characters; smoothness marks the peak | Two-stage flipbook: stepped expansion, short higher-rate burst at peak; debris updates stepped | industry practice | S11 (C, 2019, pre-2020); newer partial confirmation S1 (B, 2022): particles and debris on 2s [V: confirmed - S11 and S1 verified] |
| timing | Fewer frames "pop" more; keep the lowest-rate element from stealing the frame | Attention control | One stuttery accent layer per effect | industry practice | S7 (B, 2023) |
| shape + gameplay | Hand-drawn 2D elements on camera-facing cards, self-emissive with own lighting channel | Illustrated look, readable under any light | Flipbook billboards with LightInfluence 0, fixed colour | industry practice | S1 (B, 2022; Rift), S11 (C, 2019) |
| shape + value | Smoke split into tones (smoke tone, smoke layer, hotter layer); sims rendered two-tone | Graphic, readable, hides seam | Two emitters per puff: dark base smoke (LightEmission 0) plus hot core (additive); 2-3 value steps | industry practice | S1 (B, 2022; Spider-Verse, Bad Guys) |
| composition (seam) | Sprite library merged with two-tone particle sims so audience "couldn't tell" | Sprite and sim read as one effect | Pair flipbook puff with particles/trails in same palette and value range | industry practice | S1 (B, 2022; Matt Baer, The Bad Guys) |
| composition | Library layers placed at different depths | Depth and richness | Stack 2-3 flipbook layers with ZOffset/size differences | industry practice | S11 (C, 2019) |
| shape | Dissipation by subdividing cloud shapes over time rather than lowering opacity | Reads as drawn poof breaking up | Swap to a "smaller blobs" frame range at end of life or spawn child chips; avoid only Transparency fade | industry practice | S1 (B, 2022; Turning Red). Modified power-law timing; no numbers |
| shape + timing | Volume pass to sculpted hard-edged mesh ("scalping"/"scalloping") | Painterly hard edges with soft volume | Hard alpha-cutoff edges in sheets instead of soft gradients | industry practice | S8 (B, 2023), S9 (B, 2023) |
| colour | Textured custom glow instead of Gaussian | Painted glow | Textured halo billboard, not only Bloom | industry practice | S9 (B, 2023) |
| composition | Detail dialled down toward frame edges | Focus on heroes | Lower-detail effects for far impacts | industry practice | S10 (B, 2022) |
| gameplay (brick) | Replace simulated smoke/explosion/water with bricks of matching size and shape; hand-sculpt per-frame explosions with replacement animation | Toy stop-motion read | Explosion = brick-sized chunk puffs popping on and off per 1-2 frames, plus coloured smear bricks ("Brick Blur") for speed | industry practice | S12 (A, 2014), S13 (B, 2019); both pre-2020, no newer confirmation found [V: corrected - S12 confirmed; S13 is "hand-sculpted initially" plus procedural replacement animation, not purely per-frame hand work] |
| composition (brick) | Dust scattered procedurally, bunching in corners, thin in open areas; minimal physical smoke | Coherent toy world | Few dust puffs, denser in corners and at wall bases | industry practice | S13 (B, 2019) |
| timing | Stop-motion feel, no motion blur | Physical toy weight | No blur-style trails on bricks; short ghosts or smear bricks | industry practice | S13 (B, 2019), S12 (A, 2014) |
| shape + gameplay (anime) | Water-breathing almost all hand-drawn, CG derived from hand drawings | Cohesive painted look | Base look on authored sheets; 3D mesh/beam only carries the same drawing | industry practice | S14 (B, 2019); pre-2020, no newer read |
| gameplay (live-action scale) | High-speed photography with slow playback, forced-perspective large-scale "big-atures" | Bigger, heavier | Short hit-stop/time dip plus big debris cues near camera | industry practice | S17 (B, 2023). Slow-motion speed: no number found |
| gameplay (scale) | Distant explosion behind a human-scale subject; panicked crowd reactions | Scale by contrast | Big VFX in the distance plus small close debris crossing the camera | industry practice | S16 (B, 2024; 35 s shot), S15 (B-, 2024) |
| gameplay | Reframe blast as "super high explosive": dust, sand and rocks flying, not nuclear glow | Grounded violence | Chunky debris plus dust wave over glow-only flash | industry practice | S16 (B, 2024) |
| gameplay (audio) | Heavy bass heightens destruction | Weight | Low-end hit on every big flipbook, synced to punch frame | industry practice (critic quoted) | S15 (B-, 2024) |
| composition | Compositing of real photographed elements, mostly 2D | Real feel | Layer several authored elements, 2D-style | industry practice | S17 (B, 2023) |
| timing (windup, crescendo, follow-through) | No frame counts found for film destruction | n/a | n/a | n/a | no number found |

### 2b. Flipbook rules

| rule | numbers | why | source |
|---|---|---|---|
| Roblox layouts | None / 2x2 = 4 / 4x4 = 16 / 8x8 = 64 frames / Custom (FlipbookSizeX,Y); texture size an exact multiple of layout | Engine constraint | S18 (spec) |
| Roblox max rate | FlipbookFramerate max 30 fps; min/max range per particle allowed | Engine constraint | S18 (spec) [V: confirmed] |
| Frame spacing | Transparent spacing around each frame; mip filtering may need more | Prevents neighbour bleeding | S18 (spec); S21 (D) corroborates cropping |
| Loop vs one-shot | Loop cycles at FlipbookFramerate; OneShot ignores framerate and uses Lifetime / frame count; PingPong; Random crossfades. OneShot for explosion-then-fade, Loop for fire/aura | OneShot plays once and ends | S18 (spec) |
| OneShot rate arithmetic | 64 frames at Lifetime 1.0 s = 64 fps equivalent, above the 30 fps Loop cap. For 30 fps equivalent use Lifetime >= about 2.1 s, or a 4x4 (16 frames) at Lifetime about 0.5-0.8 s | Arithmetic | inference from S18 [V: confirmed - arithmetic holds: 64 frames / 1 s = 64 fps equivalent] |
| On 2s | 24 fps film on 2s = 12 unique frames/s. Roblox: FlipbookFramerate 12-15, FlipbookBlendFrames false (instant swap) | Hand-made stepped look | inference from S8, S11, S18 |
| Blending | FlipbookBlendFrames true = linear crossfade; false = instant swap | Smooth vs stepped | S18 (spec) |
| Random start | FlipbookStartRandom true; or FlipbookFramerate 0 + StartRandom = random static frame per particle. Unity: Start Frame, Cycles, Single Row + Random Row | Breaks identical playback; static random frames give debris variants | S18, S23, S24 (spec) |
| Other repetition levers | Randomise Rotation, size, Lifetime range, per-particle framerate range. Identical playback is the known problem; start-frame offset and UV distortion "help a little" | Repetition is noticed | S19 (C), S20 (C) for the problem; rotation/size levers = inference |
| Loop seams | Looping needs source longer than target length; Unity Random Full Cycle ends on the last frame | Avoid pop at wrap | S21 (D, corroboration), S24 (spec) |
| Match authoring rate | Baker default 30 fps; baking below authored rate repeats frames (30 frames over 1 s at 20 fps = 20 unique) | No wasted frames | S22 (spec) |
| Tile arithmetic | 1024 px at 8x8 = 128 px tiles (Epic default). 10 tiles at 1024 = 102 px, 4 px wasted, atlas jitter. Power-of-two texture, divisible tile count | Jitter, mips | S22 (spec), S18 (spec example 1024 8x8) |
| Sheet resolution | Most flipbooks 8x8, "rarely can push above 1024" except hero effects; 9x9 at 2048 and 8x8 at 2048 seen in community. Cost is texture size, not grid | Memory | S19 (C), S20 (C) [V: confirmed - S19 quote verified; dated 2017] |
| Resolution vs on-screen size | no number found in tier A-C for blur/pixelation thresholds. Working rule: cell pixels >= on-screen pixels at typical camera distance; test on phone | Avoid blur | inference; test plan in section 5 |
| Mobile memory | Clients auto-disable flipbooks when memory is low (older phones); use fewer unique animated effects, smaller textures, reuse textures | Mobile-first | S18 (spec) |
| Alpha cost | Unreal DXT1: RGBA = 2x RGB; separate alpha texture trades memory for a second lookup. No Roblox equivalent number | Memory | S19 (C, Unreal-specific) |
| Channel packing | 64 greyscale frames per R, G, B = 192 per sheet; needs decode shader; dissent that it is inconvenient. Not available in ParticleEmitter | More frames per memory | S19, S20 (C); N/A to Roblox |
| Motion-vector blending | Render vectors, skip frames (high stride), blend in engine; costs memory and shader complexity | Longer smooth effects | S20 (C). N/A to ParticleEmitter |
| Additive vs alpha | LightEmission 0 = normal blend, 1 = additive; grayscale texture with no alpha: use LightEmission 1 to hide darks; higher values glow in low light | Fire/sparks/glow additive; smoke/dust needs alpha (dark colour) | S18 (spec); S25 (C): alpha composite suits emissive, not smoke or fog |
| Recolour/tint | Tint via Color sequence over lifetime; author sheets in white/grey to tint (grey needs LightEmission 1) | One sheet, many colours | S18 (spec); greyscale advice S20 (C, Blazej) |
| Emission and lighting | Self-emissive cards independent of scene light (film); Roblox LightInfluence 0 keeps flat colour | Readable in any lighting | S1 (B, 2022); S18 property exists (Brightness/LightInfluence in yaml) |
| Soft particles near geometry | no number found; no soft-particle doc in mirror pages read (ZOffset exists) | Ground intersection lines | gap |
| Gradients after SubUV | Do not apply UV-based gradient/noise per cell; it jumps between sub-frames | Shader gotcha (not Roblox) | S27 (C, weak) |
| Mixing with meshes, beams, trails, lights, decals | Sprite library merged with two-tone sims; 3D debris geometry on 2s; cards plus draw-on lines as separate layer | Shared palette and timing hide the seam | S1 (B, 2022), S11 (C, 2019) |
| How film blends sprites with sim | Cards with procedural rays/particles inside; particles advected through partial sim become brush-texture cards; 2D artists draw over; compositing tricks | Seam hidden | S1 (B, 2022) |
| Library discipline | First film leaned on 2D libraries; sequel drew hero FX per shot and kept libraries for rain drips and background fire/smoke | Libraries read repeated on hero moments | S4 (C, 2023) newer than S11 (2019) |

## 3. Quotes used (15 words or fewer)

| quote | source |
|---|---|
| "the Jack-in-the-box of animation techniques" (Yoshiyama Yu) | S2, Tai 2024 [V: unverified - Tai PDF unreadable] |
| "start from scratch with a piece of paper" (Pav Grochola) | S1, VFX Voice 2022 [V: confirmed] |
| "traditionally hand-drawn and animated frame by frame" (Nikolaos Finizio) | S4, Toon Boom 2023 [V: corrected - source wording is "most of the 2D FX work in the movie is traditionally hand-drawn and animated frame by frame"; quoted fragment is a verbatim substring] |
| "Most of the film is on ones" (Mark Edwards) | S8, befores & afters 2023 [V: confirmed] |
| "sculpting each frame of the brick" (Mark Theriault) | S13, VFX Voice 2019 [V: confirmed - 10 words as part of "We're actually sculpting each frame of the brick..."] |
| "Every explosion that you see is digital" (Paul Lambert) | S16, VFX Voice 2024 [V: confirmed] |
| "rarely can push above 1024" (Keith) | S19, realtimevfx [V: confirmed] |

## 4. Conflicts between sources (newer first)

| topic | A | B | resolution |
|---|---|---|---|
| Library vs per-shot drawing | S11 (2019): sprite-sheet library of hand-drawn FX carried the first film | S4 (2023): sequel drew per shot, library for small background elements | Newer wins: libraries for secondary elements, author hero hits per effect |
| Spider-Verse "on twos" | Search snippets implied a strict on-twos style (not read, tier D) | S6/S7 (2023): variable 1s to 6s, per body part | Newer first-hand: rate chosen per element and shot |
| Oppenheimer practical vs Dune digital | S17: practical elements and high-speed photography | S16: all digital, practical only as reference | Both valid; shared scale cues: debris, dust, slowdown |
| "Scalloping" vs "scalping" | S8 spells scalloping | S9 spells scalping | Terminology only, same technique |
| Flipbooks vs scrolling noise | S25: flipbooks show repeating patterns | S19/S20/S23: flipbooks standard with randomisation | Use both; scrolling is not a ParticleEmitter flipbook feature |

## 5. Gaps

| question | why open | how we test it |
|---|---|---|
| Resolution vs on-screen size (blur/pixelation) | No number in tier A-C | Studio: same 8x8 sheet at 512/1024/2048, effect sized 2/6/12 studs at 10/30/60 studs distance, phone-resolution screenshots; log cell px / on-screen px where blur appears |
| Impact-frame length in frames; JJK/MAPPA and Demon Slayer technique detail | Only Tai 2024 (no frame count) and ANN; searches ran out | Prototype 1, 2, 3 frame flashes at 30 and 60 fps; owner picks; record |
| Windup/punch/crescendo millisecond timings in film destruction | No source gave them | Frame-step reference clips and log durations |
| Soft particles / depth fade in Roblox | Not found in mirror pages read | Grep mirror for depth/soft, then A/B at ground intersection in Studio |
| Additive vs alpha on grey sheets in bright scenes | Spec only | Screenshot matrix LightEmission 0/0.5/1 in day and night lighting |
| Arcane/Fortiche, Bad Guys sprite library detail, Turning Red SIGGRAPH, Epic SubUV blending, GDC Guilty Gear body | Search budget exhausted | Follow-up run with fresh search budget |
| Tai 2024 journal pp.134-141 and notes | Not read | Re-open PDF pages 14-21 |
| Slow-motion speeds for Oppenheimer | S17 gives none | Find Jackson interview or camera specs |

## 6. Leads not followed

| lead | note |
|---|---|
| beforesandafters.com/2024/11/20 ActionVFX Godzilla | paywalled; stock smoke/dust/fire elements combined CG creature (summary only) |
| beforesandafters.com/2024/02/21 Imageworks Across the Spider-Verse breakdown video | video, not read |
| Demon Slayer Infinity Castle Oscars making-of short | video; search summary only |
| sakugabooru / Sakuga Blog impact-frame posts | tier C/D, not fetched |
| nextbestpicture interview (Andrew Jackson, Giacomo Mineo, Oppenheimer) | tier D |
| Search summary claim: Oppenheimer high-speed cameras up to 2,500 fps (rumoured) and 360 fps (Photo-Sonics 35mm-4ER) | tier D, unverified, page not read |
| Diablo 3 GDC talk (Julian Love) via S25 | GDC Vault; scrolling technique, not flipbooks |
| Tuatara TFlow motion-vector package | vendor marketing |
| Know Your Meme impact frames, twinfinite, wrongeverytime blog | tier D |


## Verification log

Checked 2026-10-12 by an adversarial fact-checker (re-opened sources; WebSearch budget was exhausted, so only direct fetches were used).

| item | result |
|---|---|
| Claims proved false and removed | none |
| S13 (LEGO Movie 2) | Corrected. "Hand-sculpted brick by brick, frame by frame" overstated: source says "hand-sculpted initially with LDD" plus "procedural replacement animation like a stop-motion solution" (Theriault). Row 64 tagged. |
| S17 (Oppenheimer) | Corrected. The 150-shot / 30% in-camera figures are credited on the page to VFX producer Mike Chambers, not Andrew Jackson. |
| S19 | Corrected. Thread posts are 2017, so it is pre-2020 (was "likely"). |
| S2 (Tai 2024), tier A | Unverified. The PDF text layer is garbled in extraction and Project MUSE blocks fetches. "Split second", "Cure Flamingo", "two frames" and the "Jack-in-the-box" quote could not be confirmed. The 1-3 frame / 50-100 ms figure is inference, already labelled. Treat the tier A tag as metadata-confirmed only (Mechademia 16(2), 2024). |
| S12 (LEGO Movie 2014), tier A | Confirmed from PDF text. Note it is a SIGGRAPH 2014 talk abstract (a short talk, pre-2020), not a long peer-reviewed paper; "tier A" is generous. |
| S26 (Guilty Gear) | Not re-opened; abstract only, not used as evidence. |
| Not re-checked | S3, S5, S9, S10, S20, S21, S23-S25, S27, S28, Unity docs rows, the "Mitchells" and Turning Red details in S1. |

Gaps noticed:
- No tier-A source for flipbook or impact-frame timing numbers; every game-side frame count is inference or tier C.
- Missing obvious primary sources: Roblox DevForum or Creator Docs guidance on particle texture budgets, Spider-Verse SIGGRAPH talks (Imageworks), Tai pp.134-141, and a text-extractable copy of Tai for quote checking.
- The 15-word quote limit holds for all quotes in section 3.