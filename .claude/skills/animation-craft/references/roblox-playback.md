> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `animation-craft`. Facts: `knowledge/reference/animation/fact-check-roblox-runtime.md` (RA rows; mirror revision 7400643 refreshed 2026-10-20, forum posts dated), `knowledge/reference/rigging/fact-check-roblox.md` (RR rows), technique sheet (TC). Re-sync the mirror (`python tools/sync_roblox_docs.py`) before relying on a feature newer than the mirror (RA extra findings). Studio work: `studio-mcp` skill, one driver per Studio instance, the test place only. Revised by J018 maker animator · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (§9 hit-stop playback, §10 judging in the game; facts checked in the docs mirror: `AnimationTrack.yaml`, `GuiService.yaml`, `production/publishing/accessibility.md`).

# Roblox: import, publish, play

## 1. Import and publish
| Route | Use | Facts |
| --- | --- | --- |
| Animation Editor → Import → From File | a clip for a standard R15 rig (exact R15 joint names) | RA40 |
| Animation Clip Editor importer | several clips in one FBX or glTF, saved locally, edited and previewed before upload (GA 2026-03-31, forum-dated) | RA40; AP:729 |
| Import 3D | rig + clips, uploads directly | RA40; the rig import itself is the rigger's (`rigging-craft`) |
- Saving locally is not publishing; a clip needs an uploaded asset id before runtime use (AP:729). Group-owned experiences publish under the group (AP:821).
- Who may play an animation asset is not documented in the mirror; forum posts (2025) and an open bug (March 2026) are the only sources (RA36): test it in the target experience, label forum-reported.
- Avatar animations play in place: mute root translation before export (RA41). Native root motion is not released (RR39-RR41).
- KeyframeSequence is what the editor saves; CurveAnimation is needed for emotes and animation packs and matches joints by folder name, allows partial hierarchies and can carry FaceControls curves; quaternion-to-Euler conversion cannot be undone (RA31, RA32).
- Default avatar clips: override the Animate script's AnimationIds from a server Script, or use Avatar Settings animation packs and custom clips; a replacement default clip needs its last keyframe named `End` (RA37, RA39).

## 2. Who plays it (replication)
| Case | Where the Animator lives and who calls Play | Fact |
| --- | --- | --- |
| Player character | the Character's Animator (server-created); the owning client may start tracks and they replicate | RA02 |
| NPC or prop that others must see | load and start on the server | RA02 |
| Cosmetic crowds, decoration, local-only visuals | a client-created Animator: never replicates, by design | RA02, RA42, TC10 |
| Client visuals of server-owned NPCs | sync high-level state and time explicitly; never a hitbox | AP:759 |
- `Animator:LoadAnimation` only (the Humanoid and AnimationController versions are deprecated); the Animator must be in Workspace first; each call makes a new track: load once per Animator and cache, or `GetTrackByAnimationId` (RA03-RA05).
- Preloading an Animation with `ContentProvider:PreloadAsync` has no doc line or sample (RA34): test it; read each asset's status in the callback (AP:783).

## 3. Priority, weight, fade, speed
- Priority per joint, high to low: Action4, Action3, Action2, Action, Movement, Idle, Core. Compare by name, never enum number. Default and catalog clips play at Core, so a custom clip at Idle or above overrides them joint by joint (RA09, RA10).
- Prefer priority over weight; tracks of equal priority blend by normalized weight (RA09, RA13).
- `Play(fadeTime, weight, speed)` defaults 0.1 s, 1, 1; `AdjustWeight` and `Stop` fade 0.1 s by default (RA12-RA14). Write the fade per transition in the animation set (design value or measured, never "default because default").
- After `Stop()`, `Play()` again before adjusting; `Ended` (not `Stopped`) says the influence is gone; avoid `Stop(0)` on Motor6Ds with MaxVelocity 0 (RA14, RA15).
- `AdjustSpeed`: negative plays backward, 0 pauses; real duration = Length / Speed; `Length` is 0 until loaded; `TimePosition` settable only while playing (RA16, RA17).
- Loops: the runtime does not blend the last key into the first; the last key repeats the first pose (RA18).
- A cap on concurrently playing tracks exists and warns; the figure (64, 2026 forum) is undocumented; 256 per Animator appeared in 2023 posts (RA27). Never a budget; a warning means leaked or duplicate tracks.

## 4. Markers and events
- Author markers on the Animation Events bar (or confirm they survived import, C-17); read with `track:GetMarkerReachedSignal(name)`, connected **before** `Play()`; payload in the Parameter string (RA19, RA20). `KeyframeReached` is deprecated; `GetKeyframeMarkerReached` in `KeyframeMarker.yaml` does not exist (RA21).
- Under throttling or low frame rate, marker timing is undocumented (RA22): cosmetic cues only. Server gameplay uses its own clock and validation (AP:833).
- Test markers at low frame rate, late join, network delay, streaming in and out, interruption and looping (AP:833). Read event times from the Output log and compare with the timing list (one clock; label MCP-verified).

## 5. Procedural layers, IK, joints
- R15 avatar joints are AnimationConstraints when the avatar joint upgrade is on; Motor6D remains for mechanical rigs; never write `RigAttachment.CFrame` (RA28-RA30).
- Layer procedural motion into `Transform` during PreSimulation, after the Animator has evaluated; skip it when `Animator.EvaluationThrottled` is true (RA24, RA29).
- `PreferLodEnabled=false`: the reference says full fidelity, an April 2026 forum post says throttling is always on; do not state either, test on a device (RA25).
- IKControl: Type, EndEffector, Target, ChainRoot; off with `Enabled=false` (weight 0 leaves smoothing and pole effects) (RA33). Use runtime IK for visible contact fixes only (AP:767).

## 6. Animation Graphs
Publish the graph, load it like a clip, drive it with `SetParameter` (RA38). Graphs are released; State Machines and Expressions are a Studio-only beta: shipping content does not depend on them (RR43, AP:801). A 2026 forum report showed retained memory after graph tracks on a phone: add spawn, despawn and respawn memory tests before using graphs at scale (AP:805, forum).

## 7. Lifecycle and memory
- Keep reusable tracks; stop them; destroy on teardown; release script references and connections so animation memory can unload; strip saved animation metadata from shipped or cloned rigs (RA42, RA43). Destroying a track is not proof that memory returns (AP:763).
- Test fresh load, concurrent blends, death and respawn, cancellation and repeated spawn on a real phone (AP:870).

## 8. Doc traps (mirror revision 7400643)
`walkTrack.isPlaying` in a sample should be `IsPlaying` (RA46); `GetKeyframeMarkerReached` does not exist (RA21); the editor's "30 fps" timeline is the authoring display, not proof of the runtime rate (RA44).

## 9. Hit-stop playback
- A hit-stop is `AnimationTrack:AdjustSpeed(0)` on the attacker's track (and the animated target's) for the stop's length, then the previous speed restored; the hit's own particles freeze with `ParticleEmitter.TimeScale = 0` and are restored the same way. Physics, debris, other players and server results keep running: there is no global time scale, and the server never pauses.
- The builder writes it, triggered by the confirmed hit; you supply the freeze frame (the contact pose, named in the timing list) and check in a capture that the frozen frame is that pose. Lengths are game values (`animation-design` → `references/game-timing.md` §5).

## 10. Judging in the game
- Captures: Studio MCP play mode at the game camera, the phone viewport (the capture resampled to the floor phone's screen size from the game profile: a one-line Pillow resize, or `python tools/art/look_check.py thumb <capture> --size <WxH> --box ...` around the subject to also re-measure its value against the surroundings; with `--box` the subject is the rectangle, so silhouette numbers come from the black-fill renders or from `--mask` drawn from the effects-hidden capture), in the real place, with effects, other players and HUD on; then the same moment with the effects hidden and a grayscale copy (a one-line image conversion). These are stills: timing comes from the Output log and a known capture rate, never from one still.
- Sound sync cannot be judged from MCP stills; it is "not verified" unless captured with audio on the target device (phone speaker and Bluetooth differ).
- Reduced motion: `GuiService.ReducedMotionEnabled` reflects the player's toggle and code reads it (tweens snap to time 0 or fade). Test the clip's read with the game's shake, flashes and camera effects off; the tell and the contact must still read.
- Attempt vs outcome: in the test place, have the builder's test hook reject a hit; the confirmed-hit reaction, freeze and celebration must not play.
