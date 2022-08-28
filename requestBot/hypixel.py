import requests
import json 

data = requests.get(
    url = "https://api.hypixel.net/player",
    params = {
        "key": "fcabbf30-6a54-4c9d-af6c-6dcbee1a4245",
        "uuid": "ff5476d1-0369-4e47-9102-c673e3ad7705"
    }
).json()

with open('requestBot/hypixeldata.json', "w") as f:
    json.dump(data, f)

skywars_coins = data["player"]["stats"]["SkyWars"]["coins"]

print (skywars_coins)