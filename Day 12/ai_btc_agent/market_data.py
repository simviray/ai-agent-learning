# Import requests to call web APIs
import requests

# Import BTC_API_URL from config file
from config import BTC_API_URL

# Function to retrieve BTC price
def get_btc_price():

    # Request BTC price data using API URL from config
    response = requests.get(BTC_API_URL, timeout=10)

    # Raise error if API request fails
    response.raise_for_status()

    # Convert API response into JSON
    data = response.json()

    # Extract BTC price from JSON response
    btc_price = float(data["data"]["amount"])

    # Return BTC price to the main program
    return btc_price