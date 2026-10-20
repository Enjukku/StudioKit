---
title: Text & image labels
description: Explore how labels display customizable text and images in user interfaces.
tags: [roblox, documentation, external-reference, priority-reference, ui]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [ui/labels.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/ui/labels.md). Published page: [https://create.roblox.com/docs/ui/labels](https://create.roblox.com/docs/ui/labels).

import TextFiltering from '../includes/text-filtering/text-filtering.md'

**Labels** are `Class.GuiObject|GuiObjects` that let you display customizable text and images [[external/roblox-creator-docs/ui/on-screen-containers|on‑screen]] or [[external/roblox-creator-docs/ui/in-experience-containers|in-game]]. There are two types of labels:

- A `Class.TextLabel` is a rectangle with text that you can style through customizable properties. This is the primary way to display text in a game.

- An `Class.ImageLabel` is a rectangle with an image [[external/roblox-creator-docs/projects/assets/index|asset]] that you can style through customizable properties. Alongside [[external/roblox-creator-docs/parts/textures-decals|textures and decals]], this lets you display images in a game.

## Create labels on the screen

Labels on a screen are useful for things like displaying images of characters
with dialog.

To add a label to a screen:

1. In the **Explorer** window, select **StarterGui** and add a **ScreenGui**.

   1. Hover over StarterGui and click the &CirclePlus; button. A contextual menu displays.

   1. From the menu, insert a **ScreenGui**.

2. Select the new **ScreenGui** and add a label.

   1. Hover over **ScreenGui** and click the &CirclePlus; button. A contextual menu displays.

   1. From the menu, insert a **TextLabel** or **ImageLabel**.

   <img src="../assets/ui/button-text-input/ImageButton-Screen-New.jpg" width="80%" />

## Create labels on part faces

Labels on a part are useful for things like creating billboards, posters, and
wallpaper.

To add a label to the face of a part:

1. In the **Explorer** window, insert a **SurfaceGui** onto the part.

   1. Hover over the part instance and click the &CirclePlus; button. A contextual menu displays.

   1. From the menu, insert a **SurfaceGui**.

2. Select the new **SurfaceGui** and add a label.

   1. Hover over the **SurfaceGui** and click the &CirclePlus; button. A contextual menu displays.

   1. From the menu, insert a **TextLabel** or **ImageLabel**.

   <img src="../assets/ui/button-text-input/ImageButton-SurfaceGui-New.jpg" width="80%" />

   <Alert severity="warning">
   If you don't see the button, try [[external/roblox-creator-docs/parts/textures-decals#choose-a-face|choosing a different face]] in the <b>Face</b> property of the <b>SurfaceGui</b>.
   </Alert>

## Adjust ImageLabel properties

All images within an `Class.ImageLabel` must be assets that have been [[external/roblox-creator-docs/projects/assets/manager#asset-import|imported]] to Studio. While the image automatically scales to fit the area of the rectangle, the image looks best when it displays at its native resolution.

You can customize the visual appearance of an image with the following
properties:

- `Class.ImageLabel.ImageColor3|ImageColor3`

- `Class.ImageLabel.ImageTransparency|ImageTransparency`

- `Class.GuiObject.BackgroundTransparency|BackgroundTransparency`

For example, to display only the image and hide the rectangle, set the `Class.GuiObject.BackgroundTransparency|BackgroundTransparency` property to `1`.


## Related Files

- [[external/roblox-creator-docs/ui/2D-paths]] - 2D paths.
- [[external/roblox-creator-docs/ui/3D-drag-detectors]] - 3D drag detectors.
- [[external/roblox-creator-docs/ui/frames]] - Frames.
- [[external/roblox-creator-docs/ui/grid-table-layouts]] - Grid and table layouts.
- [[external/roblox-creator-docs/ui/in-experience-containers]] - In-game UI containers.
- [[external/roblox-creator-docs/ui/list-flex-layouts]] - List and flex layouts.
- [[external/roblox-creator-docs/ui/on-screen-containers]] - On-screen UI containers.
- [[external/roblox-creator-docs/ui/page-layouts]] - Page layouts.
- [[external/roblox-creator-docs/ui/position-and-size]] - Position and size UI objects.
- [[external/roblox-creator-docs/ui/proximity-prompts]] - Proximity prompts.
- [[external/roblox-creator-docs/ui/rich-text]] - Rich text markup.
- [[external/roblox-creator-docs/ui/scrolling-frames]] - Scrolling frames.
- [[external/roblox-creator-docs/ui/size-modifiers]] - Size modifiers and constraints.
- [[external/roblox-creator-docs/ui/buttons]] - Text & image buttons.
- [[external/roblox-creator-docs/ui/text-filtering]] - Text filtering.
- [[external/roblox-creator-docs/ui/text-input]] - Text input fields.
- ...and 11 more local docs.
