---
title: Explore Studio UI
description: Explains how to navigate Studio's fundamental UI.
tags: [roblox, documentation, external-reference, priority-reference, tutorials]
next: /tutorials/curriculums/studio/next-steps
prev: /tutorials/curriculums/studio/install-studio
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [tutorials/curriculums/studio/explore-ui.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/tutorials/curriculums/studio/explore-ui.md). Published page: [https://create.roblox.com/docs/tutorials/curriculums/studio/explore-ui](https://create.roblox.com/docs/tutorials/curriculums/studio/explore-ui).

import StudioCameraControls from '../../../includes/studio/camera-controls.md'

Welcome to your first session in Roblox Studio! Before you jump in and begin building games, let's take a moment to walk through Studio's essential UI. While this overview provides a solid foundation to get started, there are many additional windows and tools that you can discover and customize in the [[external/roblox-creator-docs/studio/ui-overview|Studio interface]].

<Alert severity="info">
<AlertTitle style={{marginBottom: 8}}>Coming to Studio from another game engine?</AlertTitle>
Check out one of the following guides that explains the key differences between Studio and Unity or Unreal: [Roblox for Unity developers](../../../unity.md) or [Roblox for Unreal developers](../../../unreal.md).
</Alert>

## Mezzanine

<img src="../../../assets/tutorials/studio-lesson/Mezzanine.jpg" width="960" alt="Mezzanine indicated at the top of Studio's window." />

The **mezzanine** is the top-most section of Studio and it includes:

- [[external/roblox-creator-docs/studio/testing-modes|Playtest options]] that allow you to simulate what players see on their devices.
- Tabs like **Model**, **Avatar**, and **Script** that filter the [toolbar](#toolbar) tools for their respective tasks.
- [[external/roblox-creator-docs/projects/collaboration|Collaborator]] information for games that you work on with others.
- The [[external/roblox-creator-docs/assistant/guide|Assistant]] tool that you can use as an aid to supplement your skills and assist with development tasks.

## Toolbar

<img src="../../../assets/tutorials/studio-lesson/Toolbar.jpg" width="960" alt="Toolbar indicated below the mezzanine bar near the top of Studio's window." />

The **toolbar** is the section right below the mezzanine that displays all tools and insertable objects that relate to your active tab:

- **Home** contains the core [[external/roblox-creator-docs/parts/index#transform-parts|transform]] tools, [[external/roblox-creator-docs/parts/index#insert-parts|part inserter]], the [[external/roblox-creator-docs/parts/index#color|color]] and [[external/roblox-creator-docs/parts/index#material|material]] widgets, the [[external/roblox-creator-docs/parts/index#group|group]] and [[external/roblox-creator-docs/parts/index#lock|lock]] tools, and [[external/roblox-creator-docs/parts/index#anchor|anchor]] toggle. Also contains the [[external/roblox-creator-docs/studio/terrain-editor|Terrain Editor]].

- **Model** contains the core [[external/roblox-creator-docs/parts/index#transform-parts|transform]] tools, the [[external/roblox-creator-docs/studio/pivot-tools|pivot]] and [[external/roblox-creator-docs/studio/align-tool|align]] tools, insertion widgets for [[external/roblox-creator-docs/effects/index|effects]] and [[external/roblox-creator-docs/physics/index#constraints|constraints]], and [[external/roblox-creator-docs/parts/solid-modeling|solid‑modeling]] tools.

- **Avatar** contains the core [[external/roblox-creator-docs/parts/index#transform-parts|transform]] tools, as well as specialized tools for building default rigs, configuring [[external/roblox-creator-docs/avatar-setup/index|avatars]], working with [[external/roblox-creator-docs/animation/index|animations]], and [[external/roblox-creator-docs/avatar/accessory-fitting-tool|creating/fitting accessories]].

- **UI** contains insertion widgets for [[external/roblox-creator-docs/ui/index#ui-objects|UI objects]] and lets you access the [[external/roblox-creator-docs/ui/styling/editor|Style&nbsp;Editor]], a comprehensive tool that allows you to create, manage, and apply UI styles.

- **Script** contains tools for writing and testing scripts, including [[external/roblox-creator-docs/studio/debugging|debugging]] tools.

- **Plugins** contains [[external/roblox-creator-docs/studio/plugins|plugins]] created by the community or plugins you've created yourself to use across your games.

When you are more comfortable with Studio, you can also create [[external/roblox-creator-docs/studio/ui-overview#custom-tabs|custom tabs]] for your own development needs.

## 3D viewport

<img src="../../../assets/tutorials/studio-lesson/3D-Viewport.jpg" width="960" alt="3D viewport indicated in center of Studio's window." />

The **3D viewport** is the largest window in Studio that provides you a view into the 3D space. After you click in the 3D viewport, you can move the camera, edit objects with your mouse, and playtest the game from your players' point-of-view.

For common camera controls, see the following table.

<StudioCameraControls components={props.components} />

<Alert severity="info">
It's **strongly** recommended to use a 2-button mouse with a scroll wheel to make navigating the 3D space easier.
</Alert>

## Toolbox

<img src="../../../assets/tutorials/studio-lesson/Toolbox.jpg" width="960" alt="Toolbox shown on the left side of Studio's window." />

The [[external/roblox-creator-docs/projects/assets/toolbox|Toolbox]] contains a selection of models, images, meshes, audio, plugins, videos, and fonts from either Roblox or fellow creators on the platform. It offers four tabs:

- **Creator Store** is a marketplace of both free and for sale assets to use within your games.
- **Inventory** contains assets that you or your groups have uploaded, or those that you found on the Creator Store.
- **Recent** contains your most recently used assets.
- **Creations** is similar to **Inventory**, but it excludes assets from the Creator Store.

## Explorer

<img src="../../../assets/tutorials/studio-lesson/Explorer.jpg" width="960" alt="Explorer window shown on the right side of Studio's window." />

The [[external/roblox-creator-docs/studio/explorer|Explorer]] window displays a hierarchical list of every object and service that runs out-of-the-box gameplay logic for the active **place** of your game. You can think of places like levels inside of a game.

<Alert severity="info">
Places are comparable to scenes in Unity or maps in Unreal Engine.
</Alert>

Games can have one or multiple places that each contain all components for that portion of the game, including its specific environment, 3D objects, and scripts; these components collectively are called the **data model**. When you switch to a different place, the **Explorer** window updates accordingly to show that place's data model.

For more information on how the **Explorer** window organizes objects in the data model, see [[external/roblox-creator-docs/projects/data-model|Data model]].

## Properties

<img src="../../../assets/tutorials/studio-lesson/Properties.jpg" width="960" alt="Properties window shown on the right side of Studio's window." />

The [[external/roblox-creator-docs/studio/properties|Properties]] window displays a selection of properties for a selected object that you can customize to change how the object looks and behaves in the 3D environment. Every time you select a different object in the 3D viewport or **Explorer** window, the **Properties** window updates accordingly to show that object's properties.

Now that you're familiar with Studio's core UI and what they're responsible for, you can continue learning about how to create with Studio.


## Related Files

- [[external/roblox-creator-docs/tutorials/curriculums/studio/create-account]] - Create Roblox account.
- [[external/roblox-creator-docs/tutorials/curriculums/studio/install-studio]] - Install Roblox Studio.
- [[external/roblox-creator-docs/tutorials/curriculums/studio/index]] - Learn about Studio.
- [[external/roblox-creator-docs/tutorials/curriculums/studio/next-steps]] - Next steps.
