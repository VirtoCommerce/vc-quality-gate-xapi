import requests
from api_clients.graphql_client import GraphQLClient
from config.settings import DEFAULT_HEADERS, BASE_URL, GRAPHQL_ENDPOINT

class RegistrationPage:
    def __init__(self, client):
        self.client = client
        self.mutation = '''
        # Define the mutation and variables
        mutation requestRegistration($command: InputRequestRegistrationType!) {
            requestRegistration(command: $command) {
         contact {
         firstName
         lastName
         middleName
         id
         status
         createdBy
         phoneNumber
         birthdate
         dynamicProperties {
           value
           name
         }
         address {
           city
           countryName
           line1
           regionName
         }
       }
       account {
         id
         username
         email
         status
         createdBy
       }
       result {
         succeeded
         errors {
           description
           parameter
           code
         }
       }
     }
   }
   '''
    variables = {
     "command": {
       "storeId": "B2B-store",
       "contact": {
         "firstName": "Waldo",
         "lastName": "Raynor",
         "phoneNumber": "337-232-7162",
         "middleName": "Vicente",
         "birthdate": "2021-11-25",
         "address": {
           "addressType": 2,
           "city": "New Rachellechester",
           "countryCode": "USA",
           "countryName": "United States",
           "email": "alivemenone@gmail.com",
           "firstName": "Maya",
           "lastName": "Wisoky",
           "line1": "1888, colgate dr",
           "name": "Steven Woodward 1888, colgate dr Thousand oaks California 91360 United States",
           "postalCode": "91360",
           "regionId": "CA",
           "regionName": "California"
         },
       },
       "account": {
         "username": "Giovanna.Murray",
         "password": "eXp1Z1qad",
         "email": "Laney_Yost3@yahoo.com"
       }
     }
   }

    # Set up the headers with the token
    headers = DEFAULT_HEADERS
    # Make the POST request
    response = requests.post(GRAPHQL_ENDPOINT, json={'query': mutation, 'variables': variables}, headers=headers)
    if response.status_code == 200:
       # Successful request
       data = response.json()
       print('Mutation executed successfully:')
       print(data)
    else:
       # Handle errors
       print(f'Failed to execute mutation: {response.status_code}')
       print(response.text)
    
    
    def request_registration(self, variables):
        return self.client.execute(self.mutation, variables)
