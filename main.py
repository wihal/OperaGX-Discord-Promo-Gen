import requests, json
from time import sleep

url = "https://api.discord.gx.games/v1/direct-fulfillment"

payload = {"partnerUserId": "ed5941bb5627375140a009235ea9779f86707a041cdab12e0cb2affb4addba96"}
headers = {
    "authority": "api.discord.gx.games",
    "content-type": "application/json",
    "origin": "https://www.opera.com",
    "referer": "https://www.opera.com/",
    "sec-ch-ua": '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0"
}

while True:
    response = requests.request("POST", url, json=payload, headers=headers)

    # create a new txt file in the same directory if not exist and adds the links
    if response.status_code == 200:
        with open("output.txt", "a") as f:
            f.write(f"https://discord.com/billing/partner-promotions/1180231712274387115/{json.loads(response.text.encode('utf8').decode('utf8')).get('token')}" + "\n")
    elif response.status_code == 429:
        break
    else:
        print("Request failed: ", response.text)
