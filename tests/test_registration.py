import pytest
from queries.registration import RegistrationPage

def test_request_registration(graphql_client):
    """Test the requestRegistration mutation."""
    registration_page = RegistrationPage()
    response = registration_page.request_registration(graphql_client)
    assert response['data']['requestRegistration']['result']['succeeded']
    print('Test passed!')

