---
title: Body scale and proportions
description: Avatars come in 3 different standard sizes, Classic, Rthro, Rthro Slender.
tags: [roblox, documentation, external-reference, priority-reference, art, assets]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [art/accessories/body-scale.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/art/accessories/body-scale.md). Published page: [https://create.roblox.com/docs/art/accessories/body-scale](https://create.roblox.com/docs/art/accessories/body-scale).

> [!warning] Not in the current upstream docs
> Not published in [github.com/Roblox/creator-docs](https://github.com/Roblox/creator-docs) as of 2026-10-20 (revision `74006430`). The closest current page is [[external/roblox-creator-docs/avatar/character-bodies/specifications]]. Kept locally so existing links keep working; read that page for current information.

Roblox supports three common avatar sizes, known as **Classic**, **Rthro**, and **Rthro Slender**. This standard sizing helps keep avatar characters consistent, allowing developers to create experiences and environments that can fit commonly sized character models.

When modeling rigid accessories, like a helmet that contours around a character's head, it's important to use a mannequin to help ensure your proportions fit. The asset provided in this tutorial example was originally modeled using **Rthro** proportions. Layered clothing, such as clothing, don't require body scale specification, since layered assets automatically stretch and deform over any body scale.

If you are modeling your asset, visit the [[external/roblox-creator-docs/avatar/resources#references|references resources]] to download any of the following mesh mannequin:

<GridContainer numColumns="3">
<figure>
    <img src="../../assets/art/resources/Body-Scale-Classic.png" />
<figcaption>
Classic blocky body scale. <br /><br /> Roughly 4.75 studs tall.
</figcaption>
</figure>
<figure>
    <img src="../../assets/art/resources/Body-Scale-Rthro-Normal.png" />
<figcaption>
Normal body scale. <br /><br /> Roughly 5.75-6.5 studs tall, with wider shoulders and narrower hips.
</figcaption>
</figure>
<figure>
    <img src="../../assets/art/resources/Body-Scale-Rthro-Slender.png" />
<figcaption>
Slender body scale. <br /><br /> Roughly 5.25-6.25 studs tall, with narrower shoulders and wider hips.
</figcaption>
</figure>
</GridContainer>

See the [[external/roblox-creator-docs/art/accessories/specifications#body-scale|accessory apecifications]] and the [[external/roblox-creator-docs/art/characters/specifications#body-scale|body specifications]] for specific range values and other geometry requirements.

## AvatarPartScaleType

Roblox represents body scale in the engine by an `AvatarPartScaleType` `Class.StringValue` object within each avatar character part and associated accessory. In most cases, asset creators do not need to directly access or modify this value object since tools, such as the [[external/roblox-creator-docs/art/accessories/accessory-fitting-tool|Accessory Fitting Tool]], automatically generate the appropriate value object on accessory creation.

In cases where you may need to identify the current body scale of a body part or accessory, the following table defines the `AvatarPartScaleType` value for each type of body size. When importing your model, use the Importer's [[external/roblox-creator-docs/studio/importer|Rig Scale]] to automatically apply a scale to your custom asset.

<table>
<thead>
  <tr>
    <th>Body Scale</th>
    <th>AvatarPartScaleType value</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Classic</td>
    <td>`Classic`</td>
  </tr>
  <tr>
    <td>Normal</td>
    <td>`ProportionsNormal`</td>
  </tr>
  <tr>
    <td>Slender</td>
    <td>`ProportionsSlender`</td>
  </tr>
</tbody>
</table>


## Related Files

- [[external/roblox-creator-docs/art/index]] - 3D art in Roblox.
- [[external/roblox-creator-docs/art/accessories/from-existing]] - Accessories from an existing model.
- [[external/roblox-creator-docs/art/accessories/accessory-fitting-tool]] - Accessory Fitting Tool.
- [[external/roblox-creator-docs/art/accessories/project-files]] - Accessory project files and references.
- [[external/roblox-creator-docs/art/accessories/automatic-skinning-transfer]] - Automatic Skinning Transfer.
- [[external/roblox-creator-docs/art/accessories/caging-best-practices]] - Caging best practices.
- [[external/roblox-creator-docs/art/characters/specifications]] - Character specifications.
- [[external/roblox-creator-docs/art/accessories/clothing-specifications]] - Clothing specifications.
- [[external/roblox-creator-docs/art/accessories/validation-tool]] - Clothing Validation Tool.
- [[external/roblox-creator-docs/art/accessories/import-clothing]] - Import clothing accessories.
- [[external/roblox-creator-docs/studio/importer]] - Importer.
- [[external/roblox-creator-docs/avatar/resources]] - Resources.
- [[external/roblox-creator-docs/art/accessories/index]] - Rigid accessories.
- [[external/roblox-creator-docs/art/accessories/specifications]] - Rigid accessory specifications.
