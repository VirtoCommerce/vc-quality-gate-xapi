def test_fetch_products(graphql_client):
    query = '''
    query GetProducts($storeId: String!) {
        products(storeId: $storeId) {
            items {
                id
                name
            }
        }
    }
    '''
    variables = {"storeId": "B2B-store"}
    response = graphql_client.send_query(query, variables)
    assert "data" in response
    assert len(response["data"]["products"]["items"]) > 0, "No products found"
