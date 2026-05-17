# Import required libraries
import requests
import time
from datetime import datetime
from pathlib import Path

# Save trade_memory.txt in the same folder where this Python file is located
memory_file = Path(__file__).parent / "trade_memory.txt"

# Function for AI decision logic
def market_agent(price):
    # If BTC price is 110,000 or higher
    if price >= 110000:
        return "Strong Buy"

    # If BTC price is 100,000 or higher
    elif price >= 100000:
        return "Buy"

    # If BTC price is 90,000 or higher
    elif price >= 90000:
        return "Hold"

    # If BTC price is below 90,000
    else:
        return "Risk Zone"


# Repeat monitoring 5 times
for i in range(5):

    # API endpoint for BTC price from Coinbase
    url = "https://api.coinbase.com/v2/prices/spot?currency=USD"

    # Request BTC data from the API
    response = requests.get(url)

    # Convert API response into JSON format
    data = response.json()

    # Extract BTC price from JSON data
    btc_price = float(data["data"]["amount"])

    # Get current date and time
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Get AI decision based on BTC price
    decision = market_agent(btc_price)

    # Print monitoring result in terminal
    print("Timestamp:", timestamp)
    print("BTC Price:", btc_price)
    print("AI Decision:", decision)
    print("----------------------")

    # Save monitoring result into trade_memory.txt
    with open(memory_file, "a") as memory:
        memory.write(f"Timestamp: {timestamp}\n")
        memory.write(f"BTC Price: {btc_price}\n")
        memory.write(f"AI Decision: {decision}\n")
        memory.write("----------------------\n")

    # Wait 5 seconds before checking BTC price again
    time.sleep(5)


# Print message when monitoring is done
print("Monitoring session completed.")
print("Trade memory saved successfully.")
print("Saved file location:", memory_file)