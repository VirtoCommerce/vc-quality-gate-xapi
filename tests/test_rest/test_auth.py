def test_authenticate(rest_client):
    token = rest_client.get_headers()["Authorization"]
    assert token, "Failed to fetch token"
