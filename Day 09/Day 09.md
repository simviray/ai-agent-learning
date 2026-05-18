# Day 9 — Timestamps, Error Logs, and Professional AI Agent Records

## Goal for Today

Learn how AI systems keep professional records using:

* timestamps,
* error logs,
* activity logs,
* and safer monitoring workflows.

Today you will upgrade your AI agent so it saves both successful activity and errors.

Estimated time: **2.5–3 hours**

---

# PART 1 — Review Day 8

Run:

```bash
python safe_monitor_agent.py
```

Open or create:

```text
error_log.txt
```

---

# Concept Explanation — Why Logs Matter

Logs are records of what happened in your system.

Professional AI systems use logs to answer:

```text
What happened?
When did it happen?
Why did it fail?
What did the AI decide?
```

Logs are important for:

* debugging,
* trading history,
* business audits,
* AI safety,
* and system improvement.

---

# PART 2 — Learn Timestamps

## Create:

```text
timestamp_practice.py
```

Code:

```python
# Import datetime so we can create timestamps
from datetime import datetime

# Get the current date and time
current_time = datetime.now()

# Format the timestamp so it is easy to read
timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")

# Print the timestamp
print("Current Timestamp:", timestamp)
```

Run:

```bash
python timestamp_practice.py
```

---

# Concept Explanation — Timestamp

A timestamp means:

```text
The exact date and time something happened.
```

Example:

```text
2026-05-17 08:30:15
```

AI systems use timestamps for:

* trade logs,
* chat history,
* error records,
* monitoring events,
* and audit trails.

---

# PART 3 — Save a Timestamped Log

## Create:

```text
timestamp_log.py
```

Code:

```python
# Import datetime for timestamps
from datetime import datetime

# Create a readable timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Open the log file in append mode
with open("activity_log.txt", "a") as log_file:

    # Save activity with timestamp
    log_file.write(f"{timestamp} - AI agent started.\n")

# Print confirmation
print("Activity saved to activity_log.txt")
```

Run:

```bash
python timestamp_log.py
```

---

# Concept Explanation — `with open()`

This is a safer way to open files.

Instead of:

```python
file = open("log.txt", "a")
file.close()
```

Use:

```python
with open("log.txt", "a") as file:
```

Why?

Because Python automatically closes the file safely.

This is the professional way.

---

# PART 4 — Save Error Logs

## Create:

```text
error_logger.py
```

Code:

```python
# Import datetime for timestamps
from datetime import datetime

try:
    # This will create an error because division by zero is not allowed
    result = 10 / 0

except Exception as error:

    # Create timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Get the error type
    error_type = type(error).__name__

    # Get the error message
    error_message = str(error)

    # Save error details into error_log.txt
    with open("error_log.txt", "a") as log_file:
        log_file.write(f"Timestamp: {timestamp}\n")
        log_file.write(f"Error Type: {error_type}\n")
        log_file.write(f"Message: {error_message}\n")
        log_file.write("----------------------\n")

    # Print friendly message
    print("Error saved to error_log.txt")
```

Run:

```bash
python error_logger.py
```

---

# Concept Explanation — `Exception as error`

This means:

```text
Catch the error and store its details inside the variable named error.
```

This lets your program save:

* error type,
* error message,
* and timestamp.

That is much better than only printing:

```text
Something went wrong.
```

---

# PART 5 — Upgrade Your Safe Monitor Agent

## Create:

```text
professional_monitor_agent.py
```

Code:

```python
# Import libraries for API requests, time delays, and timestamps
import requests
import time
from datetime import datetime

# Function to create a timestamp
def get_timestamp():
    # Return current date and time as readable text
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Function to decide market status
def market_agent(price):
    # Strong buy condition
    if price >= 110000:
        return "Strong Buy"

    # Buy condition
    elif price >= 100000:
        return "Buy"

    # Hold condition
    elif price >= 90000:
        return "Hold"

    # Risk zone condition
    else:
        return "Risk Zone"

# Repeat monitoring 5 times
for i in range(5):

    try:
        # Coinbase BTC price API
        url = "https://api.coinbase.com/v2/prices/spot?currency=USD"

        # Request BTC data with timeout protection
        response = requests.get(url, timeout=10)

        # Raise an error if the API request failed
        response.raise_for_status()

        # Convert response to JSON
        data = response.json()

        # Extract BTC price
        btc_price = float(data["data"]["amount"])

        # Get AI decision
        decision = market_agent(btc_price)

        # Create timestamp
        timestamp = get_timestamp()

        # Save successful trade monitoring record
        with open("trade_memory.txt", "a") as memory_file:
            memory_file.write(f"Timestamp: {timestamp}\n")
            memory_file.write(f"BTC Price: {btc_price}\n")
            memory_file.write(f"Decision: {decision}\n")
            memory_file.write("----------------------\n")

        # Print result
        print("Timestamp:", timestamp)
        print("BTC Price:", btc_price)
        print("AI Decision:", decision)

    except Exception as error:
        # Create timestamp for the error
        timestamp = get_timestamp()

        # Get error type
        error_type = type(error).__name__

        # Get error message
        error_message = str(error)

        # Save error details
        with open("error_log.txt", "a") as error_file:
            error_file.write(f"Timestamp: {timestamp}\n")
            error_file.write(f"Error Type: {error_type}\n")
            error_file.write(f"Message: {error_message}\n")
            error_file.write("----------------------\n")

        # Print safe error message
        print("Error saved to error_log.txt")

    # Print separator
    print("----------------------")

    # Wait 5 seconds before next check
    time.sleep(5)

# Print completion message
print("Monitoring session completed.")
```

Run:

```bash
python professional_monitor_agent.py
```

---

# Concept Explanation — `timeout=10`

This means:

```text
Wait up to 10 seconds for the API.
```

If the API does not respond, Python stops waiting and creates an error.

This prevents your AI agent from freezing.

---

# Concept Explanation — `response.raise_for_status()`

This checks if the API request was successful.

For example:

```text
200 = success
404 = not found
500 = server error
```

If the API fails, this line creates an error so your program can log it.

---

# DAY 9 CHECKLIST

## Concepts Understood

* [ ] Timestamps
* [ ] Activity logs
* [ ] Error logs
* [ ] `with open()`
* [ ] `Exception as error`
* [ ] API timeout
* [ ] `raise_for_status()`

## Coding

* [ ] timestamp_practice.py
* [ ] timestamp_log.py
* [ ] error_logger.py
* [ ] professional_monitor_agent.py

## Output Files

* [ ] activity_log.txt
* [ ] error_log.txt
* [ ] trade_memory.txt

---

# What You Learned Today

Today you learned how to make your AI agent more professional by adding:

```text
Monitoring + Memory + Error Logging + Timestamps
```

This is important for:

* AI trading systems,
* autonomous agents,
* enterprise AI tools,
* debugging,
* and audit-ready business systems.

---

# Bonus Task

Modify `professional_monitor_agent.py` so it also saves:

```text
Scan Number: 1
Scan Number: 2
Scan Number: 3
```

inside `trade_memory.txt`.

This helps track every monitoring cycle.
