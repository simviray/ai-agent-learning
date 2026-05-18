# Import trade memory file path from config
from config import TRADE_MEMORY_FILE

# Function to generate a simple report from trade_memory.txt
def generate_report():

    # Create counters for each decision type
    strong_buy_count = 0
    buy_count = 0
    hold_count = 0
    risk_zone_count = 0

    # Check if the trade memory file exists
    if not TRADE_MEMORY_FILE.exists():

        # Print message if no log file exists yet
        print("No trade memory file found yet.")

        # Stop the function
        return

    # Open the trade memory file safely
    with open(TRADE_MEMORY_FILE, "r") as memory_file:

        # Read all lines from the file
        lines = memory_file.readlines()

    # Loop through every line in the file
    for line in lines:

        # Count Strong Buy decisions
        if "Decision: Strong Buy" in line:
            strong_buy_count += 1

        # Count Buy decisions
        elif "Decision: Buy" in line:
            buy_count += 1

        # Count Hold decisions
        elif "Decision: Hold" in line:
            hold_count += 1

        # Count Risk Zone decisions
        elif "Decision: Risk Zone" in line:
            risk_zone_count += 1

    # Calculate total decisions
    total_decisions = (
        strong_buy_count
        + buy_count
        + hold_count
        + risk_zone_count
    )

    # Print report
    print("AI Agent Performance Report")
    print("---------------------------")
    print("Total Decisions:", total_decisions)
    print("Strong Buy:", strong_buy_count)
    print("Buy:", buy_count)
    print("Hold:", hold_count)
    print("Risk Zone:", risk_zone_count)

# Run the report function
generate_report()