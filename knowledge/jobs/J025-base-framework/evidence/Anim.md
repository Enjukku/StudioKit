---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J025-B5
supersedes: []
---
> Author: feature-builder · claude-opus-5-5 · medium · 2026-10-24

# Anim: Q1-Q9 evidence (contracts/Anim.md as frozen after F10)
Files (repo `roblox-game-framework`, uncommitted): `src/Anim/init.luau` (334 lines), `Anim.spec.luau` (25 Lune specs), `Anim.engine.spec.luau` (Jest, written, NOT RUN), `test/Fakes.luau`.

**Red run first** (stub `init.luau` returning no API, 2026-10-24): `lune run tools/spec/run.luau src/Anim` → `specs: 1 files, 0 passed, 25 failed`, each `attempt to call a nil value` (A-T7: `expected an error containing "must be in Workspace", got ... attempt to call a nil value`). Green after code: `25 passed, 0 failed`.

| Q | Result | Evidence |
| --- | --- | --- |
| Q1 | PASS | 10 public: `new`, `observe`, `preload` + `play/stop/isPlaying/onMarker/destroy` + observer `onMarker/destroy`. Spec-only: `_seams` (Instance.new, PreloadAsync, warn: Lune has no `Instance`/`game`), `_debugCounts` |
| Q2 | PASS (gate-verified, Anim files) | every file `--!strict`; luau-lsp: 0 errors in `src/Anim/*` (both analyzer runs); `grep ":: any" src/Anim/init.luau` = 0; stylua and selene clean on `src/Anim` |
| Q3 | PASS | row table below; 13 planted faults, 13 caught, 0 false alarms on the correct build |
| Q4 | PASS | failure rows: empty id, unknown id, LoadAnimation throws, preload fails, Animator destroyed, outside Workspace (rows A-T6, A-T7, A-T9, A-T10) |
| Q5 | PASS (Lune) | `Q5 1,000 player and observer cycles leave 0 connections and 0 entries`: half via `destroy`, half via the Animator's `Destroying`; fake connection counter back to start, `_debugCounts` delta `{owners=0,tracks=0,subscriptions=0}`. Engine half: A-T6 Jest, NOT RUN |
| Q6 | PASS offline; engine not verified | cached `play` 0.18 / 0.26 / 0.19 µs per call over 100,000 calls (3 runs, Lune `os.clock`, fake track; budget 30 µs); heap growth 0 KB over 10,000 calls (`gcinfo`, max growth). Hot paths (`play`, `isPlaying`, `stop`, observer `onPlayed`) allocate nothing; allocations only at load, `onMarker` (one closure + subscription), first warn |
| Q7 | n/a | no client input (contract "Server-authority checks: n/a"); markers presentation only (A7) |
| Q8 | PASS | `Animator.yaml:191-213` LoadAnimation (new track each call, needs Workspace), `:155-169` GetTrackByAnimationId (P4: nil, not a cache), `:217-232` replication, `:295` AnimationPlayed; `AnimationTrack.yaml:409` GetMarkerReachedSignal; `animation/events.md:65-66`; `ContentProvider.yaml:21`; `Instance.yaml:2407` Destroying. Own code still needed: the engine caches no track per id and replays reuse track objects (P4 items 4-5) |
| Q9 | PASS | `Q9 the contract's usage example runs`: the CharacterAdded body verbatim on fakes |

## Test row → spec (Lune unless marked)
| Row | Spec name (prefix) | Planted fault that turned it red |
| --- | --- | --- |
| A-T1 | `A-T1 play the same id 100 times…`, `A-T1 a track loaded by onMarker is the track play reuses`; Jest `A-T1 …one playing track` (NOT RUN) | F1 cache check removed → 10 red |
| A-T2 | `A-T2 Priority and Looped are set…before Play…`, `A-T2 speed defaults to 1…` | F4 Priority set after Play → A-T2, A4 red |
| A-T3 | `A-T3 (Lune half) onMarker before play connects before Play…`; Jest `A-T3 a marker connected before Play fires once per pass with its param string` (NOT RUN) | n/a offline (connect order is a fake read) |
| A3 | `A3 the disconnect function removes only its own handler and is safe twice` | — |
| A-T4 | `A-T4 onMarker with a marker name not in the clip table errors (new and observe)` | F5 marker check off → red |
| A-T5 / A4 | `A-T5 a looped clip played twice…`, `A4 a playing non-looped clip played again restarts…` | F7 looped restart → A-T5, Q6 red |
| A-T6 | `A-T6 (Lune half) destroy…`, `A-T6 (Lune half) the Animator's Destroying…`; Jest `A-T6 respawn x20…` (NOT RUN) | F3 no janitor cleanup → 3 red |
| A-T7 | `A-T7 an Animator outside Workspace: new errors and connects nothing` | F12 check off → red |
| A-T8 | `A-T8 (Lune half) observe matches a played track by asset id…`; Jest multi-client `A-T11/A-T8 server…` + `…client…` (NOT RUN) | — |
| A-T9 | `A-T9 empty asset id: play returns nil, one warn for 10 calls…`, `A-T9 an unknown clip id errors in every method and in preload` | F13 warn every call → red |
| A-T10 | `A-T10 LoadAnimation throws…do not retry`, `A-T10 preload failing is logged and play still loads on demand…` | F6 failed load retried → red |
| A-T11 (P4 trap) | `A-T11 P4 trap: the same track object played 3 times fires the handler once per pass, not 1x/2x/3x`; `A3b a handler added after a track was seen…`; Jest multi-client (NOT RUN) | F2 per-track dedupe off → A-T11, A3b red (per pass 1/2/3) |
| A-T12 | `A-T12 no code path reads Length…` | F10 Length read in play → red |
| A-T13 | `A-T13 observe never calls LoadAnimation; destroy disconnects…`, `A-T13 the watched Animator's Destroying cleans the observer` | F8 observe loads → red; F11 subs kept → 3 red |
| Q5 / Q6 / Q9 | `Q5 1,000…`, `Q6 a cached play costs at most 30 us and allocates nothing`, `Q9 the contract's usage example runs` | F9 one table per play → Q6 red |

Planted-fault method: each fault applied alone to `init.luau` by a scratch script, `lune run tools/spec/run.luau src/Anim`, file restored (`restored: 25 passed, 0 failed`). Tests take their own count baseline, so one red test does not redden the next.

## Engine rows (Jest, written, NOT RUN: no Studio window, brief rule)
`src/Anim/Anim.engine.spec.luau`: lane 1 (A-T1, A-T3, A-T6) runs only in a play test's Server DM (the Animator must step); lane 2 (A-T8, A-T11, 1 client) skipped unless `workspace.AnimScenario == "observe"`; recipe in the file header (start the Server run in `task.spawn`, then the Client run). Rig: AnimationController + anchored root part, clip from `KeyframeSequenceProvider:RegisterKeyframeSequence` (P4 used an R15 rig; whether markers fire on a pose-less rig is unproven).

## Open risks
- A5 on respawn needs the old character Destroyed: `Workspace.PlayerCharacterDestroyBehavior` (`Workspace.yaml:800-808`, NotScriptable) must be `Enabled` in the template, or Destroying may never fire and the player leaks until `destroy`. Ticket to step 7.
- Observer matches `track.Animation.AnimationId` to `clip.assetId` by exact string; a client-side id format other than the table's (e.g. `http://www.roblox.com/asset/?id=`) would not match. Lane-2 engine run proves it with temporary ids only; a real uploaded id is not tested.
- A track already playing when `observe` starts (an NPC streams in mid-clip) gets its markers from its next pass (no `GetPlayingAnimationTracks` scan; not in the contract).
