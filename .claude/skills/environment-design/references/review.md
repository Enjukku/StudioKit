> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit reference: universal. J008. Sources: environment paper notes `knowledge/reference/environment/03-pipeline-performance-review.md` (§4, §7: RA, RC, RS, MP, RJ, RV; §3 PF, BT) and `01-place-guidance-scale-light.md` (EC10, RU14-RU15, G05-G07, K04-c); first-game lessons `04-first-game-stages.md` (FS-V, FS-B05, FS-H). Packet format: `templates/environment/review-packet.md`. Tags: **V** VERIFIED, **E** EXPERIENCE, **O** OPINION, **U** UNKNOWN; **FS** = first-game practice with owner evidence. Revised by J018 maker environment-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (grey value pass in the order, key views and image budget in §3, the self-review checklist in §7). Revised by orchestrator · claude-opus-5-5 · high · 2026-10-23 (J021): RD1.

# Review: proving the place works before anyone sees it

## 1. Order of review (owner practice)
1. **Read plan and blueprint**, the blueprint approved by the owner before building (FS-P01).
2. **Greybox walk and grey value pass**: walked at walk speed; key light direction chosen in grey; first view and decision views measured; dead space marked. Most layout problems are cheapest here.
3. **Renders** next to the reference images at the same angle, on one labelled sheet, before Studio (FS-V01, FS-V02). Blender renders for Blender-built parts; Studio captures for Studio-built parts.
4. **Studio placement and the self-review** (§7) on the key views after each build pass; the full camera set once for the release candidate; then the review packet, then the owner (FS-V03; RU15 O).
A builder's "0 FAIL" is not a look check: a second look comparing the build with the concept found real failures the validators passed (FS-V05). Look yourself.

## 2. What a check can prove
| Evidence | Can show | Cannot show |
| --- | --- | --- |
| Screenshot from a named camera | composition, contact, facing, finish, scale against the player, repetition | whether a route feels comfortable; how anything sounds; timing (EC10 O) |
| `look_check.py` numbers on a capture (`environment-craft/references/measure-captures.md`) | luminance spread and ranking of named boxes, separation ratios, reserved-hue pixel share, chroma and flat-fill spread in named boxes, a phone-size version | taste; whether a player notices it; anything outside the boxes you named; any setting the capture did not use |
| Scene audit (structure) | floating and buried parts, counts per zone, map ids vs place ids | whether an overlap was intended; whether players notice a landmark (RV02 O) |
| Place listing through `execute_luau` | sizes, materials, positions, collision parts | how they look from the camera |
| Audio structure (positions, wires, curves) | that a source exists where planned and is connected | tone, masking, loop joins, harshness, smoothness (RS07 O; AX07 O) |
| Editor or emulator numbers | relative changes on this machine | phone frame time, memory, thermal behavior (PF10 V; DN09 O) |
| Phone trace on the declared device, busiest overlap, gameplay on | the budget verdict | other devices |
| The studio operator's play capture, the game designer's or art director's check-in | moving play, the HUD, a cold read of what a place is | anything they did not capture or say |

Pass / fail only against an approved contract or a measured project limit; otherwise `UNVERIFIED` (RA03 O; ES18 O). Never describe a planned check as done (DN10 O). Every number names its capture, quality level, camera and viewport.

## 3. The camera set and the image budget
Pick cameras by the stage's risks, not by a fixed count (RA02 O). Record position, target and FOV so anyone can repeat the shot (RA01 O).
| Kind | Why |
| --- | --- |
| first frame after spawn at the default camera | the first view tells where you are and what to do |
| player-eye approach, decision point, after commit, return trip | route guidance (G05 O) |
| reverse route | the place must read both ways (K04-c O; K08-c O) |
| busiest moment (studio operator's play capture: players, typical effects, HUD, phone viewport) | the gameplay read where it is hardest |
| smallest gameplay object on each floor type | clean floors |
| high 3/4 and front / sides / back of each structure | finish on every face; facing; silhouette against the reference (FS-V03; FS-B01) |
| top-down of the whole stage | layout, path network, zones, dead space |
| scale shot with the player figure per area | real scale (FS-S01; SC07 O) |
| contact close-ups, low oblique and under-roof views | floating, buried, intersections, missing faces between stepped layers (SD07 O; `diagnosis.md`) |
| skyline and far landmark | silhouette at distance, streaming and level of detail (K04-b O; RJ02 O) |
| stress scene | the busiest overlap of effects, sources and players (MP01 O) |
**Key views** = the first view, the busiest moment, one decision view per zone, the top-down, and one view per hazard. **Image budget** (owner light-check rule): every §7 line is answered with numbers on every pass; images you look at are the key views (one graphics setting per routine pass, both settings for the grey pass and the release candidate) plus an image only where a number fails; the full camera set once, at the lowest and the highest setting, for the release candidate. Report how many captures you took and looked at.
Capture at the lowest and highest graphics quality; keep what drops at low quality visible, never hidden by a beauty angle (MP02 O). Move the camera or character into the content first: the client may draw only content near the character (FS-V09). Restore the owner's edit camera afterwards (FS-V03).

## 4. The checks
Every check is a line of §7 with its input; the packet's look and ambience tables are filled from them. Re-review after fixes re-rates every line, not only the failed ones, so rounds compare (no point totals); a fix job runs the fix-job lines of §7.
Budget: counts per zone from the audit; frame time and memory from a phone trace (RC13 O). Hand-off completeness: revisions, asset references, settings, exceptions, owners recorded (RC15 O).

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
- **Contrast before detail.** When something does not read, find the missing contrast (value, hue, saturation, size, shape, position, motion) and change one; lower the surroundings before raising the subject. Adding detail is not a fix for a weak read.
- **One named problem per pass, the worst first.** Name it, fix it, re-measure, then the next.
- **Order:** gameplay failures, wrong source behavior, performance failures and big style drift before cosmetic polish; record the reason if the order changes (RV05 O).
- **One record per issue:** id, severity, scene and state, camera or source, what was observed (fact, apart from guesses), intended reading, likely cause and its layer, proposed change, what must be kept, responsible craft, retest evidence, owner decision if needed (RV04 O; CO08 O). A note that names a fix: restate the problem behind it, then choose the fix; a visual note is settled on a paint-over of the capture before the 3D change.
- **Retest what the fix touches,** by dependency, not by file type: moving a rock can change sightlines, collision and audio occlusion; a "cosmetic" light edit can hide the route (W12 O; ST13 O). Before and after from the same camera, settings and seed.
- **Other symptoms** (flat, cluttered, busy backdrop, lost pickups, dead or generic place, wrong scale, same-sounding zones, too costly, stepped ground, wrong render colours, gaps the checks missed): `diagnosis.md`.
- **Players miss the route?** Find the cause before adding arrows: cue off-camera, hidden, too close to background shapes, contradicted by another cue, shown too late, or read as inaccessible. Fix at the least disruptive layer; if the fix changes route length, cover or timing, it goes to the game designer (G09 O).
- **Rebuild, do not patch.** A section that keeps failing after two fixes is rebuilt from the greybox; attachment to an early version is not a reason to keep it.
- **Breadth first, polish later.** Finish the whole stage before polish rounds; keep a dated polish list and the 3 weakest points (FS-H05). Plan at least one polish round: first builds come out plain (FS-B04).

## 7. Self-review checklist (run before every hand-back)
Each line names its input. "Numbers" = the command in `environment-craft/references/measure-captures.md` named in brackets (M1-M12). "Capture" = a Studio MCP capture at the game camera. Starting values marked `PROPOSAL` come from the art bible once it has them. A line you cannot run is listed `not verified` with the input that would close it. Separation targets for characters and markers: `light-and-air.md` VB-a (the ratio is symmetric and 1.0 means no separation: `measure-captures.md` §0).
**Fix job** (a small change or fix): run the lines the change touches by dependency (§6) plus RD2, RD3, VB1, FL1 and QV3; mark the others `n/a (fix job)`.

**Read and route (RD)**
- RD1 The read plan exists, is dated before the first image, quotes the target-experience line, and every field has a source or `PROPOSAL`. Input: the file.
- RD2 First view: the goal or main landmark is in the first frame after spawn and wins the focus: its own contrast (its box alone against its ring, the competitors and the HUD excluded) reaches the marker target, and it is first among the goal and its 2-3 competitors by median or by own contrast; the p5-p95 spread is support only (a box edge on the sky fakes it). This focus rule is the one VB3, RD12 and the light-direction pass use. The game's orientation conventions hold from the spawn view. Input: 1 capture + numbers (M1: the shared run and one own-contrast run per subject).
- RD3 Busiest moment: every critical fact of the read plan is found in the studio operator's play capture (list each fact and where it is); two characters in typical avatar colours (one light, one dark) reach the character target against their ring. Input: the partner's capture + numbers (M6).
- RD4 Each decision node: the decision view shows the cue named in the blueprint §F; approach and after-commit views only for key nodes and failing ones; the reverse route where backtracking exists. Input: 1 capture per node.
- RD5 Markers: from each spawn route an objective marker is visible before entry; the objective's floor border still reads at phone size. Input: 1 approach capture per objective + numbers (M5).
- RD6 Every interactive type uses its one treatment in the place; the game designer names what each place is and what can be done there at the art check-in. Input: numbers (M8) + partner.
- RD7 Every boundary has its "why is this here?" line; collision matches the visible shape. Input: list + numbers (M8); a collision-view capture only where they differ.
- RD8 Each hazard shows its source and containment; its drawn edge sits on the hazard volume. Input: 1 capture per hazard + numbers (M8).
- RD9 Collision, openings, cover and sight-line blockers match the approved greybox within one snap step, or each difference has the game designer's sign-off. Input: numbers (M8).
- RD10 Each route-table segment shows something to see or do within its limit; vistas and reward views open at the planned pauses and achievements. Input: the game designer's route table + a list; captures at reveals only.
- RD11 Dead space and oversized areas are marked on the top-down and each is cut, shrunk or given a purpose. Input: 1 top-down capture.
- RD12 Each planned surprise is not the region that wins the focus of its view (the RD2 rule); each hidden secret sits off routes and decision points. Input: numbers (M1) + the secrets list against the route graph.
- RD13 The landmark is the tallest shape of its zone, visible from each fork, with a silhouette unlike the other landmarks; main lines on the grey first view lead to it or to the next route. Input: numbers (M8) + fork captures (key forks only: a subset of the level review's fork set, every fork in each approach direction, `level-design/references/review-artifact.md` C4, which the level review covers) + the grey image (M1).

**Value, light and colour (VB)**
- VB1 Environment band: environment-only boxes (ground, walls, props; no sky, characters, effects, UI) in each key view sit inside the environment band (p5 and p95; `light-and-air.md` VB-a); near-black share about zero. Input: numbers (M1, M2).
- VB2 Layer order: each character reaches the character target against its environment ring, the lower body boxed apart against the ground; no environment region has a wider spread than the characters and effects in the same view. Input: numbers (M6, M1).
- VB3 Focus: the focal region of each key view wins the focus among the named regions by the RD2 rule; the grey image of the first view checked. Input: numbers (M1) + 1 grey image.
- VB4 Reserved colours: in the environment boxes, gameplay objects excluded, the pixel share within the reserved distance of each reserved hue (authored and as rendered; the distance is the reserved-colours row of `art-review/references/art-bible.md` §7) is near zero (the art bible's allowed share). Input: numbers (M3).
- VB5 Player band: mean chroma from the floor to the measured eye height is below the band above it, or under the neutral limit (starting `PROPOSAL` 20) when both bands are neutral; under a coloured look (dusk, warm or cool interior, night) the chroma is measured white-balanced to a grey block under the same light (M3 `grey`), so the light's tint is not counted. Input: numbers (M4).
- VB6 Saturated colour sits on the focal elements and the read plan's eye-path accents: with those boxed into `exclude` (a second M3 run; gameplay objects stay excluded), `share_chroma_above` in the environment boxes (white-balanced to a grey block under a coloured look, M3 `grey`) is at most the stray limit (starting `PROPOSAL` 0.02); the dominant theme hue covers most of the scene (judged on the key-view image). Input: numbers (M3) + key views.
- VB7 Depth and intensity: the far band (landmark excluded) has a narrower spread than the near band; climax areas wider than hubs; with the final Atmosphere on, each route cue, edge and hazard still reaches its separation target in its decision view (a far cue at its farthest decision view). Input: numbers (M1, M6; M5 for small cues).
- VB8 Key light: one direction per place, chosen in the grey pass (`light-and-air.md` LA-15) with its variants' numbers in the look sheet; the lit and shadow sides of one material sit on opposite temperature sides as the art bible sets; every local light has a visible source (a threatening place may be lit from below by its own source); a dummy's shadow side carries a hint of the ground's hue. Input: look sheet + numbers (M11) + the light list.
- VB9 Key positions: a dummy standing at each key position reaches the character target against its background at the lowest and highest setting. Input: numbers (M6); images only where it fails.
- VB10 Without extras: each key view re-taken with bloom, colour correction, sun rays and Highlights off (one folder toggle each), and at the lowest setting, still passes RD2, RD5, VB3 and FL1. Input: captures of the key views + numbers.
- VB11 Material zoo: every material block inside the band, inside the art bible's saturation band for environment materials when the bible sets one (`mean_chroma` of the block's lit face, M3 with `grey` set to the zoo's grey block), and free of reserved hues under the stage light (the reserved hues as rendered by their reference blocks); on the blocks' lit faces no palette cluster lies farther than the palette distance from every palette role of the art bible as rendered under the same light by its reference block, never the authored hex (starting `PROPOSAL` CIEDE2000 15; the art director's number replaces it), on the capture of each look and on the neutral-light capture. Input: 1 zoo capture per look + 1 under a neutral light + numbers (M1, M3, M12).
- VB12 No large surface is one flat colour or one hue: on its lit side, in a capture with Atmosphere and fog off (haze toward a far end reads as hue variation), `look_check.py hue-spread` `hue_sd_deg` is above the flat limit (starting 3°, PROPOSAL; `measure-captures.md` §3 Flat fill; `valid` false on a near-neutral material: judge by eye); under it the surface is one hue: `monochrome` when the script's `value_spread` is above its limit (a built-in material's texture under one part Color), `flat` when both are under; both fail; record both numbers; the variation stays in one colour family (judged on the key-view image); gold and warm metal keep at least half their lit-side chroma in shadow (starting `PROPOSAL`). Input: numbers (M3, M11) + key views.
- VB13 Hazards read by rim and shape in the grey view; a dummy in front of a bright hazard still reaches the character target. Input: numbers (M1, M6).

**Floors, detail, story and scale (FL)**
- FL1 The smallest gameplay object on each floor type, at the smallest phone viewport: value ratio at least the marker target (`light-and-air.md` VB-a; lower only with a shape or outline cue the game designer confirms), hue distance recorded. Input: 1 capture per floor type + numbers (M5); images only where it fails.
- FL2 Detail clusters sit on the read plan's detail spots with quiet areas between; the player band is calmer than above it. Input: 1 phone-size sheet per key view (M10).
- FL3 No kit piece shows twice at the same angle in a key view; repeats vary in rotation, scale and grouping; a facade repeated along a route is judged on 3-4 captures along the camera path players use, where a repeating window beat or highlight shows that a still hides. Input: numbers (M8) + key views + 3-4 path captures per repeated facade.
- FL4 Sibling pieces in each cluster differ by more than about 15 % in their largest size (starting `PROPOSAL`). Input: numbers (M8).
- FL5 Each story fact has its listed carriers in the place; every main area holds one story cluster; the art director or owner names a story fact at the check-in. Input: list + partner.
- FL6 Grounding: audit 0 floating; hero props have a base, no straight clean seam and a contact shadow. Input: numbers (M7) + contact captures of hero props.
- FL7 Scale: a dummy in every space; doors, stairs, rails and seats measured against the character; a known-size object near each focal structure; exaggerations listed in the scale sheet; the default camera passes every tight route opening and low ceiling without clipping or being pushed in toward the character. Input: numbers (M8) + 1 scale shot per area + 1 play-mode capture per tight opening as the character passes it (Studio MCP play mode and character navigation, or the studio operator's walk capture).
- FL8 Theme and style: 2-3 theme cues per area present; a stage capture beside 2-3 art-bible anchors reads as the same game, and beside earlier stages reads as somewhere new; the art director names the theme at the check-in. Input: list + 1 capture pair + partner.
- FL9 Every walkable material in the place has an entry in the sound designer's footstep table; decorative floor material stays small. Input: numbers (M8).
- FL10 Every visible face and enterable room finished; directional pieces face right; stepped layers have their risers. Input: the camera set (release candidate).
- FL11 Height and layers in every area; ground materials follow the recorded slope and height rule; every height change in a play space is on the game designer's intentional list; ground steps measured round structures and along routes (`environment-craft/references/terrain-and-water.md` §3-§4). Input: numbers + the list.
- FL12 Each key place beside its approved reference image from the same angle: the iconic qualities listed for it are present and at least as strong, each gap the image left open is decided and recorded; every kit piece was accepted on its in-set capture. Input: 1 capture pair per key place + the hand-off record.
- FL13 One-off Blender pieces (cliffs, cave shells, landforms) pass the `modeling-design` review lines that apply to them (form and planes, grounding, texel density, trim sheet, separate named parts); results in the stage record. Input: those lines run on my renders and audit.

**Motion and ambience (AM)**
- AM1 Nothing fast or bright moves near a sight line or the route: list of moving things with their distance to the nearest one. Input: numbers; captures only where a distance fails.
- AM2 Ambience map vs place clean in the scene audit (names and folders by the conventions); every zone has its emotion and the stage its signature element; borders and streaming states recorded; listening "pending" until a listener has listened (`ambience.md` §5). Input: numbers (M7) + records.
- AM3 Every intense ambient channel has an off path in its spec; large-area flashes at most 3 per second. Input: the spec.

**Quality, viewing and budget (QV)**
- QV1 Every RD, VB and FL number holds at the lowest and the highest setting; the high setting is not busier in the player band. Input: key-view captures at both settings + numbers (M4, M9).
- QV2 At the smallest phone viewport the focal region and the next cue still rank first in each key view. Input: numbers (M10, M1).
- QV3 Scene audit: 0 floating, 0 buried, 0 out of bounds or each explained; counts per zone; budgets with sources or `UNKNOWN`; phone trace from the studio operator or `UNKNOWN`. Input: numbers (M7).
- QV4 The first view looked at mirrored and in grey; anything lopsided only in the mirror is fixed. Input: 1 image pair (M10).

**Process (PS)**
- PS1 Option round: 3 distinct directions, one unexpected, the warm-up labelled, the pick with its reason, each rejection recorded, inside the image budget. Input: the option sheet.
- PS2 Gates: blueprint approved before building; greybox built in the order of `environment-craft` §3 step 3 and walked; grey pass before dressing; light pass dated after the last route change; nothing approved moved without a decision; no other role wrote in my place containers without a logged hand-over. Input: the job record.
- PS3 Each build pass covered every area before the next; no area more finished than its equals in the key views; the top items of the ranked work list are visible and finished in the key views. Input: key views per pass.
- PS4 Every note maps to a visible fix with before and after from the same camera and settings, its layer named, the protected items unchanged. Input: the note record + captures.
- PS5 Close: stop criteria met or not (with reasons); passes and images used against the budget; reused and new assets named; ideas that came after a gate listed as follow-ups with their cost; 3 weakest points; could-not-check list (step, missing input, what would close it). Input: the hand-back.
