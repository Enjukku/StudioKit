---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J008-T10
supersedes: []
---
> Author: environment-designer · claude-opus-5-5 · high · 2026-10-21

# J008-T10 answers to the hidden eval prompts H1-H8

Scope: answers only. Nothing was built, opened in Studio or Blender, or measured for this task. Every check below is a **planned** check (label: not verified) until someone runs it. Numbers come with a source or are `PROPOSAL` / `UNKNOWN`.

Short keys for citations: **ED** = `environment-design` skill (SKILL.md rows E-xx, steps §3); **PR / LA / AB** = its references `place-reading.md`, `light-and-air.md`, `ambience.md`; **RV** = `environment-design/references/review.md`; **EC** = `environment-craft` skill (rows C-xx); **TW / BS / AC / AP / PF / LA2 / HO** = craft references `terrain-and-water.md`, `blender-to-studio.md`, `audit-and-capture.md`, `ambience-in-place.md`, `performance.md`, `studio-light-air.md`, `handoffs.md`; **LD** = `level-design` skill; **N03 / N04 / N05** = `knowledge/reference/environment/03-…`, `04-first-game-stages.md`, `05-roblox-look-dev.md`; **LF / PI / AU** = fact-check rows.

---

## H1. Ground jumps in chunks round buildings, grass above a floor, hill sunk

**(1) Most likely causes (ranked)**
1. **Two height sources that nobody reconciled.** The per-column ground heights were written without the building floor heights. Where ground > floor inside or at the edge of a footprint, grass shows above the floor. Where something forced the ground to a pad, the pad edge is a hard step, so the jumps cluster **round buildings**, not across the whole map.
2. **Whole-cell writes.** Terrain is a 4×4×4-stud cell grid; each cell has occupancy 0-1 that morphs neighbours into a smooth surface (TW §1; LF40, PI25). A writer that fills whole cells (occupancy only 0 or 1, or heights rounded to the next 4 studs) gives a surface that steps in 4-stud chunks and rounds **up** past a floor that sits mid-cell.
3. **Hill on the wrong datum.** The hill's base was set from a different zero (for example the lake level or 0) than the ground round it, or the ground round it was raised later (pads, blends), or, if the hill is a mesh, its pivot is at its centre and it was placed "at ground height".
4. **Possible render-only part:** terrain Grass `Decoration` blades can stand above a floor that sits at surface level even when the data is right (TW §1, LF42-LF43). This must be told apart from cause 1.

**(2) Proof before any change** (check the plan with a script, not by eye: N04 FS-P07; LD rule "measure from coordinates")
- **Delta table from the data (offline, free):** for each building, the floor height; min / median / max ground height inside the footprint; max ground height in a ring round it; and the largest height step between neighbouring columns in the ring versus elsewhere on the map. Ground above floor inside a footprint = cause 1 confirmed for that building. Steps that cluster at the rings = pad edges.
- **Quantisation test:** surface heights modulo 4 in the data. Then one read in the test place: `ReadVoxels` on one bounded region round one bad building (Edit context, read-only, `studio_id` named). Occupancies only 0 or 1 = cause 2 confirmed.
- **Hill:** compare the hill's base contour heights with the ground of the columns just outside it; if it is a mesh, read its extents and pivot (`GetExtentsSize`, BS §3).
- **Grass vs surface:** where the data puts the surface below the floor but grass still shows above it, toggle `Decoration` off on a copy (NotScriptable: a Properties-window step, EC C-09) and capture. Grass gone = render-only.
- **Water:** the same writer touched the lake; check water level against floors and walkways (N04 FS-T08; TW §2.6).
- No tolerance is invented: the delta table is reported as `MEASURED`, not pass/fail (AC §1 verdicts).

**(3) Fix** (at the source: the height data and the terrain writer, not hand-sculpting over symptoms)
- Per building, in the height data: a pad over the footprint at floor height minus a small sink so ground never shows above the floor (sink depth `PROPOSAL`), and a blend ring that eases to the natural ground (width `PROPOSAL`; where the step is large, a ramp, steps or a garden terrace that fits the theme, N04 FS-T02). Every door meets a path at its threshold height (ED E-05; N04 FS-T03).
- Write the top cell of each column with fractional occupancy (the part of the 4-stud cell under the surface) so the surface morphs smoothly instead of stepping.
- Re-base the hill on the same ground datum; let its foot blend into the ground. If it is a one-off Blender piece, sink it on purpose and record the overlap as approved (PR-21; TW §2.3), then check the seam from eye height and both sides with collision visualization.
- Rebuild terrain from the corrected data in bounded regions, one region per `execute_luau` call, read back each region, never repeat after an uncertain result (EC §3 Studio edits; PI62).
- Retest: delta table again; player-eye captures round each building and the hill at low and high quality; walk every door (RV §6 "retest what the fix touches"; N04 FS-V07).

**(4) Will not change**
- The relief of the map: no flattening (owner: "we want a little bit of terrain in every stage", D-106; ED E-05).
- Building floor heights, door heights, building positions and route heights (route contract, PR-01). If a building sits on a slope where a blend ring cannot fit without cutting a route edge, that is a proposal to the game designer (HO §1), not a silent change.
- The lake position and the hill's shape.

**(5) Not verified**
- All checks above (planned). Whether fractional `WriteVoxels` occupancy gives the expected smooth surface at these heights (test in the test place first). Sink and blend values (`PROPOSAL`). The look in Studio and on phones; walk feel.

Cites: ED E-05; TW §1-§2; LF40, PI25; EC C-09, §3; N04 FS-P07, FS-T02, FS-T03, FS-T08, FS-V07; PR-01, PR-21; RV §6; LD §5.

---

## H2. Render shows grey trim and olive walls; model palette matches the concept

**(1) Most likely cause**
The model is right and the **picture pipeline** is wrong: the difference sits in the layer "camera, exposure or graphics tier", not in the material (LA §3; N03 CO07). Candidates in that layer: the preview tool's view transform or tonemapping (it can compress white to grey and desaturate), under-exposure, a tinted world or key light (a warm or green light turns pastel into olive), a colour-space mismatch (values converted twice, or entered in the wrong space), or the preview reading a different colour path than the one checked (vertex colour vs material colour, a texture or colour map multiplying the base colour). In Studio the same symptom can come from the stage look (ColorShift_Top, OutdoorAmbient tint, Atmosphere Color, ColorCorrection TintColor; LA2 §1).

**(2) Proof before editing any colour**
- **Calibration card in the same scene and tool:** a pure white swatch, a neutral mid-grey swatch and swatches with the exact palette values, rendered with the same tool settings and camera. Sample the pixels. White renders grey and the palette swatch renders olive = the tool shifts colour; the model is not the cause.
- Read the tool's colour settings (view transform, exposure, look), the light and world colours, and which colour attribute the renderer reads.
- **Studio is the final renderer** (BS §1 "Studio is the final renderer"; AC §3 "Studio decides the final look"): capture the building in the test place under a neutral look and under the stage look, low and high quality (AC §2). Matches the concept under neutral but not under the stage look = the stage look tints it.

**(3) Fix**
- Preview at fault: fix the render setup (neutral view transform, neutral light, correct exposure), write it down as the project's render recipe, re-render the review sheet beside the concept (RV §1 step 2; N04 FS-V02).
- Stage look at fault: that is a look decision. Record it in the look sheet and send it to the art director with captures (HO §2: classify the drift layer before a fix).

**(4) Will not change**
The model's palette values and the art-bible locks. No darker or lighter paint to compensate: "fixing the wrong layer breeds compensating errors" (LA §3, CO07).

**(5) Not verified**
The cause until the card test runs. How the concept image itself was lit (it may be idealised). Final look in Studio on phones. The owner's judgement of the colour.

Cites: LA §3 (CO07); LA2 §1; BS §1; AC §2-§3; RV §1; HO §2; N04 FS-V02.

---

## H3. Passes automatic checks and 0.97 outline; porch roof shows slats with gaps; thin blue lines under the main roof

**(1) Most likely causes**
- The outline score cannot see either problem: "a numeric match score is a floor, not the finish" (N04 FS-B05) and "a builder's 0 FAIL is not a look check" (RV §1; N04 FS-V05). A gap seen from above does not change a front or side outline.
- **Porch slats: probably a real defect** — the porch roof is separate pieces that do not touch or overlap, visible only from high views. It is not a defect only if the approved drawing shows a slatted shade on purpose.
- **Blue lines: probably sky showing through** — a gap between the wall top and the roof underside, or a roof or soffit with faces missing (a single-sided surface seen from below shows what is behind it). Less likely: editor adornments in the shot (selection box, light guides), or flicker from two surfaces in the same plane.

**(2) How I decide (real vs artifact)**
A real defect is in the geometry data and stays the same across cameras and quality levels; an artifact changes with the camera, the distance, the quality level or the editor state.
- Read the parts: positions and sizes of the porch-roof pieces and the gaps between neighbours; wall-top height against the roof underside along the eave. Gap > 0 in data = real.
- Check the approved drawing and concept: solid porch roof or slats?
- Re-shoot from the same spot with no selection or adornments, then a different distance and angle, at low and high quality (RV §3, AC §2). Add a contrasting background behind the eave: if the line takes the colour of what is behind it, it is a hole. If it shimmers and moves with the camera, it is two coplanar surfaces (still a defect, different fix).
- Look at the underside from player eye under the porch and the eave (the camera set is chosen by the stage's risks, RV §3).

**(3) Fix** (at the geometry layer, by its owner)
- If the building is a modeler asset: one exact note to the modeler (via the lead while the role is planned): camera id, measured gap, expected result (continuous roof that overlaps the wall top, closed soffit, finished on every face; ED E-06), check = renders front/back/sides/3/4/top beside the reference (HO §3).
- If I assembled it in Studio from kit pieces: close the gaps (overlap the slats or use one kit roof piece; seat the roof on the wall top), one bounded change per call, read back, capture (EC §3).
- Add high 3/4, top-down and under-eave cameras to this stage's camera list so the next round catches it.

**(4) Will not change**
The outline check, its threshold or the approved drawing; no material or transparency change to hide lines ("Never change a material or a test to pass a check", N04 FS-H04). No darker sky to hide gaps.

**(5) Not verified**
Which candidate is true until the part data is read and the re-shoots exist. Whether slats were intended. Phone rendering.

Cites: RV §1, §3; N04 FS-B05, FS-V05, FS-H04; ED E-06; HO §3; EC §3; AC §2.

---

## H4. Plaza "looks flat and I don't know where to look"; art director suggests more lights

**(1) Most likely cause**
No deliberate visual hierarchy, not too little light (N03 DF01). Every surface has similar value, saturation and detail, and the fill is even (for example Ambient close to OutdoorAmbient, a high sun, many equal lights), or the plaza has no focal point at all in its layout. More lights everywhere make the same problem worse: light must lead to one thing (LA-01, LA-03; LD L-03 "the brightest, most saturated thing in view is the goal").

**(2) Proof before any change**
- Blueprint: what must the player notice here and why? Read the cue sentence for this decision point (PR-04). No sentence written = first finding.
- Captures: player-eye approach, decision point, after committing, low and high quality (RV §3; PR-08). A greyscale copy of each shows the value hierarchy. Luminance and saturation of the target focal region against competing surfaces as a diagnostic only (N03 RV02).
- Read the look sheet (Ambient vs OutdoorAmbient, Brightness, ExposureCompensation, sun direction, local light count) and classify the layer: wrong large shape, right shape badly framed, wrong value hierarchy, material response, or camera / exposure / tier (LA §3).

**(3) Fix** (at the layer the check names)
- Value hierarchy: change the relationship at the focal region: lower the fill so the key light shapes forms, aim the sun (ClockTime, GeographicLatitude) at the focal point (LA2 §1.2; the cabin tutorial lit its only exit this way, LD82), quiet the competing surfaces and keep the walkable ground calm (PR-19), and if needed one light with a visible cause at the focal point (LA-04; EC C-06). Brighten with ExposureCompensation, not Brightness (EC C-04).
- No focal point: a bolder large form or a clearer line of sight, not a brighter small prop (DF01). A new landmark is a modeler asset; a sightline or layout change is a proposal to the game designer (HO §1, §3).
- Values go into the look sheet as `PROPOSAL` and get a look-lab test (EC C-14; LA2 §8). It must also read at low quality, where shadows go off below level 4 (EC C-13).
- To the art director: answer with the captures and the classification; adding lights everywhere is the known failure; propose the specific relationship change. Style limits are the art director's; a direction change is the owner's (ED §1).

**(4) Will not change**
The plaza layout and routes without the game designer; the art-bible palette; a global Brightness lift; post effects or haze as the main fix (LA-10, LA-12).

**(5) Not verified**
The owner's and players' read ("I know where to look") needs them. Phone result. All values.

Cites: N03 DF01, RV02; LA-01, LA-03, LA-04, LA-10, LA-12, LA §3; LD L-03; PR-04, PR-08, PR-19; LA2 §1, §8; EC C-04, C-06, C-13, C-14; RV §3; ED §1.

---

## H5. Market street: props on every free surface; "busy but empty of meaning"; testers bump into things

**(1) Most likely cause**
Dressing placed as a quota: every free surface treated as a place to put something (N03 DF02), with no story per cluster (PR-17; ED E-10) and no placement exclusions for route lanes, interaction approaches and camera corridors (PR-21). Bumping: props in the walk lanes, and/or collision shapes bigger than the visual.

**(2) Proof before any change**
- Top-down capture with the route graph's lanes and interaction points over it (RV §3; LD §3); per-zone counts from the scene audit (AC §1).
- For each cluster: the one-line story (who used it, why it is still there). Clusters without one are the cut list.
- Where testers bumped: play-test positions; walk those spots with collision visualization at player eye (BS §5 "never from the render mesh").
- Compare density with the concept and the art bible.

**(3) Fix**
- Write the street's reading first (stalls, deliveries, storage, who works here), then keep clusters that tell it at stalls and stopping points; remove low-value clusters, including roof clutter unless it has a reason (DF02; PR-17; PR-19 calm walkable ground; ED E-10 "detail where the player stops").
- Clear the route lanes, interaction approaches and camera corridors (PR-21).
- Break remaining repetition by composition: grouping, rotation, spacing (PR-20).
- Remaining props near lanes: collision that matches what the player sees, cheapest fidelity that plays right; props out of reach get CanCollide / CanTouch / CanQuery off (EC C-10).
- Retest walks along the same route (RV §6).

**(4) Will not change**
Street width, lane positions and timing (game designer, PR-01; any change goes as a proposal). The iconic set-list items. I will not turn collision off on props that stand in the lane: players would walk through solid barrels, and boundaries must act like the world (LD L-09). No request for more unique meshes.

**(5) Not verified**
Whether players now read meaning (play-test). Feel of the walk. Phone cost.

Cites: N03 DF02; PR-17, PR-19, PR-20, PR-21, PR-01; ED E-10; EC C-10; BS §5; AC §1; RV §3, §6; LD L-09.

---

## H6. Stage feels like a dollhouse: tiny doors, hovering props, an obvious repeated wall panel

**(1) Most likely cause**
Wrong scale from an unverified conversion or from assets made without the player reference (N03 DF03). "Nobody changed the export settings" does not clear the chain: the fault can sit in scene units, object transforms, the importer's Scale Unit or pivot options, a stacked .01 recipe (100× off), or the asset authored at real-world size, which next to a Roblox avatar reads as a miniature (owner: "it's almost like you're making a miniature on purpose", D-091; ED E-04; N04 FS-S01). Hovering props often follow from a pivot choice or a rescale about the wrong pivot. The repeated panel is a composition problem.

**(2) Order and proof** (scale first, because resizing changes contact and repetition)
1. **Scale source.** Measure a door's opening in studs (`GetExtentsSize`) against the scale sheet's player envelope and camera (PR-12, PR-14). Re-run the calibration round trip with today's files and importer settings (BS §3). Calibration object correct = the chain is fine; the cause is asset authoring scale or the scale convention itself. Calibration wrong = find the faulty layer in this order: scene units, object transforms, export conversion, importer scaling; never resize descendants first (BS §2, PI51).
2. **Contact.** After scale is settled: scene audit floating list with gaps (AC §1); read each hovering prop's pivot and support surface (PR-21).
3. **Repetition.** A moving camera along the street (a pan shows a repeat that a still hides, PR-20; N03 RC11).
4. **Terrain joins** round the changed pieces, from both sides (DF03).

**(3) Fix**
- Fix the source layer (the asset's scale in Blender, by the modeler for kit assets; or the importer setting), re-import each asset once and duplicate in Studio (EC C-10; BS §5).
- If the convention itself reads too small: propose a deliberate exaggeration to the owner, record which relations bend; gameplay openings stay tied to the route contract (PR-15; ED E-04). No universal door size: derive openings from the motion envelope (PR-14).
- Re-seat props from the audit; then vary composition (rotation, grouping, spacing, surroundings) before asking the modeler for new panel variants (PR-20; ED E-12).

**(4) Will not change**
No hand-resizing of single doors; no export-recipe change without evidence; no stacked recipes (EC C-01). Route openings and widths change only through the game designer. No invented door size.

**(5) Not verified**
The faulty layer until the round trip runs. Feel at the new scale (an owner call, as in D-091). Runtime instancing after re-import. Phone.

Cites: N03 DF03, RC11; ED E-04, E-12; N04 FS-S01; PR-12, PR-14, PR-15, PR-20, PR-21; BS §2, §3, §5; PI51; EC C-01, C-10; AC §1.

---

## H7. Forest, beach and cave "all sound the same"; a jump into the cave; waterfall heard where there is no water

**(1) Most likely causes**
- **Same everywhere:** no ambience map, or one global loop renamed per zone (N03 DF04; AB-03 "the same loop renamed per biome is a defect").
- **Jump at the cave:** the whole mix switches at one line (a box face) instead of blending (AB-09); or a streaming fault: a source on a streamable part stops and restarts (AB-10; EC C-11, AU27); or a duplicate starts on stream-in.
- **Waterfall with no water:** the source is not anchored at the visible cause. Candidates: it plays non-spatially (a bed in SoundService, or an AudioPlayer wired straight to the output with no emitter); it has an emitter with no attenuation curve, which means inverse-square with **no end distance**, so it carries far (AP §2; AU06); its anchor or parent is in the wrong place; a duplicate is left at an old position; or the sound and picture read different states (a state-coordination fault, AB-07; DF04).

**(2) Proof before any change**
- Does an ambience map exist? If yes, scene audit map vs place: missing ids, unlisted audio, duplicate ids, kind mismatch (AC §1; AP §1).
- Inspect each audio object: class, parent, position, wire graph (player → emitter → listener, or player → output), attenuation mode and curve, and whether forest, beach and cave use the same asset.
- Play-mode border walks with a log of the active sources per position: approach, cross, walk back, stand on the edge, teleport, respawn, stream out and in; count instances on leave → return → leave for duplicates (ambience.md §5; N03 RS02, RS04, RC09). One record per state.
- At the spots where the waterfall was heard: which source is audible, where it sits, and what state the falls show.
- Is the cave's acoustic choice recorded (authored reverb or acoustic simulation, never both by accident, AB-08)?

**(3) Fix** (my part, then briefs)
- Write or complete the ambience map: per zone the four jobs filled only where needed (AB-02), sources with visible causes (AB-01), each border's blend location (the cave-mouth corridor, not a box face) and edge cases (AB-09), a keep-or-rebuild rule per source (AB-10), fallback order (AB-12).
- Put zone volumes and anchors in the place with the exact conventions; waterfall sources at the visible impact and the outflow (AP §1, §4; ambience.md §4 falls row).
- Brief the sound designer (per-zone layers, ranges, curves, gains, crossfades: their numbers, from listening checkpoints), the VFX designer if motion is involved, and the code role for the blend runtime and the rebuild-once rule (AP §1 "the environment designer never writes it"); the code role is not built, so that brief goes to the lead (HO §4-§5).
- Report a duplicate or stream-in fault to the code owner as a bug with the state log.

**(4) Will not change**
Clips, gains, ranges, curves and crossfade times (sound designer). Runtime code. Not the whole map made persistent to fix one bug (AB-10). No invented fade times or ranges (ambience.md §3).

**(5) Not verified**
Listening: "auditory acceptance pending" until someone hears it (ambience.md §5; N03 RS07). Acoustic simulation on weak phones (AB-08). Undocumented streaming behaviour (whether a server-owned AudioPlayer resumes on stream-in, AP §3).

Cites: N03 DF04, RS02, RS04, RS07, RC09; AB-01-AB-03, AB-07-AB-10, AB-12; ambience.md §3-§5; AP §1-§4; AU06, AU27; EC C-11; AC §1; HO §4-§5.

---

## H8. Stage runs badly on a test phone; one wants to delete half the props, one wants ambience and effects off

**(1) Most likely cause**
Unknown until measured. The cost has not been traced to real resources and work; instance count alone cannot tell a cheap marker (zone volumes, attachments, anchors) from an expensive dynamic system (N03 DF05; performance skill F-07). The real pressure can be CPU (scripts, physics), GPU (overlapping transparent layers, shadowed lights, shadow casters), memory and textures, or streaming.

**(2) Proof before any change**
- Name the device and the target: the owner sets the frame-time target (ED E-14; RV §5); if none exists, it is `UNKNOWN` and the first question to the owner.
- Phone trace (studio operator, HO §6): MicroProfiler at the busiest overlap with gameplay on, at least 10-15 minutes of active play (PI34), Scene Analysis snapshot beside screenshots, memory by category, low and high quality (RV §5 steps 1-4; PF §4). Studio stats and emulators show relative changes only (PI31, PI33).
- Scene audit counts per zone to see which categories dominate (AC §1).
- Name the bottleneck before changing anything (F-07).

**(3) Fix**
- Reduce the **measured** bottleneck, one cost category at a time, same scene, same device, before → after (RV §5 step 5; performance skill §3.4-3.5). Examples by category: overdraw → fewer stacked transparent layers; shadows → CastShadow off on small parts, fewer shadowed lights; physics → anchor static parts, cheapest collision, Can* off on decoration; memory → import once for instancing, reuse textures; streaming → Properties settings and SLIM for static far scenery (PF §1-§2; EC C-10).
- If cuts are needed, ask the owner what to protect (N04 FS-P11: "cheaper furniture first, not removal").
- Ambience and effects degrade in the map's fallback order (optional one-shots and decoration first, navigation and gameplay cues last), per quality level, not switched off (AB-12).
- After each change, rerun the clarity and ambience checks it can touch (ambience.md §5; N03 RP02).

**(4) Will not change**
No blind deletion of half the props (instance count is not the cost; story, landmarks and route cues would go). No ambience or effects off to pass: "If a stage passes only with ambience or effects off, it has not passed" (RV §5; DF05). No invented budget; platform caps are not targets (EC C-12).

**(5) Not verified**
Everything until the trace exists. Other devices. Thermal behaviour over a full session.

Cites: N03 DF05, RP02; ED E-14; RV §5; PF §1-§4; PI31, PI33, PI34; EC C-10, C-12; AB-12; HO §6; N04 FS-P11; performance skill F-07.

---

## Where the skills were unclear, missing or contradictory for these cases

| Case | Gap | Suggested fix (proposal) |
| --- | --- | --- |
| all | The defect-to-cause table (N03 DF01-DF05) lives only in a reference note. `review.md` §6 has a cause-first rule and only one worked diagnosis (players miss the route). Five of eight cases needed the note, not the skill. | Add a "symptom → likely cause → proof → repair" table to `review.md` §6 with DF01-DF05 and the H1-H3 cases. |
| H1 | `terrain-and-water.md` has nothing on ground-to-building joins: pads, a floor-vs-ground check, blend rings, fractional occupancy when writing heights, a shared height datum for terrain and placed landforms. FS-T08 covers only water vs floors. The scene audit "buried" check does not compare ground to floor heights. | Add a TW §2 row (pad + blend + fractional top cell + one datum) and a ground-vs-floor item to the FS-P07 plan checks. |
| H2 | No row on render colour management for preview or Blender renders (view transform, exposure, light tint, colour space) and no calibration-swatch step. `audit-and-capture.md` §3 says renders prove look, without the warning that render settings change colour. `LA §3` (classify the layer) was the only lead. | Add a "render calibration card" step to AC §3 and BS §3. |
| H3 | No rule tells a render artifact (adornments, coplanar flicker, missing faces seen from below) from a geometry gap. The scene audit has no gap/seam check between pieces. The outline-score warning (FS-B05) is in a note, not in the skill core. No under-eave or top-down-of-structure camera in the camera set by default. | Add an "artifact or defect?" row to RV §2 and a high-view / under-eave camera to RV §3. |
| H4 | Role tension: `light-and-air.md` sends look conflicts to the art director, but the environment designer owns lighting. Nothing says what to do when the art director proposes a technique ("more lights") rather than a look target. | State: the art director sets the target and limits; the environment designer picks the technique and answers with captures. |
| H5 | EC C-10 (Can* off where nothing touches) and LD L-09 (boundaries act like the world) pull in opposite directions for props in walk lanes; no row says "clear the lane, do not turn collision off". | Add that line to PR-21. |
| H6 | DF03 lists four repairs but no order; I inferred scale → contact → repetition → joins. ED E-04 "1 stud = 28 cm" next to "real size felt like miniatures" can read as a contradiction; PR-11 resolves it only if read. Who decides a scale exaggeration is implied (owner, D-091), not stated. | Order the DF03 steps in RV §6; add "exaggeration is an owner decision" to PR-15. |
| H7 | AP §3 lists a non-spatial bed in SoundService as a streaming-safe home without warning that a point source (a waterfall) put there is heard everywhere. The design consequence of "no curve = no end distance" is in the craft facts only, not in `ambience.md`. The code role that owns the blend runtime, and the modeler, art director and studio operator roles, are not built (`.agents/roles/`), so every brief in these answers goes through the lead. | Add both warnings to AB-10 / AP §3; name the interim owner of the zone runtime. |
| H8 | Covered well (RV §5, DF05, F-07). The owner's "what to protect" rule (FS-P11) is not in either skill's rules. `performance.md` (craft) does not map audit counts to cost categories. | Add FS-P11 to ED §5 rules. |

Not done (outside this brief's `owns`): the lesson draft in `knowledge/inbox/` and agent-memory notes. The hand-back carries the lesson content.
