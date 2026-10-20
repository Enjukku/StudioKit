---
title: Export character bodies
description: Use the appropriate export settings in Maya and Blender to generate Studio-ready .fbx files.
tags: [roblox, documentation, external-reference, priority-reference, avatar]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [avatar/character-bodies/export.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/avatar/character-bodies/export.md). Published page: [https://create.roblox.com/docs/avatar/character-bodies/export](https://create.roblox.com/docs/avatar/character-bodies/export).

When you are ready to export a character body model that meets Roblox's [[external/roblox-creator-docs/avatar/character-bodies/specifications|character body specifications]], it's important to review the following prerequisite information and step-by-step instructions for the `.fbx` or `.gltf` export files so that your creation takes advantage of all of Studio's [[external/roblox-creator-docs/studio/importer|Importer]] features.

This is particularly important for character body models because they contain all the mesh and texture data, including the rig and influence data that's essential for characters to move and animate properly across the platform.

<Alert severity = 'warning'>
If you are using Roblox's avatar template files, you must perform the [[external/roblox-creator-docs/art/characters/creating/combine-head-geometry|cleanup steps]] in order for the assets to properly validate.
</Alert>

<Alert severity = 'info'>
<AlertTitle>For other types of 3D models:</AlertTitle>
<ul>
<li>[[external/roblox-creator-docs/art/modeling/export-requirements|General mesh]] export settings.</li>
<li>[[external/roblox-creator-docs/avatar/rigid-accessories/export|Rigid accessory]] export settings.</li>
<li>[[external/roblox-creator-docs/avatar/layered-accessories/export|Layered accessory]] export settings.</li>
</ul>
</Alert>

## Prerequisites

Before you export your custom character body:

- Ensure that you are only exporting the Roblox-supported objects related to your model. If you have any modifiers to your mesh or project objects, make sure to apply or delete them before export.

- While your mesh objects must be parented within an armature object, you can also parent your outer cage objects to a single empty object to simplify your workspace.

  <img src="../../assets/art/avatar/Character-Data-Model-Collapsed.png" width = "60%" alt="Screenshot of a Blender project Outliner with parent objects collapsed." />

- In the cage parent object, ensure you have an [[external/roblox-creator-docs/avatar/character-bodies/specifications#outer-cages|outer cage]] for each of your 15 body parts with appropriate naming affix.

  <img src="../../assets/art/avatar/Character-Data-Model-Cages.png" width = "60%" alt="Screenshot of the 15 outer cage meshes that you must include with a character export."/>

- In the armature object, ensure that you include the all [[external/roblox-creator-docs/avatar/character-bodies/specifications#body-parts|15 mesh objects]] and [[external/roblox-creator-docs/avatar/character-bodies/specifications#attachments|19 attachments]] with the appropriate naming affix.

  <img src="../../assets/art/avatar/Character-Data-Model-Joints.png" width = "60%" alt="Screenshot of 15 child objects parented within an Armature object."/>

<Alert severity = 'info'>
For more information on supported modeling objects and proper configuration, see [[external/roblox-creator-docs/avatar/character-bodies/specifications|Character specifications]].
</Alert>

- When exporting character bodies with animation or FACS animation, ensure that your animation timeline **Start** and **End** include the entire range of your animations.

<img src="../../assets/art/avatar/basic-creation/Blender-Animation-Start-End.png" width = "60%" alt="Zoom-in of Blender animation track indicating a Start value of 0 and End value of 308." />

## Blender export settings

Blender allows you to export your character body as either a `.fbx` or `.gltf` file. If you are exporting it as a `.fbx` file, familiarize yourself with [[external/roblox-creator-docs/art/blender#adjust-scale-fbx|Blender's FBX scaling]] to ensure that you successfully import the model into Studio at the correct scale.

To export your character body in Blender as a `.fbx` file:

1. In the topbar, click **File** > **Export** > **FBX (.fbx)**. The **Blender File View** window displays.
1. On the right-hand side, set **Path Mode** to **Copy**, then toggle the **Embed Textures** button.
1. In the **Include** section, enable **Custom Properties**.
1. In the **Transform** section, set **Apply Scalings** to **FBX Unit Scale**. If you run into scaling issues on import, see [[external/roblox-creator-docs/art/blender#adjust-scale-fbx|Blender FBX scaling]] for alternative approaches.
1. In the **Armature** section, uncheck **Add Leaf Bones**.
1. Enable and expand **Animation**, then:

   1. Uncheck **NLA Strips**, **All Actions**, and **Force Start/End Keyframes**.

      <Alert severity = 'info'>
      Ensure your project animation timeline has the correct **Start** and **End** range of all your keyframes.
      </Alert>
   1. Set **Simplify** to `0.0`.

1. Click the **Export FBX** button and save the `.fbx` to the directory of your choice.

<img src="../../assets/art/avatar/basic-creation/Export-Settings.png" width = "30%" alt="Screenshot of Blender export settings" />

<Alert severity = 'success'>
You now have a `.fbx` file that you can [[external/roblox-creator-docs/avatar/character-bodies/import|import into Studio]] as a `Class.Model` character. Once the character body is in Studio, you can:

- [[external/roblox-creator-docs/avatar/character-bodies/test|Test your character]] using various Studio tooling and workflows.
- [[external/roblox-creator-docs/marketplace/publish-to-marketplace|Upload the character]] to the Marketplace.
- Use the character in an existing game project by applying a [[external/roblox-creator-docs/characters/appearance#manually-modify-appearance|HumanoidDescription]] to the `Class.Model` object.
- [[external/roblox-creator-docs/projects/assets/toolbox|Save the character]] to your **Toolbox** to use within any of your games or share with other creators.

</Alert>

## Maya export settings

To export your character body in Maya as a `.fbx` file:

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

<Alert severity = 'success'>
You now have a `.fbx` file that you can [[external/roblox-creator-docs/avatar/character-bodies/import|import into Studio]] as a `Class.Model` character. Once the character body is in Studio, you can:

- [[external/roblox-creator-docs/avatar/character-bodies/test|Test your character]] using various Studio tooling and workflows.
- [[external/roblox-creator-docs/art/accessories/creating-rigid/publishing|Upload the character]] to the Marketplace.
- Use the character in an existing game project by applying a [[external/roblox-creator-docs/characters/appearance#manually-modify-appearance|HumanoidDescription]] to the `Class.Model` object.
- [[external/roblox-creator-docs/projects/assets/toolbox|Save the character]] to your **Toolbox** to use within any of your games or share with other creators.

</Alert>


## Related Files

- [[external/roblox-creator-docs/avatar/character-bodies/test-blender]] - Blender tests for character bodies.
- [[external/roblox-creator-docs/avatar/character-bodies/index]] - Character bodies.
- [[external/roblox-creator-docs/avatar/character-bodies/project-files]] - Character body reference files.
- [[external/roblox-creator-docs/avatar/character-bodies/specifications]] - Character body specifications.
- [[external/roblox-creator-docs/avatar/character-bodies/import]] - Import character bodies.
- [[external/roblox-creator-docs/avatar/character-bodies/test-studio]] - Studio tests for character bodies.
- [[external/roblox-creator-docs/avatar/character-bodies/test]] - Test character bodies.
