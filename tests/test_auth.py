import pytest

def test_authentication(rest_client):
    headers = rest_client.get_headers()
    assert "Authorization" in headers
    assert rest_client.token is not None



