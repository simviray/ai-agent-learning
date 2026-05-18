# Day 15 — Add ETH Monitoring and Build a Multi-Asset AI Agent

## Goal for Today

Upgrade your BTC agent into a **multi-asset monitoring agent**.

Today you will learn:

* how to monitor BTC and ETH,
* how to reuse functions,
* how to avoid duplicate code,
* and how to prepare your system for more assets later.

Estimated time: **2.5–3 hours**

---

# PART 1 — Update `.env`

Add ETH settings:

```text
BTC_API_URL=https://api.coinbase.com/v2/prices/spot?currency=USD
ETH_API_URL=https://api.coinbase.com/v2/prices/ETH-USD/spot

BTC_BUY_LEVEL=100000
BTC_STRONG_BUY_LEVEL=110000
BTC_HOLD_LEVEL=90000

ETH_BUY_LEVEL=3000
ETH_STRONG_BUY_LEVEL=3500
ETH_HOLD_LEVEL=2500

SCAN_LIMIT=5
SCAN_DELAY=5
```

---

# Concept Explanation — Multi-Asset Monitoring

Before, your agent monitored only:

```text
BTC
```

Now it will monitor:

```text
BTC + ETH
```

This is the beginning of a larger trading-style system.

Later, you can add:

* SOL
* XRP
* stocks
* forex
* ETFs
* market news

---

# PART 2 — Update `config.py`

```python
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

# BTC decision levels
BTC_BUY_LEVEL = float(os.getenv("BTC_BUY_LEVEL", 100000))
BTC_STRONG_BUY_LEVEL = float(os.getenv("BTC_STRONG_BUY_LEVEL", 110000))
BTC_HOLD_LEVEL = float(os.getenv("BTC_HOLD_LEVEL", 90000))

# ETH decision levels
ETH_BUY_LEVEL = float(os.getenv("ETH_BUY_LEVEL", 3000))
ETH_STRONG_BUY_LEVEL = float(os.getenv("ETH_STRONG_BUY_LEVEL", 3500))
ETH_HOLD_LEVEL = float(os.getenv("ETH_HOLD_LEVEL", 2500))
```

---

# Concept Explanation — Centralized Settings

`config.py` is now your control center.

Instead of changing many files, you change settings in:

```text
.env
```

Then `config.py` loads them.

This is how real AI systems manage:

* API URLs,
* model names,
* risk levels,
* scan limits,
* database connections.

---

# PART 3 — Update `market_data.py`

```python
# Import requests to call APIs
import requests

# Function to get crypto price from any API URL
def get_crypto_price(api_url):

    # Send request to API
    response = requests.get(api_url, timeout=10)

    # Raise error if API request fails
    response.raise_for_status()

    # Convert API response to JSON
    data = response.json()

    # Extract price from Coinbase response
    price = float(data["data"]["amount"])

    # Return price
    return price
```

---

# Concept Explanation — Reusable Function

Before, your function was only for BTC.

Now this function works for:

```text
BTC
ETH
future assets
```

This is called **reusability**.

Instead of writing:

```python
get_btc_price()
get_eth_price()
get_sol_price()
```

You write one flexible function:

```python
get_crypto_price(api_url)
```

---

# PART 4 — Update `agent_logic.py`

```python
# Function for market decision using flexible levels
def market_agent(price, strong_buy_level, buy_level, hold_level):

    # Strong Buy condition
    if price >= strong_buy_level:
        return "Strong Buy"

    # Buy condition
    elif price >= buy_level:
        return "Buy"

    # Hold condition
    elif price >= hold_level:
        return "Hold"

    # Risk Zone condition
    else:
        return "Risk Zone"
```

---

# Concept Explanation — Flexible Decision Logic

Before, your logic was fixed for BTC.

Now it accepts:

```text
price
strong_buy_level
buy_level
hold_level
```

That means the same function can analyze different assets.

Example:

```python
market_agent(btc_price, 110000, 100000, 90000)
market_agent(eth_price, 3500, 3000, 2500)
```

This is how you avoid repeated code.

---

# PART 5 — Update `logger.py`

```python
# Import datetime for timestamps
from datetime import datetime

# Import log file paths from config
from config import TRADE_MEMORY_FILE, ERROR_LOG_FILE

# Function to create timestamp
def get_timestamp():

    # Return readable timestamp
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Function to save asset monitoring record
def save_trade_memory(scan_number, timestamp, asset_name, price, decision):

    # Open trade memory file safely
    with open(TRADE_MEMORY_FILE, "a") as memory_file:

        # Save scan record
        memory_file.write(f"Scan Number: {scan_number}\n")
        memory_file.write(f"Timestamp: {timestamp}\n")
        memory_file.write(f"Asset: {asset_name}\n")
        memory_file.write(f"Price: {price}\n")
        memory_file.write(f"Decision: {decision}\n")
        memory_file.write("----------------------\n")

# Function to save errors
def save_error_log(error):

    # Create timestamp
    timestamp = get_timestamp()

    # Get error type
    error_type = type(error).__name__

    # Get error message
    error_message = str(error)

    # Open error log safely
    with open(ERROR_LOG_FILE, "a") as error_file:

        # Save error details
        error_file.write(f"Timestamp: {timestamp}\n")
        error_file.write(f"Error Type: {error_type}\n")
        error_file.write(f"Message: {error_message}\n")
        error_file.write("----------------------\n")
```

---

# Concept Explanation — Better Logging

Your logs now include:

```text
Asset: BTC
Asset: ETH
```

This matters because your system now monitors more than one asset.

Good logs must clearly show:

* what happened,
* when it happened,
* which asset it happened to,
* and what decision was made.

---

# PART 6 — Update `main.py`

```python
# Import time for scan delay
import time

# Import settings from config
from config import (
    SCAN_LIMIT,
    SCAN_DELAY,
    BTC_API_URL,
    ETH_API_URL,
    BTC_STRONG_BUY_LEVEL,
    BTC_BUY_LEVEL,
    BTC_HOLD_LEVEL,
    ETH_STRONG_BUY_LEVEL,
    ETH_BUY_LEVEL,
    ETH_HOLD_LEVEL
)

# Import reusable price function
from market_data import get_crypto_price

# Import reusable decision function
from agent_logic import market_agent

# Import logging functions
from logger import get_timestamp, save_trade_memory, save_error_log

# Create asset settings list
assets = [
    {
        "name": "BTC",
        "api_url": BTC_API_URL,
        "strong_buy_level": BTC_STRONG_BUY_LEVEL,
        "buy_level": BTC_BUY_LEVEL,
        "hold_level": BTC_HOLD_LEVEL
    },
    {
        "name": "ETH",
        "api_url": ETH_API_URL,
        "strong_buy_level": ETH_STRONG_BUY_LEVEL,
        "buy_level": ETH_BUY_LEVEL,
        "hold_level": ETH_HOLD_LEVEL
    }
]

# Main monitoring loop
for scan in range(1, SCAN_LIMIT + 1):

    # Print current scan number
    print(f"Scan Number: {scan}")

    # Loop through each asset
    for asset in assets:

        try:
            # Get asset price
            price = get_crypto_price(asset["api_url"])

            # Get AI decision
            decision = market_agent(
                price,
                asset["strong_buy_level"],
                asset["buy_level"],
                asset["hold_level"]
            )

            # Create timestamp
            timestamp = get_timestamp()

            # Save monitoring result
            save_trade_memory(
                scan,
                timestamp,
                asset["name"],
                price,
                decision
            )

            # Print result to terminal
            print("Timestamp:", timestamp)
            print("Asset:", asset["name"])
            print("Price:", price)
            print("AI Decision:", decision)

        except Exception as error:

            # Save error log
            save_error_log(error)

            # Print safe error message
            print(f"Error logged safely for {asset['name']}.")

        # Print asset separator
        print("----------------------")

    # Wait before next scan
    time.sleep(SCAN_DELAY)

# Print completion message
print("Multi-asset AI monitoring completed.")
```

---

# Concept Explanation — List of Dictionaries

This part:

```python
assets = [
    {
        "name": "BTC",
        "api_url": BTC_API_URL
    },
    {
        "name": "ETH",
        "api_url": ETH_API_URL
    }
]
```

is a **list of dictionaries**.

This lets your program store multiple assets in one structure.

Professional systems often use this pattern for:

* multiple stocks,
* multiple APIs,
* multiple AI agents,
* multiple users,
* multiple tasks.

---

# DAY 15 CHECKLIST

## Concepts Understood

* [ ] Multi-asset monitoring
* [ ] Reusable functions
* [ ] Flexible decision logic
* [ ] List of dictionaries
* [ ] Cleaner logging
* [ ] Scalable architecture

## Coding

* [ ] Updated `.env`
* [ ] Updated `config.py`
* [ ] Updated `market_data.py`
* [ ] Updated `agent_logic.py`
* [ ] Updated `logger.py`
* [ ] Updated `main.py`
* [ ] Ran `python main.py`

---

# What You Learned Today

Today you upgraded your project from:

```text
Single-asset BTC monitor
```

to:

```text
Multi-asset BTC + ETH AI monitor
```

This is an important step toward:

* trading dashboards,
* portfolio monitoring,
* AI market scanners,
* alert systems,
* and advanced AI trading agents.

---

# Bonus Task

Add `SOL` monitoring.

You will need:

* `SOL_API_URL`
* `SOL_BUY_LEVEL`
* `SOL_STRONG_BUY_LEVEL`
* `SOL_HOLD_LEVEL`

Then add SOL into your `assets` list in `main.py`.
