# Day 10 — Modular AI Systems, Path Management, and Professional Project Structure

## Goal for Today

Learn how professional AI systems:

* organize reusable logic,
* separate responsibilities,
* manage project files safely,
* and build scalable architectures.

Today you will upgrade your AI monitoring agent using:

* modular programming,
* reusable functions,
* and professional file path management with `pathlib`.

Estimated time: **2.5–3 hours**

---

# PART 1 — Review Day 9

Run:

```bash id="rfrzof"
python professional_monitor_agent.py
```

Open:

* `trade_memory.txt`
* `error_log.txt`

Observe:

* timestamps,
* scan numbers,
* error handling,
* and monitoring logs.

---

# Concept Explanation — Why Project Structure Matters

As AI systems grow larger:

* file organization becomes critical,
* logs must save consistently,
* and systems need predictable structure.

Without structure:
projects become:

* messy,
* hard to debug,
* and difficult to scale.

Professional developers organize:

* code,
* logs,
* APIs,
* databases,
* and AI workflows carefully.

---

# PART 2 — Understanding `pathlib`

# What Is `pathlib`?

`pathlib` is a modern Python library for:

* handling file paths,
* organizing directories,
* and managing project files safely.

Instead of manually writing paths like:

```python id="blvk8n"
"C:/Users/Simeon/Desktop/project/file.txt"
```

You can use:

```python id="qj1i5f"
Path(__file__).parent / "file.txt"
```

This is:

* cleaner,
* safer,
* and cross-platform compatible.

---

# Why `pathlib` Matters in AI Systems

Professional AI systems often save:

* logs,
* memory files,
* model outputs,
* temporary files,
* and configuration files.

`pathlib` helps systems:

* locate files correctly,
* avoid broken paths,
* and stay organized.

---

# PART 3 — Create a Path Practice Script

## Create:

```text id="oww2ko"
path_practice.py
```

Code:

```python id="ijy6ee"
# Import Path library
from pathlib import Path

# Get the folder where this Python file exists
project_folder = Path(__file__).parent

# Create file path for notes.txt
notes_file = project_folder / "notes.txt"

# Save text into notes.txt
with open(notes_file, "w") as file:

    # Write sample text
    file.write("AI Agent Developer Training")

# Print success message
print("notes.txt saved successfully.")
```

Run:

```bash id="o6xygp"
python path_practice.py
```

---

# Concept Explanation — `Path(__file__).parent`

```python id="nkl1uy"
Path(__file__).parent
```

Means:

```text id="1ow0i6"
Get the folder where the current Python file exists.
```

---

# Why This Is Important

Without this:
files may save:

* in random terminal folders,
* VS Code directories,
* or unexpected locations.

Using this ensures:

## Files always save beside your Python script.

Professional systems rely heavily on predictable file structure.

---

# PART 4 — Understanding Modular Programming

# What Is Modular Programming?

Modular programming means:

> Breaking a large system into smaller reusable components.

Example AI project structure:

```text id="b8kptn"
project/
│
├── api_tools.py
├── ai_logic.py
├── memory_system.py
├── error_handler.py
├── main.py
```

Each module handles ONE responsibility.

---

# Why Modular Systems Matter

Benefits:

* easier debugging,
* reusable code,
* scalable architecture,
* easier teamwork,
* cleaner projects.

Modern AI systems are ALWAYS modular.

---

# PART 5 — Updated Professional AI Monitor

## Create:

```text id="r0q81h"
modular_btc_agent.py
```

Code:

```python id="0v3xal"
# Import required libraries
import requests
import time
from datetime import datetime
from pathlib import Path

# Save trade_memory.txt AND error_log.txt
# in the same folder where this Python file is located
trade_memory_file = Path(__file__).parent / "trade_memory.txt"
error_log_file = Path(__file__).parent / "error_log.txt"

# Function to create timestamp
def get_timestamp():

    # Return readable timestamp
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Function to retrieve BTC price
def get_btc_price():

    # Coinbase API endpoint
    url = "https://api.coinbase.com/v2/prices/spot?currency=USD"

    # Request BTC price data
    response = requests.get(url, timeout=10)

    # Raise error if request fails
    response.raise_for_status()

    # Convert API response to JSON
    data = response.json()

    # Extract BTC price
    btc_price = float(data["data"]["amount"])

    # Return BTC price
    return btc_price

# Function for AI market decision
def market_agent(price):

    # Strong Buy condition
    if price >= 110000:
        return "Strong Buy"

    # Buy condition
    elif price >= 100000:
        return "Buy"

    # Hold condition
    elif price >= 90000:
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

# Repeat monitoring 5 times
for scan in range(1, 6):

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

    # Wait 5 seconds before next scan
    time.sleep(5)

# Print completion message
print("AI monitoring session completed.")
```

Run:

```bash id="3v7xht"
python modular_btc_agent.py
```

---

# Concept Explanation — Separation of Responsibilities

Notice how each function handles ONE task:

| Function              | Responsibility       |
| --------------------- | -------------------- |
| `get_btc_price()`     | API retrieval        |
| `market_agent()`      | AI decision          |
| `save_trade_memory()` | Save monitoring logs |
| `save_error_log()`    | Save error logs      |
| `get_timestamp()`     | Generate timestamps  |

This is:

## Professional system architecture.

---

# PART 6 — Understanding Scalability

# What Is Scalability?

Scalability means:

> Your system can grow larger without becoming chaotic.

Your current system could later expand into:

* multiple AI agents,
* multiple APIs,
* cloud databases,
* dashboards,
* Azure deployment,
* and autonomous workflows.

Modular systems scale MUCH better.

---

# PART 7 — Professional Folder Thinking

# Recommended Project Structure

```text id="r5zpjm"
AI-Agent-Developer/
│
├── agents/
├── logs/
├── api_tools/
├── memory/
├── projects/
├── experiments/
├── models/
└── main.py
```

---

# Why Folder Structure Matters

Good organization improves:

* productivity,
* debugging,
* collaboration,
* deployment,
* and maintenance.

Large AI projects can contain:

* hundreds of files,
* APIs,
* models,
* databases,
* and workflows.

---

# DAY 10 CHECKLIST

## Concepts Understood

* [ ] pathlib
* [ ] Path management
* [ ] Modular programming
* [ ] Project organization
* [ ] Scalability
* [ ] Separation of responsibilities

## Coding

* [ ] path_practice.py
* [ ] modular_btc_agent.py

## Skills

* [ ] Comfortable using pathlib
* [ ] Comfortable organizing projects
* [ ] Comfortable building modular systems

---

# WHAT YOU LEARNED TODAY

Today you learned:

* professional file handling,
* modular architecture,
* scalable project structure,
* and safer file management.

These concepts are foundational for:

* enterprise AI systems,
* autonomous agents,
* AI SaaS platforms,
* cloud AI deployment,
* and large-scale automation.

---

# REAL-WORLD CONNECTION

Professional AI systems must:

* manage thousands of logs,
* organize APIs safely,
* handle memory consistently,
* and scale cleanly.

Today you learned:

## The foundation of professional AI project architecture.

---

# BONUS TASK

Modify:

```text id="8ehj0n"
modular_btc_agent.py
```

So it creates a dedicated:

```text id="9wjlwm"
logs/
```

folder automatically and saves:

* `trade_memory.txt`
* `error_log.txt`

inside that folder.

Hint:
Use:

```python id="4q6p2q"
Path.mkdir()
```

---

# ADVANCED THINKING QUESTION

Think about this:

> If your AI system grows into 50 different agents,
> how would you organize communication between them?

Hint:

* APIs,
* message queues,
* databases,
* shared memory,
* and orchestration frameworks.

Here’s the updated **BONUS TASK** version that automatically creates a:

```text id="22zv89"
logs/
```

folder and saves:

* `trade_memory.txt`
* `error_log.txt`

inside it.

---

# Updated `modular_btc_agent.py`

```python id="74ypg4"
# Import required libraries
import requests
import time
from datetime import datetime
from pathlib import Path

# Get the folder where this Python file exists
project_folder = Path(__file__).parent

# Create a logs folder path
logs_folder = project_folder / "logs"

# Create the logs folder automatically
# exist_ok=True prevents errors if the folder already exists
logs_folder.mkdir(exist_ok=True)

# Create file paths inside logs folder
trade_memory_file = logs_folder / "trade_memory.txt"
error_log_file = logs_folder / "error_log.txt"

# Function to create timestamp
def get_timestamp():

    # Return readable timestamp
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Function to retrieve BTC price
def get_btc_price():

    # Coinbase API endpoint
    url = "https://api.coinbase.com/v2/prices/spot?currency=USD"

    # Request BTC price data
    response = requests.get(url, timeout=10)

    # Raise error if request fails
    response.raise_for_status()

    # Convert API response into JSON
    data = response.json()

    # Extract BTC price
    btc_price = float(data["data"]["amount"])

    # Return BTC price
    return btc_price

# Function for AI market decision
def market_agent(price):

    # Strong Buy condition
    if price >= 110000:
        return "Strong Buy"

    # Buy condition
    elif price >= 100000:
        return "Buy"

    # Hold condition
    elif price >= 90000:
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

# Repeat monitoring 5 times
for scan in range(1, 6):

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

    # Wait 5 seconds before next scan
    time.sleep(5)

# Print completion message
print("AI monitoring session completed.")
```

---

# Concept Explanation — `Path.mkdir()`

```python id="0nfqqz"
logs_folder.mkdir(exist_ok=True)
```

Means:

```text id="gjlwm0"
Create the folder automatically if it does not already exist.
```

---

# Why `exist_ok=True` Matters

Without it:
Python creates an error if the folder already exists.

With it:
Python safely ignores the existing folder.

This is common in:

* AI logging systems,
* backend servers,
* cloud applications,
* and enterprise automation.

---

# Your Project Structure Now

After running the script:

```text id="vrhdf9"
project/
│
├── modular_btc_agent.py
│
└── logs/
    ├── trade_memory.txt
    └── error_log.txt
```

---

# Why This Is Professional

You are now using:

* organized logging,
* dedicated folders,
* modular architecture,
* safer file handling,
* and scalable structure.

This is VERY close to how real AI systems are organized.
