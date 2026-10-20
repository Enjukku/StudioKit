---
title: Import layered accessories
description: Use the Importer to add third-party models to Studio before using the Accessory Fitting Tool to convert the model to an Accessory.
tags: [roblox, documentation, external-reference, priority-reference, avatar]
keywords:
  - Layered clothing
  - Layerable accessories
  - Layered clothing accessories
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [avatar/layered-accessories/import.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/avatar/layered-accessories/import.md). Published page: [https://create.roblox.com/docs/avatar/layered-accessories/import](https://create.roblox.com/docs/avatar/layered-accessories/import).

Studio's Importer lets you import 3D assets into your projects, such as character bodies, makeup, and layered accessories. The following instructions detail how to import a layered accessory `.fbx` or `.gltf` file into Studio as a `Model` object and convert it into an `Accessory` object that you can use in your games, upload to the Marketplace, or share with other creators.

While the Importer provides object previews and error-checking to ensure that your creation meets Roblox's [[external/roblox-creator-docs/art/modeling/specifications|general 3D requirements]], it's important to ensure that your character model also meets Roblox's [[external/roblox-creator-docs/avatar/layered-accessories/specifications|layered accessory specifications]] to use or sell this asset as an avatar-ready layered accessory, otherwise you can encounter errors at different points in the workflow.

## Import accessories

To import your asset as a layered accessory:

1. In the **Home** tab, click the **Import** button to open the Importer. A file browser opens.
1. Select your layered accessory's `.fbx` or `.gltf` file. The Importer loads a preview of the layered accessory.

      <img src="../../assets/art/accessories/creating/Import-Layered-Accessory.png" width = "80%"/>

1. Select **Import**. The asset populates in your workspace as a `Class.Model` with the appropriate textures applied as a `Class.SurfaceAppearance` or `Class.MeshPart.TextureID`.

<BaseAccordion>
<AccordionSummary>Textures didn't load correctly?</AccordionSummary>
<AccordionDetails>
If your textures didn't load correctly, you can import them manually using the [[external/roblox-creator-docs/projects/assets/manager|Asset Manager]]:

1. In the **Asset Manager**, click the **Import** button. If you are unable to access the Asset Manager, save and publish your game first.
1. Upload your image files.
1. After moderation clears your images, select the `Class.MeshPart` parented within your imported `Class.Model`.
1. If you are using a single basic texture, set the `Class.MeshPart.TextureID` property to your uploaded texture image.
1. If you are using PBR textures:

   1. Add a `Class.SurfaceAppearance` child to your `Class.MeshPart`.

      <img src="../../assets/art/avatar/Avatar-Surface-Appearance.png" width = "40%"/>

   1. In the `Class.SurfaceAppearance` properties, click each property value and assign the appropriate texture image from the asset dropdown:

      1. Set the **ColorMap** to the **\_ALB** texture image.
      1. Set the **MetalnessMap** to the **\_MTL** texture image.
      1. Set the **NormalMap** to the **\_NOR** texture image.
      1. Set the **RoughnessMap** to the **\_RGH** texture image.

      <img src="../../assets/art/avatar/Avatar-Roughness-Map.png" width = "50%"/>

</AccordionDetails>
</BaseAccordion>

## Convert layered accessories

After importing your asset into Studio, you can begin **converting** the `Class.Model` object into a `Class.Accessory` using the [[external/roblox-creator-docs/avatar/accessory-fitting-tool|Accessory Fitting Tool]] (AFT) so that avatar character bodies can equip your layered accessory.

<Alert severity = 'warning'>
For shoes, you must convert the left shoe and the right shoe as separate layered accessories. Use the following instructions for each shoe before grouping both shoe accessories as a `Class.Model` when [[external/roblox-creator-docs/marketplace/publish-to-marketplace#upload-an-asset|saving to Roblox]].
</Alert>

To generate your layered accessory:

1. In the toolbar's **Avatar** tab, click **Accessory** to open the AFT. The **Accessory Fitting Tool** panel displays.
1. In the panel:

   1. Select the **Part** field, then in the **Explorer** window, select the layered accessory `Class.MeshPart` object.
   1. Back in the panel, click the **Next** button. The **Asset Type** page displays.

   <img src="../../assets/art/accessories/creating/AFT-Select-Mesh-Pants.png" />

1. In the **Asset Type** page:

   1. Set asset type to **Clothing**, then use the dropdown menu to choose the clothing type of your layered accessory.
   1. Click the **Next** button. A preview panel displays with a default character wearing your layered accessory.

   <img src="../../assets/art/accessories/creating/AFT-Select-Type-Pants.png" />

1. [[external/roblox-creator-docs/avatar/accessory-fitting-tool#test-accessories|Test]] out various sample characters and animations to make sure your layered accessory is deforming and moving correctly.

   - If necessary, make minor cage adjustments using the editing features. Larger cage changes may require returning to your third-party modeling software and re-exporting the asset.

1. After previewing your asset, click the **Generate MeshPart Accessory** button. Your 3D model populates in your project as an `Class.Accessory` object.

With this `Class.Accessory` object, you can perform any of the following:

- Begin the process of [[external/roblox-creator-docs/marketplace/publish-to-marketplace#upload-an-asset|uploading and publishing]] the layered accessory to the Marketplace.

- Use the layered accessory in your current game by equipping it to character models with [[external/roblox-creator-docs/characters/appearance#manually-modify-appearance|HumanoidDescription]], or by dragging and dropping the layered accessory under the appropriate character `Class.Model` object.

- Save the layered accessory to your [[external/roblox-creator-docs/projects/assets/toolbox|Toolbox]] or make it public on the [[external/roblox-creator-docs/production/creator-store|Creator Store]] to use within any of your games or share with other creators.


## Related Files

- [[external/roblox-creator-docs/avatar/layered-accessories/export]] - Export layered accessories.
- [[external/roblox-creator-docs/avatar/layered-accessories/index]] - Layered accessories.
- [[external/roblox-creator-docs/avatar/layered-accessories/caging-best-practices]] - Layered accessory caging best practices.
- [[external/roblox-creator-docs/avatar/layered-accessories/project-files]] - Layered accessory reference files.
- [[external/roblox-creator-docs/avatar/layered-accessories/specifications]] - Layered accessory specifications.
