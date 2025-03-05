import pytest
from api_clients.rest_client import RestClient
from api_clients.graphql_client import GraphQLClient
from dotenv import load_dotenv
import os

load_dotenv()


@pytest.fixture(scope="session")
def rest_client():
    # Get credentials from environment variables
    BASE_URL = os.getenv("BASE_URL", "https://vcst-qa-storefront.govirto.com")        
    ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin")
    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "Password3")
    AUTH_TOKEN = os.getenv("ADMIN_TOKEN", "")


    # Validate required environment variables
    if not BASE_URL:
        pytest.fail("BASE_URL environment variable is required")
    if not (AUTH_TOKEN or (ADMIN_USERNAME and ADMIN_PASSWORD)):
        pytest.fail("Either ADMIN_TOKEN or both ADMIN_USERNAME and ADMIN_PASSWORD must be provided")

    # Initialize REST client
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
    """
    Creates a GraphQL client using the authenticated REST client's base URL and credentials
    """
    return GraphQLClient(rest_client.base_url, rest_client)
