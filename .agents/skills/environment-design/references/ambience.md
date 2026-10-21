> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit reference: universal. J008. Sources: environment paper notes `knowledge/reference/environment/02-ambience-life-dressing-terrain.md` (rows AM, ZX, SS, VL, CO, AF) and `03-pipeline-performance-review.md` (W07, RS, AX); audio facts checked in `fact-check-audio.md`. Tags: **V** VERIFIED, **E** EXPERIENCE, **O** OPINION, **U** UNKNOWN.

# Ambience: how a place sounds and moves

The environment designer decides **where and why** a place sounds and moves. The sound designer decides **how it sounds** (clips, layers, curves, gains, mix). The VFX designer decides **how an effect is built**. The game designer decides which cues matter for play. The owner approves the experience (AM20 O). Write it down in the ambience map (`templates/environment/ambience-map.md`).

## 1. What makes a place sound real
| ID | Practice | Evidence |
| --- | --- | --- |
| AB-01 | **Every sound and every motion has a cause the player can see or believe.** A waterfall sound comes from the falls; drips come from a wet ceiling over a pool; frogs live in reeds (the frog itself may stay hidden). No prop makes noise without a reason, and not every prop makes noise. | AM01 E (Ghost of Tsushima); SS1-SS7 O; AX04 O |
| AB-02 | **Split each zone's plan into four jobs**, then fill only the ones the place needs: (a) a continuous layer, only if the place needs one; (b) intermittent life (calls, gusts, drops) that plays when time, weather or state allow it; (c) recognizable world sources at real positions; (d) weather and exposure that change the other three. A "bed" is a job, not a file. A cave can need almost no continuous layer; a river can be several sources along the water, not one point. | AM04 O (synthesis of A01-A03) |
| AB-03 | **Not one global loop.** Each zone gets its own causal plan. The same loop renamed per biome is a defect. | RU08 O; AX01 O |
| AB-04 | **Sound can guide, but it is never the only guide.** A source heard before it is seen (the falls behind the bend) points the player there. A non-positional layer cannot point anywhere: label it atmosphere, not navigation. If the game supports muted play, every route cue also has a visual form. | G08 O; DN07 O |
| AB-04b | **A point source is positional and ends somewhere.** A waterfall, fire or frog chorus sits at its visible cause; a non-positional bed is heard everywhere and is only for sound that has no direction. Every positional source gets an end distance from the sound designer (an emitter with no curve never fades out). | AU35 V; AU06 V |
| AB-05 | **Gameplay cues come first.** Ambience never covers a warning, a pickup or a hit. Water noise never masks a required cue. Keep listening space and resources for those cues. | AM04 O; AX02 O; ZX3 O |
| AB-06 | **Exposure is not height.** Height, shelter and weather are separate inputs. A room high on a tower is not an open ridge; a low ravine can funnel wind. At a cave mouth the outside fades by the shape of the entrance and the player's path, not by a height line. Rain sounds different in the open, under a roof or canopy, and fully inside. | AM17 O; AX03 O |
| AB-07 | **One shared environment state.** Time of day, weather, wind, water, events and the current zone are one record; sound, VFX, lights and moving plants all read it. A flag whipping over a silent, still soundscape is a defect unless the brief wants it. | CO06 O; VL02 O; K03-e O |
| AB-08 | **One acoustic choice per enclosed space.** A cave gets either an authored reverb or Roblox's acoustic simulation, recorded in the map, never both by accident. Quality of acoustic simulation can drop on weak devices, so a needed navigation hint never depends on subtle echo alone. | AM13 O; AM09 V (see fact-check-audio) |
| AB-09 | **Borders blend; they never switch.** The whole mix never changes at one line. Write the blend per border: where it happens (an entrance corridor that belongs to the route is better than a box face), how it changes, and the edge cases: walking back, standing on the edge, teleport, respawn, a camera that passes a wall before the avatar does. | AM16 O; AX05 O |
| AB-10 | **Plan for streaming.** A sound or emitter whose part streams out stops. Zone data must not live on decorative parts that can stream out. Each important source gets a real anchor and a keep-or-rebuild rule; on return it is rebuilt once, never doubled. Test leave → return → leave. Never make the whole map persistent to fix one ambience bug. | AM18 V; AM19 O |
| AB-11 | **Ambient motion has a job, a region and an off-switch.** Each moving thing is one of: a spatial cue, a material reaction, weather, or decoration. A readable cluster beats the same effect spread everywhere. Keep moving decoration out of the route and hazard silhouettes. Never cover a phone screen in mist to hide an empty background. | VL05 O; VL07 O; VL08 O |
| AB-12 | **Degrade in order.** When the device is weak or the budget is tight, drop optional one-shots and decorative layers first; navigation and gameplay cues last. Each zone writes its fallback. | VL09 O; AF14 O |

## 2. How a request to the sound or VFX designer reads
Say what the player should **work out**, not which file to use: "the waterfall is a believable clue before the turn, still there at the overlook, and duller inside the cave, in line with the cave's acoustic choice." The VFX request points at the same source, the same wind state and the visibility limits. Neither request states gains, ranges or particle counts as facts: nobody has measured them yet (CO05 O; DN02 O).

## 3. Numbers that do not exist
No source gives a usable Roblox range, gain or crossfade time for a waterfall, river, wind, fire, frogs, drips or birds, a border width, a fade time, or a safe number of ambient sources on a phone (SS1-SS7 U; AX09 U; VL09 O). These numbers come from **this stage**: the blockout coordinates set positions and bounds; the sound designer sets ranges and gains from the listening checkpoints; a phone trace sets the budget. Until then the field is `UNKNOWN`, never 0 and never a guess. A documented API bound or a tutorial's demo distance is not a preset (SS rule EP:318).

## 4. The four-zone example (planning illustration, not measured)
The paper sketches a stage with a summit, a waterfall basin, a swamp and a cave (ZX1-ZX4 O). Use it as a picture of a finished map row, never for its numbers (it has none):
- **Summit:** wind that follows exposure and weather; gusts; maybe a bird on a ridge perch. One gust state moves grass and flags. Fallback keeps the wind, drops wildlife.
- **Falls:** the main source sits at the visible impact; the outflow is its own source; heard from an approach checkpoint before the reveal; the blend to the swamp follows the outflow.
- **Swamp:** insects if approved; frog calls at reed clusters, never a constant global chorus; birds only in a chosen time or weather; frogs kept clear of the frequencies of gameplay warnings.
- **Cave:** sparse; drips from a wet ceiling into a pool; one acoustic choice recorded; the outside fades across the mouth; tested at the mouth, the first bend, the deep chamber and on the way back.

## 5. Ambience checks the environment designer owns
| Check | Evidence |
| --- | --- |
| Every zone on the route is in the map, with a feeling, bounds, neighbors and a fallback | the map |
| Every source has a visible cause and a real anchor in the place; the map ids match the ids in the place | scene audit (`environment-craft`): sources vs map |
| Each border tested: approach, crossing, walking back, standing still, teleport, respawn, stream out and in | one record per state (W07 O; RP01 O) |
| After any change made for budget, the ambience and clarity checks it can touch are run again | before/after records (W09 O) |
| Sound and picture agree: the close-up of the source and the player's view show the same active state and place | timestamped clip pair (RS03 O) |
| **Listening is not judged from pictures or data.** Positions and wires prove placement only, never tone, masking, loop joins or smoothness. Without a listener the result is "auditory acceptance pending", never pass. | RS07 O; RV03 O; AX07-AX08 O |
