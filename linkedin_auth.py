import os
import time
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlencode, urlparse

import requests

CLIENT_ID = os.environ["LINKEDIN_CLIENT_ID"]
CLIENT_SECRET = os.environ["LINKEDIN_CLIENT_SECRET"]

REDIRECT_URI = "http://localhost:8000/callback"

AUTH_URL = "https://www.linkedin.com/oauth/v2/authorization"
TOKEN_URL = "https://www.linkedin.com/oauth/v2/accessToken"


authorization_code = None


class CallbackHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global authorization_code

        parsed = urlparse(self.path)

        if parsed.path != "/callback":
            self.send_response(404)
            self.end_headers()
            return

        params = parse_qs(parsed.query)

        if "error" in params:
            error = params["error"][0]
            description = params.get("error_description", [""])[0]

            self.send_response(400)
            self.end_headers()

            self.wfile.write(f"Authorization failed: {error} {description}".encode())

            print(f"\nAuthorization failed: {error}")
            print(description)

            return

        if "code" not in params:
            self.send_response(400)
            self.end_headers()

            self.wfile.write(b"Authorization code was not provided.")

            return

        authorization_code = params["code"][0]

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

        self.wfile.write(b"""
            <html>
                <body>
                    <h2>LinkedIn authorization successful.</h2>
                    <p>You can close this window.</p>
                </body>
            </html>
            """)

    def log_message(self, format, *args):
        return


def get_authorization_url():
    params = {
        "response_type": "code",
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "scope": "w_member_social",
        "state": "leetcode-linkedin",
    }

    return f"{AUTH_URL}?{urlencode(params)}"


def exchange_code_for_token(code):
    response = requests.post(
        TOKEN_URL,
        data={
            "grant_type": "authorization_code",
            "code": code,
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "redirect_uri": REDIRECT_URI,
        },
        timeout=30,
    )

    response.raise_for_status()

    return response.json()


def main():
    print("Starting LinkedIn authorization...")

    authorization_url = get_authorization_url()

    print()
    print("Opening LinkedIn in your browser...")
    print()
    print(authorization_url)
    print()

    webbrowser.open(authorization_url)

    server = HTTPServer(
        ("localhost", 8000),
        CallbackHandler,
    )

    print("Waiting for LinkedIn authorization...")
    print("Listening on http://localhost:8000/callback")

    while authorization_code is None:
        server.handle_request()

    server.server_close()

    print()
    print("Authorization code received.")
    print("Exchanging code for access token...")

    token_data = exchange_code_for_token(authorization_code)

    access_token = token_data["access_token"]
    expires_in = token_data.get("expires_in")

    print()
    print("=" * 60)
    print("SUCCESS")
    print("=" * 60)
    print()
    print("Access token:")
    print(access_token)
    print()

    if expires_in:
        days = expires_in / 86400
        print(f"Token expires in approximately {days:.0f} days.")

    print()
    print("Add this token to GitHub as:")
    print()
    print("LINKEDIN_ACCESS_TOKEN")
    print()
    print("Do not commit this token to GitHub.")
    print()


if __name__ == "__main__":
    main()
