---
title: User notifications
description: Use Open Cloud to send experience notifications to users. Help players keep up with their favorite experiences through timely, personalized notifications.
tags: [roblox, documentation, external-reference, priority-reference, cloud, ui]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [cloud/guides/experience-notifications.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/cloud/guides/experience-notifications.md). Published page: [https://create.roblox.com/docs/cloud/guides/experience-notifications](https://create.roblox.com/docs/cloud/guides/experience-notifications).

import Intro from '../../includes/experience-notifications/intro.md'

<Intro components={props.components} />

After they receive a notification, users can join the experience directly via the **Join** button and spawn according to your [launch data](#include-launch-and-analytics-data).

For more information on features, eligibility requirements, usage guidelines, and the corresponding Engine API, see the [[external/roblox-creator-docs/production/promotion/experience-notifications|Experiences guide]].

## Implementation

The [UserNotification](/cloud/reference/UserNotification) resource lets you send experience notifications to users. Before using it, you must [[external/roblox-creator-docs/cloud/auth/api-keys|generate an API key]] or [[external/roblox-creator-docs/cloud/auth/oauth2-overview|configure OAuth 2.0]] for your app. The examples on this page use API keys.

To send an experience notification to a user:

1. [[external/roblox-creator-docs/production/promotion/experience-notifications#create-a-notification-string|Create a notification string]] in the [Creator Dashboard](https://create.roblox.com/dashboard/creations) (this step must be done in the Creator Dashboard; there's no Open Cloud API for it).
1. Form the request:
   1. Copy the API key to the `x-api-key` request header.
   1. Copy the notification string asset ID as the value of the `payload.message_id` property.
   1. Set `payload.type` to `"MOMENT"`.
   1. Set `source.universe` to be the universe resource URL `"universes/${UniverseID}"`.

```bash title="Send an experience notification"
curl --location 'https://apis.roblox.com/cloud/v2/users/${UserId}/notifications' \
--header 'x-api-key: ${ApiKey}' \
--header 'Content-Type: application/json' \
--data '{
	"source": {
		"universe": "universes/${UniverseID}"
	},
	"payload": {
		"message_id": "${AssetID}",
		"type": "MOMENT"
	}
}'
```

Example response which returns the notification ID in the `id` field:

```json
{
  "path": "users/505306092/notifications/6ca4d981-36fa-4255-82a1-14d95c116889",
  "id": "6ca4d981-36fa-4255-82a1-14d95c116889"
}
```

### Customize notifications using parameters

To customize the notification for each recipient, include **parameters** in the [notification string](#implementation). Then customize the parameters when calling the API. For example, you can define the notification string as:

<p><Chip label="{userId-friend} beat your high score by {points} points! Time to level up?" size="large" color="primary" variant="outlined" /></p>

Add the `userId-friend` and `points` parameters in the script:

```bash title="Customize Notification Using Parameters"
curl --location 'https://apis.roblox.com/cloud/v2/users/${UserId}/notifications' \
--header 'x-api-key: ${ApiKey}' \
--header 'Content-Type: application/json' \
--data '{
	"source": {
		"universe": "universes/${UniverseID}"
	},
	"payload": {
		"message_id": "${AssetID}",
		"type": "MOMENT",
		"parameters": {
			"userId-friend": {"int64_value": 3702832553},
			"points": {"string_value": "5"}
		}
	}
}'
```

### Include launch and analytics data

To further improve user experience, you can include **launch data** in the notification, useful for scenarios such as routing users to a coordinate location or personalizing the joining experience. Additionally, you can include [[external/roblox-creator-docs/production/promotion/experience-notifications#analytics|analytics]] data to segment the performance of different categories of notifications.

```bash title="Include Launch Data and Analytics Data"
curl --location 'https://apis.roblox.com/cloud/v2/users/${UserId}/notifications' \
--header 'x-api-key: ${ApiKey}' \
--header 'Content-Type: application/json' \
--data '{
	"source": {
		"universe": "universes/${UniverseID}"
	},
	"payload": {
		"message_id": "${AssetID}",
		"type": "MOMENT"
	},
	"join_experience": {
		"launch_data": "Test_Launch_Data"
	},
	"analytics_data": {
		"category": "Test_Analytics_Category"
	}
}'
```

## Rate limits and delivery

Each user can receive **one** notification per day from a given experience, and you receive transparent feedback when a user's throttle limit is reached.

There are many other reasons that a notification might not be delivered. For more information, see [[external/roblox-creator-docs/production/promotion/experience-notifications#delivery-system|Delivery system]] in the Engine guide.


## Related Files

- [[external/roblox-creator-docs/cloud/guides/advertising]] - Advertising.
- [[external/roblox-creator-docs/cloud/guides/instance]] - Engine instances.
- [[external/roblox-creator-docs/cloud/guides/configs]] - Experience configs.
- [[external/roblox-creator-docs/cloud/guides/experiments]] - Experiments.
- [[external/roblox-creator-docs/cloud/guides/usage-messaging]] - Messaging usage guide.
- [[external/roblox-creator-docs/cloud/guides/index]] - Open Cloud guides.
- [[external/roblox-creator-docs/cloud/guides/secrets-store]] - Secrets stores.
- [[external/roblox-creator-docs/cloud/guides/usage-assets]] - Usage guide for assets.
- [[external/roblox-creator-docs/cloud/guides/usage-place-publishing]] - Usage guide for place publishing.
- [[external/roblox-creator-docs/cloud/guides/inventory]] - User inventories.
