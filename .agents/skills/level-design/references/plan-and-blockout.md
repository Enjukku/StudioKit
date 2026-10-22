> Author: J018 maker level-design · claude-opus-5-5 · high · 2026-10-22. Part of `level-design` (§3 steps 1-5); built also from the owner's Riot transcripts (J018); repair round 1 2026-10-22 (story reason, option diagrams, brief fields, approach directions, peak gaps); repair round 2 2026-10-22 (first view by own contrast); repair round 3 2026-10-22 (first-view pass rule matches §6.3). The designer's rules these sheets apply live in `game-design/references/spaces.md`; this file is how I plan, sketch and block out a level so those rules can be measured.

# Plan and blockout: job card, layout options, blockout, grey read pass, teaching, pacing

## 1. The level job card (`knowledge/jobs/<job>/route-graph.md`, top section)
Write it before the first sketch or the first verdict. Every field has a source (owner D-id, game profile, brief, measurement) or is `PROPOSAL`; a field that would change a verdict and has no source is an assumption, stated.
| Field | What to write | Example (a harbour hub in a fishing simulator) |
| --- | --- | --- |
| Target experience | one type of fun (two at most), from the game profile | collection and comfort |
| Four parts | goal, opposition, decisions, rules, one line each; an empty "decisions" line is a finding | goal: sell the catch, buy a better rod, reach the next sea · opposition: travel time, bag space · decisions: sell now or fish more, which rod · rules: bag holds 20 fish |
| Progress | how the player sees how close the goal is | the next sea's gate glows brighter with each rod tier |
| Conflict and story reason | one sentence per mode, or "none" for a social space, and the objective's reason in the world's story (`spaces.md` §2) | none (social hub); the gate opens because the harbour master lets proven fishers sail to the next sea |
| Teaches | the mechanic or rule this level makes the player learn, or "none" | the sell-then-upgrade loop |
| Session shape | first visit, return visit, short phone session (minutes) | first visit 3 min; return visit 40 s per sell loop; phone session 5-8 min |
| Camera, device, group | camera mode and distance, target phones, players per server, group play | third-person default, phones first, 20 players |
| Movement metrics | walk speed and jump measured in Studio (`review-artifact.md` §6.6), sprint or mounts | 16 studs/s; jump: starting value 6.4 studs until the Studio measurement lands; no sprint |
| Personality and expectations | the place as a character in 3-5 words; the 3-5 things players expect from this theme | "busy, salty, friendly, sunlit" · a pier, boats, a fish market, gulls, a lighthouse |
| Smallest gameplay object | the smallest thing players must find on a floor, and its floor types | a dropped bait pack (1 stud) on planks and sand |
| Stop criteria, budget | the conditions that end the work; passes and option rounds allowed | every §4 check Pass at both graphics settings; 1 option round; 2 grey passes |

## 2. The layout options pass (thumbnail pass for levels)
- **Three options, distinct hooks.** Each option is a top-down route sketch (nodes, edges, spawn, objective, landmark, the first-view direction) with a one-line hook from a different source or reading of the place: a ring around a plaza, one main street, a terraced hill, a harbour you cross by boats. A resize or a mirror of another option is not an option. One option is deliberately atypical (an idea from outside games: a real town plan, a theme park, a ship's deck).
- **Warm-up first.** The first sketch is the expected idea; label it "warm-up" and make the others.
- **Same finish.** All three as plain diagrams drawn with Python + Pillow on a blank canvas from each option's route JSON (x and z in studs to pixels at one fixed scale for all three; nodes as labelled dots, edges as lines), same scale, labelled A, B, C, each with its route table (`review-artifact.md` §6.2) (seconds per edge) and its first-view sentence.
- **Pick with reasons.** One recommendation with the reason tied to the job card ("B: the first view frames the gate; sell loop 32 s against 48 s in A"); one line per rejected option on why it lost; what is kept from a rejected one. Ties go to the owner with the recommendation.
- **Budget:** diagrams only, no reference images and no Studio captures in this pass; at most two rounds before G1. The G1 packet shows the pick beside the other two.

## 3. Blockout order and player metrics
**Order** (each step is captured top-down before the next starts):
1. Spawns (position and facing), then the objective, then the main route between them; side areas, shortcuts and secrets only after the main route works.
2. Grey Parts on a fixed snap grid (the game profile's increment), in shapes that could be real structures of the theme (a pier, a market hall, a sea wall), so art can build on them; ask the environment designer early when a shape is abstract.
3. A player dummy (the game's character size, in typical avatar colours) and one known-size object (a door, a bench, a crate) in every space.
4. Landmarks as their real height and outline in grey; boundaries as their real kind (cliff, wall, water) in grey.
5. Play it: the environment designer or the studio-operator walks every edge at walk speed with the real movement tools (jump, sprint, abilities, tools) and times it; every pit, ledge and high place is tried; findings (angles closed, dead space, stuck spots) are listed per play-test.

**Metrics** (from the job card; measured, never remembered):
| Metric | Use | Check |
| --- | --- | --- |
| Walk speed (studs/s) | seconds per edge in the route table | timed walks within about 20 % of the computed time, or the difference explained (a detour, a stall, a slope) |
| Jump (studs, measured) | ledges meant to be climbed stay under it by the margin; ledges meant to block stay over it by the margin (starting `PROPOSAL` margin 1 stud) | every main-route ledge in the route script (`review-artifact.md` §6.2) |
| Character envelope and camera | doors, halls, ceilings, cover heights | the default camera passes every tight opening without clipping (environment `review.md` FL7) |
| Walk limits | longest edge without something to see or do; return-trip length | starting values `spaces.md` §3; the brief or owner replaces them |

**The blockout brief** to the environment designer (`preproduction/references/handoffs.md` format) carries, per node: position, stop or pass, critical facts and read rank, the cue that must be noticed and why it reads, sight lines to keep clear of motion and reserved colours, key positions (where players stand to fight, wait or decide), floor types and the smallest gameplay object, the hazard sheet ids. It also carries the job card, the route table, the teaching sheet, the pacing map, the material-to-rule table, the orientation conventions and the intentional-height list (`spaces.md` §3, §4, §6). Nothing about the look: that is theirs.

## 4. The grey read pass (on the greybox, before any art)
The cheapest moment to fix a read. Views: the first frame after spawn at the default camera, the decision view at each fork per approach direction, each zone's entry view, the top-down, and one view per hazard; at the game camera, in grey (the `.luminance.png` that `look_check.py value` writes), with the key light already chosen by the environment designer.
| Look for | Pass when | Measure (screening aid; eye check on the still before any fix note) |
| --- | --- | --- |
| The first view | the goal or main landmark is in frame, its own contrast reaches the marker target, it is the lightest or the strongest in contrast among its competitors (`review-artifact.md` §6.3), it is the tallest, and the lines lead to it | rank and own contrast (`review-artifact.md` §6.3) |
| Forks | a landmark or the next cue shows from each fork, from each direction players approach it (both ways, return trips included) | one capture per fork per approach direction |
| Landmarks | each zone's landmark is its tallest shape; no two landmarks share a silhouette | part tops and the flat-key silhouette comparison, shadows off, with the black-fill sheet (`review-artifact.md` §6.4-§6.5) |
| Lines | paths, walls and roof lines lead to the goal or the next route; none leads into a dead end or off-screen | traced on the grey first view |
| Dead space | every area is used by a route, a fight, a pause or a view | marked on the top-down (`review-artifact.md` §6.7) |

One named problem per pass, the worst first; re-capture from the same camera after each fix. A weak read is fixed with contrast before detail: lower the surroundings (a darker wall, a lower crate stack) before raising the goal. A fix that moves a route, cover or a sight line is a route graph revision.

## 5. The teaching sheet (one per mechanic the level teaches)
| Beat | Arrangement | Failure cost | The player infers | The action that shows it | Capture |
| --- | --- | --- | --- | --- | --- |
| 1 Safe exposure | the mechanic alone, no threat, the outcome visible | none or a few seconds back | "this platform moves on a rhythm" | waits, then jumps on the beat | the beat's approach view |
| 2 Required | the same mechanic, now needed to progress, still alone | short (a checkpoint just before) | "I must time it" | times the jump | approach and after commit |
| 3 Twist | one relationship changed so rote play fails (direction, speed, a second platform) | as beat 2 | "the rhythm can change; watch first" | pauses to read the new pattern | approach |
| 4 Independent use | the mechanic combined with an earlier one, no hint | the level's normal cost | "I know this tool" | solves it without a pause | approach and after commit |
- The first exposure is readable at the game camera and cheap to fail: the way back from a failure is measured in seconds from the route table.
- A hazard or obstacle without a learning reason is cut or given one; each beat names the tool or ability that beats it.
- Not required for open worlds, horror or social areas (L-04).

## 6. The pacing map (one row per route segment, in route order)
| Segment (edge ids) | Seconds | Intensity 0-3 | Kind | What the player sees or does |
| --- | --- | --- | --- | --- |
| spawn → fork | 6 | 0 | rest | the gate tower ahead, the market to the left |
| fork → bridge | 9 | 2 | build | gulls dive at the path (dodge) |
| bridge | 4 | 3 | peak | the swinging bridge section |
| bridge → lookout | 7 | 0 | rest + view | the next sea's gate appears behind the lighthouse |
- Kinds: rest, build, peak, reveal, reward. After each peak a rest; the gaps between peaks (from the end of one peak to the start of the next; the climax counts as a peak) are not all equal (an even beat reads as a machine); the climax sits in the last third; a reveal waits behind a turn or a rise and is framed as the player comes round; rewards and new views sit at real achievements and natural pauses.
- Intensity is a planning estimate from the encounter list and hazards (enemy rate, hazard density, time pressure); the play-tests replace it.
- Pacing frequency (how often peaks come) and difficulty (how hard each one is) are separate dials; change one at a time.
