> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Reference for `film-direction`. Source rows: N1 GC-01..07, SK-01..07, MM-00..10; N2 TC-01..07; N4 (first game, 2026-10-10..13). Everything in §3 is a proposed studio contract (O), not a report of another studio's architecture (N1 MM-00). Engine facts and the build: `film-craft`.

# Game cinematics: control, exits, shared scenes, phones

## 1. Which kind of moment
| Kind | Use when | Cost and risk |
| --- | --- | --- |
| Player-directed staging (no camera takeover) | Discovering or acting is the emotional point; a landmark can be offered with sound and a safe viewing spot | Players may miss it: design the order of opportunities (N1 SC8-4) |
| Short in-game camera moment (a few shots, then control back) | A reveal, a door opening, a boss arrival that must be seen | Every ending must restore control cleanly |
| Live authored cutscene (in engine, real avatars) | The scene must include the player's own avatar or end in play without a cut | Avatar variety, streaming, phones, all exits (N1 GC-07) |
| Pre-rendered video (rendered in Blender, played in a video frame) | Scenes that do not need the player, heavy effects or cloth simulation | Upload cost and rules, phone playback, audio, a seam into live play; see `film-craft` for the current facts (N4 V-01..V-08, proposals and open questions) |
| Hybrid (play, then a few authored shots) | The establishing or choice beat is better played than shown; only the surprise or deception needs the camera | The play beat's information becomes a level-design requirement (the goal calls by light and sound, the threat stands on the approach line, the exit is visible from the entry): list it in the beat sheet and brief the environment designer (J015 G2 gaps G15) |
| Hybrid (video, then a live part that lands on the player) | A past or a prologue, then play starts | The seam: separate clocks, so the join must not need beat alignment (N4 S-10, proposal) |

Real-time vs pre-rendered vs marketing are different labels; "in-engine" does not prove it ran live on a phone (N1 GC-04..06). No rendering method is more emotional by itself (N1 GC-07).

## 2. The five ending requirements (N1 SK-04, O; precedents E: G06, G07, G08)
| Requirement | Means | Test |
| --- | --- | --- |
| Skip | Reach the correct resulting story state without the performance; repeated presses give one result; transient cues are not replayed | Skip during each major cue, during loading, twice |
| Replay | Revisit a finished scene with no repeated rewards, progression, damage or irreversible choices | Replay after completion |
| Pause | Stop local viewing where allowed; never pretend a shared world stopped | Pause in a shared server |
| Comfort | A calmer camera (less shake, sway, roll) that keeps the information the move carried | Reduced-motion run reads the same |
| Handoff | View, movement, UI and audio restored, with a clear first playable action | Each ending lands on the same play state |

Plus the endings the paper's runtime contract adds (N2 TC-04..07): **failure** (missing asset, removed actor, camera taken over, death or respawn, interrupted teleport, a newer scene) and **disconnect** (the server releases everything even if the client never reports completion). No player is ever left immobile behind a black overlay.

- Essential objective information also exists outside the skippable part, in a short readable form (N1 SK-05).
- Repeatable boss entrances: the return after failure is tested as seriously as the first entrance; the reveal's value on attempt three is not the same as on attempt one (N1 SK-06). Offer a shorter repeat or skip where the owner agrees.
- No source gives a skip rate, a best wait-before-skip or a best length (N1 U-12, SU-06). If the owner wants data: events for start, skip offered, skip pressed, finished, interrupted, returned to play, split by first view vs replay and device (N3 MD-01..09), through the `analytics` skill.
- First game: skipping from second 1 of a forced first-time film was proposed and never ruled on (N4 P-04): ask the owner.

## 3. Shared scenes: the contract to agree before approval (N1 MM-01..09, O)
1. **Audience:** one player, a party or everyone present? What does a late joiner see?
2. **World:** do NPCs, hazards and timers keep running for viewers? What prevents unfair damage?
3. **Authority:** who decides the shared event is complete, versus one client's playback ending?
4. **Missing assets:** which actor or prop is indispensable; what happens if it is not ready? A camera never looks forever at an empty mark.
5. **Skip policy:** individual, unanimous, host-controlled or fixed shared start; shown to players, never a surprise.
6. **Return path:** where the player is, what they face, the first safe action after finish, skip, death, disconnect or cancel.
7. **Accessibility:** captions, reduced motion and alternative exposition carry the same required information.
8. **Identity:** different avatar heights, accessories and costumes keep the gesture and the focal point.

Never freeze an uninvolved player because someone else triggered a scene. Never tie a group reward to every viewer finishing a camera track. If some skip and some watch, stage the boundary between viewers and active players on purpose (N1 MM-09). The best policy depends on the game's social contract; there is no universal vote rule.

## 4. Phones
- Readability at phone size beats beauty at desktop size: silhouette, gesture, the key object (N1 SC6-3).
- The mobile part of the paper is a direction, not a measurement: every phone claim needs a real-device capture (N1 X-32; `film-craft` review).
- Letterbox bars are decoration; they do not make a new projection, and if they cover the action the shot is reframed (N2 RT-13, RT-56, see `film-craft`).

## 5. First game's lessons that hold for any game (N4)
| Lesson | Certainty |
| --- | --- |
| Plan the whole sequence the owner asks for; offer a split only as a priced option | owner decision (P-01) |
| Keep one beat list and update it per decision; story elements change between rounds | owner decision (P-02) |
| Platform limits go at the top of the beat list (romance, injury, gore) | owner decision (P-08) |
| Design and build the scene's set and cast before boards; check asset readiness against the shot list on day one | owner decision (P-07); open (X-01) |
| Cast must look like one world, side by side, before the owner sees it | owner correction (B-04) |
| Rig and face quality caused the most rejections: separate parts, own face per character, eyes that look, tested before review | owner corrections (R-01, R-03, R-04, X-02) |
| Cut or change a beat the cast cannot show; keep its story outcome | owner decision (R-09) |
| Sound and voice planned with the scenes | owner decision (S-01) |
| Ask the owner with options that each carry a recommendation; new designs go as a sheet first | owner decision (P-06) |
| Not every big moment shakes the camera | owner decision (A-05, set for effects) |
| Undecided content (the key line, names, what a shot shows) blocks voice, mouths and shots: ask early with a default | open (X-04) |
