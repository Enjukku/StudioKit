> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit reference: universal. J008. Format: `rules/messages.md` §2 (`<intent>` prose, then `<spec>` keys). What each role owns: `environment-design` §1 (CO04 O). First-game brief practice: `knowledge/reference/environment/04-first-game-stages.md` FS-H03, FS-P14. Every brief: the why in prose; exact values only with a source; the craft left open; every rule restated; one runnable check per acceptance rule. Revised by J018 maker environment-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (§2-§6 sharpened; §7 what to ask each partner for, and when). Revised by J024 writer · claude-opus-5-5 · default · 2026-10-24 (J024 design): hand-off lines for the cut flow (needs in direction, no proof, no check-ins).

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
Intent: which place, which reference, what feeling is wanted, where it drifts. Spec: `refs` = review packet with the §7 numbers, the read plan, key views at the lowest and highest setting with their grey images, the reference images, art bible version; `open` = the art director's judgment and fixes; ask them to classify each drift (large shape, framing, value hierarchy, material response, camera / exposure / tier) before suggesting a fix (CO07 O), and to answer a visual note as a paint-over on the capture; ask the goal question, not "do you like it" ("does the gate read as the goal from spawn at phone size?"); `checks` = each note names the camera, the defect, the intended reading and the layer; at the check-in they name the theme and one story fact from the captures (review lines FL5, FL8).

## 3. To the modeler: a new asset
| Key | What to give |
| --- | --- |
| intent | what the piece does in the place (landmark, route cue, dressing with a story, kit piece) and how it is seen (distance, camera, how many); the place's personality words and the story fact the piece carries (wear, repairs, age) |
| refs | approved reference image (`reference-images`), the blueprint sheet with the player figure, neighbouring kit pieces |
| fixed | size in studs with its source (scale sheet), pivot location and the surface it rests on, collision role (walkable, blocker, none), facing (main face toward the route), attach points for VFX or sound anchors, kit joins and the snap grid if it is modular, and the greybox origin it snaps to; a capture of the stage's ground under its chosen light (or the art bible values when no light is chosen yet); the environment value band and reserved colours; size steps for a family (big, medium, small); a base or skirt where it meets the ground |
| open | how it is modelled, topology, UVs, materials within the art bible |
| rules | 20,000 triangles per mesh is a cap, not a target; budgets from the owner or a measurement; finished on every face players can see; real scale against the player |
| checks | imports at the stated size and pivot with the project export recipe; renders front, back, sides, 3/4 beside the reference; I return one in-set capture of the placed piece at the game camera with a player in frame, and the piece is accepted only on it |

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
  emotion: <per zone>                       # ambience map; the same cause can be calm or frightening
  floor_materials: [...]                    # walkable materials in the place; each needs a footstep entry
open: [the sounds, layers, variation, ranges, curves, gains, mix, crossfade laws]
avoid: [one global loop, every prop audible, masking gameplay cues, a dry sound in a large enclosed space]
not_in_scope: [moving anchors or zones (ask the environment designer), game code]
rules: [Gameplay-critical cues are never masked and never sound-only when muted play is supported. Numbers come from the checkpoints in this stage, not from presets. Fill only the sound keys in the map.]
deliver: sound keys in the ambience map + the sound designer's cue cards
checks:
  - C1: every source id in the map has a cue card or a reason it has none
  - C2: listening review at every checkpoint, both directions
  - C3: every floor material in floor_materials has a footstep set, or a refusal with the existing material to use instead
return: STATUS + coverage per zone
</spec>
```

## 5. To the VFX designer: ambient motion
Same shape as §4: `refs` = ambience map §B "what moves", §C effect ids, §D shared environment state (wind), the camera ids showing each cause; `fixed` = anchor ids, the shared wind state, the route, hazard silhouettes and sight lines that must stay clear, the reserved colours; `open` = how each effect is built and its values; `rules` = every moving thing has a reason, a region, a priority and an off-switch; decorative motion is small, slow, low in brightness and partly hidden at its base, never the fastest or brightest thing near a sight line; nothing covers the route; intense channels (flashes, storm tints) have an off path and stay at most 3 flashes a second; fallback order from the map; particle caps are caps, not budgets; `checks` = effect at each anchor visible from the named cameras, the route still readable at the lowest setting, the moving-things list with distances to sight lines (review line AM1).

## 6. To the studio operator: play-test and phone checks
| Key | What to give |
| --- | --- |
| intent | what must be proven that the environment designer cannot (a play-test with movement, a phone trace, a listening pass) |
| fixed | test place, studio_id rule, the frozen route and cameras (review packet §B), device names, build id |
| checks | traversal of every entrance, stairs, room and exit; leave → return → leave for each ambience zone; the busiest-moment play capture (players, typical effects, HUD, at the smallest phone viewport) from the key views; key views at the lowest graphics setting when I cannot set it; phone trace of the busiest overlap with gameplay on (10-15 minutes active play at least, PI34) |
| rules | one Studio driver at a time; never a live game place; label every result MCP-verified or not verified |

## 7. What to ask each partner for, and when (inside the approved brief)
| Partner | Ask for | When |
| --- | --- | --- |
| game designer | the stage's job and conflict sentence, route graph and route table in seconds, the blockout brief per node, hazard sheets, read rank, material-to-rule table, orientation conventions, the approved blockout limits; a ranked work list agreed with me; a sign-off for any art change near collision, cover or sight lines; the treatment table for interactive pieces; a shape or outline cue when a pickup separates from a floor by colour only | intake; blueprint; any play-affecting change; art check-in |
| art director | the art bible version with its craft-standard rows (value bands per layer in both units and the saturation band for environment materials, separation targets, reserved colours with shape partner and allowed share, key light per place, shape vocabulary, palette roles, stylisation level); the pick among my options; paint-overs on my captures when a note is unclear; the theme and story cold read at the check-in | intake (before the read plan); option round; art check-in |
| modeler | new reusable pieces in the §3 format; my in-set capture goes back to them before a piece is accepted | after the art blockout confirms the kit piece list; each delivered piece |
| sound designer | cue cards and sound keys from the ambience map; a footstep set per floor material (or a refusal and the material to use instead) | the floor-material list at the kit list, before materials are built; after the ambience map revision; whenever a new floor material is proposed |
| VFX designer | ambient effect specs from the ambience map, away from sight lines, with off paths for intense channels | after the ambience map revision |
| studio operator | the busiest-moment play capture, multi-client walk tests, lowest-setting captures when I cannot set the quality, the phone trace | the capture-and-scripts run of each review round; release candidate |
| film director (cutscene sets) | the beat sheet draft, the value and light plan per beat (contrast key, motivated source, brightest area, what stays hidden) taken as fixed inputs for lighting the set; the shot cameras, at which I re-run the value lines (subject first in M1, M6 separation) | my needs table on the beat sheet in direction, before G1 (J024) |
| owner | approval of the references and the blueprint; protection choices when a budget forces cuts | step 3, step 4 (G1); budget cuts |
