import requests
import os
from twilio.rest import Client

account_sid = os.environ.get("AC_SID")
auth_token = os.environ.get("OWM_AUTH_TOKEN")


api_key = os.environ.get("OWM_API_KEY")

api = "https://api.openweathermap.org/data/2.5/onecall"

weather_params = {
    "lat": 43.653225,
    "lon": -79.383186,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}
response = requests.get(url=api, params=weather_params)
response.raise_for_status()
data = response.json()["hourly"][:12]
list_of_next_12hr = []
will_rain = False
for hour_data in data:
    condition_code = int(hour_data["weather"][0]["id"])
    if condition_code < 800:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="Join Earth's mightiest heroes. Like Kevin Bacon.",
            from_='+19036647114',
            to='+14379894416'
        )
    print(message.status)
