> Author: J018 maker qa-lead · claude-opus-5-5 · high · 2026-10-22. Part of `testing`; built also from the owner's Riot transcripts (J018). Examples, not rules: the rules are `SKILL.md` §3-§6 and `player-facing.md`. Numbers marked PROPOSAL are starting values a test or the owner may change. Repair round 1 after the stage 3 review (J018 maker qa-lead · claude-opus-5-5 · high · 2026-10-22): hook names, stills budget, fixed attacker for the tell; repair round 2 (same tag): range read, clarity levels, spec-only rates, no camera on repeats.

# Worked trace tables

Each example shows the player-facing rows next to the ordinary rows, the hooks asked for at plan time and the honest end. Columns shortened; a real table also carries lane, data and input label per row.

## 1. Ground slam (an enemy ability with a danger ring)
Sources at plan time: feature contract rev2 (events `slam_tell`, `slam_contact`, `slam_end`), hazard row "slam: 30 damage once inside radius 12 studs; no damage after `slam_end`", timing list rev3 (tell 0.8 s), VFX read card rev2 (ring radius field `Slam.radius`, reduced variant: steady glow plus fill countdown), sound event list rev1.
Hooks asked for (builder names): `DebugShape` from `Slam.radius`; `Trigger`; `FxLog`; `Viewer` = bystander; `Clarity`; `Reduced`; `Set` for the skin.
| Row | Check | Oracle | Conditions |
| --- | --- | --- | --- |
| Damage rule | player at 11.9 and 12.1 studs; 30 damage once, 0 outside (offline Luau with the real data table) | hazard row | — |
| PF-04 edge | drawn ring size against `Slam.radius` at tell, contact, end for skins A and B, both quality levels and both views (24 numbers, no stills); stills with the debug sphere for one key case only: lowest quality, threatened view, at tell, contact and end (3), plus any failing or borderline number | `Slam.radius` (PROPOSAL ±5 %, never inside) | lowest and highest quality; threatened and bystander view |
| PF-04 last tick | probe 1 frame after `slam_end`: telegraph instances 0 | log time of `slam_end` | — |
| PF-04 fuse | 20 runs: `slam_contact` log time minus `slam_tell` = 0.8 s ± one frame; no random spread | timing list | 100 ms inbound latency on the Network Simulator (PROPOSAL; probe) |
| PF-08 tell | boss placed at its fixed spawn position and facing before each `Trigger`; the log shows the same `cue` and `vfx` ids at the same `f` offsets from `evt slam_tell` (oracle); two folders from `slam_tell` compared up to contact on the boss's box stay at the noise floor (screening aid) | identical tell | — |
| PF-07 reduced | `Reduced` hook on (and once the Settings-menu route): the log shows the reduced variant fired; no camera shake; the countdown still visible; the ring's pulse rate from the read card within the PF-07 pulse cap | read card reduced line and rates | reduced motion, grayscale, sound off |
| PF-16 bystander | one client, `Viewer` = bystander, `Clarity` all then essential: no `cam` line, the ring's `LocalTransparencyModifier` 0 at both (the branch); second client 30 studs away: camera CFrame unchanged during the slam (the path) | per-viewer line; ring `others_ltm` 0 | one client; two clients (owner starts the server) |
| T-19 ranges | after a `Trigger`, `inspect_instance` on the two layers spec rev2 marks semantic (ring, flash): `Lifetime`, `Speed`, `Rotation`, `RotSpeed` Min = Max, `Size` and `Transparency` envelopes 0, `FlipbookStartRandom` false; 2 layers read of 2 marked; the dust layer is decorative and may vary | spec rev2 semantic marks | — |
Planted faults: ring sized from `RING_SIZE = 13.2`; telegraph left 0.3 s after `slam_end`; reduced variant without the countdown; a 0.1 size envelope on the ring emitter. All four caught (the last only by the range read: two `Seed` runs gave the same server log).
Honest end: sync and feel NOT verified (no device capture); the ring's on-screen pulse rate not verified (spec only, D) until a frame folder of one tell; the two-client half of PF-16 BLOCKED until the owner starts the server; weakness: the edge numbers are read at three moments, so a ring that pulses outward between them is not covered (next step: a frame folder of one tell).

## 2. Paid egg shop (bought currency, random pet)
Sources: odds table rev4 (6 tiers), UI state list rev2 (12 states), reveal spec rev1 (one windup, tier ladder after the result frame), `platform-policy` §A.
Hooks: `Reject` (not enough gems; inventory full); `FxLog`; `Outcome` = `egg_hatch:<tier>` (or `Seed`); `Set` for gems, the luck boost and the restricted-player flag through the game's policy module.
| Row | Check | Oracle |
| --- | --- | --- |
| Odds total | offline: sum = 100 % per egg; rounding disclaimer present when rounded | `platform-policy` §A |
| Odds shown | capture before the buy button at the smallest phone: numbers visible; with luck boost on, the shown odds change | odds table with the modifier applied |
| PF-06 windup | lowest twice (noise floor), then lowest against each tier that adds a layer after the result: windup frames at the floor | identical windup |
| PF-06 no near-miss | lowest result: no higher tier's layer in any frame after the result | tier ladder |
| PF-02 refusal | `Reject` = not enough gems: no hatch event, no gem change, the refusal names "need 40 more gems" at the button | server log, server balance |
| PF-05 counter | buy right after a gem gain while the count-up runs: allowed by the true balance; label equals the server value at rest | server value |
| Restricted path | restricted flag on: no paid roll offered, or the permitted treatment the spec names | `platform-policy` §A |
| PF-11 states | all 12 states reached, each with its text at the longest locale | state list |
Honest end: the policy route of the real `PolicyService` in a published test is NOT RUN; the windup check covers the 6 tiers in the table, not a tier added later (the row is in the shared acceptance folder so it runs again).

## 3. Coin pickup burst (a frequent event)
Sources: VFX read card (rate up to 20 per second with a magnet, merge window 100 ms PROPOSAL, live copies ≤ 8, particles ≤ 10 per copy), UI motion table (count-up ≤ 600 ms PROPOSAL), sound event list (one tick per merge window).
Hooks: `Rate` (logs the live-copy count); `FxLog`; `Set` = `coins:<n>` for the start balance.
| Row | Check | Oracle |
| --- | --- | --- |
| PF-10 steady | 100 pickups at one per second: live copies ≤ 8, no tail still visible at the next pickup (frame folder of 5 s), counts back to baseline | caps; baseline |
| PF-10 burst | 20 per second for 3 s: one label and one tick per merge window in the log; no `cam` line in either run | merge window; no camera channel on a frequent event |
| PF-05 exact | after the burst, label = server balance; count-up ≤ 600 ms | server value |
| Lifecycle | 20 respawns during a burst: connection and instance counts back to baseline | baseline |
| PF-07 flashes | busiest folder with 8 players collecting: both counts of the studio counter within the PF-07 flash cap; the coin glint's pulse rate from the read card within the pulse cap | PF-07 caps |
Planted fault: merge window set to 0 (20 labels per second) caught by the burst row.
Honest end: whether the repeat tires is the owner's call at the playable preview; the glint's on-screen pulse rate not verified (spec only, D) without a frame folder; performance on a phone BLOCKED (no device).
