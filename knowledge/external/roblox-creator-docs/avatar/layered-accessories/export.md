---
title: Export layered accessories
description: Use the appropriate export settings in Blender and Maya to generate Studio-ready .fbx files.
tags: [roblox, documentation, external-reference, priority-reference, avatar]
keywords:
  - Layered clothing
  - Layerable accessories
  - Layered clothing accessories
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [avatar/layered-accessories/export.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/avatar/layered-accessories/export.md). Published page: [https://create.roblox.com/docs/avatar/layered-accessories/export](https://create.roblox.com/docs/avatar/layered-accessories/export).

When you are ready to export a layered accessory model that meets Roblox's [[external/roblox-creator-docs/avatar/layered-accessories/specifications|layered accessory specifications]], it's important to review the following prerequisite information and step-by-step instructions for the `.fbx` or `.gltf` export files so that your creation takes advantage of all of Studio's [[external/roblox-creator-docs/studio/importer|Importer]] features.

This is particularly important for layered accessory models because they contain all the mesh and texture data, including the rig and influence data that's essential for accessories to move and animate properly with character bodies across the platform.

<Alert severity = 'info'>
<AlertTitle>For other types of 3D models:</AlertTitle>
<ul>
<li>[[external/roblox-creator-docs/art/modeling/export-requirements|General mesh]] export settings.</li>
<li>[[external/roblox-creator-docs/avatar/rigid-accessories/export|Rigid accessory]] export settings.</li>
</ul>
</Alert>

## Prerequisites

Before you export your custom layered accessory, ensure that you are only exporting the Roblox supported objects related to your model. If you have any modifiers to your mesh or project objects, make sure to apply or delete them before export.

You can export layered accessory models with the following object structure:

<table>
<tbody>
  <tr>
    <td><ul><li>Armature parent<ul><br /><li>Bones / joints</li><li>Primary mesh object</li></ul></li><li>Cage parent object<ul><br /><li>Inner cage mesh object</li><li>Outer cage mesh object</li></ul></li></ul></td>
    <td><img src="../../assets/modeling/skinned-meshes/Clothing-Data-Model.png" width="100%" alt="Blender layered accessory data model example" /></td>
  </tr>
</tbody>
</table>

You can also export shoes together. Even though left and right shoes are separate layered accessories, you can either export the left and right shoe individually, or export both shoes at the same time using the following structure:

<table>
<tbody>
  <tr>
    <td><ul><li>Armature parent<ul><br /><li>Bones / joints</li><li>Left shoe mesh object</li><li>Right shoe mesh object</li></ul></li><li>Cage parent object<ul><br /><li>Left shoe inner cage</li><li>Left shoe outer cage</li><li>Right shoe inner cage</li><li>Right shoe outer cage</li></ul></li></ul></td>
    <td><img src="../../assets/modeling/skinned-meshes/Shoe-Data-Model.png" width="100%" alt="Shoe layered accessory data model example"/></td>
  </tr>
</tbody>
</table>

<Alert severity = 'warning'>
Each shoe must include their own inner and outer cage.
</Alert>

## Blender export settings

Blender allows you to export your layered accessory as either a `.fbx` or `.gltf` file. If you are exporting it as a `.fbx` file, familiarize yourself with [[external/roblox-creator-docs/art/blender#adjust-scale-fbx|Blender's FBX scaling]] to ensure that you successfully import the model into Studio at the correct scale.

To export your layered accessory in Blender as a `.fbx` file:

1. In the topbar, click **File** > **Export** > **FBX (.fbx)**. The **Blender File View** window displays.
1. On the right-hand side, set **Path Mode** to **Copy**, then toggle the **Embed Textures** button.

   <img src="../../assets/modeling/skinned-meshes/Blender-Export-Settings-1.png" width="320" />

1. In the **Transform** section, set **Apply Scalings** to **FBX Unit Scale**. If you run into scaling issues on import, see [[external/roblox-creator-docs/art/blender#adjust-scale-fbx|Blender FBX scaling]] for alternative approaches.

   <img src="../../assets/modeling/skinned-meshes/Blender-Export-Settings-5.png" width="320" />

1. In the **Armature** section, uncheck **Add Leaf Bones**.

   <img src="../../assets/modeling/skinned-meshes/Blender-Export-Settings-3.png" width="320" />

1. Click the **Export FBX** button and save the `.fbx` to the directory of your choice.

<Alert severity = 'success'>
You now have a `.fbx` file that you can [[external/roblox-creator-docs/avatar/layered-accessories/import|import into Studio]] as a `Class.Model` layered accessory. Once the layered accessory is in Studio, you can use the [[external/roblox-creator-docs/avatar/accessory-fitting-tool|Accessory Fitting Tool]] to convert the model into an accessory.
</Alert>

## Maya export settings

To export your layered accessory in Maya as a `.fbx` file:

1. In the topbar, click **File** > **Export All**. The **Export All** window displays.
1. Near the bottom of the window, click the **Files of type** dropdown, then select **FBX export**.
1. On the right-hand side of the window, navigate to the **Options...** section.
1. In the **Geometry** section, enable **Smooth Mesh** and **Referenced Asset Content**.
1. If you need to import textures as a `.png`, in the **Embed Media** section, enable **Embed Media**.
1. In the **Advanced Options** section,
   - Navigate to **Units**, then enable **Automatic**.
   - Navigate to **Axis Conversion**, then set the **Up Axis** property to **Y**.
1. Click the **Export All** button and save the `.fbx` to the directory of your choice.

    <img src="../../assets/accessories/lc-requirements-maya-settings-with-animation-layeredaccessories.png" width = "50%" alt = "Screenshot of Maya export settings for exports with animation."/>

<Alert severity = 'success'>
You now have a `.fbx` file that you can [[external/roblox-creator-docs/avatar/layered-accessories/import|import into Studio]] as a `Class.Model` layered accessory. Once the layered accessory is in Studio, you can use the [[external/roblox-creator-docs/avatar/accessory-fitting-tool|Accessory Fitting Tool]] to convert the model into an accessory.
</Alert>


## Related Files

- [[external/roblox-creator-docs/avatar/layered-accessories/import]] - Import layered accessories.
- [[external/roblox-creator-docs/avatar/layered-accessories/index]] - Layered accessories.
- [[external/roblox-creator-docs/avatar/layered-accessories/caging-best-practices]] - Layered accessory caging best practices.
- [[external/roblox-creator-docs/avatar/layered-accessories/project-files]] - Layered accessory reference files.
- [[external/roblox-creator-docs/avatar/layered-accessories/specifications]] - Layered accessory specifications.
