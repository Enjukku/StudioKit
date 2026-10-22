> Author: J018 maker game-designer · claude-opus-5-5 · high · 2026-10-22. Part of `game-design`. Built also from the owner's Riot transcripts (J018). Roblox defaults from the local docs mirror (`_api-reference/classes/StarterPlayer.yaml`: CharacterWalkSpeed 16; CharacterUseJumpPower defaults to true, so CharacterJumpPower 50 governs the jump, and CharacterJumpHeight 7.2 applies only when it is false). The full level review (route graph, the fixed checks C1-C19, walk-throughs) is the `level-design` skill; this file is what I decide and check as the owner of routes, cover, sight lines and blocking surfaces.

# Spaces: maps and modes as gameplay

## 1. The map is the board
- The map is the board the real game is played on; players notice it only when they need to. A bespoke map mechanic (teleporter, moving door, jump pad, hazard) stays in the background and comes forward only at the 1-3 moments I plan for it. In an obby or a simulator the mechanic may be the game itself: decide which layer is the board and which is the game, in writing.
- Spec line per map mechanic: the core activity it must not compete with, its planned moments, its default look (quiet).
- Check (the level review's C15, `level-design/references/review-artifact.md` §4): on the normal-round stills, outside its planned moments the mechanic is never the brightest or most saturated thing in view and shows no motion near a decision; the seconds of eye draw at speed come from the owner's play-test.

## 2. The stage's job
- Each stage brief starts with its job: the target experience, the four parts for this space (goal, opposition, decisions, rules), what it teaches, the session shape (first visit, return visit, short phone session), and the place's personality in 3-5 words (a place or a hero prop is designed like a character: "rigid, old, timeless").
- **A level is a puzzle with holes shaped like the player's tools.** For each space list the tools or abilities that solve it (jump, sprint, an ability, a build piece) and at least one non-obvious solution; a space no tool solves frustrates, a space solved by walking is no puzzle.
- **Conflict sits in the objective.** One sentence per mode states the conflict (attack to plant, defend to stop, steal and escape); the objective has a reason in the world's story so the environment can show it.
- Check: the brief has the job, the conflict sentence and the story reason before blockout; in the play-test each listed tool really solves its space.

## 3. Starts, routes and timing (in player metrics)
- **Spawns first,** then the route from spawn to the objective, then side areas.
- **Time, not distance.** Every route in seconds at the real walk speed (Roblox default 16 studs per second: 160 studs take 10 s; a game that changes it uses its own value from the game profile). PROPOSAL default: no walk over about 15 s without something to do or see; return trips (sell, restock, respawn to goal) get shortcuts, new views or things to do on the way. A ledge meant to be climbed stays under the game's jump height, measured in the place and written in the game profile (7.2 studs applies only when the character uses JumpHeight; Roblox's default uses JumpPower 50 instead, so measure it: probe in Studio before relying on a number); one meant to block stays clearly above it.
- **Plan the first seconds.** In round-based modes compute spawn-to-contact time per route (distance divided by walk speed) and mark where sides first meet; decide which meetings should be fast and which slow. Neither side reaches neutral space much faster than the other.
- **Paths face forward.** From spawn, routes to the objective do not turn back (multiplayer); a new player never gets lost. Default for team objective maps: two ways in per side per objective. One orientation convention across all maps (the shop always right of spawn, the exit always ahead), written in the game profile.
- Check: a route table (route, distance, seconds, what the player sees or does on the way) computed with Python from coordinates; spawn-to-neutral times per side within a small margin, and play-test win share per side; every main-route ledge measured against the jump height; the new map keeps every orientation convention from the spawn view; a walk capture from each spawn to each objective never turns the camera back; ways in counted per side per objective on the top-down capture (default two).

## 4. Cover, height and geometry
- Cover gives both sides options and a counter: for each objective list each cover piece, who uses it and how the other side beats it; an intermediate spot gives choice. No side has zero options.
- Play spaces stay mostly flat; every height change is intentional and listed with its reason; in a third-person or top-down phone game no surprise height hides a threat from the camera.
- Collision is as simple and predictable as the visible shape (players lose to opponents, not to the map): boxes on routes, decoration outside the collision envelope.
- Check: every cover piece has a counter; collision view along routes shows simple shapes and no snag points; captures along each route: any threat position far above or below the expected line is on the intentional list.

## 5. Hazards and boundaries
- **Every hazard has written rules** before art, VFX or code: entry effect (kill, or damage per second), what happens to items thrown or placed in it, how long its danger lasts, the visibility rule, the server owns the damage rule. Art and design must describe the same rule.
- A hazard shows where it comes from and what contains it (a vent, a rail, a fence).
- **A dead boundary can become risk and reward:** where a corner would just be closed off, a hazard can do the job and add a brave position (a small safe spot inside it that can still be countered).
- A boundary is dressed as something believable in the world (a cliff, a building, a river), chosen with the art director from 2-3 fictional answers, never an invisible or plain wall; collision matches what players see.
- Check: the hazard sheet (`preproduction/references/documents.md` §7) has every field; a QA case per rule; for each boundary, one line answers "why is this here in the world?"; the reward spot is used and counterable in play-tests.

## 6. Art stays inside the blockout
- Order: art-bible mood image → Studio grey box with plain Parts → play-tested → rough kit over the grey box → set dressing → mechanic visuals → lighting, atmosphere and polish last, dated after the last route change.
- Any art change that affects play (a box on a sightline, a texture on a route, collision, cover) comes to me first; the environment designer never moves collision, cover or sight lines silently.
- Where a surface's behaviour matters (shootable, breakable, climbable), the gameplay rule picks the material and one material means one behaviour; the same table drives footstep and impact sounds.
- I rank the environment work with the environment designer: play spaces and routes first, landmarks and first view next, filler last.
- Check: diff the dressed level's collision and routes against the approved blockout; every difference has my sign-off; the material audit matches the material-to-rule table.

## 7. Reads in the space
- The player instantly knows where to go, where they are, who is ally or enemy, what is dangerous, how much health and threat there is. Test in the busiest moment (many players plus effects), not in an empty scene; the most intense play space gets the strictest priority.
- Every interactive piece says "what I am" and "what you can do here" (a cliff that is clearly climbable), with one treatment used everywhere for each gameplay read (all climbable ledges look alike).
- Items on the ground are identifiable even partly hidden; item types differ in their top and side profiles.
- The first view after spawn frames the goal or main landmark; each zone or team has an identity symbol visible from its entry.
- Gameplay colours stay out of set dressing; the environment stays a calm backdrop in a narrower value range than characters and effects.
- A surprise (an ambush, a hidden reward) sits outside the bright focal light or behind a turn, never in the most lit spot.
- Places show who lives there and what happened (2-3 story facts per stage) at backdrop contrast, never competing with the gameplay read.
- Check: capture of the busiest moment at the game camera on a phone viewport: each critical fact found at a glance; items 30-50 % hidden behind a box are still named by type; a fresh reader names what each place is and what can be done there; the first-frame capture after spawn shows the goal as the strongest focal point; capture at the lowest graphics setting: every gameplay cue still present (the studio-operator sets the Studio quality level; if it cannot, the check is Unproven); in the grayscale capture each planned surprise sits outside the top focus, and testers do not spot it early; a fresh reader of the captures, without notes, states at least one story fact per main area; each zone's identity symbol is visible from its entry at the game camera on a phone viewport.

## 8. Secrets, and maps over time
- Small hidden secrets (a recurring mascot, a symbol, an event teaser) reward discovery; none blocks a route or weakens the play read.
- A map is never done: player evidence brings revisions months later, so map change requests with evidence go to the live backlog. Each new world takes players somewhere clearly new (an escape), with a palette, shapes and theme that differ from the previous ones.
- Check: count hidden items per map and confirm none sits on a route or decision point; a capture of the new world next to earlier worlds shows a clear difference.

## 9. My self-review of a space plan or blockout
- Mark dead space, no-man's land and oversized areas on a top-down capture; each is cut, shrunk or given a purpose.
- The route table, spawn-to-contact table, cover list and hazard sheet exist and match the blockout.
- Run the `level-design` review (all checks, Pass / Fail / Unproven); a re-review after fixes re-rates every check, not only the ones that failed, so rounds can be compared.
- Close with an honest recap: what works, what is too tame, too big or empty, and the next iteration.
