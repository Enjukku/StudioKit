---
type: decision
scope: universal
status: active
updated: 2026-10-21
source: owner chat 2026-10-21
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# J015 decisions

| ID | date | decision | owner's words |
| --- | --- | --- | --- |
| J015-D1 | 2026-10-21 | film-director runs on Opus, high effort | "Model: Opus, high effort." |
| J015-D2 | 2026-10-21 | The film-director role replaces cutscene-director in the roster | "This agent replaces cutscene-director in the roster." |
| J015-D3 | 2026-10-21 | Material: the owner's film-director research paper, checked; Roblox camera and cutscene facts first; unbacked claims dropped | "Use it as strong evidence, but not as gospel. Check claims that matter, especially Roblox camera and cutscene facts, and drop what you cannot back up." |
| J015-D4 | 2026-10-21 | Planning before animation: beat sheet, shot list with timings, ChatGPT storyboards via reference-images (storyboard family added if needed), Blender previs/animatic | "It plans before anything is animated: a beat sheet, a shot list with timings, storyboards made with ChatGPT through the kit's reference-images skill (add a storyboard family to templates/skill/art-bible.md and the skill if needed), and a previs or animatic in Blender." |
| J015-D5 | 2026-10-21 | Templates: beat sheet, shot list (shot number, length, shot size, angle, lens, movement, action, sound, emotion, transition), storyboard image brief; machine-readable shot list, script only if research shows it is useful | "Templates: a beat sheet, a shot list (...) and a storyboard image brief." / "A shot list format a script can read, so the cutscene timings stay the same in the plan, the previs and Roblox. Only build a script if the research shows it is useful." |
| J015-D6 | 2026-10-21 | DestructionSimulator opening-film work is a read-only source; only universal lessons enter the kit | "Keep the lessons that hold for any game, and remove anything specific to that game." |
| J015-D7 | 2026-10-21 | G1 approved (job card + brief). Digest items 2-8 had no explicit answer, so their defaults apply: build `tools/film/shotlist.py` small (check, table, blender, blender-diff, luau) with offline tests, no camera-path export unless G2 needs it; the film director writes scene data + playback contract, not the player code, and a kit cutscene player is proposed as an engineering follow-up (G2 uses a throw-away Studio probe); skills `film-direction` + `film-craft`; ChatGPT boards for intent and composition, Blender previs stills as spatial truth once models exist; Sonnet helpers at high; G2 subject = the paper's 5-shot boss reveal; animator briefs held by the lead until J006 | "You may begin." |
| J015-D8 | 2026-10-21 | The film-director agent is accepted as done. No further testing in J015: G2 items (relight shot E, Roblox playback in a separate Studio, grader run) are not run; mistakes are found and fixed while making real games with the kit | "For now, the agent is just done. We're not going to do any testing right now. We will be doing a lot of testing with this kit in the future, making games. So we'll pick up mistakes and this kit should continue to keep updating and getting better." |
