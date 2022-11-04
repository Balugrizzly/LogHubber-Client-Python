import requests
import json

base_url = "http://127.0.0.1:3000/"
headers = {"Content-Type": "application/json"}


payload = json.dumps(
    {
        "Level": "INFO",
        "Timestamp": 1667256058,
        "Log": "Failed in main",
        "Project": "Boat",
        "App": "Website",
        "Client": "Cron job background task",
    }
)

url = base_url + "log"
response = requests.post(url, data={"Level": "INFO"})


print(response.text)
