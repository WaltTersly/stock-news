import requests
import smtplib

STOCK_NAME = "SHOP"
COMPANY_NAME = "Shopify Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API = "NMFDYDX0P5Y3R70I"
NEWS_API = "4d6ad2de694f494e806f34b48281bcbe"

MY_EMAIL = "terslyparadise@gmail.com"
PASSWORD = "ndkabesfainbdzxo"

stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol" : STOCK_NAME,
    "apikey" : STOCK_API,
}

new_parameters = {
    "q" : COMPANY_NAME,
    "apiKey" : NEWS_API,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_closing_price = data_list[0]["4. close"]
print(yesterday_closing_price)


day_before_yesterday_clos_price = data_list[1]["4. close"]
print(day_before_yesterday_clos_price)

diff = float(yesterday_closing_price) - float(day_before_yesterday_clos_price)
up_down = None
if diff > 0:
    up_down = "⬆️"
else:
    up_down = "⬇️"

print(diff)

diff_percent = round((diff / float(yesterday_closing_price)) * 100)
print(diff_percent)

if abs(diff_percent) > 1:
    print("Get News")
    news_response = requests.get(NEWS_ENDPOINT, params=new_parameters)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

    # print(three_articles)

    formatted_articles = [f"{STOCK_NAME}: {up_down} {diff_percent}% \n Headlines: {article['title']}.\n Brief: {article['description']}" for article in three_articles]
    
    for article in formatted_articles:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user = MY_EMAIL, password = PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject: Stocks.\n\n{article}".encode()
            )