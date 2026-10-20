---
title: User interface
description: Explore the wide variety of user interface elements that players can interact with.
tags: [roblox, documentation, external-reference, priority-reference, ui, index]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [ui/index.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/ui/index.md). Published page: [https://create.roblox.com/docs/ui](https://create.roblox.com/docs/ui).

You can quickly create high-quality graphical user interfaces with minimal scripting requirements using built-in [UI objects](#ui-objects). Depending on where you create it, UI renders either [on-screen](#on-screen-ui) or [within a game's 3D world](#in-game-ui).

## On-screen UI

[[external/roblox-creator-docs/ui/on-screen-containers|On-screen containers]] hold UI objects that you want to display on a player's screen, including [[external/roblox-creator-docs/ui/frames|frames]], [[external/roblox-creator-docs/ui/labels|labels]], [[external/roblox-creator-docs/ui/buttons|buttons]], and more. All on-screen UI objects and code are stored and changed on the client.

<figure>
<img src="../assets/ui/ui-objects/ScreenGui-Example.jpg" width="840" alt="Example ScreenGui with various GuiObject children, including a Frame, TextLabel, TextBox, and ImageButton." />
</figure>

## In-game UI

[[external/roblox-creator-docs/ui/in-experience-containers|In-game containers]] such as `Class.SurfaceGui|SurfaceGuis` and `Class.BillboardGui|BillboardGuis` hold UI objects that you want to display within your game's 3D world.

<video src="../assets/ui/in-experience/Showcase.mp4" controls width="100%"></video>

## UI objects

Most UI elements are `Class.GuiObject|GuiObjects`, 2D graphical user interface objects that you can parent to containers. The four most common are [[external/roblox-creator-docs/ui/frames|frames]], [[external/roblox-creator-docs/ui/labels|labels]], [[external/roblox-creator-docs/ui/buttons|buttons]], and [[external/roblox-creator-docs/ui/text-input|text input]] objects.

<img src="../assets/ui/ui-objects/ScreenGui-Example.jpg" width="840" />

<table>
<thead>
  <tr>
    <th>Object</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>[[external/roblox-creator-docs/ui/frames|Frame]]</td>
    <td>`Class.Frame|Frames` act as containers for other UI objects. When you manipulate frames, you also manipulate the objects they contain.</td>
  </tr>
	<tr>
    <td>[[external/roblox-creator-docs/ui/labels|Label]]</td>
    <td>`Class.TextLabel` and `Class.ImageLabel` objects allow you to display customizable text and images.</td>
  </tr>
	<tr>
    <td>[[external/roblox-creator-docs/ui/buttons|Button]]</td>
    <td>`Class.TextButton` and `Class.ImageButton` objects allow users to prompt an action.</td>
  </tr>
	<tr>
    <td>[[external/roblox-creator-docs/ui/text-input|Text&nbsp;Input]]</td>
    <td>`Class.TextBox` objects allow users to input text.</td>
  </tr>
</tbody>
</table>

Using the `Class.GuiObject.Position|Position`, `Class.GuiObject.Size|Size`, `Class.GuiObject.AnchorPoint|AnchorPoint`, and `Class.GuiObject.ZIndex|ZIndex` properties, you have complete control on how to [[external/roblox-creator-docs/ui/position-and-size#position|position]], [[external/roblox-creator-docs/ui/position-and-size#size|size]], and [[external/roblox-creator-docs/ui/position-and-size#zindex|layer]] `Class.GuiObject|GuiObjects`. You can also use [[external/roblox-creator-docs/ui/animation|tweening]] to transition a `Class.GuiObject` smoothly from one state to another and provide dynamic visual feedback.

## Layout and design

Beyond basic properties for adjusting position and size, Roblox also provides layout structures like [[external/roblox-creator-docs/ui/list-flex-layouts|list/flex]] and [[external/roblox-creator-docs/ui/grid-table-layouts|grid]], as well as [[external/roblox-creator-docs/ui/size-modifiers|size modifiers]] and [[external/roblox-creator-docs/ui/appearance-modifiers|appearance modifiers]].

<figure>
	<img src="../assets/ui/ui-objects/UIListLayout-Example.png" width="840" />
	<figcaption>`Class.UIListLayout` for horizontal or vertical item sequences</figcaption>
</figure>

<GridContainer numColumns="2">
  <figure>
    <img src="../assets/ui/ui-objects/UIStroke-Color-Solid.png" />
    <figcaption>`Class.UIStroke` on `Class.TextLabel`</figcaption>
  </figure>
  <figure>
    <img src="../assets/ui/ui-objects/UIStroke-Color-Gradient.png" />
    <figcaption>`Class.UIStroke` with `Class.UIGradient`</figcaption>
  </figure>
</GridContainer>

## Universal styling

[[external/roblox-creator-docs/ui/styling/index|Universal styling]] is a Roblox solution to stylesheets, similar to CSS, that lets you declare and globally apply overrides to UI instance properties. This engine‑level support is the foundation for the [[external/roblox-creator-docs/ui/styling/editor|Style&nbsp;Editor]] and the end‑to‑end token pipeline.

## Interactive frameworks

In addition to the core [user interface objects](#ui-objects), the following frameworks provide built‑in and customizable interactivity for your games.

### Proximity prompts

[[external/roblox-creator-docs/ui/proximity-prompts|Proximity prompts]] are unique built-in UI objects which prompt user interaction to trigger an action when they approach in-game objects such as doors, light switches, and buttons.

<video src="../assets/ui/proximity-prompt/Showcase.mp4" controls width="80%" alt="Proximity prompts used in a variety of implementations in the 3D world"></video>

### UI drag detectors

[[external/roblox-creator-docs/ui/ui-drag-detectors|UI drag detectors]] facilitate and encourage interaction with 2D user interface elements such as sliders, spinners, and more.

<video src="../assets/ui/ui-drag-detectors/Showcase.mp4" controls width="80%" alt="How to add UI Drag Detectors and Drag in Edit Mode"></video>

### 3D drag detectors

[[external/roblox-creator-docs/ui/3D-drag-detectors|3D drag detectors]] encourage physical interaction with 3D objects in a game, such as opening doors and drawers, sliding a part around, grabbing and tossing a bowling ball, pulling back and firing a slingshot, and much more.

<video src="../assets/ui/3D-drag-detectors/Showcase.mp4" controls width="80%" alt="Drag detectors used in a variety of implementations in the 3D world"></video>


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
- [[external/roblox-creator-docs/ui/labels]] - Text & image labels.
- [[external/roblox-creator-docs/ui/text-filtering]] - Text filtering.
- ...and 11 more local docs.
