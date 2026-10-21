---
type: job
scope: universal
status: active
updated: 2026-10-21
source: "J015-T09 G2 test"
supersedes: []
---
> Author: film-director · claude-opus-5-5 · high · 2026-10-21. For the animator role (planned, not built: the lead holds this brief, J015-D7). Not sent. Format: `rules/messages.md` §2.

<intent>
Shots B and C are where the player's own avatar shows the change from intention to recognition, before the player sees the threat (reveal order: geography, alarm, object, reaction - here the alarm comes before the object on purpose). The avatar is whatever the player wears, so the realisation must read from the body and head, never from the face, and it must survive avatar heights from about 4.75 to 6.5 studs. Shots D and E belong to the guardian: a statue the player walked past wakes, finds the intruder with its eyes, and closes the route to the beacon with one planted hand, then waits. Its strike is a claim, not an attack on the player: it lands between the explorer and the beacon, and it ends in a pose the encounter can start from. All camera work is static, so the acting is the motion the eye follows.
Look through the refs and the nearby files in g2/ before you act; the greybox timings are proposals you may improve inside each fixed window.
</intent>
<spec>
id: J015-T09-ANIM                                  # held by the lead until the animator role exists (J015-D7)
from: film-director
to: animator
model: opus
effort: high
skills: [film-direction, <animator craft skill, planned>]
refs:
  - output/J015-g2/movie/boss-reveal_r5_animatic_silent.mp4   # take: timing, cameras, poses at the cuts; the bodies are proxies
  - knowledge/jobs/J015-film-director/g2/boards/contact-sheet.png   # take: C's head-up lean (panel C r2), E's planted hand; avoid: panel B's palm-up hand pose
  - knowledge/jobs/J015-film-director/g2/shot-table.md   # take: continuity ledger, before/after state per shot
  - output/J015-g2/checks/ghosts/ghosts_sheet.png   # take: the avatar range in C and E
fixed:
  explorer_B: frames 1-37; reach from the interact pose toward the beacon; stops short at frame 27 (B+26) after the light dies at frame 21; never touches the beacon   # shot list B; board B r1 rejected for a touch
  explorer_C: frames 38-73; head turn up and right starts frame 45 (C+7), 4 frames after the crack sound at frame 41; one step back to screen left lands by frame 72 (C+34); end pose weight on the back foot, head up toward screen right, right hand down   # shot list C, continuity ledger
  explorer_DE: stays at the step-back mark (-4.9, 0) facing the guardian; gaze follows the guardian's head   # ledger
  guardian_D: frames 74-137; rise from the bowed kneel 74-104; head lifts into the moonlight (head enters the shaft at frame 90, measured); gaze lands on the explorer by frame 124 (D+50, vocal cue); near (left) arm draws back from frame 126 (D+52); cut at frame 138 inside the anticipation   # shot list D, cue sheet
  guardian_E: frames 138-175; hand reaches the floor at frame 144 (E+6, slam cue, locked) at the planned mark between the explorer and the beacon; settled encounter-start pose by frame 168 (E+30), held to 175   # shot list E
  acting:
    explorer: {belief: "the beacon is a prize, the statue is decoration", stimulus: "the light dies before my hand reaches it; then stone cracks above me", tactic: "none: alone with the threat", decision: "stop reaching, look up, step back"}
    guardian: {belief: "I am the beacon's keeper; something took a step too close", stimulus: "the hand near the beacon", tactic: "claim, not attack: put my hand between the intruder and the light", decision: "wake, find the intruder, close the route, wait"}
open: [poses inside each window, holds, secondary motion, how the realisation builds, the guardian's weight and stone quality, the anticipation shape]
avoid: [a face-only reaction (lost at phone size and avatar faces vary), the explorer looking at the camera, the guardian hitting the explorer, any shake or fall of the explorer, a strike that hides the beacon from CAM_E]
owns: [content/film/boss-reveal/anim/]             # PROPOSAL path
not_in_scope: [camera changes, VFX, sound, rig changes (ask the character-rigger through a ticket), timing outside the fixed windows]
rules:
  - Body and head angle must read at phone size; check from the shot camera, not the animator viewport.
  - Keep the gesture readable for avatars from about 4.75 to 6.5 studs (Roblox body scales, knowledge/external/roblox-creator-docs/art/accessories/body-scale.md:24-36).
  - No change to a frame window without a shot-list revision (ticket to the film director).
  - The cinematic decides nothing on the server: no damage, reward or beacon pickup.
deliver: content/film/boss-reveal/anim/ (explorer B-C, guardian D-E) and silent grayscale key-pose thumbnails from CAM_B..CAM_E
checks:
  - C1: in a 30 fps capture from CAM_C, the stop of the reach, the head-up and the step back each read before frame 73, with the sound off
  - C2: from CAM_B, a visible gap between fingers and beacon in frames 21-37
  - C3: from CAM_E, the guardian's hand is on the floor at frame 144 and the beacon and exit stay visible to frame 175
  - C4: repeat C1 with the 4.75-stud and 6.5-stud avatars
return: hand-back to film-director (rules/messages.md §3); key poses first (G2 sample)
</spec>
