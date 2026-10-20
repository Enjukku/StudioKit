---
title: Export
description: Use Blender's FBX export with specific settings when exporting a clothing asset.
tags: [roblox, documentation, external-reference, priority-reference, art, assets]
prev: /art/accessories/creating/modify-cage
next: /art/accessories/creating/importing
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [art/accessories/creating/exporting.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/art/accessories/creating/exporting.md). Published page: [https://create.roblox.com/docs/art/accessories/creating/exporting](https://create.roblox.com/docs/art/accessories/creating/exporting).

It's important to follow the Blender export settings to ensure a Studio-compatible `.fbx` file. Before exporting your file, ensure that you've removed extra objects, such as lights, cameras, or mannequins, and applied or removed any active modifiers.

To export your file from Blender:

1. In the Outliner, unhide all objects, make them selectable, then select everything in your project.

   <img src="../../../assets/modeling/skinned-meshes/Blender-Export-Settings-0.png" width="320" />

1. In the topbar, click **File** > **Export** > **FBX (.fbx)**. The **Blender File View** window displays.
1. On the right-hand side, set **Path Mode** to **Copy**, then toggle the **Embed Textures** button.

   <img src="../../../assets/modeling/skinned-meshes/Blender-Export-Settings-1.png" width="320" />

1. In the **Include** section, enable **Selected Objects**.
1. In the **Transform** section, set **Apply Scalings** to **FBX Unit Scale**. If you run into scaling issues on import, see [[external/roblox-creator-docs/art/blender#adjust-scale-fbx|Blender FBX scaling]] for alternative approaches.

   <img src="../../../assets/modeling/skinned-meshes/Blender-Export-Settings-5.png" width="320" />

1. In the **Armature** section, disable **Add Leaf Bones**.

   <img src="../../../assets/modeling/skinned-meshes/Blender-Export-Settings-3.png" width="320" />

1. Disable **Bake Animation**.

   <img src="../../../assets/modeling/skinned-meshes/Blender-Export-Settings-4.png" width="320" />

1. Click the **Export FBX** button.

<Alert severity ='success'>
You've completed the exporting section of this tutorial. If desired, download a [reference sample](../../../assets/art/accessories/creating/Long_Sleeve_Export.fbx) of this exported file for comparison. You can use this reference in the next importing step.
</Alert>


## Related Files

- [[external/roblox-creator-docs/art/accessories/creating/armature-setup]] - Armature setup.
- [[external/roblox-creator-docs/art/accessories/creating/caging-setup]] - Caging setup.
- [[external/roblox-creator-docs/art/accessories/creating/converting]] - Convert.
- [[external/roblox-creator-docs/art/accessories/creating/unwrapping]] - Create seams and unwrap.
- [[external/roblox-creator-docs/art/accessories/creating/texture-map]] - Create texture map.
- [[external/roblox-creator-docs/art/accessories/creating/index]] - Create your first layered accessory.
- [[external/roblox-creator-docs/art/accessories/creating/importing]] - Import.
- [[external/roblox-creator-docs/art/accessories/creating/watertight]] - Make mesh watertight.
- [[external/roblox-creator-docs/art/accessories/creating/modeling-setup]] - Modeling setup.
- [[external/roblox-creator-docs/art/accessories/creating/modify-cage]] - Modify outer cage.
- [[external/roblox-creator-docs/art/accessories/creating/sculpting]] - Sculpt detail.
- [[external/roblox-creator-docs/art/accessories/creating/test-poses]] - Test poses.
- [[external/roblox-creator-docs/art/accessories/creating/texture-painting]] - Texture painting.
- [[external/roblox-creator-docs/art/accessories/creating/trimming]] - Trim clothing shape.
