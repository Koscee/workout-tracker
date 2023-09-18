import os
import requests
from datetime import datetime

NIX_APP_ID = os.environ["NIX_APP_ID"]
NIX_API_KEY = os.environ["NIX_API_KEY"]
SHEETY_TOKEN = os.environ["SHEETY_TOKEN"]
SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

sheety_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}",
    "Content-Type": "application/json"
}

exercise_api_headers = {
    "x-app-id": NIX_APP_ID,
    "x-app-key": NIX_API_KEY
}

exercise_params = {
    "query": input("Tell me which exercise you did: ")
}

res = requests.post(url=exercise_endpoint, json=exercise_params, headers=exercise_api_headers)
res.raise_for_status()
exercises = res.json()["exercises"]
print(exercises)

now = datetime.now()
date_now = now.strftime("%d/%m/%Y")
time_now = now.strftime("%X")

for exercise in exercises:
    workout_body = {
        "workout": {
            "date": date_now,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    res = requests.post(url=SHEETY_ENDPOINT, json=workout_body, headers=sheety_headers)
    res.raise_for_status()
    print(res.text)
