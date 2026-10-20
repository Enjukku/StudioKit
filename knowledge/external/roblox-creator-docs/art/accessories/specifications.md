---
title: Rigid accessory specifications
description: Rigid accessory specifications lists the specific technical requirements for basic avatar accessories.
tags: [roblox, documentation, external-reference, priority-reference, art, assets]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [art/accessories/specifications.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/art/accessories/specifications.md). Published page: [https://create.roblox.com/docs/art/accessories/specifications](https://create.roblox.com/docs/art/accessories/specifications).

> [!warning] Not in the current upstream docs
> Not published in [github.com/Roblox/creator-docs](https://github.com/Roblox/creator-docs) as of 2026-10-20 (revision `74006430`). The closest current page is [[external/roblox-creator-docs/avatar/rigid-accessories/specifications]]. Kept locally so existing links keep working; read that page for current information.

When creating rigid accessories for Roblox, it's important to meet specific technical requirements to ensure compatibility and optimize for performance and quality. Many of these requirements must be applied when designing and modeling your asset in a third-party modeling application.

Although rigid accessories and layerable clothing accessories share many technical requirements, layerable accessories must include [[external/roblox-creator-docs/art/accessories/clothing-specifications|additional components]] to ensure the accessories deform and stretch appropriately on different body scales.

If you are intending to publish and sell these assets on the Marketplace, there are additional [[external/roblox-creator-docs/marketplace/marketplace-policy|Marketplace policy]] standards that you must follow for any accessory or clothing item.

When ready to export, see [[external/roblox-creator-docs/art/accessories/export-settings|Export requirements]] for mesh export settings for Blender and Maya.

<Alert severity = 'warning'>
<AlertTitle>If creating other types of 3D models:</AlertTitle>
<ul>
<li>For generic meshes, see [[external/roblox-creator-docs/art/modeling/specifications|general mesh specifications]] and [[external/roblox-creator-docs/art/modeling/export-requirements|general export settings]].</li> <br />
<li>For layered accessories, see [[external/roblox-creator-docs/art/accessories/clothing-specifications|layered accessory specifications]] and [[external/roblox-creator-docs/art/accessories/clothing-export-settings|layered export settings]].</li> <br />
<li>For avatar characters, see [[external/roblox-creator-docs/art/characters/specifications|avatar specifications]] and [[external/roblox-creator-docs/art/characters/export-settings|avatar export settings]].</li>
</ul>
</Alert>

## Geometry and budgets

- **Single Mesh** - Accessories must be a single mesh.
- **Budgets** - Accessories can't exceed **4k** triangles.
- **Watertight** - All geometry must be watertight without exposed holes or backfaces.
- Use **quads** whenever possible. Avoid faces with 5 or more sides.
- **Mesh Size** - Depending on the type of accessory asset, meshes must follow a standard size (in studs, centered on attachment point) depending on the [body scale](#body-scale) it is designed for.

### Body scale

Roblox supports 3 types of body scales: `Classic`, `Normal`, and `Slender`. When designing your accessory, the size of your accessory cannot exceed the following sizes based on body scale and accessory asset type. Accessory size is measured based on attachment orientation.

See [[external/roblox-creator-docs/art/accessories/body-scale|Body scale]] for more information on the different types of body proportions Roblox supports.

<Alert severity = 'info'>
You can use tools like the [[external/roblox-creator-docs/art/accessories/accessory-fitting-tool|Accessory Fitting Tool]] to help visualize and adjust the scale of your mesh on a mannequin within a visualized boundary before uploading and publishing the asset.
</Alert>

#### Classic

<table>
<thead>
  <tr>
    <th>Asset Type</th>
    <th>Width (X)</th>
    <th>Height (Y)</th>
    <th>Depth (Z)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Hat</td>
    <td>3</td>
    <td>4</td>
    <td>3</td>
  </tr>
  <tr>
    <td>Hair</td>
    <td>3</td>
    <td>5* <br /> (Not centered: 2 up, 3 down)</td>
    <td>3.5* <br /> (Not centered: 1.5 front, 2 behind)</td>
  </tr>
  <tr>
    <td>Face</td>
    <td>3</td>
    <td>2</td>
    <td>2</td>
  </tr>
  <tr>
    <td>Eyebrow and Eyelashes</td>
    <td>1.5</td>
    <td>0.5</td>
    <td>0.5</td>
  </tr>
  <tr>
    <td>Neck</td>
    <td>3</td>
    <td>3</td>
    <td>2</td>
  </tr>
  <tr>
    <td>Shoulder (attached to NeckAttachment)</td>
    <td>7</td>
    <td>3</td>
    <td>3</td>
  </tr>
  <tr>
    <td>Shoulder (other)</td>
    <td>3</td>
    <td>3</td>
    <td>3</td>
  </tr>
  <tr>
    <td>Front</td>
    <td>3</td>
    <td>3</td>
    <td>3</td>
  </tr>
  <tr>
    <td>Back</td>
    <td>10</td>
    <td>7</td>
    <td>4.5* <br /> (Not centered: 1.5 front, 3 behind)</td>
  </tr>
  <tr>
    <td>Waist</td>
    <td>4</td>
    <td>3.5* <br /> (Not centered: 1.5 up, 2 down)</td>
    <td>7</td>
  </tr>
</tbody>
</table>

#### Normal

<table>
<thead>
  <tr>
    <th>Asset Type</th>
    <th>Width (X)</th>
    <th>Height (Y)</th>
    <th>Depth (Z)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Hat</td>
    <td>1.87</td>
    <td>2.5</td>
    <td>1.87</td>
  </tr>
  <tr>
    <td>Hair</td>
    <td>1.87</td>
    <td>3.12* <br /> (Not centered: 1.25 up, 1.875 down)</td>
    <td>2.18* <br /> (Not centered: 0.9375 front, 1.25 behind)</td>
  </tr>
  <tr>
    <td>Face</td>
    <td>1.87</td>
    <td>1.25</td>
    <td>1.25</td>
  </tr>
  <tr>
    <td>Eyebrow and Eyelashes</td>
    <td>1.5</td>
    <td>0.5</td>
    <td>0.5</td>
  </tr>
  <tr>
    <td>Neck</td>
    <td>2.95</td>
    <td>3.68</td>
    <td>2.16</td>
  </tr>
  <tr>
    <td>Shoulder (attached to NeckAttachment)</td>
    <td>6.90</td>
    <td>3.68</td>
    <td>3.24</td>
  </tr>
  <tr>
    <td>Shoulder (attached to RightCollarAttachment, LeftCollarAttachment)</td>
    <td>2.95</td>
    <td>3.68</td>
    <td>3.24</td>
  </tr>
    <tr>
    <td>Shoulder (attached to RightShoulderAttachment, LeftShoulderAttachment)</td>
    <td>2.67</td>
    <td>4.40</td>
    <td>3.09</td>
  </tr>
  <tr>
    <td>Front</td>
    <td>2.95</td>
    <td>3.68</td>
    <td>3.24</td>
  </tr>
  <tr>
    <td>Back</td>
    <td>9.86</td>
    <td>8.59</td>
    <td>4.87* <br /> (Not centered: 1.623 front, 3.246 behind)</td>
  </tr>
  <tr>
    <td>Waist</td>
    <td>3.94</td>
    <td>4.29* <br /> (Not centered: 1.842 up, 2.457 down)</td>
    <td>7.57</td>
  </tr>
</tbody>
</table>

#### Slender

<table>
<thead>
  <tr>
    <th>Asset Type</th>
    <th>Width (X)</th>
    <th>Height (Y)</th>
    <th>Depth (Z)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Hat</td>
    <td>1.78</td>
    <td>2.5</td>
    <td>1.78</td>
  </tr>
  <tr>
    <td>Hair</td>
    <td>1.78</td>
    <td>3.12* <br /> (Not centered: 1.25 up, 1.875 down)</td>
    <td>2.08* <br /> (Not centered: 1.892 front, 1.189 behind)</td>
  </tr>
  <tr>
    <td>Face</td>
    <td>1.78</td>
    <td>1.25</td>
    <td>1.18</td>
  </tr>
  <tr>
    <td>Eyebrow and Eyelashes</td>
    <td>1.5</td>
    <td>0.5</td>
    <td>0.5</td>
  </tr>
  <tr>
    <td>Neck</td>
    <td>2.59</td>
    <td>3.39</td>
    <td>1.92</td>
  </tr>
  <tr>
    <td>Shoulder (attached to NeckAttachment)</td>
    <td>6.05</td>
    <td>3.39</td>
    <td>2.88</td>
  </tr>
  <tr>
    <td>Shoulder (attached to RightCollarAttachment, LeftCollarAttachment)</td>
    <td>2.59</td>
    <td>3.39</td>
    <td>2.88</td>
  </tr>
    <tr>
    <td>Shoulder (attached to RightShoulderAttachment, LeftShoulderAttachment)</td>
    <td>2.37</td>
    <td>3.96</td>
    <td>2.75</td>
  </tr>
  <tr>
    <td>Front</td>
    <td>2.59</td>
    <td>3.39</td>
    <td>2.88</td>
  </tr>
  <tr>
    <td>Back</td>
    <td>8.64</td>
    <td>7.91</td>
    <td>4.32* <br /> (Not centered: 1.443 front, 2.886 behind)</td>
  </tr>
  <tr>
    <td>Waist</td>
    <td>3.76</td>
    <td>3.29* <br /> (Not centered: 1.414 up, 1.885 down)</td>
    <td>6.73</td>
  </tr>
</tbody>
</table>

## Textures

- Textures for Marketplace assets cannot exceed 2048x2048 resolution.
- Textures created for accessories must meet Roblox's [[external/roblox-creator-docs/art/modeling/texture-specifications|texture specifications]].

## Attachment points

`Class.Attachment` objects indicate where an accessory model attaches to a point on a character body. Whether you are creating rigid or [[external/roblox-creator-docs/art/accessories/layered-clothing|layered]] accessories, Studio's [[external/roblox-creator-docs/art/accessories/accessory-fitting-tool|Accessory Fitting Tool]] (AFT) automatically adds and configures the appropriate `Class.Attachment` with the following specifications:

- **One attachment** - Each accessory, including layered clothing, require at least one attachment point to its associated body part.
- **Naming Convention** - The `Class.Attachment` name must follow a specific naming convention depending on the `Class.Accessory.AccessoryType`. The AFT generates an appropriate `Class.Attachment` name automatically.

If setting or configuring attachments manually in Studio, use the following names for your `Class.Attachment` object depending on the accessory type:

  <table>
  <thead>
    <tr>
      <th>Accessory type</th>
      <th>Attachment name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Hat</td>
      <td>`HatAttachment`</td>
    </tr>
    <tr>
      <td>Hair</td>
      <td>`HairAttachment`</td>
    </tr>
    <tr>
      <td>Back</td>
      <td>`BodyBackAttachment`</td>
    </tr>
    <tr>
      <td>Waist</td>
      <td>`WaistFrontAttachment`, `WaistCenterAttachment`, `WaistBackAttachment`</td>
    </tr>
    <tr>
      <td>Shoulder</td>
      <td>`RightShoulderAttachment`, `RightCollarAttachment`, `NeckAttachment`, `LeftCollarAttachment`, `LeftShoulderAttachment`</td>
    </tr>
    <tr>
      <td>Face, Eyelash, Eyebrow</td>
      <td>`FaceFrontAttachment`, `FaceCenterAttachment`</td>
    </tr>
    <tr>
      <td>Neck</td>
      <td>`NeckAttachment`</td>
    </tr>
    <tr>
      <td>Front</td>
      <td>`BodyFrontAttachment`</td>
    </tr>
  </tbody>
  </table>

  <Alert severity = 'warning'>
  Importing attachment objects from a third-party tool is not supported for rigid accessories, but is supported for [[external/roblox-creator-docs/art/characters/specifications#attachments|character bodies]].
  </Alert>

- **Shoulders and Collars** - Even though they are in similar locations, Shoulder and Collar attachment points interact with character rigs differently for rigid accessories.
  - Items using `RightShoulderAttachment` or `LeftShoulderAttachment` move with the character's arm.
  - Items using `RightCollarAttachment` or `LeftCollarAttachment` do not move with the character's arm.

## Layered properties

Accessories, such as clothing items, which stretch and fit around any character body type, must include additional configurations to achieve the layering effect. See [[external/roblox-creator-docs/art/accessories/clothing-specifications|Clothing specifications]] for specifications required to create layerable accessories.

## Marketplace requirements

Your items must meet the following requirements before you upload them to the Marketplace to sell:

- Ensure that your items adhere to the [[external/roblox-creator-docs/marketplace/marketplace-policy|Marketplace program guidelines]].
- Whenever applicable, ensure that your items adhere to Roblox's [[external/roblox-creator-docs/art/modeling/specifications|custom mesh specifications]].
- Object `Class.MeshPart.Material|Material` is set to `Plastic`.
- Object `Class.MeshPart.Transparency|Transparency` is set to 0.
- Object `Class.MeshPart.VertexColor|VertexColor` is the default `1, 1, 1`.
- Your `Class.Accessory` instance does not contain extraneous objects, like `Class.Script` or additional `Class.Part` instances.


## Related Files

- [[external/roblox-creator-docs/art/index]] - 3D art in Roblox.
- [[external/roblox-creator-docs/art/accessories/from-existing]] - Accessories from an existing model.
- [[external/roblox-creator-docs/art/accessories/accessory-fitting-tool]] - Accessory Fitting Tool.
- [[external/roblox-creator-docs/art/accessories/project-files]] - Accessory project files and references.
- [[external/roblox-creator-docs/art/accessories/automatic-skinning-transfer]] - Automatic Skinning Transfer.
- [[external/roblox-creator-docs/art/accessories/body-scale]] - Body scale and proportions.
- [[external/roblox-creator-docs/art/accessories/caging-best-practices]] - Caging best practices.
- [[external/roblox-creator-docs/art/characters/export-settings]] - Character body export settings.
- [[external/roblox-creator-docs/art/characters/specifications]] - Character specifications.
- [[external/roblox-creator-docs/art/accessories/clothing-specifications]] - Clothing specifications.
- [[external/roblox-creator-docs/art/accessories/validation-tool]] - Clothing Validation Tool.
- [[external/roblox-creator-docs/art/modeling/export-requirements]] - Export settings.
- [[external/roblox-creator-docs/art/modeling/specifications]] - General specifications.
- [[external/roblox-creator-docs/art/accessories/layered-clothing]] - Layered clothing.
- [[external/roblox-creator-docs/art/accessories/clothing-export-settings]] - Layered clothing export settings.
- [[external/roblox-creator-docs/marketplace/marketplace-policy]] - Marketplace policy.
- [[external/roblox-creator-docs/art/accessories/index]] - Rigid accessories.
- [[external/roblox-creator-docs/art/accessories/export-settings]] - Rigid accessory export settings.
- [[external/roblox-creator-docs/art/modeling/texture-specifications]] - Texture specifications.
