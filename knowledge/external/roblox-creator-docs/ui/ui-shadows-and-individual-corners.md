---
title: UIShadow and individual corner rounding
description: New native UI capabilities — UIShadow drop shadows/glows and per-corner UICorner radii. Base features live since 2026-06-23; the 2026-10-14 "Upgraded UIShadows" additions are Studio Beta (not publishable).
tags: [roblox, documentation, external-reference, priority-reference, ui]
---


> [!warning] Status (checked 2026-10-20; project-authored page, the official guide is [[external/roblox-creator-docs/ui/appearance-modifiers#shadow|appearance-modifiers#shadow]])
> - **Live, publishable:** base `Class.UIShadow` (BlurRadius, Color, Offset, Spread, Transparency, Enabled, ZIndex) and per-corner `Class.UICorner` radii. Beta 2026-05-14, full release 2026-06-23 ([DevForum, Roblox staff](https://devforum.roblox.com/t/studio-beta-new-ui-capabilities-shadows-individual-corners/4636263)). The "New UI Capabilities" beta flag is gone.
> - **Studio Beta, NOT publishable:** "Upgraded UIShadows" (2026-10-14): `Mode = Text` glyph shadows, `Inset`, `ShowBehindParent = false`, and a child `Class.UIGradient` on a shadow. Enable: File → Beta Features → **Upgraded UIShadows**. Known issues: Spread/Inset/ShowBehindParent do nothing in text mode; ShowBehindParent is ignored when Inset is true; rich text ignores shadow Color and Transparency ([DevForum, Roblox staff](https://devforum.roblox.com/t/studio-beta-upgraded-uishadow-capabilities/4934553)).
> - The API yaml has no beta markers. Do not read a property's presence there as "live".

Roblox is shipping two long-requested native UI primitives that replace external image assets and 9-slice workarounds for depth/glow effects and unique corner shapes:

- [Individual UICorner rounding](#individual-uicorner-rounding) — per-corner radius on `Class.UICorner`.
- [UIShadow](#uishadow-drop-shadows-and-glows) — native 2D drop-shadow / glow modifier on any frame-like GuiObject.

Both work in Explorer/Properties, the [[external/roblox-creator-docs/ui/styling/index|Styling system]], and from script. They compose with existing modifiers like `Class.UIStroke` and `Class.UIGradient`.

## Individual UICorner rounding

`Class.UICorner` previously applied one radius to all four corners via `Class.UICorner.CornerRadius|CornerRadius`. Four new per-corner properties unlock independent rounding:

- `TopLeftRadius` (`Datatype.UDim`)
- `TopRightRadius` (`Datatype.UDim`)
- `BottomLeftRadius` (`Datatype.UDim`)
- `BottomRightRadius` (`Datatype.UDim`)

### Relationship to CornerRadius

The legacy `CornerRadius` property is now an **alias** that writes all four per-corner radii at once and reads from `TopLeftRadius`. Existing experiences keep working unchanged.

Interaction rules to remember:

- Setting `CornerRadius` **overwrites** any per-corner values.
- Setting any per-corner radius marks `CornerRadius` as "overridden by individual corners" in Properties.
- In the Style Editor, style **either** `CornerRadius` **or** the per-corner properties, never both. Styling both produces unexpected behavior (release-note known issue).

### Use cases

- Speech bubbles (one square corner pointing at the speaker).
- Segmented tab/button strips (rounded outer bookends, square inner corners).
- Tab headers (rounded top, flat bottom).
- One-sided callouts and asymmetric callout cards.
- Leaf or pill shapes via two opposite-corner large radii.

### From script

```lua
local frame = Instance.new("Frame")
frame.Size = UDim2.fromOffset(200, 200)
frame.BackgroundColor3 = Color3.fromRGB(40, 90, 200)
frame.Parent = screenGui

local corner = Instance.new("UICorner")
-- Leaf shape: round only top-right and bottom-left
corner.TopRightRadius = UDim.new(0, 80)
corner.BottomLeftRadius = UDim.new(0, 80)
corner.TopLeftRadius = UDim.new(0, 0)
corner.BottomRightRadius = UDim.new(0, 0)
corner.Parent = frame
```

Per-corner radii use `Datatype.UDim` (scale + offset), same as `CornerRadius`. Scale is a percentage of the parent's shortest dimension.

## UIShadow drop shadows and glows

`Class.UIShadow` is a new modifier primitive that parents to any frame-like GuiObject and renders a 2D shadow **below** the parent. Shadows are purely visual:

- They do not affect layout.
- They do not trigger recalculations.
- An instance can carry **multiple** `Class.UIShadow` children, layered via `ZIndex`.
- Not supported on `Class.Path2D`.

For `Class.TextLabel` / `Class.TextBox` / `Class.TextButton`, the shadow applies to the element's **rectangular background**, not the text glyphs. Native text-glyph shadows are not part of this release.

### Properties

| Property | Type | Notes |
| --- | --- | --- |
| `BlurRadius` | `Datatype.UDim` | Softness. Low = sharp/hard edges, high = diffuse glow. Max `1000`. Scale is a percentage of the parent's **shortest dimension**. |
| `Color` | `Datatype.Color3` | Shadow tint. Use saturated colors for **glow / aura** effects, dark for traditional drop shadow. |
| `Transparency` | `number` | `0` = fully opaque, `1` = invisible. |
| `Offset` | `Datatype.UDim2` | Position relative to parent, simulating a light-source direction. Scale is a percentage of parent's dimensions. |
| `Spread` | `Datatype.UDim2` | Expand (positive) or shrink (negative) the shadow vs the parent. **Note:** type is `UDim2`, not `UDim`. Scale-relative properties like `BlurRadius`/`Offset` are **not** affected by Spread. |
| `ZIndex` | `integer` (negative only) | Layer order among multiple shadows. All shadows render **below** the parent, so `ZIndex` is **clamped to negative values**. |

### Inheritance from parent

- If the parent is rotated via `Class.GuiObject.Rotation|Rotation`, the shadow rotates with it.
- If the parent has rounded corners via `Class.UICorner`, the shadow inherits the rounded corner shape.

### Limitations

- Text-glyph shadows, inset shadows and gradient shadows exist only in the **Upgraded UIShadows** beta (not publishable, see the status box).
- No `Class.Path2D` or texture support.

> [!note] Style Editor caveat
> Release-note known issue: `UIShadow.ZIndex` in the Style Editor is not yet clamped to negative values. Stick to scripted/Property-panel values until fixed.

> [!note] Large corner radii + shadow
> Release-note known issue: shadows may appear **jagged** when parented to elements with a large corner radius. Roblox is investigating; expect rough edges on pill-shaped buttons with shadows until patched.

### From script

```lua
-- Find the parent ScreenGui by searching up the instance tree
local screenGui = script:FindFirstAncestorWhichIsA("ScreenGui")
if not screenGui then
    warn("Could not find a parent ScreenGui for the shadow demo!")
    return
end

-- 1. Create and center the parent frame
local parentFrame = Instance.new("Frame")
parentFrame.Name = "ShadowFrame"
parentFrame.Size = UDim2.fromOffset(150, 150)
parentFrame.AnchorPoint = Vector2.new(0.5, 0.5)
parentFrame.Position = UDim2.fromScale(0.5, 0.5)
parentFrame.BackgroundColor3 = Color3.fromRGB(255, 255, 255)
parentFrame.BorderSizePixel = 0
parentFrame.Parent = screenGui

-- 2. Create and apply the UIShadow
local uiShadow = Instance.new("UIShadow")
uiShadow.BlurRadius = UDim.new(0, 30)
uiShadow.Color = Color3.new(0, 0, 0)
uiShadow.Transparency = 0.5
uiShadow.Offset = UDim2.new(0, 10, 0, 10)
uiShadow.Parent = parentFrame
```

### Glow vs drop shadow recipe

| Effect | Color | Offset | BlurRadius | Spread | Transparency |
| --- | --- | --- | --- | --- | --- |
| Soft drop shadow | `Color3.new(0, 0, 0)` | `(0, 6, 0, 8)` | `(0, 16)` | `(0, 0, 0, 0)` | `0.5` |
| Hard drop shadow | `Color3.new(0, 0, 0)` | `(0, 2, 0, 4)` | `(0, 4)` | `(0, 0, 0, 0)` | `0.3` |
| Neon glow | rarity color, e.g. `Color3.fromRGB(255, 200, 70)` | `(0, 0, 0, 0)` | `(0, 40)` | `(0, 8, 0, 8)` | `0.2` |
| Status-tint aura | element color (Fire/Ice/Lightning etc.) | `(0, 0, 0, 0)` | `(0, 24)` | `(0, 4, 0, 4)` | `0.35` |

(`Offset` and `Spread` are both `UDim2` — written above as `(scaleX, offsetX, scaleY, offsetY)`. `BlurRadius` is `UDim` — `(scale, offset)`.)

### Multi-shadow layering

Multiple `Class.UIShadow` children on one parent stack via `ZIndex`. Common patterns:

- **Ambient + key light:** one wide diffuse shadow (`BlurRadius` ~40, `Offset` 0) for an ambient halo, plus one tight directional shadow (`BlurRadius` ~8, `Offset` (0,4,0,6)) for a grounded drop shadow.
- **Inner-glow + outer-glow:** color-matched stacked shadows with different `Spread` values to mimic a thicker neon ring.

## Performance budget

From the release notes:

- `UIShadow` is **consistently faster** than 9-sliced ImageLabel shadows it replaces.
- Recommended on-screen budget: **no more than 100 UIShadows simultaneously**.
- Per-corner rounding has **no measurable place-wide performance impact** vs uniform `CornerRadius`. Use it freely.

The 100-shadow budget is the load-bearing number for any project planning a heavily-decorated HUD plus inventory plus tooltips visible at once.

## Known issues (from the 2026 release posts)

- Shadows can appear jagged on elements with very large corner radii. Roblox is investigating.
- Styling a `Class.UICorner` with **both** `CornerRadius` and per-corner radii produces unexpected behavior. Style one or the other.
- `UIShadow.ZIndex` is not yet clamped to negative values in the Style Editor (Properties panel and script paths still enforce it correctly).


## Related Files

- [[external/roblox-creator-docs/ui/appearance-modifiers]] - UICorner / UIStroke / UIGradient / UIPadding base reference.
- [[external/roblox-creator-docs/ui/index]] - User interface index.
- [[external/roblox-creator-docs/ui/size-modifiers]] - UIScale + AutomaticSize + size constraints.
- [[external/roblox-creator-docs/ui/9-slice]] - 9-slice image scaling (the workaround UIShadow replaces).
- [[external/roblox-creator-docs/ui/styling/index|styling]] - Universal styling / Style Editor.
- [[external/roblox-creator-docs/studio/explorer]] - Explorer window.
- [[external/roblox-creator-docs/studio/properties]] - Properties window.
