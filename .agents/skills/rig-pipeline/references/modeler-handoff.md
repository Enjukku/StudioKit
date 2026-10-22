---
type: job
scope: universal
status: active
updated: 2026-10-22
source: owner chat 2026-10-20 ("The modeler does the cutting, seam clean-up and any re-modelling ... It may push back with a better cut or a better way to build the part"; "Write its side of the workflow as a planned hand-off in the brief format"); workflow.md S3-S4
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Revised by J018 maker character-rigger · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (design-for-motion findings in refs and fixed keys, static mass in `avoid`, the back game-camera view in C4; repair round 2: the `cap` group in `deliver` and C5; repair round 3: one `cap_<cut id>` group per cut, .blend part files; C1-C5 keep their numbers).

# Planned hand-off: character-rigger → modeler (S3)

This is the brief the `modeler` role (built in J007) receives at S3; its role file and `modeling-craft/references/rig-parts.md` adopt this brief and its checks as-is. If the modeler is not available, the lead runs a stand-in agent (Opus, high) with this brief (J005-D2).

```text
<intent>
The rig plan for <asset-id> needs the parts below as separate, clean pieces (or rebuilt bend zones), so the
character can move through every pose the animator listed with no seam, gap, stretch or body skew. You know
geometry best: choose how each cut is made, capped and hidden, and say so if a different cut or a different
way to build a part meets the same needs better. The approved reference image is the look target; the rest
silhouette must not change. Look through the refs and the rig sheet before you act.
</intent>
<spec>
id: <job-id>-T<nn>
from: character-rigger
to: modeler
model: opus
effort: high                       # roster: high; medium for simple models
skills: [rig-pipeline, modeling-design, modeling-craft, reference-images]
refs:
  - content/rigs/<asset-id>/rig-sheet.md            # take: §B needs, §C route, cut, deformation_zone per part
  - <approved reference image>                      # take: silhouette, proportions, material breaks
  - <source snapshot>                               # take: geometry; never edit it
  - content/rigs/<asset-id>/renders/plan_*.png       # take: the rigger's marked cut lines and zones (back and game camera included)
  - content/rigs/<asset-id>/rig-sheet.md §C design_for_motion   # take: the rigger's design-for-motion findings (rigging-design/references/design-for-motion.md §1)
fixed:
  parts_to_separate: [<part ids with route R-cut>]          # rig sheet §C, rigger S2
  bend_zones_to_rebuild: [<part ids with route R-skin>]      # rig sheet §C deformation_zone
  rom_each_cut_must_hide_through: per part, rig sheet §B rom   # animator S1
  max_triangles_per_mesh: 20000                              # knowledge/external/roblox-creator-docs/art/modeling/specifications.md:34
  project_triangle_budget: <from rig sheet §E>               # game budget
  watertight: required                                       # specifications.md:35
  design_for_motion_findings: [<finding ids with the fix or decision each needs>]   # rigger S2: mass on joints, drapes, costly parts, parts the rig moves, moving parts with room, contact points
open: [how each cut is made, capped, socketed or overlapped; topology and loop placement; UV layout; texture re-bake method; counter-proposals]
avoid: [deleting faces to close a shell (opened holes in the first game, F-020); a new neck or bridge mesh between head and body (creased, D-185); flat cuts across exposed skin where no collar or crease hides them; coincident overlapping surfaces (z-fighting); static mass inside a deformation zone or across a cut; modelled surface detail inside a bend zone that the texture could carry]
owns: [content/rigs/<asset-id>/geometry/]
not_in_scope: [joint plan, bones, weights, ROM changes, animation]
rules:
  - Work on a copy. The source snapshot stays untouched.
  - The rest silhouette and proportions match the approved reference from front, back, both sides, 3/4 and top.
  - A counter-proposal names the rig sheet rows it still meets and is sent back to the rigger before you build it (one round). Disagreement after that goes to the lead.
  - Fill only the modeler keys of the rig sheet.
  - Do your own multi-angle review before hand-back (AGENTS.md §3.5).
  - Hand back with STATUS first and coverage for every listed part (rules/messages.md §3).
deliver: part files as a .blend working copy in content/rigs/<asset-id>/geometry/ (FBX drops vertex groups with no bone), each cap's and socket's faces in a vertex group of its own named `cap_<cut id>` (cut id: the part id of the record whose §C `cut` it is, the child side of the joint, so the cap and its socket share the name; one group per cut, never two cuts in one group; a socket group holds only the faces the child's cap covers at rest: on a closed parent face, cut the child's cap outline into it, or write `socket n/a: closed parent face` in §D `build`), at weight 1 + rig sheet §D rows + review renders
checks:
  - C1: every listed part is watertight (0 non-manifold edges, scripted count)
  - C2: triangles per mesh ≤ 20000 and within the project budget (scripted count)
  - C3: no fused bridge in a moving zone (connected-part count per part matches the plan)
  - C4: rest silhouette matches the reference in the 6 review views and the back game-camera view (renders attached)
  - C5: every cap and socket is hidden at rest from the 6 review views, and its faces are in the `cap_<cut id>` group of its cut, one group for every cut of the part, a socket group only where the child's cap covers it (or `socket n/a: closed parent face` in §D `build`) (the rigger counts them with rigging-craft/references/blender-mcp.md §6 recipe 1)
  - every design_for_motion_findings item is built, or answered with a counter-proposal (one round)
  - Check budget (owner J005-D8): your self-check is scripted numbers; render images only where a number fails plus the rest views; the rigger does the full check at S4
return: hand-back to character-rigger, who runs S4 (proxy sweep through every §B extreme) and answers with one fix note or acceptance
</spec>
```
