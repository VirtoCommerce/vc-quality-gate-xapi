import requests
import time

class RestClient:
    def __init__(self, base_url, admin_user, admin_pass):
        self.base_url = base_url
        self.access_token = None
        self.token_expiration_time = None
        self.admin_user = admin_user
        self.admin_pass = admin_pass

    def authenticate(self):
        url = f"{self.base_url}/connect/token"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {
            "grant_type": "password",
            "scope": "offline_access",
            "username": self.admin_user,
            "password": self.admin_pass,
        }
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            token_data = response.json()
            self.access_token = token_data["access_token"]
            self.token_expiration_time = time.time() + token_data["expires_in"] - 60
        else:
            raise Exception(f"Token fetch failed: {response.text}")

    def is_token_expired(self):
        return not self.access_token or time.time() >= self.token_expiration_time

    def get_headers(self):
        if self.is_token_expired():
            self.authenticate()
        return {"Authorization": f"Bearer {self.access_token}"}

    def send_request(self, method, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
        headers = self.get_headers()
        response = requests.request(method, url, headers=headers, json=data)
        return response.json()
