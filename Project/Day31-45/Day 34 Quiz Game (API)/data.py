import requests
API = "https://opentdb.com/api.php?amount=10&type=boolean"
response = requests.get(
    url=API)


data = response.json()
question_data = data["results"]
