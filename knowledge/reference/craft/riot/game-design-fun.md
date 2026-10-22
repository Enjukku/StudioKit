---
type: reference
scope: universal
status: active
updated: 2026-10-22
source: "J018 stage 1b: synthesis of knowledge/jobs/J018-riot-craft/extracts (owner-supplied Riot transcripts, 14 videos)"
supersedes: []
roles: [game-designer, progression-designer, live-ops-designer, level-design, art-director, vfx-designer, sound-designer, animator, ui-ux-designer, feature-builder, environment-designer, modeler, character-rigger, film-director, marketing, reference-images, orchestrator, architect, reviewer, qa-lead]
---
> Author: J018 synthesizer · claude-opus-5-5 · high · 2026-10-21

# Game design and fun

What a game is, what makes it engaging and fair, and how art, motion and sound serve play. Includes map design as gameplay and the rules that keep cosmetics fair.
GD-01 and GD-02 are the jobs of game art and feedback. GD-03 to GD-09 are the design core (four components, named fun, behaviour sets tone, movement, art and mechanics agree, art as fantasy, numbers as constraints). GD-10 to GD-15 shape a play session (progress, arc, opposition, fairness, luck and skill, prototype). GD-16 to GD-22 are rosters, cosmetics and genre. GD-23 to GD-33 are maps and modes as gameplay (board, puzzle, conflict, starts, neutral space, cover, hazards, blockout ownership, secrets, maps never done, escape).
Related: readable worlds in `world-level-readability.md`, anticipation in `weight-timing.md` (WT-01), UI in `ui-ux.md`.
Stage 1c (DestructionSimulator cross-check) added GD-34 (feedback follows the confirmed outcome) and GD-35 (honest paid random reveals); the (DS) line in GD-11 comes from the same check.

### GD-01 Every asset has jobs: clarity first, then feel, then style
- principle: Game art is everything the player sees and hears (characters, effects, enemies, environment, UI, animation, sound). It has three jobs: clarity (the player can read the game state), satisfaction (it responds and feels good) and a cohesive style that sets the emotional tone. Animation's version: clearly display actions, make motion and physics believable, inject personality. It is "way more than just a pretty wrapping".
- why: Art is the player's only window into the game state and the main carrier of feeling; a pretty asset that hides state or gives no feedback fails.
- apply: Every brief and review names which jobs the asset serves and how; reviewers check clarity first, satisfaction second, style third [inference: order from the video's sequence, R00a:92-94]. Animation reviews ask: what is happening, does it feel physically right, could it be any other character?
- check: For each asset in a game-camera capture answer three questions: can the player read what it is and does? does it respond to the player? does it look like the rest of the game (compare with the art-bible anchors)? A clip passes all three of the animation questions.
- mistake: Treating art as decoration ("are artists just making a pretty wrapping?", R00a:86); clips that are smooth but unclear or generic.
- examples:
  - R00a: characters, effects, enemies, environment, UI, animation and sound are all art with three jobs (R00a:70-94, 211-219).
  - R00b: the three goals of game animation (R00b:2941-2949).
- roblox_fit: Same; sound and UI count as art and get the same checks; clarity weighs more at phone size with many players.
- roles: art-director, game-designer, orchestrator, vfx-designer, sound-designer, ui-ux-designer, animator, modeler, environment-designer, reviewer
- also: style-identity, critique-feedback, visual-hierarchy
- sources: R00a-F01 (R00a:70-94, 211-219); R00b-F27 (R00b:2941-2949)

### GD-02 Every action gets immediate feedback; reached goals get a short celebration
- principle: Every player action gets clear, immediate feedback: a change on the press, a good feeling on success, a bad feeling on failure. The form varies (a meaty hit-pause, a big ceremony, flowing momentum) but every action responds. When a goal or threshold is met, a short celebration confirms it without stealing attention from play.
- why: Immediate feedback confirms the input and makes the result feel caused by the player; feedback size teaches what matters.
- apply: For every input, the feature builder and crafts list the feedback stack (animation, VFX, sound, UI) and when each starts. PROPOSAL defaults [inference]: first response on the press frame or the next; failures get a distinct negative cue, not silence; an in-play celebration lasts under about 2 s and bigger ceremonies run only on non-play screens.
- check: Frame-by-frame capture at 30 fps from press to first visible change (count frames); a distinct cue exists for both success and failure; trigger each threshold in a play-test: the celebration is visible and ends before the player's next decision (measure its length).
- mistake: Feedback only for success; delayed or absent response; celebrations that run long or stack across units.
- examples:
  - R00a: hit-pause, big ceremony, momentum and simple run-and-jump as kinds of satisfaction (R00a:136-164).
  - R06: two Invokers on the board trigger a short trait celebration; in the real game it "wouldn't last that long" (R06:30-33, 74).
- roblox_fit: Play the small attempt cue on the client at once and the big layer only on the server-confirmed result (GD-34, UP-19; load `networking-security`); trigger celebrations with ParticleEmitter:Emit plus a Sound. Hit-stop is done by pausing or slowing animation tracks and effects (verified: see VR-22).
- roles: vfx-designer, sound-designer, animator, ui-ux-designer, game-designer, progression-designer, feature-builder, qa-lead
- also: vfx-reads-timing, sound, ui-ux, weight-timing
- sources: R00a-F03 (R00a:136-164); R06-F02 (R06:30-33, 74)

### GD-03 A game needs a goal, opposition, decisions and rules
- principle: A game has four components: a goal, opposition (something to overcome), decisions (ways past the opposition) and rules (the framework). Remove one and it is an activity, not a game.
- why: Eating cereal is not a game until rules and opposition are added; tennis is.
- apply: Each loop, mode or mini-game spec states all four in one line each; a section, boss or mini-game without real decisions is flagged.
- check: In the spec each of the four can be named; an empty "decisions" line fails.
- mistake: Activities with no opposition or no decision [inference].
- examples:
  - R00d: tennis is a game; eating cereal is not (R00d:5171-5205).
- roblox_fit: Applies to obbies, simulators and minigames alike.
- roles: game-designer, progression-designer, level-design
- also: none
- sources: R00d-F21 (R00d:5171-5205)

### GD-04 Name the target experience, not "fun"
- principle: "Fun" is not a useful target. Name the specific experience (alternate fantasy, thrill, fellowship, mastery of a challenge, exploring the unknown, creativity and expression) and test every addition against it; without it, the team pushes conflicting kinds of fun.
- why: A named type gives every craft a target; additions that serve another fun type dilute the core (narrative is core for some games, not for League).
- apply: The game profile and every feature brief name one or two target experiences; art, sound, VFX and UI briefs quote them. Any proposed addition (story, cutscene, extra system) is checked against them and filed if it does not serve them.
- check: Each brief and review states the experience it serves; a proposal review asks "which target experience does this serve?" and work that serves another is flagged.
- mistake: Briefs that say "make it fun"; "adding unnecessary story elements to a game like League" (R00d:5265-5271).
- examples:
  - R00d: the list of fun types (R00d:5213-5241); conflicting fun from adding what works elsewhere (R00d:5243-5271).
- roblox_fit: Roblox games are often social, so fellowship is a common target [inference].
- roles: game-designer, art-director, orchestrator, marketing, progression-designer, film-director, live-ops-designer
- also: style-identity, critique-feedback
- sources: R00d-F22 (R00d:5213-5241); R00d-F23 (R00d:5243-5271)

### GD-05 Behaviour sets the tone before art does
- principle: Mechanics shape what a thing feels like even without art: a cube that damages the area around it and then disappears is a bomb; a larger area raises the feeling of danger and power. Tuning numbers are tone tools, not only balance.
- why: Players read objects by what they do.
- apply: Write an ability's or object's behaviour first and check it already implies the theme; VFX and sound then support that behaviour (area size, duration).
- check: Greybox test: with placeholder Parts only, a tester says what the object is, and it matches the intended theme.
- mistake: Relying on art to make a behaviour feel like something it does not do [inference].
- examples:
  - R00d: an innocent cube on a grid turned into a scary explosive through mechanics (R00d:5323-5363).
- roblox_fit: Greybox objects from Parts are cheap to test in Studio [inference].
- roles: game-designer, vfx-designer, sound-designer, feature-builder, progression-designer
- also: vfx-reads-timing
- sources: R00d-F25 (R00d:5323-5363)

### GD-06 Movement patterns give enemies character
- principle: An enemy's movement pattern alone gives it personality and theme (hop = frog, dash-and-stop = ninja, shamble = zombie, grid steps = robot).
- why: Players recognise creatures by how they move before reading the model.
- apply: Specify a distinct movement pattern per enemy type and let animation and model support it.
- check: Run the enemies as plain blocks in Studio: a tester tells them apart and guesses the theme from movement alone.
- mistake: All enemies moving the same way with different skins [inference].
- examples:
  - R00d: forward movement plus a jump becomes a frog; ninja, zombie, robot, snake, tornado (R00d:5365-5391).
- roblox_fit: Distinct movement also helps when many enemies share a small phone screen [inference].
- roles: game-designer, animator, feature-builder, level-design, character-rigger
- also: character-design, rhythm
- sources: R00d-F26 (R00d:5365-5391)

### GD-07 Art and mechanics must promise the same thing
- principle: What an object looks like must match what it does: blocking objects look solid, walkable openings are walkable, cover looks like cover, and a character's role (tank, assassin) matches its design. When art and mechanics disagree, play feels unnatural and unfair.
- why: Players predict behaviour from appearance; a broken prediction feels wrong.
- apply: Any object that looks soft, open or weak behaves that way, or is redrawn; role briefs bind art and design to one reading.
- check: Play-test list of every mismatch between appearance and behaviour (collision on an open doorway, bullets stopped by leaves); each is fixed or justified.
- mistake: "open doorways that you can't walk through" (R00d:5413-5415).
- examples:
  - R00d: bushes that stop bullets, mailboxes that stop a speeding truck; original Shen was a tank to designers and a stealth assassin to artists (R00d:5393-5423).
- roblox_fit: Check CanCollide and invisible collision against the visuals [unverified].
- roles: game-designer, art-director, environment-designer, modeler, level-design, character-rigger, reviewer, qa-lead
- also: world-level-readability, character-design
- sources: R00d-F27 (R00d:5393-5423)

### GD-08 Art turns rules and numbers into a fantasy players build around
- principle: A system could run on rules and numbers alone; art gives them a fantasy so players feel they fight with warriors and cast spells, and players even choose by theme (an elf deck) over the optimal choice.
- why: Immersion is part of the fun; collecting by theme is a motive of its own.
- apply: Each system's items and stats get a visual identity and theme families players can collect or build around.
- check: Each item in a set belongs to a named theme family with a shared visual (motif, palette).
- mistake: Shipping items as numbers with generic art [inference].
- examples:
  - R10: he built Magic decks by theme and lost but had fun (R10:357-387).
- roblox_fit: Pets, towers and items collected by theme are common on Roblox [inference].
- roles: game-designer, progression-designer, art-director, ui-ux-designer, live-ops-designer, marketing
- also: style-identity
- sources: R10-F15 (R10:357-387)

### GD-09 Mechanics and numbers are design constraints for art
- principle: Rules and numbers (even health points) constrain the look; art shows what a mechanic does and how tough something is.
- why: The look must tell the player the mechanic and its strength.
- apply: Game-design briefs pass the mechanic and its numbers (HP, range, speed) to art, VFX and animation; the visual expresses them (a high-HP unit looks heavy; a pull ability shows the pull).
- check: Show the asset without text: a fresh agent says what it does and how tough it is, and both match the spec.
- mistake: Art made before mechanics, which then contradicts them [inference].
- examples:
  - R00a: the concept artist finds what an ability that pulls enemies close looks like (R00a:644-662).
- roblox_fit: No change.
- roles: game-designer, vfx-designer, animator, modeler, progression-designer, art-director
- also: references-ideation, vfx-reads-timing
- sources: R00a-F17 (R00a:644-662)

### GD-10 Make progress toward the goal visible
- principle: Players must see how they progress toward the goal; progress markers also tell the other side when to push.
- why: A measurable goal gives feedback and drives decisions on both sides.
- apply: Each goal has a visible progress measure (checkpoints, laps, position, bar, count); midpoints are shown as events. PROPOSAL default: a checkpoint or progress update at least at the halfway mark [inference].
- check: At any moment in a play-test capture, a tester says how far they are from the goal.
- mistake: "like playing a racing game without knowing what lap you're on" (R00d:5478-5482).
- examples:
  - R00d: Overwatch payload checkpoints tell both teams the state (R00d:5426-5484).
- roblox_fit: No change.
- roles: game-designer, ui-ux-designer, progression-designer, level-design
- also: ui-ux
- sources: R00d-F28 (R00d:5426-5484)

### GD-11 Build a climactic arc toward the resolution
- principle: Build rising tension toward the goal's resolution, with enough difficulty and drama that every player feels it.
- why: Rising tension makes the ending feel earned.
- apply: Design an escalation near the end: a boss at low health changes phase and "brings the heat"; last-kill or last-point moments get louder sound, stronger VFX and a music change.
- apply (DS): In a level, lay the arc out in space: easy, readable targets near spawn, bigger, harder or more valuable ones further in, and the climax piece (the landmark, the boss, the most iconic structure) near the end (DS:level-design/SKILL.md:45, 84).
- check: Plot intensity over time (enemy attack rate, music layer, VFX density): it rises toward the end, not flat.
- mistake: A flat finish [inference].
- examples:
  - R00d: a boss at low health brings the heat; the last kill: one team against the wall, the other feeling the hunt (R00d:5486-5522).
- roblox_fit: No change.
- roles: game-designer, sound-designer, vfx-designer, film-director, level-design, progression-designer
- also: rhythm, sound
- sources: R00d-F29 (R00d:5486-5522)

### GD-12 Give opposition and the tools to beat it; the right frustration
- principle: Opposition makes a game engaging but can frustrate; some frustration is fine if it is the right kind. The designer gives both the opposition and the tools to overcome it.
- why: Challenge creates the satisfaction of winning.
- apply: For each obstacle the spec names the counter tool or skill; tune difficulty so the counter is learnable.
- check: Every obstacle in the spec has a counter; in play-tests, testers attribute failures to their own mistakes.
- mistake: Removing all challenge to avoid frustration [inference].
- examples:
  - R00d: a Ninja Gaiden boss lost to repeatedly, finally beaten at the last second (R00d:5525-5627).
- roblox_fit: No change.
- roles: game-designer, progression-designer, level-design
- also: none
- sources: R00d-F30 (R00d:5525-5627)

### GD-13 Fairness comes from clear expectations and consistency
- principle: Clear expectations and consistent behaviour make a game feel fair, separate from difficulty. Unpredictable behaviour feels unfair because the player cannot learn from failure.
- why: Learnable failure keeps players trying; random-feeling failure makes them quit.
- apply: Every threat telegraphs before it hits (anticipation, VFX warning, sound cue) and behaves the same every time; no hidden trap right after an obstacle.
- check: After each play-test failure, the tester says what killed them and what to do differently; the same attack always has the same tell (compare captures).
- mistake: "Players overcome one obstacle only to be blindsided by the next" (R00d:5656-5658).
- examples:
  - R00d: troll Mario Maker levels are funny to watch, bad for most games (R00d:5628-5666).
- roblox_fit: Tells must read on a phone at the game camera [inference].
- roles: game-designer, level-design, vfx-designer, animator, sound-designer, qa-lead
- also: weight-timing, vfx-reads-timing
- sources: R00d-F31 (R00d:5628-5666)

### GD-14 Place luck and skill on purpose
- principle: Luck and skill shape opposition. Pure luck suits games not meant to need skill; competitive games leave little to chance; a mix (random start, skill-driven play) lets skilled players come back and newer players still win sometimes.
- why: Luck keeps outcomes open; skill makes wins feel earned.
- apply: Decide where randomness sits in the loop (start, loot, drops) and where skill decides; write the balance per mode for the target audience.
- check: Simulate or play-test: a skilled player can recover from a bad random start; a new player can sometimes win.
- mistake: Randomness placed by accident [inference].
- examples:
  - R00d: Candy Land (luck); Counter-Strike, League, Street Fighter (skill); PUBG and Fortnite random start and loot, skill in action (R00d:5667-5743).
- roblox_fit: Paid random items carry platform rules; load `platform-policy` when randomness is bought.
- roles: game-designer, progression-designer, live-ops-designer
- also: none
- sources: R00d-F32 (R00d:5667-5743)

### GD-15 Prove the fun with the crudest prototype before art
- principle: Build the exciting part in the simplest way possible (paper, plain blocks, "say something is red and it deals damage") and play it; art and VFX start only after a play-test says the hook works.
- why: Cheap prototypes test the fun before expensive art; a hook can take months to lock.
- apply: Prove the core loop or mechanic in a greybox Studio build (plain Parts, a damage script, a stand-in colour that cannot be mistaken for final art) and play-test it before any art brief.
- check: A play-test log with a written verdict exists before the art brief, and the art brief cites it.
- mistake: Polishing the look of a mechanic nobody has played.
- examples:
  - R00d: make or extend a game with paper and cards (R00d:5767-5785).
  - R09: a red crate texture stood in for lava; art came after (R09:52-58, 70, 310-316).
- roblox_fit: A Studio play-test through the Studio MCP is the "press play"; a damage Part is the cheap stand-in [unverified for a specific API].
- roles: game-designer, level-design, environment-designer, feature-builder, orchestrator
- also: process-iteration
- sources: R00d-F33 (R00d:5767-5785); R09-F02 (R09:52-58, 70, 310-316)

### GD-16 Cosmetics never change the gameplay read or cost gameplay
- principle: Gameplay comes first. A cosmetic keeps the character reading as the role it plays (a fragile ranged carry stays slim and sharp, never tanky), keeps the base proportions, takes no extra screen room and never hides combat information; players must not pay for a disadvantage.
- why: Players decide live (dive, avoid, protect) from how a character looks; a skin that blocks or confuses is a paid disadvantage.
- apply: Each class has a silhouette mass and shape rule (ranged = slim and sharp, tank = bulky); every variant is checked against it. Every cosmetic brief (skin, trail, aura, pet) sets a screen-footprint limit; cosmetic VFX stay below combat-effect brightness [inference].
- check: Black-fill silhouette area and width-to-height ratio of variant versus base at the game camera stay within the class band (PROPOSAL default: within about 10 % of base area [inference]); phone-size captures with and without the cosmetic compare covered screen area, and combat cues stay visible.
- mistake: "Completely decked out in medieval armor ... really tanky" (R01); "radically changing" the base item (R12).
- examples:
  - R01: Caitlyn must stay a fragile but dangerous carry; Soraka may get edgier but not change role (R01:700-738).
  - R12: a skin "shouldn't take a lot of room on your screen"; "you shouldn't pay for the disadvantage" (R12:48-50, 390-394).
- roblox_fit: Third-person and top cameras show cosmetics on many players at once; keep them from hiding hits and enemies; load `platform-policy` for paid items.
- roles: art-director, game-designer, modeler, reference-images, vfx-designer, live-ops-designer, marketing, reviewer
- also: shape-silhouette, character-design, world-level-readability
- sources: R01-F44 (R01:700-738); R12-F06 (R12:48-50, 390-394)

### GD-17 Cosmetics refresh repeated play without changing balance
- principle: Skill games create routine; cosmetics change how the routine feels (the same coffee in a new café), which makes repetition easier and more fun.
- why: Novelty in presentation renews motivation without changing balance.
- apply: Plan cosmetics as routine-breakers for repeated loops; they change no stats (GD-16).
- check: Cosmetic items change no stats in the data tables [inference].
- mistake: Cosmetics that alter balance [inference].
- examples:
  - R12: the coffee-shop analogy (R12:251-260).
- roblox_fit: Cosmetics are a common Roblox monetisation path; `platform-policy` applies to paid items [unverified].
- roles: game-designer, live-ops-designer, progression-designer, marketing
- also: style-identity
- sources: R12-F37 (R12:251-260)

### GD-18 A new character starts from the roster gap
- principle: A new character's design starts from what the game needs to fill ("we need a mage or a front line"); that role dictates many visual decisions.
- why: A character that fills a clear role reads as that role and has a place; taste-only designs may duplicate one [inference].
- apply: Before the reference-images brief for a character, unit, pet or tower, the game designer states its role and the brief lists it; the art bible maps role to shape and colour cues. PROPOSAL default: one role per character, in the brief header [inference].
- check: A tester names the role from the image alone; count roster entries that share that role and look.
- mistake: Designing only from favourites (R08:55-56).
- examples:
  - R08: TFT gameplay asks for "a mage" or "a front line" and that dictates the character (R08:50-56).
- roblox_fit: The role must read from the third-person or top camera at phone size [inference].
- roles: game-designer, art-director, modeler, character-rigger, orchestrator, reference-images
- also: character-design
- sources: R08-F01 (R08:50-56)

### GD-19 A mode change re-checks the whole roster
- principle: Changing the core mode can make existing units too strong or too weak.
- why: Kits tuned for one mode interact differently in another.
- apply: After any mode change, re-review every unit's balance.
- check: A balance pass list covering every unit exists for the new mode.
- mistake: Assuming old tuning carries over [inference].
- examples:
  - R11: Katarina "too potent" in 2v2 tag (R11:32-34).
- roblox_fit: Same.
- roles: game-designer, progression-designer, live-ops-designer, orchestrator
- also: none
- sources: R11-F31 (R11:32-34)

### GD-20 Choose themes from data; combine proven themes and tune the maturity
- principle: Which character gets which theme is backed by data; anyone may pitch; a strong pitch can combine existing themes and lower the maturity for a cuter take.
- why: Data shows demand; combining proven themes lowers risk.
- apply: Live-ops and game designers pick variant themes from player data; pitches cite the themes they combine and the maturity level.
- check: Each theme pitch lists its data and source themes.
- mistake: Picking themes by taste alone [inference].
- examples:
  - R01: Cafe Cuties combined food themes with a maid look, "taking a little bit of the more mature vibe out of it" (R01:484-489, 520-537).
- roblox_fit: Young audience: lower maturity is the default [inference]; load `market-trends` for data.
- roles: game-designer, live-ops-designer, marketing, art-director, orchestrator
- also: style-identity, references-ideation
- sources: R01-F32 (R01:484-489, 520-537)

### GD-21 Low mental load on the player's own character
- principle: While tracking the opponent, the player must not have to work out what their own character is doing; every move is recognisable at its key pose.
- why: Attention goes to the threat; an unclear own character breaks the input-feedback loop.
- apply: Animators make each attack's key pose show the designed hook clearly; game designers make own-character feedback readable without looking at it directly.
- check: Frame-by-frame capture: at each move's key pose, the move is identifiable from the silhouette alone.
- mistake: Own-character moves that look alike [inference].
- examples:
  - R11: animators take designed elements "to create really strong key poses" (R11:116-121).
- roblox_fit: In a third-person camera the player sees their own back, so the readable cues sit on the back and outline [inference].
- roles: game-designer, animator, art-director, vfx-designer, ui-ux-designer, qa-lead
- also: weight-timing, shape-silhouette
- sources: R11-F09 (R11:116-121)

### GD-22 Find the genre's demands first
- principle: Do not assume you know how to design for a genre; design is "the best solution given very particular sets of parameters". Some genre conventions exist for a reason (they let new players in) and stay.
- why: Priorities differ by genre, camera and play style.
- apply: Before any craft brief, list the game's parameters from the game profile (camera, screen size, player count, session pace, input) and judge the design against them.
- check: The brief states the parameters and the review cites them.
- mistake: Confidence "purely due to lack of challenge" (R11).
- examples:
  - R11: fighting-game clarity conventions kept even though 2XKO wants to look new (R11:136-139, 391-411).
- roblox_fit: Roblox parameters: phones, touch, third-person or top-down camera, many players, engine budgets.
- roles: game-designer, art-director, orchestrator, architect, ui-ux-designer, level-design, environment-designer
- also: style-identity, references-ideation
- sources: R11-F11 (R11:136-139, 391-411)

### GD-23 The map is the board: map mechanics stay in the background
- principle: The map is the board the real game is played on; players should not notice it except when they need to. Bespoke map mechanics stay in the background and come forward only at moments the designers planned.
- why: A mechanic that constantly demands attention takes "a lot of mind share" (R09:40) from the core activity.
- apply: For every map mechanic (teleporter, moving door, hazard, jump pad), the spec states the core activity it must not compete with and the 1-3 planned moments it comes forward; environment and VFX keep its look quiet by default [inference].
- check: Capture a normal round at the game camera: count seconds the mechanic draws the eye (motion, glow) outside its planned moments; target near zero [inference].
- mistake: A mechanic so "gamey" it dominates the map ("lava is a little bit too gamey for VAL", R09:38).
- examples:
  - R09: VALORANT's teleporters, fall-offs and rotating doors stay background to the shooting (R09:38-51).
- roblox_fit: In obbies and simulators the mechanic may be the core activity; decide which layer is the board and which is the game [inference].
- roles: game-designer, level-design, environment-designer, vfx-designer, art-director
- also: world-level-readability
- sources: R09-F01 (R09:38-51)

### GD-24 A level is a puzzle with ability-shaped holes
- principle: Levels are "glorified puzzles": the player's abilities are the pieces that fit the holes. Keep them intriguing but not too frustrating.
- why: Spaces that need the player's tools make those tools meaningful; too hard reads unfair.
- apply: For each space, list which tools or abilities solve it and at least one non-obvious solution [inference].
- check: Play-test: each listed tool really solves its space; no space is solved by no tool (frustration) or by simply walking (no puzzle) [inference].
- mistake: Spaces that ignore the player's tools [inference].
- examples:
  - R09: smokes, flashes and movement abilities are the puzzle pieces of each site (R09:96-102).
- roblox_fit: For obbies the pieces are jump, sprint and timing [inference].
- roles: game-designer, level-design, progression-designer
- also: world-level-readability
- sources: R09-F05 (R09:96-102)

### GD-25 Build conflict into the objective; tie it to the world's story
- principle: A clear conflict built into the objective (attack to plant, defend to stop) generates the gameplay questions; tying the objective to the world's story gives art something to express.
- why: Players need something to overcome; lore turns the objective into a place.
- apply: The game designer states the conflict per mode in one sentence; the environment designer gets the lore reason for the objective so the place can show it [inference].
- check: The spec has the conflict sentence and the lore reason before blockout.
- mistake: An objective with no conflict or no story reason [inference].
- examples:
  - R09: the spike steals radianite; each map shows radianite differently (R09:154-182).
- roblox_fit: Applies to any objective mode.
- roles: game-designer, level-design, environment-designer, film-director, marketing
- also: world-level-readability, style-identity
- sources: R09-F10 (R09:154-182)

### GD-26 Plan the first seconds from the round-start positions
- principle: Know where players start each round; do not build the map around them, but plan what the opening looks like, because an early fight in one area cascades into decisions everywhere. Sometimes a fast fight is wanted, sometimes slow space-taking.
- why: Opening timings set the pace of a round.
- apply: Compute spawn-to-contact times per route (walk speed x distance) and mark where teams first meet; the game designer decides which meetings should be fast [inference on the method].
- check: A table of spawn-to-contact times per route; play-tests confirm the intended first fights.
- mistake: Ignoring start positions, so opening fights happen by accident.
- examples:
  - R09: on Ascent a fast fight across mid off the barrier drop dictates how both teams play mid (R09:234-262).
- roblox_fit: Round-based games with team spawns; default WalkSpeed 16 studs per second (verified: see WL-29).
- roles: level-design, game-designer, architect
- also: rhythm, world-level-readability
- sources: R09-F13 (R09:234-262)

### GD-27 Neither side takes neutral space too easily
- principle: Check how easily each side takes the neutral space; if one side takes it too easily the map feels sided.
- why: A side stuck at its entry feels the map is against it.
- apply: Compare spawn-to-neutral times for both teams [inference].
- check: Times within a small margin; play-test win share per side.
- mistake: Neutral space too easy for one side.
- examples:
  - R09: defenders taking neutral easily puts attackers "on their heels" (R09:508-515).
- roblox_fit: Live-ops can monitor side win rates.
- roles: level-design, game-designer, live-ops-designer
- also: world-level-readability
- sources: R09-F26 (R09:508-515)

### GD-28 Cover gives both sides options and a counter
- principle: Give defenders decent cover on the objective so attackers must solve problems; give both sides options, including an intermediate spot, and ask whether a cover piece feels weird to fight around for the other side.
- why: Options let players play outside "the traditional playbook"; both sides must feel they have a chance.
- apply: For each objective list the cover pieces, who uses each and how the other side counters it [inference].
- check: Every cover piece has a counter; no side has zero options.
- mistake: Cover with no counter [inference].
- examples:
  - R09: a middle cover box for attackers, debated "maybe it should just be one box?" (R09:326-330, 437-454).
- roblox_fit: Applies to team modes.
- roles: level-design, game-designer
- also: world-level-readability
- sources: R09-F17 (R09:326-330, 437-454)

### GD-29 Turn a dead boundary into a risk and reward
- principle: Where a corner would just be made unplayable, a hazard can do the same job and add depth: players may enter briefly, and a small safe spot inside it creates a brave position with risk and reward.
- why: Bounds that do something create stories and choices.
- apply: Each hazard is marked with why it exists (boundary), what entering costs and any risky reward spot [inference].
- check: Play-test: the reward spot is used and is fair (it can be countered).
- mistake: Plain kill zones with no choice [inference].
- examples:
  - R09: a lava pit boundary with a floating brick where a movement character can hold an off-angle (R09:298-326, 352-353, 1116-1122).
- roblox_fit: Kill bricks are a familiar Roblox idiom; depth comes from the reward spot [inference].
- roles: level-design, game-designer, environment-designer, vfx-designer
- also: world-level-readability
- sources: R09-F15 (R09:298-326, 352-353, 1116-1122)

### GD-30 Every hazard has written rules
- principle: A hazard needs explicit rules: does it kill or damage, and what happens to items thrown or placed in it.
- why: Art, VFX and code can make it readable only once the rule is fixed; players need consistency.
- apply: A hazard spec table: entry effect (kill or damage per second), items placed in it (destroyed after N s), visibility rule [inference format].
- check: A QA test case per rule; art and design describe the same rule.
- mistake: Artist and designer assuming different rules ("it could kill you, or it would still like bring you down?").
- examples:
  - R09: lava kills; a molly thrown under the bridge would probably just break (R09:586-594).
- roblox_fit: The server owns the damage rule (load `networking-security`) [inference].
- roles: game-designer, feature-builder, vfx-designer, level-design, qa-lead
- also: world-level-readability
- sources: R09-F16 (R09:586-594)

### GD-31 Art stays inside the blockout's gameplay
- principle: Art follows the designer's gray box; any change that affects play (a box, a texture on a sightline, collision) is checked with the designer first.
- why: Outside those limits "you start getting an unfun game"; crafts working in isolation make a mediocre game.
- apply: Environment agents never move collision, cover or sightlines from the approved blockout without a level-design sign-off.
- check: Diff the dressed level's collision and routes against the blockout; every difference has a sign-off.
- mistake: "everybody is in their own isolation ... doesn't necessarily mean it's better for the game" (R02:466-470).
- examples:
  - R02: an embedded designer on VALORANT's environment team (R02:452-470).
- roblox_fit: None.
- roles: environment-designer, level-design, game-designer, orchestrator, modeler
- also: world-level-readability, cross-craft
- sources: R02-F25 (R02:452-470)

### GD-32 Hide small secrets that reward discovery
- principle: Small hidden collectibles or mascots reward discovery and feed community theories.
- why: Discovery is fun beyond the core loop.
- apply: Hide a recurring mascot or symbol per map; tie hidden items to releases (event teasers).
- check: Count hidden items per map; none blocks a route or hurts readability.
- mistake: Secrets placed where they confuse the play read [inference].
- examples:
  - R02: Tactibear on VALORANT maps; Bard logos on the Rift for his release, which players connected into patterns (R02:368-386, 918-934).
- roblox_fit: Fits Roblox hunts and badges.
- roles: game-designer, live-ops-designer, level-design, environment-designer, marketing
- also: world-level-readability
- sources: R02-F19 (R02:368-386, 918-934)

### GD-33 A map is never done; new worlds are an escape
- principle: Maps are revisited from player feedback months after the art was finished; each new world or update should take players somewhere clearly new, an escape from the everyday.
- why: Revisits keep the game healthy; novelty and escape are why players enjoy a new world.
- apply: Live-ops keeps map change requests with evidence in the backlog and art budgets time for returns [inference]; new worlds state their "escape" in the theme brief and differ clearly from previous ones.
- check: Compare a capture of the new world with previous worlds: palette, shapes and theme differ clearly; the backlog holds map revisits with evidence.
- mistake: Treating a map as finished forever; new worlds that look like the last one [inference].
- examples:
  - R09: "you know that map you took like so long to build? ... we want to update it" (R09:972-987).
  - R13: TFT changes worlds every four months: space, K/DA arena, cyber city (R13:174-178, 914-926).
- roblox_fit: Roblox's content-cadence guide lists playable maps and levels among recurring content updates (knowledge/external/roblox-creator-docs/production/game-design/content-updates.md:13, 25-34); load `live-ops-design` (lead fix 2026-10-22: documented, not an inference).
- roles: live-ops-designer, level-design, environment-designer, game-designer, art-director, marketing
- also: style-identity, process-iteration
- sources: R09-F47 (R09:972-987); R13-F39 (R13:174-178, 914-926)

### GD-34 Feedback follows the real outcome: a small cue on input, the big layer on confirmed success
- principle: Every input gets an instant small cue, but the big response (punch layer, celebration, reward sound, shake) plays only on the confirmed result: the hit landed, the break happened, the server accepted the sale. Its size is graded by a real cause the player can learn (material, force, weak point, chain size, rarity), never amplified past the outcome and never random. When confirmation is slow, show a pending state, never an early success.
- why: DS's evidence base reports a pre-registered study (n=1,699) in which feedback tied to success raised felt competence, while amplified feedback not tied to success lowered it (n=678), and a four-build study in which medium feedback beat extreme; raising intensity alone changed nothing measurable. Celebrating before the server answers shows players a success that may be taken back.
- apply: For each action the feedback stack (GD-02) has two rows: the attempt cue (on the input frame, small, never covering the impact point or the next contact) and the outcome response (on the confirmed event, scaled by its tier). Fix a flat effect by checking outcome link, truth, readability and timing before raising size, brightness, count or length. Escalation (combo, streak, chain) steps only at real outcome thresholds, adds one layer or one hit-stop tier at the impact point, is named by a short text label (x2, x3, CRIT) that reads with particles off, and resets visibly after idle. PROPOSAL default [inference, DS start value]: show a pending state when confirmation takes more than about 100 ms.
- check: Send a request the server rejects: no big layer, celebration or reward sound plays. Compare miss, hit, blocked, break and big break with sound off: all five are distinct. Disable particles: tier labels still read. No fix note changes only size, brightness, count or length.
- mistake: A big swing effect with a weak result; a coin shower before the purchase settles; escalation that rises while the player misses; tiers graded by a random roll.
- examples:
  - DS: a sell flow with no windup before confirmation; spark, fountain and "+N gold" on the confirmed sale; burst size in three steps by sale size (DS:vfx-design/references/moment-recipes.md:140).
- roblox_fit: Play the attempt cue on the client at once; play the outcome response when the server's confirmation reaches the client (remote event or replicated state); a predicted hit that the server rejects never shows the confirmed-hit layer (load `networking-security`) [inference].
- roles: game-designer, vfx-designer, sound-designer, ui-ux-designer, animator, feature-builder, architect, progression-designer, reviewer, qa-lead
- also: vfx-reads-timing, ui-ux, sound
- sources: DS:vfx-design/SKILL.md:47; DS:vfx-design/references/juice-repetition-sync.md:13-19, 25-33, 46-52, 69-76, 80-86, 109-111; DS:vfx-design/references/elements.md:34, 154; DS:vfx-design/references/moment-recipes.md:23-24, 140; DS:vfx-design/references/scene-and-clutter.md:118, 154; DS:vfx-design/references/review.md:55; DS:gui-ui/SKILL.md:24; DS:gui-ui/references/ui-effects.md:11

### GD-35 Paid random reveals are honest
- principle: When players pay (directly or through bought currency) for a random result, the reveal must not mislead: odds for every outcome are shown before purchase; the windup is the same for every result; escalation and rarity colour start only after the result is shown; a lower result never shows a higher tier's layers (no near-miss); a result worth less than its cost is not celebrated; luck effects never suggest better odds than the numbers.
- why: A reveal that hints at a rarer result than the roll is a near-miss trick that misleads players, many of them children, and breaks platform rules on paid random items.
- apply: The reveal spec has one shared windup (same beats and length for every tier), the result frame, then a tier ladder that adds layers with rarity (ring, rays, crescendo, a unique motif; for sound the crescendo is added notes, register and tail, never added loudness, results within 1 LU (lead fix 2026-10-22: sound-design D-03 is stricter than 'crescendo'); pure white only for the top tiers) and names the tier in text and frame shape, not by colour alone. After the result is confirmed, a tap skips to it; batch opens give only the best result the full ceremony. The odds are shown as numbers summing to 100 % before purchase (lead fix 2026-10-22: platform-policy rules.md §A requires the sum) and never covered by effects; they update while a modifier (luck boost, pity) is active and when a once-only outcome is won; only a long list may move into a pop-up behind a visible worded "Info" or "Details" label (lead fix 2026-10-22: the earlier "static, behind Details" wording contradicted platform-policy `references/rules.md`). Load `platform-policy` for the current rules; it wins over this line.
- check: Capture the windup for the lowest and the highest tier and compare them frame by frame: identical up to the result frame; no higher-tier layer appears on any lower result; each tier is nameable in a grayscale capture; odds sum to 100 % and are visible before the buy button; the restricted-player path exists.
- mistake: A rarity tint during the windup; a "so close" near-miss animation; a fanfare on a common result from a paid egg; luck-boost sparkles that imply more than the shown odds.
- examples:
  - DS: an egg reveal ladder from Common to Secret with an identical three-beat windup for every tier (DS:vfx-design/references/moment-recipes.md:146-169).
- roblox_fit: PolicyService exposes ArePaidRandomItemsRestricted per player (knowledge/external/roblox-creator-docs/_api-reference/classes/PolicyService.yaml:91; production/monetization/index.md:156-161); the paid-random-items policy page itself is not in the local mirror, so the exact disclosure wording is [unverified]: load `platform-policy`.
- roles: game-designer, progression-designer, live-ops-designer, vfx-designer, ui-ux-designer, sound-designer, feature-builder, reviewer, qa-lead
- also: vfx-reads-timing, ui-ux, style-identity
- sources: DS:vfx-design/SKILL.md:54; DS:vfx-design/references/moment-recipes.md:34-36, 146-169, 196-207; DS:vfx-design/references/effect-card-and-presets.md:184; DS:vfx-design/evals/briefs.md:48-60
