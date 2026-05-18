# Day 12 — Project Folders, Multiple Files, and Cleaner AI Agent Architecture

## Goal for Today

Learn how to organize your AI agent project into multiple files instead of one long script.

Today you will learn:

* project folders
* Python modules
* separating config, tools, and main logic
* cleaner AI architecture

Estimated time: **2.5–3 hours**

---

# PART 1 — Review Day 11

Run:

```bash
python config_btc_agent.py
```

Make sure you have:

```text
.env
logs/
config_btc_agent.py
```

---

# Concept Explanation — Why Split Code Into Multiple Files?

One big Python file becomes hard to manage.

Professional AI projects separate code by responsibility:

```text
config.py        → settings
market_data.py   → API data
agent_logic.py   → decisions
logger.py        → logs
main.py          → runs the app
```

This makes your project:

* easier to debug
* easier to reuse
* easier to expand
* more professional

---

# PART 2 — Create This Project Structure

Create:

```text
ai_btc_agent/
│
├── .env
├── main.py
├── config.py
├── market_data.py
├── agent_logic.py
├── logger.py
└── logs/
```

---

# PART 3 — `.env`

Create:

```text
.env
```

Add:

```text
SCAN_LIMIT=5
SCAN_DELAY=5

BTC_BUY_LEVEL=100000
BTC_STRONG_BUY_LEVEL=110000
BTC_HOLD_LEVEL=90000

BTC_API_URL=https://api.coinbase.com/v2/prices/spot?currency=USD
```

---

# PART 4 — `config.py`

Create:

```text
config.py
```

Code:

```python
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
    "https://api.coinbase.com/v2/prices/spot?currency=USD"
)
```

---

# Concept Explanation — `config.py`

`config.py` is the control center for settings.

It stores:

* scan limit
* scan delay
* price thresholds
* API URL
* log file paths

This prevents your settings from being scattered everywhere.

---

# PART 5 — `market_data.py`

Create:

```text
market_data.py
```

Code:

```python
# Import requests to call web APIs
import requests

# Import BTC_API_URL from config file
from config import BTC_API_URL

# Function to retrieve BTC price
def get_btc_price():

    # Request BTC price data using API URL from config
    response = requests.get(BTC_API_URL, timeout=10)

    # Raise error if API request fails
    response.raise_for_status()

    # Convert API response into JSON
    data = response.json()

    # Extract BTC price from JSON response
    btc_price = float(data["data"]["amount"])

    # Return BTC price to the main program
    return btc_price
```

---

# Concept Explanation — `market_data.py`

This file has ONE job:

```text
Get market data.
```

Later, you can add:

* ETH price
* SOL price
* stock prices
* forex prices
* news data

This is professional separation of responsibility.

---

# PART 6 — `agent_logic.py`

Create:

```text
agent_logic.py
```

Code:

```python
# Import price threshold settings from config
from config import (
    BTC_BUY_LEVEL,
    BTC_STRONG_BUY_LEVEL,
    BTC_HOLD_LEVEL
)

# Function for AI market decision
def market_agent(price):

    # Strong Buy condition
    if price >= BTC_STRONG_BUY_LEVEL:
        return "Strong Buy"

    # Buy condition
    elif price >= BTC_BUY_LEVEL:
        return "Buy"

    # Hold condition
    elif price >= BTC_HOLD_LEVEL:
        return "Hold"

    # Risk Zone condition
    else:
        return "Risk Zone"
```

---

# Concept Explanation — `agent_logic.py`

This file controls the decision logic.

It answers:

```text
What should the AI agent decide based on the price?
```

Later, this file can include:

* RSI logic
* moving averages
* AI model predictions
* risk management
* confidence score

---

# PART 7 — `logger.py`

Create:

```text
logger.py
```

Code:

```python
# Import datetime to create timestamps
from datetime import datetime

# Import log file paths from config
from config import TRADE_MEMORY_FILE, ERROR_LOG_FILE

# Function to create readable timestamp
def get_timestamp():

    # Return current date and time
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Function to save successful trade monitoring records
def save_trade_memory(scan_number, timestamp, btc_price, decision):

    # Open trade memory file safely in append mode
    with open(TRADE_MEMORY_FILE, "a") as memory_file:

        # Save scan details
        memory_file.write(f"Scan Number: {scan_number}\n")
        memory_file.write(f"Timestamp: {timestamp}\n")
        memory_file.write(f"BTC Price: {btc_price}\n")
        memory_file.write(f"Decision: {decision}\n")
        memory_file.write("----------------------\n")

# Function to save error records
def save_error_log(error):

    # Create timestamp for the error
    timestamp = get_timestamp()

    # Get error type name
    error_type = type(error).__name__

    # Get readable error message
    error_message = str(error)

    # Open error log file safely in append mode
    with open(ERROR_LOG_FILE, "a") as error_file:

        # Save error details
        error_file.write(f"Timestamp: {timestamp}\n")
        error_file.write(f"Error Type: {error_type}\n")
        error_file.write(f"Message: {error_message}\n")
        error_file.write("----------------------\n")
```

---

# Concept Explanation — `logger.py`

This file handles memory and logs.

It saves:

* successful scans
* BTC price
* AI decision
* errors
* timestamps

In professional systems, logging is separated from the main logic.

---

# PART 8 — `main.py`

Create:

```text
main.py
```

Code:

```python
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
```

Run:

```bash
python main.py
```

---

# Concept Explanation — `main.py`

`main.py` is the entry point.

It does not do everything itself.

Instead, it calls other modules:

```text
config.py        → settings
market_data.py   → gets BTC price
agent_logic.py   → makes decision
logger.py        → saves records
```

This is how professional apps are structured.

---

# DAY 12 CHECKLIST

## Concepts Understood

* [ ] Multi-file project
* [ ] Modules
* [ ] Imports
* [ ] Separation of responsibility
* [ ] Entry point
* [ ] Cleaner architecture

## Coding

* [ ] `.env`
* [ ] `config.py`
* [ ] `market_data.py`
* [ ] `agent_logic.py`
* [ ] `logger.py`
* [ ] `main.py`

---

# What You Learned Today

Today you upgraded from:

```text
One large script
```

to:

```text
A professional multi-file project
```

This is a big step toward building:

* AI agents
* trading bots
* Azure apps
* FastAPI backends
* enterprise AI systems

---

# Bonus Task

Add a file called:

```text
README.md
```

Write:

* project name
* purpose
* how to install dependencies
* how to run the project
* what each file does
