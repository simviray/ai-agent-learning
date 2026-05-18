# Import required libraries
import requests
import time

# Repeat monitoring 5 times
for i in range(5):

    # API endpoint for BTC price
    url = "https://api.coinbase.com/v2/prices/spot?currency=USD"

    # Request BTC data
    response = requests.get(url)

    # Convert response into JSON
    data = response.json()

    # Extract BTC price
    btc_price = float(data["data"]["amount"])

    # Print BTC price
    print("BTC Price:", btc_price)

    # AI decision logic
    if btc_price >= 110000:
        print("AI Decision: Strong Buy")

    elif btc_price >= 100000:
        print("AI Decision: Buy")

    elif btc_price >= 90000:
        print("AI Decision: Hold")

    else:
        print("AI Decision: Risk Zone")

    # Print separator line
    print("----------------------")

    # Wait 5 seconds before checking again
    time.sleep(5)

print("Monitoring session completed.")
