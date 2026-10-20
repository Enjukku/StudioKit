---
title: Import
description: Use the Importer to import your custom accessory into Studio.
tags: [roblox, documentation, external-reference, priority-reference, art, assets]
prev: /art/accessories/creating/exporting
next: /art/accessories/creating/converting
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [art/accessories/creating/importing.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/art/accessories/creating/importing.md). Published page: [https://create.roblox.com/docs/art/accessories/creating/importing](https://create.roblox.com/docs/art/accessories/creating/importing).

After creating your t-shirt in Blender, import the `.fbx` using Studio's Importer tool to add the t-shirt to your project as a `Class.Model`.

Use the Importer to import your `.fbx` into Studio:

1. In the **Home** tab, click the **Import** button to open the Importer. A file browser opens.
1. Select your t-shirt's `.fbx` file. The Importer loads a preview of the layered accessory.
1. Select **Import**. The asset populates in your workspace as a `Class.Model` with the appropriate textures applied as a `Class.MeshPart.TextureID`.

   <img src="../../../assets/art/accessories/creating/Exporting-Clothing-In-Studio.png" />

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


## Related Files

- [[external/roblox-creator-docs/art/accessories/creating/armature-setup]] - Armature setup.
- [[external/roblox-creator-docs/art/accessories/creating/caging-setup]] - Caging setup.
- [[external/roblox-creator-docs/art/accessories/creating/converting]] - Convert.
- [[external/roblox-creator-docs/art/accessories/creating/unwrapping]] - Create seams and unwrap.
- [[external/roblox-creator-docs/art/accessories/creating/texture-map]] - Create texture map.
- [[external/roblox-creator-docs/art/accessories/creating/index]] - Create your first layered accessory.
- [[external/roblox-creator-docs/art/accessories/creating/exporting]] - Export.
- [[external/roblox-creator-docs/art/accessories/creating/watertight]] - Make mesh watertight.
- [[external/roblox-creator-docs/art/accessories/creating/modeling-setup]] - Modeling setup.
- [[external/roblox-creator-docs/art/accessories/creating/modify-cage]] - Modify outer cage.
- [[external/roblox-creator-docs/art/accessories/creating/sculpting]] - Sculpt detail.
- [[external/roblox-creator-docs/art/accessories/creating/test-poses]] - Test poses.
- [[external/roblox-creator-docs/art/accessories/creating/texture-painting]] - Texture painting.
- [[external/roblox-creator-docs/art/accessories/creating/trimming]] - Trim clothing shape.
