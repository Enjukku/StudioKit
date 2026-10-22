---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer character-rigger · claude-opus-5-5 · high · 2026-10-22

# J018 stage 3 review: character-rigger books, round 3

Scope: `.agents/roles/character-rigger.md` (body), `.agents/skills/rigging-design/**`, `.agents/skills/rigging-craft/**` (not `evals/`), `.agents/skills/rig-pipeline/**`. I reviewed the working tree on 2026-10-22 against `df13ff4`, after maker repair round 2. I read the two earlier reviews first. Then I read the role file and all 15 book files in full, and after that the coverage and proposals files. I ran the changed recipe (recipe 1 with `tri_points` and `mark_plane_caps`) myself on synthetic parts in Blender 5.1.2 headless. The code was taken from the book text and run without edits (`rigrev3_caps.py` and `rigrev3_caps2.py` exec the python block of `blender-mcp.md` §6 recipe 1). I also checked whether FBX keeps a vertex group that has no bone (`rigrev3_fbxgroup.py`). The scripts are in the reviewer's scratchpad. I changed nothing in the repo except this file.

```text
<spec>
artifact: .agents/roles/character-rigger.md (body) + .agents/skills/rigging-design/** + .agents/skills/rigging-craft/** (not evals) + .agents/skills/rig-pipeline/** @ working tree 2026-10-22 (J018 stage 2, after repair round 2)
reviewer: J018 reviewer character-rigger (opus, high), round 3
looked_at_first: [reviews/character-rigger-rev1-reviewer.md and -rev2-reviewer.md; then the role file and the 15 book files in full and the diff of each against df13ff4; role frontmatter compared with df13ff4 (identical); SKILL.md sizes, descriptions and section offsets; old and new headings of every changed file; tools/rig/rig_audit.py audit_weights (non_deform_groups_with_weight) and the CLI flags; look_check.py and clip_check.py --help; modeling-craft/references/rig-parts.md §2-§3 and handoffs.md (part files on a working copy); then coverage/character-rigger.md (incl. both repair tables) and proposals/character-rigger.md; matrix.md (63 rigger IDs, scripted against the coverage rows); other roles' proposal rows against these books (V11); rigging-craft/evals/briefs.md; runs (Blender 5.1.2 headless, recipe 1 verbatim): a torso box, a 16-gon head weighted 100 % to its bone by an Armature modifier (cap marked by mark_plane_caps), and a plain box upper arm bounded by a shoulder cut plane and an elbow cut plane (both marked by mark_plane_caps into the one `cap` group, as the book says); rest and ±60 degree head tilts; front, back, left, right and game perspective cameras and an orthographic back camera; a dense count (171 points per triangle) over the true cap faces as the truth; the same arm with one group per cut; a Subdivision modifier after the Armature; a cube with a `cap` group exported to FBX and imported again]
findings:
  - id: F1
    class: blocking
    check: C8 V3 (and C3 G-03, P-11)
    where: "rigging-craft/references/blender-mcp.md:53 (cap faces = 'the faces whose vertices are all in the part's `cap` vertex group'), :73-76 (cap_count: one vertex set, subset test), :79-84 and :88 (mark_plane_caps writes every cut of a part into the same group); rig-pipeline/references/modeler-handoff.md:55 (deliver), :61 (C5); rig-pipeline/SKILL.md:50 (K3); rigging-craft/references/tests.md:20, :32 (§3 step 1), :70 (G-03); rigging-design/references/design-for-motion.md:50 (§4 step 2); rigging-design/SKILL.md:121 (P-11)"
    expected: "Recipe 1 counts points on the cap faces only, for every part the books apply it to: the rigger's own S2 proxy, which design-for-motion §4 step 2 makes by splitting the blockout at the §C cut planes, and the modeler's S3 parts. A part between two cuts (an upper arm cut at the shoulder and at the elbow, a torso cut at the neck and at the waist) has two caps in its group."
    observed: "A vertex group holds vertices, not faces. When one `cap` group holds both rims of a part, every side face whose corners all lie on one of the two rims counts as a cap face. A blockout box, or a low-poly part with no edge loop between its two cuts, has only such side faces. So the side faces are sampled, and the part reads cap exposure above 0 at rest from every camera that sees a side, with no error. mark_plane_caps returns 1 for each cut, which looks like a correct result. The same shared group also gives no way to run the G-03 clause 'every cut of the part with faces in the group': if one of the two caps is missing from the group, the count is still above 0."
    evidence: "rigrev3_caps.py. Box upper arm (8 vertices, 6 faces) with mark_plane_caps at z = 2.8 and z = 1.6 (returns 1 and 1). cap_count takes all 6 faces as cap faces (84 sampled = 6 x 14). At rest it reads 14 from the front, back and right cameras. The dense count over the two true caps reads 0 of 684 from those cameras (false FAIL, no error). From the game camera it reads 28, against a true 325 of 684 (the shoulder cap really shows from above in this scene). rigrev3_caps2.py: the same arm with one group per cut (`cap_shoulder`, `cap_elbow`) and recipe 1 run per group reads 0 where the dense count is 0 and 14 where it is 325, in all 18 camera-pose cells. The 16-gon weighted head: the recipe is above 0 in exactly the cells where the dense count is above 0 (44/98 vs 1107/2394 from the back at a 60 degree forward tilt), and 0 in all the others. So round-2 F1 is fixed."
    consequence: "Every S2 posed plan on a blockout, and every S4 sweep on low-poly parts (worked example 3, the blocky toy player, checks its ball-and-socket covers by cap exposure), gives a cap FAIL at rest that is not true. The agent then either sends the modeler a false fix note, which uses one of the two rounds, or learns to ignore G-03."
    smallest_fix: "One vertex group per cap or socket, named `cap_<cut id>` (the §C cut id). A cap face is a face whose vertices are all in one of these groups. cap_count runs per `cap_*` group and reports (visible, sampled) per cut. mark_plane_caps takes `group=f'cap_{cut}'`. The pass adds: every §C cut of the part has its group, with sampled above 0. A missing group then stops the recipe with a KeyError, and a group with no whole face samples 0. Make the same change in modeler-handoff `deliver` and C5, rig-pipeline K3, tests.md §2 cap row, §3 step 1 and G-03, design-for-motion §4 step 2, diagnosis.md:48, and proposal rows 2 (`rig_audit.py caps`) and 17 (`rig-parts.md` step 5). Add one diagnosis cause: 'one group holds both rims of a part, so side faces between the rims are counted'."
  - id: R1
    class: recommendation
    check: C8 V3; C7
    where: "rigging-craft/SKILL.md:31 (step 6: 'the cleanup order (remove non-deform groups → ...)'); rigging-craft/references/weights.md:14 (§3 item 1)"
    expected: "The S5 weight cleanup keeps the vertex groups that the later S5 lines need: the `cap` group(s) for R-03 (the G-03 numbers on the real rig) and the protected groups for R-02."
    observed: "SKILL step 6 says 'remove non-deform groups', with no qualifier. `rig_audit.audit_weights` lists every such group under `non_deform_groups_with_weight`, so on the real rig the report names `cap` and the protected groups. An agent that follows step 6 literally deletes them, and R-02 and R-03 then cannot run. weights.md §3 says 'accidental', which is right but does not name the groups to keep."
    evidence: "tools/rig/rig_audit.py:53-57, :79; tests.md:80-81 (R-02, R-03)"
    smallest_fix: "SKILL step 6: 'remove accidental non-deform groups (keep the `cap_*` and protected groups)'. weights.md §3 item 1: the same parenthesis."
  - id: R2
    class: recommendation
    check: C8 V3
    where: "rigging-craft/references/blender-mcp.md:86 ('The cap indices come from `ob.data`: true only while no modifier before the Armature changes the topology.')"
    expected: "The caveat names every case where the evaluated faces do not match `ob.data`."
    observed: "A topology-changing modifier after the Armature (Subdivision, Mirror, Decimate) also breaks the match. In my run the 'sampled 0 is never a pass' rule caught the result, but the sentence sends the agent to look only above the Armature."
    evidence: "rigrev3_caps.py: the weighted 16-gon head with a level-1 Subdivision after the Armature, tilted 60 degrees: (0, 0) from all six cameras, against 44/98 without it."
    smallest_fix: "'... true only while no modifier anywhere in the stack changes the topology (Subdivision, Mirror, Decimate): count on a copy with them applied or turned off; sampled 0 is the sign'."
  - id: R3
    class: recommendation
    check: C8 V10
    where: "rig-pipeline/references/modeler-handoff.md:55 (deliver: 'part files in content/rigs/<asset-id>/geometry/ (each part's cap and socket faces in a vertex group ...)')"
    expected: "The delivered file format keeps the group the rigger needs."
    observed: "The brief does not name a format. FBX does not keep a vertex group that is not bound to a bone. If the modeler sends FBX parts, the cap group is gone, recipe 1 stops with a KeyError, and S4 starts with a fix note that was not necessary. The modeler's handoffs.md says 'part files on a working copy', which suggests .blend, but the brief does not say it."
    evidence: "rigrev3_fbxgroup.py: a cube with a `cap` group, exported with export_scene.fbx and imported with wm.fbx_import, has vertex_groups []."
    smallest_fix: "deliver: '... part files as a .blend working copy (FBX drops vertex groups with no bone) ...'."
keep: [every round-1 and round-2 keep item; recipe 1 sampling through each face's triangles (n-gon, fan, quad and concave caps covered; my 16-gon run matches the dense count's zero and non-zero cells exactly); (visible, sampled) with 'sampled 0 is never a pass' (it caught the Subdivision case in my run); the hidden-part guard; the named KeyError on a missing group; mark_plane_caps as the fallback for flat caps, with a dome or tucked cap with no group sent as a fix-note item; the `cap` group asked of the modeler in deliver, C5 and K3, with the rig-parts proposal row; recipe 5 pass in degrees and `swing ≤ θ° (recipe 5)` in the manifest's validation query, with the animation-craft proposal row; the round-2 coverage cell fixes]
verdict: fix-first
</spec>
```

## Earlier findings: status

| Id | Status | Evidence |
| --- | --- | --- |
| rev1 F1-F4, R1-R9 | fixed (as round 2 recorded) | unchanged since round 2. I re-read the lines: evaluated mesh (blender-mcp.md:74), `quat` ranges (controls §3), crop count (tests.md:22), the five self-review clauses (G-01, R-04, R-11, R-13, P-06), K5 verdicts, step 10 workflow route, R15 and Curve Editor claims, orthographic rays (blender-mcp.md:60-64) |
| rev2 F1 (cap points from the first four corners) | fixed | blender-mcp.md:56-59, :74-76 sample 7 points in every loop triangle of each cap face. In my run on a weighted 16-gon head, the recipe was above 0 in exactly the 6 of 18 cells where the dense count was above 0. diagnosis.md:48 names n-gon and fan caps. Proposal row 2 names triangle sampling |
| rev2 F2 (`cap` group never asked for) | fixed, with a new fault in how the group defines a face (F1 above) | modeler-handoff.md:55, :61; rig-pipeline/SKILL.md:50; tests.md:32; rigging-craft/SKILL.md:29; blender-mcp.md:88; proposal row 17 |
| rev2 R1 (swing pass in degrees) | fixed | blender-mcp.md:131; controls-export-import.md:30; tests.md:83; proposal row 18 for animation-craft §3 step 2 |
| rev2 R2 (coverage cells for the merged §5 row) | fixed | coverage §a EX-09, EX-10, SS-15, WT-18 cite "§5 (read-controls row)" |

## Check results

| Check | Result | Notes |
| --- | --- | --- |
| C1 coverage | PASS (63 rows checked, 0 failed) | A script shows that all 63 IDs tagged for the rigger in `matrix.md` have a row. I read every book file in full in this round and matched each landed-in cell to its text. For example: PP-14 in creatures §2 and G-02; CD-27 in creatures §1 rows; SD-22 in the strain-range bullet; PP-06 in weights §4; GD-06 in motion-needs §7; WT-25 in the weights chain row and design-for-motion §2; PP-19 in the feet row and R-07; SS-10 in the spine row and G-06. The 9 rejections are still sound. |
| C2 core principles | PASS | `rigging-design` §9 is unchanged since round 2. It has 16 principles, each with an example and a check. The four "no" rows have reasons. Nothing contradicts `universal-principles.md`. |
| C3 self-review | PASS, except the G-03 and P-11 cap number on parts with two cuts (F1) | Every checkable finding has a P-, G- or R-line or a release item. |
| C4 kit rules and engine | PASS | No conflict with AGENTS.md, rules/ or J018-D2..D5. No engine claim is new since round 2. Every tool mode is real (`rig_audit.py` flags, `look_check.py silhouette`, `clip_check.py` CLI). The `cap` group is plain Blender data, not a tool mode. |
| C5 nothing valuable lost | PASS | Round 2 replaced the corner grid with triangle sampling, which is better, and added the group hand-off. It removed nothing. The coverage §c log matches the diff. |
| C6 fixed rules | PASS | Only the owned books changed (evals/ and tripo-routes.md are unchanged). The role frontmatter is byte-identical. SKILL.md lengths are 150 / 79 / 104 lines and the descriptions are 397 / 400 / 374 characters. Only appended sections are new: design §9, pipeline §8, motion-needs §7, tests §6, blender-mcp §6. The tests §4 title was reworded with its number kept. All 15 files carry the J018 phrase. The bodies have no Riot name, library ID or transcript line, and there is no tips section. |
| C7 better work | Better, with one fault to fix | See below. |
| C8 brief v2 | FAIL (F1) | V1, V2, V4 (n/a), V6, V7 (accepted in round 2), V8 and V11 pass. Partner consistency (V10) passes, with R3 as a small format gap. In my runs recipe 1 now gives the right answer on n-gon, weighted and orthographic cases. It gives a wrong number with no error on a part bounded by two cuts with no loop between them (F1). R1 and R2 are smaller V3 gaps. |

## Better work (C7)
I read the books as the agent would for eval brief 3 (a cartoon rifle: magazine drop, bolt pull, hand-to-holster, first and third person) and brief 1 again (the merged Tripo teddy).

For the rifle, the new books add four steps that the old ones did not have, and each changes the result:
- A kinematic diagram first, with moving parts given room: the bolt travel is cleared of the hand, and decoration that blocks it goes back to the modeler at S2.
- Contact points fixed across variants: the grip and stock-to-shoulder positions.
- Overlap pairs counted as 0 through the full reload cycle (recipe 2).
- No scale in clips, so a cartoon squash on the recoil becomes a swap mesh or VFX, not a rig feature that Roblox will not play.

The kept line "first- and third-person are separate review targets" covers check 3.4.

For the teddy, the S2 screen, the read controls, the posed plan at the game camera and the numbers-first S4 sweep now hold up in the hard cases found in rounds 1 and 2: weighted parts, quaternion hips, a small figure, n-gon caps, and a cap group that was never handed over.

One weak spot remains, and it is in the same recipe. The S2 posed plan is made on a blockout split at the cut planes, and a blockout limb is a box. Every box part that lies between two cuts reads "cap exposed" at rest. The agent cannot pass P-11 or G-03 honestly on these parts, and on low-poly characters it can send a false fix note. The fix is small: one group per cut.

The other weak spots are minor. The design SKILL is still about 30 KB, with the self-check past the compaction cut; round 2 accepted this, and a re-read line covers it. Step 6 also says "remove non-deform groups" without naming the groups to keep (R1).

Nothing in the new books makes the work worse than the old books, except the false cap FAIL on two-cut parts.

Could not check: the Studio import and the in-place captures (no Studio connected); a modeler's real hand-back with a `cap` group (no such hand-back exists yet).
