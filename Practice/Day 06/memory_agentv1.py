from datetime import datetime
import requests

url = "https://api.coinbase.com/v2/prices/spot?currency=USD"

response = requests.get(url)
data = response.json()

btc_price = float(data["data"]["amount"])

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

# Create timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Save to memory file
with open("trade_memory.txt", "a") as memory:
    memory.write(f"Timestamp: {timestamp}\n")
    memory.write(f"BTC Price: {btc_price}\n")
    memory.write(f"Decision: {decision}\n")
    memory.write("----------------------\n")

print("AI Agent Decision:", decision)
print("Memory stored successfully.")