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
| J020-D9 | 2026-10-23 | Takes per prompt round: minor 3, frequent 4 (kept as a variant set), important 6; at most 3 rounds (J020-D7); layers of important sounds generated separately; good unpicked takes kept in the game's library. Replaces J020-LD1 | "All right, this is number seem reasonable." |
| J020-D10 | 2026-10-23 | Exception to J020-D1: fitting a sound to the space it plays in (cave, hall, outside) is done in Roblox, so one uploaded file serves every space; no per-space copies. Everything else stays baked into the file. Replaces J020-LD2 | "I don't want to upload, multiple of the same sound for specifically because it is in a space. [...] This is one of those use cases where I actually do think the in-house Roblox studio editor is useful. It's for altering the sound to fit the space without having to re-upload the same sound." |
| J020-D11 | 2026-10-23 | Ducking (lowering other sounds while an important one plays) is decided by the sound designer for each moment, not by a fixed rule; each cue card says whether it ducks, what, how much and why | "ducking is a useful mechanic. In many situations, but it's very situational. So that's something we're gonna the AI should decide in said moment" |
| J020-D12 | 2026-10-23 | The 2D-or-3D rule must cover the many cases where 3D is right, including sounds from players that every player should hear and judge by distance (other players' footsteps) | "3D sounds can also, come from, players, things that we want. All players to, hear and, make sense of distance. Even 3D for certain footsteps from other players [...] the two D or 3D rule, I think it's not complete enough. There's a lot of use cases where you want 3D sound versus 2D sound." |
| J020-D13 | 2026-10-23 | **G1 passed:** the sound workflow (`workflow-map.md` and `research-2d-3d.md` at commit `b7f85f5`) is approved; the editor design starts. The owner will send the ElevenLabs prompting guide | "Yes, you understand it. G1 passes; begin the editor design. I'll send the ElevenLabs guide." |
| J020-D14 | 2026-10-23 | Build the editor in the design's order and keep fixing what reviews find; the owner's ElevenLabs key file is registered in the kit's `keys.json` for J020 testing (path only; it expires in about a month) | "Yeah, you can go ahead and build and continue fixing or whatever. And then this is now just going to become, like, I think this key maybe expires in like 1 month or something. So you can go ahead and use this for testing as well." |

## Lead decisions
| ID | Decision | Why |
| --- | --- | --- |
| J020-LD1 | **Superseded by J020-D9.** Takes per prompt round by cue type: minor cue 1, frequent cue 2, hero or signature cue 3; never the book's "4 takes per texture" (S-123, a proposal). Checked against the owner's ElevenLabs guide when it arrives | Credits, not tokens, pay for takes: GreatWallSim measured about 11 credits per generated second (audio plan §11). Ranking by numbers makes more takes unnecessary; the regenerate rounds (J020-D7) fix a miss |
| J020-LD2 | **Superseded by J020-D10.** Room sound: every file carries its designed tail; a separate file per space type only for sounds the player hears in clearly different spaces (footsteps, voice), named on the cue card | The owner left question 2 to the lead; J020-D1 removes Roblox reverb, so the room must be in the file, but only where it matters |
| J020-LD3 | The books' listening check-ins A, B and C (the agent asking the owner to listen at three points) are replaced by the owner's play-tests; "done" = measured and proven to play on its event | Implements GreatWallSim D-064 and J020-D3; the owner did not know the check-ins existed |
| J020-LD4 | Music and ambience duck under important sounds by a volume change (AudioFader) from a script, not by a compressor effect in Roblox | J020-D1; a volume change is playback (J020-D8) |
| J020-LD5 | The 2D-or-3D rule in `workflow-map.md` §6 goes into the workflow: every cue card names 2D or 3D with the reason, and for 3D the falloff mode, range and listener; Roblox's acoustic simulation is tried as a second route for J020-D10 in the first real game, not used by default | The owner asked that the workflow know when a sound is 2D or 3D from the Roblox docs (2026-10-23); acoustic simulation works only on 3D sounds and its quality is not checked yet |
| J020-LD6 | Space fitting (J020-D10) uses one `AudioReverb` per space type on the sound-effect bus, its settings switched by a script when the player enters a space; music and UI bypass it. The engine's acoustic simulation is a Studio probe in the first real game | The docs allow many audio players through one effect; a zone switch is predictable and also covers 2D sounds such as the player's own footsteps |

## Closed doors
| ID | Closed option | Why | May return only if |
| --- | --- | --- | --- |
| CD-1 | Tuning sounds with Roblox audio effects (EQ, compression, pitch, distortion, ...); the room reverb is the one exception (J020-D10) | J020-D1 | the owner asks for it |
| CD-2 | Reference sounds as targets | J020-D3 | the owner asks for it |
| CD-3 | CLAP text-to-audio scoring | J020-D3 | the owner asks for it |
| CD-4 | Building on or editing GreatWallSim's audio tools | J020-D5, J020-D6 | the owner asks for it |
