import requests
from datetime import datetime

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

def check_stock():
  api_url = "https://www.alphavantage.co/query"
  api_key = "stock_api_key"
  parameters = {
    "function" : "TIME_SERIES_DAILY_ADJUSTED",
    "symbol" : STOCK,
    "apikey" : api_key
  }

  response = requests.get(url=api_url, params=parameters)
  response.raise_for_status()

  data = response.json()["Time Series (Daily)"]

  data_list  = [value for (key, value) in data.items()]
  yesterday_closing_price = float(data_list[0]["4. close"])
  day_before_closing_price = float(data_list[1]["4. close"])

  delta = abs(yesterday_closing_price - day_before_closing_price)
  percentage_diff = (delta / yesterday_closing_price) * 100
  # print(yesterday_closing_price)
  # print(day_before_closing_price)
  # print(delta)
  # print(percentage_diff)

  if percentage_diff > 5:
    return True
  return False

def get_news(stock_state):
  if stock_state:
    api_url = "https://newsapi.org/v2/everything"
    api_key = "news_api_key"
    parameters = {
      "qInTitle" : COMPANY_NAME,
      "apiKey" : api_key
    }

    response = requests.get(url=api_url, params=parameters)
    response.raise_for_status()

    news = response.json()["articles"]
    top_articles = news[:3]
    return top_articles

state = check_stock()
print(get_news(state))

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

