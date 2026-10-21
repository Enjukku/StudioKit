---
type: reference
scope: universal
status: active
updated: 2026-10-20
source: "J002; research paper RP via knowledge/reference/ui/05a (RA-94..105), 06a (records 01-25, handoff fields, review method); ui-basics/references/ui-effects.md (practice timings, PROPOSAL)"
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20

# UI motion: meaning first, numbers by test

## 1. What the evidence supports
- Motion implies rules. Hearthstone's ramming animation made players think the attacker took damage back; a small move plus a quick projectile fixed it (E M04, RP:136). Test the rule players read.
- Separate events: local input acknowledged ≠ server confirmed (VALORANT's 40 / 80 ms is network latency, not hit-marker life; V M07).
- Published game timings are almost absent: Riot's ready-check video fades 200 ms in / 300 ms out (V M01, that video only); Supercell's ≈ 2.8 s logo once a day (E C02). IBM Carbon's 70-700 ms tokens and curves are non-game ingredients. **None is a game preset** (H11, H12).
- So: every duration, easing, overshoot and scale value in a spec is a **project PROPOSAL** with provenance and a tuning test. Starting values: `ui-basics/references/ui-effects.md` (practice anchors: ~100 ms reads instant; enter 225 / exit 195; press 50 / release 120-150).

## 2. Beats every animated change writes separately (RP step 6)
input acknowledged · result confirmed · information visible · input available again · decoration ends. Plus: what cancels it, what a repeat does, the reduced-motion version (same information, no travel).

## 3. Motion records (06a, records 01-25, contracts O, numbers U unless stated)
| Group | Records | Contract in one line |
| --- | --- | --- |
| Buttons and focus | 03 button acknowledgement · 04 hover/focus fade · 10 tactile press · 11 focus travel | acknowledge on press, success is a separate event; pressing never shrinks the hit area; focus moves instantly, the visual may follow |
| Panels and navigation | 05 small panel expand · 08 background dim · 12 tab continuity · 13 reversible modal | reveal from the owning control; reversal never queues another full transition; modal traps focus only while active and restores it |
| Feedback | 06 toast · 07 important result · 09 inventory stagger | merge repeated toasts, keep a history for important ones; celebrate only confirmed milestones; stagger never hides selectable items (cancel on scroll/sort) |
| Rewards and economy | 14 anticipation hold · 15 rarity step-up · 16 batch summary · 17 world-to-HUD · 18 currency count-up · 19 progress fill | real balance updates at once, the display may count toward it and skip shows the true total; rarity also by text/shape; summary always reachable |
| Combat HUD | 20 confirmed hit · 21 critical/elimination · 22 floating damage · 23 cooldown ready | marker only on confirmed hits; ready cue ends when the ability is really ready |
| Ambient | 24 menu parallax · 25 brand intro | scenic motion off in reduced motion, separate mouse vs stick; brand moment never lengthens repeat entry |

## 4. Handoff fields per animation (06a §1a, O)
element · property + units · coordinate space · origin · from / to · duration ms · easing or spring · delay / stagger · trigger · loop / overshoot · completion event · input available during? · interruption · repeat · sound / VFX markers · reduced-motion variant · performance capture · source. A field without a value = PROPOSAL + test.

## 5. Review method (06a §1b, O)
Record on the device; note device, build, input, settings, resolution, frame rate. Mark: input · first visible response · information reveal · peak · settle · next action available. `elapsed ms = frame intervals × 1000 ÷ fps` (constant frame rate only). Review at normal speed, frame by frame, muted, repeated, and with reduced motion.

## 6. Roblox limits (V R08-R12 via 06a §1c; ui-basics U-11)
Never tween `UIStroke.Thickness` on text (glyph re-render, flicker). Gradient shine sweeps add GUI effect work: animate `Offset`, not colour. Flipbooks: budget the whole sheet. Profile on a real phone; the emulator is not a memory benchmark. Reduced motion: `GuiService.ReducedMotionEnabled` or the `@ReducedMotionEnabledTrue` style query.
