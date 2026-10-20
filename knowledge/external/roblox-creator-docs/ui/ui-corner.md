---
title: UICorner (engine class reference)
description: API reference for the UICorner modifier — rounded corner deformation on GuiObjects. CornerRadius semantics, per-corner radii (live since 2026-06-23), shape rules, restrictions.
tags: [roblox, documentation, external-reference, priority-reference, ui, engine-class-reference]
---


> [!info] Source
> Roblox Engine API — `Class.UICorner`. For **how to use** examples, see [[external/roblox-creator-docs/ui/appearance-modifiers#corners|appearance-modifiers#corners]]. For **per-corner / individual radii** and `Class.UIShadow` status, see [[external/roblox-creator-docs/ui/ui-shadows-and-individual-corners]]. This page is the property-level API surface.

`Class.UICorner` applies rounded-corner deformation to its parent `Class.GuiObject`. Input events to the parent are **clipped** to the rounded shape (so a click in a now-deleted corner area does not hit the parent), but **descendants are not clipped** — child GuiObjects can still render outside the rounded silhouette.

## Properties

| Property | Type | Default | Notes |
| --- | --- | --- | --- |
| `CornerRadius` | `Datatype.UDim` | `(0, 8)` | Convenience shorthand. Setting it writes all four per-corner radii to the same value; reading it returns `TopLeftRadius`. **`NotReplicated`** — see the replication note below. |
| `TopLeftRadius` | `Datatype.UDim` | matches `CornerRadius` | Independent top-left radius. Setting `CornerRadius` overwrites this. |
| `TopRightRadius` | `Datatype.UDim` | matches `CornerRadius` | Independent top-right radius. Setting `CornerRadius` overwrites this. |
| `BottomLeftRadius` | `Datatype.UDim` | matches `CornerRadius` | Independent bottom-left radius. Setting `CornerRadius` overwrites this. |
| `BottomRightRadius` | `Datatype.UDim` | matches `CornerRadius` | Independent bottom-right radius. Setting `CornerRadius` overwrites this. |

> [!info] Per-corner radii are live (full release 2026-06-23). Style either `CornerRadius` or the per-corner properties, not both. Status detail: [[external/roblox-creator-docs/ui/ui-shadows-and-individual-corners]].

## CornerRadius semantics

`CornerRadius` is `NotReplicated` because under the hood it's an alias that **sets** all four per-corner radii at once and **reads** from `TopLeftRadius`. Implications:

- Writing `CornerRadius` overwrites any individual per-corner values you set.
- Setting any per-corner radius marks `CornerRadius` as "overridden by individual corners" in the Properties panel.
- In the [[external/roblox-creator-docs/ui/styling/index|Styling system]], style **either** `CornerRadius` **or** the per-corner properties, **never both** — combining them in style rules produces unexpected behavior.

## Shape rules

`Datatype.UDim` is `Scale` + `Offset`. UICorner applies it with these constraints:

- **X and Y radii are always equal** — radii are circular, not elliptical. You cannot create an ellipse via UICorner.
- **Scale uses the parent's shortest dimension** — `Scale = 0.5` produces a half-shortest-edge radius regardless of width vs height.
- **Pill clamp** — if `CornerRadius` resolves to a value greater than half the shortest dimension, the parent becomes a pill (semicircles capping the long axis). It does **not** keep growing past the pill.
- **Offset is pixel-exact** — `(0, 32)` rounds with a 32-pixel radius regardless of parent size.

## Restrictions

- **`Class.ScrollingFrame`** does **not** support `UICorner`. The frame's scroll mask clips before the corner rounding can apply. Use a 9-slice background ([[external/roblox-creator-docs/ui/9-slice]]) or wrap the `ScrollingFrame` in a parent `Frame` that owns the `UICorner`.
- **Input clipping vs descendant clipping** — input is clipped to the rounded shape; descendant rendering is **not**. A child `ImageLabel` that protrudes past the rounded edge still draws.
- **Decorative rounded borders** beyond simple radii — use 9-slice images instead. UICorner only handles uniform circular corners.

## Interaction with sibling modifiers

- **`Class.UIStroke`** — the stroke follows the rounded shape. `Round` `LineJoinMode` blends most cleanly with `UICorner`.
- **`Class.UIShadow`** — the shadow inherits the rounded corners. Release-note known issue: shadows may appear **jagged** on elements with very large corner radii ([[external/roblox-creator-docs/ui/ui-shadows-and-individual-corners]]).
- **`Class.UIGradient`** — gradient fills clip to the rounded shape correctly.

## Per-corner use cases

- **Speech bubbles** — square the corner pointing at the speaker; round the other three.
- **Tab headers** — round top corners, square bottom corners.
- **Segmented button strips** — first button rounds its outer-left corners, last button rounds its outer-right corners, middle buttons stay square.
- **Asymmetric callouts / one-sided callouts** — round only the "open" side.
- **Leaf / lens shapes** — two opposite corners with large radii, the other two flat.

## Related Files

- [[external/roblox-creator-docs/ui/appearance-modifiers]] - "how to use" overview for UIStroke / UIGradient / UICorner / UIPadding.
- [[external/roblox-creator-docs/ui/ui-shadows-and-individual-corners]] - **UIShadow + per-corner UICorner status and recipes.**
- [[external/roblox-creator-docs/ui/ui-stroke]] - UIStroke engine class reference (composes with UICorner on rounded borders).
- [[external/roblox-creator-docs/ui/ui-gradient]] - UIGradient engine class reference (clips to UICorner shape).
- [[external/roblox-creator-docs/ui/9-slice]] - 9-slice image scaling — alternative for decorative rounded borders.
- [[external/roblox-creator-docs/ui/scrolling-frames]] - ScrollingFrame (does **not** support UICorner directly).
- [[external/roblox-creator-docs/ui/styling/index]] - Universal styling (don't style CornerRadius + per-corner together).
- [[external/roblox-creator-docs/ui/index]] - User interface index.
