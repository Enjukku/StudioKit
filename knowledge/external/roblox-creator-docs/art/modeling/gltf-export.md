---
title: 3D Export
description: Importer imports third-party .fbx, .gltf, and .obj 3D model assets into Studio.
tags: [roblox, documentation, external-reference, priority-reference, art, assets]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [art/modeling/gltf-export.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/art/modeling/gltf-export.md). Published page: [https://create.roblox.com/docs/art/modeling/gltf-export](https://create.roblox.com/docs/art/modeling/gltf-export).

import BetaAlert from '../../includes/beta-features/beta-alert.md'

<BetaAlert betaName="glTF Export" leadIn="This feature is currently in beta. Enable it through " leadOut="." components={props.components} />

You can export your 3D Roblox assets as a **.glTF** ([GL Transmission Format](https://en.wikipedia.org/wiki/GlTF)) file format. This open standard format allows for efficient transfer of 3D assets and associated data between Studio and other software, such as Blender or Maya.

<br />
Some common use cases for .glTF export includes:

- Running [[external/roblox-creator-docs/avatar-setup/index#auto-setup|Avatar auto setup]], exporting the output and finalizing the meshes, cages, or rigging in a third-party tool.
- Exporting your entire place for high-fidelity scene renders in another 3D application.
- Creating 3D content in Studio, such as part-based models or editable meshes and making modifications in an external application.

Keep in mind that glTF supports specific 3D [components](#supported-components), has some [limitations](#limitations), and requires correct [permissions](#limitations) to export assets from Studio. Some of these specifications may change over the course of the beta.

## Supported components

glTF export supports the following types of 3D data:

- Meshes
- Textures
- Rigging and skinning data
- Vertex colors
- Cages
- Dynamic head FACS data.

## Limitations

<Alert severity = 'warning'>
See the beta announcement for the latest information on limitations and currently known bugs.
</Alert>

At this time, glTF has the following limitations:

- Does not support animation data.
- Inconsistent support for layered accessories — clothing accessories may not always position correctly and won't deform to avatar bodies outside of Roblox.

## Permissions

<Alert severity = 'warning'>
See the beta announcement for the latest information on permissions and upcoming changes.
</Alert>

You must have the correct permissions to export assets as .glTF. When exporting .glTF, Studio verifies that you have permissions to export that asset and may warn you if there are any conflicts.

<br />
You can export the following assets:

- Assets directly uploaded to your account
- Assets directly uploaded to one of your group accounts
- Mesh and image assets that have been explicitly shared with you or your group

You cannot export the following assets:

- Avatar Marketplace assets
- Acquired Creator Store assets
- Shared collaborator assets where the underlying meshes/images have not been explicitly shared
- Other `Open Use` (public) assets that have not been explicitly shared with you or your group

## How to use .glTF export

<BetaAlert betaName="glTF Export" leadIn="This feature is currently in beta. Enable it through " leadOut="." components={props.components} />

You can export selected items from the Explorer, or export the entire place.

<br />
To export from the Explorer:

1. Select the items you intend to export.
2. Right-click and navigate to **Save / Export** > **Export as glTF**.
3. Follow the prompts on screen to fine-tune your export components. Click **Export** when ready.
   1. After clicking Export, Studio runs a permission check. If there are any permission conflicts, a permission prompt appears with additional details.
4. In the file browser, select a location to save the .glTF file.

To export an entire place:

1. Navigate to **File** > **Export as glTF**.
2. Follow the prompts on screen to fine-tune your export components. Click **Export** when ready.
   1. After clicking Export, Studio runs a permission check. If there are any permission conflicts, a permission prompt appears with additional details.
3. In the file browser, select a location to save the .glTF file.


## Related Files

- [[external/roblox-creator-docs/art/modeling/assign-textures]] - Blender and Maya texture settings.
- [[external/roblox-creator-docs/art/modeling/calisthenics-tool]] - Calisthenics Tool.
- [[external/roblox-creator-docs/art/modeling/index]] - Custom 3D assets.
- [[external/roblox-creator-docs/art/modeling/export-requirements]] - Export settings.
- [[external/roblox-creator-docs/art/modeling/specifications]] - General specifications.
- [[external/roblox-creator-docs/art/modeling/material-reference]] - Material references.
- [[external/roblox-creator-docs/art/modeling/project-files]] - Modeling project files and references.
- [[external/roblox-creator-docs/art/modeling/surface-appearance]] - PBR textures.
- [[external/roblox-creator-docs/art/modeling/reimport]] - Reimport.
- [[external/roblox-creator-docs/art/modeling/rig-a-humanoid-model]] - Rig a humanoid model.
- [[external/roblox-creator-docs/art/modeling/rig-a-simple-mesh]] - Rig a simple mesh.
- [[external/roblox-creator-docs/art/modeling/rigging]] - Rigging and skinning.
- [[external/roblox-creator-docs/art/modeling/roblox-blender-plugin]] - Roblox Blender plugin.
- [[external/roblox-creator-docs/art/modeling/skin-a-humanoid-model]] - Skin a humanoid model.
- [[external/roblox-creator-docs/art/modeling/skin-a-simple-mesh]] - Skin a simple mesh.
- [[external/roblox-creator-docs/art/modeling/texture-specifications]] - Texture specifications.
