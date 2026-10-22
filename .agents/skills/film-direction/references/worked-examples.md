> Author: J018 maker film-director · claude-opus-5-5 · high · 2026-10-22. Reference for `film-direction`: built also from the owner's Riot transcripts (J018). Worked examples in our pipeline (Blender greybox and previs, ChatGPT boards, the shot-list tool, Roblox assembly through the Studio MCP). Every number here is a PROPOSAL or an example measurement, never a default. Check ids (P-, B-, R-) are the lines in `film-craft/references/review.md` §6.

# Worked examples

## 1. Boss entrance in a tower-defense game (hybrid: three authored shots, then play)
- **Problem and target.** Wave 10 brings the Swamp King; players keep building towers without noticing him. Target experience: thrill. Premise: "Everything small runs from the gate, and something huge steps out." Hook: the enemies the player has fought for nine waves are afraid. Sell list: (1) a boss is here, (2) he is big and slow, (3) he walks the middle lane, (4) towers still work.
- **Options for the key beat** (one greybox contact sheet each, phone size, equal finish): A, his shadow crosses the lane (scale by shadow); B, the small enemies flee toward the camera, then the gate bursts (alarm first); C, the lights die and one eye opens (the non-obvious one). Goal question: "which says *a boss is here* first at phone size?" Pick B: the fleeing crowd reads even at 667x375; C's eye measured 9 px tall in `look_check.py thumb` and lost; A read as weather. Rejection reasons recorded.
- **Shots and reads.** 1, wide on the lane: primary the fleeing enemies (motion toward the camera), secondary the dark gate. 2, low angle at the gate: tell (the gate cracks), build (dust trickles, the rumble rises), beat (a held moment of silence, PROPOSAL until the owner times it), peak (the gate bursts on marker `sfx.gate.burst`), result (the boss steps through, club glowing). 3, handoff on the game camera: the boss mid-lane, his club the brightest area, the towers lit, the build button visible.
- **Value plan.** Shot 1 calm and narrow; shot 2 wide, the boss underlit (this game's villain convention) and dark against the gate glow, written in the picture plan as a planned silhouette (B-06: the gate ranks first, the boss's box inside it, the boss darker than its ring); shot 3 the club ranks first among the named bright regions.
- **Scale.** In the shot 2 key frame the boss's mask height is about 4 times the nearest enemy's (B-05, MEASURED); he moves slower than the enemies.
- **Endings.** Skip lands on shot 3's state; on a retried wave a one-shot version plays (owner agreed); the server owns the wave start, the cinematic only shows it.
- **Checks run.** P-04 (pick recorded), B-04 (subject heights at phone size), B-05, B-06, B-10 (shot lengths 54, 30, 81 frames: uneven), R-04 (`log-diff` of the cut and cue log), R-07 (the handoff capture names boss, lane and build button).

## 2. New-world intro in a simulator (player-directed handoff)
- **Problem.** Players unlocking Crystal Caves do not know where the treasure is. Premise: "The cave mouth opens and the giant crystal shows the way." Target experience: exploring the unknown.
- **Options.** A, a flyover (rejected: long, the player does nothing); B, the player walks in and a crystal hum leads to the landmark (player-directed); C, a 2-shot door reveal, then control. Pick C with B's sound cue: the reveal is precise, then the player owns the discovery.
- **Picture.** Dark rock arch as framing foreground, the giant crystal in the lit midground as the tallest and brightest shape, the far cave quiet behind; the first collectible sits on the path line from the arch to the crystal.
- **Handoff frame.** The spawn camera frames the crystal (primary) and the first collectible (secondary); the HUD's collect counter is outside both.
- **Checks.** B-03 (key subjects stay out of the bars and the skip zone at the narrowest display), B-06 (the crystal ranks first; the sky patch at the top named and measured below it), R-07, R-10 (the crystal and the path still read in grayscale).

## 3. A door reveal in an obby (a 3-second in-play camera moment)
- **Problem.** Pulling a lever opens a door 60 studs away; players do not see it and wander. Camera mode: hybrid, one authored look, then control.
- **Beats.** Tell: the lever clunks. Build: a chain rattles along the wall toward the door (a flow line the camera follows). Beat: the camera settles on the door. Peak: the door slams open and light spills out on one marker. Result: the camera returns to the player's avatar, with the open door still in the background.
- **Access.** Reduced motion turns the pan into a cut; the door's light change reads in grayscale; the clunk has a visual twin (the lever moves).
- **Passes run** (sized at step 1): text options for the camera path, one blocking key frame from the authored look, the animatic with the clunk, rattle and slam markers, the Roblox lines. No option sheets, value strip, light variants, boards or two edit takes: one authored look has no key beat that needs them (n/a with that reason).
- **Checks.** B-03 and B-04 (the door inside the narrowest display and tall enough at phone size), B-06 (the door's spill of light ranks first), B-10, R-04, R-05 (repeated skip and repeat trigger give one result), R-10.

## 4. Victory after a confirmed win (round-based arena game)
- **Problem.** The winning team should feel the win; losers must not wait long. Starts only on the server's round-won event (D-40).
- **Picture.** The winners as one group silhouette on the podium, the team banner behind them as the brightest area; one peak (confetti burst and fanfare on one marker); losers' cameras stay on their own avatars.
- **Rhythm.** Short, because it plays every round; its length is set by the owner on the playable animatic. Skippable after the result is shown.
- **Checks.** R-14 (a test build where the server rejects the win: no victory sequence), B-05 (the group outline reads as a team at phone size), R-05.

## 5. A promo still from the boss entrance
- **Brief.** Marketing needs a key frame for the update thumbnail. The featured thing (the Swamp King) is the hero.
- **Build.** The shot 2 camera, re-framed for the 16:9 crop with room for the title; the boss's pose is the slam key frame from his animation set, set on the rig by the animator; three dust streams as flow lines through the club; gate debris as a dark foreground layer.
- **Order.** Composition and value pass on the clean frame (no dust, no glow); then colour; then effects.
- **Delivery.** Foreground, midground, background, lights and effects in named collections, so marketing can switch them.
- **Checks.** B-14 (layers and crops; `look_check.py silhouette --compare` of the still's black-fill with the clip's key-frame black-fill, both rendered from the still's camera, MEASURED), B-06 on the clean frame (the boss's club ranks first by p95 against the named dust and sky regions).
