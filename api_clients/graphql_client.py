import requests

class GraphQLClient:
    def __init__(self, base_url, rest_client):
        self.url = f"{base_url}/graphql"
        self.rest_client = rest_client

    def send_query(self, query, variables=None):
        headers = self.rest_client.get_headers()
        payload = {"query": query, "variables": variables or {}}
        response = requests.post(self.url, json=payload, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"GraphQL request failed: {response.text}")
