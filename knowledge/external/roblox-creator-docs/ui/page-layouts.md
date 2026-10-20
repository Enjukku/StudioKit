---
title: Page layouts
description: Explore how page layouts organize interface content into distinct pages.
tags: [roblox, documentation, external-reference, priority-reference, ui]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [ui/page-layouts.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/ui/page-layouts.md). Published page: [https://create.roblox.com/docs/ui/page-layouts](https://create.roblox.com/docs/ui/page-layouts).

When you parent a `Class.UIPageLayout` to a UI container, every sibling `Class.GuiObject` becomes a unique page that you can transition to through scripting. This layout is useful when you want to create user interfaces such as tabbed modals, tutorials, or character customization screens.

<img src="../assets/studio/explorer/UIPageLayout.png" width="320" />

After you create multiple pages within the `Class.UIPageLayout`, you need to use scripting to transition from page to page. For example, the following code, pasted into a client‑side sibling `Class.Script` of the layout, transitions forward and then backward between the pages every two seconds.

```lua
local frame = script.Parent

local pageLayout = frame:FindFirstChildWhichIsA("UIPageLayout")

task.wait(2)
pageLayout:Next()

task.wait(2)
pageLayout:Next()

task.wait(2)
pageLayout:Previous()

task.wait(2)
pageLayout:Previous()
```

If you want to view pages while editing in Studio, you can use the [[external/roblox-creator-docs/studio/ui-overview#command-bar|Command Bar]] to navigate from one page to another, letting you review where you need to make changes without having to play your game each time.

1. In the [[external/roblox-creator-docs/studio/explorer|Explorer]] window hierarchy, select the `Class.UIPageLayout` object.

   <img src="../assets/studio/explorer/UIPageLayout.png" width="320" />

2. Open the [[external/roblox-creator-docs/studio/ui-overview#command-bar|Command Bar]].
3. Input any of the following commands and press <kbd>Enter</kbd>.

   <table>
	<thead>
     <tr>
       <td>Action</td>
       <td>Command</td>
     </tr>
   </thead>
   <tbody>
     <tr>
       <td>**Next Page**</td>
       <td>`game:GetService("Selection"):Get()[1]:Next()`</td>
     </tr>
     <tr>
       <td>**Previous Page**</td>
       <td>`game:GetService("Selection"):Get()[1]:Previous()`</td>
     </tr>
     <tr>
       <td>**First Page**</td>
       <td>`game:GetService("Selection"):Get()[1]:JumpToIndex(0)`</td>
     </tr>
   </tbody>
   </table>


## Related Files

- [[external/roblox-creator-docs/ui/2D-paths]] - 2D paths.
- [[external/roblox-creator-docs/ui/3D-drag-detectors]] - 3D drag detectors.
- [[external/roblox-creator-docs/ui/frames]] - Frames.
- [[external/roblox-creator-docs/ui/grid-table-layouts]] - Grid and table layouts.
- [[external/roblox-creator-docs/ui/in-experience-containers]] - In-game UI containers.
- [[external/roblox-creator-docs/ui/list-flex-layouts]] - List and flex layouts.
- [[external/roblox-creator-docs/ui/on-screen-containers]] - On-screen UI containers.
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
