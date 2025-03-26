import requests
from requests.auth import HTTPBasicAuth
import json

# Confluence credentials and URL
confluence_url = 'https://your-confluence-instance.atlassian.net/wiki/rest/api/content'
username = 'your-email@example.com'
api_token = 'your-api-token'

# Page data
page_title = 'Your Page Title'
space_key = 'YOURSPACEKEY'
page_content = '<h1>This is a heading</h1><p>This is a paragraph.</p>'

# Create the payload
payload = {
    'type': 'page',
    'title': page_title,
    'space': {'key': space_key},
    'body': {
        'storage': {
            'value': page_content,
            'representation': 'storage'
        }
    }
}

# Make the request
response = requests.post(
    confluence_url,
    data=json.dumps(payload),
    auth=HTTPBasicAuth(username, api_token),
    headers={'Content-Type': 'application/json'}
)

# Check the response
if response.status_code == 200:
    print('Page created successfully.')
else:
    print(f'Failed to create page. Status code: {response.status_code}')
    print(response.json())