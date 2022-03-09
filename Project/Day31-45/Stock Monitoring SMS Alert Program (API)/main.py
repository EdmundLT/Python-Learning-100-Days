import requests
from send_message import send_message
import datetime as dt
from find_news import find_news
import os
from twilio.rest import Client

current = dt.datetime.now()
year = current.year
day = current.day
# day = 18
month = f"0{current.month}"

today = f"{year}-{month}-{day}"
ytd = f"{year}-{month}-{day - 1}"
two_day_before = f"{year}-{month}-{day - 2}"
# print(ytd)


STOCK = "PLTR"
COMPANY_NAME = "Palantir"

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
alpha_api_key = "KQUWJE2YFL4XGJ4W"
api_endpoint = "https://www.alphavantage.co/query"
params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "datatype": "json",
    "apikey": alpha_api_key,
}

response = requests.get(url=api_endpoint, params=params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
send_news = False
difference = float(yesterday_closing_price) - \
    float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round((difference / float(yesterday_closing_price)) * 100)


# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
if abs(diff_percent) > 1:
    api_key = "9c55f33aa64d40dcb9535cdc9472fb4e"
    api_endpoint = "https://newsapi.org/v2/everything"
    params = {
        "q": COMPANY_NAME,
        "apikey": api_key,
        "language": "en",
        "from": "2022-02-21",
        "to": "2022-02-21"
    }

    response = requests.get(url=api_endpoint, params=params)
    response.raise_for_status()
    data = response.json()
    for x in range(0, 3):
        news_title = data["articles"][x]["title"]
        news_content = data["articles"][x]["content"]

        # STEP 3: Use https://www.twilio.com
        # Send a seperate message with the percentage change and each article's title and description to your phone number.

        account_sid = os.environ.get("AC_SID")
        auth_token = os.environ.get("AUTH_TOKEN")

        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
                body=f"{STOCK} {up_down}{diff_percent}%\n\ntitle: {news_title}\n\ncontent: {news_content}",
                from_='+19036647114',
                to='+14379894416'
            )
        print(message.status)


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
