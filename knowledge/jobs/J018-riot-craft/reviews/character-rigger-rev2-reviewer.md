---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer character-rigger · claude-opus-5-5 · high · 2026-10-22

# J018 stage 3 review: character-rigger books, round 2

Scope: `.agents/roles/character-rigger.md` (body), `.agents/skills/rigging-design/**`, `.agents/skills/rigging-craft/**` (not `evals/`), `.agents/skills/rig-pipeline/**`. I reviewed the working tree on 2026-10-22 against `df13ff4`, after maker repair round 1. I read all 15 book files in full and the diff of each against `df13ff4`. I checked each round-1 finding in the books. I ran the changed measuring recipes myself on synthetic samples of the real input: Blender 5.1.2 headless (`blender -b --factory-startup --python rigrev2_ngon.py`) and `look_check.py silhouette` on anti-aliased 1170x540 black-fills (`rigrev2_crop.py`). The scripts and outputs are in the reviewer's scratchpad. The recipe code was taken from the book text and run without edits. I changed nothing in the repo except this file.

Order note: I opened `reviews/character-rigger-rev1-reviewer.md` and then `coverage/character-rigger.md` (with its repair table) before I read the book files. The round-2 spec asks for the artifact first. The findings below rest on the books and my own runs, not on the maker's table.

```text
<spec>
artifact: .agents/roles/character-rigger.md (body) + .agents/skills/rigging-design/** + .agents/skills/rigging-craft/** (not evals) + .agents/skills/rig-pipeline/** @ working tree 2026-10-22 (J018 stage 2, after repair round 1)
reviewer: J018 reviewer character-rigger (opus, high), round 2
looked_at_first: [reviews/character-rigger-rev1-reviewer.md; coverage/character-rigger.md incl. repair table; then the 15 book files in full and their diff against df13ff4; role frontmatter compared with df13ff4 (identical); SKILL.md sizes and § offsets; tools/art/look_check.py header and components() (COMPONENT_MIN_FRAC 0.005, area_px, bbox_px fields); tools/anim/clip_check.py _channel_value (deg conversion only for rotation_euler; 'quat' passes through raw); modeling-craft/references/rig-parts.md §2 steps 3 and 5 (caps made by Bisect with Fill); docs mirror animation/curve-editor.md:26-41; partner books animation-design §3 step 9, animation-craft §3 step 2, blender-keying §7, modeling-design read-and-form §6 and review.md §5 MO1-MO7; matrix.md (63 rigger IDs); proposals of all roles (V11); rigging-craft/evals/briefs.md; runs: recipe 1 verbatim on a 16-gon cap (Bisect-Fill shape) and a triangle-fan cap, both weighted 100 % to a Head bone by an Armature modifier, rest and 60 degree tilts, five perspective cameras, against a fan-sampled true count; the tests.md §2 crop block verbatim + look_check silhouette on a 127 px figure with a player block: rest, head lifted 12 px, a 10 px hand detached]
findings:
  - id: F1
    class: blocking
    check: C8 V3
    where: "rigging-craft/references/blender-mcp.md:56-59 (recipe 1 cap_points); used by tests.md:20 (Cap exposure row), :70 G-03, :81 R-03; rigging-design/SKILL.md §8 P-11; design-for-motion.md §4 step 3; region-routes.md (numbers at every extreme)"
    expected: "Recipe 1 samples the whole of every cap face it is given. The real input at S4 is the modeler's part: rig-parts.md:15 makes each cut with 'Bisect with Fill', which gives one n-gon cap. A Tripo or triangulated source gives triangle caps."
    observed: "cap_points builds a bilinear 5x5 grid from vs[0], vs[1], vs[2] and vs[3] only. The comment says 'quads; for other faces lerp centre to corners', but the code does not do this. On an n-gon it samples only the small patch spanned by the first four rim vertices, and the rest of the cap is never tested. The result depends on which side of the cap that patch lies on, and there is no error. On a triangle it raises IndexError. The maker's runs (d-04, r1-01, r1-05) used quad caps only."
    evidence: "rigrev2_ngon.py, recipe 1 verbatim from the book, head weighted to its bone (evaluated-mesh fix active). 16-gon cap, head tilted back 60 degrees: recipe 0 from the front camera, while fan sampling of the same face finds 32 of 144 points visible (false PASS, no error). Tilted forward 60 degrees: recipe 25 from back and game, true 32/144 (right by chance: the patch lies on the exposed side). Triangle-fan cap: 'IndexError: list index out of range' on every camera. Rest: 0 on both (right)."
    smallest_fix: "Replace cap_points with a fan sample that works for any face: `ctr = sum(vs, Vector()) / len(vs)`; for each rim edge (a, b) take `ctr.lerp(a.lerp(b, s), t)` for s in (0.2, 0.5, 0.8) and t in (0.25, 0.5, 0.9)`. Remove the 'quads' comment. Add 'n-gon or triangle caps (Bisect with Fill makes one n-gon)' to the diagnosis.md:48 row. Name n-gon sampling in proposal row 2 (`rig_audit.py caps`)."
  - id: F2
    class: blocking
    check: C8 V10 (and V3)
    where: "rigging-craft/references/blender-mcp.md:53 and cap_count (reads ob.vertex_groups['cap']); rig-pipeline/references/modeler-handoff.md:55 (deliver), :61 (C5); rigging-craft/SKILL.md §3 step 4; tests.md §3"
    expected: "Each input a measuring line needs is either asked of the partner who makes it or built in a named step. Recipe 1 needs every cap face in a vertex group named `cap`."
    observed: "No book asks for or makes this group. The S3 brief (modeler-handoff.md) asks for watertight parts and 'every cap and socket hidden at rest', but not for a cap group. The modeler's rig-parts.md has no vertex-group step. No rigger step at S4 builds one. On the modeler's real hand-back, recipe 1 stops with KeyError. The agent then has to mark the caps by guess, and diagnosis.md:48 already names a group that misses cap faces as a cause of a false 0."
    evidence: "grep for 'cap group', '`cap`' and 'vertex group' in modeling-craft, rigging-craft, rigging-design, rig-pipeline and templates/rig: the only hits are recipe 1 itself and the diagnosis row."
    smallest_fix: "modeler-handoff.md `deliver`: '... + each part's cap and socket faces in a vertex group named `cap`'. Add to C5: '(the rigger counts them with rigging-craft recipe 1)'. Add a proposals row for modeling-craft/references/rig-parts.md §2 step 5: assign the cap faces to `cap` when the cap is made."
  - id: R1
    class: recommendation
    check: C8 V3, V10
    where: "rigging-craft/references/blender-mcp.md:118 (recipe 5 pass rule); controls-export-import.md:30 (§3); tests.md:83 R-05"
    expected: "The swing pass compares degrees with degrees. The manifest record of a control that is measured by swing tells the animator at S6 how to check it."
    observed: "Recipe 5 says 'the largest value ≤ the larger of |min| and |max| of the manifest's tilt range'. §3 tells the agent to write quaternion ranges as ±sin(θ/2) in `quat` units. Read literally, 30 degrees is compared with 0.1305, and the result is always FAIL. If the agent stores the swing range as `deg` on the quaternion channel, the animator's `clip_check.py rom` at S6 (animation-craft §3 step 2) passes it always, which is round-1 F2 again. The books do not say how the manifest records a swing-measured control."
    evidence: "clip_check.py:381 converts only rotation_euler; blender-mcp.md:118; controls-export-import.md:28 (the manifest has a `validation query` field)"
    smallest_fix: "Recipe 5: 'the pass: the largest swing ≤ θ, the §B tilt range in degrees (the manifest holds ±sin(θ/2) on the component)'. §3: 'for a bone measured by swing, keep the `quat` component range and write `swing ≤ θ° (recipe 5)` in its validation query'."
  - id: R2
    class: recommendation
    check: C1
    where: "coverage/character-rigger.md rows EX-09 (:35), EX-10 (:36), SS-15 (:69), WT-18 (:81)"
    expected: "Each landed-in cell names a location that exists."
    observed: "These cells still cite 'rigging-design/SKILL.md §5 (wind-up row)', '(hands row)', '(hook shape row)' and '(spin row)'. Repair R1 merged those four rows into one 'Wind-ups and landings, spins, hands ... hook shapes' row that points to design-for-motion.md §2. The content is still in the other cited locations, so no row fails."
    evidence: "rigging-design/SKILL.md:75 (single merged row)"
    smallest_fix: "Change the four cells to '§5 (read-controls row)'."
keep: [every round-1 keep item, unchanged; the evaluated-mesh fix in recipe 1 (confirmed again: the weighted 16-gon head reads 25 forward-tilted where ob.data would read 0); orthographic parallel rays in recipe 1; the crop count with the area check (my run: rest 2 = 2, head lifted 3, a 10 px detached hand left unlisted but caught by the area check, 5,881 of 5,973 px listed, which sends the agent to a closer render; the full frame read 1 in all three); quaternion ranges in `quat` units with the 'a degree range always passes' warning in one home (controls §3); recipe 5 for two-axis bones; the five new self-review clauses (G-01 separable parts, R-04 convention diff, R-11 chain count, R-13 tool ticket, P-06 named real skeleton); K5 and step 11 verdict sets matching tests.md §6; step 10 workflow route for the posed-plan finding; R15 clavicle and finger claims and the Curve Editor claim as the docs state them (curve-editor.md:26, 41); D-16..D-19 as one-line pointers and the single §5 read-controls row; the eval 1.4 and look_check --min-frac proposal rows]
verdict: fix-first
</spec>
```

## Round-1 findings: status

| Round-1 id | Status | Evidence |
| --- | --- | --- |
| F1 (cap points from ob.data) | fixed | blender-mcp.md:69-73 `cap_count` uses `ob.evaluated_get(dg).to_mesh()`. In my run, the weighted head gave non-zero counts at the tilt. diagnosis.md:49 row added. |
| F2 (degree range on a quaternion channel) | fixed | controls-export-import.md:30 (`quat`, ±sin(θ/2), warning, swing route); tests.md:23, :82-83; diagnosis.md:50. The tool passes `quat` through raw (clip_check.py:381). Swing pass wording: R1 above. |
| F3 (small detached piece not listed) | fixed | tests.md:22 crop and area check; blender-mcp.md crop block. I ran it verbatim (see keep). |
| F4 (five checkable findings with no line) | fixed | tests.md:68 G-01, :82 R-04, :89 R-11, :91 R-13; rigging-design/SKILL.md:116 P-06 and §3 step 6. |
| R1 (SKILL length, repeats) | fixed in part, rest declined with a reason I accept | D-16..D-19 are pointers and the four §5 rows are one row. §7 rules start at byte 18,640 and §8 runs from 19,742 to 23,022. The §1 re-read line and the role file cover compaction, the same as the accepted animator round 2. |
| R2 (VH-07 cell) | fixed | coverage row VH-07 |
| R3 (test clips heading) | fixed | tests.md:36 |
| R4 (RB6 pointer) | fixed | worked-examples.md §2 |
| R5 (K5 verdicts) | fixed | rig-pipeline/SKILL.md:52; rigging-craft/SKILL.md:36 |
| R6 (R15 and Curve Editor claims) | fixed | D-17 evidence; design-for-motion.md §2; motion-needs.md §2; controls §6; checked against curve-editor.md:26, 39-41 |
| R7 (eval 1.4) | fixed (proposal row) | proposals/character-rigger.md last row |
| R8 (workflow owns at P3) | fixed | rigging-design/SKILL.md §3 step 10; G3 proposal row for P3 |
| R9 (orthographic rays) | fixed | blender-mcp.md `ray_origin`; maker run r1-02 |

## Check results

| Check | Result | Notes |
| --- | --- | --- |
| C1 coverage | PASS (63 rows checked, 0 failed) | All 63 rigger IDs in `matrix.md` have a row (scripted). I opened the landed-in locations of the six rows that changed in repair: WT-24, CD-11, PP-09, PP-12, PP-28 and VH-07. Each carries its rule and check. The other 57 rows were checked in round 1, and their locations are the same or carry the same content after the R1 trim. The 9 rejections stay sound. Four cells name a §5 row that was merged (R2). |
| C2 core principles | PASS | `rigging-design` §9 is unchanged except the #6 and #9 checks, which now name R-04 and R-11. No contradiction with `universal-principles.md`. The four "no" rows have sound reasons. |
| C3 self-review | PASS | Every checkable finding has a P-, G- or R-line or a release item. The five round-1 gaps are closed. The lines run with our tools. G-03's input is fixed under C8 (F1, F2). |
| C4 kit rules and engine | PASS | No conflict with AGENTS.md, rules/ or J018 decisions. The engine claims match the mirror. No invented tool mode (`quat` is a label that clip_check passes through, not a mode). |
| C5 nothing valuable lost | PASS | The repair removed only repeats (D-16..D-19 text, four §5 rows), and their content lives in design-for-motion §1-§2. Old lines are kept as in round 1. |
| C6 fixed rules | PASS | Only the owned books changed (evals/ and tripo-routes.md unchanged). Role frontmatter is byte-identical. SKILL.md lengths are 150 / 79 / 104 lines and descriptions 397 / 400 / 374 characters. Only §8 and §9 are new in rigging-design and §8 in rig-pipeline (appended), so nothing is renumbered. The J018 phrase is in all 15 files. No Riot name, library ID or transcript line in the bodies, and no tips section. |
| C7 better work | Better, with two gaps to fix | See below. |
| C8 brief v2 | FAIL (F1, F2) | V1, V2, V4 (n/a), V6, V7 (accepted), V8 and V11 pass. V3: the crop count, recipe 5 and the evaluated-mesh fix give the right answers in my runs. Recipe 1 still gives a false 0 on the cap shape the modeler really makes (F1). V10: recipe 1's `cap` group is never handed over (F2). R1 is a smaller V3/V10 wording gap. |

## Better work (C7)
I read the books as the agent would for eval brief 1: a merged Tripo teddy, a full loop with S4 on the modeler's cut parts. I also checked brief 2, the small fox seen at 12 studs.

With the new books, the rigger writes what the character must read as, screens the design for motion with an owner per finding, and offers the read controls at K2. It poses the plan at the game camera before the modeler builds, and it proves each stage in numbers that now hold in the cases round 1 found false: weighted parts, quaternion hips, and a small figure in a phone frame. For the fox, the crop and area check now catch a detached ear tip or hand that the full-frame count misses, and my run confirmed it. The design SKILL is shorter than in round 1 and repeats itself less.

What remains is in the teddy's S4. The modeler cuts the neck and limbs with Bisect with Fill, so each cap is one n-gon, and nobody puts the caps in a `cap` group. The cap-exposure line G-03 then either stops on a missing group, or, once the agent makes the group, reads 0 on a cap whose exposed side lies away from the sampled patch. That is the seam the line exists to catch. Both fixes are a few lines. After them, the agent's work is clearly better than with the old books, and nothing in the new books makes it worse.

Could not check: the Studio import and in-place captures (no Studio connected); `rig_audit.py` CLI runs on a modeler-made part (the tool did not change since round 1).
