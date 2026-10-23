---
type: decision
scope: universal
status: active
updated: 2026-10-23
source: owner chat 2026-10-23 (J020)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-23

# J020 decisions (owner's words)

| ID | Date | Decision | Owner's words |
| --- | --- | --- | --- |
| J020-D1 | 2026-10-23 | No audio editing inside Roblox: every alteration (EQ, reverb, pitch, compression, layering) is made on the files before upload; the Roblox audio graph only plays and places the sounds | "I want to make sure that we're not doing any audio editing inside of Roblox. I think that just it just comes out not as good as you would imagine." |
| J020-D2 | 2026-10-23 | The kit gets an in-house audio editor made for the agent (the owner never uses it); ffmpeg is approved | "I really do think we should just create some sort of in-house AI audio editor. [...] you could literally make it specifically for you, because I won't be touching the audio editor at all." |
| J020-D3 | 2026-10-23 | No reference-sound library, no CLAP model, no listening batches: the owner judges sounds in play-tests (as GreatWallSim D-064) | "I think reference sounds are not necessarily a good indicator of a good sound." / "I don't know about this ten-minute per batch whatnot. I'm not sure about this clap thing." |
| J020-D4 | 2026-10-23 | Understanding first: the lead reads the whole sound side and writes the workflow; the owner reviews it before any build | "I want you to fully get an understanding of what we should do and then I will review the workflow to see if it fits with what I believe it should be like." |
| J020-D5 | 2026-10-23 | The kit editor is built new for this workflow; GreatWallSim's audio tools are only a reference for what they do well; the editor covers every part of editing the workflow needs | "I don't think we should build off of the Great Wall Sims audio tools. [...] You could kind of maybe use it as reference for what it does well. But I do think it is just better to create our own. And then we should cover all the parts of editing that we need to." |
| J020-D6 | 2026-10-23 | GreatWallSim keeps its current audio tools unchanged; J020 builds the base kit only | "Just keep the Great Wall Sims current tools. We're not going to edit that. Right now, we're just trying to make our base studio kit." |
| J020-D7 | 2026-10-23 | At most 3 regenerate rounds per cue, then it goes to the owner with its numbers | "For 3 regenerated rounds per queue, is the right limit. Okay" |
| J020-D8 | 2026-10-23 | In Roblox, sounds are only played and placed: volume, and for the few sounds that come from a place (ambience near a waterfall) 3D with a falloff range set per sound; most sounds are 2D. The sound books must explain how this works, from the Roblox docs | "There's some sounds that travel in 3D space, and you can change the range at which it falls off. [...] for some sounds, it is useful to have 3D volume or whatever. But most cases, it probably won't be like that. [...] this might be good for ambient noises near a waterfall." / "this seems like you also need to study the Roblox documentation in terms of sound. And also, I mean, our sound doc should kind of say how this works." |

## Lead decisions
| ID | Decision | Why |
| --- | --- | --- |
| J020-LD1 | Takes per prompt round by cue type: minor cue 1, frequent cue 2, hero or signature cue 3; never the book's "4 takes per texture" (S-123, a proposal). Checked against the owner's ElevenLabs guide when it arrives | Credits, not tokens, pay for takes: GreatWallSim measured about 11 credits per generated second (audio plan §11). Ranking by numbers makes more takes unnecessary; the regenerate rounds (J020-D7) fix a miss |
| J020-LD2 | Room sound: every file carries its designed tail; a separate file per space type only for sounds the player hears in clearly different spaces (footsteps, voice), named on the cue card | The owner left question 2 to the lead; J020-D1 removes Roblox reverb, so the room must be in the file, but only where it matters |
| J020-LD3 | The books' listening check-ins A, B and C (the agent asking the owner to listen at three points) are replaced by the owner's play-tests; "done" = measured and proven to play on its event | Implements GreatWallSim D-064 and J020-D3; the owner did not know the check-ins existed |
| J020-LD4 | Music and ambience duck under important sounds by a volume change (AudioFader) from a script, not by a compressor effect in Roblox | J020-D1; a volume change is playback (J020-D8) |
| J020-LD5 | The 2D-or-3D rule in `workflow-map.md` §6 goes into the workflow: every cue card names 2D or 3D with the reason, and for 3D the falloff mode, range and listener; Roblox's acoustic simulation (`AcousticSimulationEnabled`: muffling through walls, bending round corners, echo) stays off | The owner asked that the workflow know when a sound is 2D or 3D from the Roblox docs (2026-10-23); acoustic simulation is processing inside Roblox (J020-D1) |

## Closed doors
| ID | Closed option | Why | May return only if |
| --- | --- | --- | --- |
| CD-1 | Tuning sounds with Roblox audio effects (AudioEqualizer, AudioReverb, ...) | J020-D1 | the owner asks for it |
| CD-2 | Reference sounds as targets | J020-D3 | the owner asks for it |
| CD-3 | CLAP text-to-audio scoring | J020-D3 | the owner asks for it |
| CD-4 | Building on or editing GreatWallSim's audio tools | J020-D5, J020-D6 | the owner asks for it |
