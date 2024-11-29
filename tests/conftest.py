import pytest
from api_clients.rest_client import RestClient
from api_clients.graphql_client import GraphQLClient
from config.settings import BASE_URL, ADMIN_USERNAME, ADMIN_PASSWORD

@pytest.fixture(scope="session")
def rest_client():
    return RestClient(BASE_URL, ADMIN_USERNAME, ADMIN_PASSWORD)

@pytest.fixture(scope="session")
def graphql_client(rest_client):
    return GraphQLClient(BASE_URL, rest_client)
