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

# bTier__Punch_Place_OS_F · B · camera side-rear, about 30 studs; dark blue tiled floor, bright blue sky with clouds; one character right of centre (about 28% of screen height), facing left
Event: the character throws a punch; white-blue impact bursts flash in front of the fist several times (about 7 marker stages in the original). Timing is our estimate (INDEX *).
Phases: burst 1 at about 370-750 ms · bursts 2-3 at about 1100-1500 · big burst with whole-screen light flash at 1856 ms · lights return to base by 2400 · long tail with sky change at 4685 ms
| ms | Coverage % | Where (box) | Shapes on screen | Colours | Brightness | Motion |
|---|---|---|---|---|---|---|
| 0 | 1.4 | .08,.01,.99,.61 | character only plus slight background shift (screen is not fully still: the sky and floor changes dominate the box) | | 0 | idle |
| 369 | 2.3 | .26,.01,.98,.67 | white 8-spike starburst in front of the fist, about 8% of screen width (sheet frame 2) | white #FFFFFF, cyan rim #70D0FF | 0.3% | pops, short |
| 746 | 2.7 | .28,.01,.97,.68 | white burst about 10% screen width, plus a thin vertical blue-white spike column of 4 lines about 6% of screen height (f022) | #FFFFFF, #60C8FF | 1.05% | holds 2-3 frames |
| 1127 | 0.6 | | gap: nothing | | 0 | |
| 1494 | 2.3 | .31,.01,.93,.67 | same burst shape with blue electric lines (f044) | white, #80B0FF | 1.06% | pop |
| 1856 | 37.7 | .15,.01,1,.88 | long 7-spike blast to the left about 12% screen width; whole sky brightens and floor lightens (scene lighting flashes; floor goes from #0A1830 to #5A7A98); sun-like glow on the horizon (f055) | white, sky #B0F0FF | 2.5% | light flash, decays in about 0.4 s |
| 2430 | 0.07 | | idle | | 0 | |
| 3161-4298 | 0.4-1.5 | | slow drift: sky clouds change slowly (not effect) | | 0 | |
| 4685+ | 5.4 | .0,.01,1,.46 | whole sky region changes (cloud layout/lighting shifts): not effect | | 0 | |
Layers seen: starburst 1 (white, 7-8 spikes), blue lightning/spike lines 3-4, whole-scene light flash 1 (only at the last burst), tiny bubbles on the hat (character item, not effect).
Size vs character: burst 0.4 to 0.5 character heights wide; 1856 ms burst about 1.2 character heights wide with a brightness flash over the entire scene.
What makes it look good:
- Burst tied to the fist position and facing; the long spikes give direction.
- The last burst adds scene lighting flash, which makes it feel heavy.
- High-contrast white-on-dark-blue.
Weak points:
- Metrics unreliable here: the sky and floor lighting change, and the big coverage at 1856 ms is lighting, not particles.
- Timing is our estimate; the original animation did not load. Bursts 1-3 are almost the same: little variation.
- No debris, shockwave or camera shake seen; burst is a small white blob.
