import requests
import requests.auth
client_auth = requests.auth.HTTPBasicAuth('app code', 'secret key')
post_data = {"grant_type": "password", "username": "USER", "password": "PASSWORD"}
headers = {"User-Agent": "ChangeMeClient/0.1 by YourUserName"}
response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
token = response.json()
print(token)
