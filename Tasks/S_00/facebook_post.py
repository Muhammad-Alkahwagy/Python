import requests

# Set the access token and post content
access_token = 'YOUR_ACCESS_TOKEN'
post_content = 'Hello, Facebook!'

# Define the URL for the Graph API endpoint
url = f'https://graph.facebook.com/me/feed'

# Define the payload for the POST request
payload = {
    'message': post_content,
    'access_token': access_token
}

# Send the POST request to Facebook using the requests library
response = requests.post(url, data=payload)

# Check if the POST request was successful
if response.status_code == requests.codes.ok:
    print('Post successful!')
else:
    print('Post unsuccessful.')