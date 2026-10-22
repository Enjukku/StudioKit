> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit reference: universal. J008. Facts: `knowledge/reference/environment/fact-check-audio.md` (**AU** rows, "Streaming-safe ambience"), `fact-check-lighting.md` (LF32-LF39 wind and particles). Design rules: `environment-design/references/ambience.md`. Docs paths are relative to `knowledge/external/roblox-creator-docs/`. The sound designer builds the sound; this file is how the environment designer puts the ambience map into the place so the sound and VFX designers can build on it. Revised by J018 maker environment-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (step 6: the footstep material list).

# Putting the ambience map into the place

## 1. Place conventions (the scene audit tool reads these; keep them exact)
| Thing | Convention |
| --- | --- |
| Zone volume | an anchored, non-colliding, invisible BasePart (CanCollide, CanTouch, CanQuery false; Transparency 1) tagged **`AmbienceZone`** with string attribute **`ZoneId`** = the map zone id |
| Source anchor | an Attachment or part at the visible cause, with string attribute **`AmbienceId`** = the map §C id. Audio and effect objects at or under it belong to that id |
| Play area | an optional BasePart tagged **`PlayArea`** covering the playable bounds (lets the audit find parts outside it) |
| Ids | never renamed; the same id in the map, the place, the sound designer's cue cards and the VFX specs |
| Data, not code | zones and anchors are data. The runtime that blends zones is written once per game by a code role (J008-D4); the environment designer never writes it |

## 2. Roblox audio facts the placement depends on
| Fact | Source |
| --- | --- |
| New work uses the audio object graph: AudioPlayer (the stream) → Wire → AudioEmitter (puts it in the world) → AudioListener (hears it) → AudioDeviceOutput | AU01-AU03 |
| An AudioEmitter needs a position: an Attachment, Camera or PVInstance parent, or PositionType Instance with a PositionInstance. Without one it is silent | `_api-reference/classes/AudioEmitter.yaml:10-17, 196-232` |
| Distance attenuation: mode Custom by default; a custom curve holds up to 400 points with gains 0-1 (distance and angle curves alike); with no curve the emitter uses inverse-square with no end distance; presets Custom, InverseTapered, Linear, LinearSquared, Inverse use DistanceAttenuationBounds (default 4-10000; unit not stated on the page); a preset ignores the stored curve | AU05-AU11; `AudioEmitter.yaml:176-181` |
| AudioFader and AudioPlayer Volume range 0-10 | `AudioFader.yaml:44-47` (AU12) |
| Acoustic simulation (occlusion, diffraction, reverb) is released (2026-09-22) but **off by default**: switch on `SoundService.AcousticSimulationEnabled`; emitters and listeners default to on. Quality can drop on weak devices. Legacy Sound instances are not supported. `SimulationFidelity` is deprecated | AU15-AU19 |
| `SoundService.AmbientReverb` affects only legacy Sound; the graph uses AudioReverb. `DefaultListenerLocation` cannot be set by scripts (PluginSecurity): set it in Studio, or create the AudioListener yourself | AU19-AU21 |
| Region tests: GetPartBoundsInBox / GetPartBoundsInRadius test bounding boxes; GetPartsInPart tests the real occupied shape; Region3 methods are deprecated | AU24-AU25; PI57 |
| Workspace.GlobalWind drives terrain grass, dynamic clouds and particles; a ParticleEmitter follows it only with WindAffectsDrag on and Drag > 0; Fire and Smoke follow by default; Reduce Motion slows grass, keeps direction | LF32-LF34 |
| Particle caps per emitter: 400/s (100/s on mobile); Lifetime capped at 20 s; LightEmission 1 is additive blending and does not light the scene; flipbooks may switch off on low memory. Caps, not budgets | LF35-LF39 |

## 3. Streaming-safe sources (docs facts, then the studio's method)
- Audio parented to an ordinary streamable part **stops at stream-out**. The docs name persistent models and non-streaming containers as the fix (`workspace/streaming/techniques.md:382`).
- Safe homes: a non-spatial bed in SoundService (outside Workspace, so streaming does not touch it; only for sound with no direction: a waterfall or fire put there is heard everywhere and points nowhere); a small Persistent Model for the few must-hear sources (memory cost: keep them few); a source inside StreamingMinRadius of everywhere the player can stand (`workspace/streaming/index.md:30, 70, 234-240`).
- Probably safe, **test first** (inference): a Model with no BasePart descendants as the emitter's parent; a client-created anchor (`index.md:72-76`).
- Not documented: whether a server-owned AudioPlayer resumes on stream-in; whether PositionInstance re-resolves. So the studio's method (inference, for the code role's runtime): shared state (zone, weather, time) server-owned and replicated; a client controller creates each zone's player, wire and emitter once on instance-added and destroys them on instance-removed; test leave → return → leave.
- The environment designer records per source in map §F: its anchor and keep / rebuild rule.

## 4. Steps in Studio (through the Studio MCP, Edit context, test place)
1. Read the approved map; take positions and bounds from the blockout coordinates (never guessed).
2. Create zone volumes and source anchors with the conventions in §1 (`execute_luau`, datamodel_type Edit). One bounded change per call; read back what was created; never repeat a call blindly after an uncertain result (H10 method).
3. Set any acoustic choice the map records (SoundService gate) and the listener location; note what scripts cannot set.
4. Run the scene audit (`environment-craft` §audit): every map id in the place, nothing unlisted, no duplicates.
5. Capture the source close-up and the player's view for each source (cause visible).
6. Hand off: brief the sound designer and the VFX designer from the map (`rules/messages.md` format); their keys in the map are theirs. Send the sound designer the list of walkable materials in the place (`measure-captures.md` M8) so every floor has a footstep entry, and the VFX designer the sight lines and the route that ambient motion must stay away from.
7. When their work is in: walk the borders in play mode (approach, cross, walk back, stand still, teleport, respawn, stream out and in) and record each state. The listening judgment is theirs or the owner's.
