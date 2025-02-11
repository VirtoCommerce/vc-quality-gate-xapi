import pytest
from queries.search_products import SearchProductsQuery


def test_search_products(graphql_client):
    """Test the SearchProducts query."""
    query = SearchProductsQuery()
    response = query.execute(graphql_client)

    # Assertions to validate the response
    assert "data" in response, "Response missing 'data' field"
    assert "products" in response["data"], "Response missing 'products' field"
    assert response["data"]["products"]["totalCount"] > 0, "No products found"
    assert len(response["data"]["products"]["items"]) > 0, "No items in products"

    # Example: Check the first product's fields
    first_product = response["data"]["products"]["items"][0]
    assert "name" in first_product, "First product missing 'name'"
    assert "id" in first_product, "First product missing 'id'"
    assert "code" in first_product, "First product missing 'code'"


