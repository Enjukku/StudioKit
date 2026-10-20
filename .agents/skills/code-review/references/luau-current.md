> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Facts extracted by a researcher agent (claude-sonnet-5-5, medium) from the docs mirror (upstream 7400643), luau.org and luau-lang releases; deprecations spot-checked by the orchestrator in the API yaml. Paths relative to `knowledge/external/roblox-creator-docs/`; Y = `_api-reference/classes/`, G = `_api-reference/globals/`, L = `_api-reference/libraries/`. **D** = marked deprecated in the API reference (a review finding). **S** = superseded practice (advice, not an error).

# Current Luau for Roblox (2026)

Formatting and lint are the tools' job (StyLua, selene, Luau-LSP). This page lists what models get wrong.

## A. Outdated habit → current
| Habit | Use instead | | Source |
| --- | --- | --- | --- |
| `wait(n)`, `delay(n, f)`, `spawn(f)` | `task.wait(n)`, `task.delay(n, f, ...)`, `task.defer(f, ...)` (old non-immediate timing) or `task.spawn` (run now) | D | G/RobloxGlobals.yaml:117-121,244-249,400-404; scripting/scheduler.md:23-30 |
| `ypcall` | `pcall` | D | G/RobloxGlobals.yaml:428 |
| `tick()` | `os.clock()` for timing, `os.time()` / `DateTime` for wall time, `time()` for game time | S | G/RobloxGlobals.yaml:274-279 |
| `getfenv` / `setfenv` | `debug.info`; they also disable optimisation and native code | D | G/LuaGlobals.yaml:180-187,745-751 |
| `table.foreach`, `table.getn` | `for k, v in t do`, `#t` | D | L/table.yaml:204-282 |
| `math.pow(x, y)` | `x ^ y` | S | L/math.yaml:684 |
| lowercase members: `:clone()`, `:destroy()`, `:findFirstChild()`, `:getChildren()`, `.childAdded`, `:connect()`, `Players.localPlayer`, `Player.userId` … | PascalCase (`:Clone()`, `:Destroy()`, `:Connect()` …) | D | Y/Instance.yaml; Y/Players.yaml; Y/Player.yaml |
| `Instance:Remove()` | `:Destroy()` (or `Parent = nil` to detach) | D | Y/Instance.yaml:1988-2008 |
| `Humanoid:LoadAnimation()` | `Animator:LoadAnimation()` | D | Y/Humanoid.yaml:2047-2050 |
| `Model:SetPrimaryPartCFrame`, `GetPrimaryPartCFrame`, `GetModelSize` | `PivotTo`, `GetPivot`, `GetExtentsSize` / `GetBoundingBox` | D | Y/Model.yaml:400-481,785-809 |
| `BreakJoints`, `MakeJoints` | `WeldConstraint`, `HingeConstraint` | D | Y/Model.yaml:563; Y/BasePart.yaml:2983 |
| `BodyVelocity`, `BodyGyro`, `BodyPosition`, `BodyAngularVelocity`, `BodyForce`/`BodyThrust`, `RocketPropulsion` | `LinearVelocity`, `AlignOrientation`, `AlignPosition`, `AngularVelocity`, `VectorForce`, `LineForce` | D | Y/BodyMover.yaml and each class; physics/mover-constraints.md |
| `part.Velocity`, `RotVelocity` | `AssemblyLinearVelocity`, `AssemblyAngularVelocity` | D | Y/BasePart.yaml:1816,2144 |
| `Friction`, `Elasticity` on parts | `CustomPhysicalProperties` | D | Y/BasePart.yaml:895-992 |
| Non-async calls renamed to `...Async`: `MarketplaceService:GetProductInfo`, `PlayerOwnsAsset`, `PlayerOwnsBundle`; `Player:LoadCharacter`, `IsFriendsWith`, `IsInGroup`; `Players:GetHumanoidDescriptionFromUserId`, `CreateHumanoidModelFromUserId`; `Humanoid:ApplyDescription`, `PlayEmote`; `TeleportService:ReserveServer` | the `...Async` version (check the yaml: `Player:GetRankInGroupAsync` itself is deprecated in favour of `GroupService:GetRolesInGroupAsync`) | D | Y/MarketplaceService.yaml:239-272,1156,1233; Y/Player.yaml:1386-2328; Y/Players.yaml; Y/Humanoid.yaml; Y/TeleportService.yaml:369 |
| `TeleportService:Teleport`, `TeleportToPlaceInstance`, `TeleportToPrivateServer`, `TeleportPartyAsync` | `TeleportService:TeleportAsync` on the server | D | Y/TeleportService.yaml:666-1012 |
| `Chat` service | `TextChatService` | D | Y/Chat.yaml |
| `PhysicsService` collision groups | per-world groups on `WorldRoot` | D | Y/PhysicsService.yaml |
| `Hint`, `Message`, `Hat`, `HopperBin`, `CustomEvent` | `TextLabel`, `Accessory`, `Tool`, `BindableEvent` | D | each class yaml |
| `Workspace.FilteringEnabled` | nothing: always on, the property does nothing | D | Y/Workspace.yaml:48 |
| `Mouse.KeyDown/KeyUp`, `Mouse.hit` | `UserInputService` or the Input Action System (`InputAction`) | D | Y/Mouse.yaml; input/input-action-system.md |
| Connect then Disconnect in the handler | `signal:Once(fn)` | S | scripting/events/deferred.md:74-89 |

## B. Language features
| Feature | Status | Source |
| --- | --- | --- |
| Type annotations, `export type`, generics, `typeof` in types, `::` casts, unions, intersections, variadics | live | luau/type-checking.md:46-354 |
| String interpolation `` `x = {x}` ``, `for k, v in t do`, `+=` and other compound assignments, `//` floor division, `continue`, if-then-else expressions | live | luau/type-checking.md:184-349; luau.org/syntax |
| `--!native`, `@native`; `@deprecated` attribute | live | luau/native-code-gen.md:17-34; luau.org/attributes |
| `signal:Once`, `ConnectParallel`, `coroutine.finally` | live | _api-reference/datatypes/RBXScriptSignal.yaml:44-98; L/coroutine.yaml:211-259 |
| require by string (`./`, `../`, `@self/`, `@game/`) | live; errors if the module does not exist yet (no waiting) | G/LuaGlobals.yaml:616-633 |
| `buffer`, `vector`, `utf8`, `bit32`; `math.lerp`, `math.map`, `table.clone`, `table.create` | live | L/*.yaml |
| `if local` / `if const` | **Studio beta** (2026-10-06): do not ship | DF 4918297 (jjtangerine) |
| Exact tables, classes, integer types | **experimental in open-source Luau**: do not use | github.com/luau-lang/luau releases 0.737-0.743 (2026-09/10) |

## C. Types
- Modes: `--!strict`, `--!nonstrict`, `--!nocheck` on line 1; the place default is `Workspace.LuauTypeCheckMode`. Types are checked while editing only; they never protect a live game (`luau/type-checking.md:27-31`).
- New type solver: default since 2025-11-20 for nonstrict and nocheck; places with strict scripts stay on the old solver unless `Workspace.UseNewLuauTypeSolver = Enabled`; strict on the new solver is still being polished (DF 4084991, 2025-11-20). The game profile records the choice.
- Module boundaries: `export type` the public shapes; annotate every exported function's parameters and returns; an untyped returned table leaks `any`. `x :: any` silences checks: only at true boundaries, with a comment.
- `typeof(v)` gives Roblox types (`"Vector3"`); `type(v)` says `"userdata"` (G/RobloxGlobals.yaml:313-316). Runtime checks on client input use `typeof`.
- Annotate `Vector3` parameters in native code; a mistyped call de-optimises it (luau/native-code-gen.md:62-86).

## D. Concurrency
- `task.spawn` runs now; `task.defer` runs at the end of the current step; `task.delay(n)` after n seconds on Heartbeat; `task.wait` returns elapsed time; `task.cancel` cannot cancel the running thread (L/task.yaml:22-256).
- Callbacks that must not yield: `UpdateAsync` transforms (Y/GlobalDataStore.yaml:434), ContextActionService handlers (treated as sink), anything a library documents as non-yielding.
- Deferred signals (`Workspace.SignalBehavior = Deferred`, the future default): never fire an event and immediately read state its handler sets; `Disconnect` drops pending calls; re-entrancy limit 10 (scripting/events/deferred.md:11-89).

## E. Modules and scripts
- A module runs once per side and is cached; a shared module required on server and client runs twice with separate state (scripting/module.md:85-87).
- Circular requires error ("required recursively"): fix the structure (`architecture` R-08), not with a delayed require (scripting/module.md:29-31).
- Roblox's recommendation: one `Script` with `RunContext = Client` in ReplicatedStorage and one with `RunContext = Server` in ServerScriptService; everything else in ModuleScripts (scripting/locations.md:36-40). Set `RunContext` explicitly in distributed models. A game may keep a StarterPlayerScripts entry instead; record it in the overlay.
