# Import os to read environment variables
import os

# Import Path to manage file and folder paths
from pathlib import Path

# Import load_dotenv to load .env settings
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get project folder
PROJECT_FOLDER = Path(__file__).parent

# Create logs folder
LOGS_FOLDER = PROJECT_FOLDER / "logs"

# Create logs folder if missing
LOGS_FOLDER.mkdir(exist_ok=True)

# Log file paths
TRADE_MEMORY_FILE = LOGS_FOLDER / "trade_memory.txt"
ERROR_LOG_FILE = LOGS_FOLDER / "error_log.txt"

# Scan settings
SCAN_LIMIT = int(os.getenv("SCAN_LIMIT", 5))
SCAN_DELAY = int(os.getenv("SCAN_DELAY", 5))

# API URLs
BTC_API_URL = os.getenv("BTC_API_URL")
ETH_API_URL = os.getenv("ETH_API_URL")
SOL_API_URL = os.getenv("SOL_API_URL")

# BTC decision levels
BTC_BUY_LEVEL = float(os.getenv("BTC_BUY_LEVEL", 100000))
BTC_STRONG_BUY_LEVEL = float(os.getenv("BTC_STRONG_BUY_LEVEL", 110000))
BTC_HOLD_LEVEL = float(os.getenv("BTC_HOLD_LEVEL", 90000))

# ETH decision levels
ETH_BUY_LEVEL = float(os.getenv("ETH_BUY_LEVEL", 3000))
ETH_STRONG_BUY_LEVEL = float(os.getenv("ETH_STRONG_BUY_LEVEL", 3500))
ETH_HOLD_LEVEL = float(os.getenv("ETH_HOLD_LEVEL", 2500))

# SOL decision levels
SOL_BUY_LEVEL = float(os.getenv("SOL_BUY_LEVEL", 180))
SOL_STRONG_BUY_LEVEL = float(os.getenv("SOL_STRONG_BUY_LEVEL", 220))
SOL_HOLD_LEVEL = float(os.getenv("SOL_HOLD_LEVEL", 140))