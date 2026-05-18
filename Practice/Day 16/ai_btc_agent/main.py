# Import time for scan delay
import time

# Import scan settings and centralized asset list
from config import SCAN_LIMIT, SCAN_DELAY, ASSETS

# Import reusable price function
from market_data import get_crypto_price

# Import reusable decision function
from agent_logic import market_agent

# Import logging functions
from logger import get_timestamp, save_trade_memory, save_error_log

# Main monitoring loop
for scan in range(1, SCAN_LIMIT + 1):

    # Print current scan number
    print(f"Scan Number: {scan}")

    # Loop through every asset inside ASSETS list
    for asset in ASSETS:

        try:
            # Get asset price using its API URL
            price = get_crypto_price(asset["api_url"])

            # Get AI decision using flexible levels
            decision = market_agent(
                price,
                asset["strong_buy_level"],
                asset["buy_level"],
                asset["hold_level"]
            )

            # Create timestamp for this scan
            timestamp = get_timestamp()

            # Save monitoring result
            save_trade_memory(
                scan,
                timestamp,
                asset["name"],
                price,
                decision
            )

            # Print result to terminal
            print("Timestamp:", timestamp)
            print("Asset:", asset["name"])
            print("Price:", price)
            print("AI Decision:", decision)

        except Exception as error:

            # Save error log
            save_error_log(error)

            # Print safe error message
            print(f"Error logged safely for {asset['name']}.")

        # Print asset separator
        print("----------------------")

    # Wait before next scan
    time.sleep(SCAN_DELAY)

# Print completion message
print("Scalable multi-asset AI monitoring completed.")