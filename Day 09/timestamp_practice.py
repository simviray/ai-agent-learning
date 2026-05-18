# Import datetime so we can create timestamps
from datetime import datetime

# Get the current date and time
current_time = datetime.now()

# Format the timestamp so it is easy to read
timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")

# Print the timestamp
print("Current Timestamp:", timestamp)