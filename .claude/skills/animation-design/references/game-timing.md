> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `animation-design`. Rebuilt by J018 maker animator · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018). Evidence: animation paper notes `knowledge/reference/animation/01-*.md` §6, §9 and `02-*.md` §4; the craft library `knowledge/reference/craft/riot/` (weight-timing, rhythm, vfx-reads-timing, cross-craft, game-design-fun); sync and hit-stop starting values agree with `vfx-design/references/juice-repetition-sync.md`. Numbers marked PROPOSAL are starting values a check may change.

# Game timing and the shared event timeline

## 1. Who owns which time
| Time | Owner | The animator's part |
| --- | --- | --- |
| Gameplay windows (startup, active, recovery, cancel, cooldown) | gameplay owner (game-designer, feature contract, config) | place readable beats inside them; report a conflict, never retime the window |
| Reaction window for a threat's tell | game-designer | hold a distinct tell pose for it; ask for it when it is missing (UNKNOWN until given) |
| Clip beats (tell, build, beat, accent, follow-through, settle) | animator | inside the window |
| VFX timing | vfx-designer, keyed from your markers, a little staggered behind the motion | name the events VFX needs |
| Sound timing | sound-designer, after the picture; hears about every change | name accents and confirmed outcomes; state the sync rule (§4) |
| Hit-stop length per hit strength | game-designer with the VFX designer (a game value) | supply the frame worth freezing on (§5) |
| Camera accents in cutscenes; camera shake in play | film-director; VFX | act inside the shot list; never bake camera motion into a gameplay clip |
| Authoritative outcome (hit, damage, open, occupied) | server gameplay code | none: a marker is presentation |

## 2. Game time is not film time
- Separate five things: the visible reaction, the authoritative start, the active window, when cancel is allowed, when control returns. A recovery pose can keep playing after control returns; a blend can cover a state change; neither shows the cancel window.
- Startup / active / recovery are analysis tools, not proof of three sequential states; note buffering, hit confirmation and rate changes.
- Input delay has several clocks (input, game acceptance, network, animation scheduling, display). A long windup is not lag. No safe general value exists for input delay, cancel window, startup or blend length: design supplies them or approves a measurement.
- **Anticipation is sized by who reacts.** An enemy's or hazard's tell is information the player needs: a distinct pose, readable as a black shape, held for the designer's reaction window, longer for bigger attacks; network delay shortens the real window, so never cut it to the bone. The player's own action answers the input on the press frame or the next and keeps its tell short and tight (PROPOSAL: about 2 frames of coiled hold at 30 fps), so it feels strong and responsive. Move visible effort around protected events instead of stretching the action.
- Protect readiness beats: a cosmetic variant keeps the base clip's tell, readiness and ammunition events.
- **Frequency sets length.** The more often a motion plays, the shorter and quieter it is: an every-second pickup or hit reaction stays brief; a once-a-round finisher may take its time.

## 3. Frame arithmetic (exact)
- seconds = source intervals / source frame rate. Poses on frames 1 and 31 at 30 fps are 30 intervals = 1 s apart.
- A 30 fps interval is exactly 100/3 ms; a 60 fps interval 50/3 ms. Keep fractions; rounding is a logged decision. At 30 fps, 0.1 s = 3 frames.
- Blender's effective rate is `render.fps / render.fps_base` [V].
- Capture rate, animation sampling rate, simulation step, render rate and display refresh are five different things. Phones vary their frame rate, so runtime timing lives in seconds, never in frames.
- A count with no stated rate ("45 frames") has no seconds equivalent.
- Retiming by k: recheck every dependent event at t × k; uniform scaling can still look wrong.

## 4. The shared event timeline (format: `templates/anim/timing-list.md`)
Fields per event: action revision, stable name, meaning, time in seconds (exact or rational), source frame and frame rate, owner, authority, replay policy, interruption behaviour, consumers.

Typical events, use only those the action has: request accepted, presentation start, tell start, anticipation complete, active start, contact candidate, active end, cancel open / close, recovery complete, attachment change, VFX trigger, audio trigger, camera accent, UI cue, clean-up.

- **One meaning per event.** Never one marker named "Hit": a trail may start before contact, a whoosh follows acceleration, a contact sound needs a confirmed surface, damage may come after prediction.
- **Use the same stage names as VFX and sound** (load, charge, release, travel, impact, tail), so markers, frame scripts and cue cards line up without translation.
- **An ability moves like its mechanic verb,** the same verb the VFX frame script and the sound cue card use: a slow decelerates and spreads, a stun snaps, a knock-back drives through, a heal rises and settles. Write the verb on the clip card.
- **A state with a timer or a breaking point gets a building tell before it ends** (a shield about to break strains and cracks, a stun wears off with a stir, a charge about to release trembles): a named event on the timing list (for example `shield_break_warn`) that sound and VFX key from, held long enough for the player to react.
- **Forecast vs confirmed.** `contact_candidate` (animator, from the pose) is not `contact_confirmed` (gameplay outcome). A miss never plays confirmed-hit feedback.
- **Attempt vs outcome.** The attempt (the swing, the reach, the button press of a character) plays on input, small and quick. The outcome layer (the target's big reaction, a hit-stop, a celebration, a reward flourish) is its own clip or layer, started by the confirmed event and scaled by its strength; a rejected request never shows it. When confirmation is slow, a pending pose holds; it never shows success early.
- **Sync rule.** VFX and sound key from your markers, and picture punch and sound transient start from one trigger event. The sound onset lands on the first lit contact frame or up to about 40 ms after it, never more than one frame (16.7 ms at 60 fps) before it; a steady small delay beats a jittering one. Studio MCP captures are stills, so sound sync is "not verified" unless captured on the target device. `sound-design`'s current window is wider; until it is aligned (J018 proposal), the sound-designer's book governs the sound side and a measured offset is reported as MEASURED, not FAIL.
- **Clean-up is an event.** Interruption clears trails, loops, grip overrides and connections.
- **One canonical time per event,** derived editor labels only; no craft keeps its own rounded frame list. A timing change bumps the revision and goes to every consumer in the same hand-back.

## 5. Hit-stop and impact
- Hit-stop freezes the attacker's and the target's animation and the hit's own particles for a moment at contact; physics, debris, other players and server results keep running (there is no global time scale). The builder implements it (pause the tracks, then restore); you supply the frame worth freezing on: the contact pose, with the source of power and the hook shapes facing the camera, readable as a black shape.
- Its length is a game value set by the gameplay owner with the VFX designer, rising with hit strength and staying well under half a second. PROPOSAL starting values: light 50 ms, heavy 100 ms, critical or finishing 150 ms; a blocked hit about two thirds; none on explosions, charges, a projectile's thrower, rapid fire, chain secondaries or crowds. The gameplay owner and the VFX designer bracket it (for example 0, 50, 100, 150, 250 ms) on a playable build before anyone fixes it; you supply the freeze-frame takes, not the bracket. The hit sound plays on the first freeze frame.
- Impact reads from approach, contact geometry, force direction, allowed deformation and consequence. Check with effects hidden: if removing the flash hides the impact, the pose or timing is unclear. When the camera is far back or shake is off, the weight must be in the pose, the timing and the sound.

## 6. Hand-offs
| With | Animator needs | Animator supplies | Accepted when |
| --- | --- | --- | --- |
| Owner | intent, personality, readability priorities | options, previews, trade-offs | decision recorded on the current revision |
| Art director | identity anchors, hook shapes, shape language, the art bible's motion line | key-pose black-fills for anchor checks | anchors visible at every key pose |
| Modeler (through the rigger) | shape, parts, silhouette limits, moving parts with room to move | contacts and the extreme-pose envelope (including costume near joints) | multi-view deformation renders |
| Rigger | parts, axes, limits, IK/FK, shoulder and hip controls, head orient, hand or finger controls, export joints, sockets | motion ranges, stress poses, failed poses (one rig note) | rig test clip and round trip |
| Gameplay | states, speed, windows, reaction windows, cancels, authority, interruption, play rate, hit-stop lengths | contact timing, displacement, feasibility, events | the same event contract in runtime tests |
| VFX | origins, directions, lifetimes, cancel | named events, attachment transforms, the freeze frame | effects align on hit, miss and interruption |
| Sound | cue meaning, intensity, surface data | accents, contact events, confirmed outcomes, stage names | no stale loop, no false hit cue, transient inside the sync window |
| UI | feedback meaning and priority | action-state and result events | UI never shows a false success |
| Marketing, film-director (promo and cutscene stills) | the one-sentence premise and the still's camera | the signature move's key pose from the set, set on the rig at that camera, shaded and black-fill | the still's pose matches the clip's key frame (`principles.md` P-06.11) |

Join at concept time: the animator says what is feasible, or that more is possible, while it is still cheap to change.

## 7. The timing grammar: tell, build, beat, hit, result
- Every action is a short story: a tell (the player learns what is coming), a build that rises, a small beat of held tension, one clear peak (the contact or release frame), and a result that starts after its cause, never with it. Tune the gaps in tenths of a second (3-frame steps at 30 fps).
- One peak per action: the hit is one frame where motion, VFX flash and sound transient meet; several competing peaks blur cause and effect.
- Uneven cadence: the gaps between beats differ, each for a reason; feel the rhythm like music ("swoop up, a little down, then the hit") and retime until it is not a metronome.
- After the peak, the motion lets the eye move on to the result: the striking part settles and quiets; the follow-through carries weight, not new attention.
- Size sets speed: an enormous creature has slower beats, longer settles and heavier contacts than a person; a giant at human speed reads small.
- One timing language for the game: the same attack always has the same tell and beats; similar actions of the same class share a tell family; motion personality matches the art bible's motion line.

## 8. Reduced motion and every player
- A tell, a contact and an outcome read from the pose and the silhouette alone, with effects hidden, sound off and colour removed. Effects, colour and sound add to the read; they never carry it alone.
- Reduced motion (the player's Roblox setting) removes camera-driven motion, shake and flashes, never the tell pose or the contact; if a clip leans on camera motion for its read, it fails.
- Nothing in a clip pulses or flickers faster than 3 times per second; a looping bob or pulse on a pickup or hazard follows its meaning: slow is safe, fast is urgent.

## 9. Paid random reveals
- An egg, crate or chest opened with real or bought currency has the same windup for every result: the same beats, the same length, the same poses up to the result frame.
- No near-miss motion (no "almost rare" shake), no rarity tint or rarity flourish before the result is shown; the tier's layers start only after the result frame, and a result worth less than its cost is not celebrated. Load `platform-policy`; the reveal rules belong to the game-designer.
