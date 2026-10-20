---
title: Calisthenics Tool
description: Calisthenics Tool is a Blender plugin that you can use to verify skinning quality of an asset.
tags: [roblox, documentation, external-reference, priority-reference, art, assets]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [art/modeling/calisthenics-tool.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/art/modeling/calisthenics-tool.md). Published page: [https://create.roblox.com/docs/art/modeling/calisthenics-tool](https://create.roblox.com/docs/art/modeling/calisthenics-tool).

<Alert severity = 'warning'>
This tool is no longer in active development. You are free to use the tool for any purpose. The tool may be out of date or incompatible with modern Roblox assets.
</Alert>

The **Calisthenics Tool** is a supplemental [Blender](https://www.blender.org/) add-on that allows you to quickly test your asset through a set of animation cycles to verify your skinning data. At any point during the animation testing, you can pause and use Blender's skinning Tools, such as [Weight Painting brushes](https://docs.blender.org/manual/en/latest/sculpt_paint/weight_paint/introduction.html), to resolve any skinning imperfections.

Skinning your layered accessories and character bodies is a critical and often time-intensive process to create high quality assets that move and fit with different character bodies. Similar to the [[external/roblox-creator-docs/art/accessories/validation-tool|Layered Accessory Validation Tool]], the Calisthenics Tool can save you time when testing your character models after rigging and skinning.

<Alert severity = 'info'>
The Calisthenics Tool doesn't provide complete verification of all potential skinning issues. You must also ensure that your custom models meet Studio's [[external/roblox-creator-docs/avatar/character-bodies/specifications|character body specifications]] and any applicable [[external/roblox-creator-docs/avatar/layered-accessories/specifications|layered accessory specifications]] for the best results in your game.
</Alert>

<GridContainer numColumns="3">
	<figure>
		<video controls loop muted src="../../assets/modeling/skinned-meshes/calisthenic-tool/Walking-Reference.mp4" width="90%"></video>
		<figcaption>Walking Animation</figcaption>
	</figure>
   <figure>
		<video controls loop muted src="../../assets/modeling/skinned-meshes/calisthenic-tool/Running-Reference.mp4" width="90%"></video>
		<figcaption>Running Animation</figcaption>
	</figure>
  	<figure>
		<video controls loop muted src="../../assets/modeling/skinned-meshes/calisthenic-tool/Movement-Reference.mp4" width="90%"></video>
		<figcaption>Generic Movements</figcaption>
	</figure>
</GridContainer>

## Installation

<Alert severity = 'info'>
The Calisthenics Tool plugin is designed for [Blender 3.0+](https://www.blender.org/download/). You can download and modify the tool for any use.
</Alert>

To install the Calisthenics Tool in Blender:

1. Download the [CalisthenicsTool.zip](https://github.com/Roblox/avatar/tree/main/Tools/CalisthenicsTool) and save the `.zip` file locally.
2. In Blender, navigate to **Edit** > **Preferences**.
   <img src="../../assets/modeling/skinned-meshes/calisthenic-tool/Blender-Preferences.png" width="70%" />

3. In the left sidebar of the **Preferences** window, navigate to the **Add-Ons** section.
4. Click the **Install…** button. A file browser displays.
5. Select the `.zip` and click **Install Add-On**.
6. Using the search bar, search for "Calisthenics Tool" and select the add-on.
7. Enable the add-on by checking the box next to the add-on name.

   <img src="../../assets/modeling/skinned-meshes/calisthenic-tool/Calisthenics-Tool-Addon.png" width="70%" />

8. Close the Preferences window. You can now access the Calisthenics Tool by expanding the tool sidebar in the Viewport.

<GridContainer numColumns ="2">
  <figure>
    <img src="../../assets/modeling/skinned-meshes/calisthenic-tool/Toolbar-Slider.png" width="97%" />
    <figcaption>Use the arrow on the side of the Viewport to open the sidebar.</figcaption>
  </figure>
  <figure>
    <img src="../../assets/modeling/skinned-meshes/calisthenic-tool/Calisthenics-Tool-Open.png" width="100%" />
    <figcaption>Access the Calisthenics Tool by selecting the tab in the sidebar tool menu.</figcaption>
  </figure>
</GridContainer>

## Use the Calisthenics Tool

After installation, you can use the Calisthenics Tool whenever you want to test a [[external/roblox-creator-docs/avatar/character-bodies/specifications#standard-r15-rigs|standard R15]] rigging armature with skinning data. With the Calisthenics Tool, you can check how a character body would move with generic animations, as well as attach reference rigid accessories to verify attachment during these movements. The tool also includes an option to automatically export your character, removing reference animation and accessory data.

You can try out the Calisthenics Tool using an [example character body model](../../assets/modeling/skinned-meshes/calisthenic-tool/Fish-Character-No-FACS.fbx).

<Alert severity = 'info'>
For demonstration purposes, this reference model doesn't contain FACS data. If you require a reference with facial animation, you can download the same model with FACS data from our [[external/roblox-creator-docs/avatar/character-bodies/specifications#reference-files|reference models]].
</Alert>

### Test animations

When testing your character body model, first set the armature in the Calisthenics Tool then select one of the reference animations. It is important to visually verify your skinning quality using various movements and angles to ensure the best results for your model.

<Alert severity ='warning'>
If you encounter any errors or warnings when setting armature or playing animations, verify that your model uses an appropriate bone hierarchy and naming convention outlined in Roblox's [[external/roblox-creator-docs/avatar/character-bodies/specifications|custom mesh requirements]].
</Alert>

To test animations:

1. Open a Blender project with an existing character body with a [[external/roblox-creator-docs/avatar/character-bodies/specifications#standard-r15-rigs|standard R15 rig]], or import an appropriate character model `.fbx` using **File** > **Import** > **FBX (.fbx)**.

2. For easier visualization, hide non-rendered mesh objects, such as armature, cages, and attachments to better preview the reference animations.

   <video controls src="../../assets/modeling/skinned-meshes/calisthenic-tool/1_Hide-Armature.mp4" width="80%"></video>

3. Set which rig you want to test a reference animation on:
   1. In the add-on's **Armature** field, select the Eyedropper.
   2. In the Outliner, select the **Armature** object that contains your character's rig data.
4. Click on an animation cycle to preview, such as **Walk**, **Run**, **Move** or **Idle**.
5. Press **Stop Animation** to clear animation data.
   <video controls src="../../assets/modeling/skinned-meshes/calisthenic-tool/2_Set-Armature-Test.mp4" width="80%"></video>

6. If you notice any unexpected skinning deformations, pause on the frame and switch to **Weight Paint mode** or use Blender's other skinning tools to resolve. See [[external/roblox-creator-docs/art/modeling/skin-a-humanoid-model|Skin a humanoid model]] for additional instruction.
   <video controls src="../../assets/modeling/skinned-meshes/calisthenic-tool/3_Fix-Skinning-Example.mp4" width="80%"></video>

### Test accessory attachments

You can add reference attachments to your character body model using the **Attach Test Accessory** buttons. These test accessories help preview how rigid accessories attach to your character and how they can move with your model. The tool includes two sets of rigid accessories to apply to your character.

<GridContainer numColumns ="2">
  <figure>
    <img src="../../assets/modeling/skinned-meshes/calisthenic-tool/Normal-Reference.png" width="85%" />
    <figcaption>**Normal Size** - Loads normal accessory references.</figcaption>
  </figure>
  <figure>
    <img src="../../assets/modeling/skinned-meshes/calisthenic-tool/Slender-Reference.png" width="85%" />
    <figcaption>**Slender Size** - Loads slender accessory references.</figcaption>
  </figure>
</GridContainer>

To test accessories:

1. Use the following **Attach Test Accessory** buttons to add or remove sample accessories to your character's attachment points:
   - **Normal Size** - Adds normal scale test accessories.
   - **Slender Size** - Adds slender scale test accessories.
   - **Detach Test Accessories** - Removes any test accessories from your character.
2. If an accessory is not attaching at an expected location, reposition the associated **Attachment object** in your character's rigging armature.

### Export models

When you are ready to export your model, you can export your character body directly through the Calisthenics Tool. The tool automatically clears any of the test data and applies appropriate export settings.

<Alert severity = 'info'>
Using this tool to export models with [[external/roblox-creator-docs/avatar/dynamic-heads/index|facial animations]] may result in unexpected behavior because the stored FACS data can conflict with the tool's reference animations.
</Alert>

To export from the Calisthenics Tool:

1. In the **Export Path** field, set the export directory by clicking the folder icon and browsing to the appropriate file directory.
   <img src="../../assets/modeling/skinned-meshes/calisthenic-tool/Exporting-Model.png" width="60%" />

2. Click the **Export Model** button. The character model `.fbx` populates in the designated folder as `Character_Model_Export.fbx`.

<Alert severity = 'warning'>
If you are manually exporting your model with Blender's `.fbx` importer instead of the Calisthenics Tool, ensure the following before export:
- Detach the Calisthenics Tool's test accessories.
- Use the **Stop Animation** button to clear test animations from the timeline.
- Return the model to the default pose with no additional pose data.
- Verify your settings follow Roblox's [[external/roblox-creator-docs/art/modeling/export-requirements|Blender export settings]].
</Alert>


## Related Files

- [[external/roblox-creator-docs/art/modeling/gltf-export]] - 3D Export.
- [[external/roblox-creator-docs/art/modeling/assign-textures]] - Blender and Maya texture settings.
- [[external/roblox-creator-docs/art/modeling/index]] - Custom 3D assets.
- [[external/roblox-creator-docs/art/modeling/export-requirements]] - Export settings.
- [[external/roblox-creator-docs/art/modeling/specifications]] - General specifications.
- [[external/roblox-creator-docs/art/modeling/material-reference]] - Material references.
- [[external/roblox-creator-docs/art/modeling/project-files]] - Modeling project files and references.
- [[external/roblox-creator-docs/art/modeling/surface-appearance]] - PBR textures.
- [[external/roblox-creator-docs/art/modeling/reimport]] - Reimport.
- [[external/roblox-creator-docs/art/modeling/rig-a-humanoid-model]] - Rig a humanoid model.
- [[external/roblox-creator-docs/art/modeling/rig-a-simple-mesh]] - Rig a simple mesh.
- [[external/roblox-creator-docs/art/modeling/rigging]] - Rigging and skinning.
- [[external/roblox-creator-docs/art/modeling/roblox-blender-plugin]] - Roblox Blender plugin.
- [[external/roblox-creator-docs/art/modeling/skin-a-humanoid-model]] - Skin a humanoid model.
- [[external/roblox-creator-docs/art/modeling/skin-a-simple-mesh]] - Skin a simple mesh.
- [[external/roblox-creator-docs/art/modeling/texture-specifications]] - Texture specifications.
