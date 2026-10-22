> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Part of `game-design`. Sources: N3 §3 (ten observable tests, worked examples, disagreements), DS §4-§7 (mechanics carry theme, progress and arcs, fairness, luck vs skill), FI. Tags as in SKILL.md. Revised by J018 maker game-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (§3-§5 sharpened with checks; new §7 feedback, §8 threats, §9 read order and loudness, §10 one code).

# Principles as tests, not slogans

## 1. The ten tests (N3 §3.2 O; review tests, not a doctrine every admired studio shares)
| # | Principle | How to check | Fail when |
| --- | --- | --- | --- |
| 1 | Clarity | can the player infer the actions, the relevant state and the immediate consequences? | key differences are carried only by decoration or by text unreadable while acting |
| 2 | Meaningful choice | show two concrete states where different actions are better | one option wins everywhere (unless it deliberately serves expression or accessibility) |
| 3 | Fairness | rebuild a loss from information available before it: learnable rule, counterplay or knowingly accepted risk | the explanation works only in hindsight; hit geometry is ambiguous; unavoidable punishment is called a skill test |
| 4 | Learnability and mastery | novices find a workable action; experts improve planning, execution, efficiency, creativity or teamwork | progression only removes early friction and adds no richer decisions |
| 5 | Feedback and feel | tell apart input received, action committed, hit or miss, state change, goal consequence; sound, motion and effects inform as well as celebrate | a particle burst covers unclear cause and effect |
| 6 | Pacing | map recovery, anticipation, escalation, payoff, reflection | constant maximum intensity, or a wait with no tension, planning, social activity or rest |
| 7 | Difficulty | name the skill tested; separate perceptual, cognitive, motor, strategic, social, economic demand | the skill was never taught; gear poverty is mislabelled as lack of skill |
| 8 | Surprise and discovery | a surprise revises the player's model, not teaches that rules cannot be trusted; leave room for inference | the world breaks its own rules |
| 9 | Expression | meaningful differences in solution, build, identity, arrangement or social role | expression is advertised but non-standard approaches are blocked; cosmetic choices are sold as power |
| 10 | Time respect | show the commitment, save progress, make stopping readable, no repeated solved chores to delay access | the game punishes stopping; quiet play is not wasted time by nature |

## 2. Worked examples (E unless marked)
| Case | What it shows | Limit |
| --- | --- | --- |
| Kirby and the Forgotten Land (D06) | hit detection accounts for camera perspective; a near-ground jump still counts ("Fuzzy Landing"): what looks successful should feel successful in 3D | supports perceptual fairness; not a reason to change every competitive collision rule in secret |
| Kid Icarus: Uprising (D07) | the player picks the challenge: intensity 0.0-9.0, 2.0 standard; the stake is in-game hearts, not money; a failed run loses the whole wager and lowers intensity a little (V, corrected in FI IC59) | never a justification for paid gambling |
| Tears of the Kingdom (D08, D09) | consistent signs: immovable crates get ropes or cloth, unbreakable jars get lids; elaborate and minimal builds both progress | affordance decisions, not a tested whole |

## 3. Mechanics carry the theme (DS §4)
- Mechanics alone set tone: a cube that deals area damage and vanishes reads as a bomb; movement implies character (hop = frog, lurch = zombie). A larger area or a slower, heavier timing raises the feeling of danger and power: tuning numbers are tone tools, not only balance. Big creatures move slowly with long settles; a giant at human speed reads small.
- Art and rules must say the same thing: a bush that stops bullets, a mailbox that stops a truck, an open doorway you cannot enter each break belief. What looks heavy acts heavy; what looks weak breaks first; cause and effect stay predictable. A character's look and its role agree (a fragile ranged unit looks slim, a tank looks bulky).
- Art turns rules and numbers into a fantasy players build around: items and units belong to named theme families (a shared motif and palette) that players collect or build by, even over the strongest option.
- Every craft brief passes the mechanic and its numbers (health, range, speed, area, duration) so the look expresses them: a pull ability shows the pull; a high-health unit looks heavy.
- Checks: plain-block test (`loops.md` §5b); a fresh reader shown the asset without text says what it does and how tough it is, and both match the spec; a play-test list of every look-vs-behaviour mismatch (collision on an open doorway, leaves that stop bullets, a ledge that looks climbable but is a wall), each fixed or justified; every item in a set names its theme family (shared motif and palette).

## 4. Progress and arcs (DS §5)
- The player always sees progress toward the goal (bars, counters, a landmark getting closer, a gate opening); in multiplayer both sides see it, and progress markers tell the other side when to push. The midpoint is shown as an event (PROPOSAL default: a checkpoint or progress update at least at the halfway mark).
- Build a climactic arc: tension rises toward the resolution (the boss changes phase at low health and brings the heat; the last target is the biggest; the last point gets louder sound, stronger effects and a music change). A flat curve ends with no peak. In a level the arc is laid out in space: readable targets near spawn, bigger and harder ones further in, the climax piece near the end.
- Checks: stop the play-test capture at random moments; the tester says how far they are from the goal. Plot intensity over the round or session (threat rate, music layer, effect density, reward size): it rises toward the end and is not flat.

## 5. Fairness and luck (DS §6-§7)
| Fair frustration | Unfair frustration |
| --- | --- |
| clear expectations, consistent rules | rules change without warning |
| the player can see why they failed and learn | a hidden or random punishment |
| the game gives tools to overcome it | no answer the player can find |
| difficulty rises with skill | a spike with no new tool |
| every threat telegraphs and behaves the same each time | a hidden trap right after an obstacle |

Some frustration is the point: removing all challenge removes the satisfaction of winning. For each obstacle the spec names its counter (tool, skill, route); after each play-test failure ask the tester what beat them and what they would do differently. Fair: they name their own mistake. Unfair: they name the game.

| Luck vs skill mix | Effect | Fits |
| --- | --- | --- |
| mostly luck | anyone can win; wins feel unearned | casual, social, very young audiences |
| mostly skill | mastery feels earned; newcomers lose | competitive play |
| random start, skill in play | lucky starts excite; good players come back | broad audiences |

Decide where randomness sits (start, loot, drops, matchmaking) and where skill decides, per mode, for the target audience; randomness placed by accident is a finding. Check by simulation or play-test: a skilled player can recover from a bad random start, and a new player sometimes wins (ask the progression designer for a `tools/progression/sim.py` run with two skill profiles over many seeds when a model exists). Paid randomness: `platform-policy` and `systems-economy.md` §9.

Pacing frequency and difficulty amplitude are separate dials: Left 4 Dead's director adjusts pacing, not difficulty; its 3-5 s peak and 30-45 s relax are that game's parameters, not a Roblox encounter clock (D11 V, N4 4.03; FI).

## 6. Where experts disagree (N3 §3.3)
- Mastery vs wider experience: Koster ties fun to progress in prediction; Sylvester centres decisions but grants socialising, imagination and creation. Neither means every second must be a hard choice.
- Quests vs exploration: Klei reports removing explicit quests from Don't Starve because a task list displaced discovery (D19; source page blocked at fact-check, unverified: treat as OPINION); Supergiant uses permanent progression and narrative in Hades to widen access (D20 E). Test which structure serves this game's motivation; neither is universally right.

## 7. Feedback follows the real outcome
Every player action gets clear, immediate feedback; its size teaches what matters. I specify the feedback stack in the feature spec (`preproduction/references/documents.md` §6); the crafts make it.
- **Two layers.** The attempt cue plays on the input (small, quick, never covering the impact point or the next contact). The outcome layer (punch, hit-stop, celebration, reward sound, shake) plays only on the confirmed result: the hit landed, the block broke, the server accepted the sale. On Roblox the attempt cue runs on the client at once; the outcome layer runs when the server's confirmation reaches the client; a request the server rejects never shows it. PROPOSAL default: a visible pending state when confirmation takes longer than about 100 ms.
- **Hit-stop is local and scaled.** A melee hit may freeze the attacker's and target's animation and the hit's own particles for a moment; physics, other players and server results keep running; the length rises with hit strength (PROPOSAL start values: light about 50 ms, heavy about 100 ms, finishing about 150 ms; none on explosions, projectile throwers, rapid fire or crowds).
- **Size follows a learnable cause.** Material, force, weak point, chain size, rarity: never a random roll and never louder than the outcome. A flat-feeling action is fixed by checking outcome link, truth, readability and timing before raising size, brightness, count or length.
- **Failure and refusal answer too.** A miss, a block and a refusal each have a distinct cue; a refused action says at the control what is wrong and how to fix it ("need 40 more gold"), in text with an icon, never colour alone and never silence; disabled controls show their reason.
- **Celebrations are short and tiered.** A reached goal gets a short celebration that ends before the player's next decision (PROPOSAL default: under about 2 s in play; bigger ceremonies only on non-play screens). Escalation (combo, streak, chain) steps only at real thresholds, adds one layer, is named by a short text label that reads with particles off, and resets visibly after idle.
- **Frequent events stay quiet.** The more often something happens, the shorter and subtler its feedback; same-kind events in a short window merge into one burst, one sound and one count (PROPOSAL default: about 100 ms window); judge a frequent effect over a hundred repeats, not one.
- **Counters tell the truth.** Logic uses the true value at once; a count-up is decoration on top and ends on the exact number.
- **Every state change has a cue.** Ability ready, taking damage, spotted, resource needed: each has a cue in at least two channels (picture plus sound, or plus text) or a written reason for none.
- Checks (on studio-operator captures; timing from a fixed-camera frame folder named `f###_<ms>ms.jpg` with 0 ms on the press, read with `python tools/vfx/clip_metrics.py <folder>`: `onset_ms` = press to first visible change, `visible_ms` = first to last changed frame; the tool's background is the median frame and every other change counts, so the clip has still frames before and after the event for more than half its length and nothing else moves (idle animation off, HUD counters outside the frame), otherwise the layer fades into the background or `visible_ms` stretches toward the whole clip; onset counts from a tenth of the clip's peak, so time the attempt cue on a clip without a big outcome, e.g. the rejected request): press to first visible change on the press frame or the next at 30 fps (PROPOSAL default); send a request the server rejects: no outcome layer, celebration or reward sound; compare miss, hit, blocked, break and big break with sound off: all distinct; trigger each threshold: the celebration's `visible_ms` ends before the next decision; trigger a frequent event at its real rate: one label and one sound per merge window, the final counter exact.

## 8. Threats read before they hit
- **Reaction window.** I set the telegraph lead of every enemy and hazard attack as a tuning key; the animator, VFX and sound designers fill it. PROPOSAL starting values, a play-test may change them: about 0.6 s for an attack with one known dodge direction, about 1.0 s with several safe spots, never below human reaction time (about 0.23 s) plus decision, touch and network time; bigger attacks get longer wind-ups; network latency shortens the real window, so err longer for dodgeable attacks. The player's own actions get a short, tight anticipation so they feel responsive.
- **Two channels, same every time.** The tell uses at least two channels (pose plus effect, or effect plus sound), is identical every time the attack happens, and ends (and is removed) on the damage frame. A threat that builds toward a break (a shield, a timer) gets a cue whose intensity rises before the break.
- **The drawn area is the real area.** A ring, edge or stop line that shows where something hurts sits on the gameplay area from warning to last tick, in every skin and quality level; its size and timing come from the gameplay data, never set by eye; nothing danger-coloured remains after the last tick; no random fuse.
- **Readable on the phone, from the real camera.** Tells read at the game camera on a phone; size gaps between threat tiers are larger than on PC; a giant's slow, heavy timing sells its weight.
- Checks: frame-step the capture: the wind-up pose has a clear silhouette and lasts at least the window; effect and sound tells start on the same frame; compare two captures of the same attack: identical tell; ask for a debug overlay of the server's hit shape at warning, contact and end: the drawn edge sits on it; after each play-test death the tester says what killed them.

## 9. What is read first, and how loud
- **Rank per scene.** Each scene, level and screen brief carries a ranked read list. Default prominence order on one screen: a threat to the local player, then the player's own action feedback, then pickups and objectives, then other players' effects, then ambient. Environment is the backdrop; UI and gameplay effects own the extremes.
- **Tier the loudness.** Effects, sounds and celebrations get importance tiers (for example basic action, ability, ultimate, rare reward) with caps on screen area, brightness, duration and loudness per tier; only the rare top tier may fill the screen. If everything is loud, nothing is.
- **Per viewer.** The same effect matters differently to the player who caused it, a bystander and the player it threatens. Threats and pickups stay full for whoever must act on them; other players' non-threat effects are toned down on my screen and never shake, flash or tint it; team colour follows my relation to the source (enemy vs ally), always paired with a shape or outline. PROPOSAL default: at most about 4 effects need attention per viewer at once (own action, nearest threat, one pickup, one ambient).
- **Camera and screen punches are rare.** Shake, field-of-view punches, slow motion and full-screen flashes only for rare, top-tier moments of the local player, never for frequent events or another player's effect.
- **Comfort settings keep the information.** Every intense channel (shake, flash, full-screen tint, fast motion) has an off path; reduced versions keep every warning; nothing pulses above 3 times per second at full contrast; slow pulses mean safe, fast mean urgent; countdowns follow the server timer.
- **Worst-case crowd.** Judge with every player's effect on at once: effects never cover other players, targets, the HUD or the shop; frequent and personal effects stay about one character wide (PROPOSAL default) and low.
- Checks: in the blurred or thumbnail view of the busiest capture, the first-noticed element is rank 1; for effects and threats with per-viewer variants, a two-client capture (the owner starts the local two-client server, so batch these in one request; without it the per-viewer check is Unproven): the bystander's camera never moves or tints from another player's effect, and the threatened player's threat is the brightest thing near them; capture with grayscale, sound off and reduced motion on: every threat, pickup and outcome is still found.

## 10. One code for the whole game
- One gravity, jump arc and impact-weight language per game (game profile), so players can predict how things move and hit; every clip, effect and code-driven motion keeps it.
- Gameplay colours are reserved (enemy, danger, team, interactable, route) and kept out of decoration; one hue never means both help and harm (poison is not green when green heals); every colour role pairs with a shape or icon. One shape code for effect meanings (heal, shield, damage) across the game.
- Similar things behave the same way: the same attack has the same tell; the same floor material sounds the same; every hazard has written rules (`spaces.md` §5); one orientation convention across maps.
- Checks: the spec's colour and shape roles list no signal with two meanings; compare jump and fall timing across characters and props against the declared values; hazard sheet complete before blockout.
