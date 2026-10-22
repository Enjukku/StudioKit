> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `rigging-design`. Sources: rigging paper RP:294-338 (notes `knowledge/reference/rigging/02-*.md` §2-3), animation paper AP:222-264 (notes `knowledge/reference/animation/01-*.md` §5.3), fact-check RR. All rows [O] unless marked. Revised by J018 maker character-rigger · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (invented creatures, several forms, moving parts with room, strain range, faces built to move).

# Non-humans, pets, mechanisms, vehicles, weapons, faces

## 1. Creatures
| Body | Rig decisions | Tests | Source |
| --- | --- | --- | --- |
| Quadruped | Separate shoulder mass, front-limb chain, pelvis / hind-limb chain, paws or hooves, neck, spine. Side-view chain from skeletal landmarks and contact reference. Decide plantigrade / digitigrade / hoof with the animator; a raised hock is not a backwards knee; do not guess the bend plane from fur | stance hold while the body moves; step; crouch; head turn | RP:296 |
| Pet | Spend articulation where it reads at the game camera: head attitude, torso bounce, ear and tail silhouette, paw contact, face. Some pets need only a rigid bobbing body and turning head. Export joints may be fewer than control joints | camera test at game size; measured crowd cost on the target phone | RP:298 |
| Tail, tentacle, snake | Enough lengthwise geometry and distributed joints for the needed curve; neutral rest that bends both ways. Per segment: keyed, spline-authored (baked) or runtime secondary. A Blender spline constraint is not a Roblox solver | base rotation; opposed curves; tip motion; neighbouring appendages | RP:300 |
| Many tentacles | Group dense central ones, keep tips separate, economical joints [V legacy Roblox case] | silhouette at camera | RP:302 |
| Active tail (balance, steer, grip, signal) | Controls that drive it as a primary part while the body responds; no "always lags" setup [V gecko tails, B05] | tail-led action with body response | AP:228 |
| Bird wing | Decide shoulder / elbow / wrist, feather spread, fold, body transition. Membranes and soft transitions skinned; feather groups rigid where shape must hold. Wing, body and tail controllable together [V pigeon B06] | full spread and full fold as silhouettes; glide is not a frozen flap [V B10] | RP:304; AP:234-238 |
| Bat wing | Left and right retract independently (asymmetric retraction turns the body) [V B07, B08]; membrane skinned | fold, extension, asymmetric retraction | AP:236 |
| Insect wing | Pick the real stroke family first; very fast strokes need a render / blur plan, not a slowed bird flap [V B09] | sampling check at 30 and 60 fps | AP:214 |
| Mixed dragon | Document which anatomy supplies which reference; do not mix bird angles, bat roosting and insect frequency into one "measured" profile | — | AP:240 |
| 6 or 8 legs | Written leg order, side convention, ground-contact map; no cross-limb IK target mix-ups. Real gaits are species-, speed- and substrate-specific hypotheses [V B12, B13] | stance feet hold in world space | RP:304; AP:244-250 |
| Ears, antennae, fins | Left / right independent of the head [V cat ears B16]; antennae active + passive [V B17]; fin rays need not bend as one paddle [V B18] | independent motion test | AP:215-218 |
| Invented creature | Name a real animal (or human) source per body part and place each joint from that source's skeleton (a lion's face, a bear's pelvis, an insect's arms); an invented part with no real source gets a question to the art director first | each part's joints bend like its source | [O] |
| Scary creature-humanoid | Threat lives in proportion and pose: give the hunched, low and reaching poses their full range so it never reads silly | the threat poses as black-fill at the game camera | [O] |
| Several forms (a transformation) | Each form is its own rig sheet and rig; a shared skeleton only where the forms really share joints | each form passes its own tests | [O] |

## 2. Mechanisms, vehicles, weapons
- Start every mechanism with a **kinematic diagram**: fixed frame, moving link, pivot or rail axis, travel envelope, parent, physical owner (RP:306).
- Wheels rotate about the axle centre; steering about the steering axis; suspension along its linkage or a stated visual simplification; doors on the hinge line, not the mesh centre; sliders along a rail; turrets split yaw and pitch frames; pistons have endpoints, linked travel and clearance checks (RP:308).
- Rigid metal uses rigid transforms. A rubbery door means wrong weights or the wrong representation (RP:308; do not repaint a rigid hinge, P06).
- Weapons: stable grip and muzzle frames; separate magazine, bolt, trigger, hammer or attachments only where they move; reload detachment and hand switching are hierarchy or ownership changes, not skin gradients (RP:306). First-person and third-person are separate review targets; a viewmodel rig may be separate (AP:442).
- Visual rig ≠ physics. A bone-driven wheel is not a physics wheel. Roblox constraints, proxies and collision are specified separately; collision does not follow bone deformation [V RR12] (RP:310).
- Moving parts need room: nesting cross-sections and a travel path cleared of the arms and body (a barrel slides, a stock retracts past the shoulder, a blade opens away from the hand); decoration that blocks the travel goes back to the modeler at S2.
- Contact points (grip, stock-to-shoulder, seat, hand positions) stay identical in every variant, with clearance so hands do not clip; variants keep the base sockets.
- A part that must show strain before it breaks, snaps or opens (a shield, a lid, a trap jaw) gets a small range of its own when §B asks for a building tell; the rig gives the range, the animator keys the tell.
- Test: full mechanism cycle (reload, open, steer, suspension, rail), clearances, collisions (RP:446): overlap pairs between parts that are not parent and child stay 0 through the cycle (`rigging-craft/references/blender-mcp.md` §6).

## 3. Faces
| Face type | Use when | Must have |
| --- | --- | --- |
| Texture swap | deliberately graphic faces, discrete expressions | UV layout, expression ids, textures, hold time, reset state, runtime swap path; test on the curved head at camera distance; no coplanar duplicate face cards (RP:321-323) |
| Skeletal face | lids, brows, mouth, jaw or gaze must move smoothly | jaw, lips, lids, eyes isolated so each moves alone (RP:327) |
| Mixed | rigid eyeballs and teeth, skinned lids and lips | as above |
| Roblox dynamic head [V] | avatar-compatible expressive heads | skinned face joints, FACS poses mapped to frames: 50 base poses, 17 required to sell, neutral at frame 0, one pose per frame; keep face joints under 50 where possible; FaceControls (RR15-RR17, RR34) |

- A painted mouth line has no mouth cavity: remodel, swap a graphic, or use a deliberately simple jaw (RP:327).
- Model what the rig moves: a mouth that must open has circular loops round the lips and opens without tearing; eyelids have enough lines to close (blinks on fast head turns need them) [V] `art/characters/creating/modeling-best-practices.md` (mouth and eye edge flow). Flag a sewn-shut mouth at S2, not after weights.
- Dynamic-head face animation is made in Studio (Face Animation Editor or animation capture); face animations cannot be imported [V] `art/characters/facial-animation/animate-heads.md`. The rig delivers the FACS-mapped head; the animator keys the face in Studio.
- 50 FACS poses are not 50 bones; the required expression count is not a joint count (RP:331).
- Blender shape keys are not a confirmed dynamic-head input; use the documented joint-pose mapping (RP:331, unresolved).
- A face the owner already likes is locked: a new face rig must match it side by side before it replaces it [E FG13].
- Face tests: neutral, eye close and gaze, smile and frown, jaw open, needed speech shapes, and combinations sharing lid / cheek or mouth regions; check lid contact, lip closure, teeth penetration, no weight leak into the neck (RP:329).
