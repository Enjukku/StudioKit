---
type: reference
scope: universal
status: draft
updated: 2026-10-23
source: J020 web research 2026-10-23 (owner request)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-23

# Which sounds are 2D and which are 3D: research for the owner's review

The owner asked for a quick web research pass before the 2D/3D rule goes into the workflow (2026-10-23). Sources are at the end. Strength labels: **docs** = an engine or middleware vendor's own documentation; **practice** = developer forums and guides (useful patterns, not authority); **lead** = my reasoning from the sources.

## 1. What the sources agree on
| # | Finding | Strength | Source |
| --- | --- | --- | --- |
| 1 | A 2D sound is "not located in a three-dimensional space"; it does not change with the player's position or facing | docs | CRI ADX guide #8; Roblox `audio/objects.md`; Unity wiki |
| 2 | 2D is "usually used for non-diegetic sounds such as music, narration, or UI, as these elements are not linked to actual objects in the game world" | docs | CRI ADX guide #8 |
| 3 | Background ambience beds "are also often set to 2D because they don't necessarily need to change based on the player's position" | docs | CRI ADX guide #8 |
| 4 | A 3D sound has a position; its volume falls with the distance between the listener and the emitter, between a minimum and a maximum distance; an angle setting can make it directional | docs | CRI ADX guide #8; Roblox `AudioEmitter` |
| 5 | 3D suits sounds from things in the world: "car horns, campfires, and gunshots"; music stays 2D because it should not depend on where the player is | docs | Unity wiki ("How Audio Works") |
| 6 | Moving 3D sources often get a Doppler pitch change | docs | CRI ADX guide #8 (Roblox's graph has no Doppler: the kit book SC-10) |
| 7 | Music score is not expected to change with position or room; spreading it in space can make players mistake it for a sound in the world | practice | Shockwave-Sound article |
| 8 | Sorting by "in the world or not" is not enough: what a sound does for the player matters | practice (peer-reviewed) | Jørgensen, *Time for New Terminology?* |

## 2. The hard cases
| Case | What the sources say | Strength |
| --- | --- | --- |
| **The player's own footsteps and body sounds** | 3D footsteps on your own character can pan badly left and right, worse when the character leans. Unreal's fix is a "non-spatialized radius": close sounds play centred. A game-audio guide lists player footsteps as unspatialized or only lightly spatialized, while enemy footsteps stay directional | practice (Unreal forum; a skill guide) |
| **Other players' sounds** | Other players hear your footsteps in 3D with volume by distance; each client can play them from the replicated movement | practice (Unity forum; a commercial Unreal footstep system) |
| **Third-person camera: where is the "ear"?** | On the camera, a sound next to the character is still quieter (the camera is far away). On the character, directions can come out wrong. CRI's fix, the "Focus Point": measure **distance from the character** and **direction from the camera**. In cutscenes, take the focus point off the character, because the character may leave the screen | docs (CRI Focus Point) |
| **Roblox's answer** | `SoundService.DefaultListenerLocation = Character` does exactly the CRI split: "the world being heard from the position of your character while matching the orientation of your camera" (an Attachment on the character's PrimaryPart, turned each frame to face where the camera faces) | docs (Roblox `ListenerLocation` enum) |
| **Blends between 2D and 3D** | Unity has a "Spatial Blend" slider from 2D to 3D; Unreal has the non-spatialized radius. Roblox's audio graph has no blend: a sound goes to the output directly (2D) or through an emitter (3D) | docs (Unity wiki), lead (Roblox) |

## 3. What this changes in our rule (`workflow-map.md` §6)
1. **The core test stays, now backed:** 2D for sounds not tied to a thing in the world (UI, music, narration, area beds); 3D for sounds from a thing whose place or distance helps the player.
2. **The actor rule stays, now backed:** the player who acts hears their own body and tool sounds 2D (Roblox has no "close = centred" blend, so 2D is the way to avoid the bad panning); everyone else hears them 3D.
3. **The listener is no longer a guess:** every game uses `DefaultListenerLocation = Character` (distance from the character, direction from the camera). During a cutscene the listener moves to the camera, by script (a Studio probe in the first cutscene).
4. **Music:** 2D; only music that plays from a thing in the world (a radio, a band on a stage) is 3D.
5. **Moving sources:** 3D, emitter on the moving part; no Doppler in Roblox, so a pass-by pitch, if needed, is baked into a one-shot or scripted (kit book SC-10).

## Sources
- [CRI ADX Beginner's Guide #8: Spatialization Basics (2024)](https://blog.criware.com/index.php/2024/05/07/adx2-beginners-guide-8-spatialization-basics)
- [CRI: Focus Point (2022)](https://blog.criware.com/index.php/2022/09/02/focus-point/)
- [Unity wiki: How Audio Works](https://unitywiki.readthedocs.io/en/latest/audio/how_audio_works.html)
- [Unreal forum: Play sounds in 2D locally and in 3D replicated? (2019)](https://forums.unrealengine.com/t/play-sounds-in-2d-locally-and-in-3d-replicated/446337)
- [Audiokinetic Q&A: distance relative to the player, panning relative to the camera](https://www.audiokinetic.com/qa/6112/unity-distance-relative-the-player-panning-relative-camera)
- [Unreal Answers: sounds from the main hero in the centre](https://answers.unrealengine.com/questions/384358/view.html?sort=votes)
- [Unity discussions: audio on a network object plays only locally](https://discussions.unity.com/t/audio-source-on-a-network-object-plays-sound-only-locally/928884)
- [Shockwave-Sound: surround music in video games](https://www.shockwave-sound.com/blog/?p=60)
- [Jørgensen: Time for New Terminology? Diegetic and Non-Diegetic Sounds in Computer Games Revisited](https://bora.uib.no/bora-xmlui/handle/1956/4287)
- Roblox Creator Docs (local mirror, read 2026-10-23): `audio/objects.md`; `_api-reference/enums/ListenerLocation.yaml`; `_api-reference/classes/AudioEmitter.yaml`, `AudioListener.yaml`
