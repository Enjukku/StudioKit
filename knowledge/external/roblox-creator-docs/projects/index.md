---
title: Projects
description: An overview of projects and games in Roblox.
tags: [roblox, documentation, external-reference, priority-reference, projects, index]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [projects/index.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/projects/index.md). Published page: [https://create.roblox.com/docs/projects](https://create.roblox.com/docs/projects).

A Roblox project is a collection of [places](#places), [assets](#assets), [settings](#settings), and other resources that together represent a **game**. Roblox stores your projects in the cloud for convenient collaboration, editing, and version control. You create and manage projects with [[external/roblox-creator-docs/studio/index|Roblox Studio]], an all‑in‑one IDE that provides building, scripting, testing, and publishing tools.

## Places

Games on Roblox are made up of individual **places**, comparable to scenes in Unity or maps in Unreal Engine. Each place contains all components for that portion of the game, including its specific environment, parts, meshes, scripts, and user interface.

See the pages for [[external/roblox-creator-docs/production/publishing/publish-games-and-places|creating and publishing]], [[external/roblox-creator-docs/projects/configure-games|configuring]], and [[external/roblox-creator-docs/projects/update-games|updating]] games and places for details.

<figure>
<img src="../assets/publishing/experiences-places-assets/Experience-Hierarchy.png" alt="A game grouping of three individual places with unique environments." width="800" />
</figure>

Every place is represented by a **data model**, a hierarchy of objects that describe everything about the place. The Roblox Engine uses the data model as a source of truth for a place's state, so it can simulate and render it on client devices. For more information on how the engine interprets the data model, see [[external/roblox-creator-docs/projects/client-server|Client-server runtime]].

Proper, intentional object organization within the data model is essential for
functionality and maintenance of your project. For more information on what
objects are available and how to organize and use them, see
[[external/roblox-creator-docs/projects/data-model|Data model]].

## Assets

In Roblox, assets such as images, meshes, and audio are stored as **cloud-based assets**, so you don't need to bundle local copies into a saved Studio game. Each asset in the cloud is assigned a unique **asset&nbsp;ID** from which multiple games can utilize them. You can create assets directly in Studio, such as models, or import assets like images, audio, and meshes from other tools.

<GridContainer numColumns="3">
  <figure>
    `rbxassetid://7229442422`
		<img src="../assets/modeling/textures-decals/Texture-Example-Grafitti04.png" alt="A decal asset of a young woman with a button for an eye." width="90%" />
  </figure>
  <figure>
    `rbxassetid://6768917255`
		<img src="../assets/modeling/meshes/Base-Mesh-In-Marketplace.png" alt="An untextured treasure chest MeshPart asset." width="90%" />
  </figure>
	<figure>
    `rbxassetid://9125402735`
		<audio controls><source src="../assets/studio/general/Boom-Impact.mp3" type="audio/mpeg"></source></audio>
  </figure>
</GridContainer>

By default, assets are private to your game and you can use an asset in any place by referencing its ID. You can also distribute them to the community in the [Creator Store](https://create.roblox.com/store/), so others can use them as well.

For more information on how to import and publish assets, see [[external/roblox-creator-docs/projects/assets/index|Assets]].

## Packages

[[external/roblox-creator-docs/projects/assets/packages|Packages]] are reusable object hierarchies that you can define and reuse in multiple places across multiple games. For any large project, packages offer the following benefits:

- Packages can be used as asset kits, allowing you to duplicate a set of objects as needed.
- Packages make it easier to update assets. For instance, a package can include a tree that's duplicated many times in an environment. If you need to make a change, such as swap textures for the tree, it can be updated once in the package instead of for each individual instance.
- A package can start with graybox assets, and eventually be replaced with final art assets. When assets are replaced, they retain all original positions and orientations.

## Settings

Game settings are managed from the [Creator Dashboard](https://create.roblox.com/dashboard/creations) or within Studio, including:

- **Basic Info** &mdash; Basic information about the game, such as its name, description, and genre. Much of the information here is used in your game's listing.
- **Communication** &mdash; Settings which enable eligible users to use [[external/roblox-creator-docs/chat/voice-chat|voice chat]] or animate their avatar via their camera within your game.
- **Permissions** &mdash; Configures who can access your game. When games are first published, they are only accessible to you as the creator, users with **Edit** or **Playtest** access, and group members with the appropriate [[external/roblox-creator-docs/projects/groups#roles-and-permissions|roles and permissions]]. When you're ready, you can [[external/roblox-creator-docs/production/publishing/publish-games-and-places#release-games|release]] the game to a wider audience.
- **Monetization** &mdash; Options for earning revenue from your game, as outlined in [[external/roblox-creator-docs/production/monetization/index|Monetization]].
- **Localization** &mdash; Configuration for different [[external/roblox-creator-docs/production/localization/index|languages and regions]].
- **Avatar** &mdash; Settings related to avatars, such as avatar scaling and
  clothing overrides.

## Collaboration

With Studio's **built-in collaboration tools**, team members can contribute to
games independently on their own time, or alongside others. Key features
include:

- Group admins can manage which members have access to collaborate and which do
  not, effectively maintaining proper roles within a large team.
- Collaborators can build alongside other team members in real time and
  automatically see changes made by others.
- Collaborators can independently edit the same scripts that others may be
  editing, test locally, and commit their changes to the cloud-based project
  when ready.

For more information, see [[external/roblox-creator-docs/projects/collaboration|Collaboration]].

## Testing

Your [[external/roblox-creator-docs/projects/groups|team]] can instantly test a game on PC, mobile, VR, and other devices you wish to support through the Roblox app; no need to compile builds, deploy to app stores, or await app store approval.

Studio offers a suite of options for testing a game before releasing it to the public:

- **Rapid playtesting** that provides a close simulation of the game
  running on the Roblox application.
- **Multi-client simulation** for comparing how each client "sees" other clients
  within the game.
- **Device emulation** that provides insight on how controls operate on a mobile
  device or how on-screen UI displays on different screens and aspect ratios.
- **Collaborative playtesting** with members of your team.

For more information on each testing option, see [[external/roblox-creator-docs/studio/testing-modes|Studio testing modes]].


## Related Files

- [[external/roblox-creator-docs/projects/activity-history]] - Activity History.
- [[external/roblox-creator-docs/projects/client-server]] - Client-server runtime.
- [[external/roblox-creator-docs/projects/collaboration]] - Collaboration.
- [[external/roblox-creator-docs/projects/configure-games]] - Configure games and places.
- [[external/roblox-creator-docs/projects/cross-platform]] - Cross-platform development.
- [[external/roblox-creator-docs/projects/data-model]] - Data model.
- [[external/roblox-creator-docs/projects/game-ownership-transfer]] - Game ownership transfer.
- [[external/roblox-creator-docs/projects/group-guidelines]] - Group guidelines.
- [[external/roblox-creator-docs/projects/groups]] - Groups (teams).
- [[external/roblox-creator-docs/projects/place-files]] - Place files.
- [[external/roblox-creator-docs/projects/update-games]] - Release game updates.
- [[external/roblox-creator-docs/projects/teleport]] - Teleport between places.
- [[external/roblox-creator-docs/projects/external-tools]] - Third-party tools.
- [[external/roblox-creator-docs/projects/version-history]] - Version History.
