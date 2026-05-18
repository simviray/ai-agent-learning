# Import required libraries
import requests

# TRY running the API workflow
try:

    # API endpoint
    url = "https://api.coinbase.com/v2/prices/spot?currency=USD"

    # Request BTC data
    response = requests.get(url)

    # Convert response into JSON
    data = response.json()

    # Extract BTC price
    btc_price = float(data["data"]["amount"])

    # Print BTC price
    print("BTC Price:", btc_price)

# Handle errors safely
except:

    # Print error message
    print("Failed to retrieve BTC data.")