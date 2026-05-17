# Import libraries for API requests, time delays, and timestamps
import requests
import time
from datetime import datetime

# Function to create a timestamp
def get_timestamp():
    # Return current date and time as readable text
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Function to decide market status
def market_agent(price):
    # Strong buy condition
    if price >= 110000:
        return "Strong Buy"

    # Buy condition
    elif price >= 100000:
        return "Buy"

    # Hold condition
    elif price >= 90000:
        return "Hold"

    # Risk zone condition
    else:
        return "Risk Zone"

# Repeat monitoring 5 times
for i in range(5):

    # Create scan number for each monitoring cycle
    scan_number = i + 1

    try:
        # Coinbase BTC price API
        url = "https://api.coinbase.com/v2/prices/spot?currency=USD"

        # Request BTC data with timeout protection
        response = requests.get(url, timeout=10)

        # Raise an error if the API request failed
        response.raise_for_status()

        # Convert response to JSON
        data = response.json()

        # Extract BTC price
        btc_price = float(data["data"]["amount"])

        # Get AI decision
        decision = market_agent(btc_price)

        # Create timestamp
        timestamp = get_timestamp()

        # Save successful trade monitoring record
        with open("./Day 09/trade_memory.txt", "a") as memory_file:
            memory_file.write(f"Scan Number: {scan_number}\n")
            memory_file.write(f"Timestamp: {timestamp}\n")
            memory_file.write(f"BTC Price: {btc_price}\n")
            memory_file.write(f"Decision: {decision}\n")
            memory_file.write("----------------------\n")

        # Print result
        print("Scan Number:", scan_number)
        print("Timestamp:", timestamp)
        print("BTC Price:", btc_price)
        print("AI Decision:", decision)

    except Exception as error:
        # Create timestamp for the error
        timestamp = get_timestamp()

        # Get error type
        error_type = type(error).__name__

        # Get error message
        error_message = str(error)

        # Save error details
        with open("./Day 09/error_log.txt", "a") as error_file:
            error_file.write(f"Scan Number: {scan_number}\n")
            error_file.write(f"Timestamp: {timestamp}\n")
            error_file.write(f"Error Type: {error_type}\n")
            error_file.write(f"Message: {error_message}\n")
            error_file.write("----------------------\n")

        # Print safe error message
        print("Error saved to error_log.txt")

    # Print separator
    print("----------------------")

    # Wait 5 seconds before next check
    time.sleep(5)

# Print completion message
print("Monitoring session completed.")