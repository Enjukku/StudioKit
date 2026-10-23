> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `animation-design`. Rebuilt by J018 maker animator · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018). Evidence: animation paper notes `knowledge/reference/animation/01-*.md` §8 (sets, loops, transitions), `03-*.md` (state machines); the craft library `knowledge/reference/craft/riot/` (pipeline-production, character-design, weight-timing).

# Animation sets, states, transitions, loops

## 1. Build the set from the game, not from a library
- A set comes from the **implemented** gameplay states and transitions. Ask the game-designer or the feature contract for the state list; never fill a library "to be complete".
- A clip is not complete until it has: entry pose, exit pose, loop policy, interruption behaviour, blend owner, attachment policy (what is held, what detaches), its events, and, for clips that carry a read, who must react to it and how often it plays.
- An action the game does not have is marked **absent on purpose**, never covered by a generic idle.
- In a game, a character is many clips that interrupt and blend under game conditions (walk / jog / run by speed, aim by direction, reactions by distance); you cannot predict which plays when, and transitions are what players see most. Plan the state machine with the builder who codes it, before keying: you own the clip list and transition intent, the builder owns the code. Make clips to blend: matching poses at the transitions, priorities set.
- Identity cues (stance, lean, rhythm, facing, the signature shape) hold across the whole set, not only the hero pose. Every common action (run, idle, attack, emote) shows who this character is.
- **Variants keep the base.** A skin, tier or upgrade keeps the base clips' identity anchors, contact points (grip, hand positions, sockets), tell and readiness beats, timing and secondary motion; a premium variant never has fewer secondary-motion sources than the base. A variant may re-theme an ability's flourish; it never changes the tell. When a variant swaps the mesh, the shared clips are replayed on it before release.
- A character with several forms is several sets of work: size it that way.

## 2. Scope checklists (take only what the game uses)
| Kind | Clips to consider |
| --- | --- |
| Playable character | idle base + variations + return; start, stop, walk, run, sprint, turns, strafes, backward, direction changes the controller needs; jump prep (if allowed), takeoff, rise, apex, fall, soft and hard landing (if gameplay tells them apart), recovery into locomotion; equip, unequip, hold, aim, use, reload, pick up, drop, interact, interrupted interaction; attack families, misses, blocked hits, hit reactions by strength (light, heavy), stagger, knockback, stun, recovery, death, respawn; emotes with enter, loop, exit, cancel, locomotion policy; seated, climbing, swimming, crawling, carrying, vehicle (only where implemented) |
| Creature, pet | rest, alert, attention shifts, gait changes, starts, stops, turns, support changes; tells for every attack; flight, glide, fold, perch, takeoff, landing, swim, burrow, climb, slither only when anatomy and mechanics call for it; pet follow, catch-up, settle, owner attention, interaction, celebration, sleep and wake, correction after a teleport; LOD versions that keep identity and major contacts |
| Weapon or tool | neutral hold, equip, ready, aim, action, recoil or rebound, recovery, stow, cancelled action; reload, charge, reset; inspect (moving parts slide without clipping the arms); empty, blocked, misfire only if gameplay has them; grip changes and attachment transfer; first and third person are separate review targets (a viewmodel rig may be separate); melee miss, wall contact and target contact when they need different recovery or effects |
| Prop, moving object | rest states, action start, moving loop, endpoint, return or reset, interrupted movement; pivot, platform occupancy, machine phase, wheel and suspension links, interaction sockets; authoritative collision and occupancy kept apart from cosmetic motion; LOD or disabled state, first load and late join, destruction or removal clean-up |

## 3. Transitions and interruptions (test these)
- Idle to every locomotion mode; locomotion to attack; airborne to hit; attack interrupted by death; equipment swap in each permitted state.
- For each interruption: which pose it leaves from, how long the blend is (a design or measured value, never a default), what is cleaned up (trails, loops, grip overrides, sounds), and what the next state is.
- A blend can hide a state change but never shows where the cancel window is.
- A short gameplay clip may carry its weight shift in the first frames of the next clip, but the shift must exist somewhere in the chain.
- Layered clips (an upper-body action over locomotion) key only the joints they mean to drive; priority settles the rest joint by joint (`animation-craft` §5).
- Proof is a play capture of each transition in Studio: no pop, no foot slide, no stuck grip.

## 4. Loops
| Decide | Rule |
| --- | --- |
| Loop interval | defined explicitly. Compare pose **and velocity** across the seam (acceleration where it matters); matching poses alone do not give smooth motion |
| Duplicate end pose | for Roblox the runtime does not blend the last key into the first, so the last key repeats the first pose and the clip length equals the period [V]. The Blender caution against a doubled end pose is about an extra **hold**: the repeated key sits at the period, not one frame later. Check the seam **after import** (`animation-craft` C-09) |
| Travelling cycles | split the in-place cycle from root travel; the controller supplies the speed; native root motion is not released, so author in place by default |
| Foot slide | a mismatch between stride, controller speed, playback speed, contact timing, retarget scale or blend mixing; more keys do not cure it |
| Idle variation | from meaning, not randomness: a nervous creature, a sleeping pet and a machine allow different irregularity; variations keep their approved entry and exit; an idle with every part in phase reads as a machine |
| Ambient loops at scale | vary phase or speed per copy so copies do not twin; vary only decorative axes, never a meaningful timing; keep the loop calm enough not to pull the eye (`worked-examples.md` §11) |

## 5. Set table fields (template: `templates/anim/animation-set.md`)
clip id · state it serves · loop / one-shot · entry and exit pose · length source (gameplay window id, reference measurement, or PROPOSAL) · priority intent · layered joints · interruption rule · blend owner · attachments · events (timing list ids) · LOD variant · status. The template also has columns for who must react and the reaction window, the play rate, the one or two pushed moments and the reduced-motion variant; fill them per clip.
