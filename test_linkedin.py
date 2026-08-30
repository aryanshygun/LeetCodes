import os
import requests

token = os.environ["LINKEDIN_ACCESS_TOKEN"]

userinfo = requests.get(
    "https://api.linkedin.com/v2/userinfo",
    headers={
        "Authorization": f"Bearer {token}",
    },
    timeout=30,
)

userinfo.raise_for_status()

member_id = userinfo.json()["sub"]
member_urn = f"urn:li:person:{member_id}"

response = requests.post(
    "https://api.linkedin.com/rest/posts",
    headers={
        "Authorization": f"Bearer {token}",
        "Linkedin-Version": "202608",
        "X-Restli-Protocol-Version": "2.0.0",
        "Content-Type": "application/json",
    },
    json={
        "author": member_urn,
        "commentary": "hello",
        "visibility": "PUBLIC",
        "distribution": {
            "feedDistribution": "MAIN_FEED",
            "targetEntities": [],
            "thirdPartyDistributionChannels": [],
        },
        "lifecycleState": "PUBLISHED",
        "isReshareDisabledByAuthor": False,
    },
    timeout=30,
)

print("Status:", response.status_code)
print("Response:", response.text)
print("Post ID:", response.headers.get("x-restli-id"))

response.raise_for_status()

print("Successfully posted 'hello' to LinkedIn.")