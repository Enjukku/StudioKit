---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer character-rigger · claude-opus-5-5 · high · 2026-10-22

# J018 stage 3 review: character-rigger books, round 1

Scope: `.agents/roles/character-rigger.md` (body), `.agents/skills/rigging-design/**`, `.agents/skills/rigging-craft/**` (not `evals/`), `.agents/skills/rig-pipeline/**`, working tree on 2026-10-22, against `df13ff4`. I read the 15 book files in full and the diff of each before I opened `coverage/character-rigger.md` and `proposals/character-rigger.md`. Then I read the matrix (63 IDs tagged for the rigger), the 63 findings, `universal-principles.md`, the stage 2 brief v2 and `tool-modes.md`, and the partner books (animation-design §3, animation-craft §3, blender-keying §7, modeling-craft `rig-parts.md`, modeling-design `review.md` §5).

I ran the measuring lines on synthetic inputs with Blender 5.1.2 headless (`blender -b --factory-startup --python rigrev_tests.py`) and with `look_check.py` on synthetic PNGs. All files are in the reviewer's scratchpad with `rigrev` names. I changed nothing in the repo except this file.

```text
<spec>
artifact: .agents/roles/character-rigger.md (body) + .agents/skills/rigging-design/** + .agents/skills/rigging-craft/** (not evals) + .agents/skills/rig-pipeline/** @ working tree 2026-10-22 (J018 stage 2, wave 2)
reviewer: J018 reviewer character-rigger (opus, high), round 1
looked_at_first: [the 15 book files in full; git diff df13ff4 of each; role frontmatter compared byte for byte with df13ff4 (identical); rigging-design SKILL.md offsets of §7, §8 and §9; tools/rig/rig_audit.py, tools/rig/roblox_fbx.py, tools/anim/clip_check.py source (check_rom, _channel_value, sample_clip), tools/art/look_check.py silhouette --help and components() (COMPONENT_MIN_FRAC 0.005); docs mirror: characters/index.md:87-95, _api-reference/classes/Pose.yaml, Bone.yaml, animation/curve-editor.md:26-41, art/characters/facial-animation/animate-heads.md:21, art/characters/creating/modeling-best-practices.md; .agents/workflows/jobs/job-character.js S2-plan and P3-proxy-pose calls; rigging-craft/evals/briefs.md; synthetic runs: recipe 1 on a bone-parented head and on the same head weighted 100 % to its bone (rest and a 70 degree tilt, back/game/front cameras); clip_check sample_clip + run_all on a quaternion Hips bone keyed to a 30 degree tilt against a -15..15 degree manifest range; rig_audit.audit_scene with and without an Action that keys the swept bone; recipe 4 on a visual-key bake; look_check.py silhouette on 1170x540 magenta black-fills with a 127 px figure and with a 380 px figure, head lifted off in each]
findings:
  - id: F1
    class: blocking
    check: C8 V3
    where: "rigging-craft/references/blender-mcp.md:53-65 (recipe 1, cap exposure); used by tests.md:20 (Cap exposure row), :70 G-03, :81 R-03; rigging-design/SKILL.md:124 P-11; rigging-design/references/design-for-motion.md:51"
    expected: "Recipe 1 counts the visible cap points on the posed geometry for every part the book applies it to: the S2 and S4 proxy, whose parts are '100% on their bone' (tests.md:32, rigging-craft SKILL.md:28), and the real rig, whose rigid parts are 'one bone at 1.0' (rigging-craft SKILL.md:31)."
    observed: "cap_points(me, poly) builds the sample points from me.vertices, and the recipe does not say which mesh `me` is. Read as written (me = ob.data), a part moved by an Armature modifier gives its rest positions. The ray goes to where the cap was at rest, the hit is not on the cap face, and the count is 0 at every pose, with no error. The note under the code mentions only the face index of a skinned part. The maker's run d-04 used a bone-parented head, so this case was not run."
    evidence: "rigrev_tests.py, same head and cap, 5x5 grid, 70 degree tilt: bone-parented: back 10, game 10, front 0 (ob.data and evaluated agree). Weighted 100 % to the Head bone with an Armature modifier: me = ob.data gives back 0, game 0, front 0 (false pass); me = the evaluated mesh (ob.evaluated_get(dg).to_mesh()) gives back 10, game 10, front 0 (right)."
    smallest_fix: "In recipe 1, take the points and the polygons from the evaluated mesh: `ev = ob.evaluated_get(dg); me = ev.to_mesh()` ... `ev.to_mesh_clear()`, and say why: 'ob.data holds the rest positions, so a weighted or skinned part reads 0 at every pose.' Add one row to diagnosis.md §2 for this cause, next to the existing 'Cap exposure reads 0' row."
  - id: F2
    class: blocking
    check: C8 V3
    where: "rigging-craft/references/controls-export-import.md:22 (quaternion for root, hips and spin-heavy controls) and :30 (manifest fields for clip_check rom); rigging-craft/references/blender-mcp.md:101; tests.md:83 R-05 (rom for the clavicle and hip controls), :86 R-08; design-for-motion.md:32"
    expected: "R-05 fails when the wind-up clip moves the hips past the manifest range. The manifest min and max come from the §B ROM in degrees (controls-export-import.md §3 'min/max (from §B ROM)'), and the books put the hips in quaternion mode."
    observed: "For a quaternion bone the books say to name the channel by index (`rotation_quaternion.1`). clip_check._channel_value then returns the raw quaternion component (about -1 to 1). It converts to degrees only for `rotation_euler`. So a degree range on a quaternion channel never fails: the clip can go far past the range and rom still gives measured 0, PASS. Nothing in the books warns about this. The maker's run d-09 found the letter-index fault but not this unit fault."
    evidence: "rigrev_tests.py: Hips in QUATERNION mode, keyed 0 -> 30 -> 0 degrees about X. Manifest {channel: rotation_quaternion.1, units: deg, min: -15, max: 15} gives rom measured 0.0, PASS, reached [0.0, 0.2588]. The same channel with min/max = ±sin(7.5 degrees) = ±0.1305 and units 'quat' gives FAIL, over 0.128, frames 6-14 (right)."
    smallest_fix: "controls-export-import.md §3 (one place; blender-mcp.md §6 and R-05 point to it): 'A quaternion channel is a raw component, not degrees: for a range of ±θ about one axis, write min/max as ±sin(θ/2) on that axis's component, with units quat. A degree range on a quaternion channel always passes.' In proposals/character-rigger.md row 3 (clip_check), add: convert quaternion channels to degrees (swing or twist about a named axis), or refuse a deg unit on a quaternion channel."
  - id: F3
    class: blocking
    check: C8 V3
    where: "rigging-craft/references/tests.md:22 (Read at the game camera row), :72 G-05; rigging-design/SKILL.md:124 P-11; design-for-motion.md:51 (step 3); blender-mcp.md:99"
    expected: "'Black-fill component count equal to rest' catches a part that comes off (a head lifted from its socket, a hand off the wrist) in the game-camera black-fill. Per blender-keying §7 that black-fill is a full phone-size frame (for example 1170x540) with the character at game distance."
    observed: "look_check.py lists only components of 0.5 % of the image or more (COMPONENT_MIN_FRAC = 0.005, no flag to change it). On a 1170x540 frame that is 3,159 px. At game distance a detached head, hand or cap is much smaller, so the count stays equal to rest and G-05 passes, with no error. The player-sized reference block that design-for-motion §4 step 2 puts in the frame is also below the limit. The maker's d-08 run used a figure that filled the frame, so it did not show this."
    evidence: "Synthetic 1170x540 magenta black-fills: figure 127 px tall, head lifted 12 px off the body: component_count 1 (the same as rest; the 676 px head is not listed). The same figure 3x larger, head lifted: component_count 2 (right). The whole-mask bbox height changed (127 -> 139) in the small case, but the books do not use it."
    smallest_fix: "In tests.md §2 (Read at the game camera row; G-05, P-11 and design-for-motion §4 point to it): 'count components on the black-fill cropped to the figure's box plus a 10 % margin (a component under 0.5 % of the image is not listed), or render the count frame closer at the same angle; the full frame is for the read and the box-edge check.' Add a proposal row for look_check.py: a --min-frac option."
  - id: F4
    class: blocking
    check: C3
    where: "rigging-craft/references/tests.md:68 G-01, :89 R-11, :91 R-13; rigging-design/SKILL.md:116 P-03, :119 P-06; rigging-design/SKILL.md:141 (§9 #6 check), :144 (§9 #9 check)"
    expected: "Owner: 'Turn every checkable finding into a line in the role's self-review.' The role file names the self-review as P-01..P-14, G-01..G-07, R-01..R-13 and the 22 release items."
    observed: "Five checkable findings have their rule in the books but no self-review line to run: WT-24 (a premium variant never has fewer secondary-motion sources than the base; §9 #9 states the rule, but R-11 checks only sockets, contacts and base clips, and base clips still play on a variant that has lost a chain); CD-11 (an invented creature's joints are placed from a named real source per part: creatures-mechanisms-faces.md:19 only); PP-09 (each separable or swappable part is its own named object or MeshPart: region-routes.md:27 only; G-01 counts connected parts, not named swappable ones); PP-12 / D-21 (names, axes, sides and sockets match the game's other rigs: only in the §9 #6 check cell, which the role file does not run); PP-28 (a step repeated on a third asset gets a tool ticket: C-18 and blender-mcp §5 only)."
    evidence: "grep of the P-, G- and R-lines for chain, secondary, source, separable, convention, ticket: no match for these five rules. The coverage table §a rows WT-24, CD-11, PP-09, PP-12 and PP-28 name no P-, G- or R-line."
    smallest_fix: "Add short clauses to existing lines: R-11 '... and every base secondary chain present (count ≥ the base)'; P-03 or P-06 'an invented creature's joints each name their real source skeleton'; G-01 '... every separable or swappable part its own named object'; R-04 'names, axes, sides and sockets diffed against the game's earlier rig manifests: no conflicting use'; R-13 '... a step repeated by hand on a third asset has a tool ticket'."
  - id: R1
    class: recommendation
    check: C8 V6, V7; C7
    where: "rigging-design/SKILL.md:64-70 (D-16..D-22), :75-78 (four new §5 rows), :99-127 (§7, §8)"
    expected: "V7: steps, rules and self-check in roughly the first 5,000 tokens (about 18 KB). V6: one rule, one place. Owner: 'better work, not longer books'."
    observed: "SKILL.md grew from 12,252 to 30,803 bytes. §7 rules start at character 19,805 and §8 (the K2 self-check) runs from 20,904 to 23,981, so after a compaction the agent loses the rules and P-01..P-14 as well as §9. SKILL.md:19 and the role file tell the agent to re-read §8 and §9, which lowers the risk (round 2 of the animator review accepted this). The 'standard needs' list (shoulders and hips, head through a spin, hands, hook shapes) is written about 10 times: §1, step 2, step 6, D-17..D-19, four §5 rows, P-02, P-07, design-for-motion §2, controls §2, motion-needs §2, R-04, and rig-pipeline K1/K2/S6/§8. D-16..D-19 restate design-for-motion §1-§2 almost word for word."
    evidence: "python offsets: '## 7.' 19805, '## 8.' 20904, '## 9.' 23981, length 30734 characters; grep 'world-orient|world orient' gives 20 hits in 10 files."
    smallest_fix: "Make D-16..D-19 one-line pointers ('design for motion and the read controls: references/design-for-motion.md §1-§2'), and the four new §5 rows a single row with the same pointer. This moves §7-§8 back inside about 18 KB. Keep the K1/K2/S6 wording, which is shared with the animator's books."
  - id: R2
    class: recommendation
    check: C1
    where: "coverage/character-rigger.md:77 (VH-07 row)"
    expected: "Each landed-in note quotes what the location really says."
    observed: "The row says G-06 holds 'the key-pose black-fill still names the character'. G-06 (tests.md:73) has 'identity anchors and hook shapes visible from the side the camera sees', which carries the rigger's part of VH-07. The quoted words are not there, and a self-check where the agent names its own character would break V1."
    evidence: "tests.md:73"
    smallest_fix: "Change the coverage cell to 'G-06 (identity anchors visible in the key poses)'."
  - id: R3
    class: recommendation
    check: C7
    where: "rigging-craft/references/tests.md:36"
    expected: "The heading matches the table (14 clips since clips 13 and 14 were added)."
    observed: "The heading still reads '## 4. The 12 test clips'."
    evidence: "tests.md:51-52 rows 13 and 14"
    smallest_fix: "'## 4. The test clips (S5; RP:437-448; 13-14 added in J018)'. Keep the section number."
  - id: R4
    class: recommendation
    check: C7
    where: "rigging-design/references/worked-examples.md:19"
    expected: "Pointers name a line that exists."
    observed: "'measured on the phone at release (R-line phone row)': no R-line covers phone cost. It is release item RB6 (tests.md:60)."
    evidence: "tests.md:79-91 R-01..R-13"
    smallest_fix: "'(release item RB6)'."
  - id: R5
    class: recommendation
    check: C7
    where: "rig-pipeline/SKILL.md:52 (K5)"
    expected: "K5 allows the verdicts the release lines allow: PASS, MEASURED without a sheet tolerance (C-08), n/a, not verified, BLOCKED."
    observed: "K5 says 'every test and every release line ... PASS, or BLOCKED with the reason'. tests.md:63 and rigging-craft SKILL.md:72 allow MEASURED and not verified. An animator who reads K5 can reject a rig that the rigger released correctly."
    evidence: "rigging-craft/SKILL.md:48 C-08; tests.md:63"
    smallest_fix: "K5: '... PASS, MEASURED (no sheet tolerance), n/a, or BLOCKED / not verified with the reason'."
  - id: R6
    class: recommendation
    check: C4
    where: "rigging-design/SKILL.md:65 (D-17 evidence), design-for-motion.md:24, :28, :32; motion-needs.md:24; controls-export-import.md:77"
    expected: "Engine claims as the docs state them."
    observed: "(a) 'clavicles exist only on advanced R15' and 'fingers exist only on advanced R15' are true among R15 avatar bodies (characters/index.md:87-95). A custom Bone rig for an NPC or creature can add them, as worked example 1 does, but the short form can make an agent refuse clavicles on a custom NPC. (b) 'Studio's Curve Editor converts to Euler ... and cannot convert back': per curve-editor.md:26, 39-41 this happens only when the default rotation type is Euler. With Quaternions set, the conversion keeps the quaternions."
    evidence: "characters/index.md:87-95; animation/curve-editor.md:26, 41 'If you set the rotation type to quaternions, the conversion to curves preserves the quaternions'."
    smallest_fix: "(a) 'among R15 bodies only advanced R15 has clavicles (fingers); a custom rig may add them'. (b) '... converts to Euler unless the Default Rotation Type is Quaternions'."
  - id: R7
    class: recommendation
    check: C7 (proposal)
    where: "rigging-craft/evals/briefs.md brief 1 check 1.4 (must) vs tests.md:33 and rig-pipeline §4a"
    expected: "Eval checks agree with the light-check rule (owner J005-D8) that the new books follow."
    observed: "Check 1.4 (must) asks for 'S4 proxy sweep through every §B extreme with 6-view renders'. The rebuilt S4 renders images only for failing numbers plus ≤ 8 key poses, so a grader fails a correct run. evals/ is fixed in this job, so this needs a proposal."
    evidence: "evals/briefs.md brief 1 table; coverage §c row for tests.md:27 (the maker saw the conflict in the book but filed no eval row)"
    smallest_fix: "Add a proposals/character-rigger.md row: eval 1.4 -> 'S4 proxy sweep through every §B extreme with numbers per pose; images for failing poses plus ≤ 8 key poses'."
  - id: R8
    class: recommendation
    check: C4 (workflow)
    where: "rigging-design/SKILL.md:43 (step 10: 'run this at the proof ... send any finding as a plan revision (bump the sheet revision)')"
    expected: "Each step can be carried out inside the saved workflow."
    observed: "In job-character.js the P3-proxy-pose call owns only `${RIG}/proof/` and the test place (line 'owns'), not §C of the sheet. So inside a workflow the rigger cannot bump the plan at P3. The G3 proposal rows extend the P3 checks but not its owns."
    evidence: ".agents/workflows/jobs/job-character.js P3-proxy-pose call: owns [`${RIG}/proof/`, test place]"
    smallest_fix: "Step 10: 'inside a saved workflow, write the finding in the proof hand-back for the lead (the P3 call owns only proof/)'. Or add `owns` §C to the G3 P3 proposal row."
  - id: R9
    class: recommendation
    check: C8 V3
    where: "rigging-craft/references/blender-mcp.md:60-63 (recipe 1 `visible`), tests.md:33 (cap exposure 'from the 6 review cameras', which the S2 inventory makes orthographic)"
    expected: "The ray direction matches what the camera sees."
    observed: "visible() casts from the camera's position to the point, which is a perspective view. For an orthographic review camera the rays are parallel to its view axis, so a camera placed close to the model gives a different visible set from its own render. I did not measure this. It is a risk, not a proven fault."
    evidence: "rigging-craft/SKILL.md:27 ('6 orthographic renders'); recipe 1 code"
    smallest_fix: "One line under recipe 1: 'for an orthographic camera cast along its -Z axis from a point behind the target (origin = point - axis * far)'."
keep: [design for motion moved to S2 on the reference set or blockout, with an owner per finding and a design_for_motion key in §C; the read controls (clavicles or upper-torso range, pelvis control, head world-orient switch on the rest world frame, hand shapes or swaps, one control per hook-shape part, chains as one mass plus offsets, quaternion for spin-heavy controls, independent left and right) offered at K2 and struck by the animator, which keeps D-02 and less-is-more; the posed plan at the game camera with a written image budget (≤ 4 + 1) that matches rig-pipeline §4a and the animator's contact sheet; the S4 sweep made numbers-first, in line with J005-D8; push routes with no clip scale (Pose.yaml, Bone.yaml) and the bone-scale probe left as a proposal; the bake findings from real runs (visual-key bake keeps the world-orient hold, a default bake drops it; Action plus slot or a frozen bake; compare re-imports by clip frame); the protected group must reach the transition, which I re-ran (a leak inside the group: 0.0155 FAIL at ±60 degrees, and an Action that keys the swept bone does not hide it, so the maker's 'clear the Action' note is not needed); recipe 4 runs on a 5.1.2 visual bake (9 scale channels, none ≠ 1); the diagnosis rows from real runs; 'the problem behind a note' in diagnosis §1, the role file and craft step 11; the partner-ask table in the role file; §9 states UP-01, 02, 04, 05, 09, 10, 11, 13, 15, 17 for rigging, adds 06, 07, 12, 14, 16, 18 with reasons and gives sound reasons for leaving out 03, 08, 19, 20, with no contradiction; K2 and S6 wording equal to animation-design §3 step 9 and animation-craft §3 step 2; C1-C5 kept in modeler-handoff, with the new check as a proposal for rig-parts.md; all three proposal rows from other roles adopted; worked examples (knight, fox, toy player, mimic, sword skin) that follow the steps]
verdict: fix-first
</spec>
```

## Check results

| Check | Result | Notes |
| --- | --- | --- |
| C1 coverage | PASS (63 rows checked, 0 failed) | All 63 rigger IDs in `matrix.md` have a row; 17 untagged rows also used. I opened every landed-in location: each carries the rigger's part of the rule. The 9 rejections are sound: colour, value, UV, form shading, size steps and proportions belong to the art director and modeler, and the rig side of VC-06 is handed over through R-10. The VH-07 wording is inexact (R2). |
| C2 core principles | PASS | `rigging-design` §9 has each principle with an example and a check. It covers the 10 the master lists for the rigger, adds 6 with reasons, and names the 4 it leaves out (UP-03, 08, 19, 20) with sound reasons. No contradiction with the master. The §9 check cells for #6 and #16 are not in the P/G/R lines (F4). §9 sits past the compaction cut, but there is a re-read line (R1). |
| C3 self-review | FAIL (F4) | The P-, G- and R-lines name their input (N, K, R, C) and run with our tools. Five checkable findings have no line (WT-24, CD-11, PP-09, PP-12/D-21, PP-28). Three lines that exist give false passes (F1-F3, under C8). |
| C4 kit rules and engine | PASS with R6, R8 | No conflict with AGENTS.md, rules/ or J018-D2/D3/D4. Engine facts are in the mirror; two are stated too broadly (R6). No invented tool mode: rig_audit (CLI and audit_scene), clip_check (CLI and sample_clip), look_check silhouette and thumb, and roblox_fbx export and check_exporter are all real. |
| C5 nothing valuable lost | PASS | Every removed old line is kept, sharpened or moved: the 7 old self-check lines are in P-01, 05, 06, 08, 10, 12, 13; D-01..D-15 are kept; the old S4 '6 views at every pose' is replaced under J005-D8; the old 'seam check' at S4 is covered by cap exposure and overlap. The coverage §c log matches the diff. |
| C6 fixed rules | PASS | Only the owned books changed (git status; evals/ and tripo-routes.md unchanged); role frontmatter byte-identical to df13ff4; SKILL.md 153 / 79 / 104 lines; descriptions 397 / 400 / 374 characters; no § renumbered; the J018 phrase in all 15 changed or new files; no Riot, game, champion, library ID or transcript line in the bodies (D-03 and C-11 evidence now read '[V] (RP:n)'); no tips section; LF endings. `sync_harness.py --check` reports the generated copies as different, which the lead fixes by running sync before the commit. |
| C7 better work | Better, with weak spots | See below. |
| C8 brief v2 | FAIL (F1-F3) | V1 pass (every line names its input; budgets: P-11 4 + 1, G-06 8 + 1, R-10 8, full set once at release; 'a still proves a pose, not timing'). V2 pass. V3 fail: three measuring lines give a wrong number with no error on the real input type (F1 weighted parts, F2 quaternion hips, F3 a small figure at the game camera); R9 is an untested risk. V4 n/a (no money, policy, saves or remotes). V6, V7: recommendation (R1). V8: findings became the §C design_for_motion key, partner asks and review lines. V10 pass (K2, S6, budget, C1-C5 consistent). V11 pass (3 adopted, 1 'not mine' with a reason). |

## Better work (C7)
I read the books as the agent would for eval brief 2 (a fox pet, up to 30 on screen, active tail, S2 only) and brief 1 (a merged Tripo teddy, full loop).

The old books planned routes, joints and cuts, then checked them in a sweep from review views. The new books make the agent do four more things before any cut. First, it writes what the pet must read as and how it moves (a hop: compress range in hips and ankles). Second, it spends joints where they read: head, two independent ears, and a tail driven as one mass plus offsets, with the swoop as the hook shape. Third, it screens the design for mass on joints, drapes and costly parts, with an owner for each. Fourth, it poses the plan at the game camera before the modeler builds. This catches the problems that cost the most later: a collar in the jaw, a cape over the arms, a mouth modelled shut, a dead wind-up, a head that turns with the body in a spin.

The craft side now has numbers for each of these, and real runs found traps the old books did not know: a default bake drops the head hold; an Action without a slot bakes a frozen pose; a short protected group reads 0. The worked fox example is almost this eval brief.

Weak spots:
- Three of the new numbers give a false pass in common real cases: weighted or skinned caps (F1), quaternion hips (F2), and a small figure in a full game-camera frame (F3). Brief 2's pet, 'small on screen', is exactly the F3 case.
- Five checkable rules have no self-review line (F4).
- The design SKILL is 2.5 times longer and repeats the read-controls list in about ten places (R1).
- Eval check 1.4 now fails a correct run (R7).

None of these makes the work worse than the old books. After F1-F4 are fixed, the agent will make clearly better rigs.

Could not check: Studio import and in-place captures (no Studio connected, as for the maker); the orthographic-camera risk (R9) by a run.
