import requests
from dotenv import load_dotenv
from dotenv import set_key
import os

class RestClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None
        load_dotenv()  # Load environment variables on initialization

    def authenticate(self, username, password):
        url = f"{self.base_url}/connect/token"
        payload = {
            "grant_type": "password", 
            "scope": "offline_access",
            "username": username,
            "password": password,
        }
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        
        try:
            response = requests.post(url, data=payload, headers=headers)
            response.raise_for_status()  # Raise exception for non-200 status codes
            
            token = response.json().get("access_token")
            if token:
                self.token = token
                set_key('.env', 'ADMIN_TOKEN', token)
                print('Token retrieved and saved successfully!')
            else:
                raise Exception("No access token in response")
                
        except requests.exceptions.RequestException as e:
            raise Exception(f"Authentication failed: {str(e)}")

    def get_headers(self):
        if not self.token:
            raise Exception("No token found. Please authenticate first.")
        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def get(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        headers = self.get_headers()
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response

    def post(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        headers = self.get_headers()
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response
