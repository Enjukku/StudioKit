---
title: Add source content
description: Learn how to manually add, edit, and remove entries to your game's cloud localization table.
tags: [roblox, documentation, external-reference, priority-reference, production]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [production/localization/add-source-content.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/localization/add-source-content.md). Published page: [https://create.roblox.com/docs/production/localization/add-source-content](https://create.roblox.com/docs/production/localization/add-source-content).

You must add source text to translate to the game's localization table before you or any collaborators add translations. You can use [Automatic Text Capture](#automatic-text-capture) to collect text strings automatically as your game is played by users or [manually add text sources](#manually-add-source-content).

See [[external/roblox-creator-docs/production/localization/localize-with-scripting#localize-images-and-sounds|Localizing images and sounds]] for instructions on localizing non-text content.

## Automatic Text Capture

The **Automatic Text Capture (ATC)** tool collects text strings that users encounter in your game through GUI objects, such as `Class.TextLabel|TextLabels` or `Class.BillboardGui` and is usually the fastest way to collect translatable text from your game. In many cases, the Automatic Text Capture tool is already enabled for [[external/roblox-creator-docs/production/localization/automatic-translations#enable-automatic-text-capture|automatic translations]].

## Manually add source content

You can also add content manually. This is recommended if your game contains text that doesn't appear during typical gameplay, like a complex conversation tree, which may take longer to collect via ATC. You can add entries to the table [in the localization page](#add-sources-with-localization-settings) or [with a `.csv` file upload](#add-sources-with-file-upload). It is recommended to use the `.csv` upload if you want to specify an entry's Key, Context, or Example fields.

<Alert severity ='warning'>
Entries in the localization table are case-sensitive.

For example, when using "hello" as a source value on the localization table, Roblox does not apply translations for "Hello" or "HELLO".
</Alert>

You can manually add image and sound asset IDs to the localization table with a `.csv` upload. For more information see [[external/roblox-creator-docs/production/localization/localize-with-scripting#localize-images-and-sounds|Localize images and sounds]].

### Add sources with localization settings

You can add source content in the [[external/roblox-creator-docs/production/localization/index#localization-settings|localization page]]. This is ideal for making quick additions to your localization table.

To add source content through the localization page:

1. In your game's localization page, click the **Translate** button on the top right.

   <img src="../../assets/localization/Portal-Translate.png"
   width="100%" />

2. Select the **Strings** tab.
3. Click **Add Entry**.
4. In the **Text to translate** field, input the source text and click **Save**.

   <img src="../../assets/localization/Portal-Add-Source-String.png"
   width="100%" />

5. If you are using key-based scripting to translate a string, input the key name in the **Key** field.
6. If the string has multiple meanings, such as a character's back and a back button, input the full path of the specific text object in the **Context** field.
7. Click **Save**.

### Add sources with file upload

You can add source content to your localization table with a `.csv` upload. You can use this option when making large numbers of updates to your localization table.

To add source content through the `.csv` upload:

1. In Studio, open **Localization Tools** from the **Window**&nbsp;⟩ **Localization**
2. In the **Cloud Localization Table** section, select **Download** to save the `.csv`.
3. Open the `.csv` in your preferred spreadsheet editor.
4. Under the **Source** column, add source text and save. You can leave the other columns blank.

      <table>
   <thead>
     <tr>
       <th>Key</th>
       <th>Context </th>
       <th>Example</th>
       <th>Source</th>
     </tr>
   </thead>
   <tbody>
     <tr>
       <td></td>
       <td></td>
       <td></td>
       <td>Options</td>
     </tr>
     <tr>
       <td></td>
       <td></td>
       <td></td>
       <td>Start</td>
     </tr>
   </tbody>
   </table>

5. In Studio, in the **Cloud Localization Table** section, select **Update** and upload the new `.csv` file.
6. Click **Confirm** on the **Confirm Upload** prompt to save the new entry to the cloud localization table.


## Related Files

- [[external/roblox-creator-docs/production/localization/add-translations]] - Add translations.
- [[external/roblox-creator-docs/production/localization/automatic-translations]] - Automatic translation.
- [[external/roblox-creator-docs/production/localization/auto-translate-dynamic-content]] - Automatically translate dynamic content.
- [[external/roblox-creator-docs/production/localization/language-codes]] - Language codes.
- [[external/roblox-creator-docs/production/localization/index]] - Localization.
- [[external/roblox-creator-docs/production/localization/localize-with-scripting]] - Localize with scripting.
- [[external/roblox-creator-docs/production/localization/manual-translations]] - Manual translations.
- [[external/roblox-creator-docs/production/localization/remove-content]] - Remove content.
- [[external/roblox-creator-docs/production/localization/translate-dynamic-content]] - Translate dynamic content.
- [[external/roblox-creator-docs/production/localization/work-with-translators]] - Work with translators.
