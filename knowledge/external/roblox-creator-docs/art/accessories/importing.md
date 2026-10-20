---
title: Import rigid accessories
description: Use the Importer to add third-party models to Studio before using the Accessory Fitting Tool to convert the model to an Accessory.
tags: [roblox, documentation, external-reference, priority-reference, art, assets]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [art/accessories/importing.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/art/accessories/importing.md). Published page: [https://create.roblox.com/docs/art/accessories/importing](https://create.roblox.com/docs/art/accessories/importing).

> [!warning] Not in the current upstream docs
> Not published in [github.com/Roblox/creator-docs](https://github.com/Roblox/creator-docs) as of 2026-10-20 (revision `74006430`). The closest current page is [[external/roblox-creator-docs/avatar/rigid-accessories/import]]. Kept locally so existing links keep working; read that page for current information.

Use the following instructions to [import](#import-3d-assets) your `.fbx` or `.gltf` third-party model into Studio and [convert](#convert-rigid-accessories) the asset to an `Accessory` object that you can save to use in your experience, share with others, or upload to the Marketplace.

<Alert severity ='info'>
The following asset example and instructions are part of the [[external/roblox-creator-docs/art/accessories/creating-rigid/index|Rigid accessory tutorial]] which covers the process of converting a model from Blender to publishing the asset to the Marketplace.
</Alert>

## Import 3D assets

Studio's Importer provides a quick and easy way to import third-party 3D assets into your projects. The importer provides object previews and error-checking to ensure that your asset meets Roblox's [[external/roblox-creator-docs/art/modeling/specifications|general 3D requirements]].

Keep in mind, the model that you intend to create as a rigid accessory must also follow Roblox's [[external/roblox-creator-docs/art/accessories/specifications|accessory specifications]] to eventually use this asset as an `Class.Accessory`, or you may experience errors later in the workflow.

To import your asset:

1. From Studio's **File** menu, select **Importer**.
2. In the file browser, select the `.fbx` or `.gltf` file saved locally. The Importer loads a preview of the object.

      <img src="../../assets/art/accessories/creating-rigid/3D-Importer.png" />

   - If textures don't load for your asset, you can manually import your textures later.
   - See [[external/roblox-creator-docs/studio/importer|Importer]] for additional information on import settings and troubleshooting.

3. Select **Import**. The asset populates in your workspace as a `Class.Model` with the appropriate textures applied as a `Class.SurfaceAppearance` or `Class.MeshPart.TextureID`.

<BaseAccordion>
<AccordionSummary>Manually add textures</AccordionSummary>
<AccordionDetails>

If textures didn't load correctly, add them manually. You may need to save and publish your experience in order to access the [[external/roblox-creator-docs/projects/assets/manager|Asset Manager]].

1. In the **Asset Manager**, click the **Import** button.
2. Upload your image files.
3. After moderation clears for your image, select the `Class.MeshPart` parented within your imported `Class.Model`.
4. Add a `Class.SurfaceAppearance` child to your `Class.MeshPart`.

   <img src="../../assets/art/accessories/creating-rigid/Adding-Surface-Appearance.png" />

5. In the `Class.SurfaceAppearance` properties, click each property value and assign the appropriate texture image from the asset dropdown:

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

## Convert rigid accessories

After importing your asset into Studio, you can begin **fitting** your imported object to a mannequin and **converting** the `Class.Model` object into a `Class.Accessory`. When fitting and converting your accessory it's important to use the [[external/roblox-creator-docs/art/accessories/accessory-fitting-tool|Accessory Fitting Tool]] (AFT) to correctly preview the placement and apply the correct configurations to your accessory.

To fit and generate your accessory:

1. In the toolbar's **Avatar** tab, click **Accessory** to open the AFT.
2. In the tool's panel, select the **Part** field and, in the workspace, select the accessory `Class.MeshPart` object in the workspace and press **Next**.

   <img src="../../assets/art/accessories/creating-rigid/AFT-Select-Mesh.png" />

3. On the Asset Type page, select the **type** of asset and the expected **body scale**. Press **Next** when complete.

   1. This example uses a **Hat** asset with an **Proportions Normal** scale.
   2. Body scale is typically set based on the original sculpting and sizing of the asset. See [[external/roblox-creator-docs/art/accessories/body-scale|Body Scale]] for additional information on rigid accessory scaling.

      <img src="../../assets/art/accessories/creating-rigid/AFT-Select-Type.png" />

4. On the preview screen, select one of the humanoid characters as a mannequin:

   1. In the Avatars section, select a humanoid base body character.
   2. In the preview panel, deselect the previous selection. Only the humanoid body displays in the preview window.

      <img src="../../assets/art/accessories/creating-rigid/AFT-Add-Avatar-Panel.png" />

5. Using both the AFT preview window and the workspace, adjust the position, scale, and rotation of the accessory.

   1. Use the AFT preview window and your mannequin as an accurate preview of how your asset fits on the character. The clothing mannequin in the workspace does not accurately portray how rigid accessories attach.
   2. In the workspace, use the **Move**, **Scale**, and **Rotate** tools to adjust the positioning of your rigid accessory.
   3. If you accidentally select something else, click back into the AFT panel to reselect the accessory and resume your adjustments using the transformation tools.

      <video controls src="../../assets/art/accessories/creating-rigid/Fitting-Mask.mp4" width="100%"></video>

6. After previewing and fitting your asset, select **Generate MeshPart Accessory** to create the Accessory and add it to your explorer.

After successful fitting and converting, your 3D model should populate in your project as an `Class.Accessory`. With this `Class.Accessory` you can perform any of the following:

- Begin the process of [[external/roblox-creator-docs/marketplace/publish-to-marketplace#upload-an-asset|uploading and publishing]] the accessory to the Marketplace.

- Use the accessory in your current experience by equipping it to character models with [[external/roblox-creator-docs/characters/appearance#manually-modify-appearance|HumanoidDescription]], or by dragging and dropping the accessory under the appropriate character `Class.Model` object.

- Save the accessory to your [[external/roblox-creator-docs/projects/assets/toolbox|Toolbox]] or make it public on the [[external/roblox-creator-docs/production/creator-store|Creator Store]] to share or use within any of your experiences.


## Related Files

- [[external/roblox-creator-docs/art/index]] - 3D art in Roblox.
- [[external/roblox-creator-docs/art/accessories/from-existing]] - Accessories from an existing model.
- [[external/roblox-creator-docs/art/accessories/accessory-fitting-tool]] - Accessory Fitting Tool.
- [[external/roblox-creator-docs/art/accessories/project-files]] - Accessory project files and references.
- [[external/roblox-creator-docs/projects/assets/manager]] - Asset Manager.
- [[external/roblox-creator-docs/art/accessories/automatic-skinning-transfer]] - Automatic Skinning Transfer.
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
- [[external/roblox-creator-docs/art/accessories/creating-rigid/index]] - Rigid accessory creation.
- [[external/roblox-creator-docs/art/accessories/specifications]] - Rigid accessory specifications.
- [[external/roblox-creator-docs/projects/assets/toolbox]] - Toolbox.
