---
title: UIStroke (engine class reference)
description: API reference for the UIStroke modifier — outlines on text and UI borders. Properties, types, behaviors, layering rules.
tags: [roblox, documentation, external-reference, priority-reference, ui, engine-class-reference]
---


> [!info] Source
> Roblox Engine API — `Class.UIStroke`. For **how to use** in context (text outlines vs borders, gradient strokes), see [[external/roblox-creator-docs/ui/appearance-modifiers#stroke|appearance-modifiers#stroke]]. This page is the property-level API surface.

`Class.UIStroke` applies an outline to text or a UI border. The behavior depends on the parent: on a text object (`Class.TextLabel` / `Class.TextBox` / `Class.TextButton`) it outlines the text glyphs by default; on any other `Class.GuiObject` (e.g. `Class.Frame`) it draws a border.

You can layer multiple `Class.UIStroke` instances on one parent and order them via `ZIndex`.

> [!note] Beta gating
> Some `Class.UIStroke` properties may require enabling the **Improved UIStrokes** beta. Check the property notes below.

## Properties

| Property | Type | Default | Notes |
| --- | --- | --- | --- |
| `ApplyStrokeMode` | `Enum.ApplyStrokeMode` | `Contextual` | On text objects: `Contextual` outlines the text glyphs; `Border` outlines the object's rectangle. Ignored on non-text parents. |
| `BorderOffset` | `Datatype.UDim` | `0` | Additional offset to the stroke's position. Scale is relative to the parent's **minimum** of width/height. |
| `BorderStrokePosition` | `Enum.BorderStrokePosition` | `Center` | `Center` / `Inner` / `Outer` — where the stroke sits relative to the parent's border edge. |
| `Color` | `Datatype.Color3` | `(0, 0, 0)` | Stroke color. A child `Class.UIGradient` overrides flat color with a gradient stroke. |
| `Enabled` | `boolean` | `true` | When `false`, the stroke is not rendered. |
| `LineJoinMode` | `Enum.LineJoinMode` | `Round` | `Round` / `Bevel` / `Miter` — corner join style. |
| `StrokeSizingMode` | `Enum.StrokeSizingMode` | depends | Whether `Thickness` is measured in **pixels** or **scaled relative to the parent** (on text + `ScaledSize`, relative to font size). |
| `Thickness` | `number` | `1` | Stroke width. Units governed by `StrokeSizingMode`. |
| `Transparency` | `number` | `0` | `0` = opaque, `1` = invisible. Independent of parent's `BackgroundTransparency` / `TextTransparency` — enables "hollow" text or outline-only borders. |
| `ZIndex` | `number` | `0` | Render order among sibling `UIStroke` instances. Lower renders under (behind) higher. **Undefined order** when two siblings share the same `ZIndex`. |

## Behavior notes

### Text vs border (`ApplyStrokeMode`)

- **Default on text objects:** `Contextual` — applies stroke to the text glyphs.
- **`Border`:** treats the text object's rectangular background like a non-text frame.
- **Combining both:** parent **two** `UIStroke` instances to a text object — one `Contextual`, one `Border` — to control glyph outline and rectangular border independently.

### Border position + offset

- `BorderStrokePosition` snaps the stroke to `Center` / `Inner` / `Outer` of the parent's border edge.
- `BorderOffset` adds extra offset on top of that, scaled to the parent's **shorter** dimension.
- These compose; expect to use both for non-trivial border placement.

### Color, gradient, transparency

- Set `Color` for solid stroke color.
- Parent a `Class.UIGradient` **child** of the `UIStroke` for a gradient stroke. The parent object can carry its own `UIGradient` independently — the stroke gradient is local to the stroke.
- `Transparency` is independent of the parent's `BackgroundTransparency` / `TextTransparency`. To render an outline-only border, set parent's `BackgroundTransparency = 1` and `UIStroke.Transparency = 0`.

### Corner style

- `Round` (default) — smooth corner blend.
- `Bevel` — flat-cut corner.
- `Miter` — sharp pointed corner. Can extend far past the corner on acute angles; check before shipping.

### Thickness + tweening warning

> [!warning] Tween hazard
> Avoid [[external/roblox-creator-docs/ui/animation|tweening]] `Thickness` on a `UIStroke` attached to a **text** object. Roblox renders + stores a new glyph atlas at every intermediate thickness each frame, causing **performance spikes** and **text flicker**. Tween container size, color, or transparency instead.

### Layering rules

- Lower `ZIndex` renders behind higher.
- Two `UIStroke` siblings with the **same** `ZIndex` have **undefined** render order. Always pick distinct values when stacking strokes.

## Rich text

`UIStroke` properties can be applied to inline text segments via rich text tags (see [[external/roblox-creator-docs/ui/rich-text]]) without instancing a new `UIStroke` per segment.

## Related Files

- [[external/roblox-creator-docs/ui/appearance-modifiers]] - "how to use" overview for UIStroke / UIGradient / UICorner / UIPadding.
- [[external/roblox-creator-docs/ui/ui-gradient]] - UIGradient engine class reference (child of UIStroke for gradient strokes).
- [[external/roblox-creator-docs/ui/ui-corner]] - UICorner engine class reference (sibling on rounded-border parents).
- [[external/roblox-creator-docs/ui/ui-shadows-and-individual-corners]] - UIShadow + per-corner UICorner (live; upgrades in beta).
- [[external/roblox-creator-docs/ui/rich-text]] - Rich text markup including inline stroke tags.
- [[external/roblox-creator-docs/ui/animation]] - UI tweening (with stroke-on-text warning).
- [[external/roblox-creator-docs/ui/index]] - User interface index.
