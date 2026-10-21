---
name: ui-basics
description: Build and review Roblox UI that works on every device - scaling, safe areas, readable text, touch and gamepad, accessibility, the 2026 styling system, button states, UI performance. Use when building a screen, HUD, shop, menu, popup or button, for "the UI is cut off on phones", "text is too small", "it does not work with a controller". Engineering only; look and UX come from the UI designer.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Kit skill: universal. J001 step 8. Evidence: `references/facts.md` (docs mirror upstream 7400643; Roblox staff posts 2026; Y = `_api-reference/classes/`). A deep UI/UX designer role will come later from owner material and will build on this.

# UI basics: every screen works on every device

## 1. When this skill starts
A screen, HUD element, popup or button is built or changed. The **look** (style, colours, art) comes from the game's UI style note and an approved mockup; this skill makes it work. If no approved look exists for a player-facing screen, ask for one before building.

## 2. Read this file when
| You need | Open |
| --- | --- |
| A property, layout rule, inset, text, styling, appearance or input fact; live vs beta | `references/facts.md` |
| Button feel, popups, toasts, currency counters, fly-to-HUD, timings | `references/ui-effects.md` |
| Text players type that others see | `platform-policy` skill § D (filtering) |
| UI cost questions beyond §4 | `performance` skill |

## 3. Steps
1. **Flow first.** For the screen: where am I, what can I do, what just happened, what next. The fewest steps per device. Agree the flow before visuals.
2. **Structure:** one ScreenGui per feature; `ScreenInsets = CoreUISafeInsets` for anything interactive; `ResetOnSpawn = false` for persistent HUD; `DisplayOrder` for layering screens.
3. **Size and place** with Scale + AnchorPoint, constraints and one outer `UIScale` for pixel-designed panels (U-02).
4. **Style** shared look with a StyleSheet and tokens; per-device and accessibility variants with style queries (U-05).
5. **Wire** input with `Activated`; the button sends a request; the UI shows the server-confirmed result (U-07).
6. **States:** idle, hover, pressed, disabled with a reason, loading, cooldown, error. No action may need hover or a long press only.
7. **Test** in the Device Simulator at a phone, a tablet, a PC and a TV size, with touch, mouse and gamepad, Largest text size and reduced motion on. Screenshot each.

## 4. Craft core
| ID | Practice | Evidence |
| --- | --- | --- |
| U-01 | **Safe areas:** interactive UI under `ScreenInsets = CoreUISafeInsets` (clear of the top bar and notches); `None` only for full-screen backgrounds; read `GuiService.TopbarInset` when placing next to the top bar. Set ScreenInsets directly, not `IgnoreGuiInset` | _includes/ui/screen-insets.md; Y/ScreenGui.yaml |
| U-02 | **Scaling:** HUD edges use Scale positions with AnchorPoint at the edge they hug; panels are designed at one canvas size and fitted with one outer `UIScale` plus `UIAspectRatioConstraint`; `UISizeConstraint` caps sizes on TVs. Never fix overflow by scaling an already-overflowing container | ui/position-and-size.md; ui/size-modifiers.md |
| U-03 | **Thumb zones:** nothing important in the bottom-left (move) or bottom-right (jump) control areas; frequent buttons in thumb reach; touch targets ≥ 44 pt with gaps (practice; Roblox gives no number); contextual buttons appear only when needed | ui/position-and-size.md:131-212 |
| U-04 | **Text:** prefer `AutomaticSize` + `TextWrapped` over `TextScaled`; if TextScaled, add `UITextSizeConstraint` (min ≥ 9). TextScaled ignores the player's PreferredTextSize, so key reading text must not use it. `FontFace`, not the Font enum | Y/TextLabel.yaml:511-547; accessibility.md:168-182 |
| U-05 | **Styling system for shared look:** tokens (`$Primary`, `$Radius`) in a StyleSheet; hover and press via state selectors and transitions; device and accessibility variants with built-in queries (`@ViewportDisplaySizeSmall`, `@PreferredInputGamepad`, `@ReducedMotionEnabledTrue`). Direct properties only for one-off or script-driven values | ui/styling/; DF 4566519, 4646870 |
| U-06 | **Every device can reach everything:** gamepad selection works on every screen (`GuiService:Select`, `NextSelection*`, a visible selection image); hints follow `UserInputService.PreferredInput`; a long-press or right-click action (`SecondaryActivated`) always has a visible alternative; **no action works only on hover** (touch and gamepad have no hover) | Y/GuiService.yaml; input/index.md; DF 4720108 |
| U-07 | **UI never grants.** Buttons use `Activated`, send a request, and update from the server's confirmed answer. Optimistic display only when it can be reverted cleanly. **Robux prices are read from Roblox** (`MarketplaceService:GetProductInfoAsync`), never typed or taken from a data file (`platform-policy` P-05) | `networking-security` N-03 |
| U-08 | **Native modifiers first (live):** `UIShadow` for drop shadows and glows (≤ 100 on screen), per-corner `UICorner`, `UIStroke`, `UIGradient` (Color, Transparency, Offset, Rotation). **Do not ship betas**: text or inset shadows, radial or conical gradients, `InputActionLabel` (Studio only until released) | DF 4636263, 4934553, 4846594, 4779420 |
| U-09 | **Clipping:** rotated clipping is default; `ClipsDescendantsSupportsRotation` disappears November 2026, so never set it; clip to rounded corners with a CanvasGroup | DF 4737864 |
| U-10 | **Accessibility:** contrast; meaning never by colour or sound alone (add icons and text); honour `ReducedMotionEnabled` and `PreferredTransparency`; test Largest text size | production/publishing/accessibility.md |
| U-11 | **UI cost:** pool list rows and update them in place; no tween of `UIStroke.Thickness` on text; few CanvasGroups and keep them static-sized; animate gradient offset and rotation, not colour; sprite sheets for many small icons; fewer layers on always-on HUD | Y/CanvasGroup.yaml; ui/appearance-modifiers.md:258; DF 4846594 |
| U-12 | **Cleanup:** every connection, tween and cloned instance of a screen has one cleanup owner that runs on close; reopening a screen 20 times leaves no extra connections. A server answer that arrives after the screen closed or the character respawned is dropped (check a generation token). UI tied to world objects handles the object streaming out; every `WaitForChild` has a timeout | `knowledge/reference/architecture/strong-codebases-2026-10.md` A-10 |

## 5. Rules (final check)
- No interactive UI outside the core UI safe area; nothing critical over the default touch controls.
- No beta-only UI feature in a published game.
- No client-side grants; UI shows confirmed server state.
- No TextScaled reading text without a size constraint; no meaning by colour alone.
- Every screen reachable and usable with a gamepad.

## 6. Self-check before returning
- [ ] Screenshots at phone, tablet, PC and TV sizes, next to the approved mockup.
- [ ] Touch, mouse and gamepad each complete the main task.
- [ ] No action needs hover or a long press only; every long-press or right-click action has a visible button too.
- [ ] Largest text size and reduced motion checked.
- [ ] All states defined; disabled states say why.
- [ ] Open and close the screen repeatedly: connection and instance counts return to baseline.

Project overlay: if `knowledge/overlays/ui-basics.md` exists, read it after this file; it wins for this game.
