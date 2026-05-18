# Import required libraries
import requests
import time
from datetime import datetime
from pathlib import Path

# Save trade_memory.txt AND error_log.txt
# in the same folder where this Python file is located
trade_memory_file = Path(__file__).parent / "trade_memory.txt"
error_log_file = Path(__file__).parent / "error_log.txt"

# Function to create timestamp
def get_timestamp():

    # Return readable timestamp
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Function to retrieve BTC price
def get_btc_price():

    # Coinbase API endpoint
    url = "https://api.coinbase.com/v2/prices/spot?currency=USD"

    # Request BTC price data
    response = requests.get(url, timeout=10)

    # Raise error if request fails
    response.raise_for_status()

    # Convert API response to JSON
    data = response.json()

    # Extract BTC price
    btc_price = float(data["data"]["amount"])

    # Return BTC price
    return btc_price

# Function for AI market decision
def market_agent(price):

    # Strong Buy condition
    if price >= 110000:
        return "Strong Buy"

    # Buy condition
    elif price >= 100000:
        return "Buy"

    # Hold condition
    elif price >= 90000:
        return "Hold"

    # Risk Zone condition
    else:
        return "Risk Zone"

# Function to save trade memory
def save_trade_memory(scan_number, timestamp, btc_price, decision):

    # Open trade memory file safely
    with open(trade_memory_file, "a") as memory_file:

        # Save scan details
        memory_file.write(f"Scan Number: {scan_number}\n")
        memory_file.write(f"Timestamp: {timestamp}\n")
        memory_file.write(f"BTC Price: {btc_price}\n")
        memory_file.write(f"Decision: {decision}\n")
        memory_file.write("----------------------\n")

# Function to save error logs
def save_error_log(error):

    # Create timestamp
    timestamp = get_timestamp()

    # Get error type
    error_type = type(error).__name__

    # Get error message
    error_message = str(error)

    # Open error log file safely
    with open(error_log_file, "a") as error_file:

        # Save error details
        error_file.write(f"Timestamp: {timestamp}\n")
        error_file.write(f"Error Type: {error_type}\n")
        error_file.write(f"Message: {error_message}\n")
        error_file.write("----------------------\n")

# Repeat monitoring 5 times
for scan in range(1, 6):

    try:

        # Get BTC price
        btc_price = get_btc_price()

        # Get AI decision
        decision = market_agent(btc_price)

        # Create timestamp
        timestamp = get_timestamp()

        # Save trade memory
        save_trade_memory(scan, timestamp, btc_price, decision)

        # Print monitoring details
        print(f"Scan Number: {scan}")
        print("Timestamp:", timestamp)
        print("BTC Price:", btc_price)
        print("AI Decision:", decision)

    except Exception as error:

        # Save error log
        save_error_log(error)

        # Print safe error message
        print("Error logged safely.")

    # Print separator
    print("----------------------")

    # Wait 5 seconds before next scan
    time.sleep(5)

# Print completion message
print("AI monitoring session completed.")