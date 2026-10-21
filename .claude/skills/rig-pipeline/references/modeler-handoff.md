---
type: job
scope: universal
status: active
updated: 2026-10-20
source: owner chat 2026-10-20 ("The modeler does the cutting, seam clean-up and any re-modelling ... It may push back with a better cut or a better way to build the part"; "Write its side of the workflow as a planned hand-off in the brief format"); workflow.md S3-S4
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20

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
  - content/rigs/<asset-id>/renders/plan_*.png       # take: the rigger's marked cut lines and zones
fixed:
  parts_to_separate: [<part ids with route R-cut>]          # rig sheet §C, rigger S2
  bend_zones_to_rebuild: [<part ids with route R-skin>]      # rig sheet §C deformation_zone
  rom_each_cut_must_hide_through: per part, rig sheet §B rom   # animator S1
  max_triangles_per_mesh: 20000                              # knowledge/external/roblox-creator-docs/art/modeling/specifications.md:34
  project_triangle_budget: <from rig sheet §E>               # game budget
  watertight: required                                       # specifications.md:35
open: [how each cut is made, capped, socketed or overlapped; topology and loop placement; UV layout; texture re-bake method; counter-proposals]
avoid: [deleting faces to close a shell (opened holes in the first game, F-020); a new neck or bridge mesh between head and body (creased, D-185); flat cuts across exposed skin where no collar or crease hides them; coincident overlapping surfaces (z-fighting)]
owns: [content/rigs/<asset-id>/geometry/]
not_in_scope: [joint plan, bones, weights, ROM changes, animation]
rules:
  - Work on a copy. The source snapshot stays untouched.
  - The rest silhouette and proportions match the approved reference from front, back, both sides, 3/4 and top.
  - A counter-proposal names the rig sheet rows it still meets and is sent back to the rigger before you build it (one round). Disagreement after that goes to the lead.
  - Fill only the modeler keys of the rig sheet.
  - Do your own multi-angle review before hand-back (AGENTS.md §3.5).
  - Hand back with STATUS first and coverage for every listed part (rules/messages.md §3).
deliver: part files in content/rigs/<asset-id>/geometry/ + rig sheet §D rows + review renders
checks:
  - C1: every listed part is watertight (0 non-manifold edges, scripted count)
  - C2: triangles per mesh ≤ 20000 and within the project budget (scripted count)
  - C3: no fused bridge in a moving zone (connected-part count per part matches the plan)
  - C4: rest silhouette matches the reference in the 6 review views (renders attached)
  - C5: every cap and socket is hidden at rest from the 6 review views
  - Check budget (owner J005-D8): your self-check is scripted numbers; render images only where a number fails plus the rest views; the rigger does the full check at S4
return: hand-back to character-rigger, who runs S4 (proxy sweep through every §B extreme) and answers with one fix note or acceptance
</spec>
```
