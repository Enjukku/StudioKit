---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: J010 (owner 2026-10-21 - every main agent learns its section of the Roblox docs); docs mirror revision 7400643 (refreshed 2026-10-20)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Roblox docs map: which part of the docs each role owns

Paths are relative to `knowledge/external/roblox-creator-docs/` (the local mirror; `_api-reference/classes/<Class>.yaml` holds every class, property, method and event). Read your rows before you design or build. The routing rule is `AGENTS.md` §0: the context packet's Roblox docs section first, a scout when it finds nothing or the system is new to you, a Studio probe when the docs are silent.

| Role | Read first (sections) | Key pages | API classes to check |
| --- | --- | --- | --- |
| architect, feature-builder, quick-builder, reviewer, qa-lead | `scripting/`, `luau/`, `physics/`, `workspace/`, `players/`, `input/`, `cloud-services/` | scripting/events/remote.md; scripting/security/; physics/sleep-system.md; physics/network-ownership.md; cloud-services/data-stores/index.md; projects/server-authority/index.md; luau/type-checking.md; luau/native-code-gen.md | the class of every Instance you touch; RemoteEvent, DataStoreService, MarketplaceService, Players, Workspace |
| performance-engineer | `performance-optimization/`, `physics/`, `workspace/streaming/` | performance-optimization/identify.md, improve.md, test-on-hardware.md, scene-analysis.md; performance-optimization/microprofiler/; physics/adaptive-timestepping.md | Stats, Workspace (PhysicsSteppingMethod, streaming), RunService |
| studio-operator | `studio/` | studio/mcp.md; studio/testing-modes.md; studio/developer-console.md; studio/device-simulator.md; studio/network-simulator.md | StudioTestService |
| film-director | `workspace/camera/`, `animation/`, `environment/`, `audio/` | workspace/camera/index.md; resources/modules/event-sequencer.md; animation/events.md; environment/lighting.md; environment/post-processing-effects.md; ui/ (letterbox, subtitles) | Camera, TweenService, Animator, AnimationTrack, Lighting, BlurEffect, DepthOfFieldEffect |
| art-director | `art/`, `environment/`, `effects/`, `parts/`, `ui/` | environment/lighting.md; environment/atmosphere.md; parts/materials.md; art/index.md; production/publishing/thumbnails.md | Lighting, Atmosphere, MaterialVariant, SurfaceAppearance |
| animator | (checked 2026-10-21, J006; facts in `knowledge/reference/animation/fact-check-roblox-runtime.md`, `fact-check-techniques.md`) `animation/`, `physics/` (constraints, network ownership, sleep), `art/modeling/` (rigging, skinning), `effects/particle-emitters.md` (flipbooks), `parts/textures-decals.md`, `environment/global-wind.md`, `workspace/streaming/`, `performance-optimization/` | animation/index.md; animation/using.md; animation/editor.md; animation/events.md; animation/curve-editor.md; animation/graph-editor.md; animation/inverse-kinematics.md; art/modeling/rigging.md; characters/adaptive-animation.md; physics/constraints/animation.md; physics/mechanical-constraints.md; physics/constraints/hinge.md; physics/constraints/prismatic.md; physics/constraints/spring.md; physics/network-ownership.md; physics/sleep-system.md; tutorials/use-case-tutorials/physics/build-a-hinged-door.md; tutorials/use-case-tutorials/physics/create-elevators.md; effects/particle-emitters.md; parts/textures-decals.md; environment/global-wind.md; workspace/streaming/techniques.md; performance-optimization/improve.md; performance-optimization/microprofiler/tag-table.md; resources/the-mystery-of-duvall-drive/develop-a-moving-world.md | Animator, AnimationTrack, Animation, AnimationController, AnimationPriority, KeyframeSequence, CurveAnimation, KeyframeMarker, Motor6D, Bone, AnimationConstraint, IKControl, TweenService, TweenInfo, EasingStyle, EasingDirection, HingeConstraint, PrismaticConstraint (SlidingBallConstraint), SpringConstraint, ParticleEmitter (Flipbook*), Texture, PVInstance (PivotTo), Workspace (GlobalWind, ClientAnimatorThrottling, StreamingEnabled), RunService |
| character-rigger, modeler | `art/characters/`, `avatar/character-bodies/`, `animation/`, `characters/`, `avatar-setup/`, `art/modeling/` | art/characters/specifications.md; art/characters/import.md; animation/editor.md; animation/graph-editor.md; animation/inverse-kinematics.md; parts/meshes.md | Bone, Motor6D, Animator, AnimationController, Humanoid, MeshPart |
| environment-designer | `environment/`, `parts/`, `workspace/streaming/` | parts/terrain.md; studio/terrain-editor.md; environment/skybox.md; environment/clouds.md; environment/global-wind.md; performance-optimization/design.md | Terrain, Lighting, Atmosphere, Sky, Clouds |
| vfx-designer | `effects/`, `environment/post-processing-effects.md` | effects/particle-emitters.md; effects/beams.md; effects/trails.md; effects/light-sources.md; effects/highlighting.md | ParticleEmitter, Beam, Trail, PointLight, Highlight |
| sound-designer | `audio/`, `sound/` | audio/index.md; audio/objects.md; audio/effects.md; sound/groups.md | AudioPlayer, AudioEmitter, AudioListener, AudioFader, Wire |
| ui-ux-designer | `ui/`, `input/` | ui/list-flex-layouts.md; ui/size-modifiers.md; ui/styling/; ui/ui-shadows-and-individual-corners.md; production/game-design/ui-ux-design.md | ScreenGui, UIListLayout, UIStroke, UICorner, GuiService |
| game-designer | `production/game-design/` | production/game-design/core-loops.md; onboarding.md; design-for-roblox.md; prototyping.md | — |
| progression-designer | `production/game-design/`, `production/monetization/` | production/game-design/balance-virtual-economies.md; season-pass-design.md; production/monetization/paid-random-items.md | MarketplaceService |
| live-ops-designer | `production/game-design/`, `production/promotion/`, `cloud/guides/` | production/game-design/liveops-essentials.md; liveops-planning.md; content-updates.md; cloud/guides/experience-notifications.md; production/experiments.md | ConfigService |
| analyst | `production/analytics/`, `cloud/guides/analytics/` | production/analytics/index.md; funnel-events.md; economy-events.md; retention.md; production/experiments.md; production/configs.md | AnalyticsService |
| marketing | `production/promotion/`, `production/publishing/` | production/publishing/thumbnails.md; discovery.md; production/recommendation.md; cloud/guides/advertising.md | — |
| trend-scout | `discovery.md`, `production/recommendation.md` | discovery.md; production/roblox-user-base.md | — |
| everyone touching paid items, chat, text, ads, younger players | `production/monetization/`, `chat/`, `ui/text-filtering.md` | production/monetization/paid-random-items.md; production/ad-placements/ | PolicyService, TextService |

New features and beta status: `knowledge/reference/roblox/whats-new.md`. Engine-first table for builders: `.agents/skills/engineering-craft/references/engine-first.md`.
