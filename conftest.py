import pytest
from api_clients.rest_client import RestClient
from api_clients.graphql_client import GraphQLClient
from config.settings import (
    BASE_URL,
    ADMIN_USERNAME,
    ADMIN_PASSWORD,
    AUTH_TOKEN
)

@pytest.fixture(scope="session")
def rest_client():
    client = RestClient(BASE_URL)
    try:
        # Use AUTH_TOKEN if available, otherwise authenticate with credentials
        if AUTH_TOKEN:
            client.set_auth_token(AUTH_TOKEN)
        else:
            client.authenticate(ADMIN_USERNAME, ADMIN_PASSWORD)
    except Exception as e:
        pytest.fail(f"Failed to initialize RestClient: {e}")
    return client

@pytest.fixture(scope="session")
def graphql_client(rest_client):
    return GraphQLClient(rest_client.base_url, rest_client)
