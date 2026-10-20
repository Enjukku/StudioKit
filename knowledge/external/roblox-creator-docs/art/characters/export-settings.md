---
title: Character body export settings
description: Use the appropriate export settings in Maya and Blender to generate Studio-ready .fbx files.
tags: [roblox, documentation, external-reference, priority-reference, art, assets]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [art/characters/export-settings.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/art/characters/export-settings.md). Published page: [https://create.roblox.com/docs/art/characters/export-settings](https://create.roblox.com/docs/art/characters/export-settings).

> [!warning] Not in the current upstream docs
> Not published in [github.com/Roblox/creator-docs](https://github.com/Roblox/creator-docs) as of 2026-10-20 (revision `74006430`). The closest current page is [[external/roblox-creator-docs/avatar/character-bodies/export]]. Kept locally so existing links keep working; read that page for current information.

<Alert severity = 'warning'>
It's important to test your assets multiple times at every point of the asset creation process, whether it is within your modeling application or after importing into Studio. See [[external/roblox-creator-docs/art/characters/testing/index|Test characters]] for more information.
</Alert>

Export your model as a `.fbx` or `.gltf` to take advantage of all of Studio's 3D import features. When rigging or skinning a layerable model, these file types contain all the mesh and texture data, including the rig and influence data, you need to later [[external/roblox-creator-docs/studio/importer|import]] into Studio.

Check that your model meets Roblox's [[external/roblox-creator-docs/art/characters/specifications|avatar character specifications]] before exporting to ensure Studio compatibility.

<Alert severity = 'warning'>
<AlertTitle>If creating other types of 3D models:</AlertTitle>
<ul>
<li>For generic meshes, see [[external/roblox-creator-docs/art/modeling/specifications|general mesh specifications]] and [[external/roblox-creator-docs/art/modeling/export-requirements|general export settings]].</li> <br />
<li>For rigid accessories, see [[external/roblox-creator-docs/art/accessories/specifications|accessory specifications]] and [[external/roblox-creator-docs/art/accessories/export-settings|accessory export settings]].</li> <br />
<li>For layered accessories, see [[external/roblox-creator-docs/art/accessories/clothing-specifications|layered accessory specifications]] and [[external/roblox-creator-docs/art/accessories/clothing-export-settings|layered export settings]].</li> <br />
</ul>
</Alert>

<Alert severity = 'error'>
If you are using Roblox's avatar template files, you must perform the [[external/roblox-creator-docs/art/characters/creating/combine-head-geometry|cleanup steps]] in order for the assets to properly validate.
</Alert>

## Before exporting

Before exporting, ensure that you are only exporting the Roblox supported objects related to your model. If you have any modifiers to your mesh or project objects, make sure to apply or delete them before export.

Use the following guidance before exporting:

- While your mesh objects must be parented within an armature object, you can also parent your outer cage objects to a single empty object to simplify your workspace.

  <img src="../../assets/art/avatar/Character-Data-Model-Collapsed.png" width = "60%" alt="Screenshot of a Blender project Outliner with parent objects collapsed." />

- In the cage parent object, ensure you have an [[external/roblox-creator-docs/art/characters/specifications#outer-cages|outer cage]] for each of your 15 body parts with appropriate naming affix.

  <img src="../../assets/art/avatar/Character-Data-Model-Cages.png" width = "60%" alt="Screenshot of the 15 outer cage meshes that you must include with a character export."/>

- In the armature object, ensure that you include the all [[external/roblox-creator-docs/art/characters/specifications#body-parts|15 mesh objects]] and [[external/roblox-creator-docs/art/characters/specifications#attachments|19 attachments]] with the appropriate naming affix.

  <img src="../../assets/art/avatar/Character-Data-Model-Joints.png" width = "60%" alt="Screenshot of 15 child objects parented within an Armature object."/>

<Alert severity = 'info'>
For more information on supported modeling objects and proper configuration, see [[external/roblox-creator-docs/art/characters/specifications|Character specifications]].
</Alert>

- When exporting characters with animation or FACS animation, ensure that your animation timeline **Start** and **End** include the entire range of your animations.

<img src="../../assets/art/avatar/basic-creation/Blender-Animation-Start-End.png" width = "60%" alt="Zoom-in of Blender animation track indicating a Start value of 0 and End value of 308." />

## Blender

Blender allows you to export in `.fbx` or `.gltf` as well as other formats. If you are using `.fbx` export, familiarize yourself with [[external/roblox-creator-docs/art/blender#adjust-scale-fbx|Blender's FBX scaling]] to ensure that you successfully import the model into Studio at the correct scale.

### Export settings

1. In the topbar, click **File** > **Export** > **FBX (.fbx)**. The Blender file browser window displays.
2. Set **Path Mode** to **Copy** and enable the **Embed Textures** icon.
3. In the Include section, enable **Custom Properties**.
4. If your project doesn't already have `.01` scene unit scaling, set the **Transform** > **Apply Scalings** to `FBX Unit Scale`. For more details, see [[external/roblox-creator-docs/art/blender#adjust-scale-fbx|Blender FBX scaling]].
5. Expand the Armature section and uncheck **Add Leaf Bones**.
6. Enable **Bake Animation**.
7. Expand Bake Animation and **uncheck NLA Strips**, **All Actions**, and **Force Start/End Keyframes**.
   1. Ensure your project animation timeline has the correct **Start** and **End** range of all your keyframes.
8. In Bake Animation, set **Simplify** to **0.0**.
9. Click the **Export FBX** button. Save the `.fbx` to the directory of your choice.

<img src="../../assets/art/avatar/basic-creation/Export-Settings.png" width = "50%" alt="Screenshot of Blender export settings" />

## Maya export settings

To export a mesh in Maya as a `.fbx` file:

1. In the topbar, click **File**. A pop-up menu displays.
2. Select **Export All**. The **Export All** window displays.
3. Near the bottom of the window, click the **Files of type** dropdown, then select **FBX export**.
4. On the right-hand side of the window, navigate to the **Options...** section.
5. In the **Geometry** section, enable **Smooth Mesh** and **Referenced Asset Content**.
6. In the **Animation** section, enable **Animation**. Avatar characters with [[external/roblox-creator-docs/art/characters/facial-animation/index|facial animation data]] require animation data.
7. Enable **Bake Animation**.
8. If you need to import textures as a `.png`, in the **Embed Media** section, enable **Embed Media**.
9. In the **Advanced Options** section,
   - Navigate to **Units**, then enable **Automatic**.
   - Navigate to **Axis Conversion**, then set the **Up Axis** property to **Y**.
10. Click the **Export All** button.

    <img src="../../assets/accessories/lc-requirements-maya-settings-with-animation.png" alt = "Screenshot of Maya export settings for exports with animation."/>

11. After exporting, use Studio's [[external/roblox-creator-docs/studio/importer|Importer]] to import your model. See [[external/roblox-creator-docs/art/characters/testing/studio|Test characters in Studio]] for additional importing and testing information.

<Alert severity = 'success'>
After importing the `Class.Model` character to Studio, you can now perform the following with this asset:

- [[external/roblox-creator-docs/art/characters/testing/index|Test your character model]] in Studio using various tools and workflows.
- [[external/roblox-creator-docs/art/accessories/creating-rigid/publishing|Upload the character]] to the Marketplace.
- Use the humanoid character on an existing experience by applying a [[external/roblox-creator-docs/characters/appearance#manually-modify-appearance|HumanoidDescription]]to the `Class.Model` object.
- Save the asset to your [[external/roblox-creator-docs/projects/assets/toolbox|Toolbox]] to share or use within any of your experiences.

</Alert>


## Related Files

- [[external/roblox-creator-docs/art/index]] - 3D art in Roblox.
- [[external/roblox-creator-docs/art/characters/index]] - Avatar characters.
- [[external/roblox-creator-docs/art/characters/project-files]] - Avatar project files and references.
- [[external/roblox-creator-docs/art/blender]] - Blender.
- [[external/roblox-creator-docs/art/characters/validation-tool]] - Blender validation tool.
- [[external/roblox-creator-docs/characters/appearance]] - Character appearance.
- [[external/roblox-creator-docs/art/characters/specifications]] - Character specifications.
- [[external/roblox-creator-docs/art/characters/head-comparison]] - Classic and Dynamic head comparison.
- [[external/roblox-creator-docs/art/accessories/clothing-specifications]] - Clothing specifications.
- [[external/roblox-creator-docs/art/characters/creating/combine-head-geometry]] - Combine head geometry.
- [[external/roblox-creator-docs/art/characters/export-avatar-animations-from-maya]] - Export avatar animations from Maya.
- [[external/roblox-creator-docs/art/modeling/export-requirements]] - Export settings.
- [[external/roblox-creator-docs/art/characters/face-caging-best-practices]] - Face caging best practices.
- [[external/roblox-creator-docs/art/modeling/specifications]] - General specifications.
- [[external/roblox-creator-docs/art/characters/head-specifications]] - Head specifications.
- [[external/roblox-creator-docs/art/characters/facial-animation/index]] - Heads.
- [[external/roblox-creator-docs/studio/importer]] - Importer.
- [[external/roblox-creator-docs/art/accessories/clothing-export-settings]] - Layered clothing export settings.
- [[external/roblox-creator-docs/art/accessories/export-settings]] - Rigid accessory export settings.
- [[external/roblox-creator-docs/art/accessories/specifications]] - Rigid accessory specifications.
- ...and 4 more local docs.
