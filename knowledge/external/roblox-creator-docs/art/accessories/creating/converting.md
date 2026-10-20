---
title: Convert
description: Use the Accessory Fitting Tool to convert a Model object to an Accessory.
tags: [roblox, documentation, external-reference, priority-reference, art, assets]
prev: /art/accessories/creating/importing
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [art/accessories/creating/converting.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/art/accessories/creating/converting.md). Published page: [https://create.roblox.com/docs/art/accessories/creating/converting](https://create.roblox.com/docs/art/accessories/creating/converting).

With the `Class.Model` in your project, the last step in the process of clothing creation requires you to convert this object to a standard `Class.Accessory` that avatars can equip. Using the [[external/roblox-creator-docs/avatar/accessory-fitting-tool|Accessory Fitting Tool]] (AFT), convert the model object to a `Class.Accessory` that you can then use in your game or publish to the Marketplace.

To generate the accessory object:

1. In the **Avatar** tab, click **Accessory** to open the AFT. The **Accessory Fitting Tool** panel displays.
1. In the panel:

   1. Select the **Part** field, then in the **Explorer** window, select the layered accessory `Class.MeshPart` object.
   1. Back in the panel, click the **Next** button. The **Asset Type** page displays.

1. In the **Asset Type** page:

   1. Set asset type to **Clothing**, then use the dropdown menu to select the clothing type. This tutorial sets it to **Shirt**.
   1. Click the **Next** button. A preview panel displays with a default character wearing your layered accessory.

1. Test out various sample characters, clothing, and animations. If necessary, make minor cage adjustments using the editing features, or larger cage changes back in your third-party modeling software. For more information on this process, see [[external/roblox-creator-docs/avatar/accessory-fitting-tool#test-accessories|Accessory Fitting Tool - Test accessories]].
1. After previewing your asset, click the **Generate MeshPart Accessory** button. Your 3D model populates in your project as an `Class.Accessory` object.

<GridContainer numColumns="2">
  <figure>
    <img src="../../../assets/art/accessories/creating/Exporting-Clothing-in-Studio-Highlight.png" />
    <figcaption>Clothing accessory in viewport</figcaption>
  </figure>
  <figure>
    <img src="../../../assets/art/accessories/creating/Exporting-Accessory-Explorer.png" />
    <figcaption>Clothing accessory in Explorer</figcaption>
  </figure>
</GridContainer>

<Alert severity = 'success'>
Congratulations, you've completed the layered accessory tutorial. With your new `Class.Accessory`, you can perform any of the following:

- [[external/roblox-creator-docs/art/accessories/creating-rigid/publishing|Upload the accessory]] to the Marketplace.
- Use the accessory in your current game by equipping it to character models with a [[external/roblox-creator-docs/characters/appearance#manually-modify-appearance|`HumanoidDescription`]], or by dragging and dropping the accessory under the appropriate character `Class.Model` object.
- Save the accessory to your [[external/roblox-creator-docs/projects/assets/toolbox|Toolbox]] to share or use within any of your games.

</Alert>


## Related Files

- [[external/roblox-creator-docs/art/accessories/creating/armature-setup]] - Armature setup.
- [[external/roblox-creator-docs/art/accessories/creating/caging-setup]] - Caging setup.
- [[external/roblox-creator-docs/art/accessories/creating/unwrapping]] - Create seams and unwrap.
- [[external/roblox-creator-docs/art/accessories/creating/texture-map]] - Create texture map.
- [[external/roblox-creator-docs/art/accessories/creating/index]] - Create your first layered accessory.
- [[external/roblox-creator-docs/art/accessories/creating/exporting]] - Export.
- [[external/roblox-creator-docs/art/accessories/creating/importing]] - Import.
- [[external/roblox-creator-docs/art/accessories/creating/watertight]] - Make mesh watertight.
- [[external/roblox-creator-docs/art/accessories/creating/modeling-setup]] - Modeling setup.
- [[external/roblox-creator-docs/art/accessories/creating/modify-cage]] - Modify outer cage.
- [[external/roblox-creator-docs/art/accessories/creating/sculpting]] - Sculpt detail.
- [[external/roblox-creator-docs/art/accessories/creating/test-poses]] - Test poses.
- [[external/roblox-creator-docs/art/accessories/creating/texture-painting]] - Texture painting.
- [[external/roblox-creator-docs/art/accessories/creating/trimming]] - Trim clothing shape.
