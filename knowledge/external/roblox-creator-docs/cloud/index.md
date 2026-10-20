---
title: Cloud API reference
description: Get comprehensive API reference documentation for Open Cloud.
tags: [roblox, documentation, external-reference, priority-reference, cloud, index]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [cloud/index.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/cloud/index.md). Published page: [https://create.roblox.com/docs/cloud](https://create.roblox.com/docs/cloud).

With Open Cloud, you can access Roblox resources through standard [REST](https://en.wikipedia.org/wiki/REST) APIs, which lets you build everything from command line automation tools to complex web apps. You can update games, restart servers, work with your data stores and memory stores, manage user restrictions, list inventory items, and much, much more.

This reference is broken into two sections:

- A [section that separates endpoints by feature](/cloud/reference/features/accounts) (Avatars, Game Passes, Users, etc.)
- A [section that separates endpoints by domain](/cloud/reference/domains/apis) (base URL)

**Both sections** contain the full list of available API endpoints. We recommend the [features section](/cloud/reference/features/accounts) since it helps consolidate endpoints by use case, but experienced Open Cloud developers might prefer to browse by domain.

- Whenever possible, use endpoints that support [[external/roblox-creator-docs/cloud/auth/api-keys|API keys]] or [[external/roblox-creator-docs/cloud/auth/oauth2-overview|OAuth 2.0]] for authentication. They have strong stability guarantees and receive regular updates.

- Legacy APIs use cookie-based authentication, can incorporate breaking changes without notice, and have minimal stability guarantees. We don't recommend them for production applications.

<Alert severity="info">
Roblox also offers [[external/roblox-creator-docs/cloud/webhooks/webhook-notifications|webhooks]], which can notify your applications when certain events occur, such as refunds or changes to subscriptions.
</Alert>

## Get started with Open Cloud

1. Set up authentication for your application.

   See the documentation for how to use [[external/roblox-creator-docs/cloud/auth/api-keys|API keys]] or [[external/roblox-creator-docs/cloud/auth/oauth2-overview|OAuth 2.0]]. API keys are the easiest way to get started.

1. Test API calls using tools like [Postman](https://www.postman.com) with [[external/roblox-creator-docs/cloud/reference/openapi|OpenAPI descriptions]] or the [[external/roblox-creator-docs/cloud/auth/oauth2-sample|OAuth 2.0 sample app]].
1. Review the [[external/roblox-creator-docs/cloud/guides/index|resource guides]] for end-to-end walkthroughs of using certain APIs.
1. Explore the left navigation for the full list of features, [[external/roblox-creator-docs/cloud/reference/patterns|common API patterns]], [[external/roblox-creator-docs/cloud/reference/types|types]], and [[external/roblox-creator-docs/cloud/reference/errors|error codes]].

## Make requests within games

`Class.HttpService` lets you make HTTP requests to a subset of the Open Cloud endpoints. For more information, see [[external/roblox-creator-docs/cloud-services/http-service|In-game HTTP requests]].


## Related Files

- [[external/roblox-creator-docs/cloud/guides/advertising]] - Advertising.
- [[external/roblox-creator-docs/cloud/guides/analytics/index]] - Analytics.
- [[external/roblox-creator-docs/cloud/guides/alerts/index]] - Analytics alerts.
- [[external/roblox-creator-docs/cloud/webhooks/automate-right-to-erasure]] - Automate right to erasure using webhooks.
- [[external/roblox-creator-docs/cloud/guides/instance]] - Engine instances.
- [[external/roblox-creator-docs/cloud/guides/error-reporting/index]] - Error reporting.
- [[external/roblox-creator-docs/cloud/reference/errors]] - Errors.
- [[external/roblox-creator-docs/cloud/guides/configs]] - Experience configs.
- [[external/roblox-creator-docs/cloud/guides/experiments]] - Experiments.
- [[external/roblox-creator-docs/cloud/guides/data-stores/request-handling]] - Handle Open Cloud data store requests.
- [[external/roblox-creator-docs/cloud/auth/api-keys]] - Manage API keys.
- [[external/roblox-creator-docs/cloud/guides/usage-messaging]] - Messaging usage guide.
- [[external/roblox-creator-docs/cloud/auth/oauth2-develop]] - OAuth 2.0 app implementation.
- [[external/roblox-creator-docs/cloud/auth/oauth2-registration]] - OAuth 2.0 app registration.
- [[external/roblox-creator-docs/cloud/auth/oauth2-reference]] - OAuth 2.0 authentication.
- [[external/roblox-creator-docs/cloud/auth/oauth2-overview]] - OAuth 2.0 overview.
- ...and 19 more local docs.
