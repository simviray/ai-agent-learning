# Import os so Python can read environment variables
import os

# Import load_dotenv so Python can load the .env file
from dotenv import load_dotenv

# Load settings from the .env file
load_dotenv()

# Read SCAN_LIMIT from the .env file
scan_limit = os.getenv("SCAN_LIMIT")

# Read SCAN_DELAY from the .env file
scan_delay = os.getenv("SCAN_DELAY")

# Print the values
print("Scan Limit:", scan_limit)
print("Scan Delay:", scan_delay)