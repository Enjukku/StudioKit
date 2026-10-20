---
title: Create your first layered accessory
description: This tutorial covers the basic steps required in Blender to create Studio-ready layered accessory assets from scratch.
tags: [roblox, documentation, external-reference, priority-reference, art, assets, index]
next: /art/accessories/creating/modeling-setup
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [art/accessories/creating/index.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/art/accessories/creating/index.md). Published page: [https://create.roblox.com/docs/art/accessories/creating](https://create.roblox.com/docs/art/accessories/creating).

<iframe width="800" height="450" src="https://www.youtube-nocookie.com/embed/C-DwGRBHvmE" title="YouTube video player" frameborder="0" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen></iframe>

**Layered accessories**, often referred to as **layered clothing**, are 3D objects that stretch and fit on an avatar character's body according to their rigging armature and cage meshes. When users purchase layered accessories on the [Marketplace](https://www.roblox.com/catalog), such as jackets, dresses, and cardigans, they expect it to move with the character's animations and layer appropriately on top of existing clothing the character is wearing.

This tutorial covers the basics of how to create a simple 3D model t-shirt in Blender using downloadable project templates with all [[external/roblox-creator-docs/avatar/layered-accessories/index#layered-accessory-components|components required for layered accessories]], import it into Studio, then convert it into a Marketplace-ready `Class.Accessory` object that you can sell, save to your toolbox, or use within your games as a layered accessory.

<Alert severity = 'warning'>
Creating, building, and sharing on Roblox is free. However, the last step of listing your item on the Marketplace requires a Roblox Plus or Premium account, an upload fee, and a publishing advance. For more information, see [[external/roblox-creator-docs/marketplace/marketplace-policy#creator-requirements|Marketplace policies]].
</Alert>

<GridContainer numColumns="2">
  <figure>
    <img src="../../../assets/art/accessories/creating/Modeling-Mannequin-Start.png" />
    <figcaption>Provided Blender mannequin template</figcaption>
  </figure>
  <figure>
    <img src="../../../assets/art/accessories/creating/Example-Product.png" />
    <figcaption>Final Studio-ready clothing asset</figcaption>
  </figure>
</GridContainer>

This tutorial is intended for creators with moderate Blender experience and uses the following processes to create a clothing item:

1. Modeling basic clothing using an existing mannequin shape.
2. Texturing your mesh to change its surface appearance and color.
3. Caging your clothing mesh using Roblox's template cages.
4. Rigging your clothing mesh using Roblox's armature templates.
5. Exporting your asset from Blender.
6. Importing and converting the model to an accessory in Studio.

<Alert severity ='info'>
While this content and the provided examples cover the Blender workflow and tools, you can apply the same concepts to other third-party modeling applications.
</Alert>


## Related Files

- [[external/roblox-creator-docs/art/accessories/creating/armature-setup]] - Armature setup.
- [[external/roblox-creator-docs/art/accessories/creating/caging-setup]] - Caging setup.
- [[external/roblox-creator-docs/art/accessories/creating/converting]] - Convert.
- [[external/roblox-creator-docs/art/accessories/creating/unwrapping]] - Create seams and unwrap.
- [[external/roblox-creator-docs/art/accessories/creating/texture-map]] - Create texture map.
- [[external/roblox-creator-docs/art/accessories/creating/exporting]] - Export.
- [[external/roblox-creator-docs/art/accessories/creating/importing]] - Import.
- [[external/roblox-creator-docs/art/accessories/creating/watertight]] - Make mesh watertight.
- [[external/roblox-creator-docs/art/accessories/creating/modeling-setup]] - Modeling setup.
- [[external/roblox-creator-docs/art/accessories/creating/modify-cage]] - Modify outer cage.
- [[external/roblox-creator-docs/art/accessories/creating/sculpting]] - Sculpt detail.
- [[external/roblox-creator-docs/art/accessories/creating/test-poses]] - Test poses.
- [[external/roblox-creator-docs/art/accessories/creating/texture-painting]] - Texture painting.
- [[external/roblox-creator-docs/art/accessories/creating/trimming]] - Trim clothing shape.
