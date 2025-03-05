import requests

class GraphQLClient:
    def __init__(self, base_url, rest_client, token=None):
        self.base_url = base_url
        self.rest_client = rest_client
        self.token = token
        self.graphql_endpoint = f"{self.base_url}/graphql"
    
    def execute_query(self, query, variables=None):
        """Send a GraphQL query with valid token."""
        headers = self.rest_client.get_headers()
        payload = {"query": query, "variables": variables or {}}
        
        response = requests.post(self.graphql_endpoint, json=payload, headers=headers)
        response.raise_for_status()
        
        return response.json()
