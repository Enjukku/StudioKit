---
type: template
scope: universal
status: active
updated: 2026-10-21
source: J005 step 1; rigging paper §3 (requirements sheet), §10 (tests); animation paper §2 (motion profile), §12 (cross-craft hand-off)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20

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
    stress_poses: [look up while torso bends]   # combined poses that must hold
    silhouette_must_keep: [ear outline from front]
    sockets_needed: []           # VFX / sound / grip / hitbox points with orientation
  rigger:                        # S2 — how the rig supports it
    route: R-cut                 # R-cut / R-skin / R-mix / R-reject
    why: ""                      # the §B need + the geometry fact that decide it
    joints: [{name: Head, parent: Neck, pivot: "x,y,z (space)", axes: "", limits: "", export: yes}]
    cut: {where: "", why: "", hide_by: collar | socket | overlap | gap | none}
    deformation_zone: {loops_needed: "", protected_regions: [chest]}   # R-skin only
    supported: yes               # yes / with limit (say which) / no + alternative
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
| G2 / G3 | owner | | | decision line |

| Revision | Date | What changed | Retests run |
| --- | --- | --- | --- |
