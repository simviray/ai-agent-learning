import requests

url = "https://api.coinbase.com/v2/prices/spot?currency=USD"

response = requests.get(url)

data = response.json()

btc_price = float(data["data"]["amount"])

print("Current BTC Price:", btc_price)

if btc_price >= 100000:
    print("Market Status: Bullish")

else:
    print("Market Status: Neutral")