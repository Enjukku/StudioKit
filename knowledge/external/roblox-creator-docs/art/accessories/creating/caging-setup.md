---
title: Caging setup
description: Isolate your outer cage meshes and hide extra objects before modifying your clothing cage.
tags: [roblox, documentation, external-reference, priority-reference, art, assets]
next: /art/accessories/creating/modify-cage
prev: /art/accessories/creating/test-poses
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [art/accessories/creating/caging-setup.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/art/accessories/creating/caging-setup.md). Published page: [https://create.roblox.com/docs/art/accessories/creating/caging-setup](https://create.roblox.com/docs/art/accessories/creating/caging-setup).

**Caging** is the process of setting the clothing's interior and exterior surfaces, referred to as the inner and outer cages respectively. This enables your clothing to layer over existing clothing and character bodies, and additional clothes to layer on top.

Since the t-shirt in this tutorial was created using the cage templates as a mannequin, there is no need to adjust the inner cage where your clothing asset already fits over. **Only the outer cage needs to be adjusted** to fit over the new clothing item.

<GridContainer numColumns="2">
  <figure>
    <img src="../../../assets/art/accessories/creating/Texturing-Complete.png" />
    <figcaption>Clothing and cage meshes before caging</figcaption>
  </figure>
  <figure>
    <img src="../../../assets/art/accessories/creating/Caging-Complete.png" />
    <figcaption>Outer cage mesh after caging process</figcaption>
  </figure>
</GridContainer>

The next two caging sections cover the following processes:

1. Setting up your project by isolating the outer cage and the t-shirt mesh in your project.
1. Modifying the outer cage to wrap over the clothing mesh using sculpting tools.

To set up your project:

1. Switch to **Object** mode.
1. In the Outliner:
   1. Hide the armature.
   1. Unhide **LongSleeve_OuterCage**.
   1. Set **LongSleeve** to unselectable to prevent accidental edits to the t-shirt mesh.
   <img src="../../../assets/art/accessories/creating/Caging-Outliner-Setup.png" />

1. With **LongSleeve_OuterCage** active, navigate to the **Object Properties** tab in the Properties Editor, then enable **Wireframe**. This helps easily visualize and access the mesh.

   <img src="../../../assets/art/accessories/creating/Caging-Outer-Cage-Properties.png" />

<video controls src="../../../assets/art/accessories/creating/Caging_01.mp4" width="100%"></video>


## Related Files

- [[external/roblox-creator-docs/art/accessories/creating/armature-setup]] - Armature setup.
- [[external/roblox-creator-docs/art/accessories/creating/converting]] - Convert.
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
