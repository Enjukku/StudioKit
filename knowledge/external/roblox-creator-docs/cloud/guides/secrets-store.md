---
title: Secrets stores
description: Covers usage for the Secrets store API.
tags: [roblox, documentation, external-reference, priority-reference, cloud, ui]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [cloud/guides/secrets-store.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/cloud/guides/secrets-store.md). Published page: [https://create.roblox.com/docs/cloud/guides/secrets-store](https://create.roblox.com/docs/cloud/guides/secrets-store).

In addition to [[external/roblox-creator-docs/cloud-services/secrets|managing your secrets within games]], you can manage secrets using the Open Cloud secrets store API.

Before using the API, you must [[external/roblox-creator-docs/cloud/auth/api-keys|generate an API key]] with the `secret-store` API system or [[external/roblox-creator-docs/cloud/auth/oauth2-overview|configure your OAuth 2.0 app]] with the `universe.secret` scope type. The examples on this page use API keys.

## Secret encryption

When creating or updating secrets on Roblox, you must encrypt secrets with a [LibSodium sealed box](https://libsodium.gitbook.io/doc/public-key_cryptography/sealed_boxes) and your game's public key, and then base64-encode the result.

First, get your game's public key:

```bash
curl --location 'https://apis.roblox.com/cloud/v2/universes/{universeId}/secrets/public-key' \
--request GET \
--header 'x-api-key: <your-secret-here>' \
```

Next, create a sealed box and base64-encode it. The example below uses Python and [PyNaCl](https://pynacl.readthedocs.io/en/latest/public/#nacl-public-sealedbox). (Run `pip install pynacl` to install it locally).

```python
from base64 import b64encode
from nacl import encoding, public

public_key = "Zgj4+V7vSaEZ06rXazKJUIcUnVa95tUNiwXAif/vdHo="
secret_content = "my_api_key_content"
public_key = public.PublicKey(public_key.encode("utf-8"), encoding.Base64Encoder())
sealed_box = public.SealedBox(public_key)
encrypted = sealed_box.encrypt(secret_content.encode("utf-8"))
print(b64encode(encrypted).decode("utf-8"))
```

You can then create or update a secret using the output. This example creates a new secret:

```bash
curl --location 'https://apis.roblox.com/cloud/v2/universes/6930499524/secrets' \
--request POST \
--header 'Content-Type: application/json' \
--header 'x-api-key: <your-secret-here>' \
--data '{
    "id": "mySecret",
    "secret": "fP9scJkcDk492F4c1VHZ5QS8v2qsAg7uI+NVVEw6zC0GBnj7xpi7UrNr++lCfr4wyq3ia9Uuu+Ao8HtIXz2gRxBX",
    "key_id": "1200590785272263122"
}'
```

After you create one, see [[external/roblox-creator-docs/cloud-services/secrets#use-secrets|Use secrets]] to use your secret in game.

## Update secrets

To update the above secret:

```bash
curl --location 'https://apis.roblox.com/cloud/v2/universes/6930499524/secrets/mySecret' \
--request PATCH \
--header 'Content-Type: application/json' \
--header 'x-api-key: <your-secret-here>' \
--data '{
    "secret": "2Fczw/PL7woOzHnGHQ65sT0MbzJjEOlfibyKxy374CqzFyEb2QTS8grtNBgG/0sfIvSHEo9JWN+pUr0NTPs0V6lj",
    "key_id": "1200590785272263122"
}'
```

If you need to clean up a secret, a deletion request looks like this:

```bash
curl --location 'https://apis.roblox.com/cloud/v2/universes/6930499524/secrets/mySecret' \
--request DELETE \
--header 'Content-Type: application/json' \
--header 'x-api-key: <your-secret-here>'
```


## Related Files

- [[external/roblox-creator-docs/cloud/guides/advertising]] - Advertising.
- [[external/roblox-creator-docs/cloud/guides/instance]] - Engine instances.
- [[external/roblox-creator-docs/cloud/guides/configs]] - Experience configs.
- [[external/roblox-creator-docs/cloud/guides/experiments]] - Experiments.
- [[external/roblox-creator-docs/cloud/guides/usage-messaging]] - Messaging usage guide.
- [[external/roblox-creator-docs/cloud/guides/index]] - Open Cloud guides.
- [[external/roblox-creator-docs/cloud/guides/usage-assets]] - Usage guide for assets.
- [[external/roblox-creator-docs/cloud/guides/usage-place-publishing]] - Usage guide for place publishing.
- [[external/roblox-creator-docs/cloud/guides/inventory]] - User inventories.
- [[external/roblox-creator-docs/cloud/guides/experience-notifications]] - User notifications.
