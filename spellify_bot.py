import requests
from datetime import date

# Replace this with your Discord webhook URL
WEBHOOK_URL = "https://discord.com/api/webhooks/1479293649228398744/S45_XadqL_5uoLttf6unV5SLPJo59mza4tSJUwwkefmJA0HjkM1bNT8-inNL2J2jU5ii"

SPELLIFY_URL = "https://edhrec.com/spellify"

message = f"🧙‍♂️ Today's Spellify challenge ({date.today()}): {SPELLIFY_URL}"

data = {
    "content": message,
    "username": "Spellify Bot"
}

response = requests.post(WEBHOOK_URL, json=data)
if response.status_code == 204:
    print("Spellify link sent successfully!")
else:
    print(f"Error: {response.status_code} {response.text}")