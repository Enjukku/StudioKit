> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Facts extracted by a researcher agent (claude-sonnet-5-5, medium) from the docs mirror (upstream 7400643) and Roblox staff DevForum posts 2026; spot-checked by the orchestrator. Paths relative to `knowledge/external/roblox-creator-docs/`; Y = `_api-reference/classes/`. "practice" = common industry practice, not a Roblox doc.

# Roblox UI facts (2026)

## Layout and scaling
| Fact | Source |
| --- | --- |
| Scale = fraction of the parent; Offset = pixels; they add. `AnchorPoint` is the origin for position and size | ui/position-and-size.md:19-63 |
| Use Scale with AnchorPoint; adapt by display size (75 % width is huge on a 4K TV) | projects/cross-platform.md:117-121 |
| `UIAspectRatioConstraint` (width / height), `UISizeConstraint` (Min/Max); a constraint overrides the size a layout gives | ui/size-modifiers.md:87-117 |
| `UIScale` multiplies size of the object and children: design zoom and hover pops | ui/size-modifiers.md:15-17 |
| `AutomaticSize`: Size becomes the minimum; with TextWrapped + AutomaticSize Y the label grows. ScrollingFrame uses `AutomaticCanvasSize` | ui/size-modifiers.md:23-79 |
| `UIListLayout` controls siblings' position and size; Padding only between items (`UIPadding` for the edge); Flex (`HorizontalFlex`, `VerticalFlex`, `UIFlexItem` Fill/Grow/Shrink/Custom) has a slight cost; `UIGridLayout` for strict grids | ui/list-flex-layouts.md:16-128 |
| `ScreenGui.ScreenInsets`: CoreUISafeInsets (default; clear of the top bar and cutouts; use for interactive UI), DeviceSafeInsets (cutouts only), TopbarSafeInsets (beside the top-bar buttons), None (backgrounds only). `IgnoreGuiInset` is the legacy switch; set ScreenInsets directly. New work does not rely on `SafeAreaCompatibility` | _includes/ui/screen-insets.md:13-31; Y/ScreenGui.yaml:38-199 |
| Runtime insets: `GuiService:GetInsetArea(insets)`, `GuiService.TopbarInset` (changes; listen to it) | Y/GuiService.yaml:318-630 |
| Phones: default controls sit bottom-left (move) and bottom-right (jump); keep UI out of them; frequent buttons in thumb reach; place custom buttons relative to jump; contextual buttons only when needed | ui/position-and-size.md:131-212 |
| Device class: `GuiService.ViewportDisplaySize` Small (phones, tablets), Medium (laptops, monitors), Large (TVs). `IsTenFootInterface` is deprecated | Y/GuiService.yaml:372-386; projects/cross-platform.md:129-152 |
| Console: viewers 8-10 ft away; design for low resolution first; TV-safe area; every element reachable with D-pad, select and back in a few moves | production/publishing/console-guidelines.md:17-59 |
| Gamepad: `GuiService.SelectedObject`, `GuiService:Select(parent)` (lowest `SelectionOrder`), `NextSelectionUp/Down/Left/Right`, `SelectionImageObject` | Y/GuiService.yaml; Y/GuiObject.yaml:531-810 |
| Touch target size: no Roblox number. Practice: ≥ 44 pt (Apple HIG) / 48 dp (Material) | practice |

## Text
| Fact | Source |
| --- | --- |
| `TextScaled` ignores TextSize, forces wrapping, can become unreadably small; docs prefer AutomaticSize; never combine the two; with TextScaled add `UITextSizeConstraint` (MinTextSize ≥ 9, a max for TVs) | Y/TextLabel.yaml:511-547; ui/size-modifiers.md:97-107 |
| `TextFits`, `TextBounds`; `TextService:GetTextBoundsAsync(GetTextBoundsParams)` yields (pcall) | Y/TextLabel.yaml:481-494; Y/TextService.yaml:144-165 |
| `FontFace` (Font datatype) replaces the legacy `Font` enum | Y/TextLabel.yaml:121-158 |
| `GuiService.PreferredTextSize` (Medium → Largest): AutomaticSize text grows; constrained text stops at its max; **TextScaled text does not scale** | production/publishing/accessibility.md:168-182 |
| RichText tags are stripped by localisation: re-apply them in translated strings | ui/rich-text.md:13-35 |
| Text players type and others see must be filtered on the server (`platform-policy` § D) | ui/text-filtering.md |

## Styling system (live)
| Fact | Source |
| --- | --- |
| `StyleSheet` holds `StyleRule`s; one `StyleLink` per ScreenGui tree; tokens are StyleSheet attributes used as `"$Name"`; themes via `StyleDerive` with shared token names | ui/styling/index.md:15-31 |
| Selectors: class, `.tag`, `#name`, `:Hover`/`:Press` states, `@query`; `>` child, `>>` descendant, `::UICorner` pseudo-instances; higher `Priority` wins | Y/StyleRule.yaml:21-135 |
| `StyleQuery` (live 2026-05-11): MinSize, MaxSize, AspectRatioRange, PreferredInput, PreferredTextSize, ReducedMotionEnabled, ViewportDisplaySize; built-ins `@ViewportDisplaySizeSmall`, `@PreferredInputTouch`, `@ReducedMotionEnabledTrue` … Wrong names fail silently; size queries that also style Size can flicker | Y/StyleQuery.yaml; DF 4566519 (missmandypanda) |
| Transitions (live 2026-07-27): `StyleRule:SetPropertyTransition` with TweenInfo; fire only on style changes (tag or state), not layout changes; repeat and reverse ignored; set `AutoButtonColor = false` on styled hover buttons | Y/StyleRule.yaml:277-549; DF 4646870 |
| Styles for shared look (colours, fonts, radii, hover, device and accessibility variants, themes); direct properties for one-off or script-driven state. Only properties on the compatibility list are styleable | ui/styling/index.md:295-330; ui/styling/compatibility.md |

## Appearance
| Fact | Status | Source |
| --- | --- | --- |
| `UICorner` Scale = fraction of the shortest edge (0.5 = pill); per-corner radii; style CornerRadius or the per-corner set, not both | live (2026-06-23) | ui/appearance-modifiers.md:380-416 |
| `UIStroke`: Contextual on text = text outline; Border mode for bounds; `BorderStrokePosition`, `LineJoinMode`; **do not tween Thickness on text** (spikes, flicker) | live | ui/appearance-modifiers.md:244-376 |
| `UIGradient` Color, Transparency, Offset, Rotation; not on ScrollingFrame or TextBox; does not cascade | live | ui/appearance-modifiers.md:34-40 |
| `UIGradient` Type (Radial, Conical), TileMode, Scale, Path2D | **beta, not publishable** (2026-09-02) | DF 4846594 |
| `UIShadow` BlurRadius, Color, Transparency, Offset, Spread, ZIndex, Enabled; follows corners and rotation; ≤ 100 on screen; faster than 9-slice shadows | live (2026-06-23) | ui/appearance-modifiers.md:439-561; DF 4636263 |
| `UIShadow` Mode = Text, Inset, ShowBehindParent = false, gradient child | **beta, not publishable** (2026-10-14) | DF 4934553 |
| `CanvasGroup`: fades or tints a whole group, clips to rounded corners and rotation; extra texture memory, blank past the cap; keep its size static | live | Y/CanvasGroup.yaml:12-31 |
| Clipping rotated elements and Path2D: on by default since 2026-09-24; `StarterGui.ClipsDescendantsSupportsRotation` is **removed November 2026**; ClipsDescendants still does not clip to UICorner (use CanvasGroup) | live | DF 4737864 (mirror pages still show the old opt-in) |
| Images: 9-slice (`ScaleType = Slice`, `SliceCenter`); sprite sheets (`ImageRectOffset`, `ImageRectSize`) load faster for many small icons | live | ui/9-slice.md:58-76; Y/ImageLabel.yaml:18-33 |

## Input and feedback
| Fact | Status | Source |
| --- | --- | --- |
| `GuiButton.Activated`: click, touch release, gamepad A; use it, not `MouseButton1Click` (mouse only) | live | Y/GuiButton.yaml:211-249 |
| `SecondaryActivated`: right-click, long press (> 1 s), R3, Alt+Enter; no standard visual cue, so always give a visible alternative | live (2026-07-06) | DF 4720108 (BitwiseAndrea) |
| `HoverHapticEffect`, `PressHapticEffect` on buttons | live | Y/GuiButton.yaml:72-146 |
| `GuiObject.Interactable = false` locks state to NonInteractable | live | Y/GuiObject.yaml:450-480 |
| `InputActionLabel` (binding hints) | **beta, not publishable**; build hints from `InputAction.PreferredBinding` meanwhile | DF 4779420 |
| `UserInputService.PreferredInput` (Touch, KeyboardAndMouse, Gamepad) beats `TouchEnabled` checks; listen for changes | live | input/index.md:31-102 |
| `GuiService.ReducedMotionEnabled` → tween time 0 or a fade; `GuiService.PreferredTransparency` multiplies background transparency | live | production/publishing/accessibility.md:102-245 |
| Accessibility: enough contrast; never meaning by colour alone or sound alone | live | production/publishing/accessibility.md:46-96 |
| `ZIndexBehavior` Sibling (default); ZIndex gaps of 100; `ScreenGui.DisplayOrder` layers whole screens | live | Y/GuiObject.yaml:943-965; Y/ScreenGui.yaml:81-90 |
| `ResetOnSpawn` (default true) re-clones the ScreenGui on respawn; false only works on a direct child of StarterGui. `ScreenGui.Enabled = false` stops render and input | live | ui/on-screen-containers.md:35-82 |
| `GuiObject.Draggable` deprecated: use `UIDragDetector`. Keep `GuiButton.Style = Custom` | live | Y/GuiObject.yaml:356-369 |

## Not documented (do not state numbers)
Touch target size, text expansion for translation, UI element-count limits, VR UI sizes, virtualised list support, colour-blind settings API.
