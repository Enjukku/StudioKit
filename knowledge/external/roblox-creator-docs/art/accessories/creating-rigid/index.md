---
title: Create your first rigid accessory
description: This tutorial covers the basic steps required to publish a custom asset on the Marketplace.
tags: [roblox, documentation, external-reference, priority-reference, art, assets, index]
next: /art/accessories/creating-rigid/modeling-setup
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [art/accessories/creating-rigid/index.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/art/accessories/creating-rigid/index.md). Published page: [https://create.roblox.com/docs/art/accessories/creating-rigid](https://create.roblox.com/docs/art/accessories/creating-rigid).

<iframe width="800" height="450" src="https://www.youtube-nocookie.com/embed/Eed29gV0hLA" title="YouTube video player" frameborder="0" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen></iframe>

**Rigid accessories** are 3D objects that attach to attachment points around an avatar character's body. When users purchase rigid accessories on the [Marketplace](https://www.roblox.com/catalog), such as props, weapons, and hats, they can adjust the position and rotation of the item away from the attachment point according to their avatar's body type.

This tutorial covers the basics of how to create a simple 3D model in Blender, import it into Studio, then convert it into a Marketplace-ready `Class.Accessory` object that you can sell, save to your toolbox, or use within your games as a rigid accessory.

<Alert severity = 'warning'>
Creating, building, and sharing on Roblox is free. However, the last step of listing your item on the Marketplace requires a Roblox Plus or Premium account, an upload fee, and a publishing advance. For more information, see [[external/roblox-creator-docs/marketplace/marketplace-policy#creator-requirements|Marketplace policies]].
</Alert>

<GridContainer numColumns="2">
<figure>
    <img src="../../../assets/art/accessories/creating-rigid/Chest-Blender.png" />
<figcaption>
  3D mesh object created in Blender
</figcaption>
</figure>
<figure>
    <img src="../../../assets/art/accessories/creating-rigid/Chest-Studio.png" />
<figcaption>
  Mesh object equipped as an `Class.Accessory` in Studio
</figcaption>
</figure>
</GridContainer>

<Alert severity = 'info'>
While this content covers the Blender workflow with a provided reference example, you can apply the same concepts to other third-party modeling applications and custom assets.
</Alert>


## Related Files

- [[external/roblox-creator-docs/art/accessories/creating-rigid/modeling-setup]] - Box modeling.
- [[external/roblox-creator-docs/art/accessories/creating-rigid/exporting]] - Export from Blender.
- [[external/roblox-creator-docs/art/accessories/creating-rigid/texturing]] - Texture painting.
- [[external/roblox-creator-docs/art/accessories/creating-rigid/publishing]] - Upload and publish.
- [[external/roblox-creator-docs/art/accessories/creating-rigid/importing]] - Use Studio's Importer.
- [[external/roblox-creator-docs/art/accessories/creating-rigid/converting]] - Use the Accessory Fitting Tool.
