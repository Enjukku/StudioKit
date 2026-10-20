---
title: Data store right to be forgotten (RTBF)
description: Configure automated deletion of data store keys and stores when you receive a right-to-be-forgotten request, using the Data Stores Manager or the Open Cloud Configs API with config templates.
tags: [roblox, documentation, external-reference, priority-reference, cloud, services, datastores]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [cloud-services/data-stores/right-to-be-forgotten.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/cloud-services/data-stores/right-to-be-forgotten.md). Published page: [https://create.roblox.com/docs/cloud-services/data-stores/right-to-be-forgotten](https://create.roblox.com/docs/cloud-services/data-stores/right-to-be-forgotten).

**Right to be forgotten (RTBF)** for data stores lets you declare which keys and data stores hold a user's data. When Roblox processes an RTBF request for your game, the system uses those templates to remove the matching data automatically. You can configure templates visually through the [[external/roblox-creator-docs/cloud-services/data-stores/data-stores-manager|Data Stores Manager]] in the Creator Hub, or programmatically through the Open Cloud [Configs API](/cloud/reference/features/configs).

## Automated RTBF

To use automated RTBF processing, you must define deletion templates. These templates tell Roblox which data stores or keys belong to a specific user. You can have up to 100 templates to identify your user data.

### Deletion templates

Automated RTBF works by matching patterns. You define a template for your user data using a `{UserId}` token. When Roblox receives a right-to-be-forgotten request, the system replaces that token with the requester's actual ID and scans your data stores for matches to delete.

### Eligibility requirements

For an entry to be eligible for automated deletion, it must meet the following criteria:

- **Storage type** — User data should be stored in a standard data store or an ordered data store. Deletion of an entire data store is supported for standard data stores only.
- **Identifier** — The user ID must be part of the `Name` or the `Scope` of the data store or key.
- **Format** — The ID must be identifiable via a static string pattern (for example, `User_{UserId}`).

## Configure automated RTBF via Data Stores Manager

The Creator Hub provides a visual interface to manage your RTBF templates without using the command line.

<Alert severity="info">
For group games, you must add the **View Analytics** permission to view configs, and the **Edit and publish experience** permission to view, edit, and publish configs. Additionally, the user themself must be [eligible to publish games](https://en.help.roblox.com/hc/en-us/articles/203313890-How-to-Publish-Public-Experiences-on-Roblox).
</Alert>

1. Select a game on the [Creator Dashboard](https://create.roblox.com/dashboard/creations).
1. In the left-hand navigation, go to **Configurations** > **Data stores manager**.
1. Select the **RTBF Deletion** tab.
1. Click **Create Template**.
1. Select the **Type** (**Standard Data Store**, **Standard Key**, or **Ordered Key**).
1. Enter the corresponding fields with your template using the `{UserId}` token (for example, `PlayerInventory_{UserId}`). This token is case-sensitive.
1. Double-check the sample output and click **Create**.

   <img src="./../../assets/data/data-store/Data-Stores-RTBF-Template.png" alt="Create template dialog with Type, Data Store, Key Pattern, and Scope fields, and a preview of the resulting data store path." />

## Configure automated RTBF via Configs API

You can also manage RTBF templates programmatically using the Open Cloud Configs API. This is useful for automation or managing templates at scale.

1. In the Creator Dashboard, [create or edit an API key](https://create.roblox.com/dashboard/credentials) to include the **`universe:read`** and **`universe:write`** permissions for every universe where you want to automate RTBF deletion. For more detail, see [[external/roblox-creator-docs/cloud/auth/api-keys|Manage API keys]].
1. Templates are stored as a JSON configuration named `user_data_templates`. There are two main types:

   - **Key template** — Identifies specific keys. Requires `data_store_type` (`STANDARD` or `ORDERED`), `data_store_name`, and `key_pattern`. `scope_pattern` is optional but recommended.
   - **Data store template** — Identifies an entire data store. Requires `data_store_type` (currently only supports `STANDARD`) and `data_store_pattern`.

   For both template kinds, the `{UserId}` token is replaced with the user's ID when an RTBF request is processed.

		```json title="Example Configuration"
		{
			"user_data_templates": [
				{
					"key_template": {
						"data_store_type": "STANDARD",
						"data_store_name": "PlayerInventory",
						"key_pattern": "User_{UserId}",
						"scope_pattern": "Scope_{UserId}"
					}
				},
				{
					"key_template": {
						"data_store_type": "ORDERED",
						"data_store_name": "PlayerLeaderboard",
						"key_pattern": "User_{UserId}",
						"scope_pattern": "global"
					}
				},
				{
					"data_store_template": {
						"data_store_type": "STANDARD",
						"data_store_pattern": "Player_{UserId}_Save"
					}
				}
			]
		}
		```

   <Alert severity="warning">
   The `{UserId}` token is **case-sensitive**. If `scope_pattern` is omitted or blank, it defaults to `global`.
	 </Alert>

1. Next, submit via the Open Cloud [Configs API](/cloud/reference/features/configs). In the following examples, replace `<API_KEY>` and `<UNIVERSE_ID>` in each request, and send all requests to the `DataStoresConfig` repository.

   <Alert severity="info">
   For additional endpoints and behavior, see the [Cloud API reference](/cloud/reference/features/configs) and the [[external/roblox-creator-docs/cloud/guides/configs|experience configs]] guide.
	 </Alert>

	 1. Create a draft via a `PUT` request that defines your configuration. If a draft already exists, this request overwrites it.

			```bash
			curl --location --request PUT 'https://apis.roblox.com/creator-configs-public-api/v1/configs/universes/<UNIVERSE_ID>/repositories/DataStoresConfig/draft:overwrite' \
				--header 'x-api-key: <API_KEY>' \
				--header 'Content-Type: application/json' \
				--data-raw '{
				"entries": {
					"user_data_templates": [
						{
							"key_template": {
								"data_store_type": "STANDARD",
								"data_store_name": "PlayerInventory",
								"key_pattern": "User_{UserId}",
								"scope_pattern": "Scope_{UserId}"
							}
						},
						{
							"key_template": {
								"data_store_type": "ORDERED",
								"data_store_name": "PlayerLeaderboard",
								"key_pattern": "User_{UserId}",
								"scope_pattern": "global"
							}
						},
						{
							"data_store_template": {
								"data_store_type": "STANDARD",
								"data_store_pattern": "Player_{UserId}_Save"
							}
						}
					]
				}
			}'
			```

	 1. Verify your draft via a `GET` request to retrieve and review the draft before it goes live.

			```bash
			curl --location --request GET 'https://apis.roblox.com/creator-configs-public-api/v1/configs/universes/<UNIVERSE_ID>/repositories/DataStoresConfig/draft' \
				--header 'x-api-key: <API_KEY>'
			```

	 1. After verification, send this `POST` request to publish. The only way to undo this action is to restore a previous version. This action also requires that the account associated with the API key is [eligible to publish games](https://en.help.roblox.com/hc/en-us/articles/203313890-How-to-Publish-Public-Experiences-on-Roblox).

			```bash
			curl --location --request POST 'https://apis.roblox.com/creator-configs-public-api/v1/configs/universes/<UNIVERSE_ID>/repositories/DataStoresConfig/publish' \
				--header 'x-api-key: <API_KEY>' \
				--header 'Content-Type: application/json' \
				--data-raw '{
				"deploymentStrategy": "Immediate"
			}'
			```

	 1. After publishing, confirm the configuration is live with this `GET` request.

			```bash
			curl --location --request GET 'https://apis.roblox.com/creator-configs-public-api/v1/configs/universes/<UNIVERSE_ID>/repositories/DataStoresConfig/full' \
				--header 'x-api-key: <API_KEY>'
			```

## Best practices

- **Case sensitivity** — Use the exact `{UserId}` token in your patterns. Variants such as `{userId}` are not accepted.
- **Manual verification** — Compare your patterns to your live Luau usage using [[external/roblox-creator-docs/cloud-services/data-stores/data-stores-manager|Data Stores Manager]] in the Creator Hub before you publish configuration.
- **Default scopes** — If a data store uses the default scope, set `scope_pattern` to `"global"` in the key template.
- **Test end-to-end flow on a test game** — For full validation of your templates, consider creating a test game and dummy account, populating it with dummy data for that account's User ID, requesting RTBF on the dummy account, and ensuring the data is deleted once the account is processed.
- **Confirm deletions** — After onboarding on your live game, when an RTBF request appears in your Roblox messages, verify that the corresponding data is removed within 30 days.


## Related Files

- [[external/roblox-creator-docs/cloud-services/data-stores/best-practices]] - Best practices for data stores.
- [[external/roblox-creator-docs/cloud-services/data-stores/error-codes-and-limits]] - Data store error codes and limits.
- [[external/roblox-creator-docs/cloud-services/data-stores/observability]] - Data store observability.
- [[external/roblox-creator-docs/cloud-services/data-stores/versioning-listing-and-caching]] - Data store versioning, listing, and caching.
- [[external/roblox-creator-docs/cloud-services/data-stores/index]] - Data stores.
- [[external/roblox-creator-docs/cloud-services/data-stores/data-stores-manager]] - Data Stores Manager.
- [[external/roblox-creator-docs/cloud-services/data-stores/player-data-purchasing]] - Implement player data and purchasing systems.
