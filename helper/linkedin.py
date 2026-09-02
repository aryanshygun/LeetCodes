import os
from pathlib import Path

import requests

LINKEDIN_API = "https://api.linkedin.com"
LINKEDIN_VERSION = os.getenv("LINKEDIN_VERSION", "202608")


def get_access_token():
    token = os.getenv("LINKEDIN_ACCESS_TOKEN")

    if not token:
        raise RuntimeError("LINKEDIN_ACCESS_TOKEN is not set.")

    return token


def get_headers(access_token):
    return {
        "Authorization": f"Bearer {access_token}",
        "Linkedin-Version": LINKEDIN_VERSION,
        "X-Restli-Protocol-Version": "2.0.0",
    }


def get_member_urn(access_token):
    response = requests.get(
        f"{LINKEDIN_API}/v2/userinfo",
        headers={
            "Authorization": f"Bearer {access_token}",
        },
        timeout=30,
    )

    if not response.ok:
        raise RuntimeError(
            f"LinkedIn userinfo failed ({response.status_code}):\n"
            f"{response.text}"
        )

    data = response.json()

    return f"urn:li:person:{data['sub']}"


def initialize_image_upload(access_token, member_urn):
    response = requests.post(
        f"{LINKEDIN_API}/rest/images?action=initializeUpload",
        headers={
            **get_headers(access_token),
            "Content-Type": "application/json",
        },
        json={
            "initializeUploadRequest": {
                "owner": member_urn
            }
        },
        timeout=30,
    )

    if not response.ok:
        raise RuntimeError(
            f"LinkedIn image initialization failed "
            f"({response.status_code}):\n"
            f"{response.text}"
        )

    data = response.json()["value"]

    return data["uploadUrl"], data["image"]


def upload_image(access_token, member_urn, image_path):
    image_path = Path(image_path)

    if not image_path.exists():
        raise FileNotFoundError(
            f"Image does not exist: {image_path}"
        )

    upload_url, image_urn = initialize_image_upload(
        access_token,
        member_urn,
    )

    with image_path.open("rb") as image:
        response = requests.put(
            upload_url,
            headers={
                "Content-Type": "image/png",
            },
            data=image,
            timeout=120,
        )

    if not response.ok:
        raise RuntimeError(
            f"LinkedIn image upload failed "
            f"({response.status_code}):\n"
            f"{response.text}"
        )

    return image_urn


def create_post(
    access_token,
    member_urn,
    caption,
    image_urn,
    alt_text,
):
    payload = {
        "author": member_urn,
        "commentary": caption,
        "visibility": "PUBLIC",
        "distribution": {
            "feedDistribution": "MAIN_FEED",
            "targetEntities": [],
            "thirdPartyDistributionChannels": [],
        },
        "content": {
            "media": {
                "id": image_urn,
                "altText": alt_text,
            }
        },
        "lifecycleState": "PUBLISHED",
        "isReshareDisabledByAuthor": False,
    }

    response = requests.post(
        f"{LINKEDIN_API}/rest/posts",
        headers={
            **get_headers(access_token),
            "Content-Type": "application/json",
        },
        json=payload,
        timeout=30,
    )

    if not response.ok:
        raise RuntimeError(
            f"LinkedIn post failed "
            f"({response.status_code}):\n"
            f"{response.text}"
        )

    return response.headers.get("x-restli-id")


def post(
    caption,
    image_path,
    alt_text="LeetCode solution",
):
    access_token = get_access_token()

    member_urn = get_member_urn(access_token)

    print(f"Using LinkedIn member: {member_urn}")

    image_urn = upload_image(
        access_token=access_token,
        member_urn=member_urn,
        image_path=image_path,
    )

    print(f"Uploaded image: {image_urn}")

    post_id = create_post(
        access_token=access_token,
        member_urn=member_urn,
        caption=caption,
        image_urn=image_urn,
        alt_text=alt_text,
    )

    print(f"LinkedIn post created: {post_id}")

    return post_id