from datetime import datetime
import requests
import os
APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
end_point = "https://www.nutritionix.com/v2/search/instant"
post_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

response = requests.get(url=end_point, headers=headers)
# print(response.text)
exercise_text = input("Tell me what you did: ")
params = {
    "query": exercise_text,
    "gender": "male",
    "weight_kg": 75,
    "height_cm": 178,
    "age": 25,
}
response = requests.post(url=post_endpoint, headers=headers, json=params)
data = response.json()

duration_min = data["exercises"][0]["duration_min"]
calories = data["exercises"][0]["nf_calories"]
exercise = data["exercises"][0]["name"].title()
sheety_endpoint = "https://api.sheety.co/aceda77c6ffdf979bd550c41b57ceb96/myWorkouts/workouts"
data = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise,
        "duration": duration_min,
        "calories": calories
    }
}
response = requests.post(url=sheety_endpoint, headers=headers, json=data)
print(response.json())
