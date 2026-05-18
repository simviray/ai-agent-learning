# Import time for scan delay
import time

# Import settings from config
from config import (
    SCAN_LIMIT,
    SCAN_DELAY,
    BTC_API_URL,
    ETH_API_URL,
    SOL_API_URL,
    BTC_STRONG_BUY_LEVEL,
    BTC_BUY_LEVEL,
    BTC_HOLD_LEVEL,
    ETH_STRONG_BUY_LEVEL,
    ETH_BUY_LEVEL,
    ETH_HOLD_LEVEL,
    SOL_STRONG_BUY_LEVEL,
    SOL_BUY_LEVEL,
    SOL_HOLD_LEVEL
)

# Import reusable price function
from market_data import get_crypto_price

# Import reusable decision function
from agent_logic import market_agent

# Import logging functions
from logger import get_timestamp, save_trade_memory, save_error_log

# Create asset settings list
assets = [
    {
        "name": "BTC",
        "api_url": BTC_API_URL,
        "strong_buy_level": BTC_STRONG_BUY_LEVEL,
        "buy_level": BTC_BUY_LEVEL,
        "hold_level": BTC_HOLD_LEVEL
    },
    {
        "name": "ETH",
        "api_url": ETH_API_URL,
        "strong_buy_level": ETH_STRONG_BUY_LEVEL,
        "buy_level": ETH_BUY_LEVEL,
        "hold_level": ETH_HOLD_LEVEL
    },
    {
        "name": "SOL",
        "api_url": SOL_API_URL,
        "strong_buy_level": SOL_STRONG_BUY_LEVEL,
        "buy_level": SOL_BUY_LEVEL,
        "hold_level": SOL_HOLD_LEVEL
    }
]

# Main monitoring loop
for scan in range(1, SCAN_LIMIT + 1):

    # Print current scan number
    print(f"Scan Number: {scan}")

    # Loop through each asset
    for asset in assets:

        try:
            # Get asset price
            price = get_crypto_price(asset["api_url"])

            # Get AI decision
            decision = market_agent(
                price,
                asset["strong_buy_level"],
                asset["buy_level"],
                asset["hold_level"]
            )

            # Create timestamp
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
print("Multi-asset AI monitoring completed.")