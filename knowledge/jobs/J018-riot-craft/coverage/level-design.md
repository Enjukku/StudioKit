---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 2 (brief v2)
supersedes: []
---
> Author: J018 maker level-design · claude-opus-5-5 · high · 2026-10-22

# J018 coverage: level-design (shared skill)

Books rebuilt (old state `df13ff4`, also the state at start): `.agents/skills/level-design/SKILL.md` (sections 1-6 rewritten inside their numbers, §7 "Core principles for this craft" appended), `references/review-artifact.md` (§1-§5 kept and sharpened; §6 measuring from Studio captures and §7 self-review checklist appended), new `references/plan-and-blockout.md` and `references/worked-examples.md`. No role file: `level-design` is a shared skill loaded by the game-designer and the environment-designer; both role files already tell them when to load it, so no role body change is needed here (deliverable 3: n/a; nothing proposed for their frontmatter).

Legend for "landed in": `S` = `level-design/SKILL.md` (L-nn = craft core row, §7 #n = core principle n); `PB` = `references/plan-and-blockout.md`; `RA` = `references/review-artifact.md` (§4 C1-C19 = the fixed review checks; §7 LD1-LD18 = the self-review checklist); `WE` = `references/worked-examples.md`. Where the self-review lives: `RA` §7 (run before every hand-back, named in `S` §6); the checks of a review in `RA` §4.

## a. Findings

All 96 findings tagged `level-design` in `matrix.md` have a row (78 landed fully or partly, 18 rejected with a reason); 17 untagged findings used follow. A text in the last column of a landed row is a scope note.

| ID | Title | Landed in (file § section) | As | Rejected: reason |
| --- | --- | --- | --- | --- |
| CD-26 | Design a prop or a place as a character | PB §1 "Personality and expectations"; S §7 #10; RA §4 C12 (mood against the personality words, repair round 1) | step / core principle / self-review check |  |
| CF-01 | Big to small: composition first, detail and effects last | S §3 steps 4-5, 7 (paper → grey → read pass → art); S §7 #4; RA §7 LD9, LD13 | step / stage / core principle / self-review check |  |
| CF-02 | Design and pose for the side the game camera shows | S L-01 (spawn position and facing); RA §1 field 1 (entry view at the game camera); RA §6.1 (captures at the default camera); RA §4 C2 | standard / self-review check | scope note: which faces of an object get finished is the environment designer's and modeler's (environment PR-22) |
| CF-07 | Judge composition on the integrated capture | S L-15; RA §4 C7; RA §7 LD16 | standard / self-review check |  |
| CF-08 | Shape flow points to the focal point, at every scale | S L-03; PB §4 row "Lines"; RA §7 LD13 | standard / stage / self-review check |  |
| CF-09 | Lines on an object lead somewhere and agree with each other | S L-03 (remove lines that lead into dead ends); PB §4 row "Lines"; RA §4 C2, §7 LD13 (main lines lead to the goal) | standard / stage / self-review check | scope note: lines inside objects are modeler and environment craft |
| CF-12 | A value gradient toward the hero | S L-03 (calm the surroundings; the brightest thing in view is the goal); PB §4 row "The first view"; RA §4 C2, §7 LD13 | standard / stage / self-review check | scope note: building the gradient is the environment designer's (environment PR-38) |
| CF-13 | A bright focal light can hide a surprise | S L-06 (the next big thing waits behind a turn or rise); PB §6 (reveals); RA §7 LD6 (surprise outside the bright focus; environment RD12 measures it) | standard / self-review check |  |
| CF-14 | Make the focal point the tallest shape | S L-02; RA §4 C4; RA §6.5 | standard / self-review check |  |
| CF-15 | Three depth groups: foreground frames, midground carries, background unifies | — | — | rejected: depth planes in a view are the environment designer's and film director's composition craft; my part (no foreground piece blocks the play camera) is covered by C3 and C7 |
| CF-17 | A giant figure behind small heroes sells scale and threat | — | — | rejected: shot staging for reveals and key art belongs to film and marketing; in play a huge part that blocks the camera is a C7 failure |
| CR-01 | Judge in the game, at the game camera, in the real place, moving | S §5 (no pass without a measurement or capture); S L-15; RA §2 (played walk vs analytic walkthrough); RA §4 C7 | rule / self-review check |  |
| CR-13 | Close with an honest recap of your own result | S §6 last line; RA §5 (honest recap); RA §7 LD18 | self-review check |  |
| CR-17 | Say what each input can prove; end with a could-not-check list | S §5 (input and label per check); RA §4 intro (Unproven when the input is missing); RA §6.8; RA §7 LD15, LD18 | rule / self-review check |  |
| GD-03 | A game needs a goal, opposition, decisions and rules | S §3 step 1; PB §1 "Four parts"; RA §4 C1 | step / self-review check |  |
| GD-06 | Movement patterns give enemies character | S L-10; RA §3 first bullet; RA §7 LD8 | standard / self-review check |  |
| GD-07 | Art and mechanics must promise the same thing | S L-09 (collision matches what players see); RA §4 C10, C18 | standard / self-review check |  |
| GD-10 | Make progress toward the goal visible | PB §1 "Progress"; RA §4 C9 | step / self-review check |  |
| GD-11 | Build a climactic arc toward the resolution | S L-06; PB §6 (climax in the last third); RA §4 C6, C8; RA §7 LD6; WE §2 | standard / stage / self-review check / example |  |
| GD-12 | Give opposition and the tools to beat it; the right frustration | S L-05; RA §3 (each encounter names its counter); RA §4 C6 | standard / self-review check |  |
| GD-13 | Fairness comes from clear expectations and consistency | RA §3 fourth bullet (same attack, same tell, two uses compared on the partner's captures); RA §7 LD8 (the same check in the self-review); RA §4 C14 (failure cost matches the intended challenge) | standard / self-review check | repair round 1: the check moved from C14 alone to LD8 |
| GD-15 | Prove the fun with the crudest prototype before art | S §3 steps 4-7 (greybox played before art); PB §3 step 5; RA §7 LD9 | step / stage / self-review check |  |
| GD-22 | Find the genre's demands first | S §3 step 1 (camera, device, group size, session shape); PB §1; RA §7 LD1 | step / self-review check |  |
| GD-23 | The map is the board: map mechanics stay in the background | S L-17; RA §4 C15 | standard / self-review check | scope note: the rule text lives in `spaces.md` §1 (V6) |
| GD-24 | A level is a puzzle with ability-shaped holes | S L-05; RA §1 field 3 (tool per action); PB §5 (each beat names its tool); RA §4 C6 | standard / step / self-review check |  |
| GD-25 | Build conflict into the objective; tie it to the world's story | PB §1 "Conflict and story reason" (pointer to `spaces.md` §2); RA §4 C1; RA §7 LD1 | step / self-review check |  |
| GD-26 | Plan the first seconds from the round-start positions | RA §4 C17 (spawn-to-contact per route); RA §1 route table | self-review check | scope note: rule text in `spaces.md` §3 (V6) |
| GD-27 | Neither side takes neutral space too easily | RA §4 C17 | self-review check | scope note: rule text in `spaces.md` §3 |
| GD-28 | Cover gives both sides options and a counter | RA §4 C17 | self-review check | scope note: rule text in `spaces.md` §4 |
| GD-29 | Turn a dead boundary into a risk and reward | S L-09 (last sentence); RA §4 C10 (reward spot used and counterable) | standard / self-review check |  |
| GD-30 | Every hazard has written rules | RA §3 last bullet (pointer to `spaces.md` §5 and the hazard sheet); RA §4 C10; RA §7 LD8 | standard / self-review check |  |
| GD-31 | Art stays inside the blockout's gameplay | S §1 (owners); S §3 step 7; RA §4 C3 (after art, routes equal the approved blockout) | step / self-review check |  |
| GD-32 | Hide small secrets that reward discovery | RA §4 C3 (secrets off routes and decision points); WE §2 (a dead end gains a secret) | self-review check / example |  |
| GD-33 | A map is never done; new worlds are an escape | RA §5 (open findings of a live map go to the revisit backlog); S §7 #11; RA §7 LD18 | standard / core principle / self-review check |  |
| LC-01 | Reserve the gameplay colours; keep them, and fast motion, out of decoration | S L-03 (off the sight lines I list); RA §1 node geometry (sight lines); RA §4 C19; RA §7 LD7 | standard / self-review check | scope note: the reserved-hue share is measured by the environment designer (environment VB4, M3) |
| LC-11 | Block light and shadow first; test lighting options on the rough | PB §4 (the grey read pass is taken with the key light already chosen on the greybox); RA §7 LD13 | stage / self-review check | scope note: the light choice is the environment designer's (LA-15) |
| LC-12 | Light leads the eye: the brightest area is the focus | S L-03; PB §4 "The first view"; RA §6.3; RA §4 C2, §7 LD13 | standard / self-review check |  |
| LC-13 | Light motivated by the setting | — | — | rejected: lighting craft of the environment designer (`light-and-air.md`, VB8); no level-design decision |
| LC-14 | Light direction sets good or evil | — | — | rejected: lighting and shot craft of the environment designer and film director |
| LC-16 | Fix the light per level and tune shadows for readability | RA §1 node geometry (key positions), handed over in the blockout brief (PB §3; RA §7 LD7) | step | scope note: the measure (a dummy at each key position at both settings) is environment VB9 |
| LC-18 | Keep the player band neutral; tame bright hazards | S L-03; RA §1 (sight lines, key positions); RA §4 C19 (environment VB5, VB13) | standard / self-review check | scope note: the band and hazard measures are environment VB5, VB13 |
| MD-01 | Indicate detail; do not spell it out | — | — | rejected: surface and detail craft of the environment designer and modeler |
| MD-02 | Budget detail by display size, camera distance and player speed | RA §1 node geometry "stop or pass" (detail and story go to stop points); S L-12; RA §7 LD7 | standard / self-review check |  |
| MD-13 | Ground every object: base, blended seams, colour bleed | — | — | rejected: environment craft (environment E-19, FL6) |
| PP-01 | Set triangle and texture budgets before building; phones first | — | — | rejected: budgets are the performance engineer's and environment designer's (environment `review.md` §5); my part, no space larger than its play, is L-13 |
| PP-24 | Kits for repeated layouts, unique shells for bespoke ones; no visible duplicates | — | — | rejected: kit and shell choice is the environment designer's (E-12) |
| PP-26 | Environment order: blockout, composition, kit, dressing, mechanics, then light and polish | S §3 steps 4-7; PB §3; RA §7 LD9 | step / stage / self-review check |  |
| PP-27 | Block out on a grid; snap the art to the approved blockout | PB §3 step 2; S §3 step 4; RA §7 LD9 | step / self-review check |  |
| PI-04 | Block out first, in the engine, and play it before detail | S §3 step 4; PB §3 step 5; RA §7 LD11 | step / self-review check |  |
| SS-05 | Shape language carries meaning: sharp is danger, round is friendly | S §7 #5 (hazards read sharp, safe ground open); RA §4 C19 (hazards read by shape) | core principle / self-review check | scope note: shape execution is environment and modeler craft |
| SS-06 | One shape vocabulary for the whole game, down to the small shapes | — | — | rejected: the art director sets it and the environment and modeler build it (art bible; environment P11) |
| SS-07 | Big, medium, small: never two shapes the same size | — | — | rejected: environment craft (environment FL4) |
| SS-19 | Design the group silhouette | RA §3 third bullet (a ring of small threats reads as danger by shape and count); RA §7 LD8 | standard / self-review check |  |
| SS-20 | Backdrop pieces: simple surfaces, elegant gesture | — | — | rejected: environment and modeler craft |
| SD-03 | Ambience, foley and one signature element put the player in the world | — | — | rejected: the ambience map belongs to the environment designer and the sound designer; my part is SD-09 |
| SD-09 | Set how far each sound carries by its importance | RA §1 node geometry ("events that must be heard from here, with their source"); RA §7 LD7 | standard / self-review check |  |
| SD-13 | Reverb and delay place the sound and glue its layers | — | — | rejected: sound and ambience craft (environment `ambience.md`) |
| SD-23 | Every floor material is a footstep callout | S L-18 (one material per gameplay rule); RA §4 C18 | standard / self-review check | scope note: the footstep table check is environment FL9 |
| SI-04 | Theme cues so a place is not generic | S L-12; RA §4 C12 | standard / self-review check |  |
| UI-09 | Proximity creates meaning | S L-17 (in-world information next to what it describes); RA §4 C18 | standard / self-review check |  |
| VC-01 | Fix a weak read with contrast, not detail | S §5 rule; PB §4 (fix rule); WE §1 (the fountain calmed); RA §7 LD17 | rule / example / self-review check |  |
| VC-04 | Make one spot the focus by lowering contrast everywhere else | S L-03; S §5 rule; WE §1; RA §7 LD17 | standard / example / self-review check |  |
| VC-05 | Give each screen layer its own value and saturation band | — | — | rejected: value bands are the art director's and the environment designer's (environment VB1) |
| VR-06 | Budget each effect's footprint for the worst-case crowd | S L-10; RA §3 (worst-case crowd); RA §7 LD8 | standard / self-review check |  |
| VR-07 | Never cover what the player needs to see; stay low | RA §3 (the worst-case crowd keeps threat, route and objective readable); RA §4 C7 | standard / self-review check | scope note: effect placement is the VFX designer's |
| VR-20 | The drawn danger area is the real hit area, from warning to last tick | S L-10; RA §3 fourth bullet; RA §7 LD8 | standard / self-review check |  |
| VH-01 | Rank what must be seen; UI and VFX first, characters second, environment last | RA §1 field 1 (read rank); S §7 #3; RA §7 LD7 | standard / core principle / self-review check |  |
| VH-05 | Clump detail in a few places; leave areas of rest | S L-06 (rest areas); RA §1 "stop or pass"; RA §7 LD7 | standard / self-review check | scope note: detail clusters are environment FL2 |
| VH-09 | Plan the read order: primary, secondary, tertiary | RA §1 field 1 (read rank 1-3); PB §3 blockout brief; RA §7 LD7 | standard / step / self-review check |  |
| VH-10 | Size signals importance | S L-02 (the landmark is the tallest shape); RA §4 C4 | standard / self-review check | scope note: threat size per enemy is the game designer's role card |
| WL-01 | Gameplay readability beats beauty; test it in the busiest moment | S §1 (rule above all); S L-15; RA §4 C7; S §7 #1 | rule / standard / self-review check / core principle |  |
| WL-02 | Items must be identifiable on the ground, even partly hidden | S L-16; RA §4 C16 | standard / self-review check |  |
| WL-03 | Every piece says "what I am" and "what you can do here" | S L-18; RA §4 C18 | standard / self-review check |  |
| WL-04 | One gameplay constraint, many fictional answers | S L-09; S §3 step 7; RA §4 C10 ("why is this here?" line) | standard / step / self-review check |  |
| WL-05 | Hazards explain themselves | RA §3 last bullet (visible source and containment); RA §4 C10; RA §7 LD8 | standard / self-review check |  |
| WL-06 | Rank the environment work: it is 90 % of the screen | — | — | rejected: the ranked work list is agreed between the game designer and the environment designer (`spaces.md` §6; environment `read-plan.md` §2); level design feeds it the read rank per node |
| WL-07 | The first view tells where you are and what to do | S L-01; RA §4 C2; WE §1 | standard / self-review check / example |  |
| WL-08 | Spawns first, then the route to the objective | S §3 step 4; PB §3 step 1; RA §7 LD9 | step / self-review check |  |
| WL-09 | Paths face forward; no doubling back in multiplayer maps | RA §4 C3 | self-review check |  |
| WL-10 | Keep the layout simple: two ways in per side | RA §4 C3 | self-review check |  |
| WL-11 | One orientation convention across all maps | RA §4 C2; S §7 #7 | self-review check / core principle |  |
| WL-12 | Mark objectives on the approach and in the floor | S L-02; RA §4 C4 | standard / self-review check | scope note: the floor border is environment RD5 |
| WL-13 | Head-height cues and directional patterns guide the eye | — | — | rejected: eye-height trim is environment PR-38, placed at the game designer's request; no separate level-design rule |
| WL-14 | Flat play spaces; every height change is intentional | RA §4 C10 (every map; intentional-height list); PB §3 blockout brief (the list goes to the environment designer) | self-review check | repair round 1: moved from C17 (team maps only) to C10 |
| WL-15 | Predictable geometry: players lose to opponents, not to the map | RA §4 C10 (collision as simple as the visible shape, every map); RA §4 C17 (cover counters, team maps) | self-review check | repair round 1: collision moved to C10 |
| WL-16 | Name dead space and oversized areas in self-review | S L-13; RA §4 C3; RA §7 LD14; PB §4; WE §2 | standard / self-review check / example |  |
| WL-17 | In a themed game, the blockout already reads as a place | PB §3 step 2; S §3 step 4; RA §7 LD9 | step / self-review check |  |
| WL-18 | Materials follow gameplay rules | S L-18; RA §4 C18 | standard / self-review check |  |
| WL-19 | Floors stay clean enough for the smallest gameplay object | S L-16; PB §1 "Smallest gameplay object"; RA §4 C16 | standard / step / self-review check |  |
| WL-21 | Scale: a player-sized reference in every blockout and scene | S L-11; PB §3 step 3; RA §4 C11; RA §7 LD10 | standard / step / self-review check |  |
| WL-22 | Environmental storytelling: someone lives here, time has passed | S L-12; RA §4 C12 | standard / self-review check |  |
| WL-23 | Give each zone or team an identity symbol | S L-02 (pointer to `spaces.md` §7); RA §4 C4 (symbol shows from the zone's entry at the game camera on a phone viewport, 1 entry capture per zone); RA §6.1 (entry view per zone); RA §7 LD13 | standard / self-review check | repair round 1: the old row pointed at the silhouette comparison, which is CF-14 |
| WL-25 | Distance lowers contrast and detail (atmospheric perspective) | — | — | rejected: environment craft (environment VB7) |
| WL-26 | A small, low-contrast busy background adds life | — | — | rejected: environment and marketing craft |
| WL-29 | Plan routes in player metrics: seconds at walk speed, ledges against jump height | S L-07; PB §1, §3 metrics; RA §1 route table; RA §6.2, §6.6; RA §4 C8, C10; RA §7 LD4, LD11, LD12; WE §1-§2 | standard / step / quality bar / self-review check / example | scope note: the 7.2-stud jump is replaced by a measured jump (the default character uses JumpPower) |
| WL-30 | Score a level review on ten fixed checks | RA §4 (fixed list, now 19 checks, every check re-rated every round, an input per check); RA §5 (one column per round); S §5; RA §7 LD15 | quality bar / self-review check | partly rejected: the 0-2 score and the total out of 20 are not adopted (the kit rates Pass / Fail / Unproven with no totals: `game-design` §5-§6; game-designer proposal row) |

Untagged findings used:
| ID | Title | Landed in (file § section) | As | Note |
| --- | --- | --- | --- | --- |
| WL-20 | It must read at the lowest graphics setting | RA §4 C19; S L-15 | self-review check |  |
| VH-04 | Judge noise in motion, with lighting and effects on | S L-15; RA §4 C7 (busiest-moment capture) | standard / self-review check |  |
| VC-06 | Test every character against every background | RA §4 C16 (marker target via environment FL1) | self-review check |  |
| RH-01 | Vary the cadence: fast and slow beats, never metronomic | S L-06 (gaps between peaks not all equal); PB §6; RA §4 C8; RA §7 LD6 | standard / self-review check | rhythm in animation also shapes the rhythm of a route |
| PI-07 | One named problem per pass; fix the worst first | S §3 step 5; PB §4; RA §7 LD17 | step / self-review check |  |
| PI-12 | Know when it is done: written stop criteria, repeating notes | S §3 step 1 (stop criteria and pass budget); PB §1; S §7 #18; RA §7 LD1, LD18 | step / core principle |  |
| PI-03 | Closing doors: from broad to narrow, never reopen | S §3 step 7 (do not reopen a closed layout without new evidence); S §7 #15 check (LD11, LD15) | rule |  |
| RI-18 | Each option gets its own hook from a different source | S §3 step 2; PB §2; RA §7 LD2 | stage | the finding names level layouts in its Roblox fit |
| RI-19 | Present options with your pick and the reasons; then iterate | S §3 step 2; PB §2; RA §7 LD2 | stage / self-review check |  |
| RI-21 | The first output is a warm-up; reject the typical idea | PB §2 ("Warm-up first"); RA §7 LD2 | stage |  |
| RI-23 | Bring in one unexpected element from outside the genre | PB §2 (one atypical option from outside games); RA §7 LD2 | stage |  |
| CR-03 | Solve the problem behind the note; separate goals from tactics | RA §7 LD17; WE §1 (the arrow note) | self-review check / example |  |
| UI-13 | Motion goal: intention, one attention motion at a time | RA §4 C15 | self-review check |  |
| VR-16 | Ambient environment effects: tiny, slow, partly hidden | RA §4 C19 (nothing fast or bright on a listed sight line) | self-review check |  |
| GD-04 | Name the target experience, not "fun" | S §3 step 1; PB §1; RA §7 LD1, RA §4 C1 | step |  |
| GD-34 | Feedback follows the real outcome | S §7 #19 (rewards and views at real achievements); RA §7 LD6 | core principle |  |
| CC-03 | Build for the next craft: ask what they need first | PB §3 (the blockout brief); RA §7 LD7; S §7 #17 | step / self-review check / core principle |  |

## b. Universal principles

| UP-ID | Applies (yes/no + reason) | Where in "Core principles for this craft" |
| --- | --- | --- |
| UP-01 | yes: the level is the board; routes, objectives, hazards and threats read first | S §7 #1 (and S §1 "rule above all") |
| UP-02 | yes: walked at walk speed, on a phone, busy, at the lowest setting | S §7 #2 |
| UP-03 | yes: read rank per node; calm the surroundings first | S §7 #3 |
| UP-04 | yes: paper, then grey, then art | S §7 #4 |
| UP-05 | yes: tallest unique landmark, shape of hazards, simple collision | S §7 #5 |
| UP-06 | yes: few ways in, rest areas, no dead space | S §7 #6 |
| UP-07 | yes: orientation conventions, one treatment per interactive type, materials by rule | S §7 #7 |
| UP-08 | yes: the opening seconds and the rest-peak rhythm laid out in space | S §7 #8 |
| UP-09 | in part: not in the master's applies list for level-design; the pushing is environment and model craft, my side is listing exaggerations and keeping traversal sizes exact (no contradiction with the master) | S §7 #9 |
| UP-10 | yes: personality and story facts shape the layout | S §7 #10 |
| UP-11 | yes: conventions kept across maps; each new world clearly new | S §7 #11 |
| UP-12 | yes: routes that differ in a named thing; uneven rhythm | S §7 #12 |
| UP-13 | yes: the level job card first | S §7 #13 |
| UP-14 | yes: the layout options pass | S §7 #14 |
| UP-15 | yes: grey before art; gates; re-block a failing section | S §7 #15 |
| UP-16 | yes: one named problem with its cause before any fix | S §7 #16 |
| UP-17 | yes: the blockout brief and route JSON for the environment designer and the progression designer | S §7 #17 |
| UP-18 | yes: stop criteria in the job card | S §7 #18 |
| UP-19 | in part: not in the master's applies list for level-design; my side is placing rewards, views and checkpoints at real achievements | S §7 #19 |
| UP-20 | yes: route and hazards readable with colour removed, no sound-only direction, lowest setting | S §7 #20 |

## c. Old book changes (line numbers at `df13ff4`)

| Old text (file:line at df13ff4) | Kept / sharpened / replaced by (new location) / moved / removed | Why |
| --- | --- | --- |
| SKILL.md:3 description | sharpened (S frontmatter: adds job card, layout options, player metrics, review from Studio captures; 394 characters) | new stages named so the skill loads for them |
| SKILL.md:6 header | kept, J018 line added (S header) | brief rule |
| SKILL.md:11 §1 "When this skill starts" | sharpened (S §1: the rule above all, who owns what, re-read after a compaction) | V7; owners match `spaces.md` and the environment books |
| SKILL.md:16-19 §2 table | sharpened (S §2: three references of this skill, `spaces.md`, `measure-captures.md`) | V6: rules and measures that live elsewhere are pointed to |
| SKILL.md:22 step 1 level job card | sharpened (S §3 step 1; PB §1 sheet with an example) | four parts, conflict, metrics, smallest object and stop criteria were missing; job-stage workflow still cites "§3 step 1" |
| SKILL.md:23 step 2 "Blockout first" | moved and sharpened (S §3 step 4; PB §3: order, grid, theme shapes, dummy, played with real tools) | the order and the measures were missing |
| SKILL.md:24 step 3 route graph | kept as step 3, sharpened (node geometry, route table, teaching and pacing sheets) | measurable inputs for the review |
| SKILL.md:25 step 4 "Review with the 14 checks" | moved to step 6 and sharpened (19 checks, each with its input) | new layout options pass and grey read pass come before it |
| SKILL.md:26 step 5 art roughs | moved (merged into S §3 step 7) | one art step after the layout plays |
| SKILL.md:27 step 6 detail, story, lighting | moved and sharpened (S §3 step 7: re-run the checks on the dressed place, busiest moment, lowest setting) | a clean greybox can fail once dressed |
| SKILL.md:32 L-01 | sharpened (spawn facing, key-action cues, never a wall) | WL-07 |
| SKILL.md:33 L-02 "distinguishable from the real approach directions and camera" | kept and sharpened (S L-02: tallest shape, every fork in each approach direction, return trips included, unique silhouette, identity symbol, markers on approach; RA §4 C4, §6.1, PB §4 carry the approach directions) | WL-23, CF-14, WL-12; environment-designer proposal. Round 1 had narrowed it to the intended direction only (review F2); repair round 1 restored every approach direction |
| SKILL.md:34 L-03 | sharpened (calm the rest first; reserved colours and motion off listed sight lines) | VC-04, LC-01 |
| SKILL.md:35 L-04 | sharpened (cheap first exposure; the teaching sheet) | GD-24, teaching sheet |
| SKILL.md:36 L-05 | sharpened (names the counter tool) | GD-12, GD-24 |
| SKILL.md:37 L-06 | sharpened (uneven gaps, reveals behind a turn, rewards at achievements; pacing map) | RH-01, CF-13, GD-11 |
| SKILL.md:38 L-07 "default jump height is 7.2 studs, so a ledge above it is a wall"; "no walk over ~15 s" | replaced (S L-07: the jump is measured, default character uses JumpPower 50; the 15 s starting value is pointed to in `spaces.md` §3; route table and timed walks in RA §6.2) | the 7.2 figure applies only when `CharacterUseJumpPower` is false (StarterPlayer.yaml:243-252, 329-339); the walk limit lives in one place (V6); environment-designer proposal |
| SKILL.md:39 L-08 | kept, one line added (a repeated trip multiplies wasted seconds) | WL-29 |
| SKILL.md:40 L-09 | sharpened ("why is this here?" line; dead boundary as risk and reward) | WL-04, GD-29 |
| SKILL.md:41 L-10 | sharpened (movement pattern, drawn area = hit area, worst-case crowd) | GD-06, VR-20, VR-06 |
| SKILL.md:42 L-11 | sharpened (dummy and known-size object in every blockout space; exaggerations listed) | WL-21 |
| SKILL.md:43 L-12 | sharpened (story facts at stop points, never on a decision cue; theme cues) | WL-22, SI-04, MD-02 |
| SKILL.md:44 L-13 | sharpened (dead space named and resolved) | WL-16 |
| SKILL.md:45 L-14 | kept | still right |
| SKILL.md:48-52 rules | kept; :50 sharpened (Unproven + could-not-check); rules added (P/F/U re-rated each round, screening aids, PROPOSAL values and probes, contrast before detail) | V14, CR-17, WL-30 |
| SKILL.md:55-59 self-check | sharpened (S §6 points to RA §7; :57 "14 checks" → 19 checks; :58 "walk times computed from coordinates at 16 studs/s" → route table plus timed walks) | the self-review moved to the file used before hand-back (RA §7) |
| review-artifact.md:1 header | kept, J018 line added | brief rule |
| review-artifact.md:6 §1 intro | kept, diagram and route JSON added | measurable route data |
| review-artifact.md:8-21 node fields | kept (10 fields); fields 1, 3, 4, 8 sharpened (read rank, tool per action, critical facts, recovery in seconds); node geometry and route table rows added | job-stage workflow cites "the 10 node fields": the count is kept |
| review-artifact.md:24 §2 | kept; analytic vs played walk labels added | CR-17 |
| review-artifact.md:27-30 §3 encounters | sharpened (movement pattern, counter, group ring, same tell, drawn area = hit area, worst-case crowd, hazard rules pointer) | GD-06, GD-12, SS-19, VR-20, VR-06, GD-30 |
| review-artifact.md:32 "Review (14 checks; ... no point totals)" | sharpened (19 checks, input column, re-rate every check) | WL-30 fixed list; game-designer and environment-designer proposals |
| review-artifact.md:34-47 checks 1-14 | kept as C1-C14; 2, 3, 4, 5, 7, 8, 10, 11, 12 sharpened with measurable pass conditions; check 3's "optional alternatives are found without rescue" kept in C3 as the optional alternatives the route graph signals (node field 10), hidden secrets excepted (repair round 3; rounds 1-2 had dropped it); check 4's "cues distinguishable from the real approach directions and camera" kept as C4 "from every fork in each direction players approach it" (repair round 1) | measurable from Studio captures |
| review-artifact.md:49 §5 output | sharpened (input per finding, one column per round, honest recap, revisit backlog) | WL-30, CR-13, GD-33 |

Nothing in the old books was removed as wrong except the 7.2-stud jump as the default (row L-07). The 14-check list grew to 19; no old check was dropped.

## d. Command runs (V3) and proposals from other roles (V11)

All runs 2026-10-22 on synthetic samples in the maker's scratch folder (`scratchpad/level-design/v3/`). No Studio instance was connected (`list_roblox_studios` returned none), so every Studio recipe is marked "probe first" in the book.

| Check id | Command or tool mode | Sample input type | Result |
| --- | --- | --- | --- |
| RA §6.2 (C3, C8, C10, LD4, LD12) | the 9-line `ld_route_table.py` exactly as printed in the book | route JSON: 5 nodes, 4 edges (two with `via` corner points), 4 ledges, walk 16, jump 6.4, margin 1 | runs; spawn→fork 96 studs 6.0 s, fork→mine 164 studs 10.2 s, mine→sell 243 studs 15.2 s OVER 10 (all hand-checked); ledges 6.0 climb and 6.8 block flagged CHECK, 3 and 10 ok. Wrong with no error: a bent path with no `via` (too short), stairs and slopes, jumps and waits not timed, sprint not in `walk_speed`, node at a part centre; listed beside the recipe |
| RA §6.3 (C2, C7, LD13) | `look_check.py value <cap> --box goal --box stall --box crates --compare-subjects` (environment M1 form) | in-scene first view 1280 × 720 with sky, ground, HUD bar, a light goal tower, two mid-value competitors | runs, writes the JSON and `<cap>.luminance.png`; `rank_by_median` goal, stall, crates; goal ratio to ring 3.51 |
| RA §6.3 false reading | same, goal tower darkened; tight box (roof corners take sky) and a loose box | in-scene, dark goal | goal ranks last by median (0.055) but shows the widest spread (0.46 tight, 0.57 loose) from the sky beside its roof: a false pass on "widest spread". Book: box below the horizon or tight to the body, read both numbers, eye check on the grey image |
| RA §6.3 (phone size) | `look_check.py thumb <cap> --size 844x390`, with and without `--box` | same capture, a phone aspect | without a box: `invalid-mask`, but the thumbnail and 4× sheet are written; letterboxed `content_box_px.x0` 75, scale 0.541; with `--box` the value re-run measures. Listed as silent behaviour |
| RA §6.4 (C4, LD13) | `look_check.py silhouette <A> --compare <B> --out <json>` (the book's form) | flat magenta-key captures 512 × 512: tower, the same tower recoloured, a dome | runs; IoU 0.94 recoloured (same silhouette: fails uniqueness), 0.23 tower vs dome; writes `<A>.silhouette.png` next to the input. In-scene capture: `invalid-mask` |
| RA §6.4 false reading | same | tower with a pink roof on the magenta key | the roof is keyed out with no error: bbox top 61 instead of 20, IoU 0.87. Book: key colour far from the landmark; compare `bbox_px` with the still |
| RA §6.5 (C4, C10, C11) | environment M8 one-liner (`scene_audit.load_probe` + part tops) | plain-JSON probe: a floor, a 4.4-stud ledge, a part tilted 30° | runs; tops 0.0, 4.4, 5.43 (hand-checked: 2 + 12/2·sin 30° + 1/2·cos 30°). Wrong with no error: wedge, mesh or union lips; terrain (not in the probe) |
| RA §6.7 (C3, §5) | the markup one-liner extracted verbatim from the book | the first-view capture + marks JSON (one arrow, two circles) | runs, writes the PNG (output identical to the test run); default font small: the table carries the numbers |
| RA §6.6 jump; §6.1 captures; C19 (M9) | Studio probes (`inspect_instance`, play-mode jump ladder, `screen_capture` top-down, quality level) | — | not run: no Studio instance connected; marked "probe first" in the book; starting value 6.4 studs computed from JumpPower 50 and Gravity 196.2 (`Humanoid.yaml:640-660`, `Workspace.yaml:458-467`) |
| RA §6.4 false reading (repair round 1) | `look_check.py silhouette <A> --compare <B> --out <json>` (the book's form) | flat magenta-key 512 × 512: the same tower with no shadow (twice), with a darker-magenta cast shadow on the key to the right and to the left | no shadow vs no shadow 1.0; with vs without shadow 0.46; shadow right vs left 0.47; bounding box 111 → 191 px; verdict "measured", no error: a false pass of uniqueness. Book: shadows off for the capture (probe first), the black-fill sheet looked at for every landmark, false reading listed |
| RA §6.4 loud case (repair round 1) | same | the tower on a flat key whose floor strip is 65 levels darker than the backdrop (a floor lit apart from the wall) | `invalid-mask` (loud); a floor strip 40 levels darker stays inside the default key tolerance and keys cleanly (IoU 1.0). Book: listed as loud, match the floor and backdrop shades |
| RA §6.4 black-fill sheet (repair round 1) | `look_check.py silhouette <landmark.png> --out <json>` once per landmark, then the Pillow sheet one-liner exactly as printed | two black fills (no shadow; shadow right) | runs; writes `<landmark>.silhouette.png` for the A input only (a `--compare` run does not write B's: the book says to run each landmark alone); the sheet (512 × 256) shows the shadow joined to the outline at a glance |
| RA §6.3 false reading (repair round 1) | `look_check.py value <cap> --box goal --box stall --box crates --compare-subjects` (M1 form), then `value` with the goal box alone | in-scene 1280 × 720: light sky, mid ground, a dark goal tower with its top against the sky, two mid-value competitors, a HUD bar | rank_by_median stall, crates, goal (goal last); goal spread 0; goal `ratio_to_ring` 3.49 (highest; stall 1.63, crates 1.26), `brighter_than_ring` false; alone against its own ring 12.1. Boxes first drawn 5 px inside the objects gave ring = subject and ratio 1.0 with no error. Book (round 1): the first read is first by median or highest `ratio_to_ring`; both false readings listed. **Corrected in repair round 2 (rev2 F1):** the 3.49 came from the shared ring (one ring around all boxes, its median the sky), not from the tower's own surroundings; a highest shared ratio does not show a goal stands out (rev2 run: a goal invisible on its wall had the highest shared ratio, 3.62). The book now reads each subject's own ratio (12.1 here) against the marker target |
| RA §6.1 Studio steps (repair round 1) | `list_roblox_studios` | — | no Studio instance connected; the shadow-free flat-key capture and the top-down are marked "probe first" (proposal row to `studio-mcp` probes) |
| RA §6.3 shared-ring false reading (repair round 2) | the book's two §6.3 runs extracted verbatim (shared `--compare-subjects` run; one `value --box <subject> --exclude-box <others>` run per subject; the printer one-liner) | in-scene 1280 × 720, light sky, mid ground, HUD bar, two dark stalls against the sky: (a) a goal sign the same value as its mid wall; (b) the same sign clearly darker than a light wall | (a) rank goal, c2, c1 (goal first by median); goal shared `ratio_to_ring` 2.39, own 1.0: invisible, and the median route alone would have passed it. (b) shared 11.9, own 8.74 (highest; stalls 7.14, 6.45). The rev2 review's own variant gave shared 3.62 (highest) against own 1.09. Book: shared ratio not read; screen = own ratio at the marker target and first by median or own ratio; both false readings listed |
| RA §6.3 median false reading (repair round 2) | same, verbatim | in-scene, a light goal tower against a light sky, two dark competitors on the ground | rank goal first by median and the highest shared ratio (3.97), own 1.04: a false pass on both shared routes; own ratio below the 3:1 marker target, so the screen fails and the still is looked at. Book: listed |
| RA §6.3 dark goal (repair round 2) | same, verbatim | in-scene, dark goal tower with its top against the sky, two mid competitors on the ground | rank c1, c2, goal (goal last); own goal 14.18 darker, c1 1.42, c2 1.32: passes on own ratio (correct) |
| RA §6.3 phone size (repair round 2) | the book's `thumb` command verbatim (`--size 844x390 --out`), then the own run on the thumbnail with boxes scaled by `scale` 0.541 plus `content_box_px.x0` 75 | the light-on-sky first view | writes the thumbnail, its sheet and the JSON; rank goal, c2, c1; own goal 1.04 at ring 8 and at ring 4 (same as full size). A box within 2 px of the letterbox edge on sky: ring median unchanged (padding is a thin share of the ring) |
| RA §6.3 printer one-liner (repair round 2) | the printer as first written, `... for f in sys.argv[1:] ...` with `<dir>/<view>-own-*.json` | run through cmd (Python `subprocess`, shell) | **failed**: cmd does not expand the glob (`OSError: Invalid argument ...-own-*.json`); PowerShell passes globs to native programs unexpanded too. Fixed: the one-liner globs itself (`glob.glob(sys.argv[1]+'-own-*.json')`, argument `<dir>/<view>`); re-run verbatim through cmd and in PowerShell: prints every subject's ratio and direction |
| RA §6.3 ring crowding (repair round 2) | own run with and without `--exclude-box` on the neighbours | a goal sign the value of its light wall, dark stalls 3 px either side | 1.05 both ways (`ring_excluded_px` 770; ring median still the wall): the ring is a median, a neighbour on a small part of it does not move it. Book: listed as silent behaviour; the exclusion stays as hygiene |
| RA §4 C19 (repair round 2) | own run per cue box at both settings (`value --box <cue>`) | in-scene: a hazard rim with a dark outline (highest setting) and the same rim without it (lowest) | 4.09 high, 1.10 low (both lighter): the drop below the marker target flags the lowest-setting view to be looked at. Book: C19 screens each cue by its own ratio at both settings |

Proposal rows from other roles against `level-design`:
| Row | Decision |
| --- | --- |
| environment-designer (proposals row on `level-design/SKILL.md`): L-07's 7.2-stud jump → measure the jump in Studio and record it in the game profile; add to the review: first view keeps the orientation conventions, landmark with a unique silhouette and an identity symbol visible from its entry, floors readable for the smallest gameplay object, hazards show source and containment | adopted: S L-07, RA §6.6; RA §4 C2 (conventions), C4 and S L-02 (silhouette; the identity symbol from each zone's entry, a check line since repair round 1), C16 (floors), RA §3 (source and containment) |
| game-designer row 21: add map mechanics in the background, spawn-to-contact and neutral parity, cover counters, intentional heights, simple collision, items 30-50 % hidden, surprises out of the focal light, dead space, materials follow rules | adopted: RA §4 C15, C17 (spawn-to-contact, neutral parity, cover counters), C10 (intentional heights and simple collision, for every map since repair round 1), C16, C3, C18; surprises in RA §7 LD6 (measured by environment RD12) |
| game-designer row 22: keep Pass / Fail / Unproven with no point totals; a re-review re-rates every check | adopted: S §5, RA §4 intro, RA §5 (one column per round) |
| progression-designer row 28: the route table in seconds goes to the progression designer as an input for earning cycles | adopted: RA §1 (route table row: sent when travel is part of an earning cycle); S §7 #17 |
| game-designer row (tool `tools/level/route_times.py`) | co-signed in `proposals/level-design.md` (the book carries a 9-line screening recipe until the tool exists) |

## Repair round 1 (review `reviews/level-design-rev1-reviewer.md`, fix-first)

Repaired by J018 maker level-design · claude-opus-5-5 · high · 2026-10-22. Keep list kept: job card, options pass, the jump correction, the route JSON and its script (unchanged), teaching sheet and pacing map, 19 fixed checks with inputs, the screening-aid rule, worked example 1, the core principles table, the proposals. Line counts after repair: SKILL.md 103 lines (§7 starts at about 16.2 KB; description 394 characters); review-artifact.md 147; plan-and-blockout.md 78; worked-examples.md 18. V5 pass (script): every C, LD and L id named in table a exists in the books; every landed row names a self-review or review line (seven untagged rows gained their LD pointer); the §6.4 sheet one-liner was extracted verbatim from the book and run (same output as the test run); worked example 2 re-read after the pacing and first-view rule changes; worked example 1 re-read after the §6.3 change (its ranking claim still holds).

| Review finding id | Fixed where / declined: why |
| --- | --- |
| F1 | Fixed. RA §6.1 flat-key row: the game-design flat-key capture (pointer to `game-design/references/review.md` §7, key filling the border, floor under the landmark included), shadows off with `Lighting.GlobalShadows` false and restored after, probe first. RA §6.4: cast-shadow false reading with my runs (0.46, 0.47) and the review's 0.78; a black-fill sheet looked at once for every landmark (so passing pairs are seen too), its one-liner run verbatim; the shaded-floor case listed as loud. RA §4 C4, §7 LD13, PB §4 Landmarks row, S §7 #5 check name shadows off and the sheet. Proposals: game-design `review.md` §7 shadow rule; `look_check.py` shadowed-key warning; `studio-mcp` probe (c); job-stage studio-operator deliverable (4) shadows off. Table d rows added |
| F2 | Fixed. S L-02 and §3 step 5, RA §4 C4, RA §6.1 (one decision view per fork per approach direction), RA §7 LD13, PB §4 views and Forks row: every direction players approach a fork, both ways, return trips included. Coverage table c rows for SKILL.md:33 and review-artifact.md:34-47 corrected (round 1 had narrowed the rule) |
| F3 | Fixed. RA §4 C4: each zone's or team's identity symbol shows from its entry at the game camera on a phone viewport (1 entry capture per zone, RA §6.1 row); LD13 names it. RA §3 and LD8: the same attack gives the same tell, two uses compared on the partner's captures. Coverage rows WL-23, GD-13 and the environment-designer proposal decision corrected |
| R1 | Fixed. WE §2 pacing map now covers the whole 81 s spiral (segments sum to 81 s; peaks at 15-19, 34-40, climax 67-81); gaps 15 s and 27 s, end to start; climax after 54 s (last third). PB §6 defines a gap as the end of one peak to the start of the next, the climax counting as a peak |
| R2 | Fixed. S §3 budget line split into "looked at" and "measured only"; RA §6.1 gains a "Count · look" column per capture; C5, C9, C10, C11, C19 inputs and RA §2 say which captures are measured only. C9 now uses the progress cue named per node and the views already taken (no extra images); C19 uses M1 at both settings with the same boxes as its screen |
| R3 | Fixed, wider than asked. RA §6.3: the first read is "first by median, or the highest `ratio_to_ring`" (spread is support only), so a dark goal against a light sky passes on its contrast; the false reading is listed with my run (goal last by median, `ratio_to_ring` 3.49 highest, 12.1 against its own ring); a box inside the object (ring = subject) added as a third silent case. S L-03 and PB §4 say "brightest or strongest contrast"; C2, C7, LD13 say "first read"; WE §2 drops "and spread" |
| R4 | Fixed. Intentional heights and simple collision moved into C10 (every map) with the intentional-height list and a collision-view capture as inputs; C17 keeps spawn-to-contact, neutral parity and cover counters. Coverage rows WL-14, WL-15 and game-designer row 21 decision corrected |
| R5 | Fixed. Two proposal rows: `spaces.md`:1 and **workflow** `job-stage.js`:591 ("14 checks" to "C1-C19") |
| R6 | Fixed. PB §3 blockout brief carries the material-to-rule table, the orientation conventions and the intentional-height list (`spaces.md` §3, §4, §6) |
| R7 | Fixed. S L-02 (identity symbol), L-03 (gameplay colours), L-09 (dead boundary as risk and reward), L-16 (items partly hidden; FL1 measures floors), L-18 (one treatment, one material) now point to `spaces.md` §5-§7 instead of restating; each keeps its level-specific part (approach directions, the sight lines I list, per-node treatment and material lists, hazards by shape and value) |
| R8 | Fixed. PB §2: options drawn with Python + Pillow on a blank canvas from each option's route JSON, x and z in studs to pixels at one fixed scale for all three; the §6.7 markup recipe is no longer named there |
| R9 | Fixed. C12: a cold reader names the theme, one story fact and a mood that matches the job card's personality words; S §7 #10 check says the same |
| R10 | Fixed. PB §1 row "Conflict and story reason": one sentence per mode and the objective's reason in the world's story (`spaces.md` §2), with an example |
| R11 | Fixed. RA §6.1 top-down row: probe first; restore the edit camera after (`studio-mcp` P-05) |

## Repair round 2 (review `reviews/level-design-rev2-reviewer.md`, fix-first)

Repaired by J018 maker level-design · claude-opus-5-5 · high · 2026-10-22. Keep list kept unchanged: every rev1 repair (flat-key shadows off, approach directions, identity symbol, same tell, pacing example, budget split, heights and collision in C10, R5-R11), the job card, options pass, blockout order and brief, the jump correction and probe, the route JSON and script, the silhouette recipe and sheet, the markup one-liner, the teaching sheet and pacing map, the 19 checks with inputs, the screening-aid rule, worked example 1, the core principles table, the proposals. Line counts after repair: SKILL.md 103 lines (description 394 characters; §7 still starts at about 16.3 KB); review-artifact.md 151 (§6.3 grew by four lines: the two runs, the screen rule, the phone step); plan-and-blockout.md 78; worked-examples.md 18. V3: every §6.3 command extracted verbatim from the book and run on in-scene samples (table d, repair round 2 rows); the run found one more fault (the printer's glob is not expanded by cmd or PowerShell), fixed and re-run. V5 (script): 113 coverage rows, every C, LD and L id they name exists in the books, every row of kind "check" names a check id; worked example 1 (first-view ranking, C2) and worked example 2 (grey read pass first view) re-read after the §6.3 change: example 2 now states the rim's own contrast against the marker target; example 1's claim (the shop not in frame) holds under the new rule.

| Review finding id | Fixed where / declined: why |
| --- | --- |
| F1 | Fixed. RA §6.3 rewritten: the shared `--compare-subjects` run is read for `rank_by_median` only; each subject (the goal and its 2-3 competitors) gets its own `value --box` run with the other boxes excluded from its ring, and a printer one-liner lists each own `subject_ring_ratio` with its direction. The screen passes when the goal's own ratio reaches the marker target (art-bible §7 separation targets, starting `PROPOSAL` 3:1) and the goal is first by median or by own ratio, and the grey image agrees. I went one step past the review's smallest fix: my runs show the median route alone passes an invisible goal too (a sign the value of its wall, a light tower on a light sky: first by median, own 1.0 and 1.04), so both routes now need the own ratio at the marker target. False readings added with numbers: the shared ring (review run 1.09 own vs 3.62 shared; my run 1.0 vs 8.7), median-first on a same-value background, ring crowding (a median: neighbours on a small part do not move it), value-only (hue-only or tiny goals judged on the still). C2 pass text names the rule; C19 screens each cue by its own ratio at both settings plus the shared rank run (a cue below the marker target at the lowest setting, or a rank change, is looked at); §6.1 settings row points to §6.3; PB §4 first-view row "strongest in contrast against its own surroundings", measure "rank and own contrast"; S §7 #3 check; WE §2. LD13 and LD16 point to §6.3 and C7/C19 and need no text change. Coverage table d row "RA §6.3 false reading (repair round 1)" corrected |
| R1 | Adopted. C16 input: numbers (environment FL1) + the modeler's occlusion render per item type (`modeling-design/references/review.md` GR3; partner); no new capture row. Art-review RD7 checks the same render in the busy scene, so the level review only reads it |
| R2 | Adopted. C15 pass: outside the planned moments no still shows the mechanic as the brightest or most saturated thing in view, and consecutive stills show no motion of it near a decision; seconds of eye draw at speed come from the owner's play-test at the gate (§6.8). Input names the normal-round stills and the busiest moment. Proposal row for `game-design/references/spaces.md` §1, whose check still counts seconds on a capture |
| R3 | Adopted. Proposal row for environment `review.md` RD2 and `measure-captures.md` M1: the first-read rule of §6.3 (own contrast at the marker target, first by median or own ratio, spread as support only) and the shared-ring false reading; the same row states that RD13's key forks are a subset of the level review's fork set, right for each role's scope |
| (own, from V3) | The §6.3 printer first used a shell glob (`<dir>/<view>-own-*.json`); cmd and PowerShell pass it unexpanded and the one-liner fails. It now globs itself; run verbatim in cmd and PowerShell. Tool proposal row: `look_check.py value --compare-subjects` to report each subject's own ring ratio, so the screen is one tested run instead of one per subject (V13) |


## Repair round 3 (final) (review `reviews/level-design-rev3-reviewer.md`, fix-first)

Repaired by J018 maker level-design · claude-opus-5-5 · high · 2026-10-22. Last round by the lead's decision; text-only. Keep list kept unchanged (every rev1 and rev2 repair, the §6.3 own-contrast screen and printer, the route JSON and script, the 19 checks with inputs, worked examples, the core principles table, the proposals). Line counts after repair: SKILL.md 103 (unchanged); review-artifact.md 152 (one line added: the coordinates-only screen); plan-and-blockout.md 78; worked-examples.md 18. The FOV half-angles were recomputed (2·atan(tan 35° · aspect): 51.2° at 16:9, 56.6° at 844x390, so "about 57°" rather than the review's 56°). Worked example 1 re-read: "turning the spawn 35° frames the gate" agrees with the new coordinates-only screen. No command changed, so no V3 re-run was needed; LF endings checked.

| Finding | Fixed where / declined: why |
| --- | --- |
| F1 | Fixed with the review's smallest fix. RA §4 C3 Pass when: "intended destinations, and the optional alternatives the route graph signals (node field 10: shortcuts, side routes, side areas), are found without rescue in the played walk; hidden secrets excepted". Table c row for `review-artifact.md:34-47` corrected (it had said "kept") |
| R1 | Adopted. PB §4 grey read pass, first-view Pass when: in frame, own contrast at the marker target, the lightest or strongest in contrast among its competitors (§6.3), the tallest, and the lines lead to it. "Lightest" alone no longer passes |
| R2 | Adopted. RA §6.3 new bullet "With coordinates only": bearing from the spawn facing to the goal and each competitor against half the horizontal field of view (`Camera.FieldOfView` vertical, default 70: about 51° at 16:9, about 57° on a wide phone; an inference), labelled analytic, C2 stays Unproven until the capture; a subject near the edge is borderline because the default camera sits behind the character |
| R3 | Adopted. RA §6.1 settings row: key views = the first view, the fork views, the zone entry views and one view per hazard (the looked-at set without the busiest moment and the stills) |
| R4 | Adopted. (a) RA §6.3 limits: a hollow or thin subject (arch, ring, gate frame) reads what shows through the gap: box its solid part or judge it on the still. (b) RA §4 C19 input: a cue thinner than the ring (rim, edge line) is boxed tight to the cue or looked at on the lowest-setting still |
| R5 | Adopted. RA §6.3 limits line keeps one example number at most per false reading (own 1.09 vs shared 3.62; ratio 1.0 for a box inside the object); the other run numbers removed (they stay in table d). RA §6.4 shadow and key-colour cases cut to one example each. The body's pointer "(coverage file, table d)" moved to the RA header, which now says the J018 runs live in table d. §6.4's calibration pair (0.94 recoloured, 0.23 tower vs dome) kept: it is the one example that sets the IoU threshold's meaning |
| R6 | Adopted. RA §7 LD17: for a failing or unmeasured read, a contrast list for the goal (value, hue, saturation, shape, size, position, motion: wins, ties or loses); the fix changes one that loses. §6.3's value-only limit points to it |
| Declined | None |
