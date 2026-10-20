---
title: Export emotes
description: Use the appropriate export settings in Maya and Blender to generate Studio-ready .fbx files.
tags: [roblox, documentation, external-reference, priority-reference, avatar]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [avatar/emotes/export.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/avatar/emotes/export.md). Published page: [https://create.roblox.com/docs/avatar/emotes/export](https://create.roblox.com/docs/avatar/emotes/export).

When you are ready to export animation data that meets Roblox's [[external/roblox-creator-docs/avatar/emotes/specifications|emote specifications]], it's important to review the following prerequisite information and step-by-step instructions for the `.fbx` or `.gltf` export files so that you don't run into any errors for the [[external/roblox-creator-docs/avatar/emotes/import|import]] process.

<Alert severity = 'info'>
<AlertTitle>How do I create animation data?</AlertTitle>
Creators typically use a third-party modeling tool like Blender or Maya to animate a character model. Once the animation is complete, you can export both the model and the animation data as a `.fbx` or `.gltf` file.
</Alert>

## Prerequisites

When you export a character model with full body animation or FACS animation data, ensure that your animation timeline's **Start** and **End** include the entire range of your animation.

<img src="../../assets/art/avatar/basic-creation/Blender-Animation-Start-End.png" width = "60%" alt="Zoom-in of Blender animation track indicating a Start value of 0 and End value of 308." />

## Blender export settings

Blender allows you to export your character model and animation data as either a `.fbx` or `.gltf` file. If you are exporting it as a `.fbx` file, familiarize yourself with [[external/roblox-creator-docs/art/blender#adjust-scale-fbx|Blender's FBX scaling]] to ensure that you successfully import the model into Studio at the correct scale.

To export your character model with animation data in Blender as a `.fbx` file:

1. Ensure your project's animation timeline has the correct **Start** and **End** range of all your keyframes.
1. In the topbar, click **File** > **Export** > **FBX (.fbx)**. The **Blender File View** window displays.
1. On the right-hand side, set **Path Mode** to **Copy**, then toggle the **Embed Textures** button.
1. In the **Include** section, enable **Custom Properties**.
1. In the **Transform** section, set **Apply Scalings** to **FBX Unit Scale**. If you run into scaling issues on import, see [[external/roblox-creator-docs/art/blender#adjust-scale-fbx|Blender FBX scaling]] for alternative approaches.
1. In the **Armature** section, uncheck **Add Leaf Bones**.
1. Enable and expand **Animation**, then:

   1. Uncheck **NLA Strips**, **All Actions**, and **Force Start/End Keyframes**.
   1. Set **Simplify** to `0.0`.

1. Click the **Export FBX** button and save the `.fbx` to the directory of your choice.

<img src="../../assets/art/avatar/basic-creation/Export-Settings.png" width = "50%" alt="Screenshot of Blender export settings" />

## Maya export settings

<Alert severity = 'info'>
For additional context on exporting animations from Maya, see the [[external/roblox-creator-docs/art/characters/export-avatar-animations-from-maya|Export avatar animations from Maya]] tutorial.
</Alert>

To export your character model with animation data in Maya as a `.fbx` file:

1. In the topbar, click **File** > **Export All**. The **Export All** window displays.
1. Near the bottom of the window, click the **Files of type** dropdown, then select **FBX export**.
1. On the right-hand side of the window, navigate to the **Options...** section.
1. In the **Geometry** section, enable **Smooth Mesh** and **Referenced Asset Content**.
1. In the **Animation** section, enable **Animation**. Avatar characters with [[external/roblox-creator-docs/avatar/dynamic-heads/index|dynamic heads]] require animation data.
1. Enable **Bake Animation**.
1. If you need to import textures as a `.png`, in the **Embed Media** section, enable **Embed Media**.
1. In the **Advanced Options** section,

   1. Navigate to **Units**, then enable **Automatic**.
   1. Navigate to **Axis Conversion**, then set the **Up Axis** property to **Y**.

1. Click the **Export All** button and save the `.fbx` to the directory of your choice.

    <img src="../../assets/accessories/lc-requirements-maya-settings-with-animation.png" width = "50%" alt = "Screenshot of Maya export settings for exports with animation."/>


## Related Files

- [[external/roblox-creator-docs/avatar/emotes/specifications]] - Emote specifications.
- [[external/roblox-creator-docs/avatar/emotes/index]] - Emotes.
- [[external/roblox-creator-docs/avatar/emotes/import]] - Import emotes.
