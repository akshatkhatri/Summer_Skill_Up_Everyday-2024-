#!/usr/bin/env python3
import requests
import sys
import json

response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term="+sys.argv[1])
data=response.json()


# print(json.dumps(data,indent=4))

for result in data["results"]:
    print(result["trackName"])

    