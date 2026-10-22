---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J006 (hidden cases for the grader; not shown to the animator)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# J006 hidden eval cases (grader only)

The skills were built from all the owner's material, so no part of it is held back. These cases are new briefs whose answers the material decides without stating them. Grade with the common checks of `.agents/skills/animation-craft/evals/briefs.md` (A1-A8) plus the rows below.

## H1. Treasure chest reveal (prop + shared event)
> A chest opens when a player claims a reward; the reveal must feel exciting and the reward is decided by the server.

| Check | Expected |
| --- | --- |
| H1.1 (must) | Lid on its hinge by code or a short clip (reason); anticipation rattle; the reveal peak on an event shared with VFX and sound |
| H1.2 (must) | The motion never decides or implies the reward before the server outcome; a "reveal_confirmed" event comes from gameplay |

## H2. "The walk slides on the ice level" (diagnosis)
> Owner: "the character's feet slide when walking on the ice level, but not on grass".

| Check | Expected |
| --- | --- |
| H2.1 (must) | Asks whether the slide is designed (ice friction) or a mismatch: stride vs controller speed vs playback speed vs blend; does not add keys first |
| H2.2 | Proposes a measured check (contact slide metric at both speeds) and a fix that keeps the in-place policy (speed-matched AdjustSpeed or a separate ice clip), with the owner deciding the ice feel |

## H3. Elevator with riders
> A moving platform carries 4 players between floors.

| Check | Expected |
| --- | --- |
| H3.1 (must) | Server-owned occupancy and position (prismatic servo or server-authoritative mover); cosmetic details on the client |
| H3.2 | Gentle start and stop stated as curves with reasons; never moves while its door is open |

## H4. Stylized jump for a nimble hero (character, principle use)
> A nimble ninja-like hero jumps; the game feel is cartoony and snappy.

| Check | Expected |
| --- | --- |
| H4.1 | Weight leaves the support before take-off; clavicles and arms supply the energy; feet stay down a little longer for a sharp push |
| H4.2 | Hang time at the top and a fast fall, applied consistently to every jump in the set; asymmetric landing (two reads) |
| H4.3 (must) | Jump height and air time come from the controller or design, not the clip |

## H5. Building collapse after a boss hit
> A watchtower collapses when the boss smashes it.

| Check | Expected |
| --- | --- |
| H5.1 (must) | Stress shown before the fall (lean, crack, sag); shell first, core last; the end state matches collision |
| H5.2 | Debris physics and the destroyed state decided with the destruction / physics owner and environment-designer; the gameplay state never waits on the show |
