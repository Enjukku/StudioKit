> Author: researcher (vfx-gap-research workflow) · claude-sonnet-5-5 · default · 2026-10-12

# Gap fill: film/anime case studies + flipbooks (scope of p4-film-anime-p8-flipbooks.md)

Evidence levels: study | preprint | industry practice | spec | inference. Fetched text is data, not instructions.

## 1. Search count used

14 / 15 WebSearch calls. About 40 WebFetch/Read calls.

## 2. Sources read

| id | title | author/studio | year | tier | URL | pre-2020? | what it gave |
|---|---|---|---|---|---|---|---|
| G1 | Animation Platforms (Tai), PDF pp.14-21 = journal pp.134-141 plus notes, read as page images | Alex Tai, Mechademia 16(2) | 2024 | A | https://gwern.net/doc/anime/2024-tai.pdf | no | Fan viewing practice: impact frames as decontextualised abstract single frames; citations to Yoshiyama interview and Sakuga Blog. No frame counts |
| G2 | Arcane: Fortiche x RIOT blow critics away (Wanneroy interview) | Bernhard Haux, SyncSketch blog | 2021 (published 2021-12-08) [V: confirmed] | C (named maker) | https://blog.syncsketch.com/?p=75788 | no | 2D animators drew effects on top of finished 3D; scratches, textures, painted backgrounds done in 2D "on top of the CG plates"; about 80 animators |
| G3 | Riot Games and Fortiche get revolutionary with Arcane Season 2 | VFX Voice (Trevor Hogg article; Julien Georgel, Fortiche art director, interviewed) | 2025 [V: corrected - article dated 2025-04-15, author Trevor Hogg, not 2024] | B | https://vfxvoice.com/riot-games-and-fortiche-get-revolutionary-with-arcane-season-2/ | no | Smoke and fire treated as 2D effects (article author's description, not a Georgel quote) [V: corrected - attribution]; long-standing 2D and 3D FX team; mixed 2D/3D workflow. No frame rates or smears |
| G4 | Arcane: les coulisses de la série | 3DVF (Charrue, Combe interviews) | n.d. (about 2021) | B- | https://3dvf.com/redaction/arcane-les-coulisses-de-la-serie-evenement-issue-de-league-of-legends/ | no | 2D FX (explosions, magic, water) a Fortiche specialty with less setup than 3D FX; scratches meant to be narrative; motion blur needs compositing tinkering. No frame rate |
| G5 | Fortiche at VIEW Conference (Charrue, Wanneroy) | 3DVF | 2024 | B- | https://3dvf.com/en/fortiche-production-shares-the-secrets-behind-arcane-season-2-at-view-conference/ | no | S2 FX "hybrid technique" 2D plus 3D. No detail |
| G6 | Why Arcane looks so good | David Winter, RedShark News | 2024 | D (no interviewees, claims unattributed) | https://redsharknews.com/why-netflixs-arcane-looks-so-good-how-fortiche-ramped-up-the-animation-pipeline | no | LEAD ONLY: hand-drawn FX at 12 fps vs 24 fps characters; smear frames on Jinx [V: confirmed - the RedShark page (David Winter, 2024-12-26) does state 12 fps FX vs 24 fps; it names no sources, so still tier D; the Jinx smear claim was not re-checked: unverified] |
| G7 | Fortiche end-of-year conferences wrap-up; 3DVF Ressencourt video page; VFX Apprentice Tom De Vis page | Fortiche; 3DVF; VFX Apprentice | 2025/n.d. | C/B- | https://forticheprod.com/blog/projects-events/end-of-the-year-conferences-wrap-up/ ; https://3dvf.com/arcane-les-equipes-de-fortiche-reviennent-sur-une-serie-dexception/ ; https://www.vfxapprentice.com/blog/2d-fx-artist-netflix-arcane-league-of-legends | no | Names makers (Aurélien Ressencourt, Lead 2D FX; Tom De Vis, Senior 2D FX) and a talk title ("After Arcane", ReAnimania). Content of talks/video not transcribed. Nothing technical |
| G8 | How The Bad Guys 2 filmmakers approached stylization and combining 2D and 3D FX | Ian Failes, befores & afters (Baer, Perifel) | 2025 | B [V: confirmed: opacity-fade drop, carved dissipation, 30% are Baer; smears replace CG motion blur is Perifel, not Baer] | https://beforesandafters.com/2025/11/18/how-the-bad-guys-2-filmmakers-approached-stylization-and-combining-2d-and-3d-fx | no | Opacity fades dropped for steam/dust; carved dissipation shapes; painted frames instead of sims; smears replace motion blur; modular tool libraries |
| G9 | Doodle: A Modular Toolset for 2D Artistic Control in the 3D Effects of The Wild Robot and The Bad Guys 2 | Michael Losure, SIGGRAPH 2025 Talk | 2025 | A (abstract only, via SIGGRAPH history page) | https://history.siggraph.org/?p=227390 | no | Painterly 2D-influenced silhouettes AND TIMING with 3D detail; paint/sculpt in 3D; hand-drawn elements combined into reusable "3D sprites". ACM DL returned 403 |
| G10 | Visual Style of Puss in Boots: The Last Wish | Connors, Jackson, Van Opstal, Necci, Bouancheau, SIGGRAPH 2023 Production Session | 2023 | A (abstract only) | https://history.siggraph.org/?p=131616 | no | Lists edge breakup, graphic rims, textured FX. No frame rates in abstract. ACM PDF 403 |
| G11 | Bad Guys 2 interview (Baer, Willis) | Carlos Aguilar, Cartoon Brew | 2025 | B | https://www.cartoonbrew.com/feature-film/the-bad-guys-2-matt-baer-ben-willis-249562.html | no | Hand-drawn motion blur; anime-hold middle ground; "cop blob" 55 hand-animated officers. Nothing on sprites or frame rate |
| G12 | Motomura handout (talk script and slides), GDC 2015 | Junya Motomura, Arc System Works | 2015 | A (maker's own talk script) | https://www.ggxrd.com/Motomura_Junya_GuiltyGearXrd.pdf | YES | Limited animation in 3D: no interpolation, every frame a key; about 500 bones; scale animation; no simulation. Full read via pdftotext. No effects (VFX) content; no fps number |
| G13 | GDC Vault page, GuiltyGearXrd's Art Style | GDC Vault | 2015 | A (abstract) | https://gdcvault.com/play/1022031/GuiltyGearXrd-s-Art-Style-The | YES | Members-only; abstract only |
| G14 | Roblox DevForum: Particles' Flipbook Release | LightBeamRays (Roblox staff post) | 2022-10-21 | Spec-adjacent (official announcement) | https://devforum.roblox.com/t/particles’-flipbook-release/2029388 | no | Flipbook textures square, power of two, 8x8 up to 1024x1024; smaller allowed to save memory; spacing advice |
| G15 | Local Roblox docs mirror: ParticleFlipbookTextureCompatible.yaml, ParticleEmitter.yaml, ParticleEmitter.Orientation/Drag/ZOffset greps | Roblox | mirror | Spec | knowledge/external/roblox-creator-docs/_api-reference/enums/ParticleFlipbookTextureCompatible.yaml and classes/ParticleEmitter.yaml | n/a | Enum says playback requires 1024x1024; ParticleEmitter says texture must be exact multiple of layout; no soft-particle or depth-fade feature in mirror (grep) |
| G16 | Standard Particle Shaders (Enable Soft Particles, Camera Fading) | Unity docs | current | Spec | https://docs.unity3d.com/Manual/shader-StandardParticleShaders.html | no | Soft particles fade near opaque depth-buffer surfaces; no numbers |
| G17 | Motion Vectors (for animated textures) thread | cEssex et al., realtimevfx | 2016 | C | https://realtimevfx.com/t/motion-vectors-for-animated-textures-how-do-you-generate-them/575?page=2 | YES | 200 to 72 frames; 5-10% movement per frame; 2048 sheet 9 wide by 12 tall; strength = value/frame resolution |
| G18 | VFX for AAA Shooter thread | VinceWee, Travis, realtimevfx | 2016 | C | https://realtimevfx.com/t/vfx-for-aaa-shooter/536 | YES | "max of 16 frames per subuv" in game, 9 for UI; motion vectors make 16 look like 36 |
| G19 | Are Motion Vectors Needed Anymore? | philT, R0i3in, realtimevfx | 2024 | C | https://realtimevfx.com/t/are-motion-vectors-needed-anymore/27800 | no | Epic SubUV sampler blend = cross fade; motion vectors distort UVs; compare in slow motion |
| G20 | How do you make your own SubUV texture? | Luos_83, ChivaTateo, realtimevfx | 2019 | C | https://realtimevfx.com/t/how-do-you-make-your-own-subuv-texture/11147 | YES | Power of two; more frames means lower per-frame resolution. No numbers |
| G21 | SubUV vs pixel shader flipbook costs | tharlevfx, alex.underhill, realtimevfx | 2017 | C | https://realtimevfx.com/t/subuv-vs-pixel-shader-flipbook-costs/2013 | YES | Only qualitative cost talk; nothing usable |
| G22 | What are Flipbooks? How are They Used in Game FX? | VFX Apprentice (author not named; page date shows 2026-09-30) | 2026 | D (unnamed author) | https://www.vfxapprentice.com/blog/what-are-flipbooks-in-games | no | Corroboration: stylized games rarely beyond 4x4; 512 for top-down, 1024 for large side-view FX; 512 at 3x3 = about 170 px tiles |
| G23 | Optimal size for animation (sprite sheet) particle texture | NathanJSmith, bgolus (Unity forum) | 2019 | C (bgolus is a known shader engineer; Tier-C claim) | https://discussions.unity.com/t/optimal-size-for-animation-sprite-sheet-particle-system-texture/735721 | YES | Pixel count matters, not shape; possible mobile bandwidth effect of non-power-of-two storage |
| G24 | Sakuga Blog glossary "Impact Frames" | Sakuga Blog | n.d. | C- (glossary, no byline) | https://blog.sakugabooru.com/glossary/impact-frames/ | n.d. | "Flash for a fraction of a second"; some animators show them longer; no counts |

Opened, gave nothing usable: Epic docs pages on SubUV, DepthFade, material expressions (JS shells, empty); docs.unrealengine.com 4.27 (403); Project MUSE/ACM DL (403); artistunknown.info Yoshiyama interview (HTTP 502, tried 3 times); web.archive.org (blocked by tool); Tokion "A-frame" (about a camera composition, not impact frames; irrelevant); Epic/Unity URP depth-fade docs (404); Toon Boom/other not retried. Search result text in Japanese and about "1-2 frames, 0.04-0.08 s" came from the search tool's own unsourced general knowledge; NOT used as evidence.

## 3. Gap-by-gap results

### GAP: (a) Arcane / Fortiche 2D effects over 3D
Status: PARTLY FILLED. Method confirmed by named makers; no timing numbers or smear detail from a maker.

| finding | numbers | evidence level | source ids |
|---|---|---|---|
| 2D animators draw effects by hand on top of finished 3D animation (Get Jinxed lineage); for Arcane scratches, textures and backgrounds were also done "in 2D, on top of the CG plates" | about 80 animators overall (Wanneroy) | industry practice | G2 |
| Smoke and fire were treated as 2D effects; studio keeps a standing 2D and 3D FX team; S2 FX described as "hybrid" 2D+3D | none | industry practice | G3, G5 |
| 2D FX (explosions, magic, water) are faster to set up than 3D FX; co-founder said the method behind an explosion did not matter to them | no number | industry practice | G4 |
| Screen scratches (film-damage look) are a narrative device tied to Jinx's state; needed many retakes | no number | industry practice | G4 |
| Painted textures, painted backgrounds (everything painted) | none | industry practice | G2, G4 |
| LEAD ONLY: hand-drawn FX at 12 fps, characters at 24 fps; smear frames on Jinx | 12 fps / 24 fps | none (tier D, no attribution; inference at best) | G6 |
| Smears, paint-like explosion shapes, FX frame counts | no number found | n/a | n/a |
| Maker talks exist (Aurélien Ressencourt, Lead 2D FX; Tom De Vis) but no transcript reachable | n/a | n/a | G7 |

Use for the agent: treat "hand-drawn explosion sprite sheet over a 3D base, paired with painted textures" as sound practice. Do not quote 12 fps as Fortiche fact. It matches our own inference (12-15 fps stepped), so keep the inference label.

### GAP: (b) The Bad Guys / Puss in Boots DreamWorks stylised FX, sprite libraries, frame rates
Status: PARTLY FILLED. Two new tier-A abstracts, no frame rates from a maker.

| finding | numbers | evidence level | source ids |
|---|---|---|---|
| SIGGRAPH 2025 talk (Losure): FX needed painterly, 2D-influenced silhouettes and timing; tools let artists paint and sculpt in 3D, then combine hand-drawn elements into reusable "3D sprites" for larger effects; also lighting and moving-camera integration | none in abstract | industry practice (abstract of talk) [V: confirmed - abstract text matches; the word TIMING in the G9 source row was not re-checked] | G9 |
| Steam and dust fades on the first film used opacity; team dropped that so effects feel 2D; artists carve the dissipation shape instead | none | industry practice (Baer, 2025); confirms first-run row on Turning Red/Bad Guys dissipation | G8 |
| Effects dept now sometimes paints frames instead of simulating; pairs CG artists with 2D FX artists; post-lighting 2D FX pass for hand-drawn lines, tears, drips, sweat | none | industry practice | G8 |
| Smears replace CG motion blur to avoid strobing and keep clean silhouettes; animators needed retraining [V: corrected - the smear statement is Perifel (G8); strobing and retraining not re-checked: unverified] | none | industry practice | G8, G11 |
| Modular reusable tool libraries; manual per-shot fixes from film 1 folded back into setups | about 80% of cloth folds right automatically (not FX) | industry practice | G8 |
| Look settled after about 30% of the film done | 30% | industry practice | G8 |
| Puss in Boots SIGGRAPH 2023 session abstract lists edge breakup, graphic rims, textured FX [V: unverified - G10 page not re-opened] | none | industry practice (abstract) | G10 |
| Frame rates / stepped timing for Bad Guys or Puss FX | no number found (G10 says not stated; G8/G11 silent) | n/a | G8, G10, G11 |
| Bad Guys sprite library detail beyond first run | no new source; first run S1 stands | n/a | n/a |

### GAP: (c) Tai 2024 pages 14-21
Status: FILLED (read as page images, 8 pages: journal pp.134-141). Result is that the unread pages hold no frame counts. [V: unverified - bibliographic data confirmed (Mechademia 16(2), 2024, pp.121-141), but the PDF text layer is garbled and I could not re-read the page images, so the absence claims and the Cirugeda/Yoshiyama details below are not independently checked. Treat FILLED as unconfirmed until re-read.]

| finding | numbers | evidence level | source ids |
|---|---|---|---|
| pp.134-138 argue single frames (impact frames, effects) can be enjoyed as abstract images once removed from motion; viewers frame-step | no frame count | study (theory/analysis, not measured) | G1 |
| [V: unverified - PDF text layer unreadable] Cirugeda (Kevin) tweet quoted p.135 on episode 45 of Tropical Rouge! Pretty Cure: at points the scene becomes a "jaw-dropping expressionistic spectacle"; eight example frames posted (Figures 5, 6) | 8 frames posted | study | G1 |
| Tai: impact frames "could" refer to a collision and effects to fire or light beams, but decontextualised they read as abstract shapes and colour with affect | none | study | G1 |
| [V: unverified - PDF text layer unreadable] Yoshiyama's style listed on p.137 as hand shapes, jagged effects, erratic timing, dynamic poses, "Jack-in-the-Box frames" | none | study | G1 |
| Notes cite a Yoshiyama interview "Impact Frames as Surprise Boxes" (artistunknown.info, 2020) and Sakuga Blog; interview could not be fetched (502) | n/a | n/a | G1 |
| First-run claims "two frames added to the finisher", "split second", "bank cut", and the quote "the Jack-in-the-box of animation techniques" are NOT in pp.134-141 | n/a | see section 5 | G1 |

Not checked: pp.121-133 (first-run read them; their claims stay as first-run recorded).

### GAP: (d) Guilty Gear Xrd GDC 2015 (Motomura)
Status: PARTLY FILLED. Full handout read; it covers limited animation but contains no effects (VFX) section and no fps number.

| finding | numbers | evidence level | source ids |
|---|---|---|---|
| [V: confirmed vs handout text] Chose "Limited Animation" (Japanese anime term, vs full animation): fewer frames, each does more work; full animation tried early and "didn't convey" 2D | none | industry practice (pre-2020, maker) | G12 |
| Interpolation between keyframes turned off: every frame is a key, like stop motion; interpolation looks smoother but more 3D | no fps number | industry practice (pre-2020) | G12 |
| Rig has a lot of bones so each frame carries more information | about 500 bones per character average [V: confirmed] | industry practice (pre-2020) | G12 |
| Deform the mesh on every key frame (add imperfection) so the brain does not read a rigid 3D object; "expressiveness over accuracy"; sacrifice 3D accuracy for composition | none | industry practice (pre-2020) | G12 |
| Scale animation used heavily: exaggeration, hide/appear, squash and stretch; engine lacked it so they built it | none | industry practice (pre-2020) | G12 |
| No simulation: it "doesn't look 2D" | none | industry practice (pre-2020) | G12 |
| Cel shading is hand-controlled: vertex-colour threshold offsets, hand-edited normals, per-character light vector; every on-screen choice intentional. Resolution was 1080p PS4, 720p PS3, old sprites 480p | about 40,000 triangles per model [V: confirmed; resolutions in this row not re-checked: unverified] | industry practice (pre-2020) | G12 |
| Effects, hit sparks, effect frame rates | no number found (not in handout) | n/a | G12 |

Use for the agent: the transferable rule is "stepped, held poses with exaggerated, imperfect shapes read as hand-made; do not smooth them". No newer confirmation sought; Spider-Verse variable rates (first-run S6, S7) are the newer parallel.

### GAP: (e) Soft particles / depth fade; SubUV and flipbook frame blending; motion-vector flipbooks
Status: PARTLY FILLED. Concept confirmed in Unity docs; Epic docs were unreadable (JS shells); Roblox has no soft-particle feature documented. Flipbook numbers from named artists added.

| finding | numbers | evidence level | source ids |
|---|---|---|---|
| [V: confirmed] Unity soft particles: particles fade as they approach surfaces written to the depth buffer; avoids hard edges where particles intersect opaque geometry | no numbers | spec | G16 |
| Unity camera fading: near fade distance (fully faded) and far fade distance (fade starts) | no numbers | spec | G16 |
| Roblox mirror: no soft-particle or depth-fade property in docs mirror (grep of "soft particle", "depth fade") ; only ZOffset (layering in studs) | none | spec (absence in mirror) | G15 |
| Epic DepthFade and SubUV blend docs | not readable; STILL OPEN as spec | n/a | n/a |
| Epic SubUV sampler blending is a plain cross-fade between frames; motion vectors instead distort UVs; compare both in slow motion | none | industry practice (named artist R0i3in, 2024-10-29; Tier-C single source) [V: confirmed] | G19 |
| Max frames per SubUV in game | 16 frames in game, 9 frames for UI [V: confirmed] | industry practice (VinceWee, 2016-09-09, pre-2020; Tier C) | G18 |
| Motion-vector blending makes 16 frames look like 36 [V: corrected - Travis said motion-vector frame blending lets a 16-frame flipbook look as smooth as 36 frames; not a vector count] | 16 vs 36 | industry practice (Travis, 2016, pre-2020; Tier C) | G18 |
| Motion-vector flipbook: 200 to 72 frames [V: corrected - one post says about 72 frames with a lifetime of 200, another says reduced from about 200 frames; the cut is ambiguous, weak evidence]; effect may not move more than 5-10% of frame width between frames | 72 / 200 frames; 5-10% | industry practice (cEssex, 2016, pre-2020; second poster supports artifacts above this) | G17 |
| Motion-vector strength = strength value / frame resolution (128 / 1024 = 0.125) [V: confirmed] | 0.125 | industry practice (cEssex, 2016) | G17 |
| Mixed grid example 2048x2048 texture, 9 frames wide by 12 tall; loop trick: clone frames, 32 to 34 with a couple of padding frames | 108 frames | industry practice | G17 |
| Cost: SubUV vs pixel-shader flipbook cost | no number found | n/a | G21 |
| Power-of-two textures; more frames lower the per-frame resolution | no numbers | industry practice | G20, G23 |
| Pixel count matters, not shape (8x2048 = 128x128 = 16,384 px); mobile worst case could be significant | 16,384 px | industry practice (bgolus, 2019) | G23 |
| Roblox ParticleEmitter flipbook: square power-of-two texture 8x8 to 1024x1024 | max 1024 | spec (official announcement, 2022-10-21, LightBeamRays) plus enum doc [V: confirmed - post says square power-of-two 8x8 to 1024x1024 pixels; mirror enum line 13 says 1024x1024 playback, ParticleEmitter.yaml line 267 says exact multiple of layout] | G14, G15 |
| Roblox: spacing around frames still advised even after border-clipping fix | none | spec | G14 |

### GAP: (f) Anime impact frames (Japanese or tier C/D)
Status: STILL OPEN for frame counts. No source with a number.

| finding | numbers | evidence level | source ids |
|---|---|---|---|
| Sakuga Blog glossary: monochromatic or stylised drawings hidden in sequences for extra punch; flash for a fraction of a second, some animators show them longer [V: confirmed] | no number found | industry practice (tier C-, unsigned) | G24 |
| Tai 2024: impact frames and effects experienced as abstract art when isolated; impact frames "grab our attention" | none | study | G1 |
| Japanese-language search returned no source describing frame counts; a search-tool summary claiming "1-2 frames, 0.04-0.08 s at 24 fps" was unsourced and is NOT used | n/a | n/a | n/a |
| Know Your Meme mention that Yutaka Nakamura popularised them (tier D lead only) | none | lead | search result, not opened |
| Yoshiyama interview ("Impact Frames as Surprise Boxes") is the best lead; failed to load | n/a | lead | G1 note 10 |

## 4. Flipbook rules with numbers (new or tightened vs first run)

| rule | numbers | evidence level | source ids |
|---|---|---|---|
| Roblox hard limits | texture 1024x1024 max (square, power of two); layouts 2x2=4, 4x4=16, 8x8=64 frames; FlipbookFramerate max 30 (first run S18) | spec | G14, G15 |
| Roblox tile pixel size | 1024 sheet: 8x8 = 128 px tiles; 4x4 = 256 px; 2x2 = 512 px (arithmetic) | inference from spec | G14 |
| Frame count in practice | 16 frames in-game (4x4), 9 for UI; "4x4 pretty much the maximum" for stylized games (tier D corroboration) | industry practice (tier C) + tier D | G18, G22 |
| Tile size vs on-screen size | no number found in tier A-C. Working rule (inference): tile px >= on-screen px of the effect at closest typical camera; 128 px tiles suit effects up to about 128-256 screen px | inference | G22 (D) only |
| Frame count vs resolution | fixed sheet: more frames means smaller tiles (1024 sheet: 64 frames at 128 px, or 16 frames at 256 px) | inference | G20, G14 |
| Frame blending | Roblox FlipbookBlendFrames true = cross-fade (first run). Epic SubUV sampler blend is also cross-fade. Motion vectors (UV distortion) smoother but cost; movement per frame must stay under 5-10% of frame width. Not available in ParticleEmitter | industry practice + spec | G17, G19 |
| Mobile | clients disable flipbooks when memory low; fewer unique animated effects; reuse textures (first run) | spec | G15 |
| Stepped fps | 12-15 fps stepped for painted look. Note: tier-D Arcane 12 fps lead matches this inference; no maker confirmation | inference | G6 (D) |
| Soft edge at ground | Roblox has no documented soft-particle: use ZOffset or fade Transparency/size near contact; test in Studio | inference | G15 |

## 5. Quotes used (15 words or fewer)

| quote | source |
|---|---|
| "All those were done in 2D, on top of the CG plates." (Alexis Wanneroy) [V: confirmed] | G2 |
| "a mix of 2D and 3D techniques" (Julien Georgel) [V: confirmed] | G3 |
| "jaw-dropping expressionistic spectacle" (Kevin Cirugeda, quoted by Tai) [V: unverified - Tai text unreadable in this check] | G1 |
| "flash for a fraction of a second" (Sakuga Blog glossary, paraphrase of "tend to flash for a fraction of a second") | G24 |
| "max of 16 frames per subuv for ingame fx" (VinceWee) [V: confirmed] | G18 |
| "Ideally you wont want the effect to move more than 5-10% the width of the frame." (cEssex) [V: confirmed] | G17 |
| "SubUV blending is nothing else than a cross fade between frames." (R0i3in) [V: confirmed] | G19 |
| "Kill everything 3D." (Junya Motomura) [V: confirmed] | G12 |

## 6. Conflicts with first-run file (p4-film-anime-p8-flipbooks.md)

| item | first run | this run | resolution |
|---|---|---|---|
| Sheet size ceiling (section 2b row "Sheet resolution", S19/S20 "9x9 at 2048 / 8x8 at 2048") | community sheets at 2048 | Roblox: texture must be 1024x1024 max (G14 2022 post; G15 enum says playback requires 1024x1024) | Roblox limit wins for our game; 2048 figures are Unreal context only. Also note G15 internal tension: ParticleEmitter.yaml says "exact multiple of layout size"; enum says 1024x1024. Test with a 512x512 and 2048x2048 texture in Studio |
| Tai 2024 S2 row 50 (Tai text "split second") and row 51 ("two frames added to the finisher") | marked unverified | pp.134-141 contain neither claim. "Cure Flamingo" appears on p.137, "Jack-in-the-Box frames" appears p.137 | The "Jack-in-the-box of animation techniques" quote (section 3, first run) is not on pp.134-141; if it is in pp.121-133 it stays; otherwise drop. Row 50 frame count stays inference |
| Row 100 "Soft particles near geometry: gap" | no number found | Still no number; Unity concept confirmed (no numbers); Roblox has no feature | Keep "no number found"; add test plan |
| S26 Guilty Gear "no numbers" | abstract only | Full handout read: about 500 bones, 40,000 triangles, limited animation rules; still no fps number | Upgrade S26 to read (tier A, maker script); no effects content |
| Bad Guys dissipation (row 60, Turning Red) | S1 2022 | G8 2025 (Baer) confirms Bad Guys dropped opacity fades for carved shapes | Consistent; newer source adds Bad Guys directly |
| Spider-Verse library vs per-shot (row 104) | libraries only for secondary elements | G9 (2025) describes "reusable 3D sprites" built from hand-drawn elements for larger effects | Not a conflict: libraries survive as reusable parts, drawn per-effect |

## 7. Still open + how we could test it ourselves

| question | status | test |
|---|---|---|
| Frame count and length of anime impact frames | no number from tier A-C | Prototype 1, 2, 3 frame full-screen flashes at 30 and 60 fps; owner picks; record in ms. Retrieve Yoshiyama interview later (502 now) |
| Arcane effect fps, smear drawing, paint-like explosions from a maker | tier D only | Ask for Ressencourt talk or VFX Voice / befores & afters Arcane FX piece next run |
| Bad Guys / Puss frame rates for FX | none | Frame-step film clips and log unique frames per second per effect |
| Tile pixel size vs on-screen size | no tier A-C number | Studio: same 8x8 sheet at 1024 (128 px tiles), 4x4 at 1024 (256 px), 2x2 at 1024 (512 px); effect sized 2/6/12 studs at 10/30/60 studs; phone-resolution screenshots; log tile px / screen px where blur appears |
| Roblox texture size limit (1024 only? multiple of layout?) | docs contradict | Upload 512x512 and 2048x2048 sheets with Custom layout; read ParticleEmitter flipbook compatibility enum |
| Soft edges at ground in Roblox | no feature found | A/B: ZOffset -0.5 vs 0 vs transparency fade-in over first 0.1 s on a ground-hit emitter; screenshots |
| Epic DepthFade / SubUV blend docs | unreadable | Fetch Epic docs from a rendered browser; or cite UE GitHub source (needs Epic account) |
| Motion vectors in Roblox | not supported by ParticleEmitter | Only possible via custom mesh and shader (not available on Roblox); use more frames or FlipbookBlendFrames cross-fade |

## Verification log

Checked 2026-10-12 (adversarial pass: WebFetch plus local pdftotext). Many claims confirmed, 4 corrected, several unverified (tags inline).

Corrections made in place:
- G3 VFX Voice article is dated 2025-04-15 and written by Trevor Hogg (file said 2024, no author). The "smoke and fire in 2D" line is the author's description, not Georgel's.
- Smears replacing CG motion blur is Pierre Perifel, not Matt Baer (G8). Baer owns the opacity-fade and 30% statements.
- "16 vs 36" (G18): Travis meant motion-vector frame blending making a 16-frame flipbook look as smooth as 36 frames.
- "200 to 72 frames" (G17): the thread is ambiguous (72 frames with a lifetime of 200, versus reduced from about 200); weak evidence.

Status fixes:
- Gap (c) Tai 2024 marked FILLED is not confirmed. The PDF text layer is garbled and the page images were not re-read. Treat as unverified until re-read. Bibliographic data is correct.
- Gap (a) tier D 12 fps lead: the RedShark page does say it, so the lead is real, but it is still tier D with no sources. PARTLY FILLED stands.
- Gaps (b), (d), (e), (f) statuses stand.

No claim was proved false, so none removed. Not re-opened: G10, G13, G20-G23, G4/G5/G7/G11, Epic pages.
