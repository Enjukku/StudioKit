---
title: Manual translations
description: Learn how to manually add, edit, and remove entries to your game's cloud localization table.
tags: [roblox, documentation, external-reference, priority-reference, production]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [production/localization/manual-translations.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/localization/manual-translations.md). Published page: [https://create.roblox.com/docs/production/localization/manual-translations](https://create.roblox.com/docs/production/localization/manual-translations).

When localizing your content, you might need to manually modify your localization table to improve translation quality, add context for when a translation should be used, or even remove unused translation entries.

Whether you have translation entries automatically captured or manually added, all the translation entries are saved to the [cloud localization table](#cloud-localization-table). To modify the localization table, you can perform the following actions:

- [[external/roblox-creator-docs/production/localization/add-source-content|Add source content]] to the table, either manually or automatically.
- [[external/roblox-creator-docs/production/localization/remove-content|Remove content]] from the table, such as usernames or other strings that shouldn't be translated.
- [[external/roblox-creator-docs/production/localization/add-translations|Add translations]] to entries in the table for any supported languages set in your game.

Before making any changes to your table, it's important to understand each field in the [cloud localization table](#cloud-localization-table) to prevent issues or conflicts.

<Alert severity = 'info'>
Users with Automatic Translations enabled in their Roblox account settings will still see all manually added translations in your game. See [[external/roblox-creator-docs/production/localization/index#user-facing-setting|User-facing setting]] for more information.
</Alert>

## Cloud localization table

The localization table is the reference for all translations within your game. It's important to understand each field of the localization table to effectively add or modify entries.

When populated, the table contains all user-facing content within your game that requires translation along with any available translations for specific languages. You can [[external/roblox-creator-docs/production/localization/add-source-content|add source content]] and [[external/roblox-creator-docs/production/localization/add-translations|add translations]] to the Cloud Localization Table or [[external/roblox-creator-docs/production/localization/add-translations#with-file-upload|download and upload a `.csv` version of your table]]. Only users who have edit permission for a game can access a game's localization table.

The localization table has the following columns:

<table>
<thead>
  <tr>
    <th>Column</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Source</td>
    <td>A required field containing the in-game source text strings gathered by automatic text capture or manual entry. This is the source text that you intend to translate to other languages. Source text is required before you can add a translation and multiple entries can share the same Source, as long as they have unique **Context** fields. <br /> <br />If you are translating dynamic content, such as partial strings, the Source field must follow one of the supported parameter formats described in [[external/roblox-creator-docs/production/localization/translate-dynamic-content|Translate dynamic content]]. </td>
  </tr>
  <tr>
    <td>Context</td>
    <td>
    An optional field containing a reference to the in-game object containing the source text. You can use the Context field to specify which translation Roblox displays on an object. See <a href="../../production/localization/localize-with-scripting.md#use-context-overrides">Using Context Overrides</a> for more details. <br /> <br /> The Automatic Text Capture system does not auto-fill the Context field and instead populates the **Location** field with similar information.
    </td>
  </tr>
  <tr>
    <td>Example</td>
    <td>An optional field containing any additional information about an entry you may want to include as notes for translators. You can use this field to show manual translators where and when your game uses a specific translation.</td>
  </tr>
  <tr>
    <td>Key</td>
    <td>
    An optional field for implementing `Class.Translator:FormatByKey()|key-based lookup` when using localization APIs. You can leave this field empty if you are not using <a href="./localize-with-scripting.md">localization APIs</a> for specific tasks, such as localizing images and sounds.
    </td>
  </tr>
  <tr>
    <td>Location</td>
    <td>
    A field that is auto-filled by the [Automatic Text Capture](#automatic-text-capture) system. It contains a reference to the in-game object containing the source text which can help you or a translator identify where the string is being encountered in your game. This field is either blank or populated by the Automatic Text Capture System. To manually add your own object reference, use the **Context** field.
    </td>
  </tr>
</tbody>
</table>

<Alert severity="warning">
Some fields in the localization table must be unique to avoid unexpected behavior. Keep in mind the following:

- For all entries, the **Source** field must not be empty.
- No two entries can share the same **Source and Context** values.
- No two entries can share the same **Key**.

</Alert>


## Related Files

- [[external/roblox-creator-docs/production/localization/add-source-content]] - Add source content.
- [[external/roblox-creator-docs/production/localization/add-translations]] - Add translations.
- [[external/roblox-creator-docs/production/localization/automatic-translations]] - Automatic translation.
- [[external/roblox-creator-docs/production/localization/auto-translate-dynamic-content]] - Automatically translate dynamic content.
- [[external/roblox-creator-docs/production/localization/language-codes]] - Language codes.
- [[external/roblox-creator-docs/production/localization/index]] - Localization.
- [[external/roblox-creator-docs/production/localization/localize-with-scripting]] - Localize with scripting.
- [[external/roblox-creator-docs/production/localization/remove-content]] - Remove content.
- [[external/roblox-creator-docs/production/localization/translate-dynamic-content]] - Translate dynamic content.
- [[external/roblox-creator-docs/production/localization/work-with-translators]] - Work with translators.
