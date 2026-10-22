> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `animation-design`. Sources: animation paper AP:398-467 (notes `knowledge/reference/animation/01-*.md` §8, SL01-SL08), AP:458-460, AP:654, AP:821 (loop seams, LM11), Riot core series R:3237-3301 (state machines, notes `03-riot-first-game.md`). Tags as in SKILL.md.

# Animation sets, states, transitions, loops

## 1. Build the set from the game, not from a library
- A set comes from the **implemented** gameplay states and transitions (AP:402). Ask the game-designer or the feature contract for the state list; never fill a library "to be complete".
- A clip is not complete until it has: entry pose, exit pose, loop policy, interruption behaviour, blend owner, attachment policy (what is held, what detaches) and its events (AP:402).
- An action the game does not have is marked **absent on purpose**, never covered by a generic idle (AP:402).
- In a game, a character is hundreds of clips that interrupt and blend; a state machine decides how they combine (walk/jog/run by speed, turning toward nearby characters, aim poses, handholds) [E] (R:3237-3301). Plan the state machine with the builder who codes it: you own the clip list and transition intent, the builder owns the code.
- Identity cues (stance, lean, rhythm, facing) hold across the whole set, not only the hero pose (AP:400).

## 2. Scope checklists (take only what the game uses)
| Kind | Clips to consider (AP:404-454) |
| --- | --- |
| Playable character | idle base + variations + return; start, stop, walk, run, sprint, turns, strafes, backward, direction changes the controller needs; jump prep (if allowed), takeoff, rise, apex, fall, soft and hard landing (if gameplay tells them apart), recovery into locomotion; equip, unequip, hold, aim, use, reload, pick up, drop, interact, interrupted interaction; attack families, misses, blocked hits, hit reactions, stagger, knockback, stun, recovery, death, respawn; emotes with enter, loop, exit, cancel, locomotion policy; seated, climbing, swimming, crawling, carrying, vehicle (only where implemented) |
| Creature, pet | rest, alert, attention shifts, gait changes, starts, stops, turns, support changes; flight, glide, fold, perch, takeoff, landing, swim, burrow, climb, slither only when anatomy and mechanics call for it; pet follow, catch-up, settle, owner attention, interaction, celebration, sleep and wake, correction after a teleport; LOD versions that keep identity and major contacts |
| Weapon or tool | neutral hold, equip, ready, aim, action, recoil or rebound, recovery, stow, cancelled action; reload, charge, reset; empty, blocked, misfire only if gameplay has them; grip changes and attachment transfer; first and third person are separate review targets (a viewmodel rig may be separate); melee miss, wall contact and target contact when they need different recovery or effects |
| Prop, moving object | rest states, action start, moving loop, endpoint, return or reset, interrupted movement; pivot, platform occupancy, machine phase, wheel and suspension links, interaction sockets; authoritative collision and occupancy kept apart from cosmetic motion; LOD or disabled state, first load and late join, destruction or removal clean-up |

## 3. Transitions and interruptions (test these, AP:404-420)
- Idle to every locomotion mode; locomotion to attack; airborne to hit; attack interrupted by death; equipment swap in each permitted state.
- For each interruption: which pose it leaves from, how long the blend is (a design or measured value, never a default), what is cleaned up (trails, loops, grip overrides, sounds), and what the next state is.
- A blend can hide a state change but never shows where the cancel window is (AP:351).
- Layered clips (an upper-body action over locomotion) key only the joints they mean to drive; priority settles the rest joint by joint (`animation-craft` §5).

## 4. Loops
| Decide | Rule |
| --- | --- |
| Loop interval | defined explicitly. Compare pose **and velocity** across the seam (acceleration where it matters); matching poses alone do not give smooth motion (AP:458) |
| Duplicate end pose | for Roblox the runtime does not blend the last key into the first, so the last key repeats the first pose and the clip length equals the period [V] (RA18, AP:821). The Blender caution against a doubled end pose (AP:654) is about an extra **hold**: the repeated key sits at the period, not one frame later. Check the seam **after import** (`animation-craft` C-09) |
| Travelling cycles | split the in-place cycle from root travel; the controller supplies the speed; native root motion is not released, so author in place by default (AP:813) |
| Foot slide | a mismatch between stride, controller speed, playback speed, contact timing, retarget scale or blend mixing; more keys do not cure it (AP:460) |
| Idle variation | from meaning, not randomness: a nervous creature, a sleeping pet and a machine allow different irregularity; variations keep their approved entry and exit (AP:460) |
| Ambient loops at scale | vary phase or speed per copy so copies do not twin; keep the loop calm enough not to pull the eye (`worked-examples.md` §9) |

## 5. Set table fields (template: `templates/anim/animation-set.md`)
clip id · state it serves · loop / one-shot · entry and exit pose · length source (gameplay window id, reference measurement, or PROPOSAL) · priority intent · layered joints · interruption rule · blend owner · attachments · events (timing list ids) · LOD variant · status.
