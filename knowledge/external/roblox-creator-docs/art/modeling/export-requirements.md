---
title: Export settings
description: Use the appropriate export settings in Maya and Blender to generate Studio-ready .fbx files.
tags: [roblox, documentation, external-reference, priority-reference, art, assets]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [art/modeling/export-requirements.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/art/modeling/export-requirements.md). Published page: [https://create.roblox.com/docs/art/modeling/export-requirements](https://create.roblox.com/docs/art/modeling/export-requirements).

Export your mesh or model as a `.fbx` to take advantage of all of Studio's 3D import features. When rigging or skinning a model, a `.fbx` export contains both the rig and influence data you need to later [[external/roblox-creator-docs/parts/meshes#import-meshes|import]] into Studio.

Check that your model meets Roblox's [[external/roblox-creator-docs/art/modeling/specifications|modeling specifications]] before exporting to ensure Studio compatibility. Specific types of assets, like characters and accessories, have additional specifications:

<Alert severity = 'warning'>
<AlertTitle>If creating other types of 3D models:</AlertTitle>
<ul>
<li>For rigid accessories, see [[external/roblox-creator-docs/avatar/rigid-accessories/specifications|accessory specifications]] and [[external/roblox-creator-docs/avatar/rigid-accessories/export|accessory export settings]].</li> <br />
<li>For layered accessories, see [[external/roblox-creator-docs/avatar/layered-accessories/specifications|layered accessory specifications]] and [[external/roblox-creator-docs/avatar/layered-accessories/export|layered export settings]].</li> <br />
<li>For avatar characters, see [[external/roblox-creator-docs/avatar/character-bodies/specifications|avatar specifications]] and [[external/roblox-creator-docs/avatar/character-bodies/export|avatar export settings]].</li>
</ul>
</Alert>

## Blender

To export the `.fbx` file in Blender:

1. In the topbar, click **File**. A pop-up menu displays.
2. Select **Export**, then **FBX (.fbx)**. The **Blender File View** window displays.
3. On the right-hand side, change **Path Mode** to **Copy**, then toggle the **Embed Textures** button.

   <img src="../../assets/modeling/skinned-meshes/Blender-Export-Settings-1.png" width="320" alt="Blender export sidebar showing Path Mode set to Copy and the Embed Textures button enabled."/>

4. Set **Transform** > **Apply Scalings** to **FBX Unit Scale**. If you run into scaling issues on import, see [[external/roblox-creator-docs/art/blender#adjust-scale-fbx|Blender FBX scaling]] for alternative approaches.

   <img src="../../assets/modeling/skinned-meshes/Blender-Export-Settings-5.png" width="320" alt="Blender export sidebar showing Apply Scalings set to FBX Unit Scale."/>

5. Under the **Armature** section, disable **Add Leaf Bones**.

   <img src="../../assets/modeling/skinned-meshes/Blender-Export-Settings-3.png" width="320" alt="Blender export sidebar showing Transform Scale set to .01"/>

6. Unless exporting content with animation keyframes, such as a walk cycle or a character with [[external/roblox-creator-docs/avatar/dynamic-heads/index|facial animation data]], disable **Bake Animation**.

   <img src="../../assets/modeling/skinned-meshes/Blender-Export-Settings-4.png" width="320" alt="Blender export sidebar showing Add Leaf Bones as unchecked"/> <br />

7. Click the **Export FBX** button.

## Maya

To export a mesh in Maya as a `.fbx` file:

1. In the topbar, click **File**. A pop-up menu displays.
2. Select **Export All**. The **Export All** window displays.
3. Near the bottom of the window, click the **Files of type** dropdown, then select **FBX export**.
4. On the right-hand side of the window, navigate to the **Options...** section.
5. In the **Geometry** section, enable **Smooth Mesh** and **Referenced Asset Content**.
6. In the **Animation** section, disable **Animation**, unless you need to import an animation to Studio. Some avatar assets require animation.
   1. If you are exporting animation, enable **Bake Animation**.
7. If you need to import textures as a `.png`, in the **Embed Media** section, enable **Embed Media**.
8. In the **Advanced Options** section,
   - Navigate to **Units**, then enable **Automatic**.
   - Navigate to **Axis Conversion**, then set the **Up Axis** property to **Y**.
9. Click the **Export All** button.

   <img src="../../assets/accessories/lc-requirements-maya-settings.png" alt="Maya export sidebar showing Bake Animation as unchecked"  />


## Related Files

- [[external/roblox-creator-docs/art/modeling/gltf-export]] - 3D Export.
- [[external/roblox-creator-docs/art/modeling/assign-textures]] - Blender and Maya texture settings.
- [[external/roblox-creator-docs/art/modeling/calisthenics-tool]] - Calisthenics Tool.
- [[external/roblox-creator-docs/art/modeling/index]] - Custom 3D assets.
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
