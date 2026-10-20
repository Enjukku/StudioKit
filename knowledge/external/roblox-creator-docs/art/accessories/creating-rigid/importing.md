---
title: Use Studio's Importer
description: Use Studio's Importer to import a third-party 3D model into Studio.
tags: [roblox, documentation, external-reference, priority-reference, art, assets]
next: /art/accessories/creating-rigid/converting
prev: /art/accessories/creating-rigid/exporting
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [art/accessories/creating-rigid/importing.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/art/accessories/creating-rigid/importing.md). Published page: [https://create.roblox.com/docs/art/accessories/creating-rigid/importing](https://create.roblox.com/docs/art/accessories/creating-rigid/importing).

<video controls src="../../../assets/art/accessories/creating-rigid/Importing.mp4" width="100%"></video>

Studio's Importer provides a quick and easy way to import third-party 3D `.fbx` or `.gltf` assets into your projects. The importer provides object previews and error-checking to ensure that your asset meets Studio's general 3D requirements.

<br />

To import your asset ([downloadable reference](../../../assets/art/accessories/creating-rigid/Chest-Texturing-Complete.fbx)):

1. In the **Home** tab, click the **Import** button to open the Importer. A file browser opens.
1. Select your asset's `.fbx` file. The Importer loads a preview of the rigid accessory.
1. Select **Import**. The asset populates in your workspace as a `Class.Model` with the appropriate textures applied as a `Class.MeshPart.TextureID`.

<BaseAccordion>
<AccordionSummary>Textures didn't load correctly?</AccordionSummary>
<AccordionDetails>

If your textures didn't load correctly, you can import them manually using the [[external/roblox-creator-docs/projects/assets/manager|Asset Manager]]:

1. In the **Asset Manager**, click the **Import** button. If you are unable to access the Asset Manager, save and publish your game first.
1. Upload your image file.
1. After moderation clears your image, select the `Class.MeshPart` parented within your imported `Class.Model`.
1. In the **TextureID** property, select the value field and add the asset ID of the texture image.

</AccordionDetails>
</BaseAccordion>

<Alert severity = 'success'>
After successful import, your model object populates in your project as a `Class.Model` with the appropriate textures applied. See [[external/roblox-creator-docs/studio/importer|Importer]] for additional information on import settings and troubleshooting.
</Alert>


## Related Files

- [[external/roblox-creator-docs/art/accessories/creating-rigid/modeling-setup]] - Box modeling.
- [[external/roblox-creator-docs/art/accessories/creating-rigid/index]] - Create your first rigid accessory.
- [[external/roblox-creator-docs/art/accessories/creating-rigid/exporting]] - Export from Blender.
- [[external/roblox-creator-docs/art/accessories/creating-rigid/texturing]] - Texture painting.
- [[external/roblox-creator-docs/art/accessories/creating-rigid/publishing]] - Upload and publish.
- [[external/roblox-creator-docs/art/accessories/creating-rigid/converting]] - Use the Accessory Fitting Tool.
