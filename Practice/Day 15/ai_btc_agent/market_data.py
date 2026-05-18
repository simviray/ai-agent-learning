# Import requests to call APIs
import requests

# Function to get crypto price from any API URL
def get_crypto_price(api_url):

    # Send request to API
    response = requests.get(api_url, timeout=10)

    # Raise error if API request fails
    response.raise_for_status()

    # Convert API response to JSON
    data = response.json()

    # Extract price from Coinbase response
    price = float(data["data"]["amount"])

    # Return price
    return price