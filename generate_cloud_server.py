import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the token and URL from the environment variable
token = os.getenv('TOKEN')
url = os.getenv('URL')

# variables for server inputs:
# Ubuntu 20.04 - '48', Ubuntu 22.04 - '65'
distributionId = "65"
zoneId = "1"
# Ubuntu 2VCPU, 1,2,4,8GB RAM: Micro, Small, Medium, Large
sizeId = "Micro" 
tag = "test4"

# if token:
#     print("Token retrieved successfully!")
#     print(f"Your token is: {url}")
# else:
#     print("Token not found. Please check your .env file.")

# Define the headers
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:133.0) Gecko/20100101 Firefox/133.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token}',
    'apollographql-client-name': 'learn-production',
    'apollographql-client-version': '3053',
    'Origin': 'https://learn.acloud.guru',
    'Connection': 'keep-alive',
    'Referer': 'https://learn.acloud.guru/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'Priority': 'u=0',
    'TE': 'trailers'
}

# Define the data payload
data = {
    "operationName": "CloudServers_provisionServerInstance",
    "variables": {
        "input": {
            "distributionId": "65",
            "zoneId": "1",
            "sizeId": "Micro",
            "tag": "test"
        }
    },
    "query": """
    mutation CloudServers_provisionServerInstance($input: CloudServers_ProvisionServerInstanceInput!) {
      CloudServers_provisionServerInstance(input: $input) {
        CloudServers_myServers {
          id
          instances {
            id
            distribution
            tag
            units
            credentials {
              username
              password
              __typename
            }
            ip {
              privateIPv4
              publicIPv4
              IPv6
              __typename
            }
            hostname
            status
            logs {
              id
              status
              message
              label
              occurredAt
              __typename
            }
            availableCommands {
              id
              commandId
              label
              __typename
            }
            activeCommandStatus
            volumes {
              id
              volumeId
              state
              path
              __typename
            }
            expiresAt
            shutdownAt
            terminalUrl
            __typename
          }
          selectedZone {
            id
            name
            __typename
          }
          unitUtilization {
            current
            available
            max
            __typename
          }
          __typename
        }
        __typename
      }
    }
    """
}

# Make the POST request
response = requests.post(url, headers=headers, json=data)

# Print the response
print(response.status_code)
print(response.json())
