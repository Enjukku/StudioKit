> Author: researcher (vfx-deep-research workflow) · claude-sonnet-5-5 · default effort · 2026-10-12

# Part 3 — The scene: placing effects so the eye goes where it should

Scope: focal point and eye path, hierarchy, clutter, gameplay clarity, ally vs enemy, stage palette, depth, pacing, film staging of a big moment.
Method notes: WebSearch budget ran out mid-task (200/turn shared limit). Later reading used direct WebFetch of known URLs only. Several tier-A pages were unreadable (403, redirect, members-only video). Where a talk was only a listing or abstract, it is marked "listing only" and gives no findings beyond the abstract.
Evidence levels: study | preprint | industry practice | spec | inference.
Field framework words used as in the brief: gameplay, shape, value, colour, timing, composition; windup, punch, crescendo, follow-through, dissipation.

## 1. Sources read

"Read" = page opened with WebFetch (or local file read) and text seen. Fetch tool returns a model-made summary of the page, so quotes below are as returned by the tool, not verified against raw HTML.

| id | title | author/studio | year | tier | URL | pre-2020? | what it gave us |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Dev: Behind the Scenes of VFX Updates | Riot Sirhaian and Riot Riru (page bylines both), Riot Games | 2022-04-25 | A | https://www.leagueoflegends.com/en-pl/news/dev/dev-behind-the-scenes-of-vfx-updates/ | no | Ranked goals: hitbox correctness > readability, noise, brightness > theme. Method: cut fine texture detail. [V: corrected - byline on page is "Riot Sirhaian and Riot Riru"; goal order, hitbox quote and date 2022-04-25 confirmed] |
| S02 | Clarity in League | bananaband1t, Riot Games | 2021-03-12 | A | https://www.leagueoflegends.com/en-us/news/dev/clarity-in-league/ | no | Hierarchy; attention = importance; projectile direction; minimal noise; big spells may be noisier. [V: confirmed - author bananaband1t, 2021-03-12, both quotes verbatim; source says spells "can and should be noisy, to a degree", not "noisier"; S02 does NOT mention 750 abilities, that is S04] |
| S03 | Anatomy of a League of Legends missile, Part 1: Areas of Focus | Oli "Beardilocks" McDonald, lead VFX artist LoL skins (post on realtimevfx) | 2020-01-06 | C (named Riot lead, first-hand) | https://realtimevfx.com/t/anatomy-of-a-league-of-legends-missile-part-1-creating-areas-of-focus/11614 | no | Area of Focus = highest and lowest value, highest saturation; areas of rest; 3 tools value/colour/shape. [V: confirmed - author, 2020-01-06, lead VFX artist role, highest and lowest value, highest saturation, both quotes] |
| S04 | Anatomy of a League of Legends missile, Part 2: What are we communicating | Beardilocks | 2020-05-25 | C | https://realtimevfx.com/t/anatomy-of-a-league-of-legends-missile-part-2-what-are-we-communicating-with-our-vfx/13062 | no | Visual Hierarchy doc, 1-10 rating per viewer (player, ally, enemy); perspective-specific looks; Morgana R example. [V: confirmed - 2020-05-25, 1-10 rating, over 750 unique abilities, Morgana R shown only to her and affected targets] |
| S05 | Nocturne, Viktor, Malzahar, Ignite VFX updates (PBE post, mirrored) | Beardilocks posting as /u/RiotSirhaian on r/LeaguePBE; read via devtrackers.gg mirror | 2020 (Patch 10.18) | C (mirror of dev post) | https://devtrackers.gg/leagueoflegends/p/95a9bd74-nocturne-viktor-malzahar-and-ignite-visual-effects-updates | no | Case fixes: 2-colour cut, brighten a damage-negating shield, ground indicators match hitbox. Confirms Beardilocks 2020 post exists. |
| S06 | 10 Design Tips from the League of Legends VFX Style Guide | VFX Apprentice (summary of Riot's 2017 guide) | summary date not shown; guide 2017-10 | C (summary of tier A) | https://www.vfxapprentice.com/blog/10-league-of-legends-vfx-design-tips | YES (guide 2017) | Value and saturation: avoid 0% and 100%; one dominant colour + complement; keep effects short; anticipation, payoff, processing time. Primary PDF (nexus.leagueoflegends.com) redirects to home page, so NOT read. [V: corrected - summary page is dated 2022-08-29; "avoid the extremes of 0 or 100" and "steer clear from 100% or 0% saturation" confirmed; guide year 2017 is only inferred from "2017/10" in a link URL, not stated on the page] |
| S07 | The Must-Know Artistic Principles of Video Game VFX | VFX Apprentice (no byline) | 2023-12-05 | C | https://www.vfxapprentice.com/blog/five-artistic-principles-gaming-vfx | no | Six principles; value is the strongest tool to direct the eye; particles leave once their job is done. |
| S08 | How Style Guides Help Define the Look of Your Game and FX | David Hall, VFX director, Sparkadia | 2023-07-12 | C (named, first-hand) | https://www.vfxapprentice.com/blog/creating-vfx-style-guides-for-games | no | Effects live in a value/saturation band above characters and below UI. Main action done within first quarter of lifetime. [V: confirmed - David Hall, VFX Director Sparkadia, 2023-07-12; wording is "first quarter", "25%" is our conversion] |
| S09 | VFX as a Game Design Language (speaker slides with notes) | An-Tim Nguyen, VFX lead, Counterplay Games (ex Destiny 2 / Halo 5) | GDC 2022 | A | https://media.gdcvault.com/GDC+2022/Speaker+Slides/VFXasagamedesignlanguage_Nguyen_An-Tim.pdf (read via pdftotext) | no | Bandwidth/hierarchy; muzzle flash must not beat threat; PvP vs PvE; faction colour (Halo Infinite); colour not sole channel; motion speed vs heartbeat; anticipation then shockwave. [V: confirmed - slide notes: too-many-particle-effects line, muzzle flash/Doom, Halo Infinite red/blue outlines, Anthem PvE vs PvP, heartbeat rule credited to Julian Love GDC 2013] |
| S10 | Data Feel: Exploring Visual Effects in Video Games to Support Sensemaking Tasks | Hongwei Zhou, Angus G. Forbes (UC Santa Cruz); arXiv:2210.03800, VIS4DH 2022 | 2022-10 | preprint (qualitative survey, no measurements) | https://arxiv.org/pdf/2210.03800 (read via pdftotext) | no | Effects separate foreground from background; Celeste: muted background, bright warm gameplay objects. |
| S11 | Attention Overload! Creating Readable VFX for "Suicide Squad: Kill the Justice League" | Hanno Hinkelbein, lead VFX artist, Rocksteady Studios | GDC 2024 | A (LISTING ONLY, talk not read) [V: corrected - speaker, Rocksteady, GDC 2024, abstract confirmed; the page does NOT state a "lead VFX artist" role, so that title is unverified] | https://gdcvault.com/play/1034360/Attention-Overload-Creating-Readable-VFX (also listed on https://www.gdcvault.com/browse/gdc-24) | no | Confirms speaker, year, abstract. No slides link; video not opened. |
| S12 | VALORANT Patch Notes 11.07 | Riot Games | 2025-09-30 | A (official notes) | https://playvalorant.com/en-us/news/game-updates/valorant-patch-notes-11-07/ | no | Placed abilities unified in teal; ally/enemy colour coding on minimap icons; remove part of a glitch effect so information is not missed; clearer dodge edges. [V: confirmed - all four items and date 2025-09-30 found] |
| S13 | Overwatch PTR patch notes, September 2018 | Blizzard | 2018-09 | A (official notes) | https://overwatch.blizzard.com/en-gb/news/patch-notes/ptr/2018/09 | YES (2018) | Nine colourblind-friendly colours; enemy and friendly colours set separately for UI and hero outlines; shields and barriers got readability visuals. Nothing on ability-effect colour. [V: confirmed - "nine different colorblind-friendly colors", separate enemy/friendly, shields/barriers readability update] |
| S14 | GDC VFX production for RAGE 2 (interview) | Oscar Bernelind, Avalanche Studios, interviewed for 80.lv | 2019-06-04 | B | https://80.lv/articles/006sdf-001gdc-vfx-production-for-rage-2 | YES (2019) | Colour reserved for weapons/abilities; blue secondary so orange projectile reads in fire; radial fade that costs impact to keep screen readable; pick the peak moment of an effect package. [V: confirmed - Oscar Bernelind, Avalanche, 2019-06-04, orange-projectile quote verbatim] |
| S15 | Comparing Team Fortress 2 and Overwatch art direction | Xavier Coelho-Kostolny (summary of his thread), 80.lv | 2017-09-11 | B (outsider critique, not Blizzard) | https://80.lv/articles/comparing-team-fortress-2-and-overwatch-art-direction | YES (2017) | Visual rest + value hierarchy make TF2 readable; always-contrasting team colours. Opinion, used only as context. |
| S16 | Rachel Day: The Game-Changing Gamemaker Behind Overwatch | Willie Clark, VFX Voice (interview with Blizzard senior VFX artist) | 2018-06-24 | B | https://vfxvoice.com/rachel-day-the-game-changing-gamemaker-behind-overwatch/ | YES (2018) | "Push to extremes, then scale back." No clutter or team-colour content. |
| S17 | The AI Systems of Left 4 Dead | Michael Booth, Valve | GDC 2009 | A | https://steamcdn-a.akamaihd.net/apps/valve/2009/ai_systems_of_l4d_mike_booth.pdf (read via pdftotext) | YES (2009) | Pacing numbers: sustain peak 3-5 s, relax 30-45 s. No newer confirmation found. [V: confirmed - PDF text: "3-5 seconds" sustain peak, "30-45 seconds" relax; GDC 2009 Booth] |
| S18 | Roblox Creator Docs (local mirror), files: effects/particle-emitters.md, effects/highlighting.md, environment/post-processing-effects.md, _api-reference/classes/DepthOfFieldEffect.yaml, BloomEffect.yaml, performance-optimization/improve.md, scene-analysis.md | Roblox | current mirror | Spec | local: knowledge/external/roblox-creator-docs/ | no | Emitter rate cap, fill-rate/overdraw warnings, 255 Highlight cap, camera-local post effects, DoF/Bloom parameters. Engine capability only. [V: confirmed - particle-emitters.md: 400/s, 100/s mobile, 20 s max lifetime; highlighting.md: 255 Highlights, extras silently ignored. DoF/Bloom/post-effect claims not re-checked] |
| S19 | Visual Effects Bootcamp: Artistic Principles of VFX | Hadidjah Chamberlain (Blizzard), Jason Keyser (Riot) | GDC 2017 | A (LISTING ONLY, video members-only) | https://www.gdcvault.com/play/1023943/Visual-Effects-Bootcamp-Artistic-Principles | YES (2017) | Abstract only: principles plus LoL/Hearthstone case studies. No findings. |
| S20 | Marvel Rivals: "Smash the Scene" | Xiaosheng Li, NetEase Games | GDC 2025 | A (LISTING ONLY) | https://www.gdcvault.com/play/1035498/Smash-the-Scene-in-Marvel | no | Abstract: destruction hierarchy, network physics. Nothing on readability. |
| S21 | Riot Art Education: Visual Effects (Episode 7) | Riot Games (no byline) | footer 2026 | A (thin) | https://www.riotgames.com/en/artedu/visual-effects | no | Restates "satisfaction and gameplay clarity". No numbers, no rules. |
| S22 | VFX Artist behind League of Legends Swarm | VFX Apprentice (Kevin Leroy / Sirhaian) | 2024-07-17 | C | https://www.vfxapprentice.com/blog/vfx-artist-league-of-legends-swarm | no | Read, no yield: no clutter technique described. |
| S23 | See how LoL Arena's Noxus portal was made | 80.lv (Sirhaian) | 2025-02-28 | B | https://80.lv/articles/see-how-league-of-legends-arena-s-noxus-portal-was-made | no | Read, no yield: no readability content. |
| S24 | GDC Vault listings: Grissom (FXVille) 2018 "Real-Time VFX: A Visual Language Spectrum"; Lyndon (SideFX) 2018 "Zip! Thwack! Ping!" | GDC Vault | 2018 | A (LISTINGS ONLY) | https://www.gdcvault.com/play/1025507/Real-Time-VFX-A-Visual ; https://www.gdcvault.com/play/1025417/Visual-Effects-Bootcamp-Zip-Thwack | YES (2018) | Abstract only. Lyndon applies the 12 principles to VFX. |
| S25 | Marvel Rivals patch cuts visual chaos | games.gg | 2026-07-17 | D | https://games.gg/news/marvel-rivals-patch-cuts-visual-chaos/ | no | LEAD ONLY. Patch 6.5 (2026-07-15) trimmed ability and Team-Up VFX, no numbers, no dev quotes. Not cited as proof. |

Tally of pages read: tier A = 11 (S01, S02, S09, S11, S12, S13, S17, S19, S20, S21, S24; S11, S19, S20, S24 are listing/abstract only, S21 is thin); tier B = 4 (S14, S15, S16, S23); tier C = 7 (S03, S04, S05, S06, S07, S08, S22); preprint = 1 (S10); spec = 1 local mirror with 6 files (S18); tier D = 1 (S25, lead only). Total 25 pages. Sources that gave real findings: about 17.

## 2. Findings

### 2.1 Scene placement rulebook

Columns: id | rule | number | how to test | evidence | sources.
Rules phrased as build instructions for the VFX designer agent. "Inference" = my reasoning from the cited sources plus Roblox spec. Where a source gave no number the cell says "no number found".

#### Focal point and eye path (composition, value, colour, shape)

| id | rule | number | test | evidence | sources |
| --- | --- | --- | --- | --- | --- |
| V-01 | Every effect has ONE Area of Focus: the element that communicates gameplay (missile front, impact point, blast origin, danger zone edge). Thematic trail and debris are secondary. | 1 focus per effect; no number found for max secondary elements | Name the focus element in the effect spec. Freeze-frame at punch: can one element be pointed at? | industry practice (Beardilocks, Riot, 2020) | S03, S06 |
| V-02 | Give the focus the highest and lowest value (highest contrast) and the highest saturation in that effect. Build the rest of the palette from mid values and mid saturation. | Palette avoids 0% and 100% value and saturation (2017 guide); focus takes the extremes (2020). No numeric ratio found. | Greyscale the frame: focus must still be the highest-contrast patch. Desaturate-to-grey and the saturation-only view: focus must be the most saturated patch. | industry practice (2017 guide via summary; Beardilocks 2020). Pre-2020 guide confirmed by 2020 post. | S03, S06 |
| V-03 | Direct the eye with three tools in this order of strength: value, then colour, then shape. | 3 tools; value called strongest; no number found | Squint/blur test: value structure alone should still show the path. | industry practice (VFX Apprentice 2023; Beardilocks 2020) | S03, S07 |
| V-04 | Plan areas of rest: calm, low-detail zones around the focus. Not every part of an effect gets detail. | no number found | Count regions with detail; focus region must hold most of it. | industry practice (Beardilocks 2020; Coelho-Kostolny 2017 as context) | S03, S15 |
| V-05 | The brightest and most saturated pixel on screen at a given moment belongs to the highest-priority gameplay element at that moment (threat, hit, pickup). Never to ambient dust, embers or decoration. | no number found | Take a screenshot, find max luminance and max saturation pixels, check they sit on the intended element. | inference from S02, S03, S09 | S02, S03, S09 |
| V-06 | Show travel direction without motion: blur or taper the tail of a projectile; make ground indicators match the real hitbox shape and lie flat on the ground. | no number found | Pause on one frame: can a viewer name the direction? Overlay hitbox: indicator edge within the hitbox edge. | industry practice (Riot 2021, 2020) | S02, S05 |
| V-07 | Direct attention to the payoff location BEFORE the payoff with a windup cue placed at that location (flash, ring, shadow, anticipation blast). | no number found | Windup cue must be on the same screen spot as the later punch. | industry practice (Nguyen 2022: Titanfall titan drop, Destiny super flash) | S09 |

#### Visual hierarchy across all on-screen effects

| id | rule | number | test | evidence | sources |
| --- | --- | --- | --- | --- | --- |
| V-08 | Rate every effect for importance before building: scale 1-10, one rating each for the player, an ally, an enemy. Attention an effect grabs (size, brightness, saturation, timing) must match its rating. | Scale 1-10, 3 perspectives. Riot: over 750 unique abilities handled this way | Table of effects with ratings; sort by measured brightness x area; rank order must match. | industry practice (Riot, 2020, 2021) | S02, S04 |
| V-09 | Priority order when goals conflict: gameplay information (hitbox, threat, pickup) first; then readability, noise, brightness; theme last. | 3 ranked tiers | When a theme feature hides a hitbox or pickup, the feature is cut. | industry practice (Riot, 2022) | S01, S03 |
| V-10 | Threat assessment beats own-weapon feedback. Muzzle flash and shot spark must stay below enemy and hazard cues. If a player notices the muzzle flash, it is too strong. | no number found | Playtest question: can the tester say what the muzzle flash looked like? Should be "no". | industry practice (Nguyen 2022, citing Doom) | S09 |
| V-11 | Layer order of value/saturation: effects sit ABOVE characters and world, BELOW UI. | Qualitative band; no number found | Sample luminance: UI > effect focus > character > world at normal play. | industry practice (Hall, Sparkadia, 2023) | S08 |
| V-12 | Size and brightness must be honest: a weak hit must not look like a big blast. Damaging effects are bigger, brighter, sharper. Control effects (stun, root) get stronger visuals than plain damage. | no number found | Rank effects by gameplay importance; size and brightness ranks should agree. | industry practice (Riot 2017 guide via summary; Beardilocks 2020) | S04, S06 |
| V-13 | A defence or counter that matters (a shield that blocks nearly all damage) must be bright enough to see; Riot brightened a shield for this reason. | Shield blocks 99% of damage (Riot case); no brightness number found | Show it beside other shield effects: equal or higher visibility. | industry practice (Beardilocks 2020) | S05 |
| V-14 | Use outline/silhouette for must-find actors instead of brighter effects: Halo Infinite uses red enemy and blue ally outlines. In Roblox use Highlight (outline) for these, within the cap. | Roblox: 255 simultaneous Highlights; extra ones ignored silently | Count active Highlights; stay under the cap with margin (margin: no number found). | industry practice (Nguyen 2022) + spec | S09, S18 |

#### Clutter (noise limits and cuts)

| id | rule | number | test | evidence | sources |
| --- | --- | --- | --- | --- | --- |
| V-15 | Cut fine texture detail the effect does not need. Busy small detail is noise. | no number found | At gameplay camera distance, remove a detail layer; if gameplay reading is the same, delete the layer. | industry practice (Riot, 2022) | S01 |
| V-16 | Limit colours: one dominant colour plus one complement; or analogous/triadic sets. Riot cut Nocturne to two colours. | 2 colours (Nocturne); 1 dominant + 1 secondary | Palette count per effect. | industry practice (Riot 2020, 2017; Hall 2023) | S05, S06, S08 |
| V-17 | Keep effects short. Lingering effects clutter combat, signal the wrong importance and block other spells cast in the same place. Main action ends or starts dissipating within the first quarter of the effect lifetime. | First 25% of lifetime for the main action (Hall) | Timeline view: main action done by 25% of lifetime. | industry practice (Hall 2023; Riot 2017 guide via summary) | S06, S08 |
| V-18 | Particles leave screen as soon as they have done their communication job (dissipation). | no number found | After the beat, count live particles: should fall fast. | industry practice (VFX Apprentice 2023) | S07 |
| V-19 | When a cue is checked often, remove decorative noise from it. Riot removed parts of a glitch effect on a camera ability. Rage 2 added a radial fade to a glitch effect and accepted less impact. | no number found | Compare before/after with the information cue circled: cue visible in every frame. | industry practice (Riot 2025; Avalanche 2019) | S12, S14 |
| V-20 | Reserve strong colour for weapons and abilities. Keep ambient and world effects grounded (low saturation). | no number found | Saturation histogram of ambient effects vs combat effects: combat higher. | industry practice (Avalanche 2019) | S14 |
| V-21 | Prefer a subtle cue over a particle burst when it carries the message: bloom pulse, rumble, camera shake. | no number found | Replace burst with cue; if the message survives, ship the cue. | industry practice (Nguyen 2022) | S09 |
| V-22 | Big, important moments may be noisier ("to a degree"). Everything else stays minimal. Reserve the noise budget. | no number found | Only the top rating tier (V-08) may exceed the normal brightness x area ceiling. | industry practice (Riot 2021) | S02 |
| V-23 | Roblox hard limits to design inside: one emitter makes at most 400 particles/s (100/s on mobile). Particle size costs fill-rate. Overlapping transparent layers cost overdraw. Particles and decals do not batch well. | 400/s desktop, 100/s mobile per emitter; 20 s max particle lifetime; 255 Highlights | Use Roblox scene analysis: it reports particle counts. A studio-level screen-coverage or overdraw budget: no number found. | spec | S18 |
| V-24 | "Too many particle effects" is a real failure mode: too many signals at once cause confusion, frustration and reduced play time. | no number found | See Gaps: build our own clutter test. | industry practice (Nguyen 2022) | S09 |

#### Gameplay clarity (hitboxes, pickups, path, UI, many players)

| id | rule | number | test | evidence | sources |
| --- | --- | --- | --- | --- | --- |
| V-25 | Hitbox accuracy outranks beauty. Danger shape and size on screen = real server blast shape and size. | no number found | Overlay blast radius debug sphere on the effect: effect edge = sphere edge. | industry practice (Riot 2020, 2022) | S01, S05 |
| V-26 | Pickups and goals stay visible above debris and effects. Use tall beacons visible at player eye height; in Roblox a Highlight with AlwaysOnTop makes an object visible through blockers. | Highlight cap 255 | Standing in a blast cloud, can the tester point at the nearest brick pickup? | industry practice (Nguyen 2022: Destiny motes) + spec (inference for brick pickups) | S09, S18 |
| V-27 | Never use colour as the only channel. Add shape or motion so colourblind players read it. | Overwatch offers 9 colourblind colours for UI and outlines | Run a colourblind filter over screenshots. | industry practice (Nguyen 2022; Blizzard 2018) | S09, S13 |
| V-28 | Motion speed carries meaning: motion faster than a heartbeat reads as danger, slower reads as safety. A healing tether stays subtle next to damage effects. | "Faster than a heartbeat" = danger (no bpm given). Source origin: Julian Love, GDC 2013 (pre-2020), cited by Nguyen 2022 | Pulse/blink rates of danger cues vs safe cues differ clearly. | industry practice (secondhand via Nguyen 2022) | S09 |
| V-29 | In multiplayer, an effect that feels strong to cast must not blind the victim. PvP effects are smaller, dimmer or more transparent than PvE equivalents. | no number found (Nguyen: PvE explosions can be "larger, brighter and more opaque") | Test from the target's camera, not the caster's. | industry practice (Nguyen 2022, Anthem example) | S09 |
| V-30 | Make the lower-priority effect yield: if two effects collide in space, the lower-rated one is dimmed or shortened (design rule). | no number found | Spawn two effects in the same spot; the higher-rated one must stay readable. | inference from S02, S04 | S02, S04 |
| V-31 | Info that the viewer checks often gets frame-by-frame clarity: Riot made dodge edges clearer so players see exactly where they are. | no number found | Static frame: edge position unambiguous. | industry practice (Riot 2025) | S12 |

#### Ally vs enemy, team colours, other players' effects

| id | rule | number | test | evidence | sources |
| --- | --- | --- | --- | --- | --- |
| V-32 | Rate and style each effect per viewer relation (self, ally, enemy). The same effect may look different by perspective. Example: Morgana's R range circle is shown only to her and affected targets. | 3 perspectives | Spec table has three columns; spawn effect as each viewer. | industry practice (Beardilocks 2020) | S04 |
| V-33 | Use a fixed ally/enemy colour pair on things that must be read fast. Valorant colour-codes ally vs enemy on minimap utility icons; Halo Infinite uses blue ally and red enemy outlines. | 2 colours (ally, enemy) | Colour of an effect depends on viewer relation, not caster identity. | industry practice (Riot 2025; Nguyen 2022) | S09, S12 |
| V-34 | Give colour a stable meaning per category and use it everywhere: Valorant placed abilities share one teal; healing is green. Do not reuse a category colour for decoration. | 1 colour per category | Colour-to-meaning table has no duplicates. | industry practice (Riot 2025; Riot 2017 guide via summary) | S06, S12 |
| V-35 | Tone down OTHER players' effects when they do not affect the local player (lower opacity/brightness, shorter life). Keep anything that threatens the local player at full strength. | no number found for the reduction | Spawn 8 players casting; the local threat must still be the clearest element. | inference from S04 and S09 (no first-hand source states a percentage) | S04, S09 |
| V-36 | Roblox note: effects can be tuned on the client per viewer (client draws particles). Post effects parented to the Camera show only to that player. Server only sends event data. | Spec: camera-parented post effects are local to that player | Flag effects client-side by owner id; confirm in Studio two-player test. | spec + inference | S18 |
| V-37 | Offer players a clutter setting. Marvel Rivals reportedly cut ability VFX in 2026, but only a tier-D page says so. Treat as a lead, not as proof. | no number found | n/a | lead only (tier D) | S25 |

#### Stage palette and value range (leaving room for effects)

| id | rule | number | test | evidence | sources |
| --- | --- | --- | --- | --- | --- |
| V-38 | Keep the background muted or cool; keep gameplay objects and effects bright and warm (Celeste). The world must not use the effect colour at the effect's own value. | no number found | Place the effect on each stage background: focus keeps higher value contrast than the background behind it. | preprint (qualitative, Zhou & Forbes 2022) | S10 |
| V-39 | Check effect colour against the scene: an all-orange projectile fails in fire-heavy scenes; Avalanche added a blue secondary. | 1 complement added | Put the effect on the brightest, most saturated stage area; still readable? | industry practice (Avalanche 2019) | S14 |
| V-40 | Introduce palette variety gradually: start muted so players learn the visual language, then add saturation and variety once foreground/background separation is learned. | no number found | Early stages: fewer hues. | preprint (Celeste observation) | S10 |
| V-41 | Keep stage value range narrow enough to leave headroom for effects (effects sit above world in the value band). | no number found | Stage luminance histogram: 99th percentile of world below the effect focus value. | inference from S08, S10 | S08, S10 |

#### Depth layers and depth of field

| id | rule | number | test | evidence | sources |
| --- | --- | --- | --- | --- | --- |
| V-42 | Separate foreground/background through brightness and motion contrast: gameplay-relevant things pop from the background. | no number found | Cover effect: do relevant objects still separate from background? | preprint | S10 |
| V-43 | Roblox depth of field has FocusDistance (studs), InFocusRadius (studs), FarIntensity, NearIntensity. It blurs distant things and can focus on a target. Use only with proof that it does not blur pickups or enemies. | no number found for good values | A/B with DoF on/off: time-to-find a distant brick pickup. | spec; use is inference | S18 |
| V-44 | Bloom brightens by Threshold (1 = only white blooms, 0 = all blooms). Keep threshold such that only focus-level pixels bloom; otherwise bloom raises ambient clutter. | Threshold range 0-1 | Screenshot: only focus pixels glow. | spec + inference | S18 |
| V-45 | ParticleEmitter LightEmission 1 = additive blend (glows even in dark); 0 = normal. Use additive for focus, normal blend for secondary smoke so the glow stays on the focus. | 0 or 1 endpoints | Compare focus vs smoke blend. | spec + inference | S18 |

#### Pacing over time and session escalation

| id | rule | number | test | evidence | sources |
| --- | --- | --- | --- | --- | --- |
| V-46 | Alternate peaks and quiet. Constant combat tires players, long inactivity bores them. Valve's model: build up, sustain the peak 3-5 s, peak fade, then relax with minimal threats for 30-45 s. | Peak 3-5 s; relax 30-45 s (Left 4 Dead, 2009, a threat-spawn model, not a VFX model) | Log effect-intensity per second in a session: peaks separated by quiet stretches. | industry practice (pre-2020, 2009); no newer confirmation found | S17 |
| V-47 | Make effect intensity scale with reward rarity so rare wins feel bigger (Hearthstone pack opening). | no number found | Intensity rank = rarity rank. | industry practice (Nguyen 2022) | S09 |
| V-48 | Do not spend the maximum on common events; hold the top tier of brightness, size and noise for rare peaks (V-22, V-47). | no number found | Count events at top tier per minute. | inference | S09, S17, S02 |
| V-49 | "Push to extremes then scale back" is a legitimate tuning method for finding the right level. | no number found | Build 150% version, then reduce until clutter test passes. | industry practice (Blizzard 2018) | S16 |

#### Film staging of a big moment

| id | rule | number | test | evidence | sources |
| --- | --- | --- | --- | --- | --- |
| V-50 | Stage a big moment as: setup (focus placed), windup (anticipation), punch (impact), follow-through/aftermath, then time to process. Build anticipation, then deliver the payoff, then give the player time to process. | no number found (no ms/frame values in the sources) | Timeline check: all five phases present and in order. | industry practice (Riot 2017 guide via summary; Nguyen 2022 Titanfall and Destiny cases) | S06, S09 |
| V-51 | Decide the peak moment of each package (muzzle, travel, or impact) and pace the other parts around it. Rage 2: snappy explosion first, then focus on the tumbling wreck. | no number found | Mark the peak; the other phases are dimmer and shorter than the peak. | industry practice (Avalanche 2019) | S14 |
| V-52 | Make the aftermath show scale: a shockwave with camera shake and dirt reveals radius and weight, and tells players how close they were. | no number found | The ground effect edge shows the true blast radius. | industry practice (Nguyen 2022, Titanfall) | S09 |

### 2.2 Clutter methods by studio

| studio | clutter method | numbers | source |
| --- | --- | --- | --- |
| Riot (League of Legends) | Goal order: hitbox correctness first; then readability, noise, brightness; theme last. Strip fine texture detail. Cut a champion to two colours. Perspective-specific appearance. Short effects. Visual Hierarchy doc rates each spell 1-10 for player, ally, enemy. | 1-10 scale; 3 perspectives; 2 colours (Nocturne); over 750 abilities; value and saturation avoid 0%/100% (2017 guide) | S01, S02, S04, S05, S06 |
| Riot (VALORANT) | Unify colour per ability category (teal for placed utility); ally/enemy colour on minimap icons; remove decorative glitch from a frequently-checked camera; clearer dodge edges. | no numbers | S12 |
| Blizzard (Overwatch) | Shields/barriers got readability visuals (2018). Colourblind team colours for UI/outlines. First-hand VFX clutter method not found. | 9 colourblind colours | S13, S16 |
| Rocksteady (Suicide Squad) | Talk exists (Hanno Hinkelbein, GDC 2024). Content not read. Abstract says: guide attention without overwhelming, include VFX in design early. | none read | S11 |
| Avalanche (Rage 2) | Colour only for weapons and abilities; complement colour for contrast; radial fade on a glitch effect even though impact drops; peak moment per package. | no numbers | S14 |
| Counterplay (ex Destiny 2, Halo 5) | Bandwidth/hierarchy; muzzle flash below threat; PvP effects smaller than PvE; use subtle cues; motion speed contrast. | no numbers | S09 |
| Sparkadia (Sparkball) | Effect value/saturation band above characters, below UI; analogous/triadic palette; main action in first quarter of lifetime. | 25% of lifetime | S08 |
| Valve (Left 4 Dead) | Pacing instead of per-effect clutter: peaks and quiet. | 3-5 s sustain; 30-45 s relax | S17 |
| Marvel Rivals (NetEase) | Reportedly trimmed ability and Team-Up VFX in 2026. Only tier D read. | no numbers | S25 (lead) |
| Apex Legends (Respawn), Fortnite (Epic) | No first-hand source found. | n/a | none |

## 3. Quotes used (15 words or fewer; as returned by the fetch tool)

| quote | who | source |
| --- | --- | --- |
| "Great art has Areas of Focus, and Areas of Rest." | Beardilocks, 2020 | S03 |
| "If Everything is important, Nothing is important." | Beardilocks, 2020 | S03 |
| "Projectiles should convey the direction they're traveling, even without motion." | Riot, Clarity in League, 2021 | S02 |
| "the amount of attention an ability grabs should match its level of importance." | Riot, Clarity in League, 2021 | S02 |
| "prioritize the correction of inaccurate hitbox indicators" | Riot Sirhaian, 2022 | S01 |
| "a completely orange projectile won't read very well" | Oscar Bernelind, Avalanche, 2019 | S14 |
| "there IS such a thing as too many particle effects" | An-Tim Nguyen, GDC 2022 slide note | S09 |

## 4. Conflicts between sources (newer first)

| topic | older | newer | what changed / my read |
| --- | --- | --- | --- |
| Value extremes | 2017 Riot guide (via summary S06): avoid 0% and 100% value and saturation, mostly mid values. | Beardilocks 2020 (S03): the Area of Focus has the highest AND lowest value and the highest saturation. | Newer practice reserves the extremes for the focus. Reconciled (inference): mid palette overall, extremes only on focus. Primary 2017 PDF unreadable, so wording of the older rule is second-hand. |
| Noise | Riot 2017: minimise clutter. | Riot 2021 (S02): big, important spells may be noisier "to a degree". | Not a reversal: noise budget is tied to importance rating (V-08, V-22). |
| Muzzle/own feedback vs power fantasy | Blizzard 2018 (S16): push effects to extremes, then scale back. | Nguyen 2022 (S09): own-weapon feedback must stay below threat cues. | Compatible: tuning method vs ceiling. Ceiling wins. |
| Overwatch team colours | 80.lv 2017 (S15, outsider): Overwatch lacks standard team colours. | Blizzard PTR 2018 (S13): customisable enemy/friendly colours for UI and outlines. | Blizzard added options for UI and outlines. Whether ability effects use fixed colours: no first-hand source found. |
| PvE vs PvP effect size | Nguyen 2022: PvE effects can be larger, brighter, more opaque. | Marvel Rivals 2026 (S25, tier D): cut VFX in team fights. | Consistent with Nguyen: PvP needs smaller effects. Tier D, do not rely on it. |

## 5. Gaps and how to test them ourselves

| question asked in scope | status | how we test it |
| --- | --- | --- |
| Rocksteady "Attention Overload": what clutter methods and numbers? | Speaker (Hanno Hinkelbein), venue (GDC 2024, Visual Arts track, Vault id 1034360) and abstract confirmed. Slides/video content not read (members-only; schedule site 403). | Owner can watch the Vault video if a GDC Vault login exists and give notes; then add a row. |
| Studio numbers for screen coverage, overdraw, brightness | None found in any source read. | Build a Studio MCP clutter harness: screenshot with effects on and off, compute % of pixels changed (coverage), luminance histogram, count live particles and emitters; sweep until a "find the pickup" test fails. Record the knee as our own budget. |
| Overwatch ally/enemy effect colour rules | No first-hand VFX source. Only UI/outline colourblind options (2018) and outsider critique (2017). | Test with 8 testers: ally vs enemy blast, time to name which is hostile; vary colour coding. |
| Apex, Fortnite VFX readability | No first-hand source found. | Same tests; keep Apex/Fortnite as unresolved. |
| Valorant VFX readability beyond patch notes | Only 11.07 notes read. Riot tech blog not located. | Look for Riot Games technology blog posts later (not found with direct fetch). |
| Marvel Rivals first-hand | Only a tier-D news page; GDC 2025 talk is on destruction (abstract only). | Watch the GDC 2025 destruction talk if accessible; it may include destruction clutter points. |
| How much to tone down OTHER players' effects | No percentage in any source. | A/B: other-player effect opacity at 100%, 70%, 40%, 0%; metric: time to spot own-threat and own-pickup; player comfort rating. |
| Depth layers and depth of field for effects | Only Roblox spec and a preprint on foreground/background. No studio rule. | A/B DoF on/off for a distant-pickup find task. Check that DoF does not blur effect focus. |
| Session escalation of intensity | Only L4D pacing (2009) and Hearthstone rarity scaling (Nguyen 2022). No newer confirmation. | Log intensity per minute in play tests; check that quiet stretches exist; vary relax time (candidates from L4D: 30-45 s). |
| Film staging with real timings (ms/frames for setup, beat before, payoff) | No numbers in any source read. Other part scopes (timing) may hold them. | Build the five phases (V-50) and iterate with frame timing from playtests. |
| Attention/clutter studies | Zhou & Forbes is qualitative only (no measures). Searches for eye-tracking VFX studies found nothing usable before the search budget ended. | Consider our own eye-tracking proxy: time-to-first-fixation on the pickup with/without effects. |

## 6. Leads not followed (tier D or unreadable)

- https://schedule.gdconf.com/session/attention-overload-creating-readable-vfx-for-suicide-squad-kill-the-justice-league/899824 : 403 on fetch; abstract was read instead from the GDC Vault page (S11).
- https://nexus.leagueoflegends.com/wp-content/uploads/2017/10/VFX_Styleguide_final_public_hidpjqwx7lqyx0pjj3ss.pdf : primary Riot 2017 style guide; redirects to the home page. Rules from it are second-hand (S06).
- https://www.scribd.com/document/384307037/LoL-Guide : user upload of the same guide; not opened (copyright, tier D).
- https://3dreference.notion.site/Visual-Effects-Bootcamp-Artistic-Principles-of-VFX-GDC-2017-fcd0698c31cf4621a70ed8a7621e17da : fan notes of Keyser/Chamberlain 2017; page returned only "Notion".
- GDC 2017 Keyser/Chamberlain video and GDC 2013 Julian Love Diablo III VFX talk (source of the heartbeat motion rule): video members-only / page not found by direct fetch.
- https://www.gdcvault.com/play/1034360 video itself: not opened.
- "Controlled Chaos: 12 Principles of Design for VFX" (GDC schedule id 914747) and "Are You Visually Literate?" (GDC 2025 Visual Effects Summit): schedule 403; not found in the Vault browse pages read.
- https://www.dexerto.com/apex-legends/apex-legends-pro-wants-particle-effects-fix-1544385 : Apex player complaint about particle effects (2021); news page, tier D.
- https://us.forums.blizzard.com/en/overwatch/t/overwatch-league-visual-effects-in-game/593284 : forum comment on red enemy effects; player opinion, tier D.
- topuplist.com Marvel Rivals articles and comicshoplocator.com Marvel Rivals article: sales/news pages, tier D.
- https://www.sportskeeda.com/esports/riot-dev-talks-clarity-league-legends : news rewrite of S02.
- Respawn / Riot VFX job listings: state readability as a goal, no method; not cited.
- Rosenholtz feature-congestion clutter measure (2007) and other vision-science clutter papers: not opened. Searches ended when the web search limit was reached.

## Verification log

Checked 2026-10-12 by fact-checker (claude-sonnet-5-5). Re-opened: S01, S02, S03, S04, S06, S08, S11, S12, S13, S14, S17 (PDF), S09 (PDF), S18 (local mirror: particle-emitters.md, highlighting.md). Tags are appended in the S-table rows in section 1.

- Claims proved false and removed: none.
- Corrected: S01 byline (page says Sirhaian and Riru, no Kevin Leroy); S06 summary page dated 2022-08-29 and the 2017 guide year is inferred from a URL only; S11 speaker role "lead VFX artist" is not on the page (Hinkelbein, Rocksteady, GDC 2024 confirmed).
- Attribution: "over 750 abilities" is in S04 only, not S02 (V-08 lists both).
- Wording: V-22 and the clutter table say "noisier"; S02 says "can and should be noisy, to a degree". Same meaning.
- Not re-checked: V-36, V-43 to V-45 (DoF, Bloom, camera-local post effects), S10 contents, S05, S07, S15, S16, S19 to S25.
- Value-extremes reconciliation (section 4): both source statements confirmed; "mid palette, extremes only on focus" stays the researcher's inference.
- Gaps: no tier-A source for screen-coverage or overdraw numbers; no first-party Riot tech-blog piece on VALORANT readability; no Epic/Respawn first-party material (Apex, Fortnite). The Rocksteady 2024 talk, the main recent AAA readability talk, is unread. L4D pacing (2009) is correctly labelled as a threat-spawn model.
