import requests
news_dict = {}


def find_news():
    global news_dict
    api_key = "9c55f33aa64d40dcb9535cdc9472fb4e"
    api_endpoint = "https://newsapi.org/v2/everything"
    params = {
        "q": "Palantir",
        "apikey": api_key,
        "language": "en",
        "from": "2022-02-21",
        "to": "2022-02-21"
    }

    response = requests.get(url=api_endpoint, params=params)
    response.raise_for_status()
    data = response.json()

    news_title = data["articles"][0]["title"]
    news_content = data["articles"][0]["content"]
    return news_content
