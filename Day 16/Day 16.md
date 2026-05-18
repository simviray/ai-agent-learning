# Day 16 — Clean Asset Configuration and Scalable Multi-Asset Design

## Goal for Today

Upgrade your agent so adding a new coin becomes easier and cleaner.

Today you will learn:

* cleaner asset configuration
* reducing repeated code
* scalable design
* how to prepare for many coins later

Estimated time: **2.5–3 hours**

---

# PART 1 — Review Day 15

Run:

```bash
python main.py
```

Your agent should now monitor:

```text
BTC
ETH
SOL
```

---

# Concept Explanation — Why We Need Cleaner Configuration

Right now, every new asset requires many edits:

```text
.env
config.py
main.py
```

That works for 3 coins, but it becomes messy for:

```text
10 coins
50 coins
100 coins
```

Today, we will make the project cleaner by building one centralized `ASSETS` list inside `config.py`.

---

# PART 2 — Update `.env`

Keep this full `.env` version:

```text
SCAN_LIMIT=5
SCAN_DELAY=5

BTC_API_URL=https://api.coinbase.com/v2/prices/spot?currency=USD
ETH_API_URL=https://api.coinbase.com/v2/prices/ETH-USD/spot
SOL_API_URL=https://api.coinbase.com/v2/prices/SOL-USD/spot

BTC_BUY_LEVEL=100000
BTC_STRONG_BUY_LEVEL=110000
BTC_HOLD_LEVEL=90000

ETH_BUY_LEVEL=3000
ETH_STRONG_BUY_LEVEL=3500
ETH_HOLD_LEVEL=2500

SOL_BUY_LEVEL=180
SOL_STRONG_BUY_LEVEL=220
SOL_HOLD_LEVEL=140
```

---

# PART 3 — Update `config.py`

Replace your asset-related settings with this cleaner version:

```python
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
    }
]
```

---

# Concept Explanation — Centralized Asset Configuration

This `ASSETS` list stores all coin settings in one place.

Each asset has:

```text
name
api_url
strong_buy_level
buy_level
hold_level
```

This makes your system easier to expand.

To add another coin later, you only add one new dictionary.

---

# PART 4 — Update `main.py`

Replace your current `main.py` with this cleaner version:

```python
# Import time for scan delay
import time

# Import scan settings and centralized asset list
from config import SCAN_LIMIT, SCAN_DELAY, ASSETS

# Import reusable price function
from market_data import get_crypto_price

# Import reusable decision function
from agent_logic import market_agent

# Import logging functions
from logger import get_timestamp, save_trade_memory, save_error_log

# Main monitoring loop
for scan in range(1, SCAN_LIMIT + 1):

    # Print current scan number
    print(f"Scan Number: {scan}")

    # Loop through every asset inside ASSETS list
    for asset in ASSETS:

        try:
            # Get asset price using its API URL
            price = get_crypto_price(asset["api_url"])

            # Get AI decision using flexible levels
            decision = market_agent(
                price,
                asset["strong_buy_level"],
                asset["buy_level"],
                asset["hold_level"]
            )

            # Create timestamp for this scan
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
print("Scalable multi-asset AI monitoring completed.")
```

---

# Concept Explanation — Why This Is Cleaner

Before, `main.py` had many asset imports.

Now it only imports:

```python
from config import SCAN_LIMIT, SCAN_DELAY, ASSETS
```

That means `main.py` does not need to know every coin manually.

It simply loops through whatever assets are inside `ASSETS`.

This is more scalable.

---

# PART 5 — Confirm Other Files Stay the Same

Your `market_data.py` should still be:

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

Your `agent_logic.py` should still be:

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

# PART 6 — Run Your Project

Run:

```bash
python main.py
```

Expected assets:

```text
BTC
ETH
SOL
```

---

# DAY 16 CHECKLIST

## Concepts Understood

* [ ] Centralized configuration
* [ ] Cleaner `main.py`
* [ ] Scalable asset design
* [ ] List of dictionaries
* [ ] Reducing repeated imports
* [ ] Easier coin expansion

## Coding

* [ ] Updated `.env`
* [ ] Updated `config.py`
* [ ] Updated `main.py`
* [ ] Ran `python main.py`
* [ ] Confirmed BTC, ETH, SOL are monitored

---

# What You Learned Today

Today you improved your project from:

```text
Multi-asset monitor
```

to:

```text
Scalable multi-asset monitor
```

This matters because real AI systems must be easy to expand.

You are now learning professional design patterns used in:

* AI agents
* trading bots
* monitoring dashboards
* backend systems
* enterprise automation

---

# Bonus Task

Add one more asset: `XRP`.

You will add:

* `XRP_API_URL`
* `XRP_BUY_LEVEL`
* `XRP_STRONG_BUY_LEVEL`
* `XRP_HOLD_LEVEL`

Then add one new dictionary inside `ASSETS` in `config.py`.

## 1. Update `.env`

Add these XRP settings:

```text id="g8m2rp"
XRP_API_URL=https://api.coinbase.com/v2/prices/XRP-USD/spot

XRP_BUY_LEVEL=2.50
XRP_STRONG_BUY_LEVEL=3.00
XRP_HOLD_LEVEL=2.00
```

Your `.env` now includes:

```text id="f5v7kn"
SCAN_LIMIT=5
SCAN_DELAY=5

BTC_API_URL=https://api.coinbase.com/v2/prices/spot?currency=USD
ETH_API_URL=https://api.coinbase.com/v2/prices/ETH-USD/spot
SOL_API_URL=https://api.coinbase.com/v2/prices/SOL-USD/spot
XRP_API_URL=https://api.coinbase.com/v2/prices/XRP-USD/spot

BTC_BUY_LEVEL=100000
BTC_STRONG_BUY_LEVEL=110000
BTC_HOLD_LEVEL=90000

ETH_BUY_LEVEL=3000
ETH_STRONG_BUY_LEVEL=3500
ETH_HOLD_LEVEL=2500

SOL_BUY_LEVEL=180
SOL_STRONG_BUY_LEVEL=220
SOL_HOLD_LEVEL=140

XRP_BUY_LEVEL=2.50
XRP_STRONG_BUY_LEVEL=3.00
XRP_HOLD_LEVEL=2.00
```

---

# 2. Update `config.py`

Add this new XRP dictionary inside `ASSETS`:

```python id="x9q4tw"
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
```

---

# Full Example of `ASSETS`

```python id="v3m8zy"
ASSETS = [
    {
        "name": "BTC",
        "api_url": os.getenv("BTC_API_URL"),
        "strong_buy_level": float(os.getenv("BTC_STRONG_BUY_LEVEL", 110000)),
        "buy_level": float(os.getenv("BTC_BUY_LEVEL", 100000)),
        "hold_level": float(os.getenv("BTC_HOLD_LEVEL", 90000))
    },
    {
        "name": "ETH",
        "api_url": os.getenv("ETH_API_URL"),
        "strong_buy_level": float(os.getenv("ETH_STRONG_BUY_LEVEL", 3500)),
        "buy_level": float(os.getenv("ETH_BUY_LEVEL", 3000)),
        "hold_level": float(os.getenv("ETH_HOLD_LEVEL", 2500))
    },
    {
        "name": "SOL",
        "api_url": os.getenv("SOL_API_URL"),
        "strong_buy_level": float(os.getenv("SOL_STRONG_BUY_LEVEL", 220)),
        "buy_level": float(os.getenv("SOL_BUY_LEVEL", 180)),
        "hold_level": float(os.getenv("SOL_HOLD_LEVEL", 140))
    },
    {
        "name": "XRP",
        "api_url": os.getenv("XRP_API_URL"),
        "strong_buy_level": float(os.getenv("XRP_STRONG_BUY_LEVEL", 3.00)),
        "buy_level": float(os.getenv("XRP_BUY_LEVEL", 2.50)),
        "hold_level": float(os.getenv("XRP_HOLD_LEVEL", 2.00))
    }
]
```

---

# 3. Run the Project

Run:

```bash id="q2w7vn"
python main.py
```

Your AI monitor now supports:

```text id="b6x9pk"
BTC
ETH
SOL
XRP
```

---

# Concept Explanation — Why This Design Is Powerful

Notice something important:

You did NOT need to update:

* `main.py`
* `market_data.py`
* `agent_logic.py`
* `logger.py`

You ONLY updated:

* `.env`
* `config.py`

That means your architecture is becoming:

## scalable and modular.

This is how professional systems are designed.
