> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `rigging-craft`. Sources: rigging paper RP:429-493 (notes `knowledge/reference/rigging/02-*.md` §6), `tools/rig/rig_audit.py`, fact-check RR. All [O] unless marked.

# Rig tests: S4 geometry acceptance and S5 release

A rig passes only when the Blender tests **and** the Roblox import / playback tests pass for the **same source revision**. A Blender pose the animator liked and an importer success message are two different facts. An item that cannot be run is BLOCKED, never PASS (RP:431). A failure made by a generator is still a failure (RP:452).

## 1. Record format (rig sheet §G)
Per item: PASS / FAIL / BLOCKED / MEASURED · reviewer · source revision · test clip and frame · evidence file · label (gate-verified / MCP-verified / not verified). Numeric thresholds come only from the rig sheet; with no tolerance the verdict is MEASURED (RP:452, 486).

## 2. Measurements (RP:486; `tools/rig/rig_audit.py`)
| Metric | How | Tool function |
| --- | --- | --- |
| Influences ≤ 4, no Root weight, no NaN | per vertex, deform groups only | `audit_weights` (hard FAIL) |
| Unweighted / not-normalized vertices | per vertex | `audit_weights` (reported) |
| Watertight, triangles ≤ 20,000, connected parts | per mesh | `audit_mesh` (hard FAIL on open edges or triangles) |
| Protected-region displacement | max vertex move while one bone sweeps | `sweep` + `max_displacement`; tolerance from §F (0 for rigid pieces with separate meshes, FG10) |
| Rigid shape kept | pairwise distances vs rest | `rigid_drift` |
| Contact hold | end-effector world position and orientation vs the reference, minus deliberate root motion | evaluated matrices (`references/blender-mcp.md`) |
| Seam | continuous seam: boundary positions and normals; overlap seam: visibility and penetration at every extreme, 6 views | renders + `sweep` |

Run inside Blender: `blender -b <file> --python tools/rig/rig_audit.py -- --mesh <M> --armature <A> --root <Root> --protect <group> --sweep <Bone:AXIS:a:b> --tolerance <from §F> --out content/rigs/<id>/tests/audit_<stage>.json`, or from the Blender MCP: add `tools/rig` to `sys.path`, `import rig_audit`, `result = rig_audit.audit_scene(...)`.

**Check budget (owner J005-D8, `rig-pipeline` §4a):** run every pose below as scripted numbers; render and look at images only for poses whose numbers fail, plus ≤ 8 key poses (gameplay camera + one close view). The full 6-view image set is made once, at release.

## 3. S4 proxy sweep (geometry acceptance, before real rigging)
1. Build a temporary rig: one bone per part, pivots from §C, each part 100% on its bone.
2. For each §B ROM extreme and stress pose: pose, render the 6 review views (front, back, left, right, ¾ high, gameplay camera), run `audit_mesh` per part and the seam check.
3. Every failure goes in **one** fix note (`templates/rig/fix-note.md`). Delete the proxy rig afterwards (idempotent stage, RP:548).

## 4. The 12 test clips (S5; RP:437-448)
| # | Clip | Motion | Reveals |
| --- | --- | --- | --- |
| 1 | Rest and reset | neutral; change controls; reset; repeat | hidden offsets, non-identity channels, stale drivers |
| 2 | Joint isolation | move one deform region; protected regions stay still | weight leakage, wrong parents, double transforms |
| 3 | Upper-body envelope | head aim, torso bend, arm raise, cross-body reach, forearm twist | neck / chest skew, shoulder collapse, twist artefacts |
| 4 | Lower-body envelope | step, crouch, leg spread, knee fold, ankle roll (within §B) | hip pinching, bad knee plane, foot dislocation |
| 5 | Contact hold | hold paw / foot / hand contact while the body moves | IK drift, export errors, parent-space mistakes |
| 6 | Locomotion and turn | required gait + start, stop, turn | sliding, timing mismatch, loop seam |
| 7 | Switch | IK/FK and space switches during a real action | pops, offsets, wrong keys |
| 8 | Face | required expressions + combinations sharing regions | lid / lip collision, wrong mapping, leaks |
| 9 | Appendage | opposed tail curves, wing fold / spread, ear motion | too few segments, fused surfaces, interpenetration |
| 10 | Mechanism | full reload / open / steer / suspension / rail cycle | wrong pivots, clearance, rubbery rigid parts |
| 11 | Blend | transitions between approved clips; additive and priority cases | conflicting channels, rest snapping |
| 12 | Runtime crowd and collision | intended instance count, cameras, device, proxies | performance regression, visual / physical mismatch |

Only the clips the asset needs: a door needs 1, 10, 11, 12; a pet usually 1-6, 9, 11, 12. Combine degrees of freedom; single-axis sweeps are not enough (RP:285).

## 5. Release checklist (RP:455-482; 22 items)
**Geometry:** G1 rest silhouette and dimensions match · G2 no fused bridges, open cuts, inverted normals, visible backfaces · G3 caps, overlap, UVs, materials valid through cameras and poses · G4 triangle counts within platform and game budget.
**Skeleton and weights:** SW1 export names, parent map, roots, sockets match the schema · SW2 pivots, bend planes, axes, ROM pass isolation · SW3 weights finite, no unintended unweighted vertices, ≤ 4 influences · SW4 no Root weight, rigid regions keep shape · SW5 protected regions within tolerance in head-only / limb-only motion · SW6 no unapproved collapse, candy-wrapper, spikes, texture stretch, seam exposure.
**Controls and export:** CE1 reset, set pose, IK/FK match, space switch work from the automation interface · CE2 exported motion matches authoring at contacts and extremes · CE3 helpers survive and are driven; nothing authoring-only is required · CE4 profile, units, axes, rest pose, clip names, FPS, ranges recorded · CE5 export re-read into a fresh scene: no missing weights, no stray controls.
**Roblox:** RB1 importer: no unresolved relevant errors, hierarchy kept · RB2 scale, forward / up, rig type, controller, attachments as required · RB3 test clips play on the intended Animator · RB4 collision proxies and VFX / weapon sockets follow the motion independently of the skin (collision does not follow bones, RR12) · RB5 expressions and avatar validation when applicable · RB6 measured crowd cost meets the target-device budget (or BLOCKED: no device) · RB7 animator and modeler accept the in-engine result (S6).
