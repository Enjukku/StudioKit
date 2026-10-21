> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit reference: universal. J008. Sources: environment paper notes `knowledge/reference/environment/03-pipeline-performance-review.md` (§4, §7: RA, RC, RS, MP, RJ, RV; §3 PF, BT) and `01-place-guidance-scale-light.md` (EC10, RU14-RU15, G05-G07, K04-c); first-game lessons `04-first-game-stages.md` (FS-V, FS-B05, FS-H). Packet format: `templates/environment/review-packet.md`. Tags: **V** VERIFIED, **E** EXPERIENCE, **O** OPINION, **U** UNKNOWN; **FS** = first-game practice with owner evidence.

# Review: proving the place works before anyone sees it

## 1. Order of review (owner practice)
1. **Blueprint**, approved by the owner before building (FS-P01).
2. **Renders** next to the reference images at the same angle, on one labelled sheet, before Studio (FS-V01, FS-V02). Blender renders for Blender-built parts; Studio captures for Studio-built parts.
3. **Studio placement and the full multi-angle review** in the test place, then the review packet, then the owner (FS-V03; RU15 O).
A builder's "0 FAIL" is not a look check: a second look comparing the build with the concept found real failures the validators passed (FS-V05). Look yourself.

## 2. What a check can prove
| Evidence | Can show | Cannot show |
| --- | --- | --- |
| Screenshot from a named camera | composition, contact, facing, finish, scale against the player, repetition | whether a route feels comfortable; how anything sounds (EC10 O) |
| Scene audit (structure) | floating and buried parts, counts per zone, map ids vs place ids | whether an overlap was intended; whether players notice a landmark (RV02 O) |
| Audio structure (positions, wires, curves) | that a source exists where planned and is connected | tone, masking, loop joins, harshness, smoothness (RS07 O; AX07 O) |
| Editor or emulator numbers | relative changes on this machine | phone frame time, memory, thermal behavior (PF10 V; DN09 O) |
| Phone trace on the declared device, busiest overlap, gameplay on | the budget verdict | other devices |

Pass / fail only against an approved contract or a measured project limit; otherwise `UNVERIFIED` (RA03 O; ES18 O). Never describe a planned check as done (DN10 O).

## 3. The camera set
Pick cameras by the stage's risks, not by a fixed count (RA02 O). Record position, target and FOV so anyone can repeat the shot (RA01 O).
| Kind | Why |
| --- | --- |
| player-eye approach, decision point, after commit, return trip | route guidance (G05 O) |
| reverse route | the place must read both ways (K04-c O; K08-c O) |
| high 3/4 and front / sides / back of each structure | finish on every face; facing; silhouette against the reference (FS-V03; FS-B01) |
| top-down of the whole stage | layout, path network, zones |
| scale shot with the player figure per area | real scale (FS-S01; SC07 O) |
| contact close-ups, low oblique and under-roof views | floating, buried, intersections, missing faces between stepped layers (SD07 O; `diagnosis.md`) |
| skyline and far landmark | silhouette at distance, streaming and level of detail (K04-b O; RJ02 O) |
| stress scene | the busiest overlap of effects, sources and players (MP01 O) |
Capture each at low and high graphics quality; keep what drops at low quality visible, never hidden by a beauty angle (MP02 O). Move the camera or character into the content first: the client may draw only content near the character (FS-V09). Restore the owner's edit camera afterwards (FS-V03).

## 4. The checks
Look: route guidance, focal hierarchy, scale and passage, camera clearance, lighting readability, atmosphere, contact, finish on every face and room, repetition while moving, cohesion with the art bible, iconic traits at play distance (RC01-RC12 O; FS-B01-B03, FS-S09).
Ambience: map vs place, visible cause per source, border behavior in every state, streaming leave → return → leave, sound-picture agreement, listening review (RC07-RC09 O; RS01-RS07 O; `ambience.md` §5).
Budget: counts per zone from the audit; frame time and memory from a phone trace (RC13 O).
Hand-off completeness: revisions, asset references, settings, exceptions, owners recorded (RC15 O).

## 5. Budgets are measured, not invented
No source gives phone budgets for stage triangles, draw calls, parts, lights, shadow casters, texture memory, ambient sources or animated props (BT01, BT06-BT08 U; KC0 O). Platform caps are not targets: a single mesh may hold at most 20,000 triangles; a particle emitter's rate is capped (100/s on mobile); these say nothing about a whole stage (BT02 V; BT05 V). The owner sets the frame-time target (BT09 O).
How a project budget is made (MP01-MP06 O; PF09-PF10 V):
1. Freeze a representative route, cameras, player load, weather and time, gameplay load and build id: spawn, the densest view, close effects, indoor-outdoor moves, skyline, repeated return trips.
2. Capture low and high quality pairs and the phone's Automatic mode.
3. Collect Scene Analysis snapshots beside the screenshots, and MicroProfiler traces and memory from the real low-end phone; find the real pressure (CPU, GPU, physics, textures, streaming) before cutting detail.
4. Play long enough to see heat slow-downs: Roblox advises at least 10-15 minutes of active play on mobile; extend to the real session length.
5. Change one cost category at a time and compare traces and silhouettes; record the accepted maximum with device, build and workload as the project budget.
6. Revisit earlier zones: counts of effects, sounds and instances must return to their expected state.
Reject the stage when a route or hazard disappears, a landmark misleads after streaming or level of detail, collision blocks an approved opening, ambience fails after re-entry, or the chosen device target fails (RJ01-RJ05 O). If a stage passes only with ambience or effects off, it has not passed.

## 6. Fixing what the review found
- **Cause first, every cause.** Before choosing a repair, list every mechanism the data could show (a symptom often has several: floors set apart from the ground **and** decorative noise; missing faces **and** an authored opening that looks like a gap), measure each one separately, and say which share of the symptom each explains. One generic repair for a many-part cause leaves the rest broken (J008 hidden test).
- **Order:** gameplay failures, wrong source behavior, performance failures and big style drift before cosmetic polish; record the reason if the order changes (RV05 O).
- **One record per issue:** id, severity, scene and state, camera or source, what was observed (fact, apart from guesses), intended reading, likely cause, proposed change, what must be kept, responsible craft, retest evidence, owner decision if needed (RV04 O; CO08 O).
- **Retest what the fix touches,** by dependency, not by file type: moving a rock can change sightlines, collision and audio occlusion; a "cosmetic" light edit can hide the route (W12 O; ST13 O).
- **Other symptoms** (flat, cluttered, wrong scale, same-sounding zones, too costly, stepped ground, wrong render colours, gaps the checks missed): `diagnosis.md`.
- **Players miss the route?** Find the cause before adding arrows: cue off-camera, hidden, too close to background shapes, contradicted by another cue, shown too late, or read as inaccessible. Fix at the least disruptive layer; if the fix changes route length, cover or timing, it goes to the game designer (G09 O).
- **Breadth first, polish later.** Finish the whole stage before polish rounds; keep a dated polish list and the 3 weakest points (FS-H05). Plan at least one polish round: first builds come out plain (FS-B04).
