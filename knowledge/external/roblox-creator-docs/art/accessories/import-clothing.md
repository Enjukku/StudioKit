---
title: Import clothing accessories
description: Use the Importer to add third-party models to Studio before using the Accessory Fitting Tool to convert the model to an Accessory.
tags: [roblox, documentation, external-reference, priority-reference, art, assets]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [art/accessories/import-clothing.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/art/accessories/import-clothing.md). Published page: [https://create.roblox.com/docs/art/accessories/import-clothing](https://create.roblox.com/docs/art/accessories/import-clothing).

> [!warning] Not in the current upstream docs
> Not published in [github.com/Roblox/creator-docs](https://github.com/Roblox/creator-docs) as of 2026-10-20 (revision `74006430`). The closest current page is [[external/roblox-creator-docs/avatar/layered-accessories/import]]. Kept locally so existing links keep working; read that page for current information.

Use the following instructions to [import](#import-3d-assets) your `.fbx` or `.gltf` third-party model into Studio and [convert](#convert-layered-accessories) the asset to a clothing `Accessory` object that you can save to use in your experience, share with others, or upload to the Marketplace.

<Alert severity ='info'>
The following asset example and instructions are part of the [[external/roblox-creator-docs/art/accessories/creating/index|Clothing accessory tutorial]] which covers the process of converting a model from Blender to publishing the asset to the Marketplace.
</Alert>

## Import 3D assets

Studio's Importer provides a quick and easy way to import third-party 3D assets into your projects. The importer provides object previews and error-checking to ensure that your asset meets Roblox's [[external/roblox-creator-docs/art/modeling/specifications|general 3D requirements]].

Keep in mind, your 3D layered accessory must also follow Roblox's [[external/roblox-creator-docs/art/accessories/clothing-specifications|clothing specifications]] to eventually use this asset as a layered `Class.Accessory`, or you may experience errors later in the workflow.

To import your asset:

1. From Studio's **File** menu, select **Importer**.
2. In the file browser, select the `.fbx` or `.gltf` file saved locally. The Importer loads a preview of the object.

   - If textures don't load for your asset, you can manually import your textures later.
   - See [[external/roblox-creator-docs/studio/importer|Importer]] for additional information on import settings and troubleshooting.

3. Select **Import**. The asset populates in your workspace as a `Class.Model` with the appropriate textures applied as a `Class.SurfaceAppearance` or `Class.MeshPart.TextureID`.

<BaseAccordion>
<AccordionSummary>Manually add textures</AccordionSummary>
<AccordionDetails>
 If textures didn't load correctly, add them manually. You may need to save and publish your experience in order to access the [[external/roblox-creator-docs/projects/assets/manager|Asset Manager]].

1.  In the **Asset Manager**, click the **Import** button.
2.  Upload your image files.
3.  After moderation clears for your image, select the `Class.MeshPart` parented within your imported `Class.Model`.
4.  If you are using a single basic texture, set the `Class.MeshPart.TextureID` property to your uploaded texture image.
5.  If you are using PBR textures:

    1. Add a `Class.SurfaceAppearance` child to your `Class.MeshPart`.

       <img src="../../assets/art/accessories/creating-rigid/Adding-Surface-Appearance.png" />

    2. In the `Class.SurfaceAppearance` properties, click each property value and assign the appropriate texture image from the asset dropdown:

       1. Set the **ColorMap** to the **\_ALB** texture image.
       2. Set the **MetalnessMap** to the **\_MTL** texture image.
       3. Set the **NormalMap** to the **\_NOR** texture image.
       4. Set the **RoughnessMap** to the **\_RGH** texture image.

       <img src="../../assets/art/accessories/creating-rigid/Surface-Appearance-Asset-Dropdown.png" />

</AccordionDetails>
</BaseAccordion>

<Alert severity = 'success'>
After successful import, your model object should populate in your project as a `Class.Model` with the appropriate textures applied. See [[external/roblox-creator-docs/studio/importer|Importer]] for additional information on import settings and troubleshooting.
</Alert>

## Convert layered accessories

With the `Class.Model` in your project, the last step in the process of clothing creation requires you to use the [[external/roblox-creator-docs/art/accessories/accessory-fitting-tool|Accessory Fitting Tool]] (AFT) to convert this object to a standard `Class.Accessory` that avatar characters can equip.

<Alert severity = 'warning'>
For shoes, you must convert the left shoe and the right shoe as separate accessories. Use the following instructions for each shoe before grouping both shoe accessories as a `Class.Model` when [[external/roblox-creator-docs/marketplace/publish-to-marketplace#upload-an-asset|saving to Roblox]].
</Alert>

To generate the accessory object:

1. In the toolbar's **Avatar** tab, click **Accessory** to open the AFT.
2. Select the `Class.Model` of the clothing item in the viewport. The tool's text field populates with the name of the object selected. Alternatively, you can select the object within the **Explorer** window.
3. Test out various sample characters, clothing, and animations. See [[external/roblox-creator-docs/art/accessories/accessory-fitting-tool#test-accessories|Test accessories]] for additional information.
   - If required, make minor cage adjustments using the editing features. Larger cage changes may require returning to your third-party modeling software and re-exporting the asset.
4. When ready to generate your accessory, click **Generate MeshPart Accessory**. The accessory object with your model populates in your workspace.

  <GridContainer numColumns="2">
  <figure>
     <img src="../../assets/art/accessories/creating/Exporting-Clothing-in-Studio-Highlight.png" />
     <figcaption>Clothing accessory in viewport</figcaption>
  </figure>
  <figure>
     <img src="../../assets/art/accessories/creating/Exporting-Accessory-Explorer.png" />
     <figcaption>Clothing accessory in Explorer</figcaption>
  </figure>
  </GridContainer>

After successful fitting and converting, your 3D model should populate in your project as an `Class.Accessory`. With this `Class.Accessory` you can perform any of the following:

- Begin the process of [[external/roblox-creator-docs/marketplace/publish-to-marketplace#upload-an-asset|uploading and publishing]] the clothing accessory to the Marketplace.

- Use the accessory in your current experience by equipping it to character models with [[external/roblox-creator-docs/characters/appearance#manually-modify-appearance|HumanoidDescription]], or by dragging and dropping the accessory under the appropriate character `Class.Model` object.

- Save the accessory to your [[external/roblox-creator-docs/projects/assets/toolbox|Toolbox]] or make it public on the [[external/roblox-creator-docs/production/creator-store|Creator Store]] to share or use within any of your experiences.


## Related Files

- [[external/roblox-creator-docs/art/index]] - 3D art in Roblox.
- [[external/roblox-creator-docs/art/accessories/from-existing]] - Accessories from an existing model.
- [[external/roblox-creator-docs/art/accessories/accessory-fitting-tool]] - Accessory Fitting Tool.
- [[external/roblox-creator-docs/art/accessories/project-files]] - Accessory project files and references.
- [[external/roblox-creator-docs/projects/assets/manager]] - Asset Manager.
- [[external/roblox-creator-docs/art/accessories/automatic-skinning-transfer]] - Automatic Skinning Transfer.
- [[external/roblox-creator-docs/art/accessories/creating/index]] - Basic clothing creation.
- [[external/roblox-creator-docs/art/accessories/body-scale]] - Body scale and proportions.
- [[external/roblox-creator-docs/art/accessories/caging-best-practices]] - Caging best practices.
- [[external/roblox-creator-docs/characters/appearance]] - Character appearance.
- [[external/roblox-creator-docs/art/accessories/clothing-specifications]] - Clothing specifications.
- [[external/roblox-creator-docs/art/accessories/validation-tool]] - Clothing Validation Tool.
- [[external/roblox-creator-docs/production/creator-store]] - Creator Store.
- [[external/roblox-creator-docs/art/modeling/specifications]] - General specifications.
- [[external/roblox-creator-docs/studio/importer]] - Importer.
- [[external/roblox-creator-docs/marketplace/publish-to-marketplace]] - Publish to Marketplace.
- [[external/roblox-creator-docs/art/accessories/index]] - Rigid accessories.
- [[external/roblox-creator-docs/projects/assets/toolbox]] - Toolbox.
