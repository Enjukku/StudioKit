---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer character-rigger · claude-opus-5-5 · high · 2026-10-22

# J018 stage 3 review: character-rigger books, round 4 (focused)

Scope: the round-3 blocking finding and its repair. I read the round-3 review first. Then I read the current books: the role body, `rigging-design/**`, `rigging-craft/**` (not `evals/`) and `rig-pipeline/**`, with every line that names a cap, a socket or `cap_<cut id>`. After that I read the coverage note "Repair round 3" and the proposal rows. I ran recipe 1 myself in Blender 5.1 headless. The code was taken from the current book text and run with no edits (`rigrev4/rigrev4_caps.py`, `rigrev4/rigrev4_mods.py` in the reviewer's scratchpad). The truth for each cell is a dense count of 105 points per triangle with the same `visible` test. For a socket, the dense count keeps only the area that the child covers at rest. I changed nothing in the repo except this file.

```text
<spec>
artifact: .agents/roles/character-rigger.md (body) + .agents/skills/rigging-design/** + .agents/skills/rigging-craft/** (not evals) + .agents/skills/rig-pipeline/** @ working tree 2026-10-22 (J018 stage 2, after repair round 3)
reviewer: J018 reviewer character-rigger (opus, high), round 4
looked_at_first: [reviews/character-rigger-rev3-reviewer.md; the books: every cap, socket and `cap_<cut id>` line (blender-mcp.md §6 recipe 1 and groups paragraph; tests.md §2 cap row, §3 step 1, G-03, R-02, R-03; weights.md §3; rigging-craft SKILL steps 4 and 6; design-for-motion.md §4; diagnosis.md cap rows; region-routes.md §5; rigging-design SKILL step 10 and P-11; modeler-handoff.md deliver and C5; rig-pipeline SKILL K3 and §8; worked-examples.md 1-4); templates/rig/rig-sheet.md §B-D (`cut.hide_by`); modeling-craft SKILL step 2 (blockout from primitives); frontmatter, SKILL sizes, descriptions and headings against df13ff4; files changed since the round-3 review (mtime); then coverage/character-rigger.md "Repair round 3" and proposal rows 2 and 17 (proposals file lines 18 and 33); runs (Blender 5.1 headless, recipe 1 verbatim): a box torso with one quad per side, a 16-gon head weighted 100 % to its bone sitting on the torso top, the round-3 8-vertex box upper arm with a shoulder and an elbow cut, and a blocky arm flush on the torso's side face; every group made by `mark_plane_caps` as the book says, the child's cap and the parent's socket for each cut; rest, head forward 60°, each arm raised 60°; front, back, left, right, game, orthographic back and ¾-high cameras (168 cells); the S5 cleanup operators with `BONE_DEFORM` on a part that carries `cap_*` groups; a head with a Subdivision after the Armature and a half head with a Mirror before it]
findings:
  - id: F1
    class: blocking
    check: C8 V3 (and C3 G-03, P-11)
    where: "rigging-craft/references/blender-mcp.md:53 (the socket on the parent shares the child's `cap_<cut id>`), :79-84 (mark_plane_caps takes every face on the cut plane), :85 (the parent counts each R-cut child's id), :87 (pass: visible 0 per cut at rest), :89; rigging-craft/references/tests.md:20, :32, :70 (G-03); rigging-design/references/design-for-motion.md:50 (§4 step 2); rig-pipeline/references/modeler-handoff.md:55 (deliver), :61 (C5); rig-pipeline/SKILL.md:50 (K3); rigging-design/SKILL.md:121 (P-11)"
    expected: "A parent part's socket group holds only the faces that the child covers at rest. The socket then reads 0 at rest from every camera when the joint area is hidden. This must also hold for parts built from primitives: the S2 proxy on a blockout (modeling-craft step 2 builds the blockout 'from primitives') and the blocky and low-poly parts of S4."
    observed: "On a blocky or primitive parent, the cut plane lies on one of the parent's own closed outer faces: the torso top under the head, or the torso side face where a blocky arm sits. That face is larger than the child's cap. mark_plane_caps puts the whole face in the socket group and reports 1 face found, which looks correct. The face outside the child's footprint is ordinary torso surface. It shows at rest, so the socket reads 'exposed' at rest with no error, while the joint area is hidden. Nothing in the books says that a socket is only the covered area, and no diagnosis row names this cause. The earlier runs (round 3 and the maker's r3-01) counted only the child's caps. They never counted a parent's socket, so this half of the naming rule was never run."
    evidence: "rigrev4_caps.py, 168 cells. The round-3 case is fixed: the box upper arm reads 0 of 14 for each cut at rest from the front, back, right and orthographic back cameras, where the dense count is 0 of 210 (round 3: 14 of 84). The weighted head reads 44 of 98 from the back at the 60° forward tilt (dense count 657 of 1470), and 0 wherever the dense count is 0. The sockets are wrong. Torso `cap_P02` (the neck socket, the whole top quad): 6 of 14 from the game camera and 4 of 14 from the ¾-high camera at rest, where the dense count over the head's footprint reads 0 of 86. Torso `cap_P09` (the shoulder socket of the flush blocky arm, the whole left side quad): 9 of 14 from the left camera and 5 of 14 from the ¾-high camera at rest, where the dense count over the arm's footprint reads 0 of 65. These are 13 of the 17 wrong cells. They are wrong in every pose, rest included."
    consequence: "Every S2 posed plan on a primitive blockout, and every S4 sweep on blocky parts (worked example 3 is a blocky toy player), gives a socket FAIL at rest on the torso and on any other parent whose face continues past the child. Diagnosis row 49 sends the agent to look for a shared group, which is not the cause. The agent then sends the modeler a false fix note, which uses one of the two rounds, or learns to ignore G-03. This is the same consequence as round-3 F1, from the parent side."
    smallest_fix: "Recipe 1 and the groups paragraph: 'A socket is only the parent's faces that the child's cap covers at rest. When the parent's face on the cut plane reaches past the child's cap (blocky and primitive parts: the torso top under the head, a side face under a flush arm), cut the child's cap outline into that face first (Knife Project from the child), or record the socket as n/a in §C (closed parent face) and count that cut on the child's cap only.' mark_plane_caps on the parent side: keep only the faces whose vertices all lie inside the child's cap outline. The 'every cut has its group' check then accepts a socket recorded as n/a. Make the same change in tests.md §2 cap row, §3 step 1 and G-03, design-for-motion §4 step 2, modeler-handoff deliver and C5, rig-pipeline K3, and proposal rows 2 (`rig_audit.py caps`: a socket fixture on a flush box parent) and 17 (`rig-parts.md` step 5). Add one diagnosis row: 'socket reads exposed at rest on a blocky or primitive parent: the group holds the parent's whole face on the cut plane, not only the area the child covers'."
  - id: R1
    class: recommendation
    check: C8 V3
    where: "rigging-craft/references/blender-mcp.md:56-58 (W: 7 fixed points per triangle, the edge points 10 % in from the edges)"
    expected: "A thin exposed strip along a cap's rim is found on a large low-poly cap (a quad box end gets 14 points)."
    observed: "The sample density is fixed per triangle, whatever the triangle's size. On a quad cap, a strip that shows along the rim and is less than about 10 % of the face width reads 0, and 0 is the pass. The 16-gon n-gon caps have more triangles, so they are less affected."
    evidence: "rigrev4_caps.py: the box upper arm's shoulder cap `cap_P05` from the ¾-high camera reads 0 of 14 at rest, at the head tilt and at both arm raises, where the dense count reads 10 to 12 of 210 (a strip at the far edge, seen past the torso's top edge). These are the other 4 of the 17 wrong cells."
    smallest_fix: "Scale the points to the triangle's area, for example a barycentric grid with n = max(3, ceil(edge length / spacing)) and the spacing in studs written in the rig sheet. Or, when a camera reads 0 on a cap whose dense count has not been run, re-count that cap with 3 times the points before the 0 is a pass. Carry the same item into proposal row 2 (the `caps` tool fixture)."
keep: [every round-1 to round-3 keep item; one `cap_<cut id>` group per cut with the child-side naming (my runs: the round-3 box arm now reads 0 where the truth is 0, for each cut); the group read from the evaluated mesh at weight 1 (my runs: a Subdivision after the Armature samples 224 points on the cap quads only, and a Mirror before it samples 98 points, the same as the whole head); the KeyError on a missing group and 'sampled 0 is never a pass'; the cleanup clause in SKILL step 6 and weights.md §3 (my run: clean, limit-4 and normalize with `BONE_DEFORM` leave the `cap_*` weights at 1.0, and the count is unchanged); .blend part files in deliver; diagnosis row 49]
verdict: fix-first
</spec>
```

## Round-3 findings: status

| Id | Status | Evidence |
| --- | --- | --- |
| rev3 F1 (one group holds both rims) | fixed in every listed place | blender-mcp.md:53, :70-84, :85, :87, :89; modeler-handoff.md:55, :61; rig-pipeline/SKILL.md:50; tests.md:20, :32, :70; design-for-motion.md:50; diagnosis.md:48, new row :49; rigging-design/SKILL.md:121 (P-11); rigging-craft/SKILL.md:29; region-routes.md author line; proposal rows 2 and 17. My run: the box arm reads 0 of 14 per cut at rest where round 3 read 14 of 84. The parent (socket) side of the same rule has a new fault: F1 above |
| rev3 R1 (cleanup deletes the groups) | fixed | rigging-craft/SKILL.md:31; weights.md:14; blender-mcp.md:89. My run: the cleanup operators keep the `cap_*` weights at 1.0 |
| rev3 R2 (modifier caveat) | fixed, with a stronger fix | membership is read from the evaluated mesh at weight 1 (blender-mcp.md:74-75, :87). My run confirms the maker's numbers: Subdivision 224 sampled, Mirror 98 sampled |
| rev3 R3 (FBX drops the group) | fixed | modeler-handoff.md:55; blender-mcp.md:89 |

## Fixed-list checks

| Check | Result |
| --- | --- |
| Only this role's books and job files changed in this round | PASS. Since the round-3 review, the files changed in rigger scope are the 10 book files of this repair plus coverage/ and proposals/character-rigger.md. The role file, tripo-routes.md and evals/ are unchanged. The other changed files belong to other roles' parallel repairs |
| Frontmatter unchanged | PASS. The role and rig-pipeline frontmatter is identical to df13ff4. The two SKILL descriptions are the stage-2 text that rounds 1-3 accepted |
| SKILL.md ≤ 500 lines | PASS: 150 / 79 / 104 |
| Descriptions ≤ 400 characters | PASS: 397 / 400 / 374 |
| No renumbering | PASS. Against df13ff4, only appended sections are new (design §9, pipeline §8, motion-needs §7, tests §6, blender-mcp §6), and the tests §4 title kept its number |
| No citations or Riot names in bodies | PASS. No Riot name or library ID is in any body. The only hit is the attribution comment in the role file, which is accepted |

## Notes
- F1 sits on the parent side of the naming rule ("the cap and its socket share the name"), which round 3 introduced. A socket that is a cup or a fill face of the parent's own cut (a merged mesh split with Bisect with Fill, a modelled socket dome) is not affected. In those cases the fill is the cross-section, and it reads correctly.
- Not checked: Studio (not connected; recipe 1 is Blender-only), and a modeler's real hand-back with `cap_<cut id>` groups (none exists yet).
