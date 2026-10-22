> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit reference: universal. J008. Facts: `knowledge/reference/environment/fact-check-performance-import.md` (**PI**, **PX**), `fact-check-lighting.md` (LF, LX). Measurement method: `environment-design/references/review.md` §5. Docs paths relative to `knowledge/external/roblox-creator-docs/`. **CAP** = engine limit; **START** = recommended starting value; neither is a budget. Revised by J018 maker environment-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (two cheap defaults in §2).

# Performance: cheap by default, budgets by measurement

## 1. Streaming (set in Studio Properties: these properties are NotScriptable, PX02)
| Setting | Value | Kind | Source |
| --- | --- | --- | --- |
| StreamingMinRadius / StreamingTargetRadius | 64 / 1024 studs (also the defaults); Target larger than Min; raising Min costs memory and server bandwidth | START | `workspace/streaming/index.md:94-138` (PI01-PI02) |
| StreamOutBehavior | Opportunistic recommended; the default is LowMemory | START | PX02 |
| ModelStreamingBehavior | Improved recommended; the default is Legacy | START | PX02 |
| StreamingIntegrityMode | PauseOutsideLoadedArea recommended | START | PI01 |
| Stress test | full traversal, distant teleports, revisits, plus a temporary run at Target 64 (the docs also say Target > Min; use 64 only as a test) | method from docs | `workspace/streaming/techniques.md:394-396` (PI36) |
| Model extent | keep each model under about 64 cubic studs so it streams in whole; split bigger ones and give each a LevelOfDetail | guidance | `techniques.md:64` (PX03) |
| Frustum streaming | opt-in per player (server only), adds camera-view loading, costs client memory and CPU; fast turns can churn far instances; Opportunistic frustum-only content lingers 1.5 s | use only for a shown far-view need | PI03-PI06 |
| SLIM | composite LoD stand-ins that keep rendering after the full instances stream out; needs StreamingEnabled, a place saved to Roblox and Team Create; static models only (no runtime changes, animations or Humanoids); local-only places produce no SLIM | for static architecture and skyline | `workspace/streaming/slim.md` (PI08-PI11) |
| `Workspace.MeshStreamingAndImprovedLods` | RolloutState, NotScriptable; when enabled, per-MeshPart RenderFidelity is ignored. Check which path is active before tuning RenderFidelity | check per place | PI12-PI13 |
Before a screenshot or a walk test, move the character or camera into the content: the client holds only what is streamed in (FS-V09).

## 2. Cheap defaults while building
| Default | Source |
| --- | --- |
| Anchor everything static; Box collision where detail is not needed; CanCollide / CanTouch / CanQuery false on parts nothing touches | PI20 |
| Import each asset once and duplicate in Studio so instancing works | PI18-PI19 |
| Few shadow-casting local lights; avoid many small parts in shadow and overlapping transparent parts (overdraw) | PI21 |
| Unique textures unless the atlas sits on batchable parts seen together (one atlas region streams the whole atlas mip) | PI17 |
| Light Range is clamped to 120 studs, so a big area is not lit by one huge light | LX01 |
| Particles: cost follows screen area and overlapping layers; caps 400/s per emitter (100/s mobile), lifetime 20 s | LF35-LF37 |
| Do not pay detail for parts nobody sees or uses | FS-T09 |
| Rest areas are cheap: the calm floors and plain walls the read needs also save parts, triangles and texture memory; spend unique assets by the read plan's ranked work list | J018 |
| Alpha cards (grass, reeds, hanging moss) are few: overlapping transparent cards are overdraw on phones | PI21; J018 |

## 3. What degrades on phones
| Behavior | Source |
| --- | --- |
| Quality level changes draw distance, shading, geometry, textures, particles, trails and post effects; the exact effect is device-specific and cannot be relied on | `_api-reference/enums/QualityLevel.yaml:19-21` (PI29, LF30) |
| Shadows degrade as quality falls and switch off below quality level 4 | `performance-optimization/improve.md:419-421` (PI28) |
| 4K textures: disabled on low-end Android under 3.5 GB; iOS needs about 3.5 GB or more (device caps, not budgets) | PI15-PI16 |
| Flipbook particles can switch off on low memory | LF39 |
| Acoustic simulation can lower its quality to hold frame rate | AU18 |

## 4. Measuring (tools and what they prove)
| Tool | Use | Source |
| --- | --- | --- |
| Scene Analysis (released 2026-07-10): instance, script-memory, unparented-instance, audio-memory, animation-memory and triangle-composition views | where the cost is, per category | PI30; through MCP: `execute_luau` (Client or Server during play) or the Studio `skill` tool's scene-analysis skill; no MCP tool carries its name (PI64) |
| MicroProfiler | frame timing and spikes; on a phone: enable in client Settings, open the shown address from a machine on the same network | PI32 |
| Real phone, 10-15 minutes of active play at least | thermal slow-down | PI34 |
| Studio stats, emulator | relative changes only; never presented as phone results | PI31, PI33 |
| FPS = 1000 / frame ms (30 FPS = 33.3 ms, 60 FPS = 16.7 ms); the owner chooses the target | arithmetic | PI35 |
Roblox's design page gives "under 1,000 draw calls and 1,000,000 triangles" only as an example of one baseline device; never copy it as a budget (PX01). Stage budgets come from the owner or the measurement method in `environment-design/references/review.md` §5.
