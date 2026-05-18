# Import os for reading environment variables
import os

# Import load_dotenv for loading the .env file
from dotenv import load_dotenv

# Load .env settings
load_dotenv()

# Read SCAN_LIMIT as text, then convert it to integer
scan_limit = int(os.getenv("SCAN_LIMIT", 5))

# Read SCAN_DELAY as text, then convert it to integer
scan_delay = int(os.getenv("SCAN_DELAY", 5))

# Read BTC price levels as text, then convert them to float
buy_level = float(os.getenv("BTC_BUY_LEVEL", 100000))
strong_buy_level = float(os.getenv("BTC_STRONG_BUY_LEVEL", 110000))
hold_level = float(os.getenv("BTC_HOLD_LEVEL", 90000))

# Print converted values
print("Scan Limit:", scan_limit)
print("Scan Delay:", scan_delay)
print("Buy Level:", buy_level)
print("Strong Buy Level:", strong_buy_level)
print("Hold Level:", hold_level)