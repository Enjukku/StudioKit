---
title: Mouse and keyboard input
description: Explains Roblox support for computer mice and keyboards.
tags: [roblox, documentation, external-reference, priority-reference, input]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [input/mouse-and-keyboard.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/input/mouse-and-keyboard.md). Published page: [https://create.roblox.com/docs/input/mouse-and-keyboard](https://create.roblox.com/docs/input/mouse-and-keyboard).

A large percentage of Roblox sessions are played on devices with a mouse and keyboard, so it's important to support these inputs when designing a game for a wide audience.

To simplify [[external/roblox-creator-docs/projects/cross-platform|cross‑platform]] inputs, including mouse/keyboard, Roblox provides the [[external/roblox-creator-docs/input/input-action-system|Input Action System]] to define **actions** such as "jump," "sprint," or "shoot" and set up **bindings** for multiple hardware inputs to drive those actions.

Roblox also supports general mouse/keyboard input through `Class.UserInputService` events like `Class.UserInputService.InputBegan|InputBegan` and `Class.UserInputService.InputEnded|InputEnded` and methods like `Class.UserInputService:IsKeyDown()|IsKeyDown()` to check if a particular key is pressed on a keyboard.

## Input type detection

In cross‑platform development, it's important that you determine and respond to the `Class.UserInputService.PreferredInput|PreferredInput` type a player is using, normally to ensure that [[external/roblox-creator-docs/ui/index#ui-objects|UI&nbsp;elements]] like on-screen buttons and menus work elegantly and support interaction across devices.

For example, a PC or laptop assumes mouse/keyboard is the default input, but a player may choose to connect a bluetooth gamepad. In this case, mouse/keyboard remains a valid input, but you can assume the player wants to switch to the connected gamepad as the **primary** input type.

See [[external/roblox-creator-docs/input/index#input-type-detection|input type detection]] for more information.

## Generic mouse/key input

Beyond the [[external/roblox-creator-docs/input/input-action-system|Input Action System]], you can capture mouse and keyboard inputs using `Class.UserInputService`. The following `Class.LocalScript`, when placed in `Class.StarterPlayerScripts`, captures the began and ended phases of key and mouse clicks and prints the result to the [[external/roblox-creator-docs/studio/output|Output]] window.

```lua title="LocalScript - Output Key/Mouse Began and Ended"
local UserInputService = game:GetService("UserInputService")

local function onInputBegan(inputObject, processedEvent)
	-- Return if another script has already processed the input
	if processedEvent then return end
	
	print(inputObject.KeyCode.Name, "began!", inputObject.Position)
end

local function onInputEnded(inputObject, processedEvent)
	-- Return if another script has already processed the input
	if processedEvent then return end
	
	print(inputObject.KeyCode.Name, "ended!", inputObject.Position)
end

UserInputService.InputBegan:Connect(onInputBegan)
UserInputService.InputEnded:Connect(onInputEnded)
```

## Mouse icon

You can customize the appearance and behavior of a player's mouse icon within your game to create a cohesive style across all of your UI elements. This includes temporarily changing the player's mouse icon in specific circumstances, such as hovering over a button.

<Tabs>
<TabItem label="Change Icon">
You can change the player's mouse icon in a `Class.LocalScript` by setting the `Class.UserInputService.MouseIcon|MouseIcon` property in `Class.UserInputService` to a custom Roblox asset ID. For example, the following `Class.LocalScript` changes the player's default mouse icon to a circle with a blue dot in the middle.

```lua highlight="3"
local UserInputService = game:GetService("UserInputService")

UserInputService.MouseIcon = "rbxassetid://3400146391"
```

</TabItem>
<TabItem label="Hide Icon">
You can hide the player's mouse icon by setting the `Class.UserInputService.MouseIconEnabled` to `false` in a `Class.LocalScript`. For example, the following code switches the mouse icon from visible to invisible and back every two seconds.

```lua highlight="5,7"
local UserInputService = game:GetService("UserInputService")

while true do
	task.wait(2)
	UserInputService.MouseIconEnabled = false
	task.wait(2)
	UserInputService.MouseIconEnabled = true
end
```

</TabItem>
<TabItem label="Lock Icon">
You can lock the mouse icon's position to the screen using `Class.UserInputService.MouseBehavior` with a `Enum.MouseBehavior` value of `Enum.MouseBehavior|LockCurrentPosition` or `Enum.MouseBehavior|LockCenter`, then unlock it again with a value of `Enum.MouseBehavior|Default`.

If a player's mouse icon is locked in a position, `Class.UserInputService.InputChanged` still fires when the player moves the mouse, passing in the distance the mouse has moved. For example, the following code sample locks the player's mouse icon after one second, then Studio prints the mouse delta whenever the player moves their mouse.

```lua highlight="5"
local UserInputService = game:GetService("UserInputService")

task.wait(5)

UserInputService.MouseBehavior = Enum.MouseBehavior.LockCurrentPosition

UserInputService.InputChanged:Connect(function(inputObject)
	if inputObject.UserInputType == Enum.UserInputType.MouseMovement then
		print("Mouse delta is (" .. tostring(inputObject.Delta.X) .. ", " ..  tostring(inputObject.Delta.Y) .. ")")
	end
end)
```

</TabItem>
</Tabs>


## Related Files

- [[external/roblox-creator-docs/input/gamepad]] - Gamepad input.
- [[external/roblox-creator-docs/input/index]] - Input.
- [[external/roblox-creator-docs/input/input-action-system]] - Input Action System.
- [[external/roblox-creator-docs/input/micro-gamepad]] - Micro gamepad input.
- [[external/roblox-creator-docs/input/mobile]] - Mobile input.
