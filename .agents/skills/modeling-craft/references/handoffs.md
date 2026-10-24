> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `modeling-craft`. Format: `rules/messages.md` (§2 brief, §3 hand-back). Content per receiver: paper notes `03-*.md` §4 (HND ids) [O]; owner 2026-10-21 (receivers). Every packet is files in the asset folder; the message points to them. Revised by J018 maker modeler · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018): read-check evidence per receiver, icon checks (§4), what to ask partners for and when (§6). Revised by J024 writer · claude-opus-5-5 · default · 2026-10-24 (J024 design): hand-off lines for the cut flow (needs in direction, no proof, no check-ins).

# Hand-offs from the modeler

## 1. Every hand-back starts the same way
`STATUS: done | blocked | needs-decision | failed. <one sentence>` then `coverage` (every item in scope: done / not done / skipped), `files`, `checks` with evidence and a label (gate-verified / MCP-verified / not verified), `decisions_made`, `proposals`, `questions`, and **renders made / renders looked at** (light-check rule), the self-review results (`modeling-design/references/review.md` §5), deviations from the reference with reasons, one honest weakness with its next step, and the could-not-check list.

## 2. What each receiver gets
| Receiver | When | Packet (files in `content/models/<asset-id>/` or `content/rigs/<asset-id>/geometry/`) | Brief keys that matter |
| --- | --- | --- | --- |
| **character-rigger** | S3 hand-back (rig-pipeline) | part files as a `.blend` working copy with one `cap_<cut id>` vertex group per cut (`references/rig-parts.md` §2 step 5); rig sheet §D modeler keys; audit json (watertight per part, triangles per part, connected parts vs the plan); the review render set; asset record | answers each cut: accepted / counter-proposal (named §B/§C rows it still meets, one round); C1-C5 of `rig-pipeline/references/modeler-handoff.md` with evidence |
| **animator** | when the animator asks for grip or contact data, or after S3 | grip and contact points, rest pose, part names, the weight class of held items, moving parts with their pivots and travel; nothing that decides motion | fixed: attach names and frames |
| **art director** | read plan (anchors); the reference set; final look when the rule calls its review (the silhouette and value gates are my own in-run self-checks, J024) | approved image id, comparison set at the same angles, the black-fill, grey and phone-size views at the game camera, the Studio capture on the real ground, the read plan, proposed exceptions as two options at the same camera | refs, checks (identity, proportions, value); never unmeasured cost as a reason (HND06) |
| **environment designer** | kit pieces, props, buildings | export files, the kit interface contract, pivots, collision role, size in studs, variants list, import notes, the base or skirt left for ground blending, the in-set capture (or the request for one) | fixed: size, pivot, facing, collision role, kit joins (its brief to the modeler, `environment-craft/references/handoffs.md` §3) |
| **VFX designer** | attach points | one row per point: name, position, orientation (which axis points where), parent part or bone, model revision, exists at rest or follows a bone, emission direction; the model's main colours (hex) so effect colours can sit next to them; when the brief asks, simple shell, ring and swirl meshes with UVs laid for scrolling textures, low in triangles | fixed: names and frames; never let VFX guess from an object origin (HND11-HND12) |
| **UI designer** | icon renders | renders of the **shipped** model: fixed icon camera, light set, material state, magenta `#FF00FF` or transparent background as the UI brief says; a list of what the close view shows that the world view does not; the §4 checks at display size | fixed: camera, light, background; the icon shows the shipped model, never a concept (HND13-HND14) |
| **owner / lead** | G3 | reference next to the model at the same angle; player-scale render; game-camera render and its phone-size view; numbers vs the budget; open trade-offs; one recommendation; the model described as the player meets it; an honest recap | `ste-writing` |

## 3. Attach-point record (VFX, tools, sound anchors)
```text
| name | parent | position (studs, parent space) | look axis | up axis | at rest / follows bone | purpose |
| BladeTip | Sword.Handle | 0, 3.6, 0 | +Y | +Z | at rest | trail start |
```
In Blender: an Empty named exactly as the attachment, parented to the part, its axes set to the look/up axes; in Roblox it becomes an Attachment (the rigger turns bone-following ones into bone sockets). Record the model revision; a new revision re-checks every point.

## 4. Icon render set (UI)
One render per icon size the UI brief names, square, model centred and filling the frame as the UI brief says, the game's light set or a neutral three-light set, background magenta `#FF00FF` for cut-out (reference-images I-09) or alpha if requested (check the alpha channel, not a painted checkerboard). File names `icon_<asset-id>_<size>.png`.
- **Light:** lightest values on the focal anchor, a little darker toward the frame edges; a rim light when the subject sits on a background close in value.
- **What fills the frame:** the identity anchors the read plan marks for the crop, large; the face readable at the crop size; a character's head and upper body, not a small whole figure; the signature pose from the clips when the brief asks; the camera at eye level for friendly subjects, a little lower for dominant ones; form shadows kept (a flat icon reads as a sticker).
- **Checks at the size players see it:** `python tools/art/look_check.py thumb <icon> --key FF00FF --size <display size>` (150x150 for shop and pass icons unless the UI brief says otherwise; `--key FF00FF` on a magenta background, nothing on an alpha one: a head-and-upper-body icon touches the frame edge, so the automatic key finds no flat border and reports `invalid-mask`): the subject is named in one glance and the anchors are visible; circular crops keep the anchors inside the circle; next to its family's other icons it is told apart in black-fill (`look_check.py silhouette <icon> --key FF00FF --compare <other icon>`).

## 5. Asking others (inside the approved brief only)
- Need a new or fixed reference: brief to whoever owns images for the job (often the art director) or make it yourself with `reference-images`.
- Need the owner to run Tripo: the Tripo input pack (`references/tripo-finish.md` §1) through the lead.
- Need a design decision (an invariant must change): `needs-decision` to the lead with two options rendered at the same camera.

## 6. What to ask each partner for, and when (inside the approved brief)
| Partner | Ask for | When |
| --- | --- | --- |
| art director | the identity anchor list and the shape language for a new character, hero or family; the value bands, key light direction and colour roles if the art bible lacks them; a paint-over on your capture when a note is unclear; a decision on any gap that changes the look | read plan (before the blockout); after a review note you cannot turn into one fix |
| character-rigger | the cut list, joint pivots and deformation zones before final topology; a yes or a fallback for every costly part; a posed proxy render when a counter-proposal needs proof | blockout; S3 counter round (one) |
| animator | the stress poses and contact points, the weight class of held items, the signature pose for icons, which hook shapes must face the camera in key poses | read plan for moving models; before icon renders |
| game designer (via the lead) | the model's role, threat or value rank, rarity tiers, what it must never look like | read plan |
| environment designer | the stage's ground and light (a capture or the art bible values), the snap grid and blockout origin, an in-set capture of a placed piece | kit and prop briefs; before the hand-back of kit pieces |
| VFX designer | which emissive areas and attach points it needs, so glow regions stay small and reserved | before the texture passes |
| UI designer | icon sizes, crop shape and background | before icon renders |
