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

# Bonus Task — Move the BTC API URL into `.env`

## Goal

Make your AI system MORE configurable by moving the API URL outside the Python code.

This is how professional systems manage:

* APIs
* databases
* cloud endpoints
* AI model URLs
* configuration settings

---

# STEP 1 — Update Your `.env` File

Open:

```text id="9c3lqv"
.env
```

Add this line:

```text id="u1m9zk"
BTC_API_URL=https://api.coinbase.com/v2/prices/spot?currency=USD
```

Your `.env` file should now look like:

```text id="y4v8tr"
SCAN_LIMIT=5
SCAN_DELAY=5
BTC_BUY_LEVEL=100000
BTC_STRONG_BUY_LEVEL=110000
BTC_HOLD_LEVEL=90000
BTC_API_URL=https://api.coinbase.com/v2/prices/spot?currency=USD
```

---

# Concept Explanation — Why This Is Better

Before:

```python id="mr5z2x"
url = "https://api.coinbase.com/v2/prices/spot?currency=USD"
```

The API URL was hard-coded directly into Python.

Problem:

* harder to change,
* duplicated in multiple files,
* less flexible.

Now:
the API URL becomes configurable.

You can later switch APIs WITHOUT changing code.

Example future upgrades:

* Coinbase API
* Binance API
* Kraken API
* Hyperliquid API

Only `.env` changes.

---

# STEP 2 — Update Your Python Code

## Update `config_btc_agent.py`

Replace this OLD section:

```python id="v0w6pt"
# Coinbase API endpoint
url = "https://api.coinbase.com/v2/prices/spot?currency=USD"
```

With this NEW version:

```python id="n8q4ym"
# Read BTC API URL from .env file
BTC_API_URL = os.getenv(
    "BTC_API_URL",
    "https://api.coinbase.com/v2/prices/spot?currency=USD"
)
```

---

# STEP 3 — Update `get_btc_price()`

Replace your OLD function:

```python id="g7r2qx"
def get_btc_price():

    url = "https://api.coinbase.com/v2/prices/spot?currency=USD"

    response = requests.get(url, timeout=10)
```

With this NEW version:

```python id="n2v9kp"
# Function to retrieve BTC price
def get_btc_price():

    # Request BTC price data using URL from .env
    response = requests.get(BTC_API_URL, timeout=10)

    # Raise error if request fails
    response.raise_for_status()

    # Convert API response into JSON
    data = response.json()

    # Extract BTC price
    btc_price = float(data["data"]["amount"])

    # Return BTC price
    return btc_price
```

---

# FULL UPDATED SECTION

Add this near your `.env` settings:

```python id="m4t8zs"
# Read settings from .env file
SCAN_LIMIT = int(os.getenv("SCAN_LIMIT", 5))
SCAN_DELAY = int(os.getenv("SCAN_DELAY", 5))

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

# Concept Explanation — Default Fallback

This part:

```python id="z8k5qn"
os.getenv("BTC_API_URL", "default_url")
```

Means:

```text id="b2v7rm"
Try to get BTC_API_URL from .env.
If it does not exist, use the default URL.
```

This prevents crashes if `.env` is missing.

Professional systems ALWAYS use safe defaults.

---

# Why This Is Professional Engineering

You are now separating:

| Area        | Responsibility  |
| ----------- | --------------- |
| `.env`      | Configuration   |
| Python code | Logic           |
| Logs folder | Monitoring data |

This is how:

* enterprise AI systems,
* cloud platforms,
* AI agents,
* and backend services
  are organized professionally.

---

# Your Project Structure Now

```text id="j5x8cn"
project/
│
├── .env
├── .gitignore
├── config_btc_agent.py
│
└── logs/
    ├── trade_memory.txt
    └── error_log.txt
```

---

# What You Just Learned

Today’s bonus task introduced:

* configurable architecture,
* environment-driven systems,
* safer API management,
* and cleaner project design.

This is VERY important later for:

* Azure AI
* OpenAI APIs
* AI agents
* cloud deployment
* Docker containers
* production systems

---

# Advanced Thinking Question

Think about this:

> If your AI agent later needs:
>
> * multiple APIs,
> * multiple AI models,
> * database connections,
> * and cloud services,
>
> how useful would centralized configuration become?

Hint:
Large systems may have:

* dozens of environment variables,
* multiple environments,
* and deployment configurations.
