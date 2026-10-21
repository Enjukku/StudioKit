> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Reference for `film-craft`. Engine facts: `knowledge/reference/film/fact-check-roblox-runtime.md` (FR, 33 rows checked 2026-10-21 against the docs mirror and live pages; row ids FC-nn). Studio contract (O): the owner's paper, N2 RT, TC, CP rows. Facts marked "status as of 2026-10-21" change: re-check before use. The film director writes the scene data and this contract; engineering builds the player (J015-D7).

# Roblox assembly: camera, cues, readiness, UI, exits

## 1. Which runtime
| Option | Use when | Facts |
| --- | --- | --- |
| Studio cutscene player (engineering builds it once per game or kit) | A private, camera-driven, skippable story scene; boss intros; in-game camera moments | Plays the `.luau` data module the shot-list tool writes (`references/shot-list-format.md`) |
| Roblox **Event Sequencer** module | Shared, multi-scene live events where everyone sees one server timeline and late joiners land mid-show (concerts, countdown shows) | Official developer module for "live, cross-server events and cutscenes" (`resources/modules/event-sequencer.md:11`). Scenes, `audio` / `animate` / `tween` / `interval` / `schedule` / `inform` configurations, `SyncToAudio`, seeking for staff only. Its page says nothing about camera, letterbox, subtitles, player skip, streaming readiness or exits. Replace mode (default) rewrites Workspace, Terrain and Lighting; in an existing game use inline mode. FR Event Sequencer section |
| `VideoFrame` (pre-rendered video) | Scenes that need no live player and benefit from offline render | Max two videos playing at once; parent `ScreenGui`, `SurfaceGui` or `BillboardGui`. Upload: beta toggle, 13+ ID-verified uploader, `.mp4`/`.mov`, ≤ 5 min, ≤ 4096x2160, < 3.75 GB, 2,000 Robux per upload, 20 per day (`ui/video-frames.md:17-34`, FR FC-48; status as of 2026-10-21). Upload limits are not length advice. The owner uploads. Audio-in-video and phone playback were never tested in the first game (N4 V-06, V-07): plan a test with the owner before relying on video |
| Moon Animator | Only if its authoring clearly speeds iteration | A third-party animation plugin (named in `avatar/emotes/index.md:55`). Version and exporter not verified (FR FC-46): validate one camera + character + audio export before building on it; keep shot and cue data outside the plugin |

## 2. Camera (facts)
- Each client has its own `Camera` (`Workspace.CurrentCamera`). Set `CameraType = Enum.CameraType.Scriptable` before writing `CFrame`; default camera scripts then stop moving it (FC-20).
- Before taking the camera, store `CameraType`, `CameraSubject`, `FieldOfView` and `FieldOfViewMode`; restore them on every ending (FC-20; restore is a studio rule).
- **Hazard:** setting `Workspace.CurrentCamera` to a new `Camera` destroys other `Camera` objects parented directly to Workspace, and post-effects parented to a camera die with it. Keep spare cameras in a Folder or Model (FC-20).
- `Camera.FieldOfView` is a **vertical** angle in degrees, clamped 1-120, default 70. `Camera.FieldOfViewMode` (default `Vertical`; also `Diagonal`, `MaxAxis`) says which angle stays constant when the viewport is resized; horizontal and vertical FOV are tied by aspect. Set `FieldOfViewMode = Vertical` explicitly for authored shots. Never write "FOV is horizontal" (FC-22..24). FOV uses the fullscreen area, not `ViewportSize` (FC-23).
- Roblox has no focal length or sensor: convert a Blender lens to a vertical angle first (`references/blender-previs.md` §3).
- `Camera.Focus` must be updated every frame while `Scriptable`; it prioritises graphics work near it. It is not a streaming control and not depth of field (FC-21).
- `RunService:BindToRenderStep(name, priority, fn)` is client only; lower priority runs first; equal priority order is random; rendering waits for the callbacks; pass `Enum.RenderPriority.Camera.Value` (200), not the enum; unbind by name (FC-25). Use one binding that writes `CFrame`, `Focus` and `FieldOfView` from the timeline; precompute heavy work elsewhere; never let two scripts race on `CFrame` (studio rule, N2 RT-16).
- Keep intended cuts as cuts: do not smooth every transition (N2 RT-17).
- Avatars vary (`HumanoidDescription` height, width, proportion, head scales): frame with margin and test the supported range (FC N3-FC-05).

## 3. Cues and clocks (facts)
| Clock | Facts | Use |
| --- | --- | --- |
| Scene timeline (our data) | Shot starts and cue times from the `.luau` module, seconds from sequence start | Cuts, subtitles, music structure |
| Animation markers | `track:GetMarkerReachedSignal(markerName)` returns a signal; the handler gets the marker's optional parameter string (FC-27). In Animation Graphs, events carry weight; zero weight silences them; blend and selection nodes can block non-primary events (FC-28) | Pose-linked details: foot contact, hand on a switch, impact accent. Test markers at blend boundaries |
| Server time | `Workspace:GetServerTimeNow()`: the client's smoothed approximation of server Unix time, rate within 0.6 % of the local clock; errors on a disconnected client; "not suitable for things like timed rewards" (FC-31) | Shared scene start: the server sends scene id + a future server-time start |
| Mixer time | `SoundService:GetMixerTime()`: stable, sample-accurate, monotonic seconds; starts at an arbitrary value and differs per machine; not for cross-network sync (FC-32, FC-33) | Local audio scheduling only |

- `AudioPlayer:Play(atTime)` / `:Stop(atTime)`: optional `atTime: double?` on the mixer clock, "sample-accurate, framerate-independent"; with `atTime` they return an `int64?` action id; `AudioPlayer:Cancel(actionId)` cancels a pending action. `IsReady` is read-only and can go false under extreme memory pressure; `TimePosition` is read/write seconds (FC-32, FC-34). Schedule from the client (the mixer clock is per machine). Cross-client accuracy is not documented: no sample-perfect multiplayer claim.
- Shared start (studio method, N2 RT-31, proposal): map the remaining time to the server-time start onto the local mixer clock; never send one client's mixer time to another; a late arrival takes a defined catch-up, wait or fallback path.
- Every cue has a stable id and a policy for pause, seek, skip and replay: a skip does not replay missed explosions or award skipped outcomes (N2 RT-24).
- Animation Graphs run in live experiences since the 2026-07-15 full release; State Machine and Expression nodes were announced as Studio beta on 2026-10-08 and, per that thread's FAQ, work only in Studio. For a shipping cutscene use base graph nodes or plain `AnimationTrack` (FC-29, FC-30; status as of 2026-10-21).

## 4. Effects and light (facts)
- `ParticleEmitter:Emit(count)` bursts (default 16); `Enabled = false` stops new particles but existing ones live until they expire; `Clear()` removes them at once (FC-35). Tag scene-spawned effects with the scene token; on a hard skip stop emission and decide what to clear. Damage stays a server decision.
- Post effects (`Bloom`, `Blur`, `ColorCorrection`, `DepthOfField`, `SunRays`, `ColorGrading`) under `Lighting` affect everyone; under `CurrentCamera` they show to that player only (FC-36). Prefer camera-parented effects for a private scene; snapshot and restore only the properties the scene owns, never overwrite a newer weather or time-of-day controller's state (N2 RT-38).
- `DepthOfFieldEffect` may render differently on low-end devices or settings (FC-37): no story beat depends on blur alone.
- The docs give no universal limit on lights, characters or moving shots for phones; cut unneeded shadow casters and lights and inspect rendering scopes in the MicroProfiler (FC-38). Measure on the supported phones (`performance` skill).

## 5. Streaming and readiness (facts)
- Instance streaming follows the replication focus. `Player:RequestStreamAroundAsync(position: Vector3, timeOut)` yields, is temporary and gives no guarantee; `timeOut = 0` waits effectively forever, so always pass a timeout (FC-39).
- `Player:AddReplicationFocus(part: BasePart)` / `RemoveReplicationFocus(part)` are server only; keep the part to release it; each extra focus adds server work and limits client memory adaptation (FC-39).
- `Player.FrustumStreaming` is a `FrustumStreamingMode` (`Default` = currently `Disabled`, `Enabled`, `Disabled`, `Automatic`), server only. Store the previous value to restore it. `Automatic` can switch on for a far scriptable camera; activation lags; fast moves churn; it does no occlusion culling and does not reduce normal streaming work (FC-40). Not a fix for whip pans to distant sets.
- `ContentProvider:PreloadAsync()` loads referenced assets, not world residency; failures show only in the callback's final `AssetFetchStatus`; the call does not error. It does nothing for `SurfaceAppearance` or `MaterialVariant` (FC-41). Preload essential assets only.
- Readiness contract (studio method, N2 RT-49..51): separate checks for required instances, geometry/textures, animation and sound; prepare the next set before cutting to it; verify named critical actors. If a reveal cannot be ready: the approved close shot, an opaque transition or a story fallback, and controls released safely. Never mark the whole cinematic world persistent to hide a loading bug.

## 6. UI layers and input (facts)
- Letterbox bars: decorative, a non-interactive full-bleed layer; `ScreenGui.ScreenInsets = None` is documented for non-interactive content. Subtitles and Skip: the default `CoreUISafeInsets` (FC-42). Bars do not change the projection: if they cover the action, reframe (N2 RT-13).
- Subtitles: wrap, speaker identity where needed, room for translation, a backing that survives bright frames. `GuiService.PreferredTextSize` is the player's text size; `TextScaled` text ignores it. Read it, never set it (FC-43).
- `GuiService.ReducedMotionEnabled` is the player's reduce-motion preference, described for UI motion; Roblox does not apply it to scripted cameras, so the cutscene reads it and uses the calmer variant itself (FC-44).
- Input Action System: `InputContext` has `Enabled`, `Priority`, `Sink`; higher priority runs first; `Sink` blocks lower matching bindings (FC-45). Give Skip its own context (touch, gamepad, keyboard) that stays enabled while gameplay contexts are off. Contexts govern `InputAction` bindings only; other control scripts are not switched off by them.
- Freecam (Left Shift + P) is a capture and debug tool for owners and editors in playtests, not a player feature (FC-47).

## 7. Endings and teardown (studio contract, N2 TC-01..07; O)
Every run has one terminal reason and one idempotent teardown:
1. Cancel future callbacks, tweens and scheduled audio (`AudioPlayer:Cancel(actionId)`).
2. Disconnect cue listeners; unbind the render step by name.
3. Stop scene-owned tracks and effects (clear or let finish, per cue policy).
4. Server releases streaming requests, replication foci and restores `FrustumStreaming`.
5. Restore camera (`CameraType`, `CameraSubject`, FOV, mode) and input contexts, only if this scene still owns them; never restore a destroyed pre-respawn `Humanoid` or overwrite a newer controller.
6. Remove subtitles and bars; hand audio mix back to its owner.

| Ending | Must happen |
| --- | --- |
| Finish | Final pose evaluated; control back at an authored safe view; only the permitted server transition requested |
| Skip | Same authorised story outcome where designed, no transient cues replayed; shared scenes follow the stated skip policy; repeated presses = one result |
| Failure | Missing asset, removed actor, camera taken over, death or respawn, interrupted teleport or a newer scene → the defined fallback + teardown; never a frozen player behind a black overlay |
| Disconnect | The server releases participants and foci even without a client completion event; rejoin follows the replay / resume / skip rule; no reward inferred from a broken presentation |

**Server authority (studio rule on documented facts, FC-49, N3-FC-01):** the server owns game state and validates every client request; a local cutscene finishing never grants a reward, a boss defeat, a teleport or a trade.

## 8. Review captures (N2 CP-01..17; O)
Capture each, with build, device, viewport, shot id, observed event, expected behaviour: normal finish; skip during each major cue; repeated skip; skip during loading; missing or denied audio; missing streamed actor; fast distant cut; low quality setting; resized and portrait viewport; large text; reduced motion; touch and gamepad; respawn mid-scene; two clients; late join. Record camera ownership, connections and instances left, server state, and what is seen and heard. Pass needs correct story understanding and restored control, not just an empty Output.
