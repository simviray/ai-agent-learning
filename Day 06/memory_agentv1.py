from datetime import datetime
import requests
from pathlib import Path

# Save trade_memory.txt in the same folder where this Python file is located
memory_file = Path(__file__).parent / "trade_memory.txt"

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
with open(memory_file, "a") as memory:
    memory.write(f"Timestamp: {timestamp}\n")
    memory.write(f"BTC Price: {btc_price}\n")
    memory.write(f"Decision: {decision}\n")
    memory.write("----------------------\n")

print("AI Agent Decision:", decision)
print("Memory stored successfully.")
print("Saved file location:", memory_file)