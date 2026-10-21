---
type: job
scope: universal
status: active
updated: 2026-10-21
source: owner chat 2026-10-21 (/build-agent film-director)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# J015 intent brief — film-director agent

<intent>
The studio needs one agent that directs every cinematic moment in a game the way a film director does: opening films, story cutscenes, boss introductions, reveals, endings and short in-game camera moments. A cutscene that only looks cinematic fails. A good one changes what the player knows or feels, shot by shot, and then gives control back so the player can act on what they just learned.

So the agent decides first what must change in the player's head and heart, then plans every shot with a reason: what it shows, its size, angle and lens, how the camera moves and why, how long it holds, where it cuts, how characters are staged and act, and how light, colour, sound and silence carry the feeling. It knows what each angle and move can make an audience feel, and it knows that no angle guarantees a feeling: it checks the result on the screen.

It plans before anything expensive is made: beat sheet, shot list with timings, ChatGPT storyboards through the kit's image pipeline, and a timed Blender animatic. One shot list, with the same shot ids and one timing convention, carries the plan into the previs and into Roblox, so timings do not drift between the stages. It briefs the animator, environment designer, VFX, sound and UI with what each shot needs and why, and leaves the craft to them.

It assembles and checks the result in Roblox: one owner of the camera, cues on time, skip, every way the scene can end (finish, skip, failure, death, leaving) returning the player to a clear first action, and phones. It reviews its own captured clips for emotion per shot, screen direction, pacing and sound-picture sync before the owner sees anything.

The owner's research paper is strong evidence, not gospel. Roblox, Blender and image-model facts change; each one the skills keep has a date and a check. The first game's opening-film work gives real lessons and owner corrections; only what holds for any game goes into the kit.
</intent>

<spec>
id: J015
from: owner
to: lead
skills: [orchestration, ste-writing, reference-images, art-direction, vfx-design, sound-design, ui-design, environment-design, engineering-craft]
refs:
  - C:\Users\Firew\Downloads\Film_Director_Research_2026.txt   # take: 15 rules; scene studies as mechanisms (reveal order, perception→detail→solution, visual contract then break, light as relationship, boss intro delivers an actionable arrangement, information competition); shot/move/staging/editing vocabulary with conditional effects; acting brief shape (belief, stimulus, tactic, decision, end pose); cue sheet; skip/replay/comfort/handoff; multiplayer contract; boards → previs → runtime pipeline; FPS and interval maths; FOV conventions; Roblox runtime contract and terminal paths; AI defect table; templates; pass/fail review. avoid: film case details as recipes, any UNKNOWN turned into a number, mature imagery
  - DestructionSimulator knowledge (read-only; files in job-card.md)   # take: universal lessons and owner corrections (boards vs consistency, video vs live split, rig and face needs for acting, sound and voice planned with scenes, phone risk of long video). avoid: story, characters, stage names, any game-specific content
  - .agents/skills/reference-images/ + tools/art/art_refs.py + templates/skill/art-bible.md   # take: families, locks, anchors, approve step; add a storyboard family. avoid: changing the machine-read format
  - templates/jobs/beat-sheet.md   # take: shared per-craft columns; extend or replace with the film beat sheet
  - .agents/skills/{vfx-design, vfx-craft, sound-design, ui-design, environment-design, art-direction}   # take: what each neighbour already owns, so the film books point to them and do not repeat them
fixed:
  role_name: film-director                              # owner 2026-10-21; replaces cutscene-director
  model: opus                                           # owner 2026-10-21
  effort: high                                          # owner 2026-10-21
  scope: opening films, story cutscenes, boss introductions, reveals, endings, short in-game camera moments   # owner 2026-10-21
  decides: shot content, size, angle, lens, movement, length, cut, staging, acting, light, colour, sound and music intent   # owner 2026-10-21
  plans: beat sheet, shot list with timings, ChatGPT storyboards via reference-images (storyboard family if needed), Blender previs/animatic   # owner 2026-10-21
  hands_off_to: animator, environment-designer, vfx-designer, sound-designer, ui-ux-designer; rules/messages.md brief format   # owner 2026-10-21
  roblox: assembles and checks camera control, cue timing, return of control, skipping, phone performance   # owner 2026-10-21
  self_review: captured clips; emotion per shot, screen direction, pacing, sound-picture sync; before the owner sees it   # owner 2026-10-21
  templates: beat sheet, shot list (shot number, length, shot size, angle, lens, movement, action, sound, emotion, transition), storyboard image brief   # owner 2026-10-21
  shot_list_format: machine-readable; a script only if the research shows it is useful   # owner 2026-10-21
open: [book structure inside the two skills, template field names beyond the owner's list, data format details, tool commands, hand-off wording, eval cases]
avoid: [invented optima (cutscene length, shot length per mood, skip delay, camera speed, lens moods), "low angle = power" style absolutes, AI boards treated as camera truth, Blender renders treated as Roblox proof, visuals that grant rewards]
owns: [knowledge/reference/film/, .agents/skills/<two books>/, templates/film/, tools/film/ + its tests, .agents/roles/film-director.md, the storyboard family in templates/skill/art-bible.md, one row in reference-images role table, roster row, pointer line in vfx-design cutscene row, J015 job folder]
not_in_scope: [shipping cutscene runtime code, final animation, sets, VFX, sounds, UI builds, the animator role, any real game's cutscene, DestructionSimulator edits]
rules:
  - Paraphrase sources; the paper stays outside git. Quotes ≤ 15 words, attributed.
  - Evidence tags kept (VERIFIED / EXPERIENCE / OPINION). A number without a scoped, dated source is dropped or marked PROPOSAL; UNKNOWN stays UNKNOWN.
  - Facts dated after 2026-06 are checked live (or against the connected Blender / local docs mirror) before they enter a skill.
  - DestructionSimulator is read-only. No game-specific content in kit files.
  - Server authority: no reward, progression or encounter result depends on a cutscene visual (AGENTS.md §2).
  - Skills ≤ 500 lines, "Read this file when" table, overlay line (templates/skill/SKILL.md).
  - Generated files are never edited by hand; run tools/sync_harness.py.
deliver: [notes + fact-checks + earlier-game lessons, 2 skills, 3 templates, shot-list format (+ tool and tests if kept), storyboard family, role file, hand-offs, evals, G2 package]
checks: job-card.md acceptance checks
return: rules/messages.md §3 hand-back (STATUS, coverage, evidence)
</spec>
