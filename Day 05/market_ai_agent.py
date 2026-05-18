import requests

url = "https://api.coinbase.com/v2/prices/spot?currency=USD"

response = requests.get(url)

data = response.json()

btc_price = float(data["data"]["amount"])

print("BTC Price:", btc_price)

def market_agent(price):

    if price >= 110000:
        return "Strong Buy"

    elif price >= 100000:
        return "Buy"

    elif price >= 90000:
        return "Hold"

    else:
        return "Risk Zone"

decision = market_agent(btc_price)

print("AI Agent Decision:", decision)