# Day 11 — Environment Variables, API Safety, and Config Files

## Goal for Today

Learn how professional AI systems protect sensitive information and separate settings from code.

Today you will learn:

* environment variables
* `.env` files
* API key safety
* configuration files
* safer project structure

Estimated time: **2.5–3 hours**

---

# PART 1 — Review Day 10

Run:

```bash
python modular_btc_agent.py
```

Check this structure:

```text
project/
│
├── modular_btc_agent.py
│
└── logs/
    ├── trade_memory.txt
    └── error_log.txt
```

---

# Concept Explanation — Why Configuration Matters

Professional AI systems need settings such as:

```text
API keys
model names
database URLs
log folder paths
scan intervals
```

You should NOT hard-code important settings everywhere in your code.

Instead, you store settings separately.

This makes your project:

* safer
* cleaner
* easier to update
* more professional

---

# PART 2 — What Is an Environment Variable?

An environment variable is:

```text
A hidden setting stored outside your Python code.
```

Example:

```text
OPENAI_API_KEY=your_secret_key_here
```

AI developers use environment variables to protect:

* OpenAI keys
* Azure keys
* database passwords
* trading API keys
* webhook URLs

---

# Concept Explanation — Why Not Put API Keys in Code?

Bad practice:

```python
api_key = "sk-your-secret-key"
```

Why bad?

Because you might accidentally:

* upload it to GitHub
* share it with others
* expose your trading account
* expose your cloud account

Professional developers keep secrets outside the code.

---

# PART 3 — Install `python-dotenv`

Open terminal:

```bash
pip install python-dotenv
```

---

# Concept Explanation — What Is `python-dotenv`?

`python-dotenv` lets Python read settings from a `.env` file.

A `.env` file stores private project settings like:

```text
SCAN_LIMIT=5
SCAN_DELAY=5
```

Later, you can also store:

```text
OPENAI_API_KEY=your_key_here
AZURE_AI_ENDPOINT=your_endpoint_here
```

---

# PART 4 — Create Your First `.env` File

Create this file in the same folder as your Python script:

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
```

---

# Concept Explanation — What These Settings Mean

| Setting                | Meaning                             |
| ---------------------- | ----------------------------------- |
| `SCAN_LIMIT`           | How many times the agent checks BTC |
| `SCAN_DELAY`           | Seconds between scans               |
| `BTC_BUY_LEVEL`        | Price level for Buy signal          |
| `BTC_STRONG_BUY_LEVEL` | Price level for Strong Buy signal   |
| `BTC_HOLD_LEVEL`       | Price level for Hold signal         |

Now you can change behavior without editing the main code.

---

# PART 5 — Practice Reading Environment Variables

Create:

```text
env_practice.py
```

Code:

```python
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
```

Run:

```bash
python env_practice.py
```

---

# Concept Explanation — `os.getenv()`

```python
os.getenv("SCAN_LIMIT")
```

Means:

```text
Get the value of SCAN_LIMIT from the environment.
```

Important note:

Environment variables are read as text.

So this:

```text
SCAN_LIMIT=5
```

is first read as:

```python
"5"
```

not:

```python
5
```

That means we must convert it when needed.

---

# PART 6 — Convert Environment Variables

Create:

```text
env_convert.py
```

Code:

```python
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
```

Run:

```bash
python env_convert.py
```

---

# Concept Explanation — Default Values

```python
os.getenv("SCAN_LIMIT", 5)
```

Means:

```text
Get SCAN_LIMIT. If it does not exist, use 5.
```

This prevents your program from crashing if a setting is missing.

---

# PART 7 — Update Your BTC Agent With `.env`

Create:

```text
config_btc_agent.py
```

Code:

```python
# Import required libraries
import os
import requests
import time
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the folder where this Python file exists
project_folder = Path(__file__).parent

# Create logs folder path
logs_folder = project_folder / "logs"

# Create logs folder automatically if it does not exist
logs_folder.mkdir(exist_ok=True)

# Create file paths inside logs folder
trade_memory_file = logs_folder / "trade_memory.txt"
error_log_file = logs_folder / "error_log.txt"

# Read settings from .env file
SCAN_LIMIT = int(os.getenv("SCAN_LIMIT", 5))
SCAN_DELAY = int(os.getenv("SCAN_DELAY", 5))
BTC_BUY_LEVEL = float(os.getenv("BTC_BUY_LEVEL", 100000))
BTC_STRONG_BUY_LEVEL = float(os.getenv("BTC_STRONG_BUY_LEVEL", 110000))
BTC_HOLD_LEVEL = float(os.getenv("BTC_HOLD_LEVEL", 90000))

# Function to create timestamp
def get_timestamp():

    # Return readable timestamp
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Function to retrieve BTC price
def get_btc_price():

    # Coinbase API endpoint
    url = "https://api.coinbase.com/v2/prices/spot?currency=USD"

    # Request BTC price data with timeout protection
    response = requests.get(url, timeout=10)

    # Raise error if API request fails
    response.raise_for_status()

    # Convert API response into JSON
    data = response.json()

    # Extract BTC price
    btc_price = float(data["data"]["amount"])

    # Return BTC price
    return btc_price

# Function for AI market decision
def market_agent(price):

    # Strong Buy condition from .env
    if price >= BTC_STRONG_BUY_LEVEL:
        return "Strong Buy"

    # Buy condition from .env
    elif price >= BTC_BUY_LEVEL:
        return "Buy"

    # Hold condition from .env
    elif price >= BTC_HOLD_LEVEL:
        return "Hold"

    # Risk Zone condition
    else:
        return "Risk Zone"

# Function to save trade memory
def save_trade_memory(scan_number, timestamp, btc_price, decision):

    # Open trade memory file safely
    with open(trade_memory_file, "a") as memory_file:

        # Save scan details
        memory_file.write(f"Scan Number: {scan_number}\n")
        memory_file.write(f"Timestamp: {timestamp}\n")
        memory_file.write(f"BTC Price: {btc_price}\n")
        memory_file.write(f"Decision: {decision}\n")
        memory_file.write("----------------------\n")

# Function to save error logs
def save_error_log(error):

    # Create timestamp
    timestamp = get_timestamp()

    # Get error type
    error_type = type(error).__name__

    # Get error message
    error_message = str(error)

    # Open error log file safely
    with open(error_log_file, "a") as error_file:

        # Save error details
        error_file.write(f"Timestamp: {timestamp}\n")
        error_file.write(f"Error Type: {error_type}\n")
        error_file.write(f"Message: {error_message}\n")
        error_file.write("----------------------\n")

# Repeat monitoring based on SCAN_LIMIT from .env
for scan in range(1, SCAN_LIMIT + 1):

    try:

        # Get BTC price
        btc_price = get_btc_price()

        # Get AI decision
        decision = market_agent(btc_price)

        # Create timestamp
        timestamp = get_timestamp()

        # Save trade memory
        save_trade_memory(scan, timestamp, btc_price, decision)

        # Print monitoring details
        print(f"Scan Number: {scan}")
        print("Timestamp:", timestamp)
        print("BTC Price:", btc_price)
        print("AI Decision:", decision)

    except Exception as error:

        # Save error log
        save_error_log(error)

        # Print safe error message
        print("Error logged safely.")

    # Print separator line
    print("----------------------")

    # Wait based on SCAN_DELAY from .env
    time.sleep(SCAN_DELAY)

# Print completion message
print("Config-based AI monitoring session completed.")
```

Run:

```bash
python config_btc_agent.py
```

---

# PART 8 — Add `.gitignore`

Create:

```text
.gitignore
```

Add:

```text
.env
logs/
__pycache__/
```

---

# Concept Explanation — What Is `.gitignore`?

`.gitignore` tells Git:

```text
Do not upload these files to GitHub.
```

This helps protect:

* secrets
* API keys
* private logs
* temporary files

Very important for AI and trading projects.

---

# DAY 11 CHECKLIST

## Concepts Understood

* [ ] Environment variables
* [ ] `.env` files
* [ ] API key safety
* [ ] `python-dotenv`
* [ ] `os.getenv()`
* [ ] Default values
* [ ] `.gitignore`

## Coding

* [ ] `.env`
* [ ] `env_practice.py`
* [ ] `env_convert.py`
* [ ] `config_btc_agent.py`
* [ ] `.gitignore`

---

# What You Learned Today

Today you learned how to separate:

```text
Code
```

from:

```text
Configuration
```

This is a professional software engineering skill.

You are now closer to building:

* AI agents
* Azure AI apps
* trading bots
* business automation systems
* enterprise-grade AI tools

---

# Bonus Task

Add this to your `.env` file:

```text
BTC_API_URL=https://api.coinbase.com/v2/prices/spot?currency=USD
```

Then update your code so the API URL also comes from `.env`.

This makes your project even more configurable.
