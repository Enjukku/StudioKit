---
type: job
scope: universal
status: active
updated: 2026-10-23
source: owner chat 2026-10-23 (after J019)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-23

# Job card: J020-sound-workbench — the sound workflow and an in-house AI audio editor

## The owner's words (verbatim, first)
> in terms of the sound designer, I would like it to be able to alter audio so it fits perfectly into my games.

> If you want really good sound design, you often need to edit those sounds. My concern is AI does not know what the sound actually sounds like. So how would it understand how it should edit it? I don't know if we should even edit it in the first place. And then the other thing is there a software that properly allows us to do so and if there isn't, should we make one?

> If we do this, it needs to be really good. [...] We want to generate the sound in 11 labs and then alter it for our game. [...] I can do all the other softwares, FMMPEG, Librosa, Pedalboard, and we obviously have 11 labs.

> I really do think we should just create some sort of in-house AI audio editor. [...] you could literally make it specifically for you, because I won't be touching the audio editor at all.

> I want to make sure that we're not doing any audio editing inside of Roblox. I think that just it just comes out not as good as you would imagine. And I'm not really sure what we're doing for the Great Wall Sims audio tools. [...] I want you to fully get an understanding of what we should do and then I will review the workflow to see if it fits with what I believe it should be like.

| Field | Value |
| --- | --- |
| Job id | J020-sound-workbench |
| Title | The sound workflow and an in-house AI audio editor |
| Size | L (a new kit tool + the sound designer's books; new workflow) |
| Type (recipe) | other: kit tool and agent upgrade (`build-agent` shape), no game |
| Job lead (agent) | lead (orchestrator) |
| Direction leads | sound-designer (craft), architect (tool shape) |
| Integrator | lead |
| Studio place (`studio_id`) | none |
| Code file owners | set when the tool design is approved |
| Linked jobs | J019 G3-P11 (sound designer tools), J018-D7 |
| Risks (review slots) | none of the game tokens; tool risk: wrong numbers that look right (J018 lesson) |
| Status | stage 0: understanding pass, then the workflow map for the owner's review |

## Four lines (goal)
| Line | Value |
| --- | --- |
| Problem | Generated ElevenLabs sounds often do not fit the game (late start, lost on phone speakers, wrong length or notes); the AI cannot hear, and no tool lets an agent alter audio by measurement |
| Constraints | ElevenLabs is the only source; all editing happens on the files, never inside Roblox (owner J020-D1); the owner does not use the editor; Claude cannot hear, so every claim is a measurement or an owner play-test; ffmpeg approved |
| Target experience | sounds that fit each game exactly, judged by the owner in play-tests |
| Success test | the owner reviews the workflow map and says it fits how sound should be made (G1); later, sounds edited by the tool pass the owner's play-test |
| Goal word | fit |

## Stages
| # | Stage | Gate |
| --- | --- | --- |
| 0 | Understanding pass: read the sound designer role and books, the kit audio tool, GreatWallSim's audio tools (run them), its audio plan, reviews and the owner's sound decisions; the ElevenLabs guide when it arrives | — |
| 1 | Workflow map: how a sound goes from idea to game, who does each step with which tool, where the gaps are; an assessment of GreatWallSim's tools | **G1** the owner reviews the workflow |
| 2 | Editor design and build, then the books' editing craft (after G1) | G3 |

## Decisions
`decisions.md` in this folder.
