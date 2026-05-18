# Import required libraries
import os
import requests
import time
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the folder where this Python file exists
project_folder = Path(__file__).parent

# Create logs folder path
logs_folder = project_folder / "logs"

# Create logs folder automatically if it does not exist
# exist_ok=True prevents errors if folder already exists
logs_folder.mkdir(exist_ok=True)

# Create file paths inside logs folder
trade_memory_file = logs_folder / "trade_memory.txt"
error_log_file = logs_folder / "error_log.txt"

# Read settings from .env file

# Number of monitoring scans
SCAN_LIMIT = int(os.getenv("SCAN_LIMIT", 5))

# Delay between scans in seconds
SCAN_DELAY = int(os.getenv("SCAN_DELAY", 5))

# BTC price levels for AI decisions
BTC_BUY_LEVEL = float(os.getenv("BTC_BUY_LEVEL", 100000))
BTC_STRONG_BUY_LEVEL = float(os.getenv("BTC_STRONG_BUY_LEVEL", 110000))
BTC_HOLD_LEVEL = float(os.getenv("BTC_HOLD_LEVEL", 90000))

# Read BTC API URL from .env file
BTC_API_URL = os.getenv(
    "BTC_API_URL",
    "https://api.coinbase.com/v2/prices/spot?currency=USD"
)

# Function to create timestamp
def get_timestamp():

    # Return current date and time as readable text
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Function to retrieve BTC price
def get_btc_price():

    # Request BTC price data using API URL from .env
    response = requests.get(BTC_API_URL, timeout=10)

    # Raise error if request fails
    response.raise_for_status()

    # Convert API response into JSON
    data = response.json()

    # Extract BTC price from nested JSON
    btc_price = float(data["data"]["amount"])

    # Return BTC price
    return btc_price

# Function for AI market decision
def market_agent(price):

    # Strong Buy condition
    if price >= BTC_STRONG_BUY_LEVEL:
        return "Strong Buy"

    # Buy condition
    elif price >= BTC_BUY_LEVEL:
        return "Buy"

    # Hold condition
    elif price >= BTC_HOLD_LEVEL:
        return "Hold"

    # Risk Zone condition
    else:
        return "Risk Zone"

# Function to save trade memory
def save_trade_memory(scan_number, timestamp, btc_price, decision):

    # Open trade memory file safely in append mode
    with open(trade_memory_file, "a") as memory_file:

        # Save scan details into the file
        memory_file.write(f"Scan Number: {scan_number}\n")
        memory_file.write(f"Timestamp: {timestamp}\n")
        memory_file.write(f"BTC Price: {btc_price}\n")
        memory_file.write(f"Decision: {decision}\n")
        memory_file.write("----------------------\n")

# Function to save error logs
def save_error_log(error):

    # Create timestamp for the error
    timestamp = get_timestamp()

    # Get error type name
    error_type = type(error).__name__

    # Get readable error message
    error_message = str(error)

    # Open error log file safely
    with open(error_log_file, "a") as error_file:

        # Save error details into the file
        error_file.write(f"Timestamp: {timestamp}\n")
        error_file.write(f"Error Type: {error_type}\n")
        error_file.write(f"Message: {error_message}\n")
        error_file.write("----------------------\n")

# Main monitoring loop
# Repeat monitoring based on SCAN_LIMIT from .env
for scan in range(1, SCAN_LIMIT + 1):

    try:

        # Get current BTC price
        btc_price = get_btc_price()

        # Get AI market decision
        decision = market_agent(btc_price)

        # Create timestamp
        timestamp = get_timestamp()

        # Save monitoring result into trade memory
        save_trade_memory(
            scan,
            timestamp,
            btc_price,
            decision
        )

        # Print monitoring details to terminal
        print(f"Scan Number: {scan}")
        print("Timestamp:", timestamp)
        print("BTC Price:", btc_price)
        print("AI Decision:", decision)

    # Handle possible errors safely
    except Exception as error:

        # Save error details into error log
        save_error_log(error)

        # Print safe error message
        print("Error logged safely.")

    # Print separator line
    print("----------------------")

    # Wait before next monitoring scan
    time.sleep(SCAN_DELAY)

# Print completion message
print("Config-based AI monitoring session completed.")