---
title: Layered clothing export settings
description: Use the appropriate export settings in Maya and Blender to generate Studio-ready .fbx files.
tags: [roblox, documentation, external-reference, priority-reference, art, assets]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [art/accessories/clothing-export-settings.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/art/accessories/clothing-export-settings.md). Published page: [https://create.roblox.com/docs/art/accessories/clothing-export-settings](https://create.roblox.com/docs/art/accessories/clothing-export-settings).

> [!warning] Not in the current upstream docs
> Not published in [github.com/Roblox/creator-docs](https://github.com/Roblox/creator-docs) as of 2026-10-20 (revision `74006430`). The closest current page is [[external/roblox-creator-docs/avatar/layered-accessories/export]]. Kept locally so existing links keep working; read that page for current information.

Export your mesh or model as a `.fbx` or `.gltf` to take advantage of all of Studio's 3D import features. When rigging or skinning a layerable model, these file types contain all the mesh and texture data, including the rig and influence data, you need to later [[external/roblox-creator-docs/studio/importer|import]] into Studio.

<Alert severity = 'warning'>
<AlertTitle>If creating other types of 3D models:</AlertTitle>
<ul>
<li>For generic meshes, see [[external/roblox-creator-docs/art/modeling/specifications|general mesh specifications]] and [[external/roblox-creator-docs/art/modeling/export-requirements|general export settings]].</li> <br />
<li>For rigid accessories, see [[external/roblox-creator-docs/art/accessories/specifications|accessory specifications]] and [[external/roblox-creator-docs/art/accessories/export-settings|accessory export settings]].</li> <br />
<li>For avatar characters, see [[external/roblox-creator-docs/art/characters/specifications|avatar specifications]] and [[external/roblox-creator-docs/art/characters/export-settings|avatar export settings]].</li>
</ul>
</Alert>

## Before exporting

Before exporting, ensure that you are only exporting the Roblox supported objects related to your model. If you have any modifiers to your mesh or project objects, make sure to apply or delete them before export.

You can export layered clothing models with the following object structure:

<img src="../../assets/modeling/skinned-meshes/Clothing-Data-Model.png" width="60%" alt="Blender clothing data model example" />

- Armature parent
  - Bones / joints
  - Primary mesh object
- Cage parent object

  - Inner cage mesh object
  - Outer cage mesh object

You can also export shoes together. Even though left and right shoes are separate accessories, you can either export the left and right shoe individually, or export both shoes at the same time using the following structure:

<img src="../../assets/modeling/skinned-meshes/Shoe-Data-Model.png" width="60%" alt="Shoe clothing data model example"/>

- Armature parent
  - Bones / joints
  - Left shoe mesh object
  - Right shoe mesh object
- Cage parent object
  - Left shoe inner cage
  - Left shoe outer cage
  - Right shoe inner cage
  - Right shoe outer cage

<Alert severity = 'warning'>
Each shoe must include their own inner and outer cage.
</Alert>

## Blender

Blender allows you to export in `.fbx` or `.gltf` as well as other formats. If you are using `.fbx` export, familiarize yourself with [[external/roblox-creator-docs/art/blender#adjust-scale-fbx|Blender's FBX scaling]] to ensure that you successfully import the model into Studio at the correct scale.

### Export settings

To export the `.fbx` file in Blender:

1. In the topbar, click **File**. A pop-up menu displays.
2. Select **Export**, then **FBX (.fbx)**. The **Blender File View** window displays.
3. On the right-hand side, change the **Path Mode** property to **Copy**, then toggle the **Embed Textures** button.

   <img src="../../assets/modeling/skinned-meshes/Blender-Export-Settings-1.png" width="320" />

4. If your project doesn't already have `.01` scene unit scaling, set the **Transform** > **Apply Scalings** to `FBX Unit Scale`. For more details, see [[external/roblox-creator-docs/art/blender#adjust-scale-fbx|Blender FBX scaling]].

   <img src="../../assets/modeling/skinned-meshes/Blender-Export-Settings-5.png" width="320" />

5. Under the **Armature** section, disable **Add Leaf Bones**.

   <img src="../../assets/modeling/skinned-meshes/Blender-Export-Settings-3.png" width="320" />

6. Click the **Export FBX** button.
7. After exporting, use Studio's [[external/roblox-creator-docs/studio/importer|Importer]] to import your model and the [[external/roblox-creator-docs/art/accessories/accessory-fitting-tool|Accessory Fitting Tool]] to convert the model into an accessory.

## Maya export settings

To export a mesh in Maya as a `.fbx` file:

1. In the topbar, click **File**. A pop-up menu displays.
2. Select **Export All**. The **Export All** window displays.
3. Near the bottom of the window, click the **Files of type** dropdown, then select **FBX export**.
4. On the right-hand side of the window, navigate to the **Options...** section.
5. In the **Geometry** section, enable **Smooth Mesh** and **Referenced Asset Content**.
6. If you need to import textures as a `.png`, in the **Embed Media** section, enable **Embed Media**.
7. In the **Advanced Options** section,
   - Navigate to **Units**, then enable **Automatic**.
   - Navigate to **Axis Conversion**, then set the **Up Axis** property to **Y**.
8. Click the **Export All** button.
   <img src="../../assets/accessories/lc-requirements-maya-settings-with-animation.png" />
9. After exporting, use Studio's [[external/roblox-creator-docs/studio/importer|Importer]] to import your model and the [[external/roblox-creator-docs/art/accessories/accessory-fitting-tool|Accessory Fitting Tool]] to convert the model into an accessory.


## Related Files

- [[external/roblox-creator-docs/art/index]] - 3D art in Roblox.
- [[external/roblox-creator-docs/art/accessories/from-existing]] - Accessories from an existing model.
- [[external/roblox-creator-docs/art/accessories/accessory-fitting-tool]] - Accessory Fitting Tool.
- [[external/roblox-creator-docs/art/accessories/project-files]] - Accessory project files and references.
- [[external/roblox-creator-docs/art/accessories/automatic-skinning-transfer]] - Automatic Skinning Transfer.
- [[external/roblox-creator-docs/art/blender]] - Blender.
- [[external/roblox-creator-docs/art/accessories/body-scale]] - Body scale and proportions.
- [[external/roblox-creator-docs/art/accessories/caging-best-practices]] - Caging best practices.
- [[external/roblox-creator-docs/art/characters/export-settings]] - Character body export settings.
- [[external/roblox-creator-docs/art/characters/specifications]] - Character specifications.
- [[external/roblox-creator-docs/art/accessories/clothing-specifications]] - Clothing specifications.
- [[external/roblox-creator-docs/art/accessories/validation-tool]] - Clothing Validation Tool.
- [[external/roblox-creator-docs/art/modeling/export-requirements]] - Export settings.
- [[external/roblox-creator-docs/art/modeling/specifications]] - General specifications.
- [[external/roblox-creator-docs/studio/importer]] - Importer.
- [[external/roblox-creator-docs/art/accessories/index]] - Rigid accessories.
- [[external/roblox-creator-docs/art/accessories/export-settings]] - Rigid accessory export settings.
- [[external/roblox-creator-docs/art/accessories/specifications]] - Rigid accessory specifications.
