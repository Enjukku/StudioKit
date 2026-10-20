---
title: Experience Settings
description: The Experience Settings window contains Studio-level settings and customization options for an experience.
tags: [roblox, documentation, external-reference, priority-reference, studio, security, debugging]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [studio/experience-settings.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/studio/experience-settings.md). Published page: [https://create.roblox.com/docs/studio/experience-settings](https://create.roblox.com/docs/studio/experience-settings).

> [!warning] Not in the current upstream docs
> Not published in [github.com/Roblox/creator-docs](https://github.com/Roblox/creator-docs) as of 2026-10-20 (revision `74006430`). The closest current page is [[external/roblox-creator-docs/projects/configure-games]]. Kept locally so existing links keep working; read that page for current information.

The **Experience Settings** window, accessible from Studio's **File** menu, contains a wide array of Studio-level settings and customization options for Roblox experiences, including settings for [permissions](#permissions), [monetization](#monetization), [security](#security), and [localization](#localization).

<Alert severity="warning">
Many settings in this window modify underlying properties in your place file that aren’t visible in Studio or accessible with scripts. This can lead to unexpected or difficult-to-debug behavior, especially when working across teams or reverting changes. Make sure you fully understand the impact of each setting before applying changes.
</Alert>

## Basic Info

The **Basic Info** tab contains general settings for an experience, such as its name, description, and promotional images.

<table>
<thead>
  <tr>
    <th>Setting</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>**Name**</td>
    <td>The experience's title.</td>
  </tr>
  <tr>
    <td>**Description**</td>
    <td>A description of the experience that describes what a potential player should expect.</td>
  </tr>
	<tr>
    <td>**Content Maturity Label**</td>
    <td>[[external/roblox-creator-docs/production/promotion/content-maturity|Content Maturity Labels]] provide information on the experience's main page about what kind of content the experience contains.</td>
  </tr>
  <tr>
    <td>**Game Icon**</td>
    <td>Lets you upload an [[external/roblox-creator-docs/production/publishing/experience-icons|icon]] to represent your experience.</td>
  </tr>
  <tr>
    <td>**Screenshots & Videos**</td>
    <td>Lets you upload [[external/roblox-creator-docs/production/publishing/thumbnails|promotional thumbnails]]. </td>
  </tr>
  <tr>
    <td>**Playable Devices**</td>
    <td>Lets you enable each applicable device that supports your experience.</td>
  </tr>
</tbody>
</table>

## Communication

<table>
<thead>
  <tr>
    <th>Setting</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>**Enable Microphone**</td>
    <td>Enables voice-eligible users to use voice chat within your experience. See [[external/roblox-creator-docs/chat/voice-chat|Voice Chat]] for more information.</td>
  </tr>
  <tr>
    <td>**Enable Camera**</td>
    <td>Enables eligible users to animate their avatar with their camera in your experience. See [Animate Your Avatar](https://en.help.roblox.com/hc/en-us/articles/17877687557396) for more information.</td>
  </tr>
</tbody>
</table>

## Permissions

The **Permissions** tab lets you control the audience for your experience.

<table>
<thead>
  <tr>
    <th>Setting</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>**Playability**</td>
    <td>Sets which users can access the experience.</td>
  </tr>
</tbody>
</table>

## Monetization

The **Monetization** tab contains settings that let you [[external/roblox-creator-docs/production/monetization/index|monetize]] your experience.

<table>
<thead>
  <tr>
    <th>Setting</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>**Badges**</td>
    <td>Lets you create and manage all [[external/roblox-creator-docs/production/publishing/badges|badges]] for your experience.</td>
  </tr>
  <tr>
    <td>**Paid Access**</td>
    <td>Lets you enable [[external/roblox-creator-docs/production/monetization/paid-access-robux|paid access in Robux]] or [[external/roblox-creator-docs/production/monetization/paid-access-local-currency|paid access in local currency]].</td>
  </tr>
  <tr>
    <td>**Private Servers**</td>
    <td>Lets you enable [[external/roblox-creator-docs/production/monetization/private-servers|private servers]].</td>
  </tr>
  <tr>
    <td>**Developer&nbsp;Products**</td>
    <td>Lets you create and manage all [[external/roblox-creator-docs/production/monetization/developer-products|developer products]] for your experience.</td>
  </tr>
</tbody>
</table>

## Security

The **Security** tab contains settings related to network communication, sales, and teleports.

<Alert severity="warning">
You should only enable the following settings if you trust all assets from other users or groups within your experience, otherwise your experience is vulnerable to security risks.
</Alert>

<table>
<thead>
  <tr>
    <th>Setting</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>**Allow HTTP Requests**</td>
    <td>Allows experiences' servers to issue requests to remote servers via `Class.HttpService`.</td>
  </tr>
  <tr>
    <td>**Secrets**</td>
    <td>Allows for the creation and configuration of `Datatype.Secret|Secrets` for local Studio sessions using `Class.HttpService`. For more information, see [[external/roblox-creator-docs/cloud-services/secrets#local-secrets|Work with secrets]].</td>
  </tr>
  <tr>
    <td>**Enable&nbsp;Studio&nbsp;Access to API Services**</td>
    <td>Lets Studio access API services. This setting is useful for testing the implementation of services like [[external/roblox-creator-docs/cloud-services/data-stores/index|data stores]].</td>
  </tr>
  <tr>
    <td>**Allow Third Party Sales**</td>
    <td>Lets players purchase items from third parties. When this setting is disabled, all purchase prompts from assets you own will continue to work while purchase prompts from assets published by other users or groups will fail.</td>
  </tr>
  <tr>
    <td>**Allow Third Party Teleports**</td>
    <td>Lets players [[external/roblox-creator-docs/projects/teleport|teleport]] to other experiences.</td>
  </tr>
  <tr>
    <td>**Allow Mesh / Image APIs**</td>
    <td>Lets you use `Class.EditableImage` and `Class.EditableMesh` in published experiences. To enable usage, you must be 13+ age verified and ID verified.</td>
  </tr>
</tbody>
</table>

## Places

The **Places** tab contains place-specific settings.

<table>
<thead>
  <tr>
    <th>Setting</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>**Create**</td>
    <td>Lets you create a new place within your experience.</td>
  </tr>
  <tr>
    <td>**&ctdot;**</td>
    <td>Opens a pop-up menu with options to **Configure&nbsp;Place** (edit place-specific settings such as the maximum number of players), or **Version&nbsp;History** to view, download, and open any previous version of the experience.</td>
  </tr>
</tbody>
</table>

## Localization

The **Localization** tab contains language settings related to [[external/roblox-creator-docs/production/localization/index|localization]] both within the experience and in the cloud.

<table>
<thead>
  <tr>
    <th>Setting</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>**Source Language**</td>
    <td>Lets you choose the language that you used to create the experience.</td>
  </tr>
  <tr>
    <td>**Automatic Text Capture**</td>
    <td>Automatically captures text from the experience's UI while users are accessing the experience.</td>
  </tr>
  <tr>
    <td>**Use Translated Content**</td>
    <td>Enables translated content within the experience.</td>
  </tr>
  <tr>
    <td>**Automatic Translation**</td>
    <td>The languages for which you'd like to enable [[external/roblox-creator-docs/production/localization/automatic-translations|automatic translation]].</td>
  </tr>
</tbody>
</table>

## World

The **World** tab includes global settings for the experience, such as
gravity, character jump behavior, and walk speed.

<table>
<thead>
  <tr>
    <th>Setting</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>**Presets**</td>
    <td>Sets the options lower in the tab to presets for **Classic**, **Realistic**, or **Action**.</td>
  </tr>
  <tr>
    <td>**Gravity**</td>
    <td>Sets the overall world gravity in studs per second² (note the meters per second² equivalent in parentheses).</td>
  </tr>
  <tr>
    <td>**Jump**</td>
    <td>Sets either the humanoid **jump height** in studs or the **jump power** in studs per second. Note how adjusting this value changes the max jump distance in relation to the walk speed.</td>
  </tr>
  <tr>
    <td>**Walk**</td>
    <td>Sets the humanoid walk speed in studs per second. Adjusting this value changes the **max jump distance** in relation to jump height or power.</td>
  </tr>
  <tr>
    <td>**Slope**</td>
    <td>Determines the maximum slope angle that humanoids can climb. If the angle of a slope is greater than this value, the humanoids will slide down the slope.</td>
  </tr>
</tbody>
</table>

## Other

The **Other** tab includes settings that are typically reserved for special situations, such as collaborative scripting and shutting down all servers.

<table>
<thead>
  <tr>
    <th>Setting</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>**Enable Drafts Mode**</td>
    <td>Enables asynchronous, drafts-based script editing in a [[external/roblox-creator-docs/projects/collaboration|collaborative]] session.</td>
  </tr>
  <tr>
    <td>**Shutdown All Servers**</td>
    <td>Shuts down all servers currently running the experience.</td>
  </tr>
</tbody>
</table>


## Related Files

- [[external/roblox-creator-docs/studio/align-tool]] - Align tool.
- [[external/roblox-creator-docs/production/localization/automatic-translations]] - Automatic translation.
- [[external/roblox-creator-docs/studio/avatar-settings]] - Avatar Settings.
- [[external/roblox-creator-docs/production/publishing/badges]] - Badges.
- [[external/roblox-creator-docs/projects/collaboration]] - Collaboration.
- [[external/roblox-creator-docs/studio/mcp]] - Connect to the Roblox Studio MCP server.
- [[external/roblox-creator-docs/production/promotion/content-maturity]] - Content maturity and compliance.
- [[external/roblox-creator-docs/cloud-services/data-stores/index]] - Data stores.
- [[external/roblox-creator-docs/studio/debugging]] - Debugging.
- [[external/roblox-creator-docs/studio/developer-console]] - Developer Console.
- [[external/roblox-creator-docs/production/monetization/developer-products]] - Developer Products.
- [[external/roblox-creator-docs/studio/explorer]] - Explorer window.
- [[external/roblox-creator-docs/production/publishing/experience-icons]] - Icons.
- [[external/roblox-creator-docs/studio/importer]] - Importer.
- [[external/roblox-creator-docs/production/localization/index]] - Localization.
- [[external/roblox-creator-docs/studio/material-generator]] - Material Generator.
- [[external/roblox-creator-docs/production/monetization/index]] - Monetization.
- [[external/roblox-creator-docs/production/monetization/paid-access-local-currency]] - Paid access in local currency.
- [[external/roblox-creator-docs/production/monetization/paid-access-robux]] - Paid access in Robux.
- [[external/roblox-creator-docs/production/monetization/private-servers]] - Private servers.
- ...and 5 more local docs.
