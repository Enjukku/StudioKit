> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Ported from DestructionSimulator `gui-ui/references/ui-effects.md` (2026-10-20, built from VFX training research), game-specific values removed. Timings are starting points ([P] = proposal); motion feel rules come from the game's VFX or animation skill when it has one.

# UI effects (juice on screen elements)

World → HUD hand-overs (a coin burst in the world that flies into the counter) are planned with the VFX role on one shared beat list: VFX owns the 3D part, UI owns the landing and the counter.

## A. UI moments
| Moment | Timing (ms) | Look | Sound | Leave out |
| --- | --- | --- | --- | --- |
| Button press | press 50 eased out; release 120-150 with a small overshoot; input accepted on press; same timing on every button | the button sinks a few pixels; highlight | click on press, not on hover | a bounce that delays the next tap; > 100 before any visible change |
| Purchase success | starts on **server confirmation**; badge enters 225; burst 300 overlapping the item's flight 450; exit 195; show a pending state if confirmation takes > 100 | success icon; item flies to the inventory; currency counts down | chime after the confirmed result | celebrating before confirmation; pending shown as success |
| Error | shake 3 cycles in 280, ±4 px; message enters 225, stays ≥ 2000 or until the next tap | danger colour + icon + text that says how to fix it | soft "no", rate-limited | whole-screen shake; meaning by colour alone; a joke hiding the fix |
| Toast | enter 225; hold 3000 (+1000 per 10 words); exit 195; ≤ 3 stacked | stable icon + text, away from the action focus | only when warranted | reward spectacle for every toast |
| Currency change | "+N" pop 150, float 600, fade 200; counter bump 120 up / 150 down; count-up ≤ 600; affordability uses the true balance at once | signed label; gains in the reward colour, spends neutral | tick on gain, clink on spend, on the confirmed update | rolling digits hiding the real balance; a sound per digit |

Anchors: about 100 ms reads as instant; short motions 50-200 ms; enter 225 / exit 195 (Material motion guidance, practice); 200-300 ms for a major change; 500 ms feels slow.

## B. Roblox tools for effects
| Effect | Tool | Notes |
| --- | --- | --- |
| Pop / squash | tween `UIScale.Scale` (1 → 1.12 → 1, Back Out) | keeps layout; one UIScale per element |
| Hover and press states | Styling transitions (`StyleRule:SetPropertyTransition`) | no script; fires on state changes only |
| Shine sweep | `UIGradient` on the element; tween `Offset` from −1 to 1 with a narrow bright band in Transparency | cheap; animate offset, not colour |
| Glow / outline pulse | `UIShadow` (live) or `UIStroke` Transparency tween on borders; ≤ 1 Hz for lasting states | never tween UIStroke Thickness on text |
| Number roll | tween a NumberValue and write the label on Changed | abbreviate big numbers |
| Shake | tween Position offsets (±4 px, 3 cycles) | never the whole screen for a UI error |
| Fly-to-HUD | pooled ImageLabels on a curve; start point from `Camera:WorldToViewportPoint` | landing = counter bump + tick |
| Burst of bits | pooled ImageLabels with random velocity, scale and fade (no native UI particles yet; planned 2027) or a ViewportFrame | pool and cap counts |
| Flash | Frame Transparency tween, ≤ 80 % white, 125 ms | counts toward flash safety |
| Group fade | `CanvasGroup.GroupTransparency` | static size; memory cost |
| Reduced motion | `GuiService.ReducedMotionEnabled` → tween time 0 or a fade; or the `@ReducedMotionEnabledTrue` style query | keep all information |

Every tween and pooled instance belongs to a cleanup owner (lifetime: the screen).
