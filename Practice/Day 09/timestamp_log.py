# Import datetime for timestamps
from datetime import datetime

# Create a readable timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Open the log file in append mode
with open("./Day 09/activity_log.txt", "a") as log_file:

    # Save activity with timestamp
    log_file.write(f"{timestamp} - AI agent started.\n")

# Print confirmation
print("Activity saved to activity_log.txt")