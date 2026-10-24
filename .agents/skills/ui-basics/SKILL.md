---
name: ui-basics
description: Build and review Roblox UI that works on every device - scaling, safe areas, readable text, touch and gamepad, accessibility, the 2026 styling system, button states, UI performance. Use when building a screen, HUD, shop, menu, popup or button, for "the UI is cut off on phones", "text is too small", "it does not work with a controller". Engineering only; look and UX come from the UI designer.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Kit skill: universal. J001 step 8. Evidence: `references/facts.md` (docs mirror upstream 7400643; Roblox staff posts 2026; Y = `_api-reference/classes/`). The UI/UX designer role (`ui-design`, `ui-figma`, the style books) owns how a screen works and looks; this skill builds it. Rebuilt by J018 maker feature-builder · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (functional pass before styling, motion from the game's motion table, attempt and outcome, refusals at the control, true counters, source-to-destination motion, reduced and transparency paths, U-13 to U-18, the self-review with inputs in §6). Numbers marked PROPOSAL are starting values a check may change.

# UI basics: every screen works on every device

## 1. When this skill starts
A screen, HUD element, popup or button is built or changed. The **design** (flow, states, motion table rows, message table, rule sheet tokens, cue ids) comes from the UI designer's spec (`content/ui/<screen-id>/spec.md`, `ui-design` §3 step 10) and an approved mockup; this skill makes it work in Roblox. If no approved spec exists for a player-facing screen, ask for one before styling; you may still build the functional pass (§3 step 2). Code rules for feedback and wiring: `engineering-craft` EC-17 to EC-24 and `references/presentation.md` there. After a context compaction, re-read §3 and §6.

## 2. Read this file when
| You need | Open |
| --- | --- |
| A property, layout rule, inset, text, styling, appearance or input fact; live vs beta | `references/facts.md` |
| Starting timings that seed the game's motion table; Roblox tools for button feel, popups, toasts, counters, fly-to-HUD, refusals | `references/ui-effects.md` |
| The game's motion table and pulse rates (design values) | `ui-design` → `references/motion.md` §7, §8 |
| The release checks and the image measures of a built screen (the UI designer runs them) | `ui-design` → `references/review.md` §1, §6 |
| Text players type that others see | `platform-policy` skill § D (filtering) |
| Shops, Robux prices, paid random items | `platform-policy` § A-B (binding; wins over this book) |
| UI cost questions beyond §4 | `performance` skill |
| A framework game (`roblox-game-framework`): open, close, back and gamepad focus through **Screens**, every tween through **Motion** and the game's motion table, never own screen stacks or `TweenInfo` literals | `engineering-craft` → `references/framework.md` §4.6, §4.7 |

## 3. Steps (cheap stages first)
1. **Read the spec and restate it.** Flow (where am I, what can I do, what just happened, what next), every state, data sources and remotes, motion-table rows, message table, tokens, cue ids. A missing piece is a question to the UI designer, with a PROPOSAL meanwhile. *Check:* restatement with zero open questions, or the questions sent.
2. **Functional pass (plain frames, no styling).** Every state reachable with touch, mouse and gamepad; data bound to the real server values; attempt and outcome wired (U-14); refusals with their reasons (U-15). Play it in Studio before any style. *Check:* U-S01, U-S02.
3. **Structure:** one ScreenGui per feature; `ScreenInsets = CoreUISafeInsets` for anything interactive; `ResetOnSpawn = false` for persistent HUD; `DisplayOrder` for layering screens.
4. **Size and place** with Scale + AnchorPoint, constraints and one outer `UIScale` for panels designed on the 1920 × 1080 canvas (U-02); world values sit on their unit with a `BillboardGui` (Adornee), short and close.
5. **Style** with a StyleSheet and the spec's tokens; per-device and accessibility variants with style queries (U-05). No colour, font or radius typed per element.
6. **Motion and sound** from the game's motion table and the cue table (U-13): press, open, close, toast, pop, refusal shake, count-up, fly-to-HUD from source to destination (U-17); every row's reduced variant; translucent backgrounds follow `PreferredTransparency` (U-10).
7. **States:** idle, hover, pressed, disabled with a reason, loading, pending, cooldown, error, success, empty. No action may need hover or a long press only.
8. **Test** in the Device Simulator at the smallest supported phone, a tablet, a PC and a TV size, with touch, mouse and gamepad, Largest text size, reduced motion and the most opaque background setting; run §6; name the captures for the UI designer's review slot (`engineering-craft` `references/presentation.md` §10).

## 4. Craft core
| ID | Practice | Evidence |
| --- | --- | --- |
| U-01 | **Safe areas:** interactive UI under `ScreenInsets = CoreUISafeInsets` (clear of the top bar and notches); `None` only for full-screen backgrounds; read `GuiService.TopbarInset` when placing next to the top bar. Set ScreenInsets directly, not `IgnoreGuiInset` | _includes/ui/screen-insets.md; Y/ScreenGui.yaml |
| U-02 | **Scaling:** HUD edges use Scale positions with AnchorPoint at the edge they hug; panels are designed at one canvas size and fitted with one outer `UIScale` plus `UIAspectRatioConstraint`; `UISizeConstraint` caps sizes on TVs. Never fix overflow by scaling an already-overflowing container | ui/position-and-size.md; ui/size-modifiers.md |
| U-03 | **Thumb zones:** nothing important in the bottom-left (move) or bottom-right (jump) control areas; frequent buttons in thumb reach; touch targets meet the project's declared touch rubric (`ui-design` D-05; ≥ 44 pt is practice, Roblox gives no number) with gaps; contextual buttons appear only when needed | ui/position-and-size.md:131-212 |
| U-04 | **Text:** prefer `AutomaticSize` + `TextWrapped` over `TextScaled`; if TextScaled, add `UITextSizeConstraint` (min ≥ 9). TextScaled ignores the player's PreferredTextSize, so key reading text must not use it. `FontFace`, not the Font enum | Y/TextLabel.yaml:511-547; accessibility.md:168-182 |
| U-05 | **Styling system for shared look:** tokens (`$Primary`, `$Radius`) in a StyleSheet from the spec's rule sheet; hover and press via state selectors and transitions; device and accessibility variants with built-in queries (`@ViewportDisplaySizeSmall`, `@PreferredInputGamepad`, `@ReducedMotionEnabledTrue`). Direct properties only for one-off or script-driven values | ui/styling/; DF 4566519, 4646870 |
| U-06 | **Every device can reach everything:** gamepad selection works on every screen (`GuiService:Select`, `NextSelection*`, a visible selection image); hints follow `UserInputService.PreferredInput`; a long-press or right-click action (`SecondaryActivated`) always has a visible alternative; **no action works only on hover** (touch and gamepad have no hover) | Y/GuiService.yaml; input/index.md; DF 4720108 |
| U-07 | **UI never grants.** Buttons use `Activated`, send a request, and show the server's confirmed answer (U-14). Optimistic display only when it can be reverted cleanly; never for money or rewards. **Robux prices are read from Roblox** (`MarketplaceService:GetProductInfoAsync`), never typed or taken from a data file (`platform-policy` P-05) | `networking-security` N-03 |
| U-08 | **Native modifiers first (live):** `UIShadow` for drop shadows and glows (≤ 100 on screen), per-corner `UICorner`, `UIStroke`, `UIGradient` (Color, Transparency, Offset, Rotation). **Do not ship betas**: text or inset shadows, radial or conical gradients, `InputActionLabel` (Studio only until released) | DF 4636263, 4934553, 4846594, 4779420 |
| U-09 | **Clipping:** rotated clipping is default; `ClipsDescendantsSupportsRotation` disappears November 2026, so never set it; clip to rounded corners with a CanvasGroup | DF 4737864 |
| U-10 | **Accessibility:** contrast on the weakest backdrop; meaning never by colour or sound alone (add icons and text); honour `ReducedMotionEnabled` through the comfort module (`engineering-craft` EC-21); multiply each translucent background's transparency by `GuiService.PreferredTransparency` (tag the backgrounds, keep the default value, re-apply on change); test Largest text size | production/publishing/accessibility.md:46-208 |
| U-11 | **UI cost:** pool list rows and update them in place; no tween of `UIStroke.Thickness` on text; few CanvasGroups and keep them static-sized; animate gradient offset and rotation, not colour; sprite sheets for many small icons; fewer layers on always-on HUD | Y/CanvasGroup.yaml; ui/appearance-modifiers.md:258; DF 4846594 |
| U-12 | **Cleanup:** every connection, tween and cloned instance of a screen has one cleanup owner that runs on close; reopening a screen 20 times leaves no extra connections. A server answer that arrives after the screen closed or the character respawned is dropped (check a generation token). UI tied to world objects handles the object streaming out; every `WaitForChild` has a timeout | `knowledge/reference/architecture/strong-codebases-2026-10.md` A-10 |
| U-13 | **Motion and sound from tables, never literals.** One helper builds every tween from a motion-table row (duration, easing, overshoot, reduced variant); travel and growth are eased, never linear; exits no longer than entrances; the same element type moves the same on every screen. The click and the press visual start from one input event; the reward chime with the first frame of the confirmed outcome | `ui-design` motion.md §4, §7 |
| U-14 | **Attempt, pending, outcome** (the rule: `engineering-craft` EC-17). On a screen: the press state and click answer in the press frame or the next, before any server reply; the pressed control shows pending after the spec's threshold; a press never needs an animation to finish before the next tap counts | `engineering-craft` presentation.md §2 |
| U-15 | **Refusals at the control.** The reason code maps to a message with its cause and fix ("Need 40 more coins") plus an icon in the danger role, next to the pressed control, held at least about 2 s or to the next tap; only that control shakes, by a `Position` offset tween on its inner content frame (a control laid out by a `UIListLayout` or `UIGridLayout` ignores its own `Position`); the refusal sound at most once per 0.5 s (PROPOSAL); a disabled control shows why and what unlocks it before it is pressed (a paid-random control for a restricted player is hidden or given a free path instead: `platform-policy` P-03) | `engineering-craft` presentation.md §7; ui/list-flex-layouts.md:16; ui/grid-table-layouts.md:40 |
| U-16 | **Counters tell the truth.** Affordability and logic read the true value the moment it changes; the count-up is decoration inside its motion-table cap that ends exactly on the server value; gains signed in the reward role, spends neutral; abbreviations follow the progression designer's display rule | presentation.md §7 |
| U-17 | **From source to destination.** A popup grows from the control that opened it and returns to it; rewards fly to the counter they raise and land with its bump. A world start point uses `Camera:WorldToScreenPoint` (accounts for the GUI inset) or `WorldToViewportPoint` (does not), whichever matches the ScreenGui's insets: probe once | Y/Camera.yaml:1254-1266, 1306-1312 |
| U-18 | **Frequent UI events merge.** Same-kind toasts and "+N" labels inside the merge window share one label with the sum; at most 3 toasts stacked, outside the play focus; other players' events stay small and never take the local player's attention motion | presentation.md §7; `ui-design` motion.md §8 |

## 5. Rules (final check)
- No interactive UI outside the core UI safe area; nothing critical over the default touch controls.
- No beta-only UI feature in a published game.
- No client-side grants; UI shows confirmed server state; no success before the result.
- No TextScaled reading text without a size constraint; no meaning by colour alone.
- Every screen reachable and usable with a gamepad.
- No tween duration, easing, colour or player-facing string typed in a screen script.

## 6. Self-review before returning (every line names its input)
Inputs: **C** Studio stills in the Device Simulator (budget: the main state at each size, every failure, and the states the UI designer's review slot names; never every state at every size) · **L** the play-test debug log (`engineering-craft` presentation.md §9) · **S** a Studio state read (`execute_luau` on Client; numbers for every state and size) · **G** a grep or code read · **T** an offline test · **D** the spec or a document · **P** the UI designer at the review slot (look, read order, feel at normal speed on a playable build). Every recipe is a screening aid: a failing or borderline reading is checked on the still or the code line before any fix note.

| ID | Look for | Input |
| --- | --- | --- |
| U-S01 | The functional pass ran: every state in the spec reached in a play-test, each with the real server data | L, C |
| U-S02 | Touch, mouse and gamepad each complete the main task; gamepad focus starts, moves and returns as the spec's focus map says; nothing needs hover or a long press only | C, S |
| U-S03 | Every state at the smallest phone, tablet, PC and TV sizes, one S read each: count of visible interactive elements whose `AbsolutePosition` and `AbsoluteSize` fall outside their ScreenGui's own rectangle under `CoreUISafeInsets` (run the Device Simulator probe of `engineering-craft` `references/probes.md` §4 once first), and of visible text objects with `TextFits` false (Y/TextLabel.yaml:481): both 0. Skip descendants of a ScrollingFrame (outside on purpose); a TextScaled label always fits. Stills: the main state at each size next to the approved mockup, plus every failure; nothing under the thumbs is judged on the phone still | S, C |
| U-S04 | Largest text size: the same `TextFits` read gives 0; reading text grows (no TextScaled on it: code read, since a scaled label always reports a fit); overlapping text judged on the stills of the main state and the failures | S, G, C |
| U-S05 | Motion: every tween is built from a motion-table row (the literals grep of `engineering-craft` `references/presentation.md` §10: hits only in the one helper, tokens or tests); reduced motion on: each row takes its reduced variant and the end state still explains the event | G, L, C |
| U-S06 | Most opaque background setting: tagged translucent backgrounds become opaque; text contrast on the weakest backdrop is the UI designer's S-18 measure (`look_check.py contrast`): the background box sits directly behind the text on the weakest backdrop the screen meets (the brightest for light text, the darkest for dark text); the text box is tight, with `--fg-stat p90` for light text and `p10` for dark text (a loose box or the wrong stat samples the backdrop: ratio near 1) | C, S |
| U-S07 | Attempt, pending, outcome: press line in the press frame or the next; with the reject switch no success line and the refusal line names the reason; with the delay switch the pending state shows; a second tap during an animation is accepted | L |
| U-S08 | Refusals and disabled states: each denial reason shows its message and icon at the control; only that control moves; spamming plays the refusal sound at most once per 0.5 s | L, C |
| U-S09 | Counters: buying right after a gain uses the new balance; the shown value ends on the server value after a burst; one label per merge window | T, L |
| U-S10 | Source to destination: the popup's first frame sits on its control and fly-to-HUD lands on its counter at the phone size (stills at start and end) | C |
| U-S11 | Open and close the screen 20 times, and respawn with it open: connection and instance counts return to baseline; a late answer is dropped | S |
| U-S12 | Every state defined; disabled states say why; status uses colour plus icon or text | C, D |
| U-S13 | Captures named for the UI designer's review slot (the states it names per size, a rejected request, reduced on, press frame folders for S-33) | D |

Project overlay: if `knowledge/overlays/ui-basics.md` exists, read it after this file; it wins for this game.
