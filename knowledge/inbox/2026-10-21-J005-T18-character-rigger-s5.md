---
type: lesson
scope: universal
status: draft
updated: 2026-10-21
source: J005-T18 (character-rigger S4b re-check and S5 build on the teddy pet)
supersedes: []
---
> Author: character-rigger · claude-opus-5-5 · high · 2026-10-21

# Lessons: rigger S5 on a skinned plush (teddy)

Owner correction, word for word (relayed by the lead): "this takes way too much usage, way too much time". The resulting budget: numbers for every pose; images only for failing poses plus up to 8 key poses; no new weight searches unless a check fails.

| # | What happened | Lesson | Evidence |
| --- | --- | --- | --- |
| 1 | A sanity sweep set pose bones to Euler and never restored them. The baked quaternion curves were then ignored, and T05 showed 15° of false foot drift | After any test that changes `rotation_mode`, restore it and assert QUATERNION before you evaluate baked clips | output/rigs/teddy/s5/scripts/build_rig.py (sweep_moves_own_region) |
| 2 | The S5 weight script reimplemented the S4b recipe, but its bandage band was 0.04 where the S4b runs used 0.05 (the sheet text also said 0.04) | Compare the shipped weights vertex by vertex with the accepted evidence's weights (dump + diff); do not trust "same maths" | s5/tests/weights_vs_s4b.json (max difference 0.0 after the fix) |
| 3 | A stricter fold metric (normal vs the weight-blended rest normal) flagged 18-170 close-view px that the accepted §F metric (flipped vs both limb and trunk frames) reads as 0 | Run the metric the sheet names for PASS/FAIL. Report the stricter one as MEASURED, and say which metric each number used | s5/tests/visible_folds_s4bmetric.json vs visible_folds.json |
| 4 | A weight-variant try (smoothstep Z1 blend) left SP3 unchanged and made SP6 worse (28 → 47 px) | Within the budget, one targeted variant is enough to show a fold is not caused by weights; then stop and report | s5/tests/visible_folds_z1smooth.json |
| 5 | Blender re-imports an FBX clip one frame later, and the FBX take is named after the scene | Round-trip compare with the frame offset; set scene.name = clip name before each clip export | s5/tests/roundtrip.json (import_frame_offset 1) |
| 6 | Ungrounded FK test clips push feet below the floor at pelvis roll or drop; with one-bone legs, leg IK holds foot rotation but not position | Measure the floor only on designed poses and report the lift that clears it. Tell the animator early that one-bone legs cannot plant feet under pelvis travel | s5/tests/floor.json, s5/tests/tests_s5.json |
| 7 | Scripted rendering is cheap; looking at images is what costs the owner | Render as many flag images as the numbers need, but look at very few: this task looked at 3 sheets | hand-back J005-T18 |
| 8 | On Windows, Python's default text mode rewrote CRLF/LF and cp1252 bytes in files I edited | Open with `encoding="utf-8", newline=""` for scripted edits of shared Markdown; diff against a backup before you report | rig-sheet.md diff (only rigger rows) |
