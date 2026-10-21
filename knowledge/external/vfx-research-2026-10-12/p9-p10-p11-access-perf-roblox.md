> Author: researcher (vfx-deep-research workflow) · claude-sonnet-5-5 · medium · 2026-10-12

# P9 Accessibility, P10 Performance/Mobile, P11 Roblox: evidence base for the VFX designer agent

Scope: photosensitivity, motion options, colour-blind safety; overdraw, budgets, LOD, mobile; Roblox VFX features.
Evidence labels: study | preprint | industry practice | spec | inference. "D/" = `knowledge/external/roblox-creator-docs/`.
Web search budget ran out mid-run (shared limit), so several leads are unread (section 6). Every cited page below was opened and read (WebFetch or local file). WebFetch uses a summariser model; numbers marked **(summariser)** came through it, so spot-check before external quoting. ITU-R BT.1702-3 was read as raw PDF text (verbatim).

## 1. Sources read

Tier "A-std" = standard text. "Spec" = Roblox Creator Docs (engine capability only, not design evidence).

| id | title | author/studio | year | tier | URL | pre-2020? | what it gave us |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | WCAG 2.2 Understanding SC 2.3.1 Three Flashes or Below Threshold | W3C WAI | 2023 (WCAG 2.2) | A-std | https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html | no | general and red flash definitions, 3/s, 0.006 sr, 341x256 px @1024x768 (summariser) |
| S2 | Rec. ITU-R BT.1702-3, Guidance for the reduction of photosensitive epileptic seizures caused by television | ITU-R | 2023 (rev 3; first 2005) | A-std | https://www.itu.int/dms_pubrec/itu-r/rec/bt/R-REC-BT.1702-3-202311-I!!PDF-E.pdf | no (current rev is 2023) | exact flash, red, area, duration and pattern criteria (verbatim) |
| S3 | Xbox Accessibility Guideline 117 (moving content, camera, motion sickness) | Microsoft Game Dev | page updated 2026-06 | A (platform holder) | https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/117 | no | avoid or allow off: camera shake, bobbing, motion blur; Halo Infinite per-effect sliders 0-100% |
| S4 | Xbox Accessibility Guideline 103 (multisensory cues, colour) | Microsoft Game Dev | page updated 2026-06 | A (platform holder) | https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/103 | no | colour never alone; shape/pattern/icon/text; configurable colours; simulators are not a substitute for testing |
| S5 | GAG: Avoid flickering images and repetitive patterns | Game Accessibility Guidelines (expert group) | undated, live | B | https://gameaccessibilityguidelines.com/avoid-flickering-images-and-repetitive-patterns/ | n/a | game-focused trigger list, "never say epilepsy safe", Harding mention (summariser) |
| S6 | GAG: Ensure no essential information is conveyed by a fixed colour alone | GAG | undated | B | https://gameaccessibilityguidelines.com/ensure-no-essential-information-is-conveyed-by-a-fixed-colour-alone/ | n/a | 8-10% of males; orange vs blue for two teams; presets plus free choice |
| S7 | GAG: Provide an option to turn off / hide background movement | GAG | undated | B | https://gameaccessibilityguidelines.com/provide-an-option-to-turn-off-hide-background-movement/ | n/a | background-motion toggle; page does NOT cover screen shake |
| S8 | Photosensitive epilepsy | Epilepsy Society (UK charity) | undated | B | https://www.epilepsysociety.org.uk/about-epilepsy/epileptic-seizures/seizure-triggers/photosensitive-epilepsy | n/a | 3% of epilepsy; 3-30 Hz common, 16-25 Hz worst, up to 60 Hz; patterns; screen advice |
| S9 | Colour blindness | Colour Blind Awareness (UK) | undated | B | https://www.colourblindawareness.org/colour-blindness/ | n/a | 1 in 12 men (8%), 1 in 200 women |
| S10 | Prevalence of congenital colour vision deficiency among Black school children in Durban | Mashige and van Staden, BMC Research Notes 12:324 | 2019 | A (study) | https://pmc.ncbi.nlm.nih.gov/articles/PMC6558866/ | no | n=1,305; 4.2% M, 0.6% F; deutan > protan; cites Birch 2012: 8% M / 0.4% F European Caucasian |
| S11 | Color Universal Design (how to make figures friendly to colorblind people) | Okabe and Ito (both protanopes), Univ. Tokyo | 2002, rev. 2008 | A (makers/scientists) | https://jfly.uni-koeln.de/color/ | **pre-2020**; newer confirmation S4, S6 repeat the rules | 8% / 5% / 4% by ancestry; redundant coding; avoid red-green; dark-red caution |
| S12 | Flashing images in advertising | UK ASA (regulator) | undated | B | https://www.asa.org.uk/news/flashing-images-in-advertising.html | n/a | regulator points to Harding FPA or equivalent; no numbers on page |
| S13 | Elementalist Lux: 10 skins, 30 megabytes | Riot Games Tech Blog | 2016-12-14 | A | https://www.riotgames.com/en/news/elementalist-lux-10-skins-30-megabytes | **pre-2020**; no newer Riot VFX memory source found | 30 MB per skin; channel packing plus palette lookup cut texture memory about two-thirds |
| S14 | Performance Budgeting Using Effect Types in Niagara | Epic Games | UE5 docs | A | https://dev.epicgames.com/documentation/en-us/unreal-engine/performance-budgeting-using-effect-types-in-niagara-for-unreal-engine | no | global budget 0-1, distance and instance scale curves |
| S15 | Measuring Performance in Niagara | Epic Games | UE5 docs | A | https://dev.epicgames.com/documentation/unreal-engine/measuring-performance-in-niagara?lang=en-US | no | halved emitter counts at Medium removed overdraw layers; culling after 1 s unrendered |
| S16 | VFX Preset Performance Optimization | OVERDARE Studio docs (other UGC platform) | undated | B (platform doc) | https://docs.overdare.com/manual/studio-manual/asset-and-resource-creation/vfx-preset-budget | n/a | per-category max distance, instances, identical effects; general vs low-spec |
| S17 | VFX Graph Optimization | Snap Inc., Lens Studio docs | undated (5.x) | B | https://developers.snap.com/lens-studio/features/graphics/particles/vfx-editor/vfx-graph-optimization | n/a | additive overdraw view; 256/128 px particle textures; 32-copy batching |
| S18 | VFX optimisation in midcore games | Stanislav Stabrov, lead VFX, Azur Games (PocketGamer.biz guest piece) | 2026-08-04 | B | https://www.pocketgamer.biz/vfx-optimisation-in-midcore-games-commonly-overlooked-techniques-and-advanced-methods/ | no | concrete particle counts: 30 to 2, 300 to 20, 200 to 50; per-effect 3-10 |
| S19 | Particles' Flipbook Release | Roblox DevForum announcement (LightBeamRays) | 2022-10-21 | A (Roblox announcement) | https://devforum.roblox.com/t/particles’-flipbook-release/2029388 | no | flipbook textures square power-of-two, 8x8 to 1024x1024 |
| S20 | Analytics: Optimize low-end Android crash rates... | Roblox DevForum announcement (signal_zzz) | 2024-09-03 | A (Roblox) | https://devforum.roblox.com/t/analytics-optimize-low-end-android-crash-rates-server-memory-and-cpu-performance/3145364 | no | low-end = under 2 GB Android; out-of-memory is a leading crash cause |
| S21 | Real-world building and scripting optimization for Roblox | Peter "MrChickenRocket" McNeill (DevForum) | 2024-08-20 | C | https://devforum.roblox.com/t/real-world-building-and-scripting-optimization-for-roblox/3127146 | no | one draw call per emitter/beam; shadow lights; 500 calls / 500k tris / 1.3 GB targets |
| S22 | Performance considerations, improvements, and optimizations when making a game | Mystifine (DevForum) | 2020-10-12 (upd. 2023) | C | https://devforum.roblox.com/t/performance-considerations-improvements-and-optimizations-when-making-a-game/817499 | no | claim: `:Emit()` ignores automatic graphics-level particle reduction; quality/10 scaler sketch |
| S23 | Bleeding-Edge Effects on Mobile (abstract only) | Andy Saia, Level Ex, GDC 2020 | 2020 | A (abstract only) | https://gdcvault.com/play/1026744/Bleeding-Edge-Effects-on | no | abstract only; no numbers; not used for findings |
| S24 | Arm Mali Best Practices 2.1 announcement | Ben Clark, Arm | 2020-06-03 | A | https://developer.arm.com/community/arm-community-blogs/b/mobile-graphics-and-gaming-blog/posts/arm-mali-best-practices | no | page has no overdraw content; guide itself not read |
| S25 | Particle System optimization (Built-In RP) | Unity manual | 6000.0 | spec | https://docs.unity3d.com/6000.0/Documentation/Manual/particle-system-optimization.html | no | only GPU-instancing links; no numbers; not used |
| R1 | Particle emitters | Roblox Creator Docs | live | spec | D/effects/particle-emitters.md (https://create.roblox.com/docs/effects/particle-emitters) | no | Rate caps, flipbook, lifetime cap, fill-rate and overdraw warnings |
| R2 | ParticleEmitter class | Roblox API ref | live | spec | D/_api-reference/classes/ParticleEmitter.yaml | no | property semantics: Brightness, Flipbook*, LightEmission, LightInfluence, Rate, TimeScale, ZOffset, Squash, Emit |
| R3 | Beams, Beam class | Roblox | live | spec | D/effects/beams.md, D/_api-reference/classes/Beam.yaml | no | Segments default 10; n-1 segments for n keypoints; ZOffset |
| R4 | Trails, Trail class | Roblox | live | spec | D/effects/trails.md, D/_api-reference/classes/Trail.yaml | no | Lifetime 0.01-20 s default 2; MinLength/MaxLength; FaceCamera |
| R5 | Highlighting objects | Roblox | live | spec | D/effects/highlighting.md | no | 255 limit; first Highlight up to 1 ms GPU on mobile |
| R6 | Light sources, Light classes | Roblox | live | spec | D/effects/light-sources.md | no | Point/Spot/Surface roles; no cost numbers |
| R7 | Lighting, Technology enum | Roblox | live | spec | D/environment/lighting.md, D/_api-reference/enums/Technology.yaml | no | Voxel = 4x4x4 voxel map; ShadowMap; Future; Technology superseded by LightingStyle |
| R8 | Post-processing effects, Bloom/ColorCorrection/DepthOfField/SunRays/Atmosphere | Roblox | live | spec | D/environment/post-processing-effects.md, D/environment/atmosphere.md, D/_api-reference/classes/ | no | property meanings; Lighting vs Camera parent scope |
| R9 | Improve performance; Design for performance | Roblox | live | spec | D/performance-optimization/improve.md, design.md | no | overdraw, shadows off below quality 4, 1024 = 4x 512 memory, example budget 1,000 / 1M |
| R10 | Optimize your experience (environmental art) | Roblox | live | spec | D/tutorials/curriculums/environmental-art/optimize-your-experience.md | no | layered transparency overdraw explanation |
| R11 | Texture specifications | Roblox | live | spec | D/art/modeling/texture-specifications.md | no | 4096 and 1024 statements; texel guidance by object size |
| R12 | NumberSequence, ColorSequence | Roblox | live | spec | D/_api-reference/datatypes/NumberSequence.yaml, ColorSequence.yaml | no | 2-20 keypoints |
| R13 | Control the user's camera; UserGameSettings; SavedQualitySetting | Roblox | live | spec | D/tutorials/use-case-tutorials/input-and-camera/control-the-users-camera.md, D/_api-reference/classes/UserGameSettings.yaml, D/_api-reference/enums/SavedQualitySetting.yaml | no | BindToRenderStep at Camera+1; quality levels Automatic and 1..10 |
| P1 | Roblox performance checklist | project researcher | 2026-10-10 | internal | knowledge/reference/roblox-performance-checklist.md | n/a | prior audit; emitter status "UNCHECKED" |
| P2 | Roblox platform facts (mobile, physics, network) | project researcher | 2026-10-06 | internal | knowledge/research/roblox-platform-mobile-2026-10-06.md | n/a | phone runs interpreter; 1.3 GB rule; device tiers |
| P3 | Debris budgets | project researcher | 2026-10-06 | internal | knowledge/research/roblox-debris-budgets-2026-10-06.md | n/a | scene part budgets |

Count: tier A 13 pages (S1-S4, S10, S11, S13-S15, S19, S20, S23, S24; S23/S24 empty for our purpose), tier B 9 (S5-S9, S12, S16-S18), tier C 2 (S21, S22), spec 13 doc groups (R1-R13) plus S25, internal 3.

## 2. Findings

### 2a. Accessibility table

| rule | numbers | source | evidence level |
| --- | --- | --- | --- |
| General flash definition | pair of opposing luminance changes (up then down, or reverse) of at least 10% of max relative luminance (1.0), with the darker image below 0.80 | S1 | spec (standard) [V: confirmed] |
| General flash, broadcast form | darker image below 160 cd/m2: a difference of 20 cd/m2 or more is harmful. At or above 160 cd/m2: more than 1/17 Michelson contrast (HDR only). SDR peak white is 200 cd/m2, so 20 is 10% | S2 | spec (standard) [V: confirmed in ITU text; 1/17 rule is HDR-only as stated] |
| Flash rate limit | no more than 3 general flashes and no more than 3 red flashes in any 1 s. ITU: a sequence with more than three flashes (six luminance changes) in a second is not permitted ONLY when the combined flash area is also over 25% of the screen | S1, S2 | spec [V: corrected - original ITU clause omitted the AND 25% area condition; WCAG 3/s part confirmed] |
| Flash spacing that is always ok | leading edges of successive flashes 334 ms or more apart at 60 Hz (360 ms at 50 Hz), whatever the brightness or area | S2 | spec [V: confirmed] |
| Isolated flashes | single, double or triple flashes are acceptable; the sequence is the problem | S2 | spec |
| Flash area, WCAG | combined flashing area at most 0.006 sr within any 10-degree visual field. Proxy: 341 x 256 px at 1024 x 768 (87,296 px). Page words it as 25% of a 10-degree field. Test at the largest scale a user may view | S1 (summariser) | spec [V: confirmed numbers; page gives 25% of a 10-degree field as the plain form] |
| Flash area, ITU | a sequence is harmful when concurrent flash area exceeds 25% of the displayed screen AND there are more than 3 flashes/s | S2 | spec [V: confirmed] |
| Flash area, arithmetic | 87,296 / 786,432 (= 1024x768) = 11.1% of that screen. WCAG area is smaller than ITU 25% of screen. Design to the stricter one | S1 + calc | inference |
| Red flash | WCAG: saturated red when R/(R+G+B) >= 0.8 in one state, chromaticity difference > 0.2 (CIE 1976 UCS), 3 per second max. ITU: any transition to or from saturated red is harmful irrespective of luminance | S1 (summariser), S2 | spec [V: confirmed both] |
| Total duration | a flashing sequence over 5 s may be a risk even when it passes the rules (ITU); GAG repeats "longer than 5 seconds" | S2, S5 | spec / industry practice [V: confirmed S2; S5 not re-opened, unverified] |
| Fast cuts | rapidly changing image sequences that make areas of the screen flash count as flashes | S2 | spec |
| Pattern limit | ITU: more than 5 light/dark stripe pairs in any orientation, when stationary and covering over 40% of the screen, or when moving, flashing or reversing and covering over 25% [V: confirmed S2]. GAG states "more than 8 static or 5 moving stripes" (different counting basis) | S2, S5 (summariser) | spec / industry practice |
| Physiology | about 3% of people with epilepsy have photosensitive epilepsy; triggers commonly 3-30 Hz; 16-25 Hz most likely; some sensitive to 60 Hz; below 3 Hz uncommon; stripes and checks worse when they change direction or flash; an effect filling the whole field of view raises risk | S8 | industry practice (charity, medical) [V: confirmed 3%, 3-30 Hz, 16-25 Hz, up to 60 Hz; whole-field point not re-checked] |
| Small screens | cinema and tiny handheld screens rarely trigger because of size and low intensity. No number found for phones | S8 | industry practice |
| Test tooling | UK ad regulator points advertisers to a Harding Flash and Pattern Analyser test or equivalent. Page gives no numbers. Whether Harding takes game capture: not verified | S12, S5 | industry practice |
| Wording of the setting | never call a setting "epilepsy safe"; name it by what it controls ("screen flash effects", "effects intensity") | S5 (summariser) | industry practice |
| Offer an off switch | where flicker cannot be removed, warn and offer an option to turn it off | S5 | industry practice |
| Camera shake and motion | avoid camera shake, bobbing, motion blur, mouse blur, or provide an option to turn them off | S3 | industry practice (Microsoft) [V: confirmed] |
| Reduce-effects, shipped games | Halo Infinite: separate sliders 0 to 100% for radial blur, screen shake, full-screen effects, speed lines. Cyberpunk 2077: "additive camera motions" setting. Elder Scrolls Online: head-bob slider. Minecraft: FOV up to 110 | S3 | industry practice [V: confirmed] |
| FOV and camera movement | adjustable FOV; adjustable camera sensitivity; ability to disable automatic camera movement | S3 | industry practice |
| Moving UI and background | mechanism to pause, hide or disable blinking, scrolling, moving content on text screens; "Animate Background" toggle example; ancillary in-game motion is out of XAG 117 scope | S3, S7 | industry practice |
| Screen shake in GAG | the GAG background-movement page does not mention screen shake; the GAG list I fetched has no shake page (related only: controller-vs-camera difference, sudden unexpected movement) | S7 | gap note |
| Colour-blind prevalence | men 1 in 12 (8%), women 1 in 200 (CBA). S10 cites Birch 2012: 8% men, 0.4% women European Caucasian. Okabe-Ito: 8% Caucasian, 5% Asian, 4% African (red-green). GAG: 8-10% of males. Durban children: 4.2% M, 0.6% F. Tritanopia about 0.001% (Okabe-Ito) | S9, S10, S11, S6 | study / industry practice [V: confirmed S9 (1 in 12, 1 in 200) and S10 numbers and Birch citation; S11, S6 and tritanopia figure not re-opened, unverified] |
| Type split | Durban boys: deutans 2.7%, protans 1.5% (deutan more common). Girls: deutan 0.4%, protan 0.1% | S10 | study (one regional sample) [V: corrected - numbers match Table 1 (601 males, 704 females, ages 7-17), but the paper's abstract swaps the sexes (704 boys, 601 girls) and gives the female total as 0.6% in text vs 0.5% in Table 1; treat as one small sample] |
| Colour never alone | add shape, pattern, icon or text label to any colour-coded information (S4). Okabe-Ito: use shape, line type, hatching, direct labels | S4, S6, S11 | industry practice [V: S4 confirmed; S6, S11 not re-opened] |
| Colour choice | avoid red-green as the only pair; two teams: orange vs blue plus a lightness difference (light blue vs dark orange); avoid pure dark red on black (use vermilion or light red); differ in lightness, not hue alone; thick, large, bold coded elements | S6, S11 | industry practice (S11 pre-2020; S4/S6 confirm) |
| Configurable colours | if colour is the primary signal, give presets (deuteranopia, protanopia, tritanopia) and ideally free colour choice | S4, S6 | industry practice |
| Simulators | useful in development; not a replacement for testing with colour-blind players; full-palette filters are blunt | S4, S6, S11 | industry practice |
| Effects consequence: red damage pulse | a full-screen red pulse is both a red-flash risk and colour-only information. Pair with direction or shape and audio; keep pulses under 3/s | S1, S2, S4 | inference |
| Effects consequence: automatic weapons | a bright full-screen muzzle flash above 3 shots/s breaks the flash-rate rule once flash area passes the threshold. Cap area and luminance step, or space flashes 334 ms or more apart | S1, S2 | inference |
| Effects consequence: post effects | ColorCorrectionEffect Brightness/TintColor pulses and Bloom pulses are whole-screen luminance changes. Count them as flashes | S1, R8 | inference |

### 2b. Performance table

| technique | numbers | source | evidence level |
| --- | --- | --- | --- |
| Transparent overdraw is the main particle cost | docs: more layers of transparent effects on screen cost more GPU; partial transparency near each other forces overlapping pixels to be shaded more than once. No pixel or layer count given | R1, R9, R10 | spec |
| Particle size vs count | Roblox: size costs fill-rate. Doubling quad width and height multiplies screen area by 4 | R1, S18 | spec / industry practice (Azur Games 2026) [V: confirmed] |
| Particle count targets from a shipped mobile game | impact 30 particles to 2; 10 simultaneous impacts 300 to 20; smoke plus sparks 200 to 50 using fewer larger particles; per-effect limit about 3-10 particles when up to 200 units trigger effects at once | S18 | industry practice [V: confirmed counts, author, date 2026-08-04; the 200-units detail not re-checked] |
| Roblox hard rate cap | 400 particles/s per emitter, 100/s on mobile; particle lifetime capped at 20 s | R1 | spec [V: confirmed in local mirror] |
| Overdraw visualisation | draw particles additive with dark grey (0.1, 0.1, 0.1, 1.0); bright means stacked; small hotspots ok, large ones hurt | S17 | industry practice |
| Overdraw cut by halving emitters | Epic test halved counts of 3 overdraw-heavy emitters at Medium and below; removed most overdraw at 7+ layers (beams) and most 10-layer coverage (ring) | S15 | industry practice [V: confirmed] |
| Particle texture size | avoid 512x512 or larger on tiny particles; use 256 or 128 or lower; match texture size to on-screen size; keep mipmaps on | S17 | industry practice |
| Texture memory scales with pixels | 1024x1024 uses 4x the graphics memory of 512x512; disk size is irrelevant | R9 | spec [V: confirmed in improve.md] |
| Texture size guide for parts | 256 for 5x5 stud objects, 512 for 10x10, 1024 for 20x20 (part textures, not particles) | R11 | spec |
| Flipbook frame size | frame px = sheet px / grid. 1024 sheet at 8x8 = 128 px per frame (64 frames); 512 sheet at 8x8 = 64 px; 256 sheet at 4x4 = 64 px. Sheet allowed 8x8 up to 1024x1024 | R1, S19, calc | spec + inference (arithmetic) [V: confirmed S19 range, author, date] |
| Flipbook memory fallback | clients auto-deactivate flipbooks when low on memory (likely older phones); reused textures cost less than unique ones | R1 | spec |
| Texture packing and reuse | Riot: channel packing (one greyscale layer per colour channel) plus a shared palette (gradient map) lookup cut texture memory about two-thirds; skin budget 30 MB; Lux loaded over 3,000 emitters; wasteful example: 1024 with full alpha on a couple-of-pixel effect | S13 | industry practice (2016, pre-2020; no newer figure found) [V: confirmed 30 MB, about two-thirds (from packed palette textures), 3000 emitters, 2016-12-14] |
| Replace particle volumes | bake detail into a texture and spawn copies; one mesh with animated noise instead of a particle volume (tornado); tighten texture padding or use cut-out meshes to drop empty alpha | S18 | industry practice |
| Draw calls for effects | Roblox: emitters, decals, textures batch poorly and add draw calls; property changes on emitters can hurt a lot. MrChickenRocket: every emitter and beam costs one draw call regardless of particle count (40 emitters = 40 calls) | R9, S21 | spec; per-emitter claim is tier C, consistent with R9 [V: confirmed S21 wording "all particle emitters take one drawcall each"] |
| Draw call and triangle budget | docs example: below 1,000 draw calls and 1,000,000 triangles. Community: 500 calls, 500k triangles, under 1.3 GB client memory; UI concern above about 150 calls | R9, S21, P2 | spec / tier C [V: confirmed S21 500 calls, 500k tris, 1.3 GB as the author's own opinion; R9 example numbers and P2 not re-checked, unverified] |
| Low-end phone definition | Roblox: low-end = Android with under 2 GB; out-of-memory among the most common crash causes. Community rule: under 1.3 GB client memory | S20, S21 | industry practice (Roblox) / tier C [V: confirmed both; S21 sets 1.3 GB to support 2 GB phones] |
| Highlight cost | 255 simultaneous Highlights (extras silently ignored); first one costs up to 1 ms GPU on mobile; later ones little; mobile cost grows with screen coverage; add/remove causes geometry rebuild and spikes, so change properties instead | R5 | spec [V: confirmed 255 and 1 ms in local mirror; doc wording: Studio displays 255 client-side, extras silently ignored] |
| Shadows | engine degrades shadows with quality and disables them below quality level 4; many shadow-casting lights and small shadow-receiving parts are a known problem. Shadow-casting lights (Future) add draw calls and triangles; example map: 36 shadow draws, about 27k shadow triangles; ShadowMap "a touch more performant" on phones | R9, S21 | spec / tier C |
| Effect budget as a system | Epic Effect Types: Max Global Budget Usage 0 to 1 (1.0 = budget used; 1.5 allowed for permissive); curves lower max distance and instance counts as budget use rises; caps per type and per system. No example distances given | S14 | industry practice |
| Effect budget numbers, other UGC platform | General: Gameplay Burst max distance 12,500 / 60 instances / 30 identical; Gameplay Looping 10,000 / 40 / 10; Background Looping 10,000 / 8 / 4; Critical no distance limit / 20 / 20. Low-spec: Gameplay Burst 1,000 / 25 / 4; Gameplay Looping 2,500 / 6 / 4; Background Burst 450 / 6 / 4; Critical 4 / 2. Units not stated | S16 | industry practice (platform doc) |
| Effect LOD by quality | Epic: spawn count scaling per scalability level; example halving emitters at Medium and below | S15 | industry practice |
| Cull behaviour trap | in Niagara, culling applies after 1 s unrendered; off-screen instances still tick; many spawned at once leaves lasting overhead; stagger distant spawns | S15 | industry practice |
| Batching shared assets | Lens Studio batches copies of one VFX asset, limit 32 per asset; shared atlas and shared shader keep draw calls down | S17, S18 | industry practice (other engines) |
| Module cost in particle systems | avoid collision, noise, trails where possible; use velocity curves instead; avoid per-pixel random; avoid GrabPass on mobile | S17, S18 | industry practice (Unity/Snap; Roblox exposes none of these) |
| Pooling | no number found for Roblox. Related: Highlight add/remove rebuilds geometry (R5); `Emit` on a persistent emitter avoids create/destroy (inference) | R5 | inference |
| Cost measurement | `Stats.RenderGPUFrameTime`, `RenderCPUFrameTime`, Render Stats (Shift+F2), MicroProfiler on a real phone; Device Simulator is not accurate for memory | P2, R9 | spec |

### 2c. Roblox table

| feature | what it is good for | key properties and values | limits and mobile cost | best practice | source |
| --- | --- | --- | --- | --- | --- |
| ParticleEmitter (core) | dust, debris puffs, sparks, smoke, flipbook explosions | Rate; Lifetime NumberRange (max 20 s, higher is capped); Speed (studs/s, negative allowed); SpreadAngle (X, Y); Shape Box/Sphere/Cylinder/Disc; ShapeStyle Volume/Surface; ShapeInOut; Orientation FacingCamera / FacingCameraWorldUp / VelocityParallel / VelocityPerpendicular; Acceleration; Drag (seconds to lose half speed); RotSpeed; LockedToPart; VelocityInheritance; EmissionDirection | fill-rate: pixel coverage costs GPU; overdraw: stacked transparent layers cost GPU; emitters batch poorly; Sphere/Cylinder shapes render wrong on an Attachment parent | keep Rate low; tune Size and other properties; fade Transparency at start and end | R1, R2, R9 |
| Rate limit [V: confirmed 400/100 in R1] | cap on continuous emission | one emitter: up to 400/s; 100/s on mobile (so a phone gets at most a quarter of an over-cap effect; the quarter is our arithmetic 100/400) | no total live-particle cap found | design to 100/s; use size, lifetime, flipbook instead of rate | R1 |
| Emit(n) bursts | instant bursts: blasts, hit sparks, debris chips | `Emit(count)` emits that many instantly | tier C claim: Emit ignores the automatic graphics-level particle reduction that Rate emission gets. Whether the mobile 100/s cap applies to Emit: no number found. Needs our own test [V: confirmed S22 says ":Emit() ignores the automatic optimisation Roblox offers" (Mystifine, 2020-10-12, updated 2023); still one tier C source] | scale Emit counts yourself by quality (S22 sketch: quality value / 10, Automatic passes through, max level 10) | R2, S22 |
| Size / Transparency / Color / Squash sequences | shape over life: pop, shrink, fade | NumberSequence and ColorSequence: at least 2 and at most 20 keypoints, first time 0, last time 1; NumberSequence keypoints can carry random envelopes. [V: confirmed 2-20 keypoints in R12] Squash: >0 shrinks horizontally and grows vertically; <0 the reverse; curve over lifetime | Size is the fill-rate lever | few keypoints (4-6 is usually enough; 20 is the hard cap); fade out the tail | R1, R2, R12 |
| Flipbook | animated smoke, fire, explosion sheets | FlipbookLayout None / Grid2x2 (4 frames) / Grid4x4 (16) / Grid8x8 (64) / Custom (FlipbookSizeX/Y); FlipbookMode Loop / OneShot (rate = Lifetime / frame count; FlipbookFramerate ignored) / PingPong / Random; FlipbookFramerate max 30 fps (NumberRange) [V: confirmed in R1; S19 does not mention it]; FlipbookStartRandom (with framerate 0 = random static frame per particle); FlipbookBlendFrames (linear crossfade vs instant swap) | square power-of-two sheet, 8x8 to 1024x1024; leave transparent spacing between frames (mip filtering may need more); clients auto-disable flipbooks when memory is low; unique sheets cost more than reused ones | OneShot for blasts so the animation spans exactly the lifetime; reuse a few sheets; 512 or 256 sheets on small effects | R1, R2, S19 |
| LightEmission | glow, fire, energy: additive blend | 0 = normal blend, 1 = additive; grayscale texture without alpha: set 1 to hide dark areas; does not light the environment | additive layers still overdraw; stacked additive can blow out to white (flash risk) | additive for glows and sparks, normal for smoke and dust; add a PointLight for real light | R1, R2 |
| LightInfluence / Brightness | make particles obey scene light, or not | LightInfluence 0 to 1: 0 = full brightness regardless of light, 1 = black in darkness; Studio-inserted default 1, `Instance.new` default 0; Brightness scales emitted light when LightInfluence is 0 | none stated | LightInfluence 0 for self-lit effects; set it explicitly in code because defaults differ | R1, R2 |
| ZOffset | layer order of particles without changing size | studs, fractional ok; positive toward camera, negative away; very negative can hide particles behind the parent | none stated | stack flash over smoke over dust; Beam also has ZOffset | R1, R2, R3 |
| TimeScale | slow an effect | 0 to 1: 1 normal, 0.5 half speed, 0 frozen | none stated | slow/freeze one effect for hit-stop feel (use is our inference) | R1, R2 |
| Beam | lasers, lightning, tethers | Attachment0/1; Width0/Width1 studs; CurveSize0/1; Segments default 10 (needs at least n-1 segments for n colour/transparency keypoints); TextureMode, TextureLength, TextureSpeed; FaceCamera; LightEmission; ZOffset; Brightness | one draw call each (tier C); stops rendering if an attachment is removed | few segments unless curved; FaceCamera for flat beams; two distinct attachments | R3, S21 |
| Trail | weapon swings, projectile and debris streaks | Attachment0/1; Lifetime 0.01-20 s (default 2); MinLength / MaxLength (0 = none); WidthScale; TextureMode Stretch / Static; FaceCamera; Color and Transparency over segment age | changing Lifetime applies to existing segments immediately | short lifetime for snappy streaks; Clear() when reusing | R4 |
| Attachment | anchor for emitters, beams, trails, lights | emitter on Attachment spawns at its position; rotate the attachment instead of EmissionDirection | Sphere/Cylinder emitter shapes need a BasePart parent | PointLight on an Attachment is recommended for point emission | R1, R6 |
| Highlight | outline and fill for pickups, targets | OutlineColor/Transparency, FillColor/Transparency, DepthMode AlwaysOnTop / Occluded, Enabled | 255 active (extras ignored; a disabled one still holds a slot); first one up to 1 ms GPU on mobile; mobile cost scales with coverage; add/remove spikes | create once, change properties; delete instead of leaving disabled; avoid nested Highlight parents (draw order) | R5 |
| PointLight / SpotLight / SurfaceLight | muzzle flash, fire glow, torch, screens | Color, Brightness (default 1; strongest at centre, limited by Range), Range studs, Shadows, Angle (Spot max 180), Face | shadow-casting lights cost more draw calls and triangles; no per-light ms number and no light-count cap found | Shadows off on most lights; short Range; small non-shadow lights are cheap (tier C) | R6, R9, S21 |
| Lighting technology | overall look and cost | Technology enum: Voxel (4x4x4 voxel map), ShadowMap (crisp sun shadows), Future (most advanced); property superseded by LightingStyle (Realistic / Soft) and PrioritizeLightingQuality | Future most expensive (tier C); ShadowMap better on phones (tier C); shadows off below quality 4; no ms numbers found | choose for the phone target; test at low quality level | R7, R9, S21, S22 |
| Atmosphere | haze, depth, mood | Density (obscures objects, not skybox), Haze, Glare, Color, Decay, Offset | no cost number found | use to hide pop-in and unify colour; keep effect colours readable against it | R8 |
| BloomEffect | glow on bright pixels | Intensity, Size (radius px; 0 disables the bleed, not the colour adjust), Threshold (1 = only pure white blooms, 0 = all blooms); multiple blooms compose; parent Lighting (all players) or Camera (one player) | full-screen pass; cost not stated; flash risk when pulsed | raise Threshold so only effects bloom; do not pulse | R8 |
| ColorCorrectionEffect | hit flash, damage tint, mood | Brightness, Contrast, Saturation, TintColor | full-screen pass; pulses count as whole-screen flashes | per-player on Camera; cap pulse rate (see 2a) | R8, S1 |
| DepthOfFieldEffect | focus pull, menu or reveal | FocusDistance (studs), InFocusRadius (studs), NearIntensity, FarIntensity | full-screen pass; cost not stated | brief use for reveals; keep off in gameplay on phones until measured | R8 |
| SunRaysEffect | god rays | Intensity, Spread (0 to 1) | tied to the sun; cost not stated | skip for destruction readability | R8 |
| Camera shake | impacts, explosions | no engine property. Pattern: `RunService:BindToRenderStep(name, Enum.RenderPriority.Camera.Value + 1, fn)` runs after the default camera; apply a CFrame offset there | forum threads (snippets only, unread) disagree on +1 vs -1 and say offsets can compound | offset from the base CFrame each frame, scale by dt, decay quickly (amplitude and duration are ours to test), player slider 0-100% like Halo | R13, S3 |
| Graphics quality | how effects scale per device | `UserGameSettings.SavedQualityLevel`: Automatic or QualityLevel1..10 (1 = lowest explicit); Studio "Editor Quality Level" setting controls what you see; lower levels simplify particles and beams, remove shadows below 4, drop water and glass shader effects (tier C) | exact particle-count scaling per level: no number found; Automatic = 0 (S22) | test effects at lowest and highest Editor Quality Level (docs say so) | R1, R9, R13, S21, S22 |
| Texture upload | sprite sheets | flipbook sheet square power-of-two 8x8 to 1024x1024; part textures: docs say both "up to 4096x4096" and "up to 1024x1024 pixel spaces" in different places; engine starts low-res and ramps up | downscaling policy for particle textures: no number found | author flipbooks at 1024 or lower; PNG with transparency; test on a device | S19, R11 |
| Mobile cost (summary) | what to budget | 100 particles/s per emitter; 255 Highlights; first Highlight up to 1 ms GPU; under 2 GB Android is the low-end class; 500 draw calls / 500k tris community target | Device Simulator inaccurate for memory | measure on a real phone | R1, R5, S20, S21, P2 |

## 3. Quotes used

| quote | attribution | id |
| --- | --- | --- |
| "Reducing particle counts and spreading them further apart can reduce overdraw." | Epic Games, Measuring Performance in Niagara (via summariser) | S15 [V: confirmed exact] |
| "Color alone should never be used to represent information." | Microsoft XAG 103 | S4 [V: confirmed exact; inside a Note box] |
| "Reusing textures costs less memory than using unique textures." | Roblox Creator Docs | R1 [V: confirmed exact] |
| ":Emit() ignores the automatic optimisation Roblox offers." | Mystifine, DevForum 2020 (tier C, via summariser) | S22 [V: confirmed exact (TLDR line)] |

## 4. Conflicts between sources (newer first)

| topic | A says | B says | resolution / what changed |
| --- | --- | --- | --- |
| Flash area | WCAG 2.2 (2023): 0.006 sr in any 10-degree field; 341x256 px at 1024x768 | ITU-R BT.1702-3 (2023) and GAG: more than 25% of the displayed screen | WCAG area is about 11% of a 1024x768 screen (our arithmetic). Use the stricter type for design. Both agree on 3 flashes/s and 10% (20 cd/m2) |
| Stripe pattern count | ITU: more than 5 light/dark pairs (about 10 stripes) | GAG (summariser): more than 8 static or 5 moving stripes | different counting basis; ITU text is primary. GAG figure unverified |
| Texture size cap | R11 says up to 4096x4096 in one place | R11 says 1024x1024 for texture maps elsewhere; S19 (2022): flipbook 8 to 1024 | for flipbook sheets use 1024 max (S19, newest staff statement). 4096 likely a different asset type; test an upload |
| Draw-call budget | docs example 1,000 calls / 1M tris | tier C and project notes: 500 / 500k | docs give an example, not a rule. Use 500 / 500k for phones until measured |
| Particle count vs overdraw | Epic and Roblox docs: overdraw is the cost | Azur Games 2026 still cuts counts hard (3-10 per effect) | not a conflict: cost is count x size x layers; cut count to cut layers |
| Emit and quality | Roblox docs: particle visual quality depends on device graphics settings | tier C: Emit ignores the automatic reduction | no staff statement found. Test (section 5) |
| Colour-blind prevalence | CBA and Okabe-Ito: 8% men | S10 sample: 4.2% boys (Black South African children) | ancestry differs; plan on 8% overall, about 4-5% as the low case |

## 5. Gaps

| question | why open | how we test it ourselves |
| --- | --- | --- |
| Do ParticleEmitter counts scale with SavedQualityLevel, by how much? | docs say quality changes visuals, no factor | Studio: fixed emitter at 400/s; count live particles by screenshot at each Editor Quality Level 1..10; repeat on a phone |
| Does `Emit()` bypass the quality reduction and the 100/s mobile cap? | one tier C source only | emit 200 in one call at quality 1 and 10, count particles; phone test |
| Flash compliance of our blast flash (area, luminance step, rate) | no tool read that measures Roblox capture | record a blast clip; run a flash analyser or the Harding service; check 10% / 3 per s / area |
| What fraction of a phone screen equals the 10-degree field | WCAG uses desktop viewing geometry | measure phone viewing distance (about 30 cm assumed, unverified); compute own area; inference only |
| Screen-shake amplitude and duration defaults | XAG gives rules, no numbers; GAG has no shake page | ship slider 0-100%, playtest default amplitude with testers |
| AbleGamers (APX) shake and flash guidance | page fetched had nothing on it | fetch specific APX pattern pages later |
| Ofcom guidance text | Ofcom PDF returned 403 | ITU BT.1702-3 (S2) is the same basis; sufficient |
| Harding FPA game-capture support and checks | datasheet PDF unreadable | read Harding product page by hand |
| Light count and shadow-light cap on phones | docs give no number | spawn N shadow lights, read `RenderGPUFrameTime` on a phone |
| Bloom / DoF / ColorCorrection ms cost on phones | docs give none | toggle each, read `RenderGPUFrameTime` |
| Roblox particle effect LOD / distance cull | no such property on emitters, beams or trails in the docs I read (inference from property lists) | script client-side distance disable; measure draw calls (Shift+F2) |
| Pooling numbers | none found | measure Emit on a persistent emitter vs clone/destroy per hit |
| Mali overdraw best-practice text | guide page empty via fetch | read `developer.arm.com/docs/101897/0201` offline |
| Texture upload downscale | docs conflict (section 4) | upload a 2048 particle sheet, inspect the result |
| Camera-shake RenderPriority sign (+1 vs -1) | only forum snippets seen | try both, check jitter |

## 6. Leads not followed

| lead | reason |
| --- | --- |
| aiskill.market technical-artist page (500 particles, 3 overdraw layers) | tier D, unverifiable |
| bugnet.io overdraw and particle-budget posts | tier D |
| wayline.io particle excess post | tier D |
| skillselion / skillsmp "roblox vfx" skill page (flipbook memory claims) | tier D, AI-written |
| gamertagmythras.com Roblox particle guide ("quarter of the effect") | tier D |
| skills.sh Nordeus Unity VFX summary | tier D summary of a talk; original talk not found |
| robloxapi.github.io ParticleFlipbookTextureCompatible (says 1024 required) | search snippet only; conflicts with S19 |
| Unreal 4.27 Particle Optimization docs | HTTP 403 |
| Unreal Niagara scalability reference page | fetched page empty |
| Ofcom Guidance Note on flashing images (PDF) | HTTP 403 |
| Harding FPA data sheet PDF | binary, no text extracted |
| Arm Mali Best Practices overdraw page | redirect then empty page |
| GDC Vault "Bringing AAA Graphics to Mobile" | old (Infinity Blade era), not opened |
| DevForum camera shake threads (EZ Camera Shake port, ADS jitter, camera bobbing) | search snippets only |
| DevForum custom particle emitting threads (968599, 1900792) | search snippets only |
| WoW Dragonriding camera shake Full/Reduced/Off | forum snippet only |
| Wikipedia Harding test | tier D |
| NEI colour-blindness types page | opened, no prevalence numbers |
| Okabe-Ito palette hex values | not on the fetched page; no numbers quoted from memory |

## Verification log

Checked 2026-10-12 by re-opening sources (WebFetch; ITU PDF read with pdftotext; Roblox docs from the local mirror). No claim was proved false enough to remove. Two corrections applied in place.

| item | result |
| --- | --- |
| ITU flash-rate clause (2a "Flash rate limit") | CORRECTED. ITU bans a sequence only when there are more than 3 flashes/s AND the combined area is over 25% of the screen. The row had dropped the area condition. The advice to stay under 3/s still stands. |
| S10 Durban study | CORRECTED note. Numbers match Table 1, but the paper is inconsistent (abstract swaps sex counts; female total 0.6% vs 0.5%). Ages 7-17, one region. |
| Confirmed | S1 numbers (10%, 0.80, 0.006 sr, 341x256, 3/s, red 0.8/0.2); S2 (20 cd/m2, 160, 25%, 334/360 ms, red, stripes 5 pairs 40%/25%, 5 s, rev 11/2023); S3; S4 quote; S8; S9; S13; S15 incl. quote; S18; S19; S20; S21; S22 quote; R1; R5; R12. |
| Not re-opened (unverified) | S5, S6, S7, S11 numbers (5%, 4%, 0.001%), S12, S14, S16, S17, R9 example budgets, R11 texture cap conflict, P1-P3. |
| Tier notes | S3 and S4 are Microsoft guideline pages, fine as platform-holder tier A. S1 page does not state the WCAG 2.2 year (shows "Updated 17 September 2025"); 2023 is from outside knowledge. S21 and S22 stay tier C. The 400/s and 100/s mobile figure is a per-emitter cap; the "quarter of the effect" reading is inference. |
| Gaps noticed | (1) No tier A source for phone flash area (WCAG geometry is desktop). (2) No Roblox staff statement on Emit vs quality scaling or the mobile 100/s cap. (3) No tier A cost data for Bloom, DoF, ColorCorrection or light counts on phones. (4) No Apple, Google or Arm mobile GPU guide read (Arm Mali guide unread). (5) No peer-reviewed study on screen shake or motion-sickness effect size; guidance rests on platform-holder pages. (6) Harding and Ofcom primary text unread. |
