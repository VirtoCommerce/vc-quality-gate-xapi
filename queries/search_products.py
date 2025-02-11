class SearchProductsQuery:
    def __init__(self):
        self.query = """
        query SearchProducts($storeId: String!, $userId: String!, $currencyCode: String!, 
                             $cultureName: String, $filter: String, $after: String, 
                             $first: Int, $sort: String, $query: String, $fuzzy: Boolean, 
                             $fuzzyLevel: Int, $productIds: [String], $withFacets: Boolean!, 
                             $withImages: Boolean!) {
          products(
            storeId: $storeId
            userId: $userId
            after: $after
            first: $first
            filter: $filter
            sort: $sort
            currencyCode: $currencyCode
            cultureName: $cultureName
            query: $query
            fuzzy: $fuzzy
            fuzzyLevel: $fuzzyLevel
            productIds: $productIds
          ) {
            totalCount
            items {
              name
              id
              code
            }
          }
        }
        """

        self.variables = {
            "storeId": "B2B-store",
            "userId": "13e898dd-ce4f-480d-9b7b-ce247cc97151",
            "cultureName": "en-US",
            "currencyCode": "USD",
            "sort": "name:asc",
            "withFacets": True,
            "withImages": True,
            "filter": "category.subtree:fc596540864a41bf8ab78734ee7353a3 price.USD:(0 TO) productfamilyid:d6bf6343-3a6b-4c25-a3e9-6bcb9a5d4279 is: product,variation",
            "first": 50,
            "after": "0"
        }

    def execute(self, client):
        return client.send_query(self.query, self.variables)
