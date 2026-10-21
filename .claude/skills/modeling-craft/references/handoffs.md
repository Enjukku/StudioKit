> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `modeling-craft`. Format: `rules/messages.md` (§2 brief, §3 hand-back). Content per receiver: paper notes `03-*.md` §4 (HND ids) [O]; owner 2026-10-21 (receivers). Every packet is files in the asset folder; the message points to them.

# Hand-offs from the modeler

## 1. Every hand-back starts the same way
`STATUS: done | blocked | needs-decision | failed. <one sentence>` then `coverage` (every item in scope: done / not done / skipped), `files`, `checks` with evidence and a label (gate-verified / MCP-verified / not verified), `decisions_made`, `proposals`, `questions`, and **renders made / renders looked at** (light-check rule).

## 2. What each receiver gets
| Receiver | When | Packet (files in `content/models/<asset-id>/` or `content/rigs/<asset-id>/geometry/`) | Brief keys that matter |
| --- | --- | --- | --- |
| **character-rigger** | S3 hand-back (rig-pipeline) | part files on a working copy; rig sheet §D modeler keys; audit json (watertight per part, triangles per part, connected parts vs the plan); the review render set; asset record | answers each cut: accepted / counter-proposal (named §B/§C rows it still meets, one round); C1-C5 of `rig-pipeline/references/modeler-handoff.md` with evidence |
| **animator** | when the animator asks for grip or contact data, or after S3 | grip and contact points, rest pose, part names; nothing that decides motion | fixed: attach names and frames |
| **art director** | reference check, blockout, final look | approved image id, comparison set at the same angles, proposed exceptions as two options at the same camera | refs, checks (identity, proportions); never unmeasured cost as a reason (HND06) |
| **environment designer** | kit pieces, props, buildings | export files, the kit interface contract, pivots, collision role, size in studs, variants list, import notes | fixed: size, pivot, facing, collision role, kit joins (its brief to the modeler, `environment-craft/references/handoffs.md` §3) |
| **VFX designer** | attach points | one row per point: name, position, orientation (which axis points where), parent part or bone, model revision, exists at rest or follows a bone, emission direction | fixed: names and frames; never let VFX guess from an object origin (HND11-HND12) |
| **UI designer** | icon renders | renders of the **shipped** model: fixed icon camera, light set, material state, magenta `#FF00FF` or transparent background as the UI brief says; a list of what the close view shows that the world view does not | fixed: camera, light, background; the icon shows the shipped model, never a concept (HND13-HND14) |
| **owner / lead** | G2 sample, G3 | reference next to the model at the same angle; player-scale render; game-camera render; numbers vs the budget; open trade-offs; one recommendation | `ste-writing` |

## 3. Attach-point record (VFX, tools, sound anchors)
```text
| name | parent | position (studs, parent space) | look axis | up axis | at rest / follows bone | purpose |
| BladeTip | Sword.Handle | 0, 3.6, 0 | +Y | +Z | at rest | trail start |
```
In Blender: an Empty named exactly as the attachment, parented to the part, its axes set to the look/up axes; in Roblox it becomes an Attachment (the rigger turns bone-following ones into bone sockets). Record the model revision; a new revision re-checks every point.

## 4. Icon render set (UI)
One render per icon size the UI brief names, square, model centred and filling the frame as the UI brief says, the game's light set or a neutral three-light set, background magenta `#FF00FF` for cut-out (reference-images I-09) or alpha if requested (check the alpha channel, not a painted checkerboard). File names `icon_<asset-id>_<size>.png`.

## 5. Asking others (inside the approved brief only)
- Need a new or fixed reference: brief to whoever owns images for the job (often the art director) or make it yourself with `reference-images`.
- Need the owner to run Tripo: the Tripo input pack (`references/tripo-finish.md` §1) through the lead.
- Need a design decision (an invariant must change): `needs-decision` to the lead with two options rendered at the same camera.
