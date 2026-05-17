# Import required libraries
import requests
import time

# Repeat monitoring 5 times
for i in range(5):

    # TRY the monitoring workflow
    try:

        # API endpoint
        url = "https://api.coinbase.com/v2/prices/spot?currency=USD"

        # Request BTC data
        response = requests.get(url)

        # Convert API response into JSON
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

    # Handle possible failures
    except:

        # Print failure message
        print("Error retrieving market data.")

    # Print separator
    print("----------------------")

    # Wait 5 seconds
    time.sleep(5)

print("Monitoring completed.")