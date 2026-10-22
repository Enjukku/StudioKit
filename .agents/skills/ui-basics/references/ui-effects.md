> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Ported from DestructionSimulator `gui-ui/references/ui-effects.md` (2026-10-20, built from VFX training research), game-specific values removed. Timings are starting points ([P] = proposal); motion feel rules come from the game's VFX or animation skill when it has one. Revised by J018 maker feature-builder · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (§A seeds the game's motion table; rows for pending, refusal sound rate, eased travel, pulses and other players' events; §B rows for the refusal shake, source-to-destination and merge).

# UI effects (juice on screen elements)

**§A seeds each game's motion table.** The UI designer copies these rows into `content/ui/_system/motion-table.md` (`ui-design` → `references/motion.md` §7) and tunes them by bracketing on a playable build; the builder reads the game's table as data (`ui-basics` U-13), never this file and never literals. Rows the table needs that are design values owned elsewhere point there instead of copying them.

World → HUD hand-overs (a coin burst in the world that flies into the counter) are planned with the VFX role on one shared beat list: VFX owns the 3D part, UI owns the landing and the counter.

## A. UI moments
| Moment | Timing (ms) | Look | Sound | Leave out |
| --- | --- | --- | --- | --- |
| Button press | press 50 eased out; release 120-150 with a small overshoot; input accepted on press; same timing on every button | the button sinks a few pixels; highlight | click on press, not on hover; click and visual from one input event | a bounce that delays the next tap; > 100 before any visible change |
| Pending | shows when the server answer takes > 100 [P]; cancelled by the result | "Buying…" or a small spinner on the pressed control; the control stays pressed | none, or a soft loop the card names | pending shown as success |
| Purchase success | starts on **server confirmation**; badge enters 225; burst 300 overlapping the item's flight 450; exit 195 | success icon; item flies to the inventory; currency counts down | chime with the first frame of the confirmed outcome | celebrating before confirmation |
| Error / refusal | shake 3 cycles in 280, ±4 px, the pressed control only (its inner content frame); message enters 225, stays ≥ 2000 or until the next tap | danger colour + icon + text that says the cause and how to fix it | soft "no", at most once per 500 when spammed [P] | whole-screen shake; meaning by colour alone; a joke hiding the fix; silence |
| Toast | enter 225; hold 3000 (+1000 per 10 words); exit 195; ≤ 3 stacked; same-kind toasts inside the merge window merge | stable icon + text, away from the action focus | only when warranted | reward spectacle for every toast |
| Currency change | "+N" pop 150, float 600, fade 200; counter bump 120 up / 150 down; count-up ≤ 600; affordability uses the true balance at once; same-kind gains inside the merge window (about 100 [P]) share one label | signed label; gains in the reward colour, spends neutral | tick on the first arrivals and one closing sound on gains; a soft clink on spend; on the confirmed update | rolling digits hiding the real balance; a sound per digit; a label per coin |
| Travel and growth | eased (fast start, slow settle), never linear; exits no longer than entrances | from its source element to its destination | — | linear moves; popups from nowhere |
| Pulses, countdowns, low health | rate classes are design values: `ui-design` `references/motion.md` §8 (nothing above 3 per second at full contrast) | — | ticks keep the visual blink's rate | — |
| Other players' events | small, at the side or in a feed: `ui-design` `references/motion.md` §8 | — | — | taking the local player's attention motion or the critical zone |

Anchors: about 100 ms reads as instant; short motions 50-200 ms; enter 225 / exit 195 (Material motion guidance, practice); 200-300 ms for a major change; 500 ms feels slow.

## B. Roblox tools for effects
| Effect | Tool | Notes |
| --- | --- | --- |
| Pop / squash | tween `UIScale.Scale` (1 → 1.12 → 1, Back Out) | keeps layout; one UIScale per element; a cartoon stretch keeps the area (one axis up, the other down) |
| Hover and press states | Styling transitions (`StyleRule:SetPropertyTransition`) | no script; fires on state changes only |
| Shine sweep | `UIGradient` on the element; tween `Offset` from −1 to 1 with a narrow bright band in Transparency | cheap; animate offset, not colour |
| Glow / outline pulse | `UIShadow` (live) or `UIStroke` Transparency tween on borders; ≤ 1 Hz for lasting states | never tween UIStroke Thickness on text |
| Number roll | tween a NumberValue and write the label on Changed; set the exact value on Completed | abbreviate big numbers; logic never reads the NumberValue |
| Refusal shake | tween the `Position` offset of the control's inner content frame (±4 px, 3 cycles) from the motion-table row | a control laid out by a `UIListLayout` or `UIGridLayout` ignores its own `Position` (`ui/list-flex-layouts.md:16`, `ui/grid-table-layouts.md:40`), so the shake would silently not play; the layout and the other controls stay still; never the whole screen |
| Fly-to-HUD | pooled ImageLabels on a curve (about 20 on screen at most [P]); start from `Camera:WorldToScreenPoint` or `WorldToViewportPoint` to match the ScreenGui's insets (`references/facts.md`); end on the counter's centre | landing = counter bump + tick |
| Grow from source | start the popup at the opening control's position and size, tween to its place; close back to it | — |
| Burst of bits | pooled ImageLabels with random velocity, scale and fade (no native UI particles yet; planned 2027) or a ViewportFrame | pool and cap counts |
| Flash | Frame Transparency tween, ≤ 80 % white, 125 ms | counts toward flash safety |
| Group fade | `CanvasGroup.GroupTransparency` | static size; memory cost |
| Reduced motion | the comfort module (`engineering-craft` EC-21): tween time 0 or a fade; or the `@ReducedMotionEnabledTrue` style query | keep all information |

Every tween and pooled instance belongs to a cleanup owner (lifetime: the screen).
