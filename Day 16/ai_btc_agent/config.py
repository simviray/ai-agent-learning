# Import os to read environment variables
import os

# Import Path to manage file and folder paths
from pathlib import Path

# Import load_dotenv to load .env settings
from dotenv import load_dotenv

# Load .env file settings
load_dotenv()

# Get the current project folder
PROJECT_FOLDER = Path(__file__).parent

# Create logs folder path
LOGS_FOLDER = PROJECT_FOLDER / "logs"

# Create logs folder if it does not exist
LOGS_FOLDER.mkdir(exist_ok=True)

# Create log file paths
TRADE_MEMORY_FILE = LOGS_FOLDER / "trade_memory.txt"
ERROR_LOG_FILE = LOGS_FOLDER / "error_log.txt"

# Read scan settings from .env
SCAN_LIMIT = int(os.getenv("SCAN_LIMIT", 5))
SCAN_DELAY = int(os.getenv("SCAN_DELAY", 5))

# Centralized asset configuration
ASSETS = [
    {
        # Asset name
        "name": "BTC",

        # API URL from .env
        "api_url": os.getenv("BTC_API_URL"),

        # Decision levels from .env
        "strong_buy_level": float(os.getenv("BTC_STRONG_BUY_LEVEL", 110000)),
        "buy_level": float(os.getenv("BTC_BUY_LEVEL", 100000)),
        "hold_level": float(os.getenv("BTC_HOLD_LEVEL", 90000))
    },
    {
        # Asset name
        "name": "ETH",

        # API URL from .env
        "api_url": os.getenv("ETH_API_URL"),

        # Decision levels from .env
        "strong_buy_level": float(os.getenv("ETH_STRONG_BUY_LEVEL", 3500)),
        "buy_level": float(os.getenv("ETH_BUY_LEVEL", 3000)),
        "hold_level": float(os.getenv("ETH_HOLD_LEVEL", 2500))
    },
    {
        # Asset name
        "name": "SOL",

        # API URL from .env
        "api_url": os.getenv("SOL_API_URL"),

        # Decision levels from .env
        "strong_buy_level": float(os.getenv("SOL_STRONG_BUY_LEVEL", 220)),
        "buy_level": float(os.getenv("SOL_BUY_LEVEL", 180)),
        "hold_level": float(os.getenv("SOL_HOLD_LEVEL", 140))
    },
        {
        # Asset name
        "name": "XRP",

        # API URL from .env
        "api_url": os.getenv("XRP_API_URL"),

        # XRP decision levels from .env
        "strong_buy_level": float(os.getenv("XRP_STRONG_BUY_LEVEL", 3.00)),
        "buy_level": float(os.getenv("XRP_BUY_LEVEL", 2.50)),
        "hold_level": float(os.getenv("XRP_HOLD_LEVEL", 2.00))
    }
]