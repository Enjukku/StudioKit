---
title: Frames
description: Frames are basic containers for UI objects.
tags: [roblox, documentation, external-reference, priority-reference, ui]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [ui/frames.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/ui/frames.md). Published page: [https://create.roblox.com/docs/ui/frames](https://create.roblox.com/docs/ui/frames).

import Clipping from '../includes/ui/clipping.md'

Basic `Class.Frame|Frames` act as containers for other `Class.GuiObject|GuiObjects` such as [[external/roblox-creator-docs/ui/labels|labels]] and [[external/roblox-creator-docs/ui/buttons|buttons]]. You can apply frames to display on a user's [[external/roblox-creator-docs/ui/on-screen-containers|screen]] or on a [[external/roblox-creator-docs/ui/in-experience-containers|surface]] within the game.

<img src="../assets/ui/ui-objects/Frame-Example.jpg" width="840" alt="Example Frame on the screen containing a TextLabel, TextBox, and ImageButton." />

Frames are ideal containers for responsive layouts such as [[external/roblox-creator-docs/ui/list-flex-layouts|list and flex layouts]], allowing you to change the size of the frame and dynamically adjust how layout items fit within it. `Class.Frame|Frames` are also core `Class.GuiObject|GuiObjects`, so you can customize properties such as `Class.GuiObject.BackgroundColor3|BackgroundColor3`, `Class.GuiObject.Transparency|Transparency`, apply a [[external/roblox-creator-docs/ui/appearance-modifiers#gradient|background gradient]] or [[external/roblox-creator-docs/ui/appearance-modifiers#stroke|border]], and more.

Aside from their common use as containers, you can also use `Class.Frame|Frames` for UI design. For example, as a visual separator between other UI elements, you can scale a frame to be thin and long until it becomes a line.

<Alert severity="success">
See also [[external/roblox-creator-docs/ui/scrolling-frames|scrolling frames]], [[external/roblox-creator-docs/ui/viewport-frames|viewport frames]], and [[external/roblox-creator-docs/ui/video-frames|video frames]] as specialty frame types with unique built‑in capabilities.
</Alert>

## Clipping

<Clipping components={props.components} />

## Automatic sizing

Frames can be set to [[external/roblox-creator-docs/ui/size-modifiers#automatic-sizing|automatically size]] depending on their content. To achieve this, set the frame's `Class.Frame.Size|Size` to the **minimum** width and/or height, then set its `Class.Frame.AutomaticSize|AutomaticSize` property to either `Enum.AutomaticSize|X`, `Enum.AutomaticSize|Y`, or `Enum.AutomaticSize|XY` depending on which axes automatic sizing should apply to. Once set, the frame will automatically resize based on the size of `Class.GuiObject|GuiObjects` and layouts within it.


## Related Files

- [[external/roblox-creator-docs/ui/2D-paths]] - 2D paths.
- [[external/roblox-creator-docs/ui/3D-drag-detectors]] - 3D drag detectors.
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
- [[external/roblox-creator-docs/ui/labels]] - Text & image labels.
- [[external/roblox-creator-docs/ui/text-filtering]] - Text filtering.
- [[external/roblox-creator-docs/ui/text-input]] - Text input fields.
- ...and 11 more local docs.
