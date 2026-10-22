> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Eval briefs for the animator (animation-design + animation-craft + rig-pipeline)

Give the agent the brief text and the named files only. A separate grader (Sonnet, high, J005-D4 precedent) grades each check pass/fail from the agent's files, not its summary. A brief passes at ≥ 80% of its checks with no "must" check failed. Common checks apply to every run. Hidden cases for the build job are kept outside the skill (`knowledge/jobs/J006-animator/evals-hidden.md`).

| ID | Common check |
| --- | --- |
| A1 (must) | No invented numbers: every length, hold, fade, delay, tolerance and budget has a source (gameplay window, owner, measurement, platform doc) or is PROPOSAL / UNKNOWN with its owner; the timing library is used only as measured context |
| A2 (must) | The read and 2-4 feel words come first; every choice of pose, timing or spacing gives its reason (a principle, a reference, the character) |
| A3 (must) | Technique chosen per moving part (keyed clip / code / physics / texture) with the reason and a docs path; no rigger step for a rigid one-axis prop; a rig need goes through `rig-pipeline` |
| A4 (must) | Gameplay windows are inputs, never changed; markers are presentation; the server owns outcomes |
| A5 | Timing list in `templates/anim/timing-list.md` form: one meaning per event, seconds + source frame + fps, owner, consumers, interruption rule |
| A6 | Light checks: clip_check numbers for every clip; images only for failing numbers plus ≤ 8 key frames; render and image counts reported |
| A7 | Hand-back in `rules/messages.md` §3 shape: STATUS first, coverage per item, evidence labels, docs_read |
| A8 (must, when exporting) | FBX through `tools/rig/roblox_fbx.py` (`kind="clip"`), export copy baked with visual keying; in-place locomotion unless a tested root-motion policy is chosen |

## 1. Heavy two-handed sword swing (held item)
> A knight swings a two-handed greatsword in a third-person melee game. The feature contract gives: startup 0.5 s, active 0.15 s, recovery 0.6 s, cancel into dodge allowed after 0.35 s of recovery. The rig is released (rig sheet + control manifest given; the sword is on a right-hand grip socket, left hand solved to the handle). Plan the clip, block it, and hand VFX and sound what they need.

| Check | Expected |
| --- | --- |
| 1.1 (must) | Phases mapped inside the given windows (load and anticipation inside startup, the accent at active start, follow-through and settle in recovery), window lengths unchanged |
| 1.2 (must) | Weight read: feet organize force, torso and arms accelerate the blade together, heavy shown by stance and phase contrast, not slow playback |
| 1.3 | Blade tip arc traced and judged from the game camera; grips held (contact metric) |
| 1.4 (must) | Separate events: acceleration (whoosh, trail start), contact candidate, follow-through end, cleanup; no single "Hit" marker; trails and flashes left to VFX |
| 1.5 | Cancel point stated as a pose the dodge can blend from; transition listed in the set |
| 1.6 | Impact reads with effects hidden (a capture or frame with VFX off) |

## 2. Castle drawbridge (prop, no rig needed for the deck)
> A drawbridge lowers when the player pulls a lever. It must feel huge and old. Players wait on the far bank; it becomes walkable only when fully down. Ten other players may watch. Write what is needed.

| Check | Expected |
| --- | --- |
| 2.1 (must) | Technique: code-driven or servo rotation of the deck about its base hinge, with reason; chains as a short clip, texture or code detail; no rigger step for a one-axis deck (a rig only if several linked parts are keyed) |
| 2.2 (must) | Motion spec in `templates/anim/motion-spec.md` form: pivot and axis, travel with units, phases with lengths (PROPOSAL or sourced) and named curves with reasons; slow start, gravity takes over, heavy landing; no ease-in-out on the whole travel |
| 2.3 (must) | Cosmetic motion on the client; `walkable` and collision server-owned; a server tween is not used (replicates every frame) |
| 2.4 | Late joiner and stream-in start at the current state; retrigger mid-travel defined |
| 2.5 | Lever: hand contact on the character clip; hard stop on the lever; events `release`, `land_contact`, `walkable` on the timing list |

## 3. A row of flags and windmills (ambient loops at scale)
> A harbour town: 120 flags on poles and 12 windmills, phones first. Make them feel alive without distracting from the market stalls.

| Check | Expected |
| --- | --- |
| 3.1 (must) | Technique per object with reason: windmills as constant-speed rotation in one client loop (or a motor, with reason); flags as a short bone loop on a client Animator, a code sway or a texture/flipbook, chosen by distance and count |
| 3.2 (must) | States that no documented per-copy cost exists and plans the measurement at the peak count on the floor phone (or BLOCKED without a phone); no invented budget |
| 3.3 | Copies out of step (phase or speed per copy, stable seed); calm amplitude; a still or slow variant for reduced motion |
| 3.4 | Global wind is not relied on to move flags or meshes; streaming restart and no far LOD for animated models planned |
| 3.5 | Loop seam: last key repeats the first pose, length = period; seam checked after import |

## 4. Creature action: a heavy beast's pounce
> A big wolf-like beast pounces at the player from 8 studs. The game-designer gives a 0.8 s telegraph window and a 0.25 s active window; players must be able to dodge on a phone. The beast has a skinned rig with an active tail. Plan the motion profile items you need, the clip and the events.

| Check | Expected |
| --- | --- |
| 4.1 (must) | Telegraph is readable as a silhouette at phone size from the player camera, inside the 0.8 s window |
| 4.2 | Hind legs load and push, front legs reach and catch, stance feet planted while loading (contact metric) |
| 4.3 | Tail treated as active (counterbalance in the air), not a generic lag |
| 4.4 (must) | AnimationController + Animator, loaded and played on the server if every player must see it; `Animator:LoadAnimation`, track cached |
| 4.5 | Landing: fast contact, then the catch; no scoot; events `telegraph_start`, `launch`, `land_contact`, `recover_end` |

## 5. Teddy pet set on the released J005 rig (G2 brief)
> The J005 teddy rig (`output/rigs/teddy/s5/`, control manifest, rig sheet revision named in the brief) is a cozy companion pet: walk beside the player, stand idle, wave. Up to 8 on screen on phones; third-person camera. Accept the rig (S6), then make an idle loop, a walk loop and a wave with a timing list, export, and prepare the Roblox import in the test place (the owner clicks Import).

| Check | Expected |
| --- | --- |
| 5.1 (must) | S6: every §B extreme posed through the control manifest; numbers first; one rig note or a signed §H row with evidence |
| 5.2 (must) | Idle and walk loops pass the seam check (pose and velocity) and the walk's planted feet pass the slide check against a stated tolerance, or report MEASURED with no tolerance |
| 5.3 | Personality from the feel words (soft, light, friendly, never stiff) visible in a named pose or timing choice per clip |
| 5.4 (must) | Walk in place, the controller owns travel; export via `roblox_fbx.export(kind="clip")` after a visual-keying bake; fresh-scene round trip |
| 5.5 | Import steps for the owner (route named, test place only); after import, played on an AnimationController Animator with the stated priority; marker times from the Output log against the timing list (MCP-verified) or BLOCKED with reason |
| 5.6 | Wave layered over idle/walk keys only the arm and head joints, at a higher priority |
