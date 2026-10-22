---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 G3
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-22

# G3 packet: J018 Riot craft rebuild

**Decision asked:** accept the rebuilt agents (all 17 roles and the shared skills reference-images, orchestration and level-design, commits `9d8fa2a`, `034dce9`, `61cc867` and the close-out commit), and answer the 11 owner-gated proposal groups in `g3-proposals.md` (one word each; defaults stated there).

## What changed, in one paragraph
Every role's design and craft books and role-file body were rebuilt with the Riot craft library as a core source: 443 findings and 20 universal principles (`knowledge/reference/craft/riot/`). Each book now has a "Core principles for this craft" section checked against `universal-principles.md` (J018-D2), new cheap stages before detail (options at equal finish, grey value and black-fill passes at the game camera, blocking before polish, beat sheets, read plans), and a self-review in which every line names its input. Measures written into books are labelled screening aids with their known false readings, and a failing number is checked by eye before a fix note. No tools, rules, job recipes, saved workflows, templates or evals changed; those are the G3 proposals.

## Per role: what it gained, coverage, review
Coverage = library findings tagged for the role; landed in the books (including untagged findings the maker chose to use) or rejected with a reason. Full tables: `coverage/<role>.md` (findings, universal principles, old-book changes, command runs, proposal sweep, master follow).

### animator
Coverage: 139 tagged, 153 landed, 2 rejected with a reason; old rules removed as wrong: 2; review: pass (rev3); table: [coverage/animator.md](coverage/animator.md)

- Tells are sized by who reacts. An enemy's tell is a distinct pose held for the designer's reaction window, and the player's own move stays tight. The pick is proved from frame counts and black-fill at the game camera with effects hidden, in grayscale and with reduced motion on.
- Plan stages come before keys: a beat sheet with subtext and the mechanic verb, identity anchors and hook shapes, and one black-fill contact sheet per key clip with a recorded pick. Blocking is shown at a check-in before any spline. Timing takes are compared in numbers, and the owner picks feel on playable previews at the gate.
- Self-review lines for each pass run on clip_check numbers, sample-curve computations, at most 8 key frames and Studio captures. In-game checks now name the test hooks the builder must supply: a hit-reject hook, a rate trigger and a hit-area overlay.
- The timing list is a shared contract with VFX and sound: stage names, verb, end-of-state tells, freeze frame and sync rule. Confirmed-outcome motion waits for the server, and paid reveals share one windup.
- Promo, thumbnail and cutscene stills now start from a one-sentence premise and reuse the signature key pose from the game's set. This is checked with silhouette --compare against the clip's key frame, so marketing and cutscene art shows the character players meet in play.

### modeler
Coverage: 230 tagged, 221 landed, 9 rejected with a reason; old rules removed as wrong: 2; review: pass (rev4, lead-added round); table: [coverage/modeler.md](coverage/modeler.md)

- Every checkable standard now has a line in the self-review. New: detail clumped on the detail spots (detail-density image at phone size), archetype readable in every option's black-fill, basic-form shading, the saturation peak on the focal zone, theme nods and the costume motif on props, iconic qualities checked again on the finished model at hand-off, and the reads in the planned order.
- A held weapon or tool is now judged in the avatar's hand at the game camera, back and front, not lying on the floor. This is the read players actually get.
- Studio captures now use the game's FOV and the phone's aspect. The top-5 % value and saturation images no longer mark a whole flat torso as 'the extremes'. Every new command line was run on test images.
- Simple models have one short path, stated the same way in every place the agent reads it. The texture, rig and kit books keep only the how and point to one place for each standard, so a later fix lands once.
- The books are leaner where they are loaded. The craft SKILL fits fully inside the compaction window. The design SKILL now keeps the principles up to P14 after compaction (before: P11).

### game-designer
Coverage: 145 tagged, 141 landed, 4 rejected with a reason; old rules removed as wrong: 0; review: pass (rev3); table: [coverage/game-designer.md](coverage/game-designer.md)

- Pitches start with a labelled warm-up round. Each candidate has its own hook source, and the batch includes one idea from outside games and one big swing. All options are shown at equal finish, with one pick and a goal question to the owner. First images are drawn from the game camera and checked at the real tile size (size from surfaces.md, --box on the hero; with no measured size the check reads 'not measured', never an invented size).
- Pre-production and feature specs start from the target experience and the game's parameters. Behaviour is designed before looks, with a feedback stack per action, threat and hazard sheets, role cards and a read rank. A loop gets no production art until it has a dated grey-box verdict. Briefs use the full shared header and write TBD (step N) for values a later step decides, instead of inventing them.
- Reviews name the four parts and label each input by what it can prove. They finish with a could-not-check list. When the agent reviews another craft's output, it has one check list per job-recipe slot, judged on studio-operator captures rather than the maker's hand-back.
- Measured checks now run on inputs the tools can actually read. Black-fill measures (lineup size rank, look-alike IoU, variant footprint) use flat-key captures. Clip timing uses still-before-and-after clips with nothing else moving, so onset_ms and visible_ms mean what the books say. The studio-operator is asked for exactly these captures.
- Fairness and honesty rules carry their checks. Odds are shown before the buy button and update while a boost is active. Every paid reveal tier has the same windup, and there is no near-miss. Cosmetics change no stats and stay inside a footprint band. Every threat has a counter and a two-channel tell, and its drawn area comes from the data.

### character-rigger
Coverage: 63 tagged, 54 landed, 9 rejected with a reason; old rules removed as wrong: 1; review: closed by lead after final repair (rev4 edge case fixed; measures are screening aids); table: [coverage/character-rigger.md](coverage/character-rigger.md)

- Before the modeler builds anything, the rigger checks the character for motion problems: mass on joints, drapes over the arms, costly capes and chains. It then poses the plan at the game camera and gives each finding an owner, so collar-in-jaw and cape-through-arm problems are fixed with a sentence, not a re-cut.
- It offers the controls that make poses read: clavicles and hips for wind-ups, a head world-orient switch for spins, hand shapes, one control per hook-shape part, and chains driven as one mass. Each control goes in the manifest with its range and the need it serves.
- S4 and S5 are proven in numbers that hold in the cases that used to give false passes. Cap exposure now covers caps of any face shape (Bisect-with-Fill n-gons, fans, concave caps) on the posed mesh, and it stops on a missing or empty `cap` group or a hidden part. The black-fill count runs on a crop with an area check. Quaternion ranges are in `quat` units, and two-axis bones are measured by swing in degrees.
- Hand-offs carry what the checks need: the modeler delivers each part's cap and socket faces in a `cap` group. The manifest's validation query passes the swing check on to the animator at S6.
- Images only where a number fails, plus a few key poses at the game camera. Every self-review line names its input (numbers, key images, Studio captures).

### art-director
Coverage: 277 tagged, 255 landed, 22 rejected with a reason; old rules removed as wrong: 1; review: pass (rev3); table: [coverage/art-director.md](coverage/art-director.md)

- Direction rounds now go: success test, research board, hooks with the warm-up set aside, equal-finish roughs inside one image cap (regenerations count toward it), then a grey and black-fill pass before any colour pick. The owner sees only the 2-3 options that passed, and each option's packet answers the game designer's six concept-art questions.
- Each environment measure (band, depth contrast, saturation field, reserved hues) is now read from the environment-only capture, and clipped white from the UI-off cut below the horizon. Characters, the HUD or a sun disk can no longer push the result into a wrong brief to the environment or VFX designer.
- The bible's section 7 is now the one place for every standard the crafts measure against: value bands with the lower-body ratio, separation targets (1.5:1 for a character, 3:1 for a marker), reserved colours, key light per place, shape code and one identity-anchor count. The art director's checks match the modeler's and the environment designer's own.
- Reviews start with a cold read and run big to small. They pick their self-review lines from the job-type table and use tested commands, each with its 'wrong with no error' traps. Each visual note gets a marked capture; a generated paint-over is used only for the 1-2 worst notes, inside the image cap.
- Brief checks name measures that can answer them (for example, the slam core's p95 from value --compare-subjects), and every tool mode is named with the flags it requires (thumbnail --size-source).

### environment-designer
Coverage: 195 tagged, 179 landed, 16 rejected with a reason; old rules removed as wrong: 1; review: pass (rev4); table: [coverage/environment-designer.md](coverage/environment-designer.md)

- Walls and ground can no longer pass review as one hue. VB12 now passes a surface only on hue variation, so a built-in material under one part Color is flagged 'monochrome'. The book gives the Roblox fixes: hue-shifted part Colors, a MaterialVariant or SurfaceAppearance ColorMap, and terrain patches of materials with different MaterialColors.
- Saturated colour stays on the focus. VB6 measures the saturated pixels outside the focal elements and the read plan's eye-path accents against a starting limit of 0.02 (PROPOSAL). This fails loud walls and decoration spread along the route; a warm, quiet upper wall still passes.
- New materials come from the game's palette. VB11 and the new M12 recipe compare the material zoo's lit faces with the art bible's palette roles. An off-palette material shows up as a number, not only as a judgement on a picture.
- The core principles, the self-review lines and the art bible's standards use the same measures and one set of starting values. The value bands and the reserved-colour distance are read from the art bible's §7, so the art director and the environment designer cannot drift apart.
- The whole rebuild: a read plan before any image, one option round with a reasoned pick, the sun chosen in grey on the greybox, separation targets that can fail, and a 51-line self-review that names its inputs and has a fix-job scope. The result: places where players find the route, pickups and hazards on a phone in the busiest moment.

### film-director
Coverage: 76 tagged, 75 landed, 1 rejected with a reason; old rules removed as wrong: 1; review: closed by lead (rev4 finding fixed in the shared flash counter); table: [coverage/film-director.md](coverage/film-director.md)

- The flash count on the animatic now gives the same count at 30 and 60 fps. It counts an eased flash once and ignores camera pans over pillars and windows. It still catches two halves of the frame that flash in turn. The old count gave 10 or 0 flashes per second for the same 4 Hz pulse, depending on the frame rate.
- The value check no longer fails a planned silhouette reveal, for example the boss dark in a fire-lit gate. The check passes when the backdrop ranks first, the subject's box is inside the backdrop's box and the subject is darker than its ring. The sky can now be measured with its own mask.
- A planned J cut or a sound warning before a reveal is checked against its own planned offset, not reported as a sync fault. Only cues marked sync: locked must keep the one-sided sync rule.
- A 3-second in-play camera moment runs only the passes it needs: text options, one blocking key frame with its numbers, the animatic and the Roblox checks. The full options, value, boards and two-take passes are kept for moments with a key beat. Skipped passes are marked n/a with the reason.
- The rebuild as a whole: the director now pitches a premise, a hook and a sell list. It compares 2-3 greybox options at equal finish and plans a first-second read and a value key per shot. It blocks and checks values on proxies before the boards, and times key beats as tell, build, beat, peak and result. It self-reviews each stage with named inputs: numbers for every case, images only within the cap.

### vfx-designer
Coverage: 214 tagged, 184 landed, 30 rejected with a reason; old rules removed as wrong: 4; review: closed by lead after final repair; table: [coverage/vfx-designer.md](coverage/vfx-designer.md)

- The agent fills a read card before it builds any layer: verb, three read lines, a loudness tier with caps, values that must match the game rules and come from config, the information areas, and stop criteria. It then compares 2-3 options and picks one for a stated reason, so it no longer polishes its first guess.
- It blocks each effect with placeholder sprites on the real timing and checks it in. Then it passes value (grey) and black-fill silhouette gates before it adds colour. Footprint, peak time and stage starts are frozen after the check-in, so texture work never hides a weak read.
- Its self-review proves build, one peak on the contact marker, fast-in, footprint and cover with clip numbers and masked stills. The fast-in check now reads the effect's size, not its screen area, so a correctly eased ring passes and a linear-growth burst fails.
- The flash-safety count now uses the same algorithm as the film director's script (net rise and fall). An eased flash or a grade pulse counts once at 30 or 60 fps. A second count at 3 % of the screen catches medium flashes that the first count missed, and the books list each case where a count is wrong with no error.
- Its in-game pass covers the busiest scene, grayscale and reduced modes, the bystander's view on a second client, an overlay of the server's hit area, a 100-trigger repeat and device sync, each with a named input and image budget. Feel at normal speed stays the owner's call on a playable preview.

### sound-designer
Coverage: 96 tagged, 91 landed, 5 rejected with a reason; old rules removed as wrong: 2; review: closed by lead after final repair; table: [coverage/sound-designer.md](coverage/sound-designer.md)

- Paid reveals are now proven honest by the right number. Results are compared by their momentary maximum loudness: a 400 ms window, or the shortest result's length if shorter. A louder rare result can no longer pass by hiding behind a longer tail, and an honest longer result is no longer failed. Sample peaks are compared too.
- The pooling check now catches per-hit AudioPlayer creation. It counts creations during a 10 s burst on the Client data model, and a grep for Instance.new("AudioPlayer") outside the pool module backs it up. The old before-and-after count passed create-and-destroy code.
- The sharp-is-danger check compares like with like: threat hits against friendly one-shots. Correct tells, warnings and charges are no longer failed, and nothing pushes the agent to flatten them.
- The worked examples teach the right sizes. A T2 bag-full event gets a 150-300 ms confirm, not a milestone flourish.
- Across the whole rebuild, the agent frames each cue by job, verb and rate. It stages cues on the animator's event ids, with the attempt cue at once and the outcome layer on confirmation. It does a temp pass before polish and measures every file. Each measure lists its known wrong-number traps. The owner answers named goal questions at three check-ins, so the agent never claims it listened.

### ui-ux-designer
Coverage: 144 tagged, 138 landed, 5 rejected with a reason; old rules removed as wrong: 1; review: pass (rev3); table: [coverage/ui-ux-designer.md](coverage/ui-ux-designer.md)

- Press timing is now measured correctly in real Studio play-tests. A new lag line reads each frame's coverage from metrics.json and finds the first frame after the press that rises above the highest pre-press value. A popup closing or a reveal inside the capture no longer makes a 33 ms press read as 100-167 ms, which was a false FAIL sent back to the builder.
- The agent can no longer pass the touch-size check by calling a target 'minor'. How often the player uses a target sets its kind: buy, close, back, tabs and HUD buttons are frequent at 44 pt. The worked example's close X is now 150 x 150.
- Paid reveals are checked for tells on every tier, not only the lowest against the highest. A rarity tint that only rare items show during the windup is now caught.
- Each screen-size term has one meaning. The 'phone layout frame' is the 1920 x 1080 canvas that holds the small-viewport arrangement. The 'phone-fit view' is the 565 x 318 resample used for reading checks. The touch-size thresholds apply to the right frame.
- Whole rebuild: flow sheet with tap counts, then 2-3 wireframes, then a grey value pass proving the read order, then rule sheet, target images, Figma and motion. Self-review S-01 to S-49 is staged by step, and each line names its input. Measured checks give their wrong-without-error cases, attempt cues are kept apart from confirmed outcomes, and the review slot asks for named captures.

### marketing
Coverage: 135 tagged, 117 landed, 18 rejected with a reason; old rules removed as wrong: 1; review: pass (rev4); table: [coverage/marketing.md](coverage/marketing.md)

- Works big to small like box art: a brief with the hero, the things the image must sell, a one-line premise and the symbol. Then a labelled warm-up, 3-5 rough options from different hooks judged at tile size, and an approval point after which the big shapes do not move. Every crop is cut from one layered master, and no crop is ever stretched.
- Measures with masks traced from the image itself and checked on an overlay, not coarse polygons or boxes. Its value study uses fixed, checked cuts. It knows where each tool gives a wrong number without an error and labels every self-review line by what proved it.
- Plans a new game's icon as its own brief and round of roughs (identity). An update or event icon is a crop of the master. Under a capped brief like E1 (8 images), it has a clear plan: 1 warm-up + 3 thumbnail roughs + 3 icon roughs + 1 spare.
- Can now actually run its short-video checks. One command steps the edit into stills named with their times and counts flashes per second. A second reads sound onsets from the editor's WAV without music. There is a budget of about 12 stills, a sync window that matches the sound designer's (-17 to +40 ms), a masking check, and 'not verified' when there is no WAV or no onset.
- One rule lives in one place: the image route is in image-pipeline section 1, the light-check budget in image-review section 1, and the video stills budget in channel-kits section 3. The role file and the craft core table now only point to them.

### progression-designer
Coverage: 20 tagged, 36 landed, 0 rejected with a reason; old rules removed as wrong: 0; review: pass (rev2); table: [coverage/progression-designer.md](coverage/progression-designer.md)

- Every reward event gets a tier from what it changes for the player, measured at its real rate, and each tier is rarer than the one below it. Frequent rewards stay small, so rare ones still feel big. VFX, sound, UI and art receive one table with each event's trigger, rate and text name.
- Reward rates are now right for obbies and tycoon tasks too. Repeated activity completions and repeated kills are counted from the event trace. The book also names the stretches where a player gets no reward, and which inputs make the numbers wrong without an error.
- The decision check compares the two policies run by run between resets, so it finds tracks with no real choice after each rebirth as well as at the start.
- Paid random rewards are honest: odds are exact fractions that sum to exactly 1, results worth less than the price get no celebration, and the 90% and 99% roll counts are computed. An outcome that sells back into the currency it was paid with is stopped and sent to the owner as the stake-and-win-back case.
- Hand-backs are leaner: a tier table only when rewards change, capstones checked on each finite track's planned finish, a set tuning-round budget, and every self-check line names its input.

### live-ops-designer
Coverage: 36 tagged, 61 landed, 0 rejected with a reason; old rules removed as wrong: 0; review: pass (rev2); table: [coverage/live-ops-designer.md](coverage/live-ops-designer.md)

- Before release, the agent checks every event, theme, variant, limited item or new world on 13 named Studio captures with 19 checks. The checks cover the event promise, the entrance in the first view, rarer rewards looking bigger, no celebration on a rejected purchase, identity kept across variants, honest paid reveals (event luck boosts included) and a new world that looks clearly new. The agent no longer judges an event from the makers' hand-backs.
- Each event brief is checked against one list of brief lines: promise, what fans want with counts, theme niche, story, tone shift, reward family, kept anchors, variant type, the new world's escape and tier rows. Each line is filled or marked n/a with a reason, so a line can no longer be left out without anyone seeing it.
- Each craft gets its ask at the cheapest stage, with the capture it will be judged on. The concept round now states how each option fits the approved scope, and it does not argue against a premise the owner already fixed.
- Feedback counts are less likely to mislead. The book now lists the tool's silent wrong readings with an eye check for each: a date-only end date, several loud authors none with half the messages, the same message in two overlapping exports, and an end date set later than the window.
- Every self-review line names its input, and each rule is written in one place (partner timings, brief lines, the core principles that point to their L-rules), so the books do not drift apart.

### architect
Coverage: 24 tagged, 23 landed, 1 rejected with a reason; old rules removed as wrong: 1; review: pass (rev3); table: [coverage/architect.md](coverage/architect.md)

- Plans for any feature players see or hear now include a written hand-over row by row (attempt, outcome by tier, pending, refusal, tell, cleanup), so effects, sounds and UI react to the real server result, and a refused action never shows a hit or a reward.
- Client prediction now has one rule in one place: a 'predicted' row, used only where the spec allows it, only on the player's own client, removed in the frame a denial arrives, and never for money, rewards or paid reveals. A shooter keeps fast feedback and a purchase can never fake success.
- Hit-stop is now planned so it always ends: one owner per track and per emitter sets the speed back to the base speed. An overlap test and a check with a 150 ms delay are named in the QA seeds and the review checklist, so 'frozen after two quick hits' and 'freeze on the wrong pose under lag' are caught before players see them.
- Each player sees effects for their own role: bystanders get no camera shake or flash, and every gameplay fact has two channels so that it still reads in grayscale, with sound off, with reduced motion and at the lowest graphics quality. The architect checks this with a 21-line self-review that names the input for each line.
- Asks to partners go to the right owner (the animator gives the clip list and the contact-pose hold; the architect decides where each clip starts). Test hooks and comfort settings point to the builder's single list, so the books no longer drift apart.

### feature-builder
Coverage: 52 tagged, 49 landed, 3 rejected with a reason; old rules removed as wrong: 2; review: pass (rev3); table: [coverage/feature-builder.md](coverage/feature-builder.md)

- Wires what players see and hear truthfully: the press answers in the input frame, the big moment waits for the server's confirmed result (a predicted layer only as a small predicted contract row the spec allows), pending when slow, refusals say the fix at the control, counters never lie, paid reveals are honest and go through the policy module.
- Hit-stops can no longer freeze a character or drop a slow or attack-speed change: one owner per track with a stop-until time and the last-set base speed, only on the attacker's and target's clients, with offline overlap, interruption and speed-change tests and a replication probe.
- Delivers the partners' test hooks and debug log in the test build only (the published build is proven to contain none by a rojo build + grep check), Studio-gated, with leftover hook settings printed and cleared so the next play-test is not silently wrong.
- Self-review with named inputs: a tested literals grep that now catches Title Case helper strings, legacy waits and BrickColor; UI safe-area and text-fit checks as numbers for every state and size, with stills only for the main state and failures.
- Works in the right order with the right partners: contract with feedback stack, playable skeleton, presentation pass, then a worst-case pass on every change; asks the qa-lead, animator, VFX, sound, UI and progression partners for their tables at the named step.

### qa-lead
Coverage: 77 tagged, 58 landed, 19 rejected with a reason; old rules removed as wrong: 1; review: pass (rev3); table: [coverage/qa-lead.md](coverage/qa-lead.md)

- Every state-changing request gets tested for a rejection (no success layer, no balance change, refusal cue present, a pending state under latency). The server log is the oracle, not the eye.
- Drawn danger areas, countdowns, counters and shown tiers are checked against the gameplay data field. PF-04 uses numbers for every variant and only 3 key stills. Paid reveals get identical windups and the platform-policy rows.
- Random variation is tested where it lives. Each semantic particle layer gets a property read on the candidate (no range, no keypoint envelope, no random start). Ranges the code rolls are run at both ends offline. The Seed hook only repeats a server roll.
- Rows run under the conditions players meet: smallest phone, busiest moment, lowest and highest quality, latency, reduced motion, grayscale, sound off and two clients. These include clarity levels that keep threats at full strength and frequent events that never move the camera.
- Every result names its input, and a spec-only rate stays 'not verified' on screen. Image measures are screening aids with their false readings listed. Findings use the binding format with a separate evidence field and a fix direction plus retest rows.

### reviewer
Coverage: 137 tagged, 54 landed, 83 rejected with a reason; old rules removed as wrong: 1; review: closed by lead after final text repair; table: [coverage/reviewer.md](coverage/reviewer.md)

- The reviewer reads the code before the builder's claims and reads every change in two orders (file order, then each player path with one failure sweep). It tries to make each candidate safe before reporting it, and it closes with protect and retest steps, a could-not-check list and a weakest-part line.
- For anything players see or hear, it checks 19 code-side rows. It catches success shown on a denied request, counters that logic reads, paid reveals that hint at a better result, shakes on bystanders, hit-stops that stay frozen, presentation that decides gameplay, and test hooks that run outside Studio.
- Comfort checks now cover all five settings in the architect's contract (reduced motion, shake, flashes, screen effects, clarity). The reviewer reports a flash or tint that checks the wrong setting, or no setting at all, and a setting the comfort module does not provide.
- Its screening patterns give the same results in ripgrep and in git grep at a fixed revision, and each one lists its known false hits and misses. S8 now finds repeating tweens built from function calls.
- One stop rule for each review depth, a calibrated example of a clean change, and worked examples that match the severity table. The reviewer gives an honest 'no blocking findings' instead of inventing a finding.

### reference-images
Coverage: 176 tagged, 168 landed, 8 rejected with a reason; old rules removed as wrong: 0; review: pass (rev2); table: [coverage/reference-images.md](coverage/reference-images.md)

- Every new look now starts with 6-12 one-line hooks written as text, which cost no images. Only the 3-5 strongest are generated beside a labelled warm-up, with one radical option. This is the same broad search the art director runs.
- Rough options no longer fight their family's lock. Character, prop and model roughs keep the lock's three-quarter view, and the game-camera read is checked at R3 on a named input (a view image, or the modeler's blockout render). If none exists, the check is reported as NOT REVIEWED.
- Light and mid-value subjects (cream pets, gold, white fur) are no longer dropped from the pick sheet because of the image model's backdrop. RO5 now tests the subject against the game's own ground (new check C12). On the test pet this gave 4.17 on green (it separates) and 1.31 on sand (a real merge).
- The self-review now carries checks it only claimed before: depth in three planes, detail grouped inside a contrasting frame, palette role shares summed by hue family, the prop top line, the jump apex, edge finish, swatch-first materials, read order and where saturation peaks. The asymmetry check now looks at the element itself and at a mirror copy, so it can actually fail.
- The known false readings are wider: a radial backdrop falloff gives the wrong box with no error, the mirror number is useless on three-quarter views, a role's share is read wrong on shaded images, and a final is no longer compared against a pick from another family. Each of these cases was re-run on synthetic samples and recorded in coverage table d.

### orchestration
Coverage: 79 tagged, 75 landed, 4 rejected with a reason; old rules removed as wrong: 0; review: pass (rev3); table: [coverage/orchestration.md](coverage/orchestration.md)

- Before any brief, the lead writes four lines: the problem, the constraints (camera, device and input, player count, budget, policy, locks), a named target experience and a success test the owner will see. Every brief then carries budget, stop criteria, Roblox docs rows and display sizes. The worked example brief now passes the lead's own self-check, and its image caps follow the reference-images rounds.
- Gate packets fit one screen in a fixed order: the artifact as players meet it, one goal question that uses the job card's goal word, options at equal finish with play value and cost, the recommendation with its weakest part, labelled checks with a could-not-check list, and the doors the answer closes. Each question has its own Shown: line, counted line by line against the image budget.
- D1 direction asks each lead for the right kind of answer. Leads that own a look bring research, hooks, a warm-up set aside and one radical option. The architect and performance engineer return limits, never option menus. The progression designer keeps the options its books shape, so the owner still chooses between concrete experiences.
- Owner notes become one-problem repair briefs by layer, and the owner's note always stands. A closed option stays out of later briefs. A retime is a contract change with one rule in one place. 'Done' is said only with evidence, including a rejected-request capture.
- The self-check now starts 1.5 KB earlier (byte 18,703). It covers every per-type card item, the effect row included. The screening aids (taste grep, per-line Shown count, hand-back hook) were run on sample files, and each lists its false hits and misses, including the empty payload file.

### level-design
Coverage: 96 tagged, 78 landed, 18 rejected with a reason; old rules removed as wrong: 1; review: closed by lead after final text repair; table: [coverage/level-design.md](coverage/level-design.md)

- Judges whether the goal is the first thing a player reads in the first view by the goal's contrast with its own surroundings: one shared run gives the ranking, then one run per subject. The screen passes only when the goal reaches the 3:1 marker target and ranks first by brightness or by own contrast. Goals that blend into their wall or the sky now fail; a dark tower against a bright sky now passes.
- Plans a level from a job card, three layout options, a route graph with node geometry, and a route table in seconds from a tested script. The jump is measured in Studio, not taken as the wrong 7.2 studs.
- Reviews with 19 fixed checks. Each check names an input it can really get: C15 is judged on what its stills can show, and C16 uses the modeler's occlusion render. A missing input makes a check Unproven instead of guessed.
- Checks the gameplay read under low graphics settings by measuring each cue's own contrast at both settings. A cue that falls below the marker target is looked at before any fix note.
- Every measuring recipe is a labelled screening aid with its tested false readings listed. The commands run unchanged in PowerShell, cmd and Bash.

## Blind pilot
Not run: the owner dropped the blind old-vs-new test (J018-D3, "we will not be doing the test though."). Instead, each stage 3 reviewer judged on one of the role's eval briefs whether the new books make better work than the old (`df13ff4`); every reviewer answered yes, with the weak spots it named fixed or listed. Real games are the test bed.

## What was checked, and what was not
- Gate-verified: `python tools/verify.py` RESULT: PASS (sync, index, 665 tests, SKILL.md sizes, descriptions) at the close-out commit.
- Script-verified by the lead: all 649 extract findings mapped into the library; every library finding has all fields; role frontmatter (tools, model, effort, skills) byte-identical to `df13ff4`; no library IDs, transcript lines or Riot names added to book bodies.
- Reviewer-verified: coverage rows opened at their landed location; commands run on synthetic samples of the real input form (Blender headless renders, synthetic captures and frame folders).
- Not verified: every step that needs Roblox Studio (no Studio was connected in J018; those lines are written as "probe in Studio first"); feel at normal speed (the owner's call on a playable preview); results on a real phone.

## Usage (record only, J018-D4)
| Stage | Tokens (subagents) |
| --- | --- |
| 1a readers (17) | 2.08 M |
| 1b synthesizer | 0.77 M |
| 1c DestructionSimulator cross-check | 0.50 M |
| wave 1 (3 roles, 18 agents) | 5.85 M |
| wave 1 modeler round 3 | 0.42 M |
| wave 2 (9 roles, 52 agents) | 17.59 M |
| wave 2 rounds 3-4 | 2.12 M |
| wave 2 final repair | 0.63 M |
| wave 3 (5 roles + 3 skills, 44 agents) | 13.09 M |
| wave 3 final repair | 0.23 M |
| proposal sweep + library keeper | 1.67 M |
| master follow | 0.73 M |
| G3 consolidator | 0.31 M |
| **Total** | **45.99 M** (owner estimate 10-15 M, dropped as a limit by J018-D4; the lead chat not counted) |

Why it ran over the estimate: 20 rebuild targets instead of 17, Opus high for every maker and reviewer (J018-D4), and review loops on hand-written measuring code (3-4 rounds for six roles). That loop is the main lesson: G3-P1 moves those measures into tested tools.

## Owner decisions open (from `g3-proposals.md`)

| ID | Decision | Rows | Recommendation | Default if you do not answer |
| --- | --- | --- | --- | --- |
| G3-P1 | Make the kit tools give right numbers | 22 | yes | Known tool bugs stay. Books keep hand-written measures. |
| G3-P2 | Job recipes: cheap passes first, crafts join early | 33 | yes | Recipes keep the old order. |
| G3-P3 | Job recipes: review evidence and review slots for truth | 17 | yes, only for jobs with that risk | No new review slots. |
| G3-P4 | Saved workflows follow the recipes, stale text fixed | 27 | yes | Stale lines stay. Workflows skip the new stages. |
| G3-P5 | Binding rules: honest reveals, no success on denial, review keys | 5 | yes | Rules stay only in the role books. |
| G3-P6 | Templates, game records and eval briefs carry the new stages | 50 | yes | Agents add fields by hand. Some eval checks fail correct work. |
| G3-P7 | Studio probes and capture recipes, run once | 13 | yes | These checks stay "not verified". |
| G3-P8 | New measuring options in existing tools | 44 | yes, after G3-P1 | Books keep one-line commands outside the tool record. |
| G3-P9 | Option images: new art bible families, medium-quality roughs | 7 | yes | Old locks stay. Roughs stay at medium. |
| G3-P10 | New kit tools | 15 | later | Later. |
| G3-P11 | Sound designer: Studio tools and preloaded skills | 2 | no | No change. |

Rows counts include 5 rows that split across two decisions (see the appendix).

Full reasons, evidence, risk and the appendix of all 238 rows: [g3-proposals.md](g3-proposals.md).

