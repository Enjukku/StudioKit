> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Revised by J018 maker feature-builder · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (§4 open probes for presentation wiring). Surprises from the first game's rework study (`knowledge/reference/engineering/rework/` git-a E-rows, git-b EG-rows, logs EL-rows, records RG-rows); each was found by a measurement or a probe. Docs lines checked in the mirror where named.

# Studio probes: ask the engine, then build

## 1. When to probe
Your design depends on an engine behaviour, and the docs page does not state it (timing, ordering, sleep, replication, query bounds, what a property write does). Or two docs pages disagree. Or the behaviour changed in a recent release. A probe costs minutes; the first game's guesses cost 3-4 rounds each.

## 2. How
1. **One question.** "Does writing Anchored on a resting part wake its neighbours?" Not "test the physics".
2. **Smallest scene.** An empty Baseplate place; create only the parts the question needs.
3. **Under 30 lines.** `execute_luau` in Edit for API and compile questions; a play-test (`start_stop_play`, then `execute_luau` on Server or Client) for runtime, replication and physics questions. Yield with `task.wait()` in loops (`studio-mcp` skill).
4. **Positive control.** Include a case where you know the answer, so a broken probe cannot pass (the first game discarded one probe that had no control).
5. **Print numbers, not opinions.** Counts, velocities, timings, states. Run it 3 times if physics is involved; report all three.
6. **Clean up** the probe parts and scripts.
7. **Cite it** in the hand-back: the question, the code (or its path), the output, the Studio build. Label it MCP-verified.

## 3. Behaviours that surprised the first game (universal ones)
| Area | Wrong assumption | What the engine did | Evidence |
| --- | --- | --- | --- |
| Spawn | the character's position is valid at `CharacterAdded` | Roblox places the character after the event; read RespawnLocation, then the server position after the character is in Workspace and one Heartbeat has passed | git-a E1, A17 |
| Camera | multiplying a recoil offset into `camera.CFrame` is safe | the default camera reads `CFrame` back as its base, so the offset accumulated (about 10° up per shot); apply a per-frame offset and remove it the next frame | git-a E2 |
| Sleep | a slow hinged door closes on a spring | the engine put the slow leaf to sleep about 13° short; a servo closed it | git-a E5, A11 |
| Ownership | a client character can push a server-owned motor leaf open | the client stopped its character at the leaf; the server had to swing it | git-a E6 |
| Replication | replacing an assembly's root Part is harmless | the new root had no replication history; clients held the old pose, then jumped 3.6-4.6 studs; keep one root, re-assert `SetNetworkOwner(nil)` after a Part joins a free assembly | git-a E7, A01 |
| Stepping | a VectorForce lift acts once | under Adaptive stepping the force was applied about 4× after a landing (26 of 144 pairs launched; 0 of 144 under Fixed) | git-a E4, A03 |
| Movers | a LinearVelocity with a target has no side effects | it is an actuated joint the engine later sleeps; slow bodies crept before resting | git-a E15 |
| Queries | an overlap query sees every Part | default-group params never saw parts in a group that does not collide with Default; set the CollisionGroup on the params | git-a E3 |
| Queries | a Lua box test of CFrame × Size equals `GetPartBoundsInBox` | engine bounds of round shapes are tighter: 158 wrong verdicts; OverlapParams.Tolerance adds up to 0.05 studs | git-b EG3, B17 |
| Sleep | anchoring and un-anchoring rubble is a safe way to "rest" it | any physics property write wakes the assembly (physics/sleep-system.md, additional wake situations); 37-69 % of rests were undone within 0.1 s | git-b EG10, logs EL4 |
| Replication | a server folder of invisible collider Parts in Workspace is free | every Workspace descendant replicates to every client, with every add, remove and move | git-b EG4 |
| Placement | shared modules and compiled content belong in ReplicatedStorage | it downloads to every client and can be decompiled (5.2 MB data, 1.56 MB server code) | git-b EG5, records R02 |
| Properties | `CollisionFidelity` can be set by a content rule at run time | it is not script-settable at run time (authoring only) | git-b EG6; factcheck-engine §3 item 13 |
| Classes | effect classes are `Bloom`, `ColorCorrection` | they are `BloomEffect`, `ColorCorrectionEffect`, `SunRaysEffect`, `DepthOfFieldEffect`; check every class name in `_api-reference/classes/` | git-b EG1, B08 |
| Contacts | `BindToCollisionSummaries` can feed contact forces | it errored "not enabled" on 2026-10-04 and was reported enabled by 2026-10-09: a flag changed under the project; probe before relying on it | git-a E12, logs EL2, records RG1 |
| Studio | two Studio windows on one place can be driven by two agents | they do not work together: one instance, one driver | git-b EG7 |
| Measuring | Studio numbers compare fairly in the background; Play Solo numbers are the game's | a background Studio throttles; Play Solo runs server and client in one process with 130-520 ms stalls even when idle; scanning LogService during a run added 140-1,800 ms frames | git-b EG8, logs EL9, git-a E14, records RG4 |
| Measuring | offline Luau CLI speed-ups show up in Studio | 2-3.8× CLI gains were invisible over Studio noise; only memory and call-count cuts showed | git-b EG9, records RG5 |
| Measuring | the device emulator shows phone cost | it changes screen size, density and input only; no CPU, GPU or memory emulation | logs EL10; `performance` F-11 |
| Measuring | client Heartbeat rate is rendered FPS | Heartbeat measures update frequency; one fresh Play gave 0 RenderStepped samples vs 300 Heartbeat in 5 s | logs EL3 |
| Profiler | a profiler label's total is one real cost | recursion was counted twice (154.7 ms shown, about 75-80 ms real) | records RG6 |
| MCP | `require` of a project module from an MCP command reaches the live service | it returned a separate, uninitialised copy; use attribute hooks or Studio-only observers | logs EL5 |
| MCP | `screen_capture` camera arguments work during Play | the player camera scripts overrode them; set the camera to Scriptable and move it first | logs EL6 |
| Input | a `MoveTo` probe carries walking intent | it did not; observe the real client move | logs EL7, records RG3 |
| Streaming | a screenshot shows the whole stage from anywhere | the client draws only what has streamed in near the character | git-c G7 |

## 4. Open probes for presentation wiring (run once per game before relying on them; record the output)
| Question | Why it matters | Probe |
| --- | --- | --- |
| Does an attribute change set from `execute_luau` reach the game's hook script in the same play-test, on Server and on Client? | the test hooks (`presentation.md` §9) depend on it | set `TestHooks.FxLog = true`, read the hook's acknowledgement line in Output |
| Can `execute_luau` (plugin context) write `settings().Network.InboundNetworkMinDelayMs` before Play, and does the delay show in a remote round trip? | the optional slow-network check; the property is PluginSecurity (Y/NetworkSettings.yaml:173-197) | Edit: set 300; Play; log send and result `os.clock` on the client; positive control: 0 |
| Where must a camera shake run so the default camera does not overwrite it or accumulate it? | shake that drifts was the first game's recoil bug (§3 Camera row) | `BindToRenderStep` at `Enum.RenderPriority.Camera.Value + 1`: apply a 2° offset one frame, remove it the next; read `CurrentCamera.CFrame` over 60 frames: no drift |
| Do a marker's VFX emit and cue play started in one handler land in the same rendered frame? | the sync rule can only be met from one trigger | log `f` for both on 20 hits at 60 and 30 fps caps |
| Does `ParticleEmitter.TimeScale = 0` hold a frame still for `screen_capture` during Play? | key stills of an effect | freeze, capture twice 0.5 s apart, compare; restore 1 |
| Does `Model:ScaleTo` scale emitter sizes with the model? | one scale factor per effect | scale a model with one emitter by 2, read `Size` keypoints |
| Does `GuiService.ReducedMotionEnabled` signal a change while the game runs (`GetPropertyChangedSignal`)? | the comfort module reads it once per screen or effect until this is known | Play; connect the signal; toggle Reduce Motion in the in-game settings; log the signal; positive control: `PreferredTransparency`'s signal, which the docs show |
| How many `print` lines per second does Output keep in a burst before `get_console_output` drops or merges them? | repetition counts (`presentation.md` §11) | print 200 numbered lines in one second; read history; count gaps |
| In the Device Simulator, does an `execute_luau` read on Client see the emulated screen, and does a ScreenGui under `CoreUISafeInsets` report the inset area as its own `AbsolutePosition` and `AbsoluteSize`? | the UI bounds and `TextFits` read (`ui-basics` U-S03) | Play at the smallest phone size; read `workspace.CurrentCamera.ViewportSize` and the ScreenGui's rectangle; positive control: a second ScreenGui with `ScreenInsets` None reports the full viewport |
| Does `AdjustSpeed(0)` on another player's replicated character track hold on the observing client, and does the owning client's own pause replicate to everyone? | the hit-stop on the target's client and the bystander rule (`presentation.md` §4); the docs state only that clips started on the owning client replicate (Y/Animator.yaml:217-232) | two-client session (the lead batches it): on client A pause A's own playing track for 2 s and read its `TimePosition` on client B three times 0.5 s apart; then on B pause A's track as B sees it and read `TimePosition` on B and on A; positive control: the same reads at speed 1 advance |
