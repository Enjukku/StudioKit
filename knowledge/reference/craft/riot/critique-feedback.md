---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: "J018 stage 1b: synthesis of knowledge/jobs/J018-riot-craft/extracts (owner-supplied Riot transcripts, 14 videos)"
supersedes: []
roles: [reviewer, orchestrator, art-director, modeler, environment-designer, animator, vfx-designer, ui-ux-designer, sound-designer, reference-images, game-designer, level-design, marketing, feature-builder, architect, progression-designer, live-ops-designer, film-director, qa-lead]
---
> Author: J018 synthesizer · claude-opus-5-5 · high · 2026-10-21

# Critique and feedback

How work is judged and how notes are asked for, given and turned into fixes. In our studio reviewers never edit; makers fix; notes go up in a fixed order on one frozen version.
CR-01 is where to judge (in game). CR-02 to CR-07 are asking for, giving and acting on notes (goal questions, the problem behind the note, concrete fixes, paint-overs, direct notes with one driver, early and often). CR-08 to CR-10 are self-review tools (diagnose by layer, fresh eyes, happy misreads). CR-11 to CR-13 are choosing and reporting honestly. CR-14 to CR-16 are pitching, pain points and calibration.
Related: options and picks in `references-ideation.md` (RI-02, RI-19), when to stop in `process-iteration.md`, sound review in `sound.md` (SD-26, SD-27).
Stage 1c (DestructionSimulator cross-check) added CR-17 (what each input can prove; the could-not-check list); the (DS) line in CR-04 comes from the same check.

### CR-01 Judge in the game, at the game camera, in the real place, moving
- principle: A design only proves itself in the game view. Beauty shots and editor viewports excite but mislead: judge at the game camera, in the real map next to its real colours, while moving, after every change.
- why: Camera, scale, surroundings, lighting and motion change the read; it is easy to get attached to glamour-shot choices that fail in game, and an effect can look right in the editor and render wrong in play.
- apply: Every concept, model, clip and effect is reviewed as a play-mode capture at the game camera (Studio MCP `start_stop_play` + `screen_capture`), standing and moving in the real map (also in its brightest and darkest areas), at phone resolution. Blender review renders put a capture of the game map behind the character. Hand-backs label each check MCP-verified.
- check: The review packet includes play-mode captures at the game camera in the real map and decisions cite them; `look_check.py value` and `palette` on those captures show the subject separating from its ground and still fitting the art bible; no decision rests only on a turnaround or editor view.
- mistake: "Difficult to do away with them once you move to an in-game space" (R01); judging only in the modelling tool (R03:1046-1054); "if you don't test it in game, it might look wonky" (R06:129).
- examples:
  - R01: he paints directly over an in-game screenshot to see what works on the Rift (R01:267-275, 916-930).
  - R03: the game map kept behind Caitlyn while painting (R03:234-240); testing her running around Summoner's Rift is how she learned readability (R03:1044-1062).
  - R06: the first cloud was "way too high" and then rendered on the units' bodies in game (R06:65-69, 129).
- roblox_fit: Phone aspect ratio and camera distance change on-screen size; capture at phone resolution and at the game's real camera (third-person or top-down).
- roles: art-director, reference-images, modeler, environment-designer, vfx-designer, animator, marketing, feature-builder, level-design, reviewer, qa-lead
- also: world-level-readability, value-contrast, composition-focus
- sources: R01-F16 (R01:267-275, 916-930); R03-F45 (R03:1044-1062); R06-F07 (R06:65-69, 129); R03-F11 (R03:234-240)

### CR-02 Ask a goal question, never "do you like it?"
- principle: Ask specific questions tied to the goal ("which feels the scariest?"); a broad "do you like this?" gets scattered answers. Others' reactions to labelled options ("this doesn't feel like them", "this feels cooler") then narrow the choice.
- why: A goal question makes every reviewer judge the same thing; the maker is biased toward risky picks.
- apply: Every owner or review question names the goal from the brief ("which reads as most dangerous at phone size?"). Present labelled options to the art director or owner with a recommendation and record who chose and why.
- check: The question text contains the goal word from the brief; the choice record names who chose and the reason.
- mistake: "Hey do you like this?"; picking the option "that definitely doesn't work for anyone" (R11).
- examples:
  - R00a: "which feels the scariest?" (R00a:860-874).
  - R11: he offloads decisions to others' reactions (R11:269-275).
- roblox_fit: No change.
- roles: orchestrator, reviewer, art-director, qa-lead, marketing, game-designer, ui-ux-designer, reference-images
- also: references-ideation
- sources: R00a-F24 (R00a:860-874); R11-F30 (R11:269-275)

### CR-03 Solve the problem behind the note; separate goals from tactics
- principle: A note or request often carries a proposed solution; find the problem behind it ("what are you trying to do?") before acting, because the suggested fix is often not the best. Keep the goal (what the player should feel or do) separate from tactics (how), and say which one a note is about.
- why: The note-giver sees the symptom; the maker knows the craft and can find a better fix. Teams argue past each other when one talks goals and the other tactics.
- apply: For every note that names a solution, the receiving agent restates the underlying problem in one line and, if it differs, proposes its own fix and why. Reviewers write notes as problems ("busy and noisy"), not solutions. Specs and notes have two parts: "player should feel or do" and "how"; a tactic change cites the goal it serves.
- check: Each fix in a hand-back names the problem it solves; after the fix, the original problem is re-checked (for example the noise level in a capture), not only whether the suggested change was made; review comments are tagged goal or tactic.
- mistake: Doing what the note says literally (deleting all the trees); debating tactics while disagreeing on goals [inference].
- examples:
  - R00b: "delete all the trees" meant "really busy and noisy"; cleaner textures and a better composition fixed it; a requested tool to hide water became a fish counter (R00b:2167-2201, 2461-2497).
  - R00d: advice the designer wished they had had when young (R00d:5827-5855).
- roblox_fit: No change.
- roles: reviewer, orchestrator, art-director, environment-designer, feature-builder, architect, modeler, animator, vfx-designer, ui-ux-designer, sound-designer, game-designer, progression-designer, live-ops-designer, qa-lead
- also: game-design-fun
- sources: R00b-F16 (R00b:2167-2201, 2461-2497); R00d-F35 (R00d:5827-5855)

### CR-04 Answer every note with a concrete visible fix; protect the anchor
- principle: Accept notes and answer each with a concrete visual fix, while naming and protecting the asset's identity anchor ("we have to keep the golden disk as a golden disk").
- why: Feedback improves the work; the anchor keeps the one-second read.
- apply: List each note, write the planned fix, make a paint-over (CR-05), apply; name the elements that must not change.
- apply (DS): Write each note as one moment (phase, time or frame, viewer), one symptom, the probable cause (layer and property), one change (from and to, or 'raise or lower until <check> passes, record the value'), what the change must protect, and the retest step; highest rank first; 'make it pop' is not a note (DS:vfx-design/references/review.md:62-63, 116-132).
- check: Before/after captures: each note maps to a visible change; the anchor element is unchanged.
- mistake: Changing the identity element to satisfy a general note.
- examples:
  - R13: "more colour", "not spacey enough", "one plant is boring" answered with crystal rocks, debris, more colour and varied plants (R13:806-848, 1031-1035).
- roblox_fit: No change.
- roles: art-director, environment-designer, modeler, reviewer, orchestrator, reference-images
- also: character-design, style-identity
- sources: R13-F32 (R13:806-848, 1031-1035)

### CR-05 Give and solve visual notes as paint-overs on a capture
- principle: The best feedback is a paint-over on a capture of the real work, shown as before and after; and visual problems are solved in 2D before 3D: screenshot, paint over, approve, then change the model.
- why: A visual correction is unambiguous where words are not; a 2D change is "a couple of strokes" while a 3D change means model, UVs and more.
- apply: The reviewer (or the art director) captures the work at the game camera and asks reference-images for a paint-over of that exact capture showing the fix, plus a before/after pair; the maker builds toward the approved paint-over. Environment builds get a paint-over after each major pass.
- check: Feedback includes a marked image, not only text; every 3D change after review traces to an approved paint-over; side-by-side of the result and the paint-over lists the differences in shape, value and light, each closed or consciously rejected.
- mistake: Building from the concept once and never comparing again; exploratory changes directly in 3D.
- examples:
  - R00b: "constant paintovers, jamming on ideas to push the design" (R00b:1803-1813).
  - R03: Tom painted over her sculpt: legs longer, face changed; "does this feel like Caitlyn to you?" (R03:790-817, 826-833).
  - R13: a feedback screenshot painted over with three notes, then applied in 3D (R13:203-219, 826-832).
- roblox_fit: Captures come from Studio MCP `screen_capture` at the game camera.
- roles: art-director, reference-images, modeler, environment-designer, animator, vfx-designer, ui-ux-designer, orchestrator, reviewer
- also: references-ideation, process-iteration
- sources: R00b-F03 (R00b:1803-1813); R03-F35 (R03:790-817, 826-833); R13-F08 (R13:203-219, 826-832)

### CR-06 Notes are direct and visual; the maker drives; conflicts go up
- principle: Give feedback straight, without ego, with a clear vision (often a paint-over). Taking feedback, the maker is the driver: listen to some passengers, not all ("too many cooks"); conflicting notes are not averaged.
- why: Fast honest notes speed iteration; one owner keeps coherence; clear visual notes are actionable.
- apply: Reviews state each problem plainly with evidence and a reference or paint-over; each asset has one maker who decides; conflicting notes go to the art director or owner with the conflict stated; makers fix without defence.
- check: Review notes contain concrete problems with a visual or concrete target, not softened praise or bare opinion; conflicting notes show a recorded decision by one owner.
- mistake: Trying to satisfy every note; softening notes until they say nothing.
- examples:
  - R05: quick huddles: "remove the ego and just focus on the craft" (R05:435-457).
  - R13: you are the driver; give feedback as pen-overs with a clear vision (R13:877-892).
- roblox_fit: No change.
- roles: orchestrator, reviewer, art-director, game-designer, environment-designer, modeler, qa-lead
- also: process-iteration
- sources: R05-F14 (R05:435-457); R13-F34 (R13:877-892)

### CR-07 No grand reveals: show early and often, partner crafts first
- principle: Show work early and often; if something must change, know as soon as possible. Ask partner crafts at the thumbnail or rough stage, when anything can still change.
- why: Late discovery of a wrong direction wastes the most work; early notes are worth far more.
- apply: Agents hand back rough states (proxy renders, first clips, option sheets) for checks before polish; the orchestrator schedules a review right after options exist; partner crafts review each other (the modeler on concept, the art director on renders, the rigger on the model).
- check: The job log shows feedback taken at the option or rough stage, not only at the final.
- mistake: The grand reveal; staying "in your head" and "precious" without other opinions.
- examples:
  - R00a: "avoid grand reveals" (R00a:876-884).
  - R08: two concept artists and a splash artist review each other's stages (R08:478-500, 876-888).
- roblox_fit: No change.
- roles: orchestrator, art-director, modeler, animator, vfx-designer, reference-images, reviewer
- also: process-iteration, cross-craft
- sources: R00a-F25 (R00a:876-884); R08-F19 (R08:478-500, 876-888)

### CR-08 Diagnose by layer; "not happy" may mean "not done"
- principle: Unhappiness mid-work does not mean the work is bad; it may not be done. When it fails, ask why by layer (composition, drawing or form, value, colour, shape, flow, detail), fix one layer at a time, and re-check, since a fix can create another problem.
- why: A named cause gives a fix; "it's off" does not.
- apply: Every review note names its layer and one fix; after each fix re-check the other layers; record what a failed image taught.
- check: Every review finding names a layer and a fix; after a fix, a full re-check is logged.
- mistake: Abandoning or polishing without knowing what fails.
- examples:
  - R10: the questions he asks himself during a piece (R10:579-597, 883-901).
- roblox_fit: No change.
- roles: art-director, reviewer, marketing, modeler, environment-designer, orchestrator, qa-lead
- also: visual-hierarchy, process-iteration
- sources: R10-F21 (R10:579-597, 883-901)

### CR-09 Fresh eyes: flip the image, change the reviewer
- principle: The eye adapts to errors in an image it has looked at too long. Mirror the image often to see it new, and after long work hand it to another maker or reviewer.
- why: A sudden change resets the eye; fatigue and familiarity hide problems.
- apply: Every self-review of an image or render also views a horizontally mirrored copy (a one-line flip in Python) and a grayscale copy; for long art tasks the orchestrator schedules a second agent's pass instead of more passes by the same agent [inference].
- check: Original versus mirror: eye lines, shoulder lines and verticals stay level and nothing looks lopsided only in the mirror; long jobs show a second agent's pass.
- mistake: Long looks at the same image; poor symmetry that slants.
- examples:
  - R11: he flips constantly; rotating the canvas works too but is slower (R11:164-178).
  - R09: another artist "has a crack at it" and it comes back better (R09:750-753).
- roblox_fit: Same for UI mocks and thumbnails.
- roles: art-director, reviewer, modeler, reference-images, ui-ux-designer, marketing, orchestrator, qa-lead
- also: value-contrast, process-iteration
- sources: R11-F13 (R11:164-178); R09-F40 (R09:750-753)

### CR-10 Keep the right mistakes: follow a happy misread
- principle: Try things and make mistakes; "real art is knowing which mistakes to keep". When a rough shape reads as something else that also works (zombies reading as graves), consider changing the plan to use the read.
- why: The viewer's first read is the truth; exploring reveals accidents a single plan never finds.
- apply: In review, write what each main shape reads as at first glance; adopt a good misread, fix a bad one; name any accident worth keeping from rejected options.
- check: A cold read of the capture lists what each main shape looks like, compared with intent; review notes record what was kept from rejected options.
- mistake: Forcing a shape to mean what it does not read as [inference].
- examples:
  - R05: foreground zombies read as graves, so the foreground became a graveyard (R05:489-493, 524-527).
  - R00d: "real art is knowing which mistakes to keep" (R00d:5089-5103).
- roblox_fit: No change.
- roles: art-director, environment-designer, ui-ux-designer, reference-images, reviewer
- also: references-ideation, shape-silhouette
- sources: R05-F17 (R05:489-493, 524-527); R00d-F20 (R00d:5089-5103)

### CR-11 The project's needs come first; the lead curates the best solution
- principle: Feedback comes from people solving other problems; the maker's job is to meet all those needs ("looking good is the cherry on top"). Painful feedback often signals a gap in shared goals. The best designers are not those with the best ideas but those who curate the best solution from everyone into one cohesive experience.
- why: Art that ignores the project's goals has no use; cohesion matters more than idea ownership.
- apply: Briefs state the job of the asset; hand-backs map each feedback item to done or questioned (with the reason). The lead collects proposals from all crafts, chooses by fit to the target experience and records where each idea came from.
- check: The hand-back maps every feedback item; the decision record lists options considered, their sources and why one won.
- mistake: Makers who cannot take feedback openly (R10:660-664); "the best designers are the ones that always have the best ideas" (R00d:5791-5793).
- examples:
  - R10: team work versus art for yourself; state goals openly to reduce friction (R10:644-676, 722-750, 793-805).
  - R00d: nearly every ability in the speaker's champion kits came from somebody else (R00d:5787-5825).
- roblox_fit: No change.
- roles: orchestrator, reviewer, art-director, marketing, game-designer, qa-lead
- also: cross-craft, game-design-fun
- sources: R10-F22 (R10:644-676, 722-750, 793-805); R00d-F34 (R00d:5787-5825)

### CR-12 When every option meets the brief, choose and commit
- principle: Use the brief as the filter: most of the choice is objective; if every option passes, the rest is taste ("95% is pretty objective"). Choose a direction and stop.
- why: Without a decision rule polishing has no end, and finals get reopened.
- apply: Reviews score options against the brief first; only passing options go to the choice; ties go to the owner with a recommendation; then commit and polish one.
- check: Each option has a brief-pass yes or no; the pick is recorded and not reopened without a new reason.
- mistake: Pushing forever; reopening a final the next day (R05:832, 848-850).
- examples:
  - R05: "95% is pretty objective", 5 % the artist's aesthetic (R05:830-846).
- roblox_fit: No change.
- roles: orchestrator, art-director, reviewer, marketing
- also: process-iteration, references-ideation
- sources: R05-F35 (R05:830-846)

### CR-13 Close with an honest recap of your own result
- principle: Close every piece with an honest recap: what worked, what is too tame, what is too big, what needs another iteration.
- why: It guides the next pass and keeps the owner's view accurate.
- apply: Hand-backs list strengths, named weaknesses and the next iteration [inference].
- check: The hand-back contains at least one named weakness with a proposed next step, or says why there is none.
- mistake: Reporting only what worked [inference].
- examples:
  - R09: "I probably kept it a little tame"; the site "probably too big"; "a lot of dead space in the back" (R09:1116-1141).
- roblox_fit: No change.
- roles: reviewer, game-designer, level-design, orchestrator
- also: process-iteration
- sources: R09-F51 (R09:1116-1141)

### CR-14 Pitch the experience the player will have, with conviction
- principle: Present work as the moment it creates for the player: what they see, hear and feel in play, told with conviction. The presenter is often the team's inspiration.
- why: The team builds the fantasy it understands; a mumbled pitch loses it.
- apply: Hand-backs and owner pitches describe the moment in play (motion, effect, sound), not only the asset list.
- check: The pitch names the player's experience in one or two concrete sentences.
- mistake: "I don't know if you guys dig it or not"; "a guy with, like, wings" (R00a).
- examples:
  - R00a: Darius with a chainsaw axe and a winged jetpack flies up for his ultimate and comes down with a rain of fire, chainsaw grinding (R00a:886-918).
- roblox_fit: No change.
- roles: orchestrator, art-director, marketing, film-director, game-designer
- also: game-design-fun
- sources: R00a-F26 (R00a:886-918)

### CR-15 Start from the player's pain points
- principle: Design is problem solving: play the game, find the pain points, then work out a solution.
- why: A change that answers a real pain is worth more than a restyle.
- apply: Before UI changes and live-ops plans, play-test the current build and list pain points (taps, confusion, missed information) with where each was observed.
- check: Each proposed change names the pain point it fixes and where it was observed.
- mistake: Restyling with no observed problem [inference].
- examples:
  - R00d: "go play a game and find the pain points" (R00d:4987-4999).
- roblox_fit: Use play-test captures and analytics as evidence (`analysis-design`) [inference].
- roles: ui-ux-designer, game-designer, live-ops-designer, reviewer, qa-lead
- also: ui-ux, game-design-fun
- sources: R00d-F18 (R00d:4987-4999)

### CR-16 Calibrate on simple basics in many moods
- principle: Good work stands on strong basics, not complexity. One simple exercise in many variations (heavy ball, light ball, happy ball, sad ball) shows where skill is weak.
- why: Variants isolate one skill at a time.
- apply: Agent calibration and eval briefs use one simple action (bounce, jump, hit, button press, chime) in several weights and moods; prefer a simple piece done well over a complex one done badly.
- check: A reviewer tells each variant apart without labels.
- mistake: "Animating complex things ... just to show other people how good at animating I could be" (R00b).
- examples:
  - R00b: the bouncing ball in many variations (R00b:3364-3390).
- roblox_fit: No change.
- roles: animator, vfx-designer, ui-ux-designer, sound-designer, reviewer
- also: weight-timing, process-iteration
- sources: R00b-F41 (R00b:3364-3390)

### CR-17 Say what each input can prove; end with a could-not-check list
- principle: A review is only as good as its inputs. A config or spec shows values but no read; one screenshot shows one moment (no timing, onsets, sound, repetition or cost); a frame sequence at a known frame rate adds timing; video with audio adds sound and sync; player tests, owner ratings and real-device performance need a test, not a claim. Label every check by what proved it, never report a check as passed when the input cannot show it, and end with what could not be checked.
- why: Passing what was never seen hides the real risk; naming the missing input tells the lead which capture closes it.
- apply: For each review step, note the input it used and label the result (gate-verified, MCP-verified, owner-confirmed, not verified). Close the review with a could-not-check list: the step, the missing input, and the capture or test that would close it. Convert frames to milliseconds only at a known capture rate. Slow playback finds problems but never proves feel: re-check every retime at 1x. Before/after comparisons share camera, seed and competing effects, or they are "not verified". Every coverage, brightness or timing number names device, resolution, quality level, camera distance and frame rate.
- check: Each review line names its input and label; the review ends with a could-not-check list (or says why it is empty); no timing claim rests on a single screenshot; before/after pairs share camera and seed.
- mistake: "Timing looks good" from a still; "performance is fine" from the Studio emulator; a before/after pair taken from different cameras.
- examples:
  - DS: a table of what config, one screenshot, a frame sequence and video can and cannot check (DS:vfx-design/references/review.md:13-22).
- roblox_fit: Studio MCP captures are frames, not video with sound; sound sync and device latency stay "not verified" unless captured on the target device [inference].
- roles: reviewer, qa-lead, art-director, vfx-designer, animator, sound-designer, ui-ux-designer, environment-designer, level-design, orchestrator
- also: process-iteration, pipeline-production
- sources: DS:vfx-design/references/review.md:13-22, 32, 49-54, 60-61, 67, 73; DS:vfx-design/references/scene-and-clutter.md:107; DS:level-design/SKILL.md:77
