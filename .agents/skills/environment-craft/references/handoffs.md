> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit reference: universal. J008. Format: `rules/messages.md` §2 (`<intent>` prose, then `<spec>` keys). What each role owns: `environment-design` §1 (CO04 O). First-game brief practice: `knowledge/reference/environment/04-first-game-stages.md` FS-H03, FS-P14. Every brief: the why in prose; exact values only with a source; the craft left open; every rule restated; one runnable check per acceptance rule.

# Hand-off briefs from the environment designer

Send each brief whole, in one message, as a ledger ticket. If the role is still planned (not built), the brief goes to the lead. Build each brief from files: point to paths, never paste large content.

## 1. To the game designer: a layout proposal
```text
<intent>
<What the player would gain, which decision point or route it touches, and why the art pass alone cannot fix it.>
</intent>
<spec>
id: <job>-T<nn>
from: environment-designer
to: game-designer
skills: [level-design]
refs: [content/stages/<stage>/blueprint.md §F (node), review/<camera ids> (evidence)]
fixed: {route_graph_revision: <rev>  # game designer}
open: [accept, change or reject the proposal]
proposal: <the change, with measured lengths in studs and walk-time effect at the game's walk speed>
not_in_scope: [art changes that keep the route (the environment designer does those)]
rules: [Routes, cover, encounter timing and pacing are the game designer's; nothing changes until they answer.]
deliver: reply in the ticket with the decision
checks: [C1: the decision names the node id and the new route-graph revision if accepted]
return: STATUS + decision
</spec>
```

## 2. To the art director: a look review
Intent: which place, which reference, what feeling is wanted, where it drifts. Spec: `refs` = review packet, camera ids at low and high quality, the reference images, art bible version; `open` = the art director's judgment and fixes; ask them to classify each drift (large shape, framing, value hierarchy, material response, camera / exposure / tier) before suggesting a fix (CO07 O); `checks` = each note names the camera, the defect, the intended reading and the layer.

## 3. To the modeler: a new asset
| Key | What to give |
| --- | --- |
| intent | what the piece does in the place (landmark, route cue, dressing with a story, kit piece) and how it is seen (distance, camera, how many) |
| refs | approved reference image (`reference-images`), the blueprint sheet with the player figure, neighbouring kit pieces |
| fixed | size in studs with its source (scale sheet), pivot location and the surface it rests on, collision role (walkable, blocker, none), facing (main face toward the route), attach points for VFX or sound anchors, kit joins if it is modular |
| open | how it is modelled, topology, UVs, materials within the art bible |
| rules | 20,000 triangles per mesh is a cap, not a target; budgets from the owner or a measurement; finished on every face players can see; real scale against the player |
| checks | imports at the stated size and pivot with the project export recipe; renders front, back, sides, 3/4 beside the reference |

## 4. To the sound designer: the ambience
```text
<intent>
<For each zone: what the player should feel and work out. Example: the falls are a clue before the turn, still there at the overlook, and duller inside the cave.>
</intent>
<spec>
id: <job>-T<nn>
from: environment-designer
to: sound-designer
skills: [sound-design]
refs:
  - content/stages/<stage>/ambience-map.md   # take: zones, sources, causes, blends, states, checkpoints
  - review/<camera ids>                      # take: each source's visible cause
fixed:
  zone_ids: [...]          # ambience map; ids never change
  source_ids: [...]        # ambience map §C
  anchors: in place, attribute AmbienceId   # environment-craft ambience-in-place §1
  acoustic_choice: <per enclosed space>     # ambience map §A
open: [the sounds, layers, variation, ranges, curves, gains, mix, crossfade laws]
avoid: [one global loop, every prop audible, masking gameplay cues]
not_in_scope: [moving anchors or zones (ask the environment designer), game code]
rules: [Gameplay-critical cues are never masked and never sound-only when muted play is supported. Numbers come from the checkpoints in this stage, not from presets. Fill only the sound keys in the map.]
deliver: sound keys in the ambience map + the sound designer's cue cards
checks:
  - C1: every source id in the map has a cue card or a reason it has none
  - C2: listening review at every checkpoint, both directions
return: STATUS + coverage per zone
</spec>
```

## 5. To the VFX designer: ambient motion
Same shape as §4: `refs` = ambience map §B "what moves", §C effect ids, §D shared environment state (wind), the camera ids showing each cause; `fixed` = anchor ids, the shared wind state, the route and hazard silhouettes that must stay clear; `open` = how each effect is built and its values; `rules` = every moving thing has a reason, a region, a priority and an off-switch; nothing covers the route; fallback order from the map; particle caps are caps, not budgets; `checks` = effect at each anchor visible from the named cameras, the route still readable at low quality.

## 6. To the studio operator: play-test and phone checks
| Key | What to give |
| --- | --- |
| intent | what must be proven that the environment designer cannot (a play-test with movement, a phone trace, a listening pass) |
| fixed | test place, studio_id rule, the frozen route and cameras (review packet §B), device names, build id |
| checks | traversal of every entrance, stairs, room and exit; leave → return → leave for each ambience zone; phone trace of the busiest overlap with gameplay on (10-15 minutes active play at least, PI34) |
| rules | one Studio driver at a time; never a live game place; label every result MCP-verified or not verified |
