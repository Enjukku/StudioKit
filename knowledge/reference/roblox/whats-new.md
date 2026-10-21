---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: "J001 step 0: mirror refresh 7400643 + official Roblox posts 2026-04..10"
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Research rows from two researcher agents (claude-sonnet-5-5, medium) that read each DevForum post's first-post date and author.

# Roblox: what is new in 2026 (engine, Studio, policy)

| | |
| --- | --- |
| **What** | Features, betas and rules Roblox shipped or announced in 2026, newest first per area. Universal: true for any Roblox game. |
| **Read it when** | Before you write or update an engineering skill, before you say a Roblox feature does not exist, and before you use any UI, Studio or policy feature from memory. |
| **Status words** | **live** = publishable now. **beta** = Studio Beta flag (File → Beta Features); usually **not publishable** to live games. **planned** = on the roadmap; treat as unavailable. |
| **Hard rules** | 1. The API yaml in the mirror has **no beta markers**: a property in `_api-reference/` is not proof it is live. 2. Planned rows are not features. 3. Policy numbers move (thresholds, rates): link the page, do not copy the number into a skill without its date. |
| **Sources** | Rank 1: local mirror `knowledge/external/roblox-creator-docs/` (revision below). Rank 2: DevForum posts by Roblox staff (author in each row). "recap" = a staff weekly-recap thread that names no author for the item. |
| **Step** | The J001 skill step each row feeds (1 MCP, 2 policy, 3 data, 4 performance, 5 networking/security, 6 architecture/Luau, 8 UI, 9 analytics). |

## Mirror refresh 2026-10-20

- Upstream `Roblox/creator-docs` revision `7400643072eb304fe85ef89cffe96f5c56f98c7e` (was `4fc84785`, 2026-10-10). 864 pages, 2 new, 132 changed, 57 retired pages kept with a successor banner. API reference: classes 626, enums 515.
- New pages: `cloud/guides/error-reporting/index` (Open Cloud Error Reporting API), `avatar/in-experience-creation-makeup`.
- New API: `Class.Logger` (hierarchical structured loggers from `LogService:GetLogger`; its yaml warns output may be truncated), `Enum.AudioSortType`, `Enum.PromptCreateOutfitResult`.
- Corrected the four project-authored UI pages (`ui/ui-shadows-and-individual-corners`, `ui-corner`, `ui-gradient`, `ui-stroke`): they still said "beta, not publishable" for features that went live in June.
- Refresh: `python tools/sync_roblox_docs.py` (`--check` first). Then update this note.

## UI (step 8)

| Feature | Status | Date | Source | What it means |
| --- | --- | --- | --- | --- |
| UIShadow base (BlurRadius, Color, Offset, Spread, Transparency, Enabled, ZIndex) + per-corner UICorner (TopLeftRadius ...) | **live** | full release 2026-06-23 | [DF 4636263](https://devforum.roblox.com/t/studio-beta-new-ui-capabilities-shadows-individual-corners/4636263), missmandypanda; mirror `ui/appearance-modifiers#shadow`, `#corners` | Native shadows and glows replace 9-slice image shadows. Keep ≤ 100 shadows on screen. Style either CornerRadius or the per-corner properties, not both. Jagged shadows on very large radii |
| Upgraded UIShadows: `Mode = Text`, `Inset`, `ShowBehindParent = false`, UIGradient under a shadow | **beta, not publishable** | 2026-10-14 | [DF 4934553](https://devforum.roblox.com/t/studio-beta-upgraded-uishadow-capabilities/4934553), missmandypanda | Text shadows and inner shadows. Spread/Inset/ShowBehindParent do nothing in text mode; rich text ignores shadow colour |
| Upgraded UIGradients: `Type` Radial/Conical, `TileMode`, `Scale`, Path2D, linear-space blend | **beta, not publishable** | 2026-09-02 | [DF 4846594](https://devforum.roblox.com/t/studio-beta-upgraded-ui-gradients/4846594), missmandypanda | Mirror guide shows them unmarked. ≤ 1,000 gradients; animate offset/rotation/scale, not colour |
| Styling Transitions (TweenInfo in StyleRules, hover/pressed) | **live** | full release 2026-07-27 | [DF 4646870](https://devforum.roblox.com/t/full-release-styling-transitions/4646870), missmandypanda; mirror `ui/styling/` | Style-sheet driven hover and press motion without scripts |
| StyleQuery (MinSize, MaxSize, AspectRatioRange, PreferredInput, ReducedMotionEnabled, PreferredTextSize) | **live** | full release 2026-05-11 | [DF 4566519](https://devforum.roblox.com/t/full-release-stylequery-more-styling-features/4566519), missmandypanda; `StyleQuery.yaml` | Responsive UI rules (like CSS media queries) for phone/tablet/console and reduced motion |
| Clipping of rotated GuiObjects and Path2D (`StarterGui.ClipsDescendantsSupportsRotation`) | **live, opt-out**; the property is **removed in November 2026** | 2026-07-14 / 09-24 | [DF 4737864](https://devforum.roblox.com/t/opt-out-phase-introducing-clipping-support-for-rotated-elements-path2d/4737864), missmandypanda | Do not depend on the property. ClipsDescendants still does not clip to UICorner: use a CanvasGroup |
| InputActionLabel (shows the current binding as text or icon) | **beta, not publishable**; `InputAction.PreferredBinding`, `InputBinding.DisplayName/DisplayImage` are live | 2026-08-06 | [DF 4779420](https://devforum.roblox.com/t/studio-beta-no-code-hotkey-hints-with-inputactionlabel/4779420), missmandypanda | Hotkey hints; until release, build hints from PreferredBinding |
| `GuiButton.SecondaryActivated` | **live** | 2026-07-06 | [DF 4720108](https://devforum.roblox.com/t/introducing-guibuttonsecondaryactivated/4720108), BitwiseAndrea; `GuiButton.yaml` | Right-click, long press (> 1 s), R3, Alt+Enter; no standard visual cue, so give a visible alternative |
| Roadmap: 2D particles, animated image containers, UI blur (early 2027) | **planned** | 2026-09-18 | [Roadmap DF 4880208](https://devforum.roblox.com/t/creator-roadmap-2026-fall-update/4880208) | Not available |

## Studio, MCP and AI tools (step 1)

| Feature | Status | Date | Source | What it means |
| --- | --- | --- | --- | --- |
| Built-in Studio MCP server (stdio; Windows `%LOCALAPPDATA%\Roblox\mcp.bat`) | **live** | 2026 | mirror `studio/mcp.md` | Tools: script_read, multi_edit, script_search, script_grep, execute_luau (Edit/Client/Server), get_studio_state, start_stop_play, get_console_output, screen_capture, character_navigation, user_keyboard_input, user_mouse_input, search_game_tree, inspect_instance, subagent (explore, playtest), generate_mesh/material/procedural_model, search_asset, insert_asset, upload_image, store_image, http_get, skill, list_roblox_studios |
| MCP multi-agent: every call needs `studio_id`; `set_active_studio` **removed** | **live** | 2026-08-19 | [DF 4820583](https://devforum.roblox.com/t/studio-mcp-multi-agent-improvements-and-connected-ai-clients/4820583), Urukeli | `list_roblox_studios` returns Place IDs. During a play-test the Edit data model is taken over, so Edit-targeted tools fail |
| Playtest Agent (MCP `subagent` type playtest) | **beta** (no graduation post found) | 2026-04-09 | [DF 4566767](https://devforum.roblox.com/t/studio-beta-studio-assistant-mcp-playtest-agent/4566767), Miratar | Pass/Fail report; can report false passes; stops after 50 turns; daily cap. Evidence, not proof |
| MicroProfiler analysis through Assistant and MCP | **live** | 2026-06-26 | [DF 4704417](https://devforum.roblox.com/t/automated-performance-profiling-with-microprofiler-and-assistant/4704417), ZenMa1n | Ctrl+F6, pause a capture, then ask for analysis |
| Creator-authored Assistant skills (markdown, `name` + `description`) | **live** | 2026-07-09 | [DF 4728447](https://devforum.roblox.com/t/assistant-updates-introducing-creator-authored-skills/4728447), swish741; mirror `assistant/skills.md` | Account-scoped; reachable from MCP via the `skill` tool. Place-scoped skills planned |
| Studio Debugger Luau API (ScriptDebuggerService, breakpoints, stack traces) | **beta**, plugin security | 2026-06-18 | [DF 4691312](https://devforum.roblox.com/t/beta-studio-debugger-luau-api/4691312), nidr_71 | Reachable through execute_luau; read variables only on a paused thread |
| Script Sync (scripts ↔ `.luau` files) | **live** (roadmap "shipped"; no full-release post found) | beta 2025-11-12 | mirror `scripting/sync.md`, `InstanceFileSyncService.yaml` | Syncs scripts and folders only, not attributes or tags; ≤ 10,000 scripts per root. Roblox says it does not replace Rojo |
| Package Overrides | **beta** (Studio 743+) | 2026-10-15 | [DF 4936628](https://devforum.roblox.com/t/studio-beta-package-overrides-and-usability-improvements/4936628), NeoShr3dder | Edit a package in place and keep updates; in Team Create everyone must enable it |
| Auto-Reimport of models, SurfaceAppearances, decals | **beta** | 2026-09-08 | [DF 4859863](https://devforum.roblox.com/t/studio-beta-auto-reimport-automatically-reimport-external-files-on-changes/4859863), bballerblox | Each reimport makes new asset IDs |
| Next-Gen Draggers | **beta** | 2026-06-25 | [DF 4703155](https://devforum.roblox.com/t/beta-next-gen-draggers-new-move-rotate-scale-tools/4703155), NeoShr3dder | Builder tools only |
| Studio "going agentic": Planning Mode, mesh generation, procedural models | announced | 2026-04-15 | about.roblox.com newsroom (Nick Tornow, SVP Engineering) | 44 % of the top 1,000 creators used Assistant or MCP (March-April 2026) |

## Luau and runtime (step 6)

| Feature | Status | Date | Source | What it means |
| --- | --- | --- | --- | --- |
| Structured logging: `LogService:Info/Warn/Error/Log` with `{key}` templates + context table | **live** | 2026-06-04 | [DF 4668415](https://devforum.roblox.com/t/full-release-debug-faster-with-new-structured-logging-methods/4668415), PureBigMadBoatMan; `LogService.yaml` | Expandable context in Output and F9; context > 1 KiB is dropped in Creator Hub server logs |
| `Logger` / `LogService:GetLogger` (named, nested loggers) | in the API reference; no announcement found | 2026-10 | `_api-reference/classes/Logger.yaml` | Group logs by system (`Combat.Damage`). Yaml warns output may be truncated. Check it works before a skill depends on it |
| `if local` / `if const` bindings | **beta** | 2026-10-06 | [DF 4918297](https://devforum.roblox.com/t/beta-if-local-statements-and-expressions/4918297), jjtangerine | Not in shipped code yet; no multi-return form |
| Luau 0.734-0.743 | released | 2026-08-14 .. 10-16 | github.com/luau-lang/luau/releases | Faster pcall/xpcall, string.split, gsub, table.find; `loadstring` removed from built-in type definitions; experimental exact tables |
| Instance attributes (`InstanceHandle`, `GetAttribute():Get()/:Wait()`) | **live** | 2026-07-23 | [DF 4753441](https://devforum.roblox.com/t/reference-instances-directly-with-attributes/4753441), Climber; `datatypes/InstanceHandle.yaml` | Store Instance references in attributes |
| New type solver | default since 2025-11; strict mode needs `Workspace.UseNewLuauTypeSolver = Enabled` | 2025-11-20 (no 2026 change found) | [DF 4084991](https://devforum.roblox.com/t/general-release-luaus-new-type-solver/4084991); mirror `luau/type-checking.md` | Write code for the new solver |
| Parallel Luau / Actors, native codegen | no 2026 change found (roadmap: Android native codegen shipped) | - | roadmap | Mirror `scripting/multithreading`, `luau/native-code-gen` stay current |

## Performance and observability (step 4)

| Feature | Status | Date | Source | What it means |
| --- | --- | --- | --- | --- |
| Device Simulator toolbar + Network Simulator (latency, jitter, loss; 3G/4G/Wi-Fi profiles) | **live** | full release 2026-10-16 | [DF 4861695](https://devforum.roblox.com/t/full-release-new-device-simulator-toolbar-and-network-simulator/4861695), avienn_a; mirror `studio/network-simulator`, `device-simulator` | `NetworkSettings` properties make it scriptable. Does not model device memory or GPU |
| Frustum Streaming (`Player.FrustumStreaming`) | **live, opt-in** (roadmap said late 2026) | 2026-09-29 | [DF 4904553](https://devforum.roblox.com/t/frustum-streaming-stream-what-your-players-see/4904553), 77BigBig77; mirror `workspace/streaming/frustum` | Streams far objects in view without a bigger radius; costs client memory |
| Scene Analysis tool, `SceneAnalysisService` | **live** | 2026-05-05 | [DF 4620678](https://devforum.roblox.com/t/full-release-scene-analysis-tool/4620678), MrChickenRocket; mirror `performance-optimization/scene-analysis` | Memory and triangle treemaps of the place |
| LibMP (MicroProfiler Luau API, `SetMemTargetMB`) | beta → enabled in live games (Oct update) | 2026-06-25 | [DF 4703136](https://devforum.roblox.com/t/studio-beta-introducing-libmp-the-microprofiler-api/4703136), ZenMa1n | One profiling API for client, server and Studio |
| Client CPU time by category (Scripts, Networking, Physics, Animation) | **live** | 2026-07-14 | [DF 4737435](https://devforum.roblox.com/t/analytics-break-down-your-client-cpu-time-by-category/4737435), quazotheduck; mirror `production/analytics/performance` | Find which system eats the frame on real devices |
| Error Reports: custom rules (≤ 100), first-seen version; Open Cloud Error Reporting API (60 req/min) | **live** | 2026-07 | mirror `production/analytics/error-report`, `cloud/guides/error-reporting` | Agents can read live errors with an API key the owner creates |
| Collision Summaries (`BasePart:BindToCollisionSummaries`), tunable collision precision | **live** | 2026-10-06, 2026-09 | [DF 4918568](https://devforum.roblox.com/t/collision-summaries-api-detailed-collision-data-from-the-engine/4918568), [DF 4878198](https://devforum.roblox.com/t/collision-geometry-workflow-improvements-tunable-precision-and-better-visualizations/4878198), m0bsterlobster | Engine contact point, normal, pre-solve speed; network owner only; cheaper than Touched |
| WorldModel collision groups on WorldRoot | **live** | 2026-08-31 week | [DF 4848541](https://devforum.roblox.com/t/expanding-worldmodel-simulation-capabilities-support-for-collision-groups/4848541) (recap) | PhysicsService collision-group code for WorldModels is outdated |
| Earlier 2026 (mirror): SLIM model LOD, predictive streaming, transparent batching | **live** | 2026 | mirror `workspace/streaming/slim`, `workspace/streaming/index`, `scripting/transparent-batching` | SLIM is for static models; batching needs concurrent calls, not serial loops |
| Collections (live-query groups on CollectionService); SLIM debug tints | **beta** | 2026-08 / 10 | [DF 4809228](https://devforum.roblox.com/t/studio-beta-collections/4809228), [DF 4924019](https://devforum.roblox.com/t/slim-debug-tints-in-studio-and-roblox-player/4924019) | Not in shipped code yet |
| Roadmap: adaptive streaming radius, path pre-fetch, observability platform, 200-500 stud minimum draw distance on low-end | **planned** | 2026-09 | roadmap; RDC26 [DF 4865880](https://devforum.roblox.com/t/rdc26-what-we-announced/4865880) | Not available |

## Networking and security (step 5)

| Feature | Status | Date | Source | What it means |
| --- | --- | --- | --- | --- |
| Server Authority (`Workspace.AuthorityMode = Server`) | **live, opt-in** | 2026-07-09 | [DF 4727993](https://devforum.roblox.com/t/full-release-ship-fair-and-competitive-games-with-server-authority/4727993), welblander; mirror `projects/server-authority/` | Turns on next-gen replication, InputAction player scripts, Deferred signals, streaming, fixed simulation. Limits: 8 playing tracks per Animator, 64 attributes per instance. RemoteEvents are not on the shared timeline. `CameraContext.CameraAction` removed |
| Input Action System (live); Input Action Manager editor | system **live**; editor **beta** | 2026-07-14 | [DF 4737890](https://devforum.roblox.com/t/studio-beta-input-action-manager/4737890), missmandypanda | New input code uses InputAction, not raw UserInputService |
| RemoteEvent / UnreliableRemoteEvent | no 2026 change found | - | mirror `scripting/events/remote` | Read payload limits from the mirror, not forum threads (they disagree) |
| `Player:IsVerified()` with Low/High levels | **live** | 2026-08-17 week | [DF 4820514](https://devforum.roblox.com/t/full-release-isverified-api-now-supports-verification-levels/4820514) (recap) | Gate trading or ranked play |
| Web API rate limits cut (badges, datastores, inventory, thumbnails, users web endpoints) | **live** after 2026-10-19 | 2026-09-30 | [DF 4906160](https://devforum.roblox.com/t/api-update-api-rate-limit-tuning/4906160), huaraz | External tools use Open Cloud, not cookie web endpoints |
| Roadmap: Android anti-cheat attestation, Safety Callback API, unified agentic permissions | **planned** | 2026-09-18 | roadmap | Not available |

## Data (step 3)

| Feature | Status | Date | Source | What it means |
| --- | --- | --- | --- | --- |
| One DataStore request budget shared by game servers and Open Cloud; storage 100 MB → 500 MB + 1 MB per lifetime player | **live** | 2026-07-29 | [DF 4739240](https://devforum.roblox.com/t/unifying-data-stores-open-cloud-and-game-apis-and-increasing-storage-limits/4739240), LeafGreen888; mirror `cloud-services/data-stores/error-codes-and-limits` | External tools can starve game servers: throttle them. Read current numbers from the mirror page |
| `OrderedDataStore:BatchGetAsync` | **live** | 2026-08-10 week | recap; `GlobalDataStore.yaml` | Fewer requests for leaderboards; missing keys are omitted |
| Native friends and global leaderboards (Creator Hub, backed by an OrderedDataStore) | **live** | 2026-09-14 week | [DF 4832224](https://devforum.roblox.com/t/full-release-add-persistent-friends-and-global-leaderboards-easily/4832224) (recap); mirror `players/leaderboards` | One active leaderboard per game |
| DataStore alerts, automated right-to-be-forgotten for DataStores | **live** (roadmap "shipped") | 2026-09 | roadmap | Tooling, no new API |
| Transaction Refunded webhook (Open Cloud) | **live** | 2026-09-21 week | [DF 4890339](https://devforum.roblox.com/t/new-transaction-refunded-webhook-notifies-when-a-purchase-is-cancelled/4890339) | Developer-product benefits are ours to revoke: store the receipt id when granting. No retry if the endpoint is down |
| Roadmap: player-data management (transactions, session locking, schemas), OrderedDataStore histograms (early 2027) | **planned** | 2026-09-18 | roadmap | Still write our own session lock and schema migration |

## Platform policy and monetization (step 2)

| Rule or feature | Status | Date | Source | What it means |
| --- | --- | --- | --- | --- |
| Paid random items: clarifications (bundles with a random item, luck passes, blind restocks and nested boxes all count; every outcome must give value; hiding is the preferred restricted treatment) | policy clarification | 2026-05-26 | [DF 4654622](https://devforum.roblox.com/t/clarifying-requirements-for-paid-random-items/4654622), dinobotsnarl824 | Detail in skill `platform-policy` |
| Paid random items (base rules) | standing policy | - | mirror `production/monetization/paid-random-items`; `PolicyService.yaml` | Numeric odds summing to 100 % before purchase, also for indirect currency; check `ArePaidRandomItemsRestricted` per player and offer a fixed alternative |
| Age check: `Player:PromptAgeCheck()`, `Player.AgeChecked` | **live** | API section 2026-10-12 | [DF 4607091](https://devforum.roblox.com/t/introducing-the-us-18-devex-rate-earn-42-more-on-spend-from-18-us-players/4607091), peraldon | Never gate core gameplay on it; console and VR cannot run the flow |
| Age check to chat; chat groups by age | **live** | early 2026 | `TextChatService.yaml` (`GetChatGroupsAsync`) | Do not assume all players can chat with each other |
| Social media links only for age-checked 16+; no in-game social-link sharing | policy | 2026-06-30 | [DF 4685717](https://devforum.roblox.com/t/roblox-kids-and-select-global-launch-upcoming-updates-to-eligibility-ads-manager-and-expedited-review/4685717), RbxRocketMan; mirror `production/promotion/social-media-links` | Do not build social-link UI |
| Rewarded video: native format only (custom versions banned from 2026-05-04); no third-party ad SDKs; no reward ads for under-13 | policy | 2026-03-20, upd. 04-15, 06-17 | [DF 4527365](https://devforum.roblox.com/t/new-advertising-policies-standards/4527365), superburr0; mirror `production/promotion/rewarded-video-ads` | Only the official rewarded video API |
| Kids and Select: reward-driven autoplay / infinite-scroll media feeds banned; Highly Engaged Player thresholds keep dropping | policy | 2026-08-25; 2026-10 | [DF 4829188](https://devforum.roblox.com/t/roblox-kids-and-select-new-restrictions-on-reward-driven-media-feeds/4829188), [DF 4820164](https://devforum.roblox.com/t/highly-engaged-player-threshold-drops-to-250/4820164) | Read the current number on the day; do not hard-code |
| Simpler publish path (one 16+ question, Playtest/Public, up to 10 early testers) | rolling out | 2026-10-12 | [DF 4930524](https://devforum.roblox.com/t/a-simpler-path-to-publish-plus-invite-early-testers/4930524), Sourdough_Sam | Restricted content and Kids/Select still need the full questionnaire |
| Managed Pricing (regional pricing + price tests, every ≥ 90 days) | **live** | 2026-06-15 | [DF 4684738](https://devforum.roblox.com/t/managed-pricing-one-system-for-better-pricing-and-earnings-growth/4684738), pearvessel; mirror `production/monetization/regional-pricing` | **Never hard-code prices in UI**: read them from MarketplaceService |
| Shop: passes and products findable outside the game; `MarketplaceService:OpenShop()` | **live** | 2026-09 | [DF 4888425](https://devforum.roblox.com/t/players-can-now-find-in-game-items-outside-your-game/4888425), [DF 4701505](https://devforum.roblox.com/t/introducing-shop-a-personalized-in-game-storefront/4701505) | ProcessReceipt must handle purchases made outside the game |
| US 18+ DevEx rate; R15-only avatar setting required (unless custom rig or no characters) | **live** | 2026-06-08 | DF 4607091 | A design input for the avatar setting |
| Homepage recommendations need a custom 16:9 thumbnail | **live** | 2026-10-19 | [DF 4945086](https://devforum.roblox.com/t/homepage-recommendation-eligibility-now-requires-a-custom-thumbnail/4945086), itsblueberrycoffee | Launch checklist item |
| Creator Store publishing: age check or ID, 2-step verification for model and plugin sellers | policy | 2026-08-26 | [DF 4820095](https://devforum.roblox.com/t/new-requirements-to-publish-to-the-creator-store/4820095), Kairomatic | Affects publishing agent-made plugins or models |
| Terms of Use update (Roblox as merchant of record) | effective 2026-11-01 | 2026-10-01 | [DF 4907620](https://devforum.roblox.com/t/updates-to-the-roblox-terms-of-use-november-2026/4907620) | Re-read before writing sales wording |
| AI-generated content | standing docs: visible AI notice, disclosure in the maturity questionnaire; no 2026 rule found | - | create.roblox.com/docs/generative-AI (not verified) | Games with AI interaction need the notice |
| Deleted accounts: usernames retired | **live** | 2026-09-28 | mirror `production/publishing/RTBF-and-creators` | Key all data by UserId, never username |
| Pre-roll video ads; Wallet and Card | announced | 2026-09-11 | RDC26 DF 4865880 | Not available |

## Analytics (step 9)

| Feature | Status | Date | Source | What it means |
| --- | --- | --- | --- | --- |
| Open Cloud APIs: Analytics Query, Events, Experiments, Thumbnail Personalization | **live** | 2026-08-24 | [DF 4828676](https://devforum.roblox.com/t/new-opencloud-apis-for-analytics-events-experiments-and-thumbnail-personalization/4828676), OrogeneIstari | An analyst agent can read metrics with an owner-made key (`universe.analytics:read`) |
| Custom dashboards; Explore page with calculated metrics | **live** | 2026-05 / 08 | [DF 4844585](https://devforum.roblox.com/t/analytics-custom-dashboards-to-save-organize-and-share-custom-charts/4844585); mirror `production/analytics/custom-dashboards` | Funnel, economy and custom events unchanged; read limits from the mirror |
| Experiments early harm detection | rolling out | 2026-09-28 week | [DF 4907734](https://devforum.roblox.com/t/experiments-catch-experiment-regressions-faster-with-early-harm-detection/4907734) | Faster A/B regression checks |
| Discovery measurement on a new pipeline | **live** | 2026-10-12 | [DF 4930122](https://devforum.roblox.com/t/improved-discovery-measurement-in-creator-analytics/4930122) | Do not compare impressions across 2026-10-12 |
| Roadmap: analytics agent, journey (Sankey) funnels | **planned** (journeys: method in the API reference) | 2026-09-18; reference checked 2026-10-21 | roadmap; mirror `_api-reference/classes/AnalyticsService.yaml:598-656` (`LogJourneyEvent`) | Analytics agent not available. `LogJourneyEvent` exists in the API reference with no guide page; whether the Creator Hub chart is live is not confirmed |

## Not verified or contradictory

- Release-note bodies 738-743 were not readable; Studio or Luau items there may be missing from this note.
- Playtest Agent: beta in April; no graduation post found. Frustum Streaming: roadmap said "late 2026", the post says released.
- Rows marked "recap" or "post not read" rely on a staff weekly recap or the API yaml, not the full post.
- No 2026 change found for RemoteEvents or AI content rules. Absence of evidence, not proof. Paid random items: the 2026-05-26 clarification (row above, DF 4654622) is the only 2026 change found.
