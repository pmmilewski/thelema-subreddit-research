import requests
import requests.auth
import json

headers = {"Authorization": "bearer ACTIVETOKEN", "User-Agent": "ChangeMeClient/0.1 by YourUserName"}
responses = list()
after = ""
not_finished = True
while not_finished:
    parameters = {"t": "all", "limit": 100, "after": after}
    response = requests.get("https://oauth.reddit.com/r/Thelema/new", headers=headers, params=parameters)
    responses.append(response.json())
    after = "t3_" + responses[-1]["data"]["children"][-1]["data"]["id"]
    if len(responses[-1]["data"]["children"])< 100:
        not_finished = False


with open('data.json', 'w') as outfile:
    json.dump(responses, outfile)
