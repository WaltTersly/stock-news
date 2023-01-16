Asimple  stock news notifications .

It implements using twoi different Api's.
1. STOCK_ENDPOINT = "https://www.alphavantage.co/query" - for the stock ranges and market forecast.
2. NEWS_ENDPOINT = "https://newsapi.org/v2/everything" - For news articles on the various companies involved.

Then one sends the stocks optiions and the related news to the stocks via email using the smtplib module.