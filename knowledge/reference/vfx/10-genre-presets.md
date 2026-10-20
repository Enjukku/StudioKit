---
type: reference
scope: universal
status: active
updated: 2026-10-20
source: "moved from DestructionSimulator 2026-10-20"
supersedes: []
---
> Author: kit-mover · claude-sonnet-5-5 · medium · 2026-10-20 (moved from DestructionSimulator; original author line kept below)

> Author: vfx-synthesis (vfx-reference-synthesis workflow) · claude-opus-5-5 · default · 2026-10-12

# VFX reference 10: genre presets (Output 10)

**Scope and use.** A short VFX profile for 8 Roblox genres, so the VFX agent can start an effect set with the right emphasis before it opens the moment rows. Load the shared baseline first, then the genre profile; pick the profiles that match the game (several can apply).
Every value is either evidence-cited (R-id from `00-sources.md` + evidence level) or `PROPOSAL (inference)`. No source in either research run validates a genre-wide VFX default, and no credited VFX breakdown of a named Roblox game exists (R-413, tier D lead; ChatGPT `10_genre_presets` says the same): the profiles are proposed emphases to test, and every number in them stays a proposal until the owner confirms it.
Inputs: ChatGPT `10_genre_presets.json` (8 qualitative profiles, all marked inference) plus the rules in 01-07; where two section files set different start values, the start value comes from `contradictions.md` (PD rows).

Keys: importance ratings use Riot's per-viewer 1-10 scale (R-368, single tier C; no source maps a rating to size, brightness or duration, X-27). "Rating ≥8 rights" = 100% white core, FOV kick, post-effect flash, slow motion, camera moves (PD-06). Moment names point to rows in `02a-moments-action.md` (action) and `02b-moments-reward-mood.md` (ids R1-R6, V1-V8, M1-M5, A1-A6, U1-U5).

## Shared baseline (every genre unless its profile overrides)

| key | value | evidence |
| --- | --- | --- |
| priority order | correct gameplay information (hitbox, threat, pickup, path) > readability, noise, brightness > theme | industry practice (Riot dev blog 2022) R-060; R-367, R-120; corr 3 |
| truth | drawn area = server area at cast, impact and expiry; same footprint in every skin, quality tier and viewer variant | industry practice (Riot 2021, 2022, 2025) R-080, R-060, R-033; corr 3+ |
| outcome link | big feedback only on the confirmed outcome; the action cue stays small and never covers the impact point | study (Kao CHI 2024, n=1,699; Model A n=678) R-043 |
| amount | medium build by default; more intensity is not a fix | study R-101 (n=3,018), preprint R-005; PROPOSAL 05 P-03 |
| hierarchy | attention taken ranks with importance; only rating ≥8 gets the top channels | industry practice R-080, R-368; PD-06 PROPOSAL bands |
| flash safety | composite screen ≤3 general and ≤3 red flashes in any 1 s, or WCAG area route; design target ≤2 large-area flashes per rolling 1 s; client governor P24 | spec R-165, R-167, R-168; PROPOSAL 05 P-14, 07 P24 (PD-11) |
| colour | never the only channel: add shape, icon, pattern or label; orange vs blue for two sides | industry practice R-015, R-398, R-148; spec R-450 |
| others' effects | other players' non-threat effects reduced on each client (start: LocalTransparencyModifier 0.5, no shake/flash/post effect from others); own effects, threats, pickups full | industry practice (Blizzard 2025) R-028; (NetEase 2026) R-008; PROPOSAL PD-08 |
| settings | shake 0-100%, flash effects Full/Reduced, others' effects Full/Reduced/Essential; ReducedMotionEnabled sets shake to 0 | industry practice (Microsoft XAG 117, 2022) R-074; spec R-455, R-450; PROPOSAL 07 P26 |
| mobile | Rate cap 400/s per emitter, 100/s on mobile, Lifetime ≤20 s (ceilings, not budgets); flipbooks need 1024x1024 sheets and turn off on low-memory clients, so every sheet has a static fallback; test 10-15 min on a 2 GB-class Android | spec R-209, R-214, R-231; industry practice (Roblox 2024) R-036 |
| sync | sound transient from the same event as the punch frame; measured sound 0-40 ms late, at most 1 frame early | spec R-169, R-170; study R-070; PROPOSAL 05 P-13 (PD-14) |

## Simulator (collect, sell, upgrade, hatch)

| key | value | evidence |
| --- | --- | --- |
| core feeling | satisfaction (many small confirmations), progress, anticipation, triumph on rare results | 02b feeling index; study R-043, R-088 (abstract); industry practice R-316 |
| importance ceiling | PROPOSAL (inference): routine collect/sell/UI ≤5 (pickup 2, sell 4-5, purchase 5); level-up and unlock 6-7; reveals up to 8 (Legendary), Mythic/Secret 9-10 for the hatching player only, a toast for others; basis: 02b ratings on the R-368 scale, viewer split R-028; tune by: T-RANK / 02b T7 | PROPOSAL (inference) on the R-368 scale (single tier C); no rating-to-parameter mapping exists (X-27) |
| palette and value strategy | reward gold reserved for the reward role, never on ambient or threats; ambient muted; rarity read by name + layer count + motif, not hue alone; pure white only on Legendary and above | inference from R-080, R-367 (02b G10); industry practice (Avalanche 2019) R-300; R-015, R-398 (02b G7); R-372 single tier C (02b G11) |
| signature moments | 02b R1 Pickup, R2 Coins to counter, R3 Backpack full, R4 Selling, R5 Level-up, R6 Unlock, V1-V8 Reveals, U1-U5 UI; 02a Toy plastic and bricks when collection comes from breaking | 02a, 02b rows |
| camera/screen policy | none on collect, sell and UI; reveal push-in 3-12% and at most one short shake only on Epic and above, off under reduced motion | PROPOSAL (inference) 02b escalation ladder; basis: R-316 camera work, R-319; tune by: 02b T6 |
| density and clutter policy | same-kind pickups within 100 ms merge into one burst/sound/label; ≤8 live copies of a frequent effect, ≤10 particles each; representative coin sprites (project cap 20); other players' rewards shown as a toast only | PROPOSAL 05 P-04, P-11 (basis R-153, R-248, R-326); project PROPOSAL R-466; industry practice R-028 |
| repetition policy | design for the 5th and later view; 3 recombined visual variants, about 10 sound variants, pitch jitter 0.95-1.05; random variety hides repetition but does not motivate; escalate only on a real outcome | study R-094 (faces, transfer = inference), R-043; industry practice R-383 (sound, single tier C); PROPOSAL 05 P-08, P-10 |
| mobile policy | UI glow painted into sprites (post effects do not touch GuiObjects); coin flight ≤0.5 s, count-up ≤0.6 s; static coin frame when flipbooks drop | spec R-220, R-209; vendor doc R-158 (over 400 ms reads slow); PROPOSAL 05 P-05 |
| accessibility defaults | tier name + frame shape always shown; reduced motion = no flight, chip pulse + "+N"; paid random items show every outcome's % (sum 100) before Robux is spent and explain luck boosts in numbers | spec R-208 (paid random items), R-455, R-450; industry practice R-015 |
| what to avoid | celebration before server confirmation; rarity tint during the windup; a windup length that changes with the rolled tier; near-miss presentation; endless coin showers; counters slower than the spendable balance; top-tier spectacle on routine events | preprint R-005, study R-043 (02b G1); industry practice R-316; inference (both runs); tier D lead R-414; industry practice R-071, R-360 |

## Destruction

| key | value | evidence |
| --- | --- | --- |
| core feeling | impact, weight, satisfaction; light humour on toy bricks; awe and fear on collapses | 02a feeling index; humour: no source tests it (inference); industry practice R-001, R-263 |
| importance ceiling | PROPOSAL (inference): one brick 1, small group 3, wall break or medium blast 5, huge explosion 8, building collapse 9; basis: 02a ratings on the R-368 scale, frequency (R-370); tune by: 02a T-RANK | PROPOSAL (inference) on the R-368 scale (single tier C); no rating-to-parameter mapping exists (X-27) |
| palette and value strategy | brick palette only: chips and dust take the source brick colour shifted to the nearest palette colour; additive (LightEmission 1) only for flash cores and sparks, normal blend for dust and smoke so dark mass survives; desaturated blast light; 100% white only on rating ≥8 blasts | industry practice (Animal Logic) R-313, R-314, R-135; spec R-211; industry practice R-344 (single tier C); R-372 single tier C |
| signature moments | 02a Small, Medium, Huge, Chain explosion, Delayed charge; Wood, Stone and concrete, Glass, Metal, Toy plastic and bricks breaking; Whole building collapse; Weapon impact; 02b R1 Pickup of loose bricks | 02a, 02b rows |
| camera/screen policy | trauma shake by mass and distance, rotation only, t³, delayed by distance to match the shock front; no shake per single brick; explosions 0 ms hit-stop by default; FOV kick only for rating ≥8 | industry practice (Eiserloh GDC 2016) R-124; R-363 (single tier C); PROPOSAL PD-02, PD-03, PD-04 |
| density and clutter policy | server sends break event + bounds, cosmetic bits are client-only and culled per client; chunk : cosmetic bits : dust start 1 : 5-10 : 20-50; anything that blocks sight is see-through by 2 s; the new hole reads after the dust | industry practice (DICE 2025) R-021, (Embark 2025) R-030; PROPOSAL 04 tier ratio, PD-16; industry practice R-255, R-031 |
| repetition policy | same material + same weapon = same break family (readable, deterministic); randomise only cosmetic bits (rotation, chip cell, size ±15-25%); ≥2 sheets or ≥16 cells for chips and dust; each chain link keeps its own onset | industry practice (DICE, Sirland 2025) R-255, R-126; PROPOSAL 04 repetition levers; industry practice (Song 2005) R-144 |
| mobile policy | High: hero blast ≤5 emitters + 1 light; Low: ≤3 emitters; ≤4 full-detail blasts per client, more play the primary layer only; Control's ≤200 live bodies is a reference, not a Roblox budget; debris fades, never pops | PROPOSAL PD-10 (07 P23, 06 card, 04); industry practice (Remedy via CGWorld 2020) R-295; (Embark 2026) R-011 |
| accessibility defaults | chained large flashes ≥340 ms apart; reduced effects keeps footprint, contact flash (as a steady shape), outcome and pickups; shake slider honours ReducedMotionEnabled | spec R-165; PROPOSAL 02a chain row; inference (06 M-89); R-074, R-455 |
| what to avoid | VFX that fakes or hides a structural change; object vanishing before the flash; smoke outrunning the shockwave; debris pop-in; floating leftovers after a collapse; uniform cubes; realistic smoke on toy bricks; hit-stop on every brick of a chain | industry practice R-099, R-255; R-363 (single tier C); R-011; R-031; R-303; R-134 |

## Battlegrounds and combat

| key | value | evidence |
| --- | --- | --- |
| core feeling | power, impact, danger, trust that hits and warnings are fair | 02a feeling index; industry practice R-080 |
| importance ceiling | PROPOSAL (inference): basic hit 2, heavy 4, critical 5, area attack 5, final blow 7 (≤4 for bystanders), ultimate-class 9-10, telegraph aimed at the viewer 9; rated separately for self, allies, enemies; basis: 02a ratings, R-368 per-viewer scale; tune by: 02a T-RANK | PROPOSAL (inference) on the R-368 scale (single tier C); no rating-to-parameter mapping exists (X-27) |
| palette and value strategy | ally/enemy colour keyed to the viewer's relation (red enemy / blue ally outlines; customisable sets); one colour per ability category, never reused as decoration; extremes only on the focus of top-tier effects | industry practice (Nguyen GDC 2022) R-071, (Riot 2020) R-104, (Blizzard 2018) R-111, (Riot 2025) R-033; R-372, R-120 |
| signature moments | 02a Light, Heavy, Critical hit, Final blow, Blocked hit, Windup and charge, Projectile, Trail, Muzzle flash, Weapon impact, Area attack, Telegraph, Danger zone, Low health | 02a rows |
| camera/screen policy | hit-stop local and scaled: start 50 / 100 / 150 ms (light / heavy / critical or finisher), none for a projectile's thrower, on rapid fire or in crowds; shake by strength, direction encodes cause; no cinematic zoom when many players share the scene; review from the target's camera | industry practice (Capcom) R-156, (Sakurai 2015) R-134, R-128; preprint R-073; PROPOSAL PD-02; tier D lead R-443 + inference (03 V-56); R-071 |
| density and clutter policy | PvP effects smaller, dimmer or more transparent than PvE; ranges shown only to viewers who can act; own weapon feedback stays below threat cues; PROPOSAL (inference) ≤4 attention-needing effects per viewer (own action, nearest threat, pickup, one ambient); basis: capacity 3-5 items R-139, tracking R-145; tune by: 03 V-31 sweep | industry practice R-071, R-368, R-049 |
| repetition policy | every rapid hit keeps its own onset (impacts under ~5 frames apart at a stated 30 fps read as one); skins keep primary silhouette and indicator size | industry practice (Song 2005) R-144; (Riot 2021, 2022) R-080, R-060; (Blizzard 2023) R-049 |
| mobile policy | muzzle and tracer from the next rendered frame after input, client-side; a confirmed hit waits for the server round trip and looks different; quality settings change only cosmetics, never information | industry practice (Riot, Kevin Lee 2020) R-102; (Riot 2020) R-104; spec R-209 |
| accessibility defaults | telegraph lead start 600 ms (one dodge direction) / 1000 ms (2-4 choices); audio cue ahead of the hit plus a visual and a shape; shake and flash sliders | study R-130, R-108; industry practice R-373 (single tier C), R-080, R-320; PROPOSAL PD-07; R-074 |
| what to avoid | an indicator drawn larger or smaller than the hitbox; a critical or finisher effect hiding the next live threat; an amplified swing covering the hit; victory shown before the server confirms; bloom widening the perceived area | industry practice R-080 vs R-336 (X-31); inference (02a); study R-043; R-102; inference |

## Horror

| key | value | evidence |
| --- | --- | --- |
| core feeling | fear, tension, uncertainty, then relief | ChatGPT 10 profile (inference); pacing industry practice (Valve 2009) R-140 |
| importance ceiling | PROPOSAL (inference): ambient 1, clue or anomaly 3-4, active threat and its telegraph 8-9, a scare peak 9 and rare; basis: R-368 scale, rare peaks after quiet stretches (R-140, R-077); tune by: T-RANK plus a session intensity log (03 V-75) | PROPOSAL (inference) on the R-368 scale (single tier C); no rating-to-parameter mapping exists (X-27) |
| palette and value strategy | low-value stage with a few small emissive accents; gameplay markers still ≥3:1 against their local background; muted background, gameplay objects brighter; red pulses follow the red-flash rule | spec (Beyond the Dark sample keeps glow on selected small areas) R-179; spec R-238; preprint R-063; spec R-165 |
| signature moments | 02b A3 Fog, A1 Dust in light, A6 Stage atmosphere; 02a Danger zone, Telegraph, Timer, Low health; 02b U4 for clues (no horror-specific row exists) | 02a, 02b rows |
| camera/screen policy | no forced disorienting camera effects; vignette as a UI overlay ≤40% opacity, pulse 1 Hz (start value: PD-12), removed under reduced effects; scare flashes count toward the composite flash cap | PROPOSAL 01 vignette row (basis R-165, R-074); industry practice R-074; spec R-165, R-167 |
| density and clutter policy | sparse anomalies on a quiet baseline; rare onsets keep their pull; fog never hides a hazard, pickup or route (Atmosphere Density hides objects) | industry practice R-140; study R-077 (abstract); spec R-174; 02b A3 |
| repetition policy | an identical repeated scare or flash loses pull: vary the non-semantic parts (timing jitter, position, variant), keep threat language fixed | study R-087 (suppression), R-094 (habituation; transfer = inference); industry practice R-033 |
| mobile policy | Atmosphere before camera-near fog sheets (transparent overdraw); judge dark scenes on a real phone; sound ducking by priority keeps cues audible | spec R-209, R-231; spec (Duvall Drive tutorial: nested SoundGroups duck low-priority sounds) R-453 |
| accessibility defaults | the picture carries every warning without sound; a warning screen is not a flash fix; reduced-flash mode; colour never alone; opaque text backing when PreferredTransparency is 0 | industry practice R-015 (06 M-63), R-396, R-016; spec R-450 |
| what to avoid | repetitive flashes and saturated-red full-screen pulses; fog hiding navigation; every emissive fleck becoming the brightest pixel in a dark scene; sound-only warnings | spec R-165, R-168; ChatGPT 10 profile (inference); inference from G10 (02b); R-015 |

## Obby (obstacle course)

| key | value | evidence |
| --- | --- | --- |
| core feeling | flow, lightness, precision; triumph at a checkpoint or finish | ChatGPT 10 profile (inference); 02b feeling index |
| importance ceiling | PROPOSAL (inference): jump and landing 1-2, dash 3, checkpoint 5-6, stage finish or gate 6-7, hazard telegraph 8-9; basis: 02b M and R6 ratings, R-368 scale; tune by: T-RANK | PROPOSAL (inference) on the R-368 scale (single tier C); no rating-to-parameter mapping exists (X-27) |
| palette and value strategy | platform edges, goals and hazards carry the contrast; movement effects use their own low-saturation palette, separate from hazard and reward colours; goal effect distinct from ambient particles | 02b M rows (ChatGPT recipe, inference); spec (Island Jump tutorial) R-188; industry practice R-300 |
| signature moments | 02b M1 Dash, M2 Jump, M3 Landing, M4 Speed lines, M5 Teleport, R6 Unlock (checkpoint, gate), A1-A6; 02a Telegraph, Danger zone, Timer for moving hazards | 02a, 02b rows |
| camera/screen policy | no shake on routine movement; optional 0.2 s directional nudge on dash; speed-boost FOV +5° only behind the motion setting; no camera takeover during play | first-party code (Celeste) R-154; PROPOSAL 02b M1, M4 (PD-05); inference + spec R-182 (03 V-88) |
| density and clutter policy | trails and puffs never cover a platform edge or the next landing spot; Bloom Threshold ≥0.9 so edges do not wash out; ambient never holds the brightest pixel | ChatGPT 10 profile (inference); spec R-180, PROPOSAL 07 P12; inference (02b G10) |
| repetition policy | jump and landing puffs short and subtle (puff Lifetime 250-350 ms); landing size in 3 steps by fall height | industry practice R-370 (single tier C); PROPOSAL 02b M2, M3 |
| mobile policy | first visible response within 100 ms of the tap; keep input-to-effect delay constant across moves; trail Lifetime 0.15-0.3 s | industry practice (Nielsen 1993) R-153; study R-064; study R-053 (touch tap JND 69 ms, second-hand); PROPOSAL 07 P09 |
| accessibility defaults | reduced motion removes FOV change, speed lines and camera dips; hazards carry shape as well as colour | spec R-455; industry practice R-074, R-015 |
| what to avoid | trails that suggest a path or traversable geometry; radial jump bursts that read as an area attack; bloom washing platform edges; a checkpoint celebration that hides the next jump | 02b M1, M2 (ChatGPT recipe, inference); spec R-180; inference |

## Tycoon

| key | value | evidence |
| --- | --- | --- |
| core feeling | satisfaction, progress, causality ("my purchase built that") | ChatGPT 10 profile (inference); success-linked feedback study R-043 |
| importance ceiling | PROPOSAL (inference): resource tick 1, purchase 5, machine or building complete 5-6, area unlock 6-7, rebirth or prestige 8; basis: 02b U2, R5, R6 ratings, R-368 scale; tune by: T-RANK | PROPOSAL (inference) on the R-368 scale (single tier C); no rating-to-parameter mapping exists (X-27) |
| palette and value strategy | one colour per resource or category everywhere; reward gold reserved; ambient machine loops low saturation and below interactables | industry practice (Riot 2025) R-033; R-300; inference (02b G10) |
| signature moments | 02b R2 Coins to counter (resource flow), U2 Purchase success, U5 Currency change, R5 Level-up, R6 Unlock, U1 Button press, U4 Toast | 02b rows |
| camera/screen policy | none on routine ticks; camera pan to a new unlock ≤1.5 s, skippable, only outside danger | PROPOSAL 02b R6 (basis R-153); tune by: 02b T8 |
| density and clutter policy | machine loops subordinate and local; skip or thin loops nobody can see; ≤8 live copies of a frequent effect | industry practice (Embark 2025) R-030, (DICE 2025) R-021; PROPOSAL 05 P-11 |
| repetition policy | frequent ticks shorter and subtler; near-simultaneous ticks merge; count-up ≤0.6 s; 3 recombined variants | industry practice R-370 (single tier C); PROPOSAL 05 P-04, P-05, P-08 |
| mobile policy | many machines: continuous emitters ≤40 live particles each (Rate x Lifetime); reuse sheets and texture ids | PROPOSAL PD-20 (07 P01); spec R-209, R-200 |
| accessibility defaults | signed "+N" / "-N" labels with the true balance; reduced motion; never colour alone | 02b U5 (PROPOSAL); R-455; R-015 |
| what to avoid | maximum spectacle on every purchase; counters that lag the spendable balance; constant loops that compete with the build-state change | inference from R-071, R-043; 02b U5 (ChatGPT recipe); ChatGPT 10 profile (inference) |

## Disaster survival

| key | value | evidence |
| --- | --- | --- |
| core feeling | danger, fear, awe, urgency; relief on survival | ChatGPT 10 profile (inference); industry practice R-001 ("a moment to react"), R-263 |
| importance ceiling | PROPOSAL (inference): active lethal hazard boundary and its warning 9-10, collapse 9, weather and ambient 1-2, survival reward 5; basis: priority order R-060, R-368 scale; tune by: T-RANK | PROPOSAL (inference) on the R-368 scale (single tier C); no rating-to-parameter mapping exists (X-27) |
| palette and value strategy | one hazard colour + shape language across all disasters; weather low salience; spectacle never brighter than the hazard boundary | industry practice R-033, R-015; inference (02b G10); R-060 |
| signature moments | 02a Whole building collapse, Huge explosion, Danger zone, Telegraph, Timer, Low health; 02b A5 Weather, A3 Fog, U4 Toast | 02a, 02b rows |
| camera/screen policy | collapse trauma scaled by distance; no camera takeover while a threat is live; lightning counts as a flash | PROPOSAL 02a collapse row (R-124); inference + spec R-182 (03 V-88); spec R-165 |
| density and clutter policy | degrade cosmetic smoke and debris before threat geometry; quality settings never remove information; sight-blocking dust see-through by 2 s; the safe route stays visible | ChatGPT 10 profile (inference); 07 cut-cost order (R-467 model inference, R-200); industry practice R-104; PROPOSAL PD-16; R-255 |
| repetition policy | hazard language deterministic and identical every time; timers monotonic | industry practice R-255; inference (02a timer) |
| mobile policy | test the worst overlap (weather + collapse + many players) at the lowest quality on a 2 GB-class Android for 10-15 min; Atmosphere changes tweened over 2-5 s | industry practice R-036; spec R-231; PROPOSAL 02b A3 |
| accessibility defaults | every warning has audio, visual and shape channels; flash analyser on composite captures | industry practice R-080, R-320, R-015; spec R-165; industry practice R-155 |
| what to avoid | spectacle that hides the safe route or leaves no cover; lingering dust over escape routes; lightning strobing above 3 per second; fake safe gaps | industry practice (DICE, Sirland 2025) R-255; inference (02a); spec R-165; inference |

## Anime-style games

| key | value | evidence |
| --- | --- | --- |
| core feeling | power, surprise, graphic force, hype | 02a feeling index; industry practice R-278, R-404 |
| importance ceiling | PROPOSAL (inference): basic attack 2, special 5, ultimate 9-10 (the only tier with an impact frame); basis: R-368 scale, impact frames as a rare accent (R-278); tune by: T-RANK | PROPOSAL (inference) on the R-368 scale (single tier C); no rating-to-parameter mapping exists (X-27) |
| palette and value strategy | hard light/dark split with few intentional value shapes; two-tone smoke; black-and-white impact inserts as a rare accent; element identity from one shape family across charge, travel and contact | industry practice (Arc System Works, Motomura GDC 2015) R-131; (VFX Voice 2022) R-286; (Kameda 2023) R-278; (Demon Slayer makers) R-301, R-296 |
| signature moments | 02a Windup and charge, Critical hit (impact card), Final blow, Area attack, Projectile, Trail (crescent slash), Muzzle flash; 02b M1 Dash, M4 Speed lines | 02a, 02b rows; industry practice R-337 (single tier C) |
| camera/screen policy | impact frame as a local card, or a full-screen frame ≤2 f@60 on the top tier only, counted in the flash cap; charge: zoom in, hold, fast zoom out; speed-lines slider | industry practice R-404 (C-), R-337 (single tier C); spec R-165; preprint R-073 (DBFZ); industry practice R-074; PROPOSAL 01 flash-frame row |
| density and clutter policy | one impact frame per beat; at most one stuttery (lowest-rate) accent layer per effect; impact frames, speed lines and saturated effects must not stack into a flash field | industry practice (Hawkins 2023) R-275; ChatGPT 10 profile (inference) |
| repetition policy | limited animation: stepped holds, FlipbookBlendFrames false; libraries for secondary effects, a bespoke sheet for each hero move | industry practice R-131, R-112; spec R-211; industry practice R-353, R-381 |
| mobile policy | FlipbookFramerate 15 default (on 2s of 30); hero sheets 4x4 at 1024 (256 px cells); static fallback cell | PROPOSAL PD-15 (04); spec R-214; industry practice R-338 (C-), R-394 (C) |
| accessibility defaults | reduced-flash mode swaps the impact card for a persistent local shape; inversion flashes are never assumed safe | PROPOSAL 02a critical row (R-074); spec R-165; ChatGPT 10 profile |
| what to avoid | soft CG motion blur instead of drawn smears; stepping physics bricks (stepping applies to sprite layers only); a full-screen inversion on routine hits; an impact frame that misses the contact frame | industry practice (DreamWorks 2025) R-251, (Imageworks 2018) R-308; 04 §3 mixing rule (inference); spec R-165; industry practice R-346 (06 M-03) |

## Conflicts

| topic | reading A | reading B | resolution |
| --- | --- | --- | --- |
| Numbers in genre profiles | ChatGPT `10_genre_presets`: emphases only, no universal particle counts, colours, timings or shake values | task and merge rule 5: the agent needs concrete starting values | both kept: emphases from the ChatGPT profiles; every number is a labelled PROPOSAL with a basis and a test, or an R-id; nothing is a validated genre default |
| Genre evidence base | named Roblox games (The Strongest Battlegrounds, Blox Fruits, DOORS, Pet Simulator 99, Jujutsu Shenanigans, Grow a Garden) | no credited VFX breakdown found by either run; one player guess (R-413, tier D) | unresolved: profiles transfer rules from other fields (inference); see `12-gaps.md` G-88, G-89 |
| Start values that differ between section files | e.g. hit-stop, FOV kick, others' effects, flash margin | `contradictions.md` PD-01..PD-21 | profiles use the PD start values |
| Horror and tycoon rows | no moment row in 02a/02b was built for these genres | profiles reuse general rows (fog, danger zone, resource flow) | inference; test with genre prototypes before relying on them |

## Open / test ourselves

| item | why open | test |
| --- | --- | --- |
| Each profile's importance ceiling | ratings are PROPOSALs on R-368's scale; no mapping exists (X-27) | per genre prototype: rate every effect 1-10, measure screen coverage %, peak value and lifetime, require the same order; owner + 5 testers name "which mattered more" (12-gaps G-01) |
| Genre transfer of juice findings | the studies tested an action RPG, a UI and lab tasks, not simulators or obbies (ChatGPT 12_gaps "Genre and reward transfer") | 12-gaps G-85 |
| Horror darkness vs readability | no source on dark-scene effect contrast on phones | darkest planned stage on a 2 GB Android: markers' contrast vs local background ≥3:1 (R-238), time to spot a threat with ambient on/off (12-gaps G-03, G-60) |
| Obby trail interference | inference only | dash and trail variants over a platform course; misjudged-landing rate with trails 0.15 / 0.3 / 0.6 s (12-gaps G-59) |
| Disaster worst overlap | no measured budget | weather + collapse + 16 players at quality 1 on a 2 GB phone; frame time and hazard find time (12-gaps G-28, G-77, G-80) |
| Anime impact-frame length | no maker frame count (X-24) | 12-gaps G-08 |
| Roblox genre exemplars | no credited breakdowns | 12-gaps G-88 |
