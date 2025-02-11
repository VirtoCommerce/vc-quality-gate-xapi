import requests
from dotenv import load_dotenv, set_key
import os

global auth_token


class RestClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None

    def authenticate(self, username, password):
        url = f"{self.base_url}/connect/token"
        payload = {
            "grant_type": "password",
            "scope": "offline_access",
            "username": username,
            "password": password,
        }
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = requests.post(url, data=payload, headers=headers)
        if response.status_code == 200:
            self.token = response.json().get("access_token")
        else:
            raise Exception(f"Auth failed: {response.status_code} - {response.text()}")
                
        # Extract the token from the response
        token = response.json().get('access_token')
        if token:                   
           set_key('.env', 'ADMIN_TOKEN', token)
           print('Token retrieved and saved successfully!')
        else:
            print('Failed to retrieve token')
            print(response.text)
   

    def get_headers(self):
        if not self.token:
            raise Exception("No token found. Please authenticate first.")
        return {"Authorization": f"Bearer {self.token}"}

    def get(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        headers = self.get_headers()
        response = requests.get(url, headers=headers)
        return response

    def post(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        headers = self.get_headers()
        response = requests.post(url, json=data, headers=headers)
        return response
