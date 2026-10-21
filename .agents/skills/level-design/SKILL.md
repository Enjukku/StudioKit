---
name: level-design
description: Plan, block out and review a Roblox level, map, hub, lobby, arena, route or encounter - route graph, first view, landmarks, teaching a mechanic, pacing, scale, pass/fail review. Use for "players get lost", "it's boring to walk", "players miss the shop", "this area feels empty", "too hard here", or a blockout or map needing a second opinion. Never edits stage files.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Kit skill: universal. J003. Sources: the DestructionSimulator `level-design` skill (Riot "So You Wanna Make Games??" ep. 1, 4, 10 transcripts, 2026-10-15) = **DS**, game-specific parts removed; owner research paper Part 2 §4-§5 (notes `knowledge/reference/game-design/04-levels-social-review.md` = **N4**); Roblox defaults from the local docs mirror (`_api-reference/classes/StarterPlayer.yaml`, read 2026-10-20). Tags: **V** VERIFIED, **E** EXPERIENCE, **O** OPINION. Load `game-design` with this skill.

# Level design: the place where the rules meet the player

## 1. When this skill starts
A level, map, hub, route or encounter is planned, blocked out, built or under review. It answers: what is this place's job, how does a new player find the way without words, what does it teach, how does tension rise and rest, what happens on failure, and does it hold up for groups, on phones, in the real camera. Design is the owner's: output is reviews and proposals, never silent changes.

## 2. Read this file when
| You need | Open |
| --- | --- |
| The route graph and its 10 node fields, the 5 player walk-throughs, encounter rules, the full 14-item review with reasons | `references/review-artifact.md` |
| Loops, pacing principles, fairness, social rules | `game-design` skill |
| How a level brief is written and handed to the environment designer (who builds the place: `environment-design`) | `preproduction/references/handoffs.md` |
| Studio walk tests and screenshots | ask the studio-operator (`studio-mcp` skill); one Studio driver at a time |

## 3. Steps
1. **Level job card** (write before judging): target experience (one type of fun) · player goal here and how progress shows · opposition · what the level teaches · session shape (first visit, return visit, short phone session) · camera and device · group size · the 3-5 things players expect to find in this theme. Missing field that changes the verdict → state an assumption.
2. **Blockout first.** Grey blocks only: routes, obstacles, spawn, goals, boundaries, sight lines. Walk it at player speed before any art; changes here are cheap (DS §2).
3. **Route graph** (`review-artifact.md` §1): nodes and edges with the 10 node fields; walk it as 5 player types; trace a wrong turn, a death, a disconnect and an empty resource.
4. **Review** with the 14 checks (Pass / Fail / Unproven); measure distances and walk times from coordinates, never guess.
5. **Art roughs** that keep the blockout's gameplay limits (the same boundary can be a wall, a cliff or a river: pick the most believable one on theme).
6. **Detail, story props, lighting** only after the layout works in play; then play-test against the target experience. Do not reopen a closed layout without new evidence.

## 4. Craft core
| ID | Practice | Evidence |
| --- | --- | --- |
| L-01 | **The first view tells the player where they are, what they can do and where to go.** Frame the main goal or landmark in it | DS §3 |
| L-02 | **Landmarks orient.** One big landmark visible from anywhere per zone; smaller ones at decisions; unique silhouettes, not colour only; distinguishable from the real approach directions and camera | DS §3; N4 L2 O |
| L-03 | **Lead with shapes and light.** Paths, fences, rivers, roof lines and light point to the next goal; the brightest, most saturated thing in view is the goal; remove lines that lead into dead ends | DS §3 |
| L-04 | **Teach in steps.** Expose a mechanic safely → require it in a harder arrangement → change one relationship so rote play fails → ask for independent use. State what the player should infer and the action that shows it. An adaptation from Super Mario 3D Land's one-concept-per-level practice; not required for open worlds, horror or social areas | D10 E (FI); N4 4.02 O |
| L-05 | **Escalation names the changed demand** and the skill it tests; hazards without a learning reason create arbitrary difficulty | N4 L4 O |
| L-06 | **Rest and peak alternate.** Calm open areas between dense ones; a climax piece near the end; a reward or new view at each natural pause; pacing frequency is a separate dial from difficulty | DS §3-§4; D11 V (FI) |
| L-07 | **Measure walk time.** Roblox default walk speed is 16 studs/s, so 160 studs take 10 s; default jump height is 7.2 studs, so a ledge above it is a wall. Proposal: no walk over ~15 s without something to do or see (DS heuristic, O) | StarterPlayer.yaml V |
| L-08 | **Return trips are part of the loop.** Keep them short or make them interesting (shortcuts, new views, things to do on the way) | DS §4 |
| L-09 | **Boundaries look and act like the world.** Cliffs, water, walls, fences, buildings on theme; never invisible walls; collision, fall, reset rules and recovery paths match what players see; test with the movement tools players really have | DS §5; N4 L7 O |
| L-10 | **Encounters elicit behaviour.** Each enemy states the behaviour it asks of the player; enemies fair alone can be unfair together; telegraphs must be usable at the moment of decision, not only on a paused screenshot | N4 §1.2 O |
| L-11 | **Scale is what the player touches.** Doors, stairs, rails, counters sized for the character; walk next to them in the real camera | DS §5 |
| L-12 | **Story in the space.** Climate, age, culture and use show through props and wear; the 3-5 things players expect in this theme are present and easy to find | DS §5 |
| L-13 | **A big world is not more play.** Scenery is not content; paths, breadcrumbs, landmarks, waypoints and soft vs hard boundaries do the guiding (Minecraft Education guide, classroom scope) | D24 E (FI) |
| L-14 | **Groups and failure are designed.** Late join, separation and regrouping handled; a solo bottleneck can exclude party members; checkpoints keep what the player learned, not only transit; failure cost and retry route match the intended challenge | N4 L8-L9, R3 O |

## 5. Rules (final check, short)
- Proposals only, labelled PROPOSAL; never edit stage or content files.
- Every finding cites evidence: a coordinate, a node id, an image region or `path:line`.
- No pass/fail on walk times or reach without measurement from coordinates or a Studio capture; otherwise "could not check".
- Readability checked under the real screen, effects and player count: a clean grey box can fail in the production scene (N4 L5 O).
- Rights: no copied maps, landmarks or signature layouts from other games.

## 6. Self-check before returning
- [ ] Level job card written; assumptions stated.
- [ ] Route graph with node fields; 5 walk-throughs and 4 failure traces done or listed as not checked.
- [ ] 14 checks rated Pass / Fail / Unproven with evidence; no point totals.
- [ ] Walk times computed from coordinates at 16 studs/s (or the game's speed).
- [ ] Ranked fixes (`game-design` review §3) with cost; marked-up top-down image when one exists; "keep" and "could not check" lists.

Project overlay: if `knowledge/overlays/level-design.md` exists, read it after this file; it wins for this game.
