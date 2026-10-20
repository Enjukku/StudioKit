---
title: Abilities
description: Abilities in the Character Controller Library (CCL) evaluate what a character can do, as well as enable flexible behavior composition such as a character being able to move while also aiming and crouching.
tags: [roblox, documentation, external-reference, priority-reference, characters]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [characters/character-controller-library/abilities.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/characters/character-controller-library/abilities.md). Published page: [https://create.roblox.com/docs/characters/character-controller-library/abilities](https://create.roblox.com/docs/characters/character-controller-library/abilities).

> [!warning] Not in the current upstream docs
> Not published in [github.com/Roblox/creator-docs](https://github.com/Roblox/creator-docs) as of 2026-10-20 (revision `74006430`). The closest current page is [[external/roblox-creator-docs/characters/character-controller-library/custom-abilities]]. Kept locally so existing links keep working; read that page for current information.

**Abilities** in the [[external/roblox-creator-docs/characters/character-controller-library/index|Character Controller Library]] (CCL) evaluate what a character can do, such as the ability to run, jump, climb, and swim. Instead of relying on rigid engine‑defined character states like those in `Enum.HumanoidStateType`, the CCL enables flexible behavior composition such as a character being able to move while also aiming and crouching.

<Alert severity="info">
At this time, custom abilities are not supported, although the CCL fully supports the traditional character abilities (run, climb, jump, swim, etc.) and you can customize their behaviors more easily. In the future, custom abilities will allow you to add new character mechanics such as crouching, aiming, wall‑jumping, and more.
</Alert>

## Enable CCL

The CCL is **opt-in** through Studio's [[external/roblox-creator-docs/studio/avatar-settings|Avatar Settings]] window. To enable it:

1. From the **Avatar** tab, open [[external/roblox-creator-docs/studio/avatar-settings|Avatar Settings]].

   <img src="../../assets/studio/general/Toolbar-Avatar-Settings.png" width="800" alt="Avatar Settings indicated in Studio's toolbar" />

2. Select the **Movement** tab on the left side of the window and, in the **Abilities** section, select **Character&nbsp;Controller&nbsp;Library**.

   <img src="../../assets/studio/general/Avatar-Settings-CCL.png" width="600" alt="Character Controller Library toggle in the Avatar Settings window" />

3. All of the standard abilities like **Running**, **Jumping**, and **Climbing** are enabled by default. To disable any of them at runtime, uncheck the associated box.

   <Alert severity="warning">
	 It's not recommended to disable **Running**, as doing so will prevent characters from moving along the ground. Additionally, you should always keep **Getting&nbsp;Up** enabled if **Falling&nbsp;Down** is enabled, as a mismatch will allow characters to fall down (trip) but never get back up.
	 </Alert>

## Configuration

While your experience is running (or through a script that runs from `Class.ServerScriptService`), you can experiment with the built‑in ability configurations. You can also modify specific [[external/roblox-creator-docs/characters/character-controller-library/controllers|controllers]] to adjust the physical simulation of the character and its interaction with the environment, such as the character's base movement speed.

### Runtime

To experiment with ability configurations at runtime:

1. Begin a playtest.
2. In the [[external/roblox-creator-docs/studio/explorer|Explorer]], locate the character model in the `Class.Workspace` and then expand the `Abilities` tree under `AbilityManagerActor`:

   <img src="../../assets/studio/explorer/Character-Model-Abilities.png" width="320" />

3. Select one of the built-in abilities and, within its **Attributes** section of the [[external/roblox-creator-docs/studio/properties|Properties]] window, customize [[external/roblox-creator-docs/studio/properties#instance-attributes|attributes]] such as those noted below.

   <table>
   <thead>
     <tr>
       <th>Ability</th>
       <th>Attributes</th>
     </tr>
   </thead>
   <tbody>
     <tr>
       <td>`Climbing`</td>
       <td>
			 - `Enabled` &nbsp;⇔&nbsp; `Class.Humanoid:SetStateEnabled()|Humanoid:SetStateEnabled(Enum.HumanoidStateType.Climbing)`
			 - `SpeedMultiplier` — Multiplier to the `Class.ClimbController.MoveSpeedFactor` property when character is climbing.
       </td>
     </tr>
     <tr>
       <td>`Dead`</td>
       <td>
			 - `Enabled` — Character dies when health is `0` or less.
			 - `Health` &nbsp;⇔&nbsp; `Class.Humanoid.Health`
			 - `MaxHealth` &nbsp;⇔&nbsp; `Class.Humanoid.MaxHealth`
			 - `RequiresNeck` &nbsp;⇔&nbsp; `Class.Humanoid.RequiresNeck`
       </td>
     </tr>
     <tr>
       <td>`FacingMoveDirection`</td>
       <td>
			 - `Enabled` &nbsp;⇔&nbsp; `Class.Humanoid.AutoRotate`
       </td>
     </tr>
     <tr>
       <td>`FallingDown`</td>
       <td>
			 - `Enabled` &nbsp;⇔&nbsp; `Class.Humanoid:SetStateEnabled()|Humanoid:SetStateEnabled(Enum.HumanoidStateType.FallingDown)`
       </td>
     </tr>
     <tr>
       <td>`Freefall`</td>
       <td>
			 - `Enabled` &nbsp;⇔&nbsp; `Class.Humanoid:SetStateEnabled()|Humanoid:SetStateEnabled(Enum.HumanoidStateType.Freefall)`
			 - `SpeedMultiplier` — Multiplier to the `Class.AirController.MoveSpeedFactor` property when character is free‑falling. Note that the effect may be subtle when the character free‑falls for a very short duration.
       </td>
     </tr>
     <tr>
       <td>`GettingUp`</td>
       <td>
			 - `Enabled` &nbsp;⇔&nbsp; `Class.Humanoid:SetStateEnabled()|Humanoid:SetStateEnabled(Enum.HumanoidStateType.GettingUp)`
       </td>
     </tr>
     <tr>
       <td>`Jumping`</td>
       <td>
			 - `Enabled` &nbsp;⇔&nbsp; `Class.Humanoid:SetStateEnabled()|Humanoid:SetStateEnabled(Enum.HumanoidStateType.Jumping)`
			 - `JumpHeight` &nbsp;⇔&nbsp; `Class.Humanoid.JumpHeight`
			 - `JumpPower` &nbsp;⇔&nbsp; `Class.Humanoid.JumpPower`
			 - `UseJumpPower` &nbsp;⇔&nbsp; `Class.Humanoid.UseJumpPower`
       </td>
     </tr>
     <tr>
       <td>`NoLocomotion`</td>
       <td>
			 - `Enabled` &nbsp;⇔&nbsp; `Class.Humanoid:SetStateEnabled()|Humanoid:SetStateEnabled(Enum.HumanoidStateType.PlatformStanding)`
       </td>
     </tr>
      <tr>
       <td>`Running`</td>
       <td>
			 - `Enabled` &nbsp;⇔&nbsp; `Class.Humanoid:SetStateEnabled()|Humanoid:SetStateEnabled(Enum.HumanoidStateType.Running)`
			 - `SpeedMultiplier` — Multiplier to the `Class.GroundController.MoveSpeedFactor` property when character is running.
       </td>
     </tr>
     <tr>
       <td>`Sitting`</td>
       <td>
			 - `Enabled` &nbsp;⇔&nbsp; `Class.Humanoid:SetStateEnabled()|Humanoid:SetStateEnabled(Enum.HumanoidStateType.Seated)`
       </td>
     </tr>
      <tr>
       <td>`Swimming`</td>
       <td>
			 - `Enabled` &nbsp;⇔&nbsp; `Class.Humanoid:SetStateEnabled()|Humanoid:SetStateEnabled(Enum.HumanoidStateType.Swimming)`
			 - `EnableFastRise` — Rise to surface more quickly by holding the jump input.
			 - `SpeedMultiplier` — Multiplier to the `Class.SwimController.MoveSpeedFactor` property when character is swimming.
       </td>
     </tr>
   </tbody>
   </table>

### Scripted

To set ability configurations for all characters through a script:

1. Create a new server-side `Class.Script` within `Class.ServerScriptService` and rename it to `AbilitiesScript`.
2. Copy and paste the following code into the new script. This example multiplies the base movement speed for the `Running` ability by `2`. Feel free to adjust other ability attributes such as those described in the [table above](#configuration).

		```lua title="Script in ServerScriptService"
		local Players = game:GetService("Players")

		local function onCharacterAdded(character)
			local AbilityManagerActor = character:WaitForChild("AbilityManagerActor")
			local Abilities = AbilityManagerActor:WaitForChild("Abilities")

			local Running = Abilities:FindFirstChild("Running")
			if Running then
				-- Double base move speed
				Running:SetAttribute("SpeedMultiplier", 2)
			end	
		end

		local function onPlayerAdded(player)
			if player.Character then
				onCharacterAdded(player.Character)
			end
			player.CharacterAdded:Connect(onCharacterAdded)
		end

		Players.PlayerAdded:Connect(onPlayerAdded)
		```


## Related Files

- [[external/roblox-creator-docs/characters/character-controller-library/index]] - Character Controller Library.
- [[external/roblox-creator-docs/characters/index]] - Characters.
- [[external/roblox-creator-docs/characters/character-controller-library/controllers]] - Controllers.
- [[external/roblox-creator-docs/studio/explorer]] - Explorer window.
- [[external/roblox-creator-docs/studio/properties]] - Properties window.
