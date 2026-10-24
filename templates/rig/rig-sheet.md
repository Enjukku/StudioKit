---
type: template
scope: universal
status: active
updated: 2026-10-22
source: J005 step 1; rigging paper §3 (requirements sheet), §10 (tests); animation paper §2 (motion profile), §12 (cross-craft hand-off); J019 P6 (G3-P6): slots for `rig-pipeline` §3 K1/K2, `rigging-design/SKILL.md` §3 steps 1, 4, 6, 8, 10 and `rigging-craft/references/tests.md` §4, §6
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20; revised by J019 P6 maker · claude-opus-5-5 · medium · 2026-10-22 (G3-P6)

# Rig sheet: <asset-id> · revision <n>

Workflow: `rig-pipeline` skill. Copy to `content/rigs/<asset-id>/rig-sheet.md`. Blank = unresolved, never "unlimited". Every number has a unit and a source (owner D-id, platform doc file:line, reference id, measured file, or PROPOSAL). Each role writes only its own keys (`animator:` / `rigger:` / `modeler:`); others comment in §H, never edit.

## A. Asset (lead, S0)
| Key | Value |
| --- | --- |
| asset_id / revision | |
| purpose | avatar body / custom player / NPC / pet / weapon / vehicle / moving prop |
| approved reference image | path + decision line |
| model source | hand-made (Blender file) / Tripo task id + generation model version / other |
| source snapshot | path + hash (never edited) |
| camera and size on screen | third person / first person / both; typical distance in studs |
| target device; max visible at once | e.g. low-end phone (named model); count |
| runtime driver | Humanoid + Animator / AnimationController + Animator / Motor6D scripted / tween only / UNKNOWN |
| movement owner | in-place clips, controller moves the root (default: in-place clips; root motion is not released, fact-check RR39-RR41) |
| physics and collision | collision proxy parts; detachable pieces; what physics owns |
| units and axes | studs; forward / up as tested in the import profile |
| tools and versions | Blender build; add-ons; MCP server; Studio build |

## B–D. Parts (one record per part or region; same part IDs everywhere)
| Key | Value |
| --- | --- |
| animator: feel words (motion profile TP01) | |
| rigger: role read, movement pattern, game camera and distance (`rigging-design/SKILL.md` §3 step 1) | |

```yaml
- part: P01                      # stable id, used in notes, tests, clips
  name: head
  animator:                      # S1 — what moves, how far, how
    what_it_is: skull + ears + hair tuft      # semantic label, not the bone name
    moves: yes                   # yes / no / only with parent
    driver: active               # active (intent, gaze, balance, steering) / passive (follows, settles) / rigid (rides parent) / mechanical
    rom:                         # every axis the action list needs; unit + the pose or clip that needs it + source
      - {axis: yaw, range: "-60..60 deg", needed_by: idle look-around, source: PROPOSAL}
    own_motion_parts: []         # parts that need their own motion inside this region (ears, jaw, eyes)
    contacts: []                 # planted / gripped / hinge contacts this part keeps
    stress_poses: [look up while torso bends]   # combined poses that must hold; include costume near joints (`animation-design/references/body-and-species.md` §1)
    standard_needs:              # rig-pipeline §3 K1; each: {needed: yes, pose: <pose or clip>} or not needed
      wind_up_range: not needed  # shoulders and hips for wind-ups, throws, jumps, landings
      head_world_orient: {needed: yes, pose: spin attack}   # head holds its world direction through a spin
      hand_shapes: not needed    # hand or finger shapes where hands must read
      hook_shape: {needed: yes, pose: ear tuft toward camera on the idle hold}   # each hook-shape part the camera must see
    silhouette_must_keep: [ear outline from front]
    sockets_needed: []           # VFX / sound / grip / hitbox points with orientation
  rigger:                        # S2 — how the rig supports it
    route: R-cut                 # R-cut / R-skin / R-mix / R-reject
    why: ""                      # the §B need + the geometry fact that decide it
    joints: [{name: Head, parent: Neck, pivot: "x,y,z (space)", axes: "", limits: "", export: yes}]
    cut: {where: "", why: "", hide_by: collar | socket | overlap | gap | none}
    deformation_zone: {loops_needed: "", protected_regions: [chest]}   # R-skin only
    supported: yes               # yes / with limit (say which) / no + alternative
    design_for_motion:           # S2 step 4 (`rigging-design/SKILL.md` §3; screen: `rigging-design/references/design-for-motion.md` §1)
      - {id: DFM01, finding: "", owner: modeler, fix_asked: "", pose: ""}   # owner: modeler / art director (through the lead)
    read_controls:               # S2 step 6 (`design-for-motion.md` §2); one per standard need marked needed
      - {control: "", range: "", serves: ""}   # serves: the §B need, e.g. head_world_orient
    push_route:                  # S2 step 8 (`design-for-motion.md` §3); never clip scale
      - {push: "", route: ""}
  modeler:                       # S3 — how the geometry delivers it
    cut_response: accept         # accept / counter (with reason + the §B/§C rows it still meets)
    build: ""                    # how the cut is made, capped, socketed; retopology; UV and texture work
    triangles: 0
    status: todo                 # todo / done / fix-round-1 / fix-round-2
```

## E. Budgets (rigger fills, sources required)
| Item | Limit | Source | Actual |
| --- | --- | --- | --- |
| triangles per mesh | ≤ 20,000 (platform ceiling) and game budget | specifications.md:34; game profile | |
| triangles total | game budget or PROPOSAL | | |
| influences per vertex | ≤ 4 | specifications.md:59 | |
| Root weights | 0 | specifications.md:60 | |
| deform / control / export bones | game budget or PROPOSAL (no universal cap) | | |
| materials and textures | game budget | | |
| measured phone cost at max visible count | target from game profile | | not measured |

## F. Test plan (rigger, from §B)
| Test | Parts | Poses / extremes (from §B) | Pass rule (unit, view) |
| --- | --- | --- | --- |
| rest and reset | all | | returns to rest exactly |
| isolation (protected regions stay still) | | | max vertex move in protected region ≤ <tolerance> |
| upper / lower envelope | | | |
| combined stress poses | | | |
| posed plan at the game camera (S2 step 10; `rigging-design/SKILL.md` §8 P-11) | | hardest 2-3 stress poses + signature pose | overlaps, cap exposure, black-fill components vs rest |
| spin hold (test clip 13; `rigging-craft/references/tests.md` §6 R-06) | head | §B spin | head drift ≤ <tolerance> after bake and re-import |
| wind-up (test clip 14; `tests.md` §6 R-05) | clavicles / upper torso, hips | §B wind-up range | rom inside the manifest range, reaches the §B range |
| contact hold | | | end point drift ≤ <tolerance> |
| appendage (tail, wings, ears) | | | |
| mechanism (weapon, door, wheel) | | | |
| seam cover (R-cut parts) | | every §B extreme, 6 review views | no cap, gap or backface visible |
| Roblox round trip | all | test clips on the intended Animator | hierarchy, scale, axes, clips match |

## G. Test record (rigger, S4–S5)
| Test | Result PASS / FAIL / BLOCKED | Evidence file | Label (gate / MCP / not verified) | Date |
| --- | --- | --- | --- | --- |

## H. Sign-offs, notes, change log
| Step | Who | Result | Date | Note / ticket |
| --- | --- | --- | --- | --- |
| K1 needs complete | rigger | | | |
| K2 plan covers needs | animator | | | |
| K3 geometry self-check | modeler | | | |
| S4 geometry accepted | rigger | | | |
| K5 rig tested | rigger | | | |
| S6 rig accepted | animator | | | |
| G3 (J024: no G2) | owner | | | decision line |

| Revision | Date | What changed | Retests run |
| --- | --- | --- | --- |
