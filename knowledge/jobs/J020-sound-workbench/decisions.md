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

## Closed doors
| ID | Closed option | Why | May return only if |
| --- | --- | --- | --- |
| CD-1 | Tuning sounds with Roblox audio effects (AudioEqualizer, AudioReverb, ...) | J020-D1 | the owner asks for it |
| CD-2 | Reference sounds as targets | J020-D3 | the owner asks for it |
| CD-3 | CLAP text-to-audio scoring | J020-D3 | the owner asks for it |
