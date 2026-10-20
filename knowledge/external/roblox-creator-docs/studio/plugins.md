---
title: Studio plugins
description: Explains how to create, publish, and monetize extensions to Studio that add custom functionality.
tags: [roblox, documentation, external-reference, priority-reference, studio, debugging]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [studio/plugins.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/studio/plugins.md). Published page: [https://create.roblox.com/docs/studio/plugins](https://create.roblox.com/docs/studio/plugins).

A **plugin** is an extension that adds additional features or functionality to Studio. You can [[external/roblox-creator-docs/production/creator-store#find-assets|install]] community-made plugins from the Creator Store, or you can [create](#create-new-plugins) and [publish](#upload-plugins) your own to the [[external/roblox-creator-docs/projects/assets/toolbox|Toolbox]] to use across your games.

If you choose to also distribute your plugins to the Creator Store, you can either offer them for free or sell them for **United States Dollars**. Roblox offers a market-leading revenue share for these sales, as only taxes and payment processing fees are deducted. For more information on selling plugins, see [[external/roblox-creator-docs/production/creator-store#distribute-and-sell-assets|Creator Store - Distribute and sell assets]].

## Create new plugins

You can create your own plugins to improve your workflow in Studio. The following code sample is a plugin called **AddEmptyScript** that inserts an empty `Class.Script` as the child of an `Class.Instance` or in `Class.ServerScriptService`. The following sections explain the major parts to creating this plugin.

To begin, you should enable **Plugin Debugging Enabled** in the **Studio** section of Studio's settings. This will expose the `Class.PluginDebugService` in Studio which provides real-time debugging for your plugin's code and makes it easier to reload and save your plugin.

```lua title="AddEmptyScript Plugin"
local ServerScriptService = game:GetService("ServerScriptService")
local Selection = game:GetService("Selection")

-- Create a new toolbar section and Plugins menu folder titled "Custom"
local toolbar = plugin:CreateToolbar("Custom")

-- Add a toolbar button labeled "Empty Script"
local newScriptButton = toolbar:CreateButton("Empty Script", "Create an empty script", "rbxassetid://14978048121")

-- Make button clickable even if 3D viewport is hidden
newScriptButton.ClickableWhenViewportHidden = true

local function onPluginButtonClicked()
	local selectedObjects = Selection:Get()
	local parent = selectedObjects[1] or ServerScriptService
	local newScript = Instance.new("Script")
	newScript.Source = ""
	newScript.Parent = parent
end

newScriptButton.Click:Connect(onPluginButtonClicked)
```

### Save plugin script

To create a plugin, first create a `Class.Script` and save it locally.

1. Insert a new `Class.Script` inside `Class.ServerStorage` and rename it to `AddEmptyScript`.

   <img src="../assets/studio/explorer/Plugin-Empty-Script-Adder.png" width="320" />

2. Copy and paste the **AddEmptyScript Plugin** code above into the new script.
3. With the new script selected in the **Explorer** window, select **Save as Local Plugin** from Studio's **Plugins** menu.
4. In the popup window, click **Save** to insert the plugin script into your local **Plugins** folder of the Studio installation.
5. The plugin should appear in `Class.PluginDebugService` and start running.
6. <Chip label="IMPORTANT" size="small" variant="outlined" color="warning" /> Delete the original script in `Class.ServerStorage` and work from the `AddEmptyScript` plugin inside `Class.PluginDebugService`, otherwise you may end up applying changes to the wrong script.

   <img src="../assets/studio/explorer/Plugin-Created.png" width="320" />

<Alert severity="info">
To update a specific plugin within `Class.PluginDebugService`, right‑click it and select **Save&nbsp;and&nbsp;Reload&nbsp;Plugin** from the context menu. If you simply want to reload the plugin, for example to step through a section of code using a breakpoint without saving the plugin, right‑click it and select **Reload&nbsp;Plugin**.

At the broadest level, you can also update **all** plugins by right-clicking `Class.PluginDebugService` and selecting **Save&nbsp;and&nbsp;Reload&nbsp;All&nbsp;Plugins&nbsp;in&nbsp;Debugger** (shortcut <kbd>Ctrl</kbd><kbd>Shift</kbd><kbd>L</kbd> or <kbd>⌘</kbd><kbd>Shift</kbd><kbd>L</kbd>).
</Alert>

### Add toolbar button

To add a button for your plugin to the **Plugins** tab of the Studio toolbar, use the `Class.Plugin:CreateToolbar()` and `Class.PluginToolbar:CreateButton()` methods. In the code for `AddEmptyScript`, line 5 creates a new section in the toolbar and **Plugins** menu folder titled **Custom**, while line 8 creates a button labeled **Empty Script**.

<img src="../assets/studio/general/Toolbar-Custom-Plugin-Button.png" width="800" alt="New plugin button added to toolbar in Studio" />

### Execute code on click

To make the plugin execute code when a user clicks the toolbar button, connect a function to the button's `Class.PluginToolbarButton.Click` event. In the code for `AddEmptyScript`, the connecting function is `onPluginButtonClicked()`.

### Check user selection

To modify a plugin's behavior based on what the user has selected, use the `Class.Selection` service. The `onPluginButtonClicked()` function checks if the user has anything selected and creates the new script as its child instead of inside `Class.ServerScriptService`. If the user doesn't have anything selected, it creates the new script in `Class.ServerScriptService`.

<img src="../assets/studio/explorer/Plugin-Inserted-Script.png" width="320" />

### Support undo and redo

Use `Class.ChangeHistoryService` to allow users to undo and redo changes made by a plugin within a game. In your script, set the plugin to call `Class.ChangeHistoryService:TryBeginRecording()|TryBeginRecording()` and store the identifier assigned to the API call before making changes. Then set the plugin to call `Class.ChangeHistoryService:FinishRecording()|FinishRecording()` after making changes, so it captures any changes made during the recording session for undo and redo.

The following code sample creates an example plugin that can apply the neon material to selected parts. It uses `Class.ChangeHistoryService` to record and manage the changes made by the plugin:

```lua title="Example Material Plugin with Recordings for Undo and Redo"
local ChangeHistoryService = game:GetService("ChangeHistoryService")
local Selection = game:GetService("Selection")

-- Create an example plugin
local toolbar = plugin:CreateToolbar("Example Plugin")
local button = toolbar:CreateButton("Neon it up", "", "")

-- Connect a function to the click event
button.Click:Connect(function()
	-- Try to begin a recording with a specific identifier
	local recording = ChangeHistoryService:TryBeginRecording("Set selection to neon")

	-- Check if recording was successfully initiated
	if not recording then
		-- This indicates that your plugin began a previous recording and never completed it
		-- You may only have one recording per plugin active at a time
		return
	end

	-- Iterate through the selected instances
	for _, instance in Selection:Get() do
		-- Check if the instance is a BasePart
		if instance:IsA("BasePart") then
			instance.Material = Enum.Material.Neon -- Set the material of the part to Neon
		end
	end

	-- Finish the recording, committing the changes to the history
	ChangeHistoryService:FinishRecording(recording, Enum.FinishRecordingOperation.Commit)
end)
```

<Alert severity="warning">
Note the following caveats with `Class.ChangeHistoryService` recordings:
* If you're using the [[external/roblox-creator-docs/studio/ui-overview#command-bar|Multi-line Command Bar]], don't run any code in the command bar that will always be running while you have a place open, since the command bar uses `Class.ChangeHistoryService` recordings to allow for undo/redo with commands that make changes to the `Class.DataModel`.
* Reloading a plugin won't cancel its ongoing `Class.ChangeHistoryService` recordings, so make use of [[external/roblox-creator-docs/scripting/attributes#create-attributes|attributes]] to store the last recording identifier so it can be canceled by the plugin when it reloads.
</Alert>

## Upload plugins

After you finish creating a plugin, you can upload it to your inventory so that it is accessible across all of your projects.

To upload a plugin:

1. In the **Explorer** window, select a plugin script.
1. Navigate to Studio's **Plugins** menu, then select **Publish as Plugin**.
1. <Chip label="OPTIONAL" size="small" variant="outlined" /> In the upper-left corner of the asset configuration window, click the default puzzle piece image to upload a 512&times;512 image thumbnail for your plugin.
1. Fill in the following fields:

   - **Name** — A title for your plugin.
   - **Description** — A description that describes what a potential user can expect the plugin to do.
   - **Creator** — The creator or group that you want to attribute as the creator of the plugin.

1. Click the **Submit** button. Your plugin is now available to you in the [[external/roblox-creator-docs/projects/assets/toolbox|Toolbox]] under the **Inventory** and **Creations** tabs.

## Distribute and sell plugins

You can publicly distribute and sell your own plugins on the Creator Store for others to use within their own game development. This monetization method lets you earn 100% of net proceeds on transactions, bypassing platform fees and DevEx rates. For more information on this process, including how to set up a seller account to set prices and receive payouts, see [[external/roblox-creator-docs/production/creator-store#distribute-and-sell-assets|Creator Store - Distribute and sell assets]].


## Related Files

- [[external/roblox-creator-docs/studio/align-tool]] - Align tool.
- [[external/roblox-creator-docs/studio/avatar-settings]] - Avatar Settings.
- [[external/roblox-creator-docs/studio/mcp]] - Connect to the Roblox Studio MCP server.
- [[external/roblox-creator-docs/studio/controller-emulator]] - Controller Emulator.
- [[external/roblox-creator-docs/studio/debugging]] - Debugging.
- [[external/roblox-creator-docs/studio/developer-console]] - Developer Console.
- [[external/roblox-creator-docs/studio/device-simulator]] - Device Simulator.
- [[external/roblox-creator-docs/studio/explorer]] - Explorer window.
- [[external/roblox-creator-docs/studio/importer]] - Importer.
- [[external/roblox-creator-docs/studio/material-generator]] - Material Generator.
- [[external/roblox-creator-docs/studio/network-simulator]] - Network Simulator.
- [[external/roblox-creator-docs/studio/output]] - Output.
- [[external/roblox-creator-docs/studio/pivot-tools]] - Pivot tools.
- [[external/roblox-creator-docs/studio/properties]] - Properties window.
- [[external/roblox-creator-docs/studio/rig-builder]] - Rig Generator.
- [[external/roblox-creator-docs/studio/index]] - Roblox Studio.
- ...and 8 more local docs.
