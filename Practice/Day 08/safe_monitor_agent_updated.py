# Import required libraries
import requests
import time
from datetime import datetime
from pathlib import Path

# Save error_log.txt in the same folder where this Python file is located
error_log_file = Path(__file__).parent / "error_log.txt"


# Function to save errors into error_log.txt
def log_error(error):
    # Get the current date and time
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Get the error type, such as ConnectionError or HTTPError
    error_type = type(error).__name__

    # Get the failure message
    failure_message = str(error)

    # Save error details into error_log.txt
    with open(error_log_file, "a") as file:
        file.write(f"Timestamp: {timestamp}\n")
        file.write(f"Error Type: {error_type}\n")
        file.write(f"Failure Message: {failure_message}\n")
        file.write("----------------------\n")


# Repeat monitoring 5 times
for i in range(5):

    # TRY the monitoring workflow
    try:

        # API endpoint
        url = "1https://api.coinbase.com/v2/prices/spot?currency=USD"

        # Request BTC data with a timeout so the program does not hang
        response = requests.get(url, timeout=10)

        # Raise an error if the API request failed
        response.raise_for_status()

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
    except Exception as error:

        # Print failure message
        print("Error retrieving market data.")

        # Save timestamp, error type, and failure message into error_log.txt
        log_error(error)

    # Print separator
    print("----------------------")

    # Wait 5 seconds
    time.sleep(5)

print("Monitoring completed.")
print("Error log location:", error_log_file)