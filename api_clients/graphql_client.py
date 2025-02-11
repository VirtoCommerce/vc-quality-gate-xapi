import requests
import json

class GraphQLClient:
    def __init__(self, base_url, rest_client, token=None):
        self.base_url = base_url
        self.rest_client = rest_client
        self.token = token
    
    def send_query(self, query, variables=None):
        """Send a GraphQL query with valid token."""
        return self._post_request(self.base_url, query, variables)

    def execute_query(self, query, variables=None):
        url = f"{self.base_url}/graphql"
        return self.send_query(query, variables)

    def _post_request(self, base_url, query, variables=None):
        headers = self.rest_client.get_headers()
        payload = {"query": query, "variables": variables or {}}
        response = requests.post(base_url, json=payload, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            if response.status_code == 200:
                return response.json()
            else:
                raise Exception(f"GraphQL query failed: {response.text}")
    
    def execute(self, query, variables=None):
        response = requests.post(self.url, json={'query': query, 'variables': variables}, headers=self.headers)
        response.raise_for_status()
        return response.json()



