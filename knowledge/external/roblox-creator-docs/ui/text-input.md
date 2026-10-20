---
title: Text input fields
description: Text input fields allow users to input text from their physical or on-screen keyboard.
tags: [roblox, documentation, external-reference, priority-reference, ui]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [ui/text-input.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/ui/text-input.md). Published page: [https://create.roblox.com/docs/ui/text-input](https://create.roblox.com/docs/ui/text-input).

import TextFiltering from '../includes/text-filtering/text-filtering.md'

A `Class.TextBox` is a rectangle that allows a user to provide text input while it's in focus. When you [script](#script-text-inputs) a `Class.TextBox`, you can use it as a search bar or an input field on a form. To help users know what type of text they should input, you can also provide a prompt through the `Class.TextBox.PlaceholderText|PlaceholderText` property.

<img src="../assets/ui/ui-objects/TextBox-Example.jpg" width="840" />

Because these objects are `Class.GuiObject|GuiObjects`, you can customize
properties such as `Class.GuiObject.BackgroundColor3|BackgroundColor3`,
`Class.GuiObject.BorderMode|BorderMode`,
`Class.GuiObject.Transparency|Transparency`, and
`Class.GuiObject.Rotation|Rotation` to fit the aesthetics of your game.

## Create text inputs on the screen

A `Class.TextBox` on a screen is useful for
things like an input field for a form.

To add a `Class.TextBox` to a screen:

1. In the **Explorer** window, select **StarterGui** and add a **ScreenGui**.

   1. Hover over StarterGui and click the &CirclePlus; button. A contextual menu displays.

   1. Insert a **ScreenGui**.

2. Select the new **ScreenGui** and add a **TextBox**.

   1. Hover over **ScreenGui** and click the &CirclePlus; button. A contextual menu displays.

   1. Insert a **TextBox**.

## Create text inputs on part faces

To add a `Class.TextBox` to the face of a part:

1. In the **Explorer** window, select **StarterGui** and add a **SurfaceGui**.

   1. Hover over StarterGui and click the &CirclePlus; button. A contextual menu displays.

   1. Insert a **ScreenGui**.

2. Select the new **SurfaceGui** and add a **TextBox**.

   1. Hover over **SurfaceGui** and click the &CirclePlus; button. A contextual menu displays.

   1. Insert a **TextBox**.

3. Adorn the **SurfaceGui** to the **part** on which you want to display the **TextBox**.

   1. In the **Properties** window, select the **Adornee** property. Your cursor changes.

   1. In the **Explorer** window, select the part.

<Alert severity="warning">
  If you don't see the `Class.TextBox`, try [[external/roblox-creator-docs/parts/textures-decals#choose-a-face|choosing a different face]] in the <b>Face</b> property of the <b>SurfaceGui</b>.
</Alert>

## Script text inputs

Like [[external/roblox-creator-docs/ui/buttons|buttons]], you can script any action for a `Class.TextBox` object when a user interacts with it. For example, the following script connects the `Class.TextBox.FocusLost|FocusLost` event which fires when the user presses the <kbd>Enter</kbd> button or clicks outside the box. If `enterPressed` is `true`, meaning the user submitted the input instead of merely clicking outside the box, the script prints the contents of the entry to the [[external/roblox-creator-docs/studio/output|Output]] window.

```lua title="Basic Text Input Handling"
local textBox = script.Parent

local function onFocusLost(enterPressed, inputObject)
	if enterPressed then
		print(textBox.Text)
	end
end

textBox.FocusLost:Connect(onFocusLost)
```

As another example, you might want to allow only numbers in a `Class.TextBox`. The following code uses the `Class.TextBox.GetPropertyChangedSignal` event to detect when the `Class.TextBox.Text` changes, such as when a user starts typing, then it uses the `Library.string.gsub()` function to disallow non‑numbers.

```lua title="Restricting Text Input to Numbers"
local textBox = script.Parent

local function allowOnlyNumbers()
	textBox.Text = string.gsub(textBox.Text, "%D", "")
end

textBox:GetPropertyChangedSignal("Text"):Connect(allowOnlyNumbers)
```

## Text filtering

<TextFiltering components={props.components} context="characters/strings that users input through text inputs" />


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
