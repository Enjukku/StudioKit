---
type: reference
scope: universal
status: active
updated: 2026-10-20
source: "moved from DestructionSimulator 2026-10-20"
supersedes: []
---
> Author: kit-mover · claude-sonnet-5-5 · medium · 2026-10-20 (moved from DestructionSimulator; original author line kept below)

> Author: frame-script agent · claude-sonnet-5-5 · medium · 2026-10-20

# sTier__Elemental_Guns_E_follow · S · camera follow (behind the projectile), moving camera so coverage is unreliable
Event: same fire-and-ice shot seen from the bolt: a white flash at launch, then a fire ball and an ice snowflake orb fly side by side.
Phases: gun idle 0-1200 ms · launch flash 1226-1330 · travel with fire and ice 1400-2900.
| ms | Coverage % (metrics) | Where (box) | Shapes on screen | Colours | Brightness | Motion |
| 0-1122 | 9.2 (baseline) | | character with gun at right, small | | | static |
| 1226 | 75 | whole frame | near-white screen wash, pink-white blobs, 4-point sparkles, snowflakes | #ffffff, pink #ffb0d0, cyan #80e0ff | bright 19% (peak) | camera snaps into the bolt |
| 1329 | 48 | x.12-1 y.36-1 | white fog clears, big white snowflakes and 4-point stars bottom left, pink-orange burst top right | #e8f8ff, #ff9060 | 10% | wash clears in ~100 ms |
| 1430 | 35 | | orange glowing disc (hot yellow centre) right side, ice orb left | disc #ffb030 to #ff7010 | 1.4% | camera trails behind |
| 1543-2143 | 25-30 | x.15-1 y.36-1 | fire: ball plus ~15 flame blobs in a long tail; ice: bright blue-white orb inside a ring arc, chain of 5-6 white snowflake sprites, thin blue speed lines | fire #ff8a20 / #ffd040, ice #a8e8ff, white #ffffff | 1-3% | snowflakes spin, fire blobs flicker; ice lower left, fire upper right |
| 2238-2936 | 7-9 | x.2-1 | bolts partly out of frame; flame tail and snowflakes at the edge | | 1% | camera loosens |
Layers seen: launch flash 1, fire disc 1, flame blobs ~15, orange sparks ~10, ice orb 1, snowflake sprites ~6 (large), pink magic glints ~6, 4-point sparkles ~8, thin ring arcs 2, speed lines ~5.
Size vs character: orb discs fill about 15-20% of screen height each; no character in view during travel.
What makes it look good:
- Cartoon flame blobs and flat snowflake sprites with strong shapes: anime style, not soft smoke.
- Warm orange against cold white-cyan side by side gives clear contrast.
- The launch flash lasts only about 100 ms and then clears.
Weak points:
- Moving camera, so coverage is mostly camera and sky; use it for timing only (flash at 1226, about 100 ms).
