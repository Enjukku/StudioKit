> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21; revised by J019 P6 maker · claude-opus-5-5 · medium · 2026-10-22 (G3-P6: check 1.4 rewritten)

# Eval briefs for the character-rigger (rig-pipeline + rigging-design + rigging-craft)

Give the agent the brief text and the named files only. A separate grader (Sonnet, high, J005-D4) grades each check pass/fail from the agent's files, not its summary. A brief passes at ≥ 80% of its checks with no "must" check failed. Common checks apply to every run.

| ID | Common check |
| --- | --- |
| R1 (must) | No invented numbers: every ROM, tolerance, budget and bone count has a source (rig sheet, owner, platform doc, measurement) or is marked PROPOSAL / UNKNOWN; no universal bone cap, loop count or joint angle stated as fact |
| R2 (must) | Platform limits right where used: ≤ 4 influences, no Root weight, ≤ 20,000 triangles per mesh, watertight; avatar budgets only for avatar bodies |
| R3 (must) | Route chosen per region (R-cut / R-skin / R-mix / R-reject) with a reason that names the need and the geometry fact; geometry inspected before deciding |
| R4 | Every cut says where, why, what hides it and the extremes it must survive; every bend zone names protected regions |
| R5 (must) | Role boundaries kept: the rigger does not cut or remodel when a modeler / stand-in exists; a look change goes to the lead / owner; notes use the fix-note format with every failed item, evidence and a pass condition |
| R6 | Hand-back in `rules/messages.md` §3 shape: STATUS first, coverage per item, evidence labels (gate / MCP / not verified) |
| R7 (must, when exporting) | FBX exported through `tools/rig/roblox_fbx.py` or with every option named; never Blender defaults |

## 1. Merged Tripo plush biped, full loop (G2 brief)
> A raw Tripo teddy bear (one merged mesh, read-only copy of `DestructionSimulator/content/art/story/models_src/teddy/teddy+bear+3d+model.fbx`). It must walk, wave, look around and sit for a cozy pet game; 8 on screen on phones; third-person camera. Rig it for Roblox. The animator's needs are in `content/rigs/teddy/rig-sheet.md` §B.

| Check | Expected |
| --- | --- |
| 1.1 (must) | S2 inventory names connected parts, open edges and triangles per mesh from a script run, with the evidence file |
| 1.2 (must) | Head, arms, legs routed per region with reasons; stylized-merged default (R-cut first where a cover can hide it) applied or a stated reason to skin |
| 1.3 | Head pivot at the neck base, not the head centre; no bridge neck mesh |
| 1.4 (must) | S4 proxy sweep through every §B extreme with numbers per pose (overlaps, cap exposure, black-fill count); images for failing poses plus ≤ 8 key poses; ≥ 1 real fix note round sent or an explicit "all passed" with evidence (`rigging-craft/references/tests.md` §3 step 2; `rig-pipeline` §4a) |
| 1.5 (must) | `rig_audit.py` report: weights and geometry PASS; head-only sweep with a protected body group; body move reported against the sheet's tolerance |
| 1.6 | Control manifest covers every §B ROM |
| 1.7 (must) | Studio import with Rig Type Custom and Keep Zero Influence Bones decided on purpose; test clips played on an Animator; MCP-verified evidence |

## 2. Quadruped pet with an active tail
> A fox pet that follows the player, sits, and swishes its tail to balance when it turns sharply; ears flick on their own. Small on screen, up to 30 visible. Plan the rig (S2 only); the animator's §B is given below. (Grader gives a §B with ROM for neck, legs, tail base and tip, ears; tail marked "active" for turns.)

| Check | Expected |
| --- | --- |
| 2.1 (must) | Tail rigged as an active primary part (drivable, body responds), not only a lagging chain |
| 2.2 | Ears left / right independent of the head |
| 2.3 | Leg plan names digitigrade / plantigrade with the animator, side-view chain from landmarks, contact pivots |
| 2.4 (must) | Articulation spent where it reads at the camera; budget left as game budget or PROPOSAL to measure with 30 on screen |
| 2.5 | AnimationController + Animator chosen (no Humanoid need) with the deprecation note (use `Animator:LoadAnimation`) |

## 3. Rifle with reload and holster
> A cartoon rifle: magazine drops and is replaced, bolt pulls back, the gun moves from hand to back holster. First- and third-person views. Plan the rig and the control manifest.

| Check | Expected |
| --- | --- |
| 3.1 (must) | Kinematic diagram: fixed frame, moving links, pivots / rails, travel, owner |
| 3.2 | Magazine and bolt separate only because they move; grip and muzzle frames stable; sockets as non-deforming bones kept through export (allowlist; Keep Zero Influence Bones) |
| 3.3 (must) | Hand-to-holster as a space / ownership switch with world-pose matching, not a skin gradient |
| 3.4 | First-person and third-person as separate review targets |

## 4. Diagnose: the chest moves when the head turns
> An animator's rig note says: "Turning the head 40 degrees left drags the upper chest; see `tests/audit_s5.json` (protected group chest_protect, max 0.031 m at vertex 1822) and `renders/head_yaw40_front.png`." Triage and fix.

| Check | Expected |
| --- | --- |
| 4.1 (must) | Follows the debug order: hierarchy and parents, then joint position, then bridges, then weights; does not start by smoothing weights |
| 4.2 | Checks for head weights on chest vertices, a torso bone inheriting from the head, and duplicate deformation |
| 4.3 (must) | Re-runs the same sweep and reports the new number against the sheet tolerance; hand-back per note item |

## 5. Tripo auto-rig candidate for a winged creature
> A Tripo dragon with wings and a tail. Someone suggests "just use Tripo auto-rig". Decide whether and how; you may not call the API without approval.

| Check | Expected |
| --- | --- |
| 5.1 (must) | Names the rig model explicitly (`v2.5-20260210` or `v3.0-20260909`; default `v1.0-20240301` is biped only) and a `rig_type`; runs or requests rig-check first |
| 5.2 (must) | Treats the result as a candidate: same audit as a hand rig, every §B extreme, Roblox round trip |
| 5.3 | Notes no Roblox / R15 naming preset; export names mapped to the rig sheet schema |
| 5.4 (must) | Does not call the Tripo API or spend credits; asks the lead with the cost of doing so |
| 5.5 | Wing type named; fold and spread tested as silhouettes |

## 6. S2 plan for a caped hero with a signature spin (the new S2 stages)
> A third-person hero with a short cape, a high collar and a ponytail; the signature move is a spinning slash that ends in a held pose facing the camera; the wind-up lifts the shoulders. Reference set (front, back, sides, game camera) and the animator's §B records are given. Plan the rig (S2 only), up to K2. New in J019: the rows are not must until a real job has passed them (lead decision J019-LD3).

| Check | Expected |
| --- | --- |
| 6.1 | The design-for-motion screen runs on the reference set including the back and the game camera: the collar (mass on a joint), the cape (drape over the arms, costly part) and the ponytail (costly part) each get an owner (modeler in the S3 brief, art director through the lead, or animator) and a fix; the cape is kept only with a written reason and a rigid or bundled fallback (`rigging-design/references/design-for-motion.md` §1) |
| 6.2 | The read controls are offered at K2 with a reason each: clavicles from the wind-up poses, hips separate from the root, head world orient for the spin, hand shapes where the held pose needs them, one control for each hook-shape part (ponytail, cape tip), quaternion rotation for root, hips and the spin; the animator strikes what the clip list does not need; each kept control goes to the manifest with its range and read need (§2) |
| 6.3 | Pushes use Roblox-safe routes: no scale in clips; a stretch or smear is a swap mesh, a Trail or Beam on a tip socket, or a VFX ring; an extended range only on joints that can take it, with the cut cover or bend zone sized for it (§3) |
| 6.4 | The posed plan at the game camera: the hardest 2-3 combined §B stress poses and the signature held pose on a proxy (or a split copy with one `cap_<cut id>` group per cut); numbers for every pose first (overlap pairs, cap exposure, black-fill pieces) read as screening aids; then at most 4 poses as black-fill and shaded from one pass plus one close view of the worst (§4; rig-pipeline image budget) |
| 6.5 | Every finding from 6.1-6.4 ends as a design-for-motion note, a route change or a limit stated at K2; a "not supported" that changes the look returns needs-decision to the lead (rig-pipeline S2 row, K2) |

## Hidden test (models the skills were not built from)
Run S2 (rig plan only) on two raw Tripo sources the skills never used: `DestructionSimulator/content/art/story/models_src/bunny/cute+bunny+3d+model.fbx` and `.../villain.glb` (read-only copies). The grader scores R1-R6 plus: geometry inspected by script, ≥ 1 fused bridge or open-shell issue found if present, cut list ties to needs, no invented numbers. Pass: ≥ 5 of 6 per model, no must failed.
