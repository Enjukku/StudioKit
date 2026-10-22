---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: "J018 stage 1b: synthesis of knowledge/jobs/J018-riot-craft/extracts (owner-supplied Riot transcripts, 14 videos)"
supersedes: []
roles: [orchestrator, art-director, reference-images, modeler, environment-designer, animator, vfx-designer, sound-designer, ui-ux-designer, level-design, game-designer, feature-builder, architect, marketing, film-director, live-ops-designer, reviewer, qa-lead]
---
> Author: J018 synthesizer · claude-opus-5-5 · high · 2026-10-21

# Process and iteration

ADDED TOPIC (prefix PI). How work moves from rough to done: cheap stages first, gates that freeze decisions, passes over the whole, one problem at a time, letting go, time boxes, and knowing when to stop. Folds in the small extract topics timebox, stage gates, production gates and decisiveness.
PI-01 to PI-05 set the order (cheap first, gates, closing doors, blockout in engine, work small). PI-06 to PI-08 run passes (even level, one problem at a time, bracketing). PI-09 to PI-11 keep momentum (not precious, park the hard part, time box). PI-12 to PI-15 end well (when done, useful finish, scope, decisive marks).
Related: options and picks in `references-ideation.md`, notes in `critique-feedback.md`, composition before detail in `composition-focus.md` (CF-01).

### PI-01 The cheapest stage goes first; expect big changes while it is rough
- principle: Concept and roughs go first because huge changes are cheap with quick images and expensive once art is polished. Assume rough work may change completely; changes after feedback are normal. Early passes are for experiments and mistakes: "fail fast and learn quickly".
- why: The cost of change rises with every stage; fear of mistakes means nothing interesting gets made.
- apply: Pipeline order per asset: reference images, then blockout or proxy, then final. No final Blender models, polished VFX or final audio until the owner approved the reference direction. Rough passes are labelled rough and made loose and quick, several options before refining one.
- check: Each job has an approved reference revision dated before final production starts; the work shows more than one rough option or pass before polish; no part is polished while the whole is still rough.
- mistake: Polishing before direction is set; being "too scared of making mistakes" (R03:102-104).
- examples:
  - R00a: the foil's drawings came back with changes: "Is that normal ...? Yes" (R00a:802-820).
  - R03: loose AO painting on Caitlyn's hair in the early pass (R03:100-106, 128-132).
- roblox_fit: No change.
- roles: orchestrator, art-director, reference-images, modeler, environment-designer, vfx-designer, animator, sound-designer, ui-ux-designer, architect, reviewer
- also: references-ideation, composition-focus
- sources: R00a-F21 (R00a:802-820); R03-F04 (R03:100-106, 128-132)

### PI-02 Gates freeze decisions: rough, approved direction, materials, polish
- principle: Visual work passes gates, each freezing a level of decision: a rough or blockout gate (read, story, shapes, UVs and base colours in place), a direction or early-production gate (refined; feedback still welcome, but nothing moves drastically after it), a render or materials gate (metal looks metal, fabric fabric), and polish (only small light and finish touches; big changes such as "change the composition" go to the next update).
- why: Collaboration needs open phases, but a project must close feedback at some point to finish and ship; each frozen level protects the work built on it.
- apply: Every visual job states its gates and tags each review request with the current gate; after the direction gate, layout and pose do not move; at polish, structural notes are logged as follow-ups for the next update. Studio mapping [inference]: blockout, approved layout, materials (SurfaceAppearance, materials), lighting and post-effects polish.
- check: A gate record per stage with a capture each; after the direction gate, diff the layout and pose against the approved version: nothing moved; review notes carry their gate tag; big changes after polish appear as follow-up tickets, not edits.
- mistake: Moving parts after green light; working "on different people's feedback for forever" (R13:695); skipping stages.
- examples:
  - R08: thumbnail, green light, render, polish; green light usually reached in 1.5-2 weeks of a 5-6 week illustration (R08:45-46, 656-692, 706-712).
  - R13: blockout, early production, polish: "it's a bit too late ... maybe next time" (R13:663-697).
  - R10: brief, reference, sketch on template, grayscale form, colour, rebalance, detail; about a day per step (R10:43-49, 918-938).
- roblox_fit: Fits live updates: deferred changes go to the next update [inference]. Matches the kit's owner gates (G1, G2, G3) at job level.
- roles: orchestrator, art-director, reviewer, modeler, environment-designer, marketing, reference-images, live-ops-designer, qa-lead
- also: critique-feedback, pipeline-production
- sources: R08-F27 (R08:45-46, 656-692, 706-712); R13-F30 (R13:663-697); R10-F26 (R10:43-49, 918-938)

### PI-03 Closing doors: from broad to narrow, never reopen
- principle: Explore from broad to narrow: show a broad set, then each round close what did not work and expand what the team liked. Resist reopening closed doors.
- why: Each cycle gets more precise; reopening restarts the spiral.
- apply: The orchestrator records closed directions in the job folder (and in tried-and-failed when final); later briefs never re-propose them without new owner words.
- check: Each round has fewer, more specific options than the last; no closed direction reappears without a new owner decision.
- mistake: Going around in circles; reopening closed doors.
- examples:
  - R00a: the Closing Doors method described by the concept artists (R00a:836-858).
- roblox_fit: No change.
- roles: orchestrator, art-director, reference-images, game-designer, reviewer
- also: references-ideation, critique-feedback
- sources: R00a-F23 (R00a:836-858)

### PI-04 Block out first, in the engine, and play it before detail
- principle: Start with a quick proxy of big shapes and colour blocks to check proportions and silhouette, in the engine, so you can press play at any moment and test it with the real player tools. Only then push readability and add detail.
- why: A proxy changes fast, so the big picture is settled before costly detail; something that looks good may not play right, and only playing shows it.
- apply: Blender primitives with flat colours (or Studio Parts) imported into Studio and captured at the game camera next to the default avatar before detailing; level blockouts are built in Studio and play-tested through the Studio MCP during blockout, naming the player tool tested (sprint, ability, weapon) [inference].
- check: The proxy capture at the game camera passes a black-fill check for proportion and silhouette before any detail; the blockout hand-back lists the play-tests run and what they found (angles closed, dead space).
- mistake: Detailing before proportion and silhouette are proven in game; blocking out in an external tool and testing late (R09:869-878).
- examples:
  - R00a: the process starts with a proxy of shape and colour blocks (R00a:1181-1205).
  - R09: Diego plays a smoke character to test chokes, then closes an angle and spots dead space (R09:202-208, 370-389, 869-878).
- roblox_fit: Studio Play through the Studio MCP; Parts blockouts are the direct analogue [inference].
- roles: modeler, environment-designer, level-design, game-designer, feature-builder, art-director, reviewer, qa-lead
- also: shape-silhouette, world-level-readability, game-design-fun
- sources: R00a-F33 (R00a:1181-1205); R09-F12 (R09:202-208, 370-389, 869-878)

### PI-05 Work small early so only big shapes can be judged
- principle: Do early stages at a small size: it stops you rendering detail you do not need yet and keeps the focus on the whole image.
- why: At large size you see pixels and want them to look good; at small size you can only judge big shapes.
- apply: Early option images and renders at low resolution (small ChatGPT images, Blender preview renders), reviewed at small size; full resolution only after the direction is fixed [inference for sizes].
- check: Early-stage files are small and are reviewed at thumbnail size, not zoomed in.
- mistake: Working big early and polishing pixels before the image works.
- examples:
  - R08: small canvas "literally disallows you from being able to do more than you need to" (R08:302-312, 713-724).
- roblox_fit: Small viewing also matches phone display size [inference].
- roles: reference-images, art-director, modeler, marketing, environment-designer
- also: composition-focus, references-ideation
- sources: R08-F13 (R08:302-312, 713-724)

### PI-06 Work in passes over the whole; big things before small
- principle: Bring every part of the asset or scene to one level of finish, then the next; never finish the head while the rest is blank. Body and big motion first; hair, face and small details last: the last 10 % lifts good to great.
- why: The whole is judged together; an even pass gives a strong first read early and a consistent finish; one over-finished part looks out of place.
- apply: Plan passes over the whole asset (blockout all, base colour all, shading all, detail all; for clips: root, body, offsets, then hair, fingers and face). Review compares parts of equal importance side by side.
- check: In each review render, no region is clearly more finished than its neighbours of equal importance; clips have body mechanics approved before secondary detail is keyed.
- mistake: "work on the face a lot and then everything else was just kind of left untouched" (R03:220-222); grass "a blur" while the statue is finished (R02:420-422).
- examples:
  - R02: moving to the pedestal before detailing the fox further (R02:260-268, 420-422, 562-564).
  - R03: her own early habit of finishing the face first, corrected (R03:220-232).
  - R04: body, root cadence, poses and offsets get most of the way; hair and face add appeal; "a good animation ... for three hours of work" (R04:972-982, 1078-1088).
- roblox_fit: On phones details are hidden first, so the body and big forms matter most [inference].
- roles: modeler, environment-designer, animator, vfx-designer, ui-ux-designer, art-director, orchestrator, reviewer
- also: weight-timing, critique-feedback
- sources: R02-F16 (R02:260-268, 420-422, 562-564); R03-F10 (R03:220-232); R04-F40 (R04:972-982, 1078-1088)

### PI-07 One named problem per pass; fix the worst first
- principle: Name the problem you are solving now and solve problems in order (pose, then how the pose supports the story, then lighting). In each review pass, find what feels worst, fix that, and look again; checklists help, but the end result decides.
- why: One problem at a time is manageable and each solved step constrains the next; fixing the biggest problem first converges fastest.
- apply: Each work stage in a brief names its single problem and its check; the agent opens the next problem only when the current one passes [inference]. Each review pass: render, name the single worst problem, fix, re-render; keep a short craft checklist as backup.
- check: The hand-back or review log lists one problem per pass with its check result and before/after captures.
- mistake: Mixing all problems at once.
- examples:
  - R08: "the pose is good; what's her story? How does her pose support the story?" (R08:311-318, 464-472).
  - R04: "animation is just about looking at it and seeing what feels wrong" (R04:724-748).
- roblox_fit: No change.
- roles: art-director, animator, modeler, vfx-designer, film-director, orchestrator, reviewer, qa-lead
- also: critique-feedback
- sources: R08-F14 (R08:311-318, 464-472); R04-F33 (R04:724-748)

### PI-08 Find the right number by bracketing
- principle: Much of the work is trial and error: try a value, look, overshoot, come back. Bracket each key number with a too-low and a too-high value, then pick between.
- why: Feel is found by comparison; two extremes show where the right value is.
- apply: For each key number (count, height, size, start time, volume, tween length) capture 2-3 options at the game camera and compare. Source values: spawn count 35, then 200 (R06:56); height 200, 800 too high, 400 right, 600 (R06:68-75); spread 100 then 150 (R06:102-103).
- check: The hand-back shows the tested values and why the chosen one won.
- mistake: Keeping the first value without comparing.
- examples:
  - R06: "a big part of my job is just messing with things and seeing if it works" (R06:56, 68-75, 99-103).
- roblox_fit: Change properties live through the Studio MCP and capture each option.
- roles: vfx-designer, animator, environment-designer, sound-designer, ui-ux-designer, reviewer
- also: critique-feedback
- sources: R06-F08 (R06:56, 68-75, 99-103)

### PI-09 Not precious: most attempts fail, so delete, redo and let go
- principle: Polished work hides many failed versions: more than 80 % of what an experienced artist makes is never seen, and the best result may take three to five tries. Early on, do not get attached: move things freely, delete a section that misbehaves and redo it, drop your own idea for a better one, and welcome notes.
- why: Quality comes from iterating and selecting, not a perfect first try; attachment stops necessary changes; rebuilding tangled work is cheaper than patching it.
- apply: Plan 3-5 options or passes for key assets (key poses, hero models, key art, signature sounds) and pick. Early option work is disposable: regenerate or reshape freely. When a section breaks (a twisting arm), clear its keys for that range and re-key. Do not defend a first version against a better proposal.
- check: The hand-back shows the options tried and why the chosen one won; review notes record whether a broken section was rebuilt or patched.
- mistake: The "inability to sort of, like, let go of your precious ideas" (R00b); being "married" to earlier work (R04:426); "getting too attached to something can really be sometimes the burden" (R08).
- examples:
  - R00b: 80 % "absolute garbage"; three to five tries at the same animation (R00b:2255-2277, 3316-3336).
  - R04: "my arm was twisting around weirdly ... so I'm just starting over" (R04:418-432).
  - R08: smudging parts around at about 50 % instead of careful liquify (R08:534-553, 642-656).
  - R07: do not be precious; bad output is normal; ask for feedback (R07:610-615).
- roblox_fit: No change.
- roles: animator, modeler, environment-designer, vfx-designer, ui-ux-designer, sound-designer, art-director, reference-images, orchestrator, reviewer
- also: critique-feedback, references-ideation
- sources: R00b-F19 (R00b:2255-2277, 3316-3336); R04-F19 (R04:418-432); R08-F24 (R08:534-553, 642-656); R07-F30 (R07:610-615)

### PI-10 Park a stuck part and come back
- principle: When a part does not come right (a face, a likeness), leave it, work on another part, and return with a fresh view, like skipping a hard question on a test.
- why: It frees head space, keeps the whole moving, and the answer often comes in the background.
- apply: Time-box each part in the build plan; log a stuck part, move on, revisit after the next pass.
- check: The plan log shows stuck parts revisited, not abandoned or over-worked.
- mistake: Staying on one part too long.
- examples:
  - R03: she leaves the face for the hair and returns (R03:402-404, 984-994).
- roblox_fit: Same.
- roles: modeler, art-director, animator, vfx-designer, sound-designer, ui-ux-designer, environment-designer
- also: none
- sources: R03-F18 (R03:402-404, 984-994)

### PI-11 A time box forces the readable choice
- principle: Real production has time boxes (a League skin: 6-7 weeks per character, legendaries about 8; a polished prop "a day's worth"). The box forces the question "what reads at game height and meets player expectations?" and gives permission to stop; without it, work sinks into rabbit holes.
- why: Unlimited time leads to endless doodling and half-finished assets.
- apply: Every brief states a budget (passes, iterations or time); agents spend it on the game-height read first. Each review asks three questions at the game camera: does it look right in the play space, does it read right, does it tell the right story?
- check: The hand-back states the budget used and answers the three questions with a play-space capture; the far read was done before detail.
- mistake: Going "down a rabbit hole" and having "only gotten the head done" (R02:158-160); her first full-time skin got "this doesn't look quite ready" (R03:458-468).
- examples:
  - R03: Sun-Eater Kayle's many wings and materials inside the box (R03:449-492).
  - R02: the fox statue reviewed for play space, reading and story (R02:154-164).
- roblox_fit: Capture in Studio at the real camera via the Studio MCP.
- roles: orchestrator, modeler, art-director, animator, vfx-designer, environment-designer, reviewer, qa-lead
- also: critique-feedback
- sources: R03-F20 (R03:449-492); R02-F09 (R02:154-164)

### PI-12 Know when it is done: written stop criteria, repeating notes
- principle: Work is never finished, only stopped; over-rendering is real. Stop when the written criteria hold: every material reads at game height (gold reads gold, not bronze), the finish matches the approved characters, nothing looks incomplete up close. The review loop ends when notes stop coming or only repeat; the lead calls done.
- why: Past that point extra work is invisible to players and costs time; most viewers do not notice small flaws.
- apply: The brief states stop criteria: (1) every material identifiable at game size, (2) finish level matches the anchors, (3) no unfinished area in one close render. Reviewers write "no new notes" when a round only repeats; the orchestrator sets polish budgets and calls done.
- check: At the game camera name each material; side by side with approved characters for finish; one close render for incomplete areas; compare notes between rounds: all repeats means close.
- mistake: Not knowing when to stop; "I could take like two years" (R08).
- examples:
  - R03: "the golds are actually gold and not bronze or like silver" (R03:430-448, 1088-1092).
  - R08: done "when the notes stop coming in ... they're not really adding to the piece anymore" (R08:807-821).
  - R04: "I'll tell you when you're done" (R04:818-856).
- roblox_fit: Phone size moves the stop point earlier [inference].
- roles: modeler, art-director, orchestrator, animator, environment-designer, reviewer, qa-lead
- also: critique-feedback, materials-detail
- sources: R03-F19 (R03:430-448, 1088-1092); R08-F30 (R08:807-821); R04-F45 (R04:818-856)

### PI-13 Finish a concept only as far as the next maker needs
- principle: Concepts are not taken to full illustration; they go as far as the next maker needs. "Concepts live and die off of being useful."
- why: Finishing is slow and adds little to a concept.
- apply: Reference-images deliverables stop at clear shapes, colours, values and callouts the modeler or rigger needs; polish goes into key art only when marketing needs it.
- check: The modeler builds from the sheet without questions about shape or colour.
- mistake: Spending time polishing concept art.
- examples:
  - R11: the final concept brought to "a form of finish that I would typically do for a concept" (R11:302-305, 436-438, 448).
- roblox_fit: Same.
- roles: orchestrator, art-director, reference-images, modeler, film-director, marketing
- also: references-ideation, cross-craft
- sources: R11-F24 (R11:302-305, 436-438, 448)

### PI-14 "It would be cooler" is new scope: log it
- principle: Teams keep adding work because "it would be cooler" and then bite off more than they can chew; know what you sign up for before raising scope.
- why: Uncounted ambition breaks budgets.
- apply: A "make it cooler" idea mid-job becomes a logged ticket or an owner decision with its cost, never silent scope.
- check: Items added after G1 appear as tickets with a cost estimate.
- mistake: "We bit off way more than we can chew" (R10:402).
- examples:
  - R10: Riot teams repeatedly raising scope (R10:398-406, 412-416).
- roblox_fit: No change.
- roles: orchestrator, game-designer, live-ops-designer, architect, feature-builder
- also: cross-craft
- sources: R10-F16 (R10:398-406, 412-416)

### PI-15 Decisive marks: few bold decisions, not many small tweaks
- principle: Make each mark a decision and do not rework the same area again and again; "they can see your fear if you show it in your brush." Accept a mistake and fix it later rather than averaging options together.
- why: Repeated, indecisive strokes read as unsure and muddy; decisive shapes read as confident and design the gesture fast.
- apply: Prefer few, bold shape decisions: in Blender change a shape with one deliberate edit and re-render, not dozens of micro tweaks; in reference prompts ask for "bold, confident, clean shapes, hard edges"; avoid blurred, overworked paint-overs.
- check: In the render or image, look for muddy, overworked zones (many tiny value steps, blurry edges); fail where a shape boundary is unclear.
- mistake: "If you repeat your brush too much, they'll know that you're not sure what you're doing" (R13:105-107).
- examples:
  - R13: the default hard round brush at 100 % opacity for all shape design (R13:11, 95-129).
- roblox_fit: No change.
- roles: art-director, modeler, environment-designer, vfx-designer, animator, reference-images
- also: shape-silhouette, materials-detail
- sources: R13-F05 (R13:11, 95-129)
