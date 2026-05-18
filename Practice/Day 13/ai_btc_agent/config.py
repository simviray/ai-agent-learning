# Import os to read environment variables
import os

# Import Path to manage file and folder paths
from pathlib import Path

# Import load_dotenv to load .env file settings
from dotenv import load_dotenv

# Load settings from .env file
load_dotenv()

# Get the folder where this Python project exists
PROJECT_FOLDER = Path(__file__).parent

# Create logs folder path
LOGS_FOLDER = PROJECT_FOLDER / "logs"

# Create logs folder if it does not already exist
LOGS_FOLDER.mkdir(exist_ok=True)

# Create log file paths
TRADE_MEMORY_FILE = LOGS_FOLDER / "trade_memory.txt"
ERROR_LOG_FILE = LOGS_FOLDER / "error_log.txt"

# Read scan settings from .env
SCAN_LIMIT = int(os.getenv("SCAN_LIMIT", 5))
SCAN_DELAY = int(os.getenv("SCAN_DELAY", 5))

# Read BTC price level settings from .env
BTC_BUY_LEVEL = float(os.getenv("BTC_BUY_LEVEL", 100000))
BTC_STRONG_BUY_LEVEL = float(os.getenv("BTC_STRONG_BUY_LEVEL", 110000))
BTC_HOLD_LEVEL = float(os.getenv("BTC_HOLD_LEVEL", 90000))

# Read BTC API URL from .env
BTC_API_URL = os.getenv(
    "BTC_API_URL",
    "1https://api.coinbase.com/v2/prices/spot?currency=USD"
)