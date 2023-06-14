import requests
import json 

data = requests.get(
    url = "https://api.hypixel.net/player",
    params = {
        #THESE ARE IN THE GITIGNORED FILE HYPIXELAPIKEY.PY
    }
).json()

with open('requestBot/hypixeldata.json', "w") as f:
    json.dump(data, f)

skywars_coins = data["player"]["stats"]["SkyWars"]["coins"]

print(data)
print (skywars_coins)