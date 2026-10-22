> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `rigging-craft`. Sources: rigging paper RP:429-493 (notes `knowledge/reference/rigging/02-*.md` §6), `tools/rig/rig_audit.py`, fact-check RR. All [O] unless marked. Revised by J018 maker character-rigger · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (numbers-first S4 sweep, test clips 13-14, the S4 and S5 self-review lines in §6; every command named here was run on Blender 5.1.2 headless on a synthetic proxy rig, 2026-10-22; repair round 1: evaluated-mesh caps, the crop count, quaternion ranges, five review lines extended; repair round 2: caps of any face shape, the `cap` group checked before the sweep, the swing pass in degrees; repair round 3: one `cap_<cut id>` group per cut; repair round 4: sockets only where the child covers them, numbers as screening aids).

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
| Cap exposure | per §C cut of the part, points inside every triangle of every face in that cut's `cap_<cut id>` group (one group per cut: a group holding both rims of a part counts the side faces between them; a socket holds only the parent's faces the child's cap covers at rest: on a closed parent face, cut the child's cap outline in or record the socket n/a and count the child's cap; any face shape: a Bisect-with-Fill n-gon, a quad, a triangle fan, a concave cap), on the **evaluated** (posed) mesh, ray-cast from each review camera (parallel rays for an orthographic one): count of points whose first hit is the cap itself; 0 at rest and at every extreme, with points sampled for every cut (a missing group stops the count; a group with no whole cap face samples 0 points: never a pass) | `references/blender-mcp.md` §6 recipe 1 |
| Part overlap | overlapping face pairs between parts that are not parent and child, world space, at each pose; compared with the rest count | `references/blender-mcp.md` §6 recipe 2 |
| Read at the game camera | black-fill render of the pose at the game camera; `python tools/art/look_check.py silhouette <png>` on the full frame for the figure's box (a box touching the frame edge means a cropped figure: reframe, every number is wrong); the component count (a detached piece adds one) on a crop of that box plus a 10 % margin, compared with rest measured the same way, and trusted only when the listed components' areas add up to the mask area (`look_check.py` lists only pieces of 0.5 % of the image or more; when the areas do not add up, render the count frame closer at the same angle) | `animation-craft/references/blender-keying.md` §7; `look_check.py`; crop: `references/blender-mcp.md` §6 |
| Control range, contact hold, flips | sampled test clip: `python tools/anim/clip_check.py <samples.json> --manifest <manifest.json> --tol <tol.json> --up z`: rom (over-range per control; quaternion channels in `quat` units, `references/controls-export-import.md` §3; a quaternion bone that turns about two axes in the clip: swing, recipe 5), contact_slide (planted foot or grip), pops (frame-to-frame acceleration ratio per landmark) | `clip_check.sample_clip` inside Blender; `references/blender-mcp.md` §6 recipe 5 |
| Head hold | the head's rotation difference from the clip's first frame, per frame, on the authoring rig, the baked export skeleton and the FBX re-import (compared by clip frame) | `references/blender-mcp.md` §6 recipe 3 |
| Scale keys | scale F-curves with any key other than 1.0 in every export clip's Action: none (a bake's constant-1 scale channels are harmless) | `references/blender-mcp.md` §6 recipe 4 |

Run inside Blender: `blender -b <file> --python tools/rig/rig_audit.py -- --mesh <M> --armature <A> --root <Root> --protect <group> --sweep <Bone:AXIS:a:b> --tolerance <from §F> --out content/rigs/<id>/tests/audit_<stage>.json`, or from the Blender MCP: add `tools/rig` to `sys.path`, `import rig_audit`, `result = rig_audit.audit_scene(...)`.

**Every number in this table is a screening aid.** The known false readings of each recipe and of `look_check.py` and `clip_check.py` stand next to them in `references/blender-mcp.md` §6. Known false readings of `rig_audit.py`: a protected group that stops short of the planned transition passes with max 0.0 while the chest moves; an active Action can override the swept value (clear it before a sweep); `non_deform_groups_with_weight` lists the `cap_*` and protected groups and still passes (information, not a fault). A FAIL or a borderline number is checked by eye on the still of that pose and camera before it goes in a fix note, and a pass in a known-false case is checked the same way. No fix note goes out on a number alone.

**Check budget (owner J005-D8, `rig-pipeline` §4a):** run every pose below as scripted numbers; render and look at images only for poses whose numbers fail or fall in a known-false case, plus ≤ 8 key poses (gameplay camera + one close view). The full 6-view image set is made once, at release.

## 3. S4 proxy sweep (geometry acceptance, before real rigging)
1. Build a temporary rig: one bone per part, pivots from §C, each part 100% on its bone. Check that every §C cut of each part has its own `cap_<cut id>` group holding that cut's cap or socket faces (the modeler delivers them in a .blend; for a flat cap with none, `references/blender-mcp.md` §6 `mark_plane_caps` builds it from that cut's plane, once per cut; a socket dome with none is a fix-note item; a socket on a closed parent face is marked with `child=`, so only the area the child covers counts, or recorded n/a in §C).
2. For each §B ROM extreme and stress pose, numbers first: `audit_mesh` per part, cap exposure from the 6 review cameras (front, back, left, right, ¾ high, gameplay camera), part overlap against the rest count, and the game-camera black-fill measured by `look_check.py silhouette` (rendered, not looked at). Then images: the 6 views only for poses whose numbers fail, plus ≤ 8 key poses at the gameplay camera and one close view (§6 G-06).
3. Every failure confirmed by eye on its still goes in **one** fix note (`templates/rig/fix-note.md`). Delete the proxy rig afterwards (idempotent stage, RP:548).

## 4. The test clips (S5; RP:437-448; 13-14 added in J018)
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
| 13 | Spin hold | the body turns 180° (or the §B spin) under a head held by the world-orient switch; the switch toggled at rest | head drift, a switch that moves the head at rest, a hold lost in the bake or the re-import |
| 14 | Wind-up and landing | the §B wind-up (clavicles raise and tighten, hips sink), throw or jump take-off, and the landing sink | missing shoulder or hip range, shoulder collapse at the top of the range, hip pinch at the bottom |

Only the clips the asset needs: a door needs 1, 10, 11, 12; a pet usually 1-6, 9, 11, 12; a character with a world-orient switch or a wind-up need also 13 and 14. Combine degrees of freedom; single-axis sweeps are not enough (RP:285). Ship clip 5 and a ROM sweep clip with the rig: the animator runs them again at S6.

## 5. Release checklist (RP:455-482; 22 items)
**Geometry:** G1 rest silhouette and dimensions match · G2 no fused bridges, open cuts, inverted normals, visible backfaces · G3 caps, overlap, UVs, materials valid through cameras and poses · G4 triangle counts within platform and game budget.
**Skeleton and weights:** SW1 export names, parent map, roots, sockets match the schema · SW2 pivots, bend planes, axes, ROM pass isolation · SW3 weights finite, no unintended unweighted vertices, ≤ 4 influences · SW4 no Root weight, rigid regions keep shape · SW5 protected regions within tolerance in head-only / limb-only motion · SW6 no unapproved collapse, candy-wrapper, spikes, texture stretch, seam exposure.
**Controls and export:** CE1 reset, set pose, IK/FK match, space switch work from the automation interface · CE2 exported motion matches authoring at contacts and extremes · CE3 helpers survive and are driven; nothing authoring-only is required · CE4 profile, units, axes, rest pose, clip names, FPS, ranges recorded · CE5 export re-read into a fresh scene: no missing weights, no stray controls.
**Roblox:** RB1 importer: no unresolved relevant errors, hierarchy kept · RB2 scale, forward / up, rig type, controller, attachments as required · RB3 test clips play on the intended Animator · RB4 collision proxies and VFX / weapon sockets follow the motion independently of the skin (collision does not follow bones, RR12) · RB5 expressions and avatar validation when applicable · RB6 measured crowd cost meets the target-device budget (or BLOCKED: no device) · RB7 animator and modeler accept the in-engine result (S6).

## 6. Self-review lines at S4 and S5 (run before each hand-back; the S2 lines are `rigging-design` §8)
Write each line as PASS, FAIL, MEASURED, not verified or n/a with its evidence. **Input:** N = numbers (scripts, `rig_audit.py`, `clip_check.py`, `look_check.py` on renders nobody looks at); K = key images you look at, inside the budget below; C = Studio MCP captures. Say what each input can prove: a still proves a pose, not timing; Studio MCP captures are stills; feel at normal speed and phone cost need the owner's preview or a device. A line whose input cannot show it is "not verified", never PASS.

### S4 geometry acceptance (proxy sweep on the modeler's parts)
| ID | Look for | In |
| --- | --- | --- |
| G-01 | Every part watertight, triangles within the platform limit and the game budget, connected-part count equal to the plan; every separable or swappable part (helmet, weapon, removable armour, a skin's swap piece) its own named object or MeshPart | N (`audit_mesh`, object list) |
| G-02 | At every §B extreme and stress pose: no new overlap between parts that are not parent and child (a hand in the helmet, a collar in the jaw, a barrel through the arm); each remaining pair has a decision | N (recipe 2) |
| G-03 | Cap exposure 0 from every review camera, at rest and at every extreme, per §C cut of each part, on every face of that cut's `cap_<cut id>` group (one group per cut; points over each face's triangles, never only the face centre; every cut of the part has its group, with a sampled count above 0; a socket holds only what the child covers at rest, or is n/a on a closed parent face; a FAIL is checked on its still first) | N (recipe 1), K for a FAIL |
| G-04 | Each rigid part keeps its shape with its parent held still; unrelated parts stay still | N (`rigid_drift`, `max_displacement`) |
| G-05 | Game-camera black-fill per pose: component count equal to rest, counted on the crop with the area check of §2 (Read at the game camera); the figure's box inside the frame | N (`look_check.py silhouette`) |
| G-06 | Failing poses and ≤ 8 key poses (the signature pose, the tell, the hardest stress pose, the widest wind-up) at the game camera plus one close view: seams hidden; limbs, hands, head and feet separate; identity anchors and hook shapes visible from the side the camera sees; nothing hanging over the arms; the signature pose shows one dominant line of action | K |
| G-07 | Every design-for-motion finding of the plan is resolved in the geometry or carries a decision | N (rig sheet, the modeler's MO results) |

### S5 release (the real rig)
| ID | Look for | In |
| --- | --- | --- |
| R-01 | Rest and reset return exactly; every switch toggled at rest moves nothing (the head world-orient switch: 0°) | N |
| R-02 | Isolation: protected groups reach the start of each planned transition; largest protected move ≤ the sheet's tolerance in every sweep | N (`rig_audit.py --protect --sweep --tolerance`) |
| R-03 | Envelope and combined stress poses on the real rig: the G-02, G-03 and G-05 numbers hold | N |
| R-04 | The manifest holds every kept read control with its range, keying policy and the need it serves: clavicles (or upper torso) and hips, head world-orient, hand shapes, one control per hook-shape part, chain base controls; quaternion channels named by index, with `quat` ranges (±sin(θ/2)); each channel matches its bone's rotation mode; names, axes, sides and sockets diffed against the game's earlier rig manifests (`content/rigs/*/control-manifest.json`): no conflicting use | N (manifest, diff) |
| R-05 | Wind-up clip (test 14): `clip_check.py` rom inside the manifest range for the clavicle and hip controls, and the clip reaches the §B wind-up range; a quaternion control that also turns about a second axis in the clip measured by recipe 5 swing against θ in degrees, as its validation query says | N |
| R-06 | Spin clip (test 13): head drift ≤ the sheet's tolerance (MEASURED without one) on the authoring rig, after the visual-key bake and after the FBX re-import, compared by clip frame | N (recipe 3) |
| R-07 | Contact-hold clip (test 5): `clip_check.py` contact_slide ≤ the sheet's tolerance with the IK feet planted while the hips move | N |
| R-08 | Spin and sweep clips: `clip_check.py` pops ≤ the sheet's tolerance, with at least one landmark off each spin axis | N |
| R-09 | No scale key other than 1.0 in any export clip; every push past real ships through its named route (swap mesh, separate part, VFX socket) | N (recipe 4) |
| R-10 | In Studio, the key poses of G-06 captured at the game camera in the real place (≤ 8 captures): the same reads hold; MCP-verified | C |
| R-11 | Variants and skins: sockets and contact points equal the base within the sheet's tolerance; every secondary chain of the base present (chain count ≥ the base: a premium variant never loses a moving part); the base clips play with no hand or body clipping (G-02 numbers at the swing and use extremes) | N |
| R-12 | The 22 release items of §5 recorded with labels | N |
| R-13 | Renders made and images looked at counted; the could-not-check list; one honest weakness with its next step; a step repeated by hand on a third asset has a tool ticket in the proposals | N |

### Image budget (owner J005-D8; `rig-pipeline` §4a)
- Numbers for every pose and clip (G-01..G-05, R-01..R-09, R-11): renders measured by a tool count as renders made, not images looked at.
- S2 posed plan: at most 4 poses at the game camera (black-fill and shaded from one pass) plus one close view; route options: one black-fill per option at the worst pose (`rigging-design` §8 P-05, P-11).
- S4: images only for failing numbers plus ≤ 8 key poses (G-06). S5: the full 6-view image set once, at release; in Studio ≤ 8 key-pose captures (R-10).
- No exploratory variants (weights, overlap depths) unless a number fails; then bracket one value (too low, too high), pick between, and stop at the first that passes.

