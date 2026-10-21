---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: J008-T06
supersedes: []
---
> Author: fact-checker · claude-sonnet-5-5 · high · 2026-10-21

# Fact check: audio, acoustic simulation, streaming lifecycle (environment paper)

Scope: every audio and ambience claim the extractors flagged in `02-ambience-life-dressing-terrain.md` section 7 (CK01-CK30, CK43-CK45), `01-place-guidance-scale-light.md` section 9 (FC30-FC33) and `03-pipeline-performance-review.md` (CA01-CA07), plus contradiction X13. Out of scope and skipped: CK31-CK42 (wind drag, particle caps, terrain, Blender: other checkers).

## How I checked

| Item | Value |
| --- | --- |
| Mirror | `knowledge/external/roblox-creator-docs/`, upstream revision 7400643, refreshed 2026-10-20 (`README.md:7-9`). Read 2026-10-21. Paths below are relative to the mirror root. `ref/` = `_api-reference/classes/`, `enum/` = `_api-reference/enums/`. |
| Live web | Read 2026-10-21 through a page-fetch tool that summarizes pages (not a raw browser). Used only where the mirror lacks the page: the DevForum acoustic thread (DF, two separate fetches that agreed), the live SoundService page (code sample, two fetches that agreed), raw upstream `AudioFader.yaml` (GitHub main), and industry sources. Forum posts are not release notes. |
| DF | https://devforum.roblox.com/t/full-release-acoustic-simulation-emit-audio-with-presence/4307121 (staff post by Doctor_Sonar) |
| Verdicts | confirmed (source matches), corrected (source gives a different value), partly (matches with a limit or a missing piece), unverified (not found; I say what I tried), contradicted (source says the opposite). |
| Row ids | AU01-AU44, in the order of the flagged ids. `AF` was not used: the note already uses AF01-AF32 for ambience-map fields. Rows are grouped: 02 note audio (AU01-AU33), 01 note (AU34-AU37), 03 note (AU38-AU44). |

## Summary

| Verdict | Count | Rows |
| --- | --- | --- |
| confirmed | 38 | all others |
| corrected | 1 | AU12 |
| partly | 3 | AU31, AU37, AU42 |
| unverified | 2 | AU33, AU36 |
| contradicted | 0 | none |
| Total rows | 44 | C1: every flagged audio id has one row. Skipped: CK31-CK42 (not audio). |

Corrected, with the right value:

| Row | Claim in the notes | Right value | Source |
| --- | --- | --- | --- |
| AU12 (CK12, AM08, X03) | AudioFader.Volume range is 0-3 | 0-10 ("Ranges from 0 to 10"). The default is not stated on the page. AudioPlayer.Volume is also 0-10. X03's contrast "0-3 versus legacy 0-10" is void: both are 0-10. The "no need above 2" hint stays on the legacy Sound page only. | `ref/AudioFader.yaml:44-47`; raw upstream `AudioFader.yaml` (GitHub main), read 2026-10-21 |

Partly or unverified (act on these):

| Row | What to do |
| --- | --- |
| AU31 (CK43) | Wind through wooden slats, creaking roof and per-mode mix priority are in the interview. "Wet surfaces keep dripping" is narrower there: only drops falling off leaves after rain. "Paper screens" appear as shoji doors that rattle. Reword AM01. |
| AU33 (CK45) | Sea of Thieves page returned HTTP 403; search found no readable text. Do not cite any Sea of Thieves audio claim. |
| AU36 (FC32) | Valve AMA not readable (Reddit blocked). A search snippet says only "numerous Steam Audio improvements". Drop HRTF/DSP/occlusion unless the owner supplies the thread. |
| AU37 (FC33) | Sunken Plaza muffling: unverified (page text not readable). Zelda: the sound staff asked programmers where the surface/sky line is; they did not set it. Esperança recordings: confirmed. "Tsushima" is not among the cited sources C11/C05/C06. |
| AU42 (CA05) | Stream-out stopping audio is documented; "must survive or be rebuilt" is the paper's design rule. The docs name one fix: persistent model or non-streaming container. |

Other findings that change the notes (all documented below):

| Finding | Where |
| --- | --- |
| `SoundService.AcousticSimulationEnabled` is Disabled by default (DF). Emitters and listeners default to enabled (DF). A place that wants acoustic simulation must switch on the SoundService gate. The reference page itself states no default. | AU17 |
| `SimulationFidelity` on emitter and listener is deprecated (it was the Studio Beta control). The control is now the boolean `AcousticSimulationEnabled` on SoundService, emitter and listener. | AU15, AU17 |
| `DefaultListenerLocation` is PluginSecurity for read and write: a script cannot set it at runtime. Set it in Studio, or create the AudioListener by script and set it to None. | AU21 |
| An emitter with no custom curve uses an inverse-square curve (default mode Custom, empty curve). It has no end distance. | AU06, AU10 |
| Distance presets exist: Custom, InverseTapered, Linear, LinearSquared, Inverse. The notes name none of them. | AU07 |
| Streaming: a server-owned AudioPlayer in a streamable part stops on stream-out. The docs do not say whether it resumes on stream-in. | Streaming section |

## Claims

Columns: id, claim (flagged id first), note row and EP line, paper source ID, checked against (read 2026-10-21), what the source says, verdict, note.

### Group 1: 02 note, graph objects and attenuation (CK01-CK14)

| id | claim | note row, EP | paper src | checked against | what the source says | verdict | note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AU01 | CK01: Sound, SoundGroup, SoundEffect are discouraged for new work in favor of audio objects | AM05, EP:270 | A04 | `audio/objects.md:22-24` | An info box says the three legacy classes are discouraged in favor of audio objects. | confirmed | Discouraged, not removed (`ref/SoundService.yaml:11-20` still documents both systems). |
| AU02 | CK02: Graph roles: AudioPlayer stream, Wire connection, AudioEmitter into the world, AudioListener receives, AudioDeviceOutput to the device | AM05, EP:270 | A04 | `audio/objects.md:28-37, 83-90` | Player loads and plays the asset; emitter is a virtual speaker; listener is a virtual microphone; output is real hardware; wire carries streams. | confirmed | Wires can also be placed anywhere; the docs put them next to the objects they link. |
| AU03 | CK03: AudioPlayer wired straight to AudioDeviceOutput is non-spatial | AM05, EP:270; FC31 | A04 | `audio/objects.md:41-47` | 2D audio is a player, a wire and an output. It is non-directional and keeps the same volume wherever the player stands. | confirmed | |
| AU04 | CK04: The standalone 3D demo uses 6 objects; its numbers are 50 and 70 studs | AM05, X08, EP:270, 318 | A04 | `audio/objects.md:75-81, 116-118` | Six objects: player, emitter, listener, output device, two wires. The 50/70 numbers describe the example DistanceAttenuation curve: half volume at 50 studs, zero at 70. | confirmed | The paper did not say which property: it is the emitter's DistanceAttenuation curve. Still a doc example, not a preset. |
| AU05 | CK05: AudioEmitter custom distance curve accepts up to 400 distance/gain pairs | AM06, EP:272 | A05 | `ref/AudioEmitter.yaml:503-506` | "Tables containing up to 400 key-value pairs are supported." | confirmed | Same 400 limit for the angle curve (`ref/AudioEmitter.yaml:454-457`; angle keys 0-180). The text says keys and values are "expected", not enforced. |
| AU06 | CK06: Curve gains lie in [0,1]; linear interpolation; end values held outside the domain | AM06, EP:272 | A05 | `ref/AudioEmitter.yaml:503-519` | Keys unique and >= 0; values 0 to 1; straight lines between points; beyond the end points the curve holds the end value outward without limit. An empty or nil table gives an inverse-square curve. | confirmed | Design point: no custom curve means no end distance. Also `ref/AudioEmitter.yaml:349-365`: GetDistanceAttenuation returns an empty table for the default curve. |
| AU07 | CK07: DistanceAttenuationMode defaults to Custom; presets use DistanceAttenuationBounds, default [4, 10000] | AM06, EP:272 | A05 | `ref/AudioEmitter.yaml:135-152, 167-181`; `enum/DistanceAttenuationMode.yaml:24, 32, 44, 55, 65` | Bounds default to NumberRange [4, 10000]; used only when the mode is not Custom. Mode defaults to Custom. Enum items: Custom (0), InverseTapered (1), Linear (2), LinearSquared (3), Inverse (4). Full volume inside the minimum, silent at or beyond the maximum. | confirmed | The emitter page states no unit for the bounds. The legacy Sound page says studs (`ref/Sound.yaml:533-537`). Treat studs as inference. |
| AU08 | CK08: PositionType default Parent; PositionInstance names another instance when PositionType is Instance | AM06, EP:272 | A05 | `ref/AudioEmitter.yaml:196-232`; `enum/EmitterPositionType.yaml:17-27` | Default Parent. PositionInstance works only with Instance. A nil or position-less instance means the emitter is not heard. | confirmed | |
| AU09 | CK09: GetAudibilityFor reports combined distance and angle attenuation, not final loudness | AM06, EP:272 | A05 | `ref/AudioEmitter.yaml:298-324` | Returns 0 to 1 for a given listener, counting distance and angle attenuation on both emitter and listener. | confirmed | "Both sides" is a detail the paper omits. |
| AU10 | CK10: A preset attenuation mode overrides the stored custom curve (paper's inference) | AM07, EP:274 | A05 | `ref/AudioEmitter.yaml:176-181, 359-365, 499-501` | With any mode other than Custom, the custom curve is ignored. GetDistanceAttenuation still returns the stored curve in any mode. | confirmed | Now documented, not inference. Reading the stored curve does not show what plays. |
| AU11 | CK11: An emitter under a non-positional parent can end up inaudible or unpositioned | AM07, AM19, EP:274, 300 | A05 | `ref/AudioEmitter.yaml:10-17, 209-210` | Parent must be an Attachment, Camera or PVInstance. Otherwise the emitter is "effectively silent". A PositionInstance with no position or nil: not heard. | confirmed | Documented, not just opinion. PVInstance covers BasePart and Model (`ref/PVInstance.yaml:16-19`). |
| AU12 | CK12: AudioFader multiplies stream volume; Volume range 0-3 | AM08, X03, EP:276 | A06 | `ref/AudioFader.yaml:40-48`; raw upstream `AudioFader.yaml` (GitHub main) | "Volume level which is multiplied onto the input stream. Ranges from 0 to 10." | corrected | Right value: 0-10, not 0-3. Multiplication is right. Default not stated. The live reference page, read through the fetch tool, showed no range text; the mirror and upstream source agree on 0-10. See Conflicts C1. |
| AU13 | CK13: AudioFilter exposes FilterType, Frequency, Gain, Q | AM08, EP:276 | A07 | `ref/AudioFilter.yaml:44, 65-71, 86-93, 108-116`; `enum/AudioFilterType.yaml:18-95` | All four exist. Frequency 20-22000; Gain -30 to 30; Q 0.1-10. Types: Peak, LowShelf, HighShelf, Lowpass 6/12/24/48 dB, Highpass 12/24/48 dB, Bandpass, Notch. | confirmed | |
| AU14 | CK14: AudioReverb has decay, delay, dry/wet and filtering controls (key word DecayTime) | AM08, EP:276 | A08 | `ref/AudioReverb.yaml:63-67, 123-129, 144-148, 163-169, 184-189, 268-273` | DecayTime 0.1-20 s; DryLevel and WetLevel -80 to 20; EarlyDelayTime 0-0.3 s; LateDelayTime 0-0.1 s; HighCutFrequency 20-20000; plus DecayRatio, Density, Diffusion, shelf and reference frequency. | confirmed | |

### Group 2: acoustic simulation and SoundService (CK15-CK21)

| id | claim | note row, EP | paper src | checked against | what the source says | verdict | note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AU15 | CK15: Acoustic simulation client beta announced 2026-01-28; full-release update 2026-09-22 | AM09, ES6-4, EP:278, 335 | A09 | DF (live), read 2026-10-21; mirror has no page (searched `audio/`, `releases.md`: no hit) | Original post "January 28, 2026" in Client Beta. In-thread update "September 22, 2026" says it is out of beta. | confirmed | One thread, not two announcements. The thread title says "Full Release" but the January body is a beta description. Studio Beta's SimulationFidelity was replaced by boolean properties (DF); mirror agrees (`ref/AudioEmitter.yaml:247-263`, tag Deprecated). |
| AU16 | CK16: Gives automatic occlusion, diffraction and reverberation via the advanced audio system | AM09, EP:278 | A09 | `ref/SoundService.yaml:31-46`; `ref/AudioEmitter.yaml:29-41` | Occlusion (muffled through walls), diffraction (bends around corners), reverberation (echo off walls); applies to AudioEmitter and AudioListener. | confirmed | Geometry inputs per DF: `BasePart.AudioCanCollide`, `PhysicalProperties.AcousticAbsorption` (reflection), `PhysicalProperties.Density` (occlusion). Mirror: `ref/BasePart.yaml:269`, `datatypes/PhysicalProperties.yaml:182`. |
| AU17 | CK17: SoundService holds the global enable; emitter and listener settings also matter | AM09, EP:278 | A09, A05 | `ref/SoundService.yaml:31-46`; `ref/AudioEmitter.yaml:29-41`; `ref/AudioListener.yaml:27-41`; DF | SoundService false overrides the per-instance settings. Emitter and listener must both be true for the effect. | confirmed | Added: DF says the SoundService property is Disabled by default and the emitter/listener ones default enabled. The reference pages state no defaults. Re-check in the installed Studio. |
| AU18 | CK18: Accuracy may reduce, or features turn off, to hold frame rate | AM09, AM13, EP:278, 286 | A09 | DF | Reverb, occlusion and diffraction "may lower accuracy or turn themselves off" to keep frame rate (part of the quality system). | confirmed | Single source (the forum post). |
| AU19 | CK19: As of 2026-09-22, Sound-instance support is still in development | AM09, X01, EP:278 | A09 | DF | Acoustic simulation requires the Advanced Audio API. Sound-instance support was planned for the full release; the September update says work continues. Not shipped as of the read. | confirmed | Consistent with the mirror: acoustic properties are documented under "advanced audio system" only (`ref/SoundService.yaml:31-35`). Re-check in the installed Studio. |
| AU20 | CK20: SoundService.AmbientReverb applies to Sound only, not AudioPlayer/AudioEmitter graphs | AM10, EP:280 | A10 | `ref/SoundService.yaml:61-77` | It affects Sound instances and "not" the advanced audio system. AudioReverb is the graph tool. | confirmed | |
| AU21 | CK21: SoundService.DefaultListenerLocation (PluginSecurity) is the current name; the overview page still says ListenerLocation | AM10, X02, EP:280 | A10, A04 | `ref/SoundService.yaml:117-141`; `enum/ListenerLocation.yaml:17-70`; `audio/objects.md:96-106`; live SoundService page | Property `DefaultListenerLocation`, type Enum.ListenerLocation, read and write security PluginSecurity. Overview text and steps use "ListenerLocation". Values: Default, None, Character, Camera. | confirmed | Scripts cannot set it at runtime (PluginSecurity): set it in Studio. Default builds a listener only with the default voice and audio-API setup (`enum/ListenerLocation.yaml:17-25`; `audio/objects.md:99`): with None or without voice, create the AudioListener yourself. Camera and Character also make the AudioDeviceOutput and Wire (`enum/ListenerLocation.yaml:33-70`). |

### Group 3: legacy Sound, AudioPlayer, queries (CK22-CK26)

| id | claim | note row, EP | paper src | checked against | what the source says | verdict | note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AU22 | CK22: Sound has RollOffMinDistance, RollOffMaxDistance, RollOffMode; Volume multiplicative 0-10; guide says loud audio likely needs no Volume above 2 | AM11, X03, EP:282 | A17 | `ref/Sound.yaml:533-572, 714-719`; `sound/objects.md:117-120, 133-148`; `enum/RollOffMode.yaml:19-48` | Volume 0-10, default 0.5. Guide: if the source is loud, you likely need not exceed 2, because the property multiplies. Rolloff distances are in studs. Modes: Inverse (default), Linear, LinearSquare, InverseTapered. | confirmed | Default 0.5 and the mode list are extras. |
| AU23 | CK23: AudioPlayer.Asset is current; AssetId deprecated; IsReady exists | AM12, X04, EP:284 | A11 | `ref/AudioPlayer.yaml:21-60, 161-176` | Asset is the property. AssetId is tagged Hidden, NotReplicated, Deprecated, with the message "use Asset". IsReady turns true when loading is done and can turn false under extreme memory pressure. | confirmed | The IsReady drop under memory pressure is an extra: an ambience player may need a re-check. |
| AU24 | CK24: GetPartBoundsInBox / InRadius test bounding boxes; GetPartsInPart tests occupied volume | AM14, EP:290 | A12 | `ref/WorldRoot.yaml:667-690, 718-740, 769-790` | The two Bounds methods test part bounding boxes (efficient, rough). GetPartsInPart uses the exact occupied volume with a full collision check. For simple volumes the docs suggest the bounds methods. | confirmed | |
| AU25 | CK25: Old Region3 query methods are deprecated | AM14, EP:290 | A12 | `ref/WorldRoot.yaml:457-516, 520-541, 548-591, 599-641, 953-1021, 1029-1067` | FindPartsInRegion3, its lowercase alias, the WithIgnoreList and WithWhiteList variants and IsRegion3Empty (both forms) are tagged Deprecated. The message says to use GetPartBoundsInBox with OverlapParams. | confirmed | |
| AU26 | CK26: SoundService's tagged-part dynamic-reverb example omits absolute-value and lower-bound checks | AM14, X05, EP:290 | A10 | Live SoundService page, code sample "Reverb System", read 2026-10-21 (two fetches). The code sample is not in the mirror (`ref/SoundService.yaml:22` only names it). | `positionInPart` converts the point to the part's local space, then checks only that each offset is below the half-size: no `math.abs`, no check against the negative side. | confirmed | Read through a summarizing tool, twice, same result. A point far on the negative side passes. Use the local-space compare in AM15. |

### Group 4: streaming lifecycle (CK27-CK29)

| id | claim | note row, EP | paper src | checked against | what the source says | verdict | note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AU27 | CK27: Audio from a Sound or AudioPlayer stops once the 3D object it is parented to streams out | AM18, EP:298 | A13 | `workspace/streaming/techniques.md:382`; `workspace/streaming/index.md:79` | "stops when that object streams out". Fix named by the docs: put the emitter in a persistent model or non-streaming container. A streamed-out instance is parented to nil. | confirmed | The sentence covers Sound and AudioPlayer. AudioEmitter is not named: an emitter in a streamed-out part loses its position anyway (AU11). |
| AU28 | CK28: Client spatial queries see only streamed-in content; add/remove signals fire for streaming | AM18, EP:298 | A13 | `workspace/streaming/techniques.md:359-361`; `workspace/streaming/index.md:79` | Raycast, GetPartBoundsInBox and GetBoundingBox reflect streamed-in content only. On stream-out, removal signals (ChildRemoved, DescendantRemoving) fire on the parent or ancestor. | confirmed | |
| AU29 | CK29: Persistent models use memory, so keep them few | AM18, EP:298 | A13 | `workspace/streaming/techniques.md:87, 251`; `workspace/streaming/index.md:234-240` | Persistent models load after join, never stream out and permanently use memory. Use them sparingly, for rare cases. "Not intended to circumvent streaming." | confirmed | |

### Group 5: wind, outside audio but flagged as CK30

| id | claim | note row, EP | paper src | checked against | what the source says | verdict | note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AU30 | CK30: Workspace.GlobalWind drives terrain grass and clouds | VL01, EP:339 | P12 | `ref/Workspace.yaml:434-442` | A Vector3 for the direction and strength of wind: terrain grass, dynamic clouds and particles. | confirmed | Only this row checked; CK31-CK32 left to the wind and particle checker. Neither this page nor the paper says audio reads GlobalWind (VL02 is right). |

### Group 6: industry audio claims (CK43-CK45)

| id | claim | note row, EP | paper src | checked against | what the source says | verdict | note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AU31 | CK43: Ghost of Tsushima: wind on slats, roofs, paper screens; residual drips after rain; per-mode mix priority | AM01, EP:260 | A01 | https://www.asoundeffect.com/ghost-of-tsushima-sound/ , read 2026-10-21 | Wind through wooden slats and a creaking half-destroyed roof; broken shoji doors rattle with wind speed. Only "residual raindrops falling off of leaves" after rain. Exploration has the loudest ambience; infiltration lowers it; combat pushes combat sounds forward. Meyer is audio director and Lord senior sound designer. | partly | Drips are narrower than the note says; "paper screens" are shoji doors. Other points hold. |
| AU32 | CK44: Ghost of Yotei: 4 mono wind emitters; 8-channel cube rain/snow; 4 surface-dependent mono rain layers; no ambisonic beds; near/mid/far Sound Scenes | AM02, EP:262 | A02 | https://www.asoundeffect.com/ghost-of-yotei-game-audio/ , read 2026-10-21 | Wind rig of four mono emitters around the player; "no ambisonic beds in the game at all"; 8-channel cube files for rain and snow (8 instead of 36 channels); four mono rain surface layers chosen by a downward ray; near assets with mid and far renders blended by distance. One-shots follow sub-biomes around the listener. | confirmed | "Sub-biomes" is finer than the note's "biome". PS5 production, not Roblox. |
| AU33 | CK45: Sea of Thieves: sound changes below deck | AM03, EP:264 | A03 | https://www.seaofthieves.com/news/archive/inn-side-story-6 , read 2026-10-21 | Not read: HTTP 403. A search found only "Short Haul #6, Sounds of the Ship" (a different video, descent to the lower decks); no readable text for Inn-side Story 6. | unverified | Tried the page twice and a web search. Cite nothing from it. |

### Group 7: 01 note (FC30-FC33)

| id | claim | note row, EP | paper src | checked against | what the source says | verdict | note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AU34 | FC30: No Roblox audio API or number is claimed in EP:1-255 | 01 section 9, EP:1-255 | n/a | `Environment_Designer_Research_2026.txt:1-255`, searched for AudioEmitter, AudioPlayer, SoundService, AudioListener, AudioFader, attenuation, "acoustic simulation", "Roblox audio" | No match in lines 1-255. | confirmed | Absence claim over the paper file; this is a statement about the paper, not Roblox. |
| AU35 | FC31: A non-positional stereo bed cannot point to a source such as a waterfall | 01 section 9, EP:159 | E00 | `audio/objects.md:41-47`; `sound/objects.md:44-48` | 2D audio is non-directional and does not change with position. Legacy Sounds in SoundService or Workspace also keep fixed volume and pan. | confirmed | Engine behavior matches the paper's assumption. |
| AU36 | FC32: Valve team reports Steam Audio HRTF, DSP and occlusion in Alyx | 01 section 9, EP:107 | C10 | https://www.reddit.com/r/HalfLife/comments/esen9b/were_developers_from_the_halflife_alyx_team_ask/ (fetch refused); web search, read 2026-10-21 | Thread not readable. Search results confirm the AMA and mention "numerous Steam Audio improvements" only. HRTF, DSP and occlusion not seen. | unverified | Tried Reddit, SteamDB (HTTP 403) and a search. |
| AU37 | FC33: Deadlock Sunken Plaza muffles outside sound; TOTK sound staff set where surface and sky audio switch; Esperança sound recording notes | 01 section 9, EP:113, 75, 81 | C11, C05, C06 | https://www.playdeadlock.com/cityneversleeps ; Nintendo "Ask the Developer Vol. 9" page; Blizzard Esperança article, read 2026-10-21 | Deadlock page: no text for Sunken Plaza or muffling in the fetch. TOTK: sound staff pressed programmers to define the surface/sky dividing line; transition triggers mark where music switches. Esperança: a sound recordist recorded in Lisbon and Porto, day and night. | partly | One row, three sub-claims: Deadlock unverified; TOTK partly (they asked for the line, not set it); Esperança confirmed. "Tsushima" in the claim text has no source among C11/C05/C06. |

### Group 8: 03 note (CA01-CA07)

| id | claim | note row, EP | paper src | checked against | what the source says | verdict | note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AU38 | CA01: AudioAnalyzer exposes PeakLevel and RmsLevel; spectrum processing can be disabled when only levels are needed | 03 CA01, EP:651 | A14 | `ref/AudioAnalyzer.yaml:25-31, 48-56, 73-80` | Both level properties exist. SpectrumEnabled false makes GetSpectrum return an empty array and "dramatically" cuts CPU; use it when only volume is needed. | confirmed | The default of SpectrumEnabled is not stated. |
| AU39 | CA02: Server audio processing is disabled, so analysis belongs on the client | 03 CA02, EP:651, 675 | A14 | `ref/AudioAnalyzer.yaml:11-17, 31, 55-56` | All audio processing is disabled on the server; the analyzer returns empty or zero results there; PeakLevel and RmsLevel are 0 on the server. | confirmed | Both levels are also NotReplicated (`ref/AudioAnalyzer.yaml:25-35`). |
| AU40 | CA03: Wire.Connected marks an active valid connection (valid pins, no cycle) | 03 CA03, EP:653 | A15 | `ref/Wire.yaml:57-74` | True when source and target instances and pin names are all assigned, the pins exist, and the connection does not make a cycle. ReadOnly and NotReplicated. | confirmed | The name `Connected` is right. NotReplicated: read it on the machine whose graph matters. It says nothing about whether the audio is heard. |
| AU41 | CA04: Spatial queries separate bounding boxes from the occupied shape | 03 CA04, EP:672 | A12 | `ref/WorldRoot.yaml:667-690, 769-790` | As AU24. | confirmed | |
| AU42 | CA05: A persistent ambient source must survive or be rebuilt after stream-out | 03 CA05, EP:673 | A13, A05 | `workspace/streaming/techniques.md:382, 274`; `ref/AudioPlayer.yaml:113-125, 138-150` | Audio parented to a 3D object stops at stream-out; the docs' fix is a persistent model or non-streaming container. Rebuild-on-return is not described. AutoPlay does not apply to replicated players; IsPlaying replicates. | partly | Behavior confirmed. "Rebuilt" is the paper's design rule (opinion). The docs do not say whether a re-streamed player resumes. The AudioEmitter page (A05) says nothing on streaming; only A13 supports this. |
| AU43 | CA06: A deprecated-property assumption is a review item (AssetId deprecated, Asset current) | 03 CA06, EP:657 | A11 | `ref/AudioPlayer.yaml:43-60` | AssetId is Deprecated and Hidden, NotReplicated; use Asset. | confirmed | EP:657 names no property, as the note says. |
| AU44 | CA07: Legacy Sound and the advanced graph differ; acoustic simulation left beta; do not promise it on low-end phones | 03 CA07, EP:755 | A09, A10 | `ref/SoundService.yaml:11-20, 61-77`; DF | Separate systems: SoundService settings split between Sounds and the graph. Out of beta on 2026-09-22. Reverb, occlusion and diffraction may lower accuracy or turn off to hold frame rate. | confirmed | The "do not promise on low-end phones" part is the paper's opinion; DF's fallback sentence supports it. |

## Streaming-safe ambience (answers X13)

Question: `sound-design` S-150 puts shared ambience on server-owned players. A13 says audio parented to a streamed object stops on stream-out. Where can a zone's AudioPlayer and AudioEmitter live so they keep playing or restart correctly with StreamingEnabled?

Facts from the docs:

| Fact | Source |
| --- | --- |
| Streaming applies only to descendants of Workspace. Other containers (ReplicatedStorage, ReplicatedFirst) are not eligible. | `workspace/streaming/index.md:30` |
| A Sound or AudioPlayer parented to a 3D object stops when that object streams out. Docs fix: persistent model or non-streaming container. | `workspace/streaming/techniques.md:382` |
| A streamed-out instance is parented to nil. Local-only property changes can be lost on return. | `workspace/streaming/index.md:79` |
| Persistent models are sent whole after join, before `PersistentLoaded`, and never stream out. Use sparingly; wait for PersistentLoaded on the client. | `workspace/streaming/index.md:234-240`; `workspace/streaming/techniques.md:87, 251` |
| Regions inside `StreamingMinRadius` never stream out. | `workspace/streaming/index.md:70` |
| A Model with no BasePart descendants is exempt from streaming out unless it becomes a descendant of a BasePart. | `workspace/streaming/index.md:72, 220` |
| Instances created or cloned by client scripts are exempt from streaming out unless parented under a server-created instance. | `workspace/streaming/index.md:74-76` |
| `Player:RequestStreamAroundAsync()` (temporary) and `Player:AddReplicationFocus()` (limited use) keep an area loaded. | `workspace/streaming/techniques.md:205`; `workspace/streaming/index.md:145` |
| An emitter works with an Attachment, Camera or PVInstance parent, or with PositionType Instance and a PositionInstance. Otherwise it is silent. | `ref/AudioEmitter.yaml:10-17, 196-232` |
| AudioPlayer.IsPlaying is read-only and replicates; Play() replicates server to client; AutoPlay does not apply to replicated players. | `ref/AudioPlayer.yaml:113-125, 138-150, 517-519` |
| Audit code that plays audio on spawn: flag the first spawn so a later stream-in does not replay it. | `workspace/streaming/techniques.md:274` |

Places a zone's ambience can live:

| # | Place | Keeps playing at stream-out? | Status |
| --- | --- | --- | --- |
| 1 | Non-spatial bed: AudioPlayer in SoundService wired to an AudioDeviceOutput (2D). Not a Workspace descendant, so streaming does not touch it. | Yes | Documented scope (`index.md:30`); applying it to audio objects is inference. Not directional (AU03, AU35). |
| 2 | Persistent Model holding the AudioPlayer, Wire and AudioEmitter (emitter on an Attachment or part inside it, at the source position). | Yes | Documented (`techniques.md:382`). Cost: memory; the docs call persistent models rare. Keep to a few small parts (the "small" part is inference). |
| 3 | A Model with no BasePart descendants as the emitter's parent. Model is a PVInstance, so the emitter takes the model's position. | Probably | Exemption documented (`index.md:72`). That the emitter uses the part-less model's pivot is inference. Test. |
| 4 | Client-created anchor part or Attachment (a LocalScript makes it, parents it to Workspace) with the player, wire and emitter. | Probably | Exemption documented (`index.md:74-76`). That a direct Workspace parent counts as "not under a server-created instance" is inference. Test. |
| 5 | Server-owned AudioPlayer in SoundService, wired to a client-side or persistent emitter. | Player yes; emitter per its own container | Inference. Wire status is `Wire.Connected` (`ref/Wire.yaml:57-69`); what a Wire does when its target is nil is not documented. |
| 6 | Source inside `StreamingMinRadius` of every place the player can stand, or held by a replication focus. | Yes while the player is near | Documented (`index.md:70`; `techniques.md:205`). Does not cover far sources such as a waterfall heard from a distance. |

Not safe: AudioPlayer or AudioEmitter parented to ordinary streamable parts or models (the default case): audio stops at stream-out (AU27).

Unknown (no doc statement; test with leave, return, leave):

| Unknown | Why it matters |
| --- | --- |
| Whether a server-owned AudioPlayer that was playing resumes on a client when its part streams back in | `AutoPlay` does not apply to replicated players; `IsPlaying` replicates, but the docs do not say it restarts playback on stream-in. |
| Whether `PositionInstance` re-resolves after its target streams out and in | Nil position means silent (`AudioEmitter.yaml:209-210`). |
| What a Wire does when one end is parented to nil | Not documented. |

Recommended pattern (inference, matches AM19): the shared ambience state (zone, weather, time) is server-owned and replicated as attributes or values. A client controller owns the audio objects: tag the zone anchors; on instance-added create the AudioPlayer, Wire and AudioEmitter once; on instance-removed destroy them. This avoids both the doubled loop and the lost loop. For a source that must always sound (hero landmark), use place 2 or a replication focus. This needs a Studio play-test; nothing here is tested.

Three-line answer:

1. Anything parented to an ordinary streamable part stops at stream-out; the docs name persistent models and non-streaming containers as the only fixes.
2. Safe homes: a 2D bed in SoundService (not a Workspace descendant), a small Persistent Model for the few must-hear sources, and (inference) a part-less Model or a client-created anchor for the rest.
3. Whether a re-streamed server-owned player resumes is undocumented, so build zone audio on the client from stream-in and stream-out signals and test leave, return, leave.

## Conflicts with the sound-design skill

Skill read: `.agents/skills/sound-design/SKILL.md`, `references/roblox-audio.md`, `evidence/sound-emotion-reference.md`. Not edited. Only Roblox facts I verified are compared; the skill's other S-ids (uploads, compressor and limiter ranges, policy) were not in my scope.

| # | Skill statement | Verified fact | Source | Verdict |
| --- | --- | --- | --- | --- |
| C1 | S-141 evidence row: "One AudioFader per bus ... Volume 0-3, default 1" (`evidence/sound-emotion-reference.md:532`); `references/roblox-audio.md:15`: "AudioFader ... Volume (0-3, default 1)" | Range is 0-10. Default is not stated on the page, so "default 1" is unverified. The rule "one fader per bus" is unaffected. | `ref/AudioFader.yaml:44-47`; raw upstream `AudioFader.yaml` | contradicted |

Consistent with the skill (no change needed): `roblox-audio.md:13` AudioPlayer Volume 0-10 and PlaybackSpeed 0-20 (`ref/AudioPlayer.yaml:294-299, 356-362`); `:16` 400 curve points and angle 0-180 (`ref/AudioEmitter.yaml:454-457, 503-506`); `:20` AudioFilter ranges (`ref/AudioFilter.yaml:71, 93, 116`); `:22` AudioReverb ranges (`ref/AudioReverb.yaml:67, 129, 148, 169, 189, 273`); S-145 RolloffScale has no effect on the graph (`ref/SoundService.yaml:324-349`); S-147 AmbientReverb does not touch the graph (`ref/SoundService.yaml:74-77`); S-146/S-226 three-part gate (`ref/SoundService.yaml:31-46`, emitter, listener); S-151 IsReady (`ref/AudioPlayer.yaml:161-176`); S-222 Asset replaces AssetId (`ref/AudioPlayer.yaml:43-60`); S-140 no new Sound objects (`audio/objects.md:22-24`).

Gaps (not contradictions; the skill is silent):

| # | Gap | Why it matters | Source |
| --- | --- | --- | --- |
| G1 | S-146/S-226 do not say `SoundService.AcousticSimulationEnabled` is Disabled by default | A place that never sets it gets no acoustic simulation, even with emitter and listener flags true | DF |
| G2 | S-150/S-219 say server players hold shared ambience but not where the player and emitter live | A server-owned player under a streamable part stops at stream-out (X13 section) | `techniques.md:382` |
| G3 | S-140 does not state the listener setup | Default ListenerLocation builds a listener only with the default voice and audio-API setup; the property is PluginSecurity | `enum/ListenerLocation.yaml:17-25`; `ref/SoundService.yaml:117-134` |
| G4 | S-118 gives a custom curve but not the no-curve case | No custom curve gives an inverse-square curve with no end distance | `ref/AudioEmitter.yaml:521-522` |
| G5 | Skill lists `AcousticSimulationEnabled` but not the geometry inputs | AudioCanCollide, AcousticAbsorption and Density change the result | DF; `ref/BasePart.yaml:269` |

Note fixes owed (not mine to make): `02-ambience-life-dressing-terrain.md` AM08 and CK12 (0-3 to 0-10) and X03 (void premise); AM01 wording on drips and paper screens (AU31); AM10 may add the PluginSecurity consequence (set in Studio).
