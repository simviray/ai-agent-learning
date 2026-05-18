# Import datetime for timestamps
from datetime import datetime

# Import log file paths from config
from config import TRADE_MEMORY_FILE, LOGS_FOLDER

# Create report file path
REPORT_FILE = LOGS_FOLDER / "daily_report.txt"

# Function to create readable timestamp
def get_timestamp():

    # Return current date and time
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Function to generate and save report
def generate_daily_report():

    # Create decision counters
    strong_buy_count = 0
    buy_count = 0
    hold_count = 0
    risk_zone_count = 0

    # Check if trade memory exists
    if not TRADE_MEMORY_FILE.exists():

        # Save message if no data exists
        with open(REPORT_FILE, "a") as report_file:
            report_file.write("No trade memory file found yet.\n")

        # Stop function
        return

    # Open trade memory file
    with open(TRADE_MEMORY_FILE, "r") as memory_file:

        # Read all log lines
        lines = memory_file.readlines()

    # Count each decision type
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

    # Create timestamp
    timestamp = get_timestamp()

    # Save report
    with open(REPORT_FILE, "a") as report_file:

        # Write report details
        report_file.write(f"Report Timestamp: {timestamp}\n")
        report_file.write("AI Agent Daily Report\n")
        report_file.write("---------------------\n")
        report_file.write(f"Total Decisions: {total_decisions}\n")
        report_file.write(f"Strong Buy: {strong_buy_count}\n")
        report_file.write(f"Buy: {buy_count}\n")
        report_file.write(f"Hold: {hold_count}\n")
        report_file.write(f"Risk Zone: {risk_zone_count}\n")
        report_file.write("=====================\n")

    # Print confirmation
    print("Daily report saved to logs/daily_report.txt")

# Run the report
generate_daily_report()