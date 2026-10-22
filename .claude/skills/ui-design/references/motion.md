---
type: reference
scope: universal
status: active
updated: 2026-10-22
source: "J002; research paper RP via knowledge/reference/ui/05a (RA-94..105), 06a (records 01-25, handoff fields, review method); ui-basics/references/ui-effects.md (practice timings, PROPOSAL); J018 (motion goals, the game's motion table, refusals, counters, frequent events, pulse rates)"
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Rebuilt by J018 maker ui-ux-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (§1 motion goals, §2 attempt and outcome, §4 new fields, §5 inputs, §7 motion table, §8 refusals, counters, frequent events, pulses, celebrations).

# UI motion: meaning first, numbers by test

## 1. What motion is for
- **The still explains; motion makes it felt.** Every event must read from its end frame with sound off (label, icon, colour); motion and sound add weight and feeling. An event explained only by motion fails reduced motion and a glance.
- **Five goals, in this order.** (1) Responsiveness: the press answers at once, before any server reply. (2) Intention: motion points at the one thing to act on now; one attention motion per screen state, everything else still. (3) Awareness: things come from their source and go to their destination (a popup grows from the button that opened it; coins fly to the counter they raise). (4) Consistency: each element type moves the same way everywhere, from one motion table (§7). (5) Material: the game's UI moves like one physical material from its world (light paper, heavy metal, bouncy jelly), written in the rule sheet, so the motion tells the tone before anything is read.
- **Motion implies rules.** Hearthstone's ramming animation made players think the attacker took damage back; a small move plus a quick projectile fixed it (E M04, RP:136). Test the rule players read.
- **Separate events:** local input acknowledged ≠ server confirmed (VALORANT's 40 / 80 ms is network latency, not hit-marker life; V M07).
- Published game timings are almost absent: Riot's ready-check video fades 200 ms in / 300 ms out (V M01, that video only); Supercell's ≈ 2.8 s logo once a day (E C02). IBM Carbon's 70-700 ms tokens and curves are non-game ingredients. **None is a game preset** (H11, H12). So every duration, easing, overshoot and scale value is a **project PROPOSAL** in the game's motion table (§7), with provenance and a tuning test.

## 2. Beats every animated change writes separately (RP step 6)
attempt cue (on the press: small, client side, the press frame or the next) · result confirmed (server) · information visible · input available again · decoration ends. Plus: what cancels it, what a repeat does, the reduced-motion version (same information, no travel). The outcome layer (burst, chime, "+N", celebration) starts only on the confirmed result and is sized by its real tier; when confirmation takes longer than about 100 ms (PROPOSAL) a pending state shows ("Buying…"), never an early success; a rejected request shows the refusal (§8), never the success layer. Bigger moments tell a short story: a build that rises (smaller to bigger, dim to bright), a short beat, one peak, then the result after its cause; the gaps between beats are uneven, never metronomic.

## 3. Motion records (06a, records 01-25, contracts O, numbers U unless stated)
| Group | Records | Contract in one line |
| --- | --- | --- |
| Buttons and focus | 03 button acknowledgement · 04 hover/focus fade · 10 tactile press · 11 focus travel | acknowledge on press, success is a separate event; pressing never shrinks the hit area; the same press timing on every button; focus moves instantly, the visual may follow |
| Panels and navigation | 05 small panel expand · 08 background dim · 12 tab continuity · 13 reversible modal | reveal from the owning control and return to it; reversal never queues another full transition; exits are shorter than entrances; modal traps focus only while active and restores it |
| Feedback | 06 toast · 07 important result · 09 inventory stagger | merge repeated toasts, keep a history for important ones; celebrate only confirmed milestones; stagger never hides selectable items (cancel on scroll/sort) |
| Rewards and economy | 14 anticipation hold · 15 rarity step-up · 16 batch summary · 17 world-to-HUD · 18 currency count-up · 19 progress fill | real balance updates at once, the display may count toward it and skip shows the true total; rarity also by text and shape; summary always reachable; world-to-HUD on one beat list with the VFX designer (VFX owns the world part, I own the landing and the counter); a filling meter rises steadily and peaks on the real threshold |
| Combat HUD | 20 confirmed hit · 21 critical/elimination · 22 floating damage · 23 cooldown ready | marker only on confirmed hits; ready cue ends when the ability is really ready; HUD cues take their event names and times from the animator's timing list |
| Ambient | 24 menu parallax · 25 brand intro | scenic motion off in reduced motion, separate mouse vs stick; brand moment never lengthens repeat entry |

## 4. Handoff fields per animation (06a §1a, O; J018 additions last)
element · property + units · coordinate space · origin · from / to · duration ms · easing or spring · delay / stagger · trigger · loop / overshoot · completion event · input available during? · interruption · repeat · sound / VFX markers · reduced-motion variant · performance capture · source · **motion-table row** · **start and end anchor** (source and destination element) · **attempt or outcome** · **expected rate and merge window** (frequent events). A field without a value = PROPOSAL + test.

Sound sync for UI: the click and the press visual start from one input event; the sound onset lands on the first changed frame or up to about 40 ms after it, never more than one frame before it; the reward chime starts with the first frame of the confirmed outcome. Studio captures are stills, so sync stays "not verified" unless captured on the target device (`review.md` §4).

## 5. Review method (06a §1b, O; inputs per J018)
Timing is measured from a frame folder at a known frame rate (`f###_<ms>ms.jpg`, ms from the capture start, idle frames before the input, the input frame's ms noted): from the studio-operator's Studio capture rig through the lead, or from a Figma `export_video` of the prototype split into frames (`ui-figma/references/figma-mcp.md` §6). Mark: input · first visible response · information reveal · peak · settle · next action available. `elapsed ms = frame intervals × 1000 ÷ fps` (constant frame rate only). Press onset: `review.md` §6 S-33 and its capture rules. I see stills: feel at normal speed, the motion material and the rhythm are judged by the owner on a playable preview at the gate; slow playback finds problems but never proves feel. Review muted, repeated, and with reduced motion.

## 6. Roblox limits (V R08-R12 via 06a §1c; ui-basics U-11)
Never tween `UIStroke.Thickness` on text (glyph re-render, flicker). Gradient shine sweeps add GUI effect work: animate `Offset`, not colour. Flipbooks: budget the whole sheet. Profile on a real phone; the emulator is not a memory benchmark. Reduced motion: `GuiService.ReducedMotionEnabled` or the `@ReducedMotionEnabledTrue` style query; set the tween time to 0 or swap to a fade (`production/publishing/accessibility.md:184-188`). Easing styles are set per tween (default Quad); Back and Elastic give an overshoot (`ui/animation.md:406-474`).

## 7. The game's motion table (one per game)
One table holds every UI motion of the game, one row per element type and action; every screen reads it, so the same element always moves the same way and the builder keeps it as shared data, not per-script values. I write it once per game in `content/ui/_system/motion-table.md`, seed it from the starting values in `ui-basics/references/ui-effects.md` §A (all PROPOSAL), and tune it by bracketing (a too-short and a too-long value beside the pick, compared on the owner's playable preview). Approved rows become owner decisions.
| Column | Holds |
| --- | --- |
| Element type and action | button press, button release, panel open, panel close, popup, toast, reward badge, "+N" label, counter bump, count-up, fly-to-HUD, refusal shake, pulse class, tab switch |
| Duration and easing | ms and easing style; travel, growth and exits follow the `ui-effects.md` §A "Travel and growth" row, and durations its anchors (instant, major change, slow) |
| Overshoot | none, or one crossing of the target (for example 1.0 → 1.12 → 1.0 on a reward pop); never on a frequent press, never delaying the next tap |
| Material | the rule sheet's motion material, how this row shows it (paper flutters, metal slams, jelly wobbles once); a cartoon game may stretch a fast-flying coin along its path and squash it on landing through `UIScale`, keeping its area |
| Sound | the cue id from the sound designer's UI cue list; the sync rule (§4) |
| Reduced variant | snap (time 0) or a fade; the information kept |
| Source of the value | starting value, bracket tested, owner decision id |

## 8. Refusals, counters, frequent events, pulses, celebrations
Starting timings for refusals, toasts, "+N" labels, counter bumps and count-ups are the rows of `ui-basics/references/ui-effects.md` §A, copied into the game's motion table (§7); the values below are only those that table lacks (PROPOSAL).
- **Refusals.** The pressed control answers: only it shakes; the message names the cause and the fix ("Need 40 more coins") in text plus icon in the danger colour, next to the control; a soft "no" sound, rate-limited when the player spams it (the `ui-effects.md` §A "Error / refusal" row). Never a whole-screen shake, a red flash alone, a joke that hides the fix, or silence. A disabled control shows why and what unlocks it before it is pressed.
- **Counters.** The true value updates at once and drives logic and affordability; the "+N" label, bump and count-up are decoration that ends on the exact server value; gains are signed in the reward colour, spends stay neutral (red is for danger); numbers follow the progression designer's display rule and fixtures (`progression-craft/references/data-handoff.md` §5: balances round down, prices and requirements round up, one suffix table, so a shown balance never looks affordable when it is not); a few representative coins (about 20 on screen at most) fly on curved paths to the counter, a tick on the first arrivals and one closing sound, never a sound per digit or per coin.
- **Frequent events.** The more often it happens, the shorter and quieter it is. Same-kind gains inside the merge window (the `ui-effects.md` §A "Currency change" row) share one label and one sound; toasts stay outside the play focus. Judge a frequent cue over a burst (about 20 per second) and over a hundred repeats, never from one. Other players' events (their rare hatch, their level-up) appear small, on the side or in a feed, and never take the local player's one attention motion or cover the critical zone.
- **Pulse rates carry meaning.** Lasting states are steady or pulse at most about 1 Hz; a claimable reward or the one next action may pulse slowly (it is the screen's one attention motion); countdowns tick at 1 Hz, then 2 Hz in the last 2 s and 3 Hz in the last 1 s, landing on the event; low health is a 1 Hz edge pulse with a small brightness swing and the number, never a full red wash; nothing pulses above 3 Hz at full contrast (photosensitivity). Timers follow the server's value.
- **Celebrations.** Sized by the real outcome tier; in play they end in under about 2 s, before the next decision; bigger ceremonies only on non-play screens; a pop reaches most of its size fast and eases out slowly; reaction and emote icons are pushed to full expression for a two-second read. Escalation (x2, x3) steps only at real thresholds, is named by a short text label that reads with effects off, and resets visibly.
