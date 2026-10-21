---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: J008-T02, Environment_Designer_Research_2026.txt lines 256-434
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-21

# Environment paper part 2: ambience, ambient life, set dressing, terrain, art-director cohesion (lines 256-434)

Paraphrased notes. The paper (EP) stays outside git. Every row cites `EP:<line>`. Nothing here is fact-checked yet: claims are the paper's, listed in section 7 for the fact-check pass. The paper's research date is 2026-10-21; its live Roblox documentation was read the same day. The paper built, heard and measured nothing (EP:15, outside this range): every procedure in it is a plan, not a test result.

## 0. How to read

| Key | Meaning |
| --- | --- |
| EP:n | line n of `Environment_Designer_Research_2026.txt`. One paragraph or table row = one line. Register = EP:763-1469. |
| Tag | The paper's own mark. VERIFIED = official spec or measured result (the live docs, read 2026-10-21). EXPERIENCE = a named studio or practitioner account, kept in its original context. OPINION = the paper's proposal, interpretation, example or acceptance rule. UNKNOWN = the paper looked and found no source value; it stays UNKNOWN and is never turned into a fact or a zero (EP:304). A row with two tags has two kinds of sentence. |
| Src | paper source ID, resolved in section 9. E00 = the paper's own proposed workflow (not an external source). "accessed" = living page with no publication date; the access date is not a release date. |
| Stage | my labels (the paper has no stage numbers; the lead may remap): E0 intake (route contract, art bible version, listener policy, scale); E1 blockout and target scene; E2 plan (zones, ambience map, dressing intent, terrain or mesh choice); E3 build and place (terrain, dressing, emitters, zone volumes); E4 runtime behavior (blends, streaming lifecycle, state record); E5 verify (cameras, listening checkpoints, phone profile); E6 review and hand-off (packet, briefs to crafts, owner). |
| Role | blank = the environment designer (ENV) owns it. Otherwise: [sound-owns], [vfx-owns], [art-director], [modeler], [game-designer], [animator]. "ENV places / X owns" = ENV decides where and why, X decides how. [sound-owns] is also set where the studio's `sound-design` skill already has the rule (overlaps in section 8). |
| Row IDs | AM ambience (paper section 6), ZX zone example, SS seven-source table, VL ambient life (7), SD set dressing (8), TN terrain (9), CO cohesion (10), ES evidence-summary row, AF map field, RC related contract, CK claim, X contradiction or limit, UN unknown. |

## 1. Section 6: ambience zones and coherent soundscapes (EP:256-336)

### 1.1 Studio cases (EP:258-266)

| ID | EP | Lesson | Tag | Src | Stage | Role |
| --- | --- | --- | --- | --- | --- | --- |
| AM01 | 260 | Ghost of Tsushima (Sucker Punch; audio director Bradley D. Meyer, senior sound designer Josh Lord): ambience is described as part of the island's identity, not wallpaper under the music. Their examples: wind acting on wooden slats, damaged roofs and rattling shoji doors; after the rain, drops keep falling off leaves (fact-check AU31 narrowed the paper's "wet surfaces keep dripping" and "paper screens"); exploration, infiltration and combat each need a different mix priority. Paper's transfer: a changing place whose sounds have causes. It is not a rule that every visible object makes constant noise. | EXPERIENCE (facts); OPINION (transfer) | A01, 2020-07-22 | E2 | [sound-owns] mix priority per mode |
| AM02 | 262 | Ghost of Yotei (Sucker Punch / PlayStation Studios): procedural one-shots depend on species and biome; ambience is mostly positioned in the world; a wind rig around the player uses 4 mono emitters, each sampling a different surrounding biome; the team reports no ambisonic ambience beds at all; rain and snow use 8-channel cube layers; rain also has 4 surface-dependent mono layers; "Sound Scenes" blend near, mid and far assets. Counterexample to the belief that every great game keeps one constant stereo bed per biome. These are PS5 production choices, not Roblox mobile limits and not a universal architecture. | EXPERIENCE | A02, 2025-11-06 | E2 | [sound-owns] |
| AM03 | 264 | Sea of Thieves (Rare): the developer-video introduction stresses that sound changes below deck, and mentions recording experiments. It backs attention to space and material only. It gives no measured reverb value and no implementation detail (the video was not watched). | EXPERIENCE | A03, 2016-10-21 | E2 | |
| AM04 | 266 | Split every ambience plan into four functional parts: (a) non-directional continuity, only if needed; (b) authored intermittent life; (c) recognizable world sources; (d) weather and exposure modulation. A "bed" is a function, not a file format. A cave can get by with hardly any continuous bed; a river can be built from several spread-out sources rather than one clear point. Keep resources and listening space for game-critical cues. Synthesis of A01-A03, not a studio recipe. | OPINION | A01-A03, E00 | E2 | ENV places / [sound-owns] clips |

### 1.2 What Roblox supports now (EP:268-286)

| ID | EP | Lesson | Tag | Src | Stage | Role |
| --- | --- | --- | --- | --- | --- | --- |
| AM05 | 270 | Current graph. For new work the guide steers away from Sound, SoundGroup and SoundEffect and toward audio objects. Roles: AudioPlayer = the stream; Wire = the connection; AudioEmitter = puts audio into the world; AudioListener = receives it; AudioDeviceOutput = hands it to the device. A player wired straight to the device output has no spatial effect. The guide's standalone 3D demo happens to use 6 objects; that count does not mean each waterfall needs its own listener and output. | VERIFIED | A04, accessed 2026-10-21 | E3 | [sound-owns] wiring |
| AM06 | 272 | AudioEmitter attenuation facts: a custom distance curve holds up to 400 distance/gain pairs; gain values stay within [0,1]; points are joined linearly; beyond the supplied range the end values stay in force. DistanceAttenuationMode defaults to Custom; preset modes use DistanceAttenuationBounds, documented default [4,10000] (unit not stated by the paper). These are API values, not suitable waterfall radii. PositionType defaults to Parent; PositionInstance names a different positional instance when PositionType is Instance. GetAudibilityFor returns the distance and angle attenuation combined, not the final loudness. | VERIFIED | A05, accessed 2026-10-21 | E3, E5 | [sound-owns] curves |
| AM07 | 274 | Authoring consequences: a custom range that has an end should finish at gain 0. Check the active attenuation mode, not only the stored curve (a preset mode makes a good-looking curve irrelevant). Write down how each source gets its position: an emitter whose parent has no position must not end up silent unnoticed. Review directionality apart from distance, especially for sources the player should hear before seeing them. | OPINION | A05 (derived) | E2, E3, E5 | ENV: position semantics / [sound-owns] curve |
| AM08 | 276 | AudioFader scales the stream volume, Volume range 0-10 (the paper says 0-3; corrected by fact-check AU12, `AudioFader.yaml:44-47`). AudioFilter has the properties FilterType, Frequency, Gain and Q. AudioReverb has decay, delay, dry/wet and filtering settings. They show what can be set; none of this proves a single right cave preset. | VERIFIED | A06, A07, A08, accessed 2026-10-21 | E3 | [sound-owns] |
| AM09 | 278 | Acoustic simulation: first announced 2026-01-28 as a client beta; an update dated 2026-09-22 states it is fully released. It adds occlusion, diffraction and reverberation automatically, inside the advanced audio system. The global on/off sits on SoundService; settings on the emitter and listener matter too. The announcement warns that precision may fall, or parts of the simulation turn off, so the frame rate holds. The September update still describes support for Sound instances as under development; the plan for Sound support in the older announcement text must not be written up as shipped. | VERIFIED | A09 (2026-01-28; 2026-09-22), A05 | E2, E3, E5 | [sound-owns] design; ENV records the choice |
| AM10 | 280 | Old and new reverb are separate systems. SoundService.AmbientReverb only affects Sound instances and never an AudioPlayer/AudioEmitter graph; the graph-side tool is AudioReverb. Where the default listener sits is set by SoundService.DefaultListenerLocation, which is PluginSecurity; the overview page still uses the name ListenerLocation. Count that as documentation drift: read the installed Studio API and do not write a runtime assignment from memory. | VERIFIED | A10, A04, accessed 2026-10-21 | E3 | [sound-owns] |
| AM11 | 282 | Legacy Sound: RollOffMinDistance, RollOffMaxDistance, RollOffMode exist; Volume is multiplicative with documented range 0-10; the legacy guide says source audio that is loud enough likely needs no Volume above 2. Conditional guidance only: not a per-source mix target, and it does not change AudioFader's 0-3 range. | VERIFIED | A17, accessed 2026-10-21 | E3 | [sound-owns] |
| AM12 | 284 | AudioPlayer's asset property is Asset; AssetId is deprecated though older examples still use it; IsReady allows readiness checks. Existing class names and a working graph say nothing about whether the experience may use a given audio asset (that caution is the paper's workflow opinion). | VERIFIED; OPINION (permission caution) | A11, accessed 2026-10-21 | E3 | [sound-owns] |
| AM13 | 286 | Choosing echo: give the cave one explicit design, either an authored graph reverb or acoustic simulation. Audition deliberate combinations; do not stack both by accident. Geometry-reactive echo may sound different on different devices because quality adapts. Never let a mandatory navigation hint depend only on subtle diffraction or reverb. A low-detail fallback keeps the recognizable source and its distance envelope and drops spatial richness. | OPINION | A09 (bound) | E2, E5 | ENV records which / [sound-owns] design |

### 1.3 Zones, boundaries, weather, height, streaming (EP:288-300)

| ID | EP | Lesson | Tag | Src | Stage | Role |
| --- | --- | --- | --- | --- | --- | --- |
| AM14 | 290 | Region detection: WorldRoot:GetPartBoundsInBox and GetPartBoundsInRadius test part bounding boxes; GetPartsInPart tests occupied volume, more exact, but not the efficient pick for every simple volume. The old Region3 query methods are deprecated. SoundService's page shows a tagged-part dynamic-reverb example, yet the point-in-box tests printed there leave out the absolute-value and lower-bound checks; do not copy it as a proven containment test. | VERIFIED | A12 (alias B10), A10, accessed 2026-10-21 | E3, E4 | |
| AM15 | 292 | Zone record (proposed) holds a stable ID, a world transform, half-extents or another stated shape, vertical limits, a priority, the neighbors and a transition corridor. Oriented box: convert the listener position to box-local space, then test each axis by absolute value against its half-extent. State whether the camera or the avatar stands for the listener; with a third-person camera the camera may pass a wall while the avatar is still inside. Keep overlap queries for cases where true geometry matters; they are no excuse to skip a plain numeric test. | OPINION | E00 (A12 gives API options) | E2, E4 | |
| AM16 | 294 | Blending: derive zone weights from signed distance to the authored boundary, or to an entrance corridor that belongs to one route. Write down what happens in each odd case: overlapping zones, uncovered space, teleport, respawn, camera change, walking back the other way, and a player parked on the edge. Move smoothly toward target weights instead of launching a fresh tween on every update. Choose linear or another crossfade only after checking the real clips (loops that are correlated add up differently from unrelated material). The paper found no universal crossfade time or border width. | OPINION | E00 (authored recommendation, 2026-10-21) | E2, E4, E5 | ENV: weights and edge cases / [sound-owns] crossfade law |
| AM17 | 296 | Exposure is not altitude alone. Treat height, shelter and weather as separate inputs: an enclosed room high up need not sound like an open ridge, and a low ravine can channel wind. Drive wind sound, plant motion and flying debris from one agreed weather/exposure state, with local modifiers on top. At a cave mouth, bring outdoor ambience down by the entrance shape and the listener's path, not by a global Y threshold. For rain, tell apart open ground, canopy or awning cover, and fully enclosed space. Proposals inspired by A01-A02, not meteorology and not measured Roblox presets. | OPINION | A01, A02, E00 | E2, E3 | [vfx-owns] debris; [sound-owns] wind audio |
| AM18 | 298 | Streaming changes audio behavior: when the 3D object that holds a Sound or AudioPlayer streams out, the audio stops. On the client, spatial queries can only find content that is currently streamed in, and streaming also raises the add and remove signals. Persistent models cost memory, so keep them few. | VERIFIED | A13 (alias P28), accessed 2026-10-21 | E4 | |
| AM19 | 300 | Lifecycle contract (proposed): zone data and non-spatial controller state must not depend on decorative objects that can stream out. For each critical spatial source, pick and write down a valid positional anchor and a keep-or-rebuild policy (parking an emitter under a non-positional container does not count). At stream-out, cancel that source's pending events and release its graph instances. At return, rebuild exactly once so loops never double. Test leave, return, leave again, not just the first spawn. Do not mark the whole map persistent to fix an ambience bug. | OPINION | A05, A13 | E4, E5 | |

### 1.4 Ambience map template and the four-zone example (EP:302-314)

| ID | EP | Lesson | Tag | Src | Stage | Role |
| --- | --- | --- | --- | --- | --- | --- |
| AM20 | 304 | Every map row needs the 16 fields listed in section 6 (AF01-AF16). A missing number is written UNKNOWN, never 0. Role split the paper states: ENV authors placements and transitions; the sound designer owns clips and mix; the VFX designer owns effects; the game designer owns route and cue priority; the owner approves the experience. | OPINION | E00 | E2 | [sound-owns] [vfx-owns] [game-designer] |
| AM21 | 306 | The filled example is a planning illustration: no level was built, and it is not a shipped studio map. Its four zones form an imagined stage. Real coordinates, extents and path lengths have to come from the approved blockout, which the paper was not given. Number fields stay open on purpose, because invented studs would break the brief. The source IDs and landmark anchors are only authoring assignments; no such instances exist. | OPINION | E00 | E2 | |
| AM22 | 314 | Completion gate: before the work is accepted for implementation, each measurement-pending field is filled with real data (exported blockout coordinates or reviewed mix data), with units, revision and the responsible agent written beside it. The example is a finished design brief, not a parameter sheet pretending to be complete. A range must never be inferred from an asset's filename. | OPINION | E00 | E2 to E5 | |

Four-zone example (EP:308-312). Columns in the paper: zone and feel; sound layers and anchors; ranges, gains, transitions; visual cause, review, fallback. All distances, extents and gains are UNKNOWN in the paper (no number appears), tag OPINION, src E00 (anchors also lean on A01, A02).

| ID | EP | Zone, feel, bounds | Sound layers and anchors | Ranges, gains, transitions | Visual cause, captures, fallback |
| --- | --- | --- | --- | --- | --- |
| ZX1 | 309 | Z-MOUNTAIN: exposed summit. Bounds = summit walkable polygon plus approved vertical volume; measurement pending. | Wind continuity layer; intermittent gusts; optional bird at ridge perch BIRD-RIDGE; no automatic frog ambience. | Wind strength follows exposure and weather, not height alone. BIRD-RIDGE curve and gain UNKNOWN. Summit-to-falls corridor follows the descent route; transition width and time UNKNOWN until a route capture exists. | One shared gust state moves grass, flags and approved debris. Capture summit at eye level, reverse view, overhead of zone bounds. Fallback keeps wind identity, drops optional wildlife and particles. |
| ZX2 | 310 | Z-FALLS: loud water landmark and route reward. Bounds = basin plus approach; measurement pending. | FALL-MAIN anchor at the visible turbulent fall and impact region; RIVER-OUT follows the visible outflow; intermittent spray detail only if the mix needs it. | Audible from a designated approach checkpoint before the first visual reveal. FALL-MAIN and RIVER-OUT range and gain UNKNOWN; measure listener-to-anchor distance at approach, near basin, cave entrance. Basin-to-swamp overlap runs along the outflow, not a hard switch. | Water motion, splash origin and spray line up with the sound position. Capture approach occluder, reveal, close basin, reverse exit. Optional spray detail ranks below waterfall identity. |
| ZX3 | 311 | Z-SWAMP: quieter wet life with readable hazards. Bounds = wetland route volume; measurement pending. | Insect continuity layer if approved; FROG-REEDS = intermittent calls at reed clusters; BIRD-CANOPY = eligible only in a chosen time or weather state; never a global chorus running all the time. | Frog and bird range and gain UNKNOWN; after mix review, keep them clear of the frequencies used by gameplay warnings. River stays audible only while the outflow is an intended source. Cave-mouth blend keyed to the entrance corridor. | Reeds, local ripples and a few fireflies; not every frog needs to be seen. Capture the path silhouette with effects on and with them off, an overhead map of sources, and the lowest-detail view. Cut optional fireflies before any effect the player navigates by. |
| ZX4 | 312 | Z-CAVE: enclosed, sparse, locally resonant. Bounds = chambers plus entrance corridor; measurement pending. | Optional quiet room layer; DRIP-POOL = localized intermittent drops from the wet ceiling into the pool; PEBBLE-LEDGE occasional eligible event; no invented perpetual waterfall beyond its intended carry. | Every curve and gain UNKNOWN. Pick acoustic simulation or authored reverb as the baseline and record the pick. The outdoor layer fades back across the mouth; no decay preset is required. Test at the mouth, first bend, deep chamber and on the way back. | Wet marks and pool match the drip zone; pebbles need a plausible ledge. Capture mouth looking in and out, chamber at eye level, section view. Fallback keeps dry localized drips if the acoustic simulation degrades. |

### 1.5 Seven-source table (EP:316-327)

Rule (EP:318, OPINION, E00, 2026-10-21): none of the primary sources reviewed provides a typical Roblox range or a correct gain that carries over to any source below. The right range depends on the geometry, the clip, the listener, competing gameplay and the reveal wanted. So UNKNOWN is a finding, not a gap. The A04 demo's 50 and 70 stud attenuation numbers (the paper does not say which parameters) and the A05 API bounds must not be relabeled as presets for these sources.

| ID | EP | Source | Typical Roblox range | Volume guide | Visual and placement proposal | Tag and src |
| --- | --- | --- | --- | --- | --- | --- |
| SS1 | 321 | Waterfall | UNKNOWN | Mix against route cues; set listening checkpoints at approach and near; no fixed gain | Source at the real fall and impact; spray and outflow match | OPINION; A04, A05 (2026-10-21); A02 spatial-water example (2025-11-06) |
| SS2 | 322 | River | UNKNOWN | Do not let identical loud loops pile up unchecked | Anchor or segments follow the flowing channel, not the dry bank | OPINION; A05 |
| SS3 | 323 | Wind | UNKNOWN (a bed that is not spatial has no emitter range) | Follow a weather/exposure curve and shelter response, not one universal Volume | Plants, flags and drifting particles share the wind state | OPINION informed by EXPERIENCE A01, A02 |
| SS4 | 324 | Fire | UNKNOWN | Local crackle, signed off against the interaction cues | Origin at the fire; sparks and smoke only while it burns | OPINION; A04, A05, A16 (2026-10-21) |
| SS5 | 325 | Frogs | UNKNOWN | Intermittent, locally eligible calls; overlap reviewed | Wet habitat or reeds; an unseen animal is fine if habitat is plausible | OPINION informed by procedural amphibians in A02 (2025-11-06) |
| SS6 | 326 | Cave drips | UNKNOWN | Keep spacing and quiet; approve echo separately | Wet ceiling and the pool that receives the drops; if a visible hero drip is meant to be the same event, line it up with the sound | OPINION; A08, A09 (2026-10-21) |
| SS7 | 327 | Birds | UNKNOWN | Eligibility by time, weather, biome; protect directional gameplay cues | Perches, canopy or flight path; no visible bird required per call | OPINION informed by A02 (2025-11-06) |

All seven rows: [sound-owns] clips, gains, ranges; ENV supplies placement and visible cause. Stage E2 (plan), E3 (place), E5 (listen).

### 1.6 Section 6 evidence summary (EP:329-335)

| ID | EP | Rule | Number | Mark | Src, date |
| --- | --- | --- | --- | --- | --- |
| ES6-1 | 332 | Audio is now a wired graph; legacy AmbientReverb is a separate system | API default values must not be used as mix targets | VERIFIED | A04-A11, accessed 2026-10-21 |
| ES6-2 | 333 | Source positions and gains come from the real stage | 7 source types; every range UNKNOWN | OPINION | E00, 2026-10-21 |
| ES6-3 | 334 | Plan for stream-out and return | No universal radius for keeping content | VERIFIED; the lifecycle rule is OPINION | A13, accessed 2026-10-21 |
| ES6-4 | 335 | Acoustic simulation: fully released, quality adapts | Release update dated 2026-09-22 | VERIFIED | A09, 2026-09-22 |

## 2. Section 7: ambient visual life (EP:337-359)

| ID | EP | Lesson | Tag | Src | Stage | Role |
| --- | --- | --- | --- | --- | --- | --- |
| VL01 | 339 | Workspace.GlobalWind moves terrain grass and clouds. A ParticleEmitter follows it only if WindAffectsDrag is on and Drag is above 0; Fire and Smoke objects follow without that setup. The Reduce Motion setting slows animated grass but leaves the wind direction alone. | VERIFIED | P12, accessed 2026-10-21 | E3 | [vfx-owns] emitters |
| VL02 | 339 | Feed vegetation motion, VFX and the sound designer's wind layer from one authored wind state. Do not assume that custom mesh plants or audio read GlobalWind by themselves. | OPINION | E00 (P12 context) | E2, E4 | [vfx-owns] [sound-owns] |
| VL03 | 341 | Particle cost follows the screen area covered and the number of stacked transparent layers, not just the emitter count. Documented per-emitter rate caps: 400 particles/second, 100/second on mobile. Lifetime is limited to 20 seconds. These are engine ceilings, not amounts that are safe to spend in a scene. LightEmission = 1 means additive blending; it does not stand in for a local light. Flipbook animation can be switched off when memory is tight. | VERIFIED | P13 (alias A16), accessed 2026-10-21 | E3, E5 | [vfx-owns] |
| VL04 | 341 | Review particles at low and at high Studio quality, then on real hardware. | Advice sentence inside a VERIFIED paragraph (my reading: OPINION) | P13 | E5 | |
| VL05 | 343 | Classify each ambient effect by its job: spatial cue, material reaction, weather or decorative life. ENV states where it sits, which way it points, its visible extent, why it matters and what replaces it; the VFX designer owns the authored emitters. Waterfall spray sits where water lands and churns, loose leaves follow the wind state, cave drips start from surfaces that could plausibly be wet. | OPINION | E00 | E2, E6 | ENV places / [vfx-owns] |
| VL06 | 343 | Keep activation and cleanup ownership per zone. On re-entry do not clone effects again until the previous zone instance is confirmed retired. | OPINION | E00 | E4 | |
| VL07 | 343 | Keep decorative motion out of the route and hazard silhouette envelope set by the game designer. Nothing found fixes a universal safe quantity of fireflies, birds, smoke layers or props that move, for phones. | OPINION | E00 | E2, E5 | [game-designer] envelope |
| VL08 | 351 | Ambient restraint: every moving effect needs a reason, a region, a visual priority and a rule for when it is switched off. Dust belongs where light and open space let it be seen; leaves near plants or along a wind path; fireflies must not compete with collectible or attack markers. A deliberate, readable cluster beats the same effect spread everywhere. Do not cover a phone screen in layered mist only to hide a bare background. A single quiet moving prop can suggest life without any particle blanket. All systems read the environment's shared weather state; none rolls its own randomness. | OPINION | E00 (design proposals, 2026-10-21) | E2, E3 | [vfx-owns] |
| VL09 | 353 | Budgets and degradation: the paper found no universal figure for how many ambient sounds, acoustic emitters, reverb nodes or moving props a Roblox phone can run at once. A hardware voice limit, a PS5 case-study count or an emitter rate maximum must not be restated as a performance guarantee. Begin with the smallest setup that conveys the place, profile the busiest overlap on the target phone, and add more only while frame time and memory stay inside the project's budgets. Log: simultaneous players, emitters and effect nodes; loaded audio memory; how much of the screen particles cover; the device quality mode. When cutting, remove optional one-shots and decorative layers first and navigation cues last (a proposed order, not an engine guarantee). | OPINION | A09, A16 (bound) | E5 | [sound-owns] voice caps, priority |

Paper table inside section 7 (EP:345-349) and its evidence summary (EP:355-359):

| ID | EP | Rule | Number | Mark | Src, date |
| --- | --- | --- | --- | --- | --- |
| VLT1 | 346 | Wind-driven emitter prerequisite | Drag above 0 and WindAffectsDrag = true | VERIFIED | P12, accessed 2026-10-21 |
| VLT2 | 347 | A rate cap is not a budget for the stage | 100/s on mobile; 400/s elsewhere (documented per-emitter cap) | VERIFIED | P13, accessed 2026-10-21 |
| VLT3 | 348 | Lifetime has a built-in cap | 20 seconds | VERIFIED | P13, accessed 2026-10-21 |
| VLT4 | 349 | Check close-up spray and smoke views as well as far-away showcase views | Screen coverage and layer count; approved budget UNKNOWN | OPINION, resting on the verified fill-rate behavior | P13, accessed 2026-10-21 |
| ES7-1 | 358 | One shared weather state, with a named owner per effect | No universal count of ambient effects | OPINION | E00, 2026-10-21 |
| ES7-2 | 359 | Particle caps are not a phone budget for the stage | 100/s mobile per emitter; 20 s lifetime cap | VERIFIED | P13, A16, accessed 2026-10-21 |

## 3. Section 8: set dressing and detail (EP:361-389)

| ID | EP | Lesson | Tag | Src | Stage | Role |
| --- | --- | --- | --- | --- | --- | --- |
| SD01 | 365 | Every dressing cluster serves a purpose: it can show use, history, ownership, movement, damage, ecology or an activity under way. Crates in large numbers tell no story by themselves; how they sit can mean delivery, storage, a barricade or abandonment, and each reading leads to different silhouettes, paths and collision needs. Decide the reading first, then choose how the props are spread. | OPINION | E00 | E2 | |
| SD02 | 367 | Split objects into composition-critical and swappable detail. An arch that frames the destination is part of the composition contract; a small rope on the ground can be exchanged. Record each object's role in the scene manifest, so an AI cleanup pass can tell which edits need art-direction or design review. | OPINION | E00 | E2, E6 | [art-director] [game-designer] review |
| SD03 | 369 | Use calm areas on purpose. Walkable ground may need quiet value structure so characters, pickups and ability effects stay readable; a narrative alcove can hold more detail because the player may stop and look. "Empty" is a question of function, not an instance count. A bare room that gives no sense of direction, story or spatial rhythm may call for one intentional structural element, not scattered small props. | OPINION | E00 | E2 | [art-director] value structure |
| SD04 | 373 | Repetition is a question of composition, not only of assets. A kit should allow variation in grouping, rotation, spacing, height, material treatment and surroundings. Do not answer visible repetition just by making more unique meshes; first see whether the same modules can be arranged into different large forms and gaps. Hold attachment conventions fixed so rearranging stays dependable. | OPINION | E00 | E2, E3 | [modeler] kit |
| SD05 | 375 | In Blender a linked duplicate points at the same mesh data but has its own object transform, which keeps kit edits consistent in the authoring scene. Nothing here promises how Roblox deduplicates or draws the imported resources; follow the real mesh and texture references after import. | VERIFIED (B07); OPINION (import caution) | B07, accessed 2026-10-21; E00 | E3, E5 | [modeler] |
| SD06 | 377 | Judge a repeated facade from the camera path players will really use, not a close still. A recurring highlight, stain, window beat or outline can expose the repeat even if the mesh itself is quiet, and a pan along the row makes it plainer. Record a traversal clip and measure it against the art bible's tolerance for repetition. | OPINION | E00 | E5 | [art-director] tolerance |
| SD07 | 381 | Separate deliberate intersection from defect. A rock sunk into a bank can be valid construction; a chair hovering over the floor is normally a defect unless the story needs it. A flat ban on all intersection would reject good modular building. Mark where overlap is approved, what ground contact is expected, and how much clearance moving parts need. | OPINION | E00 | E2, E5 | |
| SD08 | 383 | For each prop family record: the surface it rests on, pivot location, allowed slope handling, collision role, visibility priority, and placement exclusions (route lanes, interaction approach volumes, camera corridors, source emitters, VFX attachment zones). A script can check these, but where its geometry test is only a bounding-box estimate it has to say how uncertain the result is. | OPINION | E00 | E2, E5 | [modeler] pivot; [game-designer] lanes |

Paper evidence summary (EP:385-389):

| ID | EP | Rule | Number | Mark | Src, date |
| --- | --- | --- | --- | --- | --- |
| ES8-1 | 388 | Give detail by meaning and attention priority | No prop density is required | OPINION | E00, 2026-10-21 |
| ES8-2 | 389 | Share mesh data, but do not assume Roblox keeps it shared | Linked data, separate transforms | VERIFIED; import caution OPINION | B07, accessed 2026-10-21 |

## 4. Section 9: terrain and nature (EP:391-403)

| ID | EP | Lesson | Tag | Src | Stage | Role |
| --- | --- | --- | --- | --- | --- | --- |
| TN01 | 393 | Terrain is a grid of 4x4x4-stud cells, each with an occupancy value 0-1 and a material; interpolation gives the smooth look. Heightmap import: 1 pixel stands for 4 studs; JPEG or PNG; up to 4096x4096 pixels. Terrain can recolor materials, hold water and show animated Grass decoration. The documented GrassLength range is 0.1-1. | VERIFIED | P14, P15, accessed 2026-10-21 | E1, E3 | |
| TN02 | 393 | Do not treat GrassLength as proof of a real blade height in meters. Do not take a heightmap resolution as a suggested world size. | OPINION | P14 | E2 | |
| TN03 | 395 | Terrain versus mesh: Terrain fits where a continuous, sculptable volume and smooth material blends help; meshes fit where the design needs chosen silhouettes, hard stylized strata, overhangs, modular reuse or exact UV direction. Combine large terrain masses with reusable rock and foliage kits. Re-check seams from player eye height and from the extreme points of traversal. Concentrate foliage around readable masses instead of spreading it evenly. Do not claim Terrain always beats mesh terrain for speed; no universal like-for-like benchmark exists. Compare on the target phone with the same camera coverage, material variety, collision needs and streaming state. | OPINION | P14, P15 (scope); P24, P25 (measurement) | E2, E5 | [modeler] kits |
| TN04 | 397 | Split water into separate responsibilities: the visible surface or volume, how the player moves in it, its sound sources, mist, and shoreline dressing. For an organic landmark, protect the silhouette at every viewing distance before small cracks. A biome is a coordinated set of palette, material, wind and sound, not just Terrain materials in other colors. | OPINION | E00 | E2 | [sound-owns] [vfx-owns] [art-director] |

Paper table inside section 9 (EP:399-403):

| ID | EP | Rule | Number | Mark | Src, date |
| --- | --- | --- | --- | --- | --- |
| TNT1 | 400 | Work with Terrain's native cell size | 4x4x4 studs; occupancy 0-1 | VERIFIED | P15, accessed 2026-10-21 |
| TNT2 | 401 | A heightmap's maximum size is no performance budget | 1 pixel = 4 studs; max 4096x4096 pixels | VERIFIED | P14, accessed 2026-10-21 |
| TNT3 | 402 | Decoration range is just a property setting | GrassLength 0.1-1 | VERIFIED | P14, accessed 2026-10-21 |
| TNT4 | 403 | Choose Terrain or mesh by measuring a like-for-like scene | No universal cost ratio found | OPINION | P14, P15 (capability scope); P24, P25 (measurement) |

## 5. Section 10: cohesion with the art director (EP:405-433)

| ID | EP | Lesson | Tag | Src | Stage | Role |
| --- | --- | --- | --- | --- | --- | --- |
| CO01 | 409 | The art bible is a versioned input. Before starting a stage, note the approved version, palette roles, shape families, material response, light-direction conventions, detail hierarchy, reference anchors and the points that stay flexible. A lock can set how angular cliffs are in general without fixing every rock's position. Naming the flexible parts keeps places from becoming clones while the world stays recognizable. | OPINION | E00 | E0 | [art-director] |
| CO02 | 411 | An environment reference image shows the look to aim for; it is not a full geometric plan. A generated picture can hide impossible routes, mismatched scale, or lighting the target graphics tier cannot reproduce. Turn it into an annotated target listing the focal point, the camera, the walkable area, silhouette layers, material roles, light sources and every unclear point that needs a decision. Keep the approved fantasy, and settle the unclear points with the game designer and art director. | OPINION | E00 | E0, E1 | [art-director] [game-designer] |
| CO03 | 413 | Make one target scene that contains a typical character, an environment surface, a UI state, an ability effect and an interactive object, and judge the environment with all of them present. A background that is rich on its own may fight the character's outline or bury the moment of an attack. Reduce or relocate the competing environment signal instead of brightening every foreground item. | OPINION | E00 | E1, E5 | [art-director] [vfx-owns] |
| CO04 | 417 | Who gives what: art director = hierarchy and style limits; game designer = route, interaction and pacing intent; modeler = reusable geometry and material structure; rigger and animator = how far plants, doors, machines and creatures move; sound designer = source design and mix; VFX designer = particle or shader craft; ENV = placement, spatial purpose, scene context, what must stay visible, and transition behavior; the owner rules on conflicts that matter. | OPINION | E00 | E0, E6 | all roles listed |
| CO05 | 419 | A good request to the sound designer says what the player should work out, not just which file to use. The paper's example, restated: the waterfall becomes a believable spatial clue before the turn, is still present at the overlook, and loses high-frequency presence inside the cave in line with the approved acoustic setup. A VFX request points at the same source, the wind state and the visibility limits. Neither request presents gain values or expensive particle counts as researched fact. | OPINION | E00 | E6 | [sound-owns] [vfx-owns] |
| CO06 | 421 | Keep a shared environment state record: time of day, weather, wind, water state, event state, zone. It is a coordination contract, not a call to write one monolithic script; each craft subscribes to what it needs. Do not show strong wind in flags over a perfectly still interior soundscape unless the mismatch is a narrative choice. | OPINION | E00 | E4 | [sound-owns] [vfx-owns] |
| CO07 | 425 | When a stage drifts from the target, classify before giving feedback: wrong large shape, right shape badly framed, wrong value hierarchy, inconsistent material response, or a different camera, exposure or graphics tier. Fixing the wrong layer breeds compensating errors; example: a darker texture can hide an over-strong fill light while ruining the material elsewhere. | OPINION | E00 | E5 | [art-director] |
| CO08 | 427 | Review note fields: location and camera; observed defect; intended reading; likely cause; responsible specialist; constraints to keep; evidence needed for acceptance. Avoid mood-only notes that do not say whether the fault is focal hierarchy, depth, light direction or motion. ENV may propose a fix but leaves the specialist room to choose the implementation. | OPINION | E00 | E5, E6 | |

Paper evidence summary (EP:429-433):

| ID | EP | Rule | Number | Mark | Src, date |
| --- | --- | --- | --- | --- | --- |
| ES10-1 | 432 | Version the art targets and write down exceptions | No universal palette ratio | OPINION | E00, 2026-10-21 |
| ES10-2 | 433 | Review the environment together with characters, UI and effects | Shared cameras and scene states | OPINION | E00, 2026-10-21; C02, 2014-11-11 |

## 6. Ambience map fields proposed by the paper

The lead builds `ambience-map.md` from this section. "Category" is my mapping onto the lead's eight words (zone, layer, cause, point source, blend, state, lifecycle, priority); the paper does not use these category names. All fields are OPINION (E00) unless stated.

### 6.1 The 16-field row (EP:304)

| ID | EP | Field | What it holds (paper) | Category | Filled by |
| --- | --- | --- | --- | --- | --- |
| AF01 | 304, 292 | Zone ID | Stable ID, never renamed | zone | ENV |
| AF02 | 304, 292 | Bounds / transform and height range | Transform, half-extents or another stated shape, vertical limits; numbers come from the approved blockout and stay measurement-pending until then | zone | ENV |
| AF03 | 304, 292 | Listener policy | Camera or avatar counts as the listener | zone | ENV, checked by [sound-owns] |
| AF04 | 304 | Semantic intent | What the player should infer or feel in the zone | zone | ENV, [game-designer] |
| AF05 | 304, 266 | Continuous layer | Non-directional continuity, only if needed; may be absent | layer | [sound-owns] designs, ENV records |
| AF06 | 304, 266 | Intermittent events with eligibility | Authored one-shots; eligible by time, weather, biome or state | layer | [sound-owns] |
| AF07 | 304, 309-312 | Positioned-source IDs / anchors | ID plus landmark anchor (examples: FALL-MAIN, RIVER-OUT, BIRD-RIDGE, FROG-REEDS, BIRD-CANOPY, DRIP-POOL, PEBBLE-LEDGE) | point source | ENV |
| AF08 | 304, 272-274 | Attenuation mode / curve / terminal distance | Active mode, stored curve, end distance at gain 0; position semantics (PositionType / PositionInstance) | point source | [sound-owns] curve; ENV anchor |
| AF09 | 304 | Gain reference and approved mix revision | Reference level and the mix revision that approved it | layer, priority | [sound-owns] |
| AF10 | 304, 286 | Acoustic treatment | Explicit choice: authored graph reverb or acoustic simulation; record which | layer | [sound-owns], ENV records |
| AF11 | 304 | Visible causal partners | Visible thing that explains each sound or motion (fall, pool, reeds, wet ceiling) | cause | ENV, [vfx-owns] |
| AF12 | 304, 292, 294 | Neighbor transition | Neighbor zone, transition corridor, overlap rule | blend | ENV |
| AF13 | 304, 300 | Streaming lifecycle | Anchor, retention or rebuild policy, stream-out cleanup | lifecycle | ENV |
| AF14 | 304, 353 | Degradation priority | What is dropped first; optional one-shots and decor before navigation cues | priority | ENV, [sound-owns] |
| AF15 | 304, 309-312 | Capture / listening checkpoints | Named camera views and listening points (e.g. approach, near basin, cave mouth, first bend, deep chamber) | state (verification) | ENV |
| AF16 | 304 | Owner and approval state | Who owns the row and whether it is approved | state (approval) | ENV, owner |

### 6.2 Further fields the paper proposes elsewhere in the range (all OPINION, E00, at the EP lines shown)

| ID | EP | Field | What it holds (paper) | Category |
| --- | --- | --- | --- | --- |
| AF17 | 292 | Zone priority | Priority among overlapping zones | priority |
| AF18 | 292 | Neighbors list | Adjacent zones | blend |
| AF19 | 292, 294 | Transition corridor | Route-specific entrance corridor used for weights | blend |
| AF20 | 294 | Blend weight rule | Weights from signed distance to boundary or corridor; written handling of overlap, gaps, teleport, respawn, camera change, reverse travel and edge-standing | blend |
| AF21 | 294 | Smoothing | Smooth toward target weights; no new independent tween each update; crossfade law checked on real clips; duration and border width UNKNOWN | blend |
| AF22 | 296, 421 | Weather / exposure state | Shared state (time of day, weather, wind, water state, event state, zone) plus local modifiers; rain split into exposed, canopy, enclosed | state |
| AF23 | 266 | Layer function class | (a) continuity, (b) intermittent life, (c) world sources, (d) weather/exposure modulation | layer |
| AF24 | 300 | Positional anchor and retention policy | Valid anchor for each critical spatial source | lifecycle |
| AF25 | 300 | Stream-out / return handling | Cancel source events, release graph instances; rebuild once on return; leave-return-leave test | lifecycle |
| AF26 | 343 | Effect activation and cleanup owner | Per zone | lifecycle |
| AF27 | 343 | Ambient effect spec from ENV | Location, direction, visible bounds, relevance, fallback; function class (spatial cue, material reaction, weather, decorative) | cause, point source |
| AF28 | 351 | Moving-effect contract | Reason, region, visual priority, disable policy | cause, priority |
| AF29 | 309-312 | Fallback | Per-zone low-detail behavior (keep identity, drop optional layers) | priority |
| AF30 | 314 | Units, revision, responsible agent | For every replaced measurement-pending field | state |
| AF31 | 353 | Measurement log | Concurrent players, emitters, effect nodes; loaded audio memory; particle screen coverage; device quality mode | state |
| AF32 | 304 | UNKNOWN rule | A missing number is UNKNOWN, never 0 | state |

### 6.3 Related contracts (not the ambience map; all OPINION, E00)

| ID | EP | Contract | Fields |
| --- | --- | --- | --- |
| RC1 | 367 | Scene manifest role tag | composition-critical or exchangeable |
| RC2 | 383 | Prop family | support surface, pivot, slope treatment, collision role, visibility priority, placement exclusions |
| RC3 | 381 | Intersection record | approved overlap zones, ground-contact expectation, moving-part clearance |
| RC4 | 409 | Art-bible input | version, palette roles, shape families, material response, light direction, detail hierarchy, reference anchors, flexible items |
| RC5 | 411 | Annotated reference target | focal point, camera, walkable area, silhouette layers, material roles, light sources, open questions |
| RC6 | 419 | Brief to sound or VFX | what the player should infer; same source, wind state, visibility limits; no unsupported gains or counts |
| RC7 | 427 | Review note | location and camera, defect, intended reading, likely cause, responsible specialist, constraints, acceptance evidence |

## 7. Claims to fact-check

Kinds: audio-API, audio-behavior, acoustic-sim, streaming, query-API, wind, particle, terrain, blender, number, industry. "Risk" = my guess of how likely the claim is version-sensitive or mis-stated (H/M/L), not a verdict. Numbers are listed with their unit as the paper gives it. Source IDs resolve in section 9. Items marked ! are the five I most want checked.

| ID | Claim | EP | Src | Kind | Tag | Risk |
| --- | --- | --- | --- | --- | --- | --- |
| CK01 | Sound, SoundGroup, SoundEffect are discouraged for new work in favor of audio objects | 270 | A04 | audio-API | VERIFIED | M |
| CK02 | Graph roles: AudioPlayer stream, Wire connection, AudioEmitter into the world, AudioListener receives, AudioDeviceOutput to the device | 270 | A04 | audio-API | VERIFIED | L |
| CK03 | Wiring AudioPlayer directly to AudioDeviceOutput is non-spatial | 270 | A04 | audio-behavior | VERIFIED | L |
| CK04 | The guide's standalone 3D demo uses 6 objects; its attenuation numbers are 50 and 70 studs (paper's wording: "50/70-stud demonstration"; which properties is not stated) | 270, 318 | A04 | number | VERIFIED (doc example, not a preset) | M |
| CK05 ! | AudioEmitter custom distance curve accepts up to 400 distance/gain pairs | 272 | A05 | number | VERIFIED | H |
| CK06 ! | Curve gains lie in [0,1]; linear interpolation; end values held outside the supplied domain | 272 | A05 | audio-behavior | VERIFIED | H |
| CK07 ! | DistanceAttenuationMode defaults to Custom; preset modes use DistanceAttenuationBounds with default [4,10000] (unit not stated) | 272 | A05 | number | VERIFIED | H |
| CK08 | PositionType default is Parent; PositionInstance names a different positional instance if PositionType is Instance | 272 | A05 | audio-API | VERIFIED | M |
| CK09 | GetAudibilityFor reports combined distance and angle attenuation, not final loudness | 272 | A05 | audio-API | VERIFIED | M |
| CK10 ! | A preset attenuation mode overrides the stored custom curve (the paper's inference, EP:274) | 274 | A05 | audio-behavior | OPINION | H |
| CK11 | An emitter under a non-positional parent can end up inaudible or unpositioned | 274, 300 | A05 | audio-behavior | OPINION | M |
| CK12 | AudioFader multiplies stream volume; Volume range 0-3 (CORRECTED: 0-10, fact-check AU12) | 276 | A06 | number | VERIFIED | H |
| CK13 | AudioFilter exposes FilterType, Frequency, Gain, Q | 276 | A07 | audio-API | VERIFIED | M |
| CK14 | AudioReverb exposes decay, delay, dry/wet and filtering controls (register key word: DecayTime) | 276 | A08 | audio-API | VERIFIED | M |
| CK15 ! | Acoustic simulation: client beta announced 2026-01-28; full-release update 2026-09-22 | 278, 335 | A09 | acoustic-sim | VERIFIED | H |
| CK16 ! | Acoustic simulation gives automatic occlusion, diffraction and reverberation via the advanced audio system | 278 | A09 | acoustic-sim | VERIFIED | H |
| CK17 | SoundService holds the global enable for acoustic simulation; emitter and listener settings also matter | 278 | A09, A05 | acoustic-sim | VERIFIED | H |
| CK18 | Simulation accuracy may reduce, or features disable, to maintain frame rate | 278, 286 | A09 | acoustic-sim | VERIFIED | H |
| CK19 ! | As of the 2026-09-22 update, Sound-instance support in acoustic simulation is still in development | 278 | A09 | acoustic-sim | VERIFIED | H |
| CK20 | SoundService.AmbientReverb applies to Sound instances only, not AudioPlayer/AudioEmitter graphs | 280 | A10 | audio-API | VERIFIED | M |
| CK21 | SoundService.DefaultListenerLocation (PluginSecurity) is the current name; overview page still says ListenerLocation | 280 | A10, A04 | audio-API | VERIFIED | H |
| CK22 | Sound has RollOffMinDistance, RollOffMaxDistance, RollOffMode; Volume multiplicative, range 0-10; guide says loud source audio likely needs no Volume above 2 | 282 | A17 | number | VERIFIED | M |
| CK23 | AudioPlayer.Asset is current; AssetId deprecated; IsReady exists | 284 | A11 | audio-API | VERIFIED | M |
| CK24 | GetPartBoundsInBox and GetPartBoundsInRadius test part bounding boxes; GetPartsInPart tests occupied volume | 290 | A12 (B10) | query-API | VERIFIED | M |
| CK25 | Old Region3 query methods are deprecated | 290 | A12 (B10) | query-API | VERIFIED | M |
| CK26 | SoundService's tagged-part dynamic-reverb example omits absolute-coordinate and lower-bound checks | 290 | A10 | audio-behavior | VERIFIED | L |
| CK27 ! | Audio from a Sound or AudioPlayer stops once the 3D object it is parented to streams out | 298 | A13 | streaming | VERIFIED | H |
| CK28 | Client spatial queries see only streamed-in content; add/remove signals fire for streaming | 298 | A13 | streaming | VERIFIED | M |
| CK29 | Persistent models consume memory (so keep them minimal) | 298 | A13 | streaming | VERIFIED | L |
| CK30 | Workspace.GlobalWind drives terrain grass and clouds | 339 | P12 | wind | VERIFIED | M |
| CK31 | ParticleEmitters follow GlobalWind only if WindAffectsDrag is on and Drag > 0; Fire and Smoke follow by default | 339, 346 | P12 | wind | VERIFIED | H |
| CK32 | Reduce Motion lowers animated-grass speed, not its vector direction | 339 | P12 | wind | VERIFIED | M |
| CK33 ! | Single-emitter rate caps: 400 particles per second; 100 per second on mobile | 341, 347, 359 | P13 (A16) | number | VERIFIED | H |
| CK34 ! | Particle Lifetime capped at 20 seconds | 341, 348, 359 | P13 (A16) | number | VERIFIED | H |
| CK35 | Particle cost depends on screen pixels covered and overlapping transparent layers, not emitter count alone | 341 | P13 (A16) | particle | VERIFIED | M |
| CK36 | LightEmission = 1 selects additive blending | 341 | P13 | particle | VERIFIED | M |
| CK37 ! | Flipbooks may be disabled under memory pressure | 341 | P13 | particle | VERIFIED | H |
| CK38 | Terrain uses 4x4x4-stud cells with occupancy 0-1 and a material; interpolation smooths the surface | 393, 400 | P15 | terrain | VERIFIED | M |
| CK39 ! | Heightmap import: 1 pixel = 4 studs; JPEG or PNG; up to 4096x4096 pixels | 393, 401 | P14 | number | VERIFIED | H |
| CK40 | Terrain supports material color changes, water, animated Grass decoration | 393 | P14 | terrain | VERIFIED | M |
| CK41 ! | GrassLength documented range 0.1-1 | 393, 402 | P14 | number | VERIFIED | H |
| CK42 | Blender linked duplicates share mesh data and keep separate object transforms | 375, 389 | B07 | blender | VERIFIED | L |
| CK43 | Ghost of Tsushima audio claims in AM01 (wind tied to slats, roofs, paper screens; residual drips after rain; per-mode mix priority) | 260 | A01 | industry | EXPERIENCE | L |
| CK44 | Ghost of Yotei audio claims in AM02 (4 mono wind emitters; 8-channel cube layers for rain and snow; 4 surface-dependent mono rain layers; no ambisonic beds; near/mid/far Sound Scenes) | 262 | A02 | industry | EXPERIENCE | M |
| CK45 | Sea of Thieves: sound changes below deck | 264 | A03 | industry | EXPERIENCE | L |

The five "most need checking" groups: (1) CK15-CK19 acoustic simulation status; (2) CK05-CK07 and CK10 attenuation facts; (3) CK27 stream-out stops audio; (4) CK33, CK34, CK37 particle caps and flipbooks; (5) CK31, CK39, CK41 wind drag prerequisite, heightmap and GrassLength. CK12, CK20, CK21 are next in line.

## 8. Contradictions and limits

| ID | EP | Item | Handling in skills |
| --- | --- | --- | --- |
| X01 | 278, 335 | A09 declares full release, yet its body keeps beta-era wording and its September update says Sound-instance support is still in development. | Describe acoustic simulation as of 2026-09-22 and re-check the installed Studio. Never call Sound support shipped. |
| X02 | 280 | Property naming drift: DefaultListenerLocation (API page) versus ListenerLocation (overview page). | Check the installed API; do not hard-code either name from the paper. |
| X03 | 276, 282 | The paper contrasts AudioFader Volume 0-3 with legacy Sound Volume 0-10; fact-check AU12 shows both are 0-10, so the contrast is void. The "no need above 2" hint still belongs to the legacy Sound page only. | Never move legacy Volume advice onto AudioFader. |
| X04 | 284 | Old examples use AssetId; current docs list Asset and mark AssetId deprecated. | Code examples use Asset. |
| X05 | 290 | The SoundService dynamic-reverb example compares points with boxes without absolute-value and lower-bound checks. | Do not copy it. Use the local-space compare in AM15. |
| X06 | 262 | A02 is a counterexample to "one constant stereo bed per biome", but only for a PS5 production. | Use as a pattern (positioned sources, no mandatory bed), never as a Roblox limit. |
| X07 | 264 | A03 video not watched; the page supports attention to space only. | No reverb or implementation claim from Sea of Thieves. |
| X08 | 318 | A04's 50/70-stud demo numbers and A05's API bounds are not source presets. | Leave every source range UNKNOWN until measured on the stage. |
| X09 | 306-314 | The example zones carry no numbers by design. | Keep fields empty (UNKNOWN) in templates; no invented studs. |
| X10 | 294 | No universal crossfade duration or border width. | Skill says "decide per route and clip"; never a default number. |
| X11 | 343, 353 | No universal ambient-effect count, voice ceiling, reverb-node count or phone budget. The studio's `sound-design` skill lists voice caps (S-152: at most 24 one-shots per client on mobile, 32 on PC; Roblox publishes none) as a proposal. | Those caps are the sound skill's PROPOSAL, not paper content. Do not cite the paper for them. |
| X12 | 353, 321-327 | The paper gives no fixed gain for any source; `sound-design` has a priority ladder (S-107/S-108: ambience is tier 7, about -18 dB slot, droppable) and ducks (S-109). Compatible with the paper's drop order (VL09), but those levels are the sound skill's proposals. | Environment skills point to `sound-design` for levels; they quote no dB. |
| X13 | 298, 300 | Observation by me, not in the paper: `sound-design` S-150 has server players for shared ambience; A13 says audio parented to a streamed object stops on stream-out. | Lead to check how a server-owned ambience player gets a streaming-safe anchor (AF24). |
| X14 | 341, 359 | P13 and A16 are one page (aliases). Rate caps are per-emitter ceilings. | Never use 400 or 100 as a scene budget (VL03, VLT2). |
| X15 | 393-403 | GrassLength is a property range, not blade height; heightmap size is a capacity, not a budget; no Terrain-versus-mesh cost ratio. | Measure on the target phone. |
| X16 | 433 | The ES10-2 row cites C02, a preserved reprint of a Riot dev blog (reprint date 2014-11-11, original date not recovered, not official hosting); the row itself is tagged OPINION. | Treat C02 as a dated practitioner voice, not as a Riot rule. |
| X17 | 375 | B07 is Blender behavior; Roblox import may not keep shared mesh data. | Verify runtime references after import (modeler / import fact-check). |
| X18 | 304-314 | The map schema and the four-zone example are proposals; none was built or heard. | Mark all as PROPOSAL until a test stage exists. |
| X19 | alias | Aliases in the register: A12 = B10 (WorldRoot), A13 = P28 (streaming techniques), A16 = P13 (particle emitters). | Cite each page once. |
| X20 | stage | My stage labels E0-E6 and the AF categories are mine, not the paper's. | Lead may remap. |

### 8.1 Values the paper leaves UNKNOWN (never fill with a guess)

| ID | EP | Unknown | Method the paper gives |
| --- | --- | --- | --- |
| UN01 | 318, 321-327 | Typical Roblox range and correct gain for waterfall, river, wind, fire, frogs, cave drips, birds | Measure listener-to-anchor distance at approach, near and entrance checkpoints; reviewed mix data |
| UN02 | 309-312 | All zone bounds, extents, path distances, curves, gains, transition widths and times in the example | Export from the approved blockout; route capture |
| UN03 | 294 | Crossfade duration and border width | Check actual clips; audition |
| UN04 | 334 | Universal retained radius for streaming | Test leave, return, leave |
| UN05 | 343, 353 | Safe count of fireflies, birds, smoke layers, moving props, ambient sounds, acoustic emitters, reverb nodes on phones | Profile busiest overlap on target phone |
| UN06 | 349 | Approved particle screen coverage and layer budget | Compare close-up views; project decision |
| UN07 | 388 | Required prop density | Meaning and attention priority |
| UN08 | 403 | Terrain versus mesh cost ratio | Equivalent-scene measurement (P24, P25) |
| UN09 | 432 | Universal palette ratio | Art bible version |

### 8.2 Overlap with the existing `sound-design` skill (rows marked [sound-owns])

| Paper topic | Existing skill rule | Note |
| --- | --- | --- |
| Graph objects, Asset property | S-140 | Same advice: audio objects, no new Sound objects, Asset property |
| Ambience as droppable layer, degradation | S-107, S-108, S-109 | Skill gives levels; paper gives only the drop order (AM, VL09) |
| Voice and effect counts | S-152 | Skill numbers are proposals (X11) |
| Shared ambience on server | S-150 | See X13 |
| Long-stay loops | S-100 | Paper does not cover it |
| Phone speaker | S-156, S-157 | Paper does not cover it |

## 9. Source IDs used in lines 256-434 (resolved from EP:763-1469)

| ID | Source | Date and evidence | Scope limit (register) | EP |
| --- | --- | --- | --- | --- |
| E00 | The paper's own proposed workflow and templates | 2026-10-21, not an external source | no quotation | 765 |
| A01 | A Sound Effect, Crafting Ghost of Tsushima's Tremendous Sound | 2020-07-22, EXPERIENCE | named interview with Sucker Punch audio director and senior sound designer; not an independent benchmark | 1011 |
| A02 | A Sound Effect, Crafting Captivating Game Audio for Ghost of Yotei | 2025-11-06, EXPERIENCE | named interview; PS5 architecture is not a Roblox mobile budget | 1021 |
| A03 | Rare, Inn-side Story 6: Sound Design (Sea of Thieves) | 2016-10-21, EXPERIENCE | article and video intro inspected; video not watched | 1031 |
| A04 | Roblox, Audio objects | undated live, accessed 2026-10-21, VERIFIED | demo attenuation numbers are examples, not source presets; listener property naming lags the API | 1041 |
| A05 | Roblox, AudioEmitter | undated live, accessed 2026-10-21, VERIFIED | source range, loudness and phone budget not established | 1051 |
| A06 | Roblox, AudioFader | undated live, accessed 2026-10-21, VERIFIED | gain range is not a recommended mix value | 1061 |
| A07 | Roblox, AudioFilter | undated live, accessed 2026-10-21, VERIFIED | property inventory; no frequency or gain recipe | 1071 |
| A08 | Roblox, AudioReverb | undated live, accessed 2026-10-21, VERIFIED | no universal cave preset | 1081 |
| A09 | Roblox DevForum, Full Release: Acoustic Simulation | original 2026-01-28; full-release update 2026-09-22, VERIFIED | Roblox staff post; update says legacy Sound support still in development; body keeps beta wording | 1091 |
| A10 | Roblox, SoundService | undated live, accessed 2026-10-21, VERIFIED | separates legacy Sounds from the advanced graph; printed point-in-box demo not to be copied | 1101 |
| A11 | Roblox, AudioPlayer | undated live, accessed 2026-10-21, VERIFIED | AssetId deprecated, Asset current | 1111 |
| A12 (= B10) | Roblox, WorldRoot API | undated live, accessed 2026-10-21, VERIFIED | register key word GetPartBoundsInBox | 995 |
| A13 (= P28) | Roblox, Instance streaming: techniques and conversion | undated live, accessed 2026-10-21, VERIFIED | official guidance on streaming lifecycle and sound behavior | 1121 |
| A16 (= P13) | Roblox, Particle emitters | undated live, accessed 2026-10-21, VERIFIED | 100 particles/s on mobile is a per-emitter ceiling, not a scene budget | 1151 |
| A17 | Roblox, Sound objects (legacy) | undated live, accessed 2026-10-21, VERIFIED | legacy Volume and rolloff advice only; does not transfer to AudioFader | 1161 |
| P12 | Roblox, Global wind | undated live, accessed 2026-10-21, VERIFIED | official documentation, not an independent benchmark | 1281 |
| P14 | Roblox, Environmental terrain | undated live, accessed 2026-10-21, VERIFIED | same | 1291 |
| P15 | Roblox, Terrain API | undated live, accessed 2026-10-21, VERIFIED | same | 1301 |
| P24 | Roblox, MicroProfiler | undated live, accessed 2026-10-21, VERIFIED | same | 1391 |
| P25 | Roblox, Test on hardware | undated live, accessed 2026-10-21, VERIFIED | emulation cannot fully replace real hardware | 1401 |
| B07 | Blender 5.2 manual, Duplicate Linked | undated live, accessed 2026-10-21, VERIFIED | Blender behavior, not Roblox import | 971 |
| C02 | Riot, Defining the Rift's Visual Style (mobafire reprint) | 2014-11-11 (reprint date), EXPERIENCE | preserved reprint; original date not recovered | 779 |
