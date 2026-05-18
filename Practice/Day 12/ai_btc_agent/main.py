# Import time to create delay between scans
import time

# Import settings from config
from config import SCAN_LIMIT, SCAN_DELAY

# Import market data function
from market_data import get_btc_price

# Import AI decision function
from agent_logic import market_agent

# Import logging functions
from logger import get_timestamp, save_trade_memory, save_error_log

# Main monitoring loop
for scan in range(1, SCAN_LIMIT + 1):

    try:
        # Get current BTC price
        btc_price = get_btc_price()

        # Get AI market decision
        decision = market_agent(btc_price)

        # Create timestamp
        timestamp = get_timestamp()

        # Save scan result into trade memory
        save_trade_memory(scan, timestamp, btc_price, decision)

        # Print results to terminal
        print(f"Scan Number: {scan}")
        print("Timestamp:", timestamp)
        print("BTC Price:", btc_price)
        print("AI Decision:", decision)

    except Exception as error:

        # Save error details into error log
        save_error_log(error)

        # Print safe message
        print("Error logged safely.")

    # Print separator
    print("----------------------")

    # Wait before next scan
    time.sleep(SCAN_DELAY)

# Print completion message
print("Multi-file AI BTC agent completed.")