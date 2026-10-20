---
title: UIGradient (engine class reference)
description: API reference for the UIGradient modifier — color/transparency gradients on UI elements. Properties, supported parents, performance constraints.
tags: [roblox, documentation, external-reference, priority-reference, ui, engine-class-reference]
---


> [!info] Source
> Roblox Engine API — `Class.UIGradient`. For **how to use** in context (color sequences, offset, rotation), see [[external/roblox-creator-docs/ui/appearance-modifiers#gradient|appearance-modifiers#gradient]]. This page is the property-level API surface plus performance constraints.

`Class.UIGradient` applies a color and transparency gradient to the UI elements rendered by its **parent** `Class.GuiObject`. Configurable via `Color` (`Datatype.ColorSequence`), `Transparency` (`Datatype.NumberSequence`), `Offset` (`Datatype.Vector2`), and `Rotation` (`number`).

> [!warning] Upgraded UIGradients are Studio Beta (checked 2026-10-20)
> `Type` (Linear / Radial / Conical), `TileMode` (Clamp / Repeat / Mirror), `Scale`, Path2D support and linear-space colour blending come from the **Upgraded UIGradients** beta (2026-09-02, File → Beta Features). **Not publishable** to live games yet. The official guide and API yaml show them without a beta marker. Staff guidance: stay under 1,000 gradients; animating scale, tile mode, type, offset or rotation is cheaper than animating colour or transparency ([DevForum, Roblox staff](https://devforum.roblox.com/t/studio-beta-upgraded-ui-gradients/4846594)).

> [!warning] Does not cascade
> `UIGradient` only applies to its **immediate** parent — it does **not** affect child or descendant GuiObjects. To gradient multiple objects, instance a separate `UIGradient` under each one.

## Supported parents

- `Class.Frame`
- `Class.TextLabel`
- `Class.TextButton`
- `Class.ImageLabel`
- `Class.ImageButton`
- `Class.ViewportFrame`

Also valid as a **child of `Class.UIStroke`** to make a gradient stroke (the gradient applies to the stroke, not the parent fill).

> [!warning] Unsupported parents
> `Class.ScrollingFrame` and `Class.TextBox` do **not** currently support `UIGradient`.

## Properties

| Property | Type | Default | Notes |
| --- | --- | --- | --- |
| `Color` | `Datatype.ColorSequence` | white→white | Color blended with the parent along the gradient direction. Behaves like `Class.Beam.Color` / `Class.Trail.Color` but in UI space. |
| `Enabled` | `boolean` | `true` | When `false`, the gradient is not applied. |
| `Offset` | `Datatype.Vector2` | `(0, 0)` | **Scalar** translation from the center of the parent. Pixel offset = `Offset * parent.AbsoluteSize`. Depending on `Rotation`, the gradient can become partially or fully invisible. |
| `Rotation` | `number` (degrees) | `0` | Clockwise rotation of the gradient axis. Control points snap to parent edges but maintain the rotation angle. |
| `Transparency` | `Datatype.NumberSequence` | `0→0` | Opacity along the gradient axis. Envelope values on `NumberSequenceKeypoint` are **ignored**. |

## Geometry — Offset + Rotation

- `Rotation = 0` → gradient runs **left → right**.
- `Rotation = 90` → gradient runs **top → bottom**.
- `Offset.X = 1` shifts the gradient one parent-width to the right; large `Offset` can push the gradient completely off-frame.
- `Offset` is **scalar** (parent-relative) — no pixel-absolute form. Use `Class.UIScale` or AbsoluteSize math if you need pixel-fixed gradient positioning.

## Performance constraints

These come straight from Roblox's own guidance — treat as hard rules on a mobile-first project:

- **Cap color stops at 6.** More keypoints in `Color` (and `Transparency`) increase per-frame cost. The Style Editor and design guide use ≤ 6.
- **Avoid `UIGradient` on objects with `TextStrokeColor3`** — the engine tries to blend the gradient with the stroke and can spike frame time. Use `Class.UIStroke` (the new modifier) instead if you need a stroke + gradient combo.
- **Don't reassign `Color` or `Transparency` frequently.** Every reassignment rebuilds the gradient color array, which is expensive. To animate a gradient, tween `Offset` or `Rotation`, or tween the parent's `BackgroundColor3` / `ImageColor3` / `TextColor3` instead.
- **Static gradient → consider a baked image.** For a never-changing gradient on a high-mutation parent, there is a **processing vs memory** trade: `UIGradient` recomputes per frame; a static gradient `Class.ImageLabel` (PNG/JPEG asset) is a one-shot texture upload. On mobile, asset memory is usually cheaper than per-frame blending.

## Animation guidance

- ✅ Tween `Offset` for a "sweep" effect (animated highlights).
- ✅ Tween `Rotation` for a spinning gradient (e.g. rarity card aura).
- ❌ Don't tween `Color` — every step rebuilds the keypoint sequence.
- ❌ Don't tween `Transparency` — same cost as `Color`.

## Related Files

- [[external/roblox-creator-docs/ui/appearance-modifiers]] - "how to use" overview for UIStroke / UIGradient / UICorner / UIPadding.
- [[external/roblox-creator-docs/ui/ui-stroke]] - UIStroke engine class reference (can host a `UIGradient` child for gradient strokes).
- [[external/roblox-creator-docs/ui/ui-corner]] - UICorner engine class reference.
- [[external/roblox-creator-docs/ui/ui-shadows-and-individual-corners]] - UIShadow + per-corner UICorner (live); a UIGradient on a UIShadow is the "Upgraded UIShadows" beta only.
- [[external/roblox-creator-docs/ui/animation]] - UI tweening (Offset/Rotation are the safe tween targets).
- [[external/roblox-creator-docs/ui/9-slice]] - 9-slice image scaling — alternative to gradient for cheap static fills.
- [[external/roblox-creator-docs/ui/index]] - User interface index.
