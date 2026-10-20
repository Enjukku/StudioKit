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

# aTier__soear · A · camera side, about 6 studs (a long spear fills the full screen height)
Event: an item idle loop: a tall purple spear glows with white-violet aura at the head and electric sparkles up the shaft; every second or so a pure white beam fills the shaft for 200-400 ms.
Phases: idle glow throughout · white pulse 742 ms · pulses 1111-1660 · idle 1843-2981
| ms | Coverage % | Where (box) | Shapes on screen | Colours | Brightness | Motion |
| --- | --- | --- | --- | --- | --- | --- |
| 0-550 | 0.4-0.8 | 0.50-0.71 x, 0.02-1.0 y | thin purple shaft with a glowing white-violet cloud at the head and crossguard, ~20 white sparkle dots, lightning squiggles on the shaft, faint vertical light rays | #B58CE8, #E8E0FF aura | 0.06-0.19 % | sparkles drift |
| 742 | 4.0 | 0.50-0.69 x | whole lower shaft turns into a solid white column about 0.02 of screen width | #FFFFFF | 2.8 % near-white | 1-3 frame pulse |
| 931 | 0.7 | same | back to purple shaft | #B898E8 | 0.07 % | pulse ends |
| 1111 | 3.6 | 0.50-0.71 x | white column again, shorter | #F0EAFF | 2.5 % | pulse |
| 1293 | 2.0 | same | column half length | #E8DCF5 | 1.4 % | decays |
| 1474-1660 | 3.1-4.0 | same | 2 more white pulses | #FFFFFF | 2-2.8 % | pulse |
| 1843-2981 | 0.4-0.9 | same | idle purple shaft, sparkle dots, rays | #A890D8 | 0-0.06 % | idle loop |
Layers seen: head aura cloud 1, sparkle dots ~20, lightning squiggles 4-6, light rays 3-4, white beam pulses (4 in 2 s), floor purple glow 1.
Size vs character: no character; the spear is about 1.0 of screen height, about 0.02 of width.
What makes it look good:
- white pulses on a purple base: strong value jump (about 2 % of the screen goes pure white)
- pulses at uneven spacing (about 370 ms then 180 ms)
- constant fine sparkles keep the idle alive
Weak points:
- an idle loop: it partly sits in the median background, so the coverage reads low
- the effect lives on an item, so size depends on the camera distance
