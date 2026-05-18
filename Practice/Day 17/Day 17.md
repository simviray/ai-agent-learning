# Day 17 — Portfolio Summary and Daily Performance Report

## Goal for Today

Upgrade your AI agent so it creates a simple daily performance report.

Today you will learn:

* summary reporting
* counting decisions
* storing results in memory
* reading log files
* turning raw logs into useful insights

---

# PART 1 — Concept Explanation

Right now your agent saves logs like:

```text
Asset: BTC
Price: 105000
Decision: Buy
```

But professional systems do more than save logs.

They also create reports:

```text
Total scans: 5
Buy signals: 3
Hold signals: 6
Risk Zone signals: 2
```

This helps you understand what your AI agent is doing.

---

# PART 2 — Create `report.py`

Create a new file:

```text
report.py
```

Add this code:

```python
# Import trade memory file path from config
from config import TRADE_MEMORY_FILE

# Function to generate a simple report from trade_memory.txt
def generate_report():

    # Create counters for each decision type
    strong_buy_count = 0
    buy_count = 0
    hold_count = 0
    risk_zone_count = 0

    # Check if the trade memory file exists
    if not TRADE_MEMORY_FILE.exists():

        # Print message if no log file exists yet
        print("No trade memory file found yet.")

        # Stop the function
        return

    # Open the trade memory file safely
    with open(TRADE_MEMORY_FILE, "r") as memory_file:

        # Read all lines from the file
        lines = memory_file.readlines()

    # Loop through every line in the file
    for line in lines:

        # Count Strong Buy decisions
        if "Decision: Strong Buy" in line:
            strong_buy_count += 1

        # Count Buy decisions
        elif "Decision: Buy" in line:
            buy_count += 1

        # Count Hold decisions
        elif "Decision: Hold" in line:
            hold_count += 1

        # Count Risk Zone decisions
        elif "Decision: Risk Zone" in line:
            risk_zone_count += 1

    # Calculate total decisions
    total_decisions = (
        strong_buy_count
        + buy_count
        + hold_count
        + risk_zone_count
    )

    # Print report
    print("AI Agent Performance Report")
    print("---------------------------")
    print("Total Decisions:", total_decisions)
    print("Strong Buy:", strong_buy_count)
    print("Buy:", buy_count)
    print("Hold:", hold_count)
    print("Risk Zone:", risk_zone_count)

# Run the report function
generate_report()
```

Run:

```bash
python report.py
```

---

# PART 3 — Concept Explanation: Reading Files

This line:

```python
lines = memory_file.readlines()
```

means:

```text
Read every line from the log file and store them in a list.
```

This allows Python to analyze old agent activity.

---

# PART 4 — Concept Explanation: Counting Patterns

This code:

```python
if "Decision: Buy" in line:
    buy_count += 1
```

means:

```text
If this line contains “Decision: Buy,” add 1 to the Buy counter.
```

This is how simple reporting systems work.

---

# PART 5 — Optional Upgrade: Save Report to File

Create:

```text
daily_report.py
```

Add this code:

```python
# Import datetime for timestamps
from datetime import datetime

# Import log file paths from config
from config import TRADE_MEMORY_FILE, LOGS_FOLDER

# Create report file path
REPORT_FILE = LOGS_FOLDER / "daily_report.txt"

# Function to create readable timestamp
def get_timestamp():

    # Return current date and time
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Function to generate and save report
def generate_daily_report():

    # Create decision counters
    strong_buy_count = 0
    buy_count = 0
    hold_count = 0
    risk_zone_count = 0

    # Check if trade memory exists
    if not TRADE_MEMORY_FILE.exists():

        # Save message if no data exists
        with open(REPORT_FILE, "a") as report_file:
            report_file.write("No trade memory file found yet.\n")

        # Stop function
        return

    # Open trade memory file
    with open(TRADE_MEMORY_FILE, "r") as memory_file:

        # Read all log lines
        lines = memory_file.readlines()

    # Count each decision type
    for line in lines:

        # Count Strong Buy decisions
        if "Decision: Strong Buy" in line:
            strong_buy_count += 1

        # Count Buy decisions
        elif "Decision: Buy" in line:
            buy_count += 1

        # Count Hold decisions
        elif "Decision: Hold" in line:
            hold_count += 1

        # Count Risk Zone decisions
        elif "Decision: Risk Zone" in line:
            risk_zone_count += 1

    # Calculate total decisions
    total_decisions = (
        strong_buy_count
        + buy_count
        + hold_count
        + risk_zone_count
    )

    # Create timestamp
    timestamp = get_timestamp()

    # Save report
    with open(REPORT_FILE, "a") as report_file:

        # Write report details
        report_file.write(f"Report Timestamp: {timestamp}\n")
        report_file.write("AI Agent Daily Report\n")
        report_file.write("---------------------\n")
        report_file.write(f"Total Decisions: {total_decisions}\n")
        report_file.write(f"Strong Buy: {strong_buy_count}\n")
        report_file.write(f"Buy: {buy_count}\n")
        report_file.write(f"Hold: {hold_count}\n")
        report_file.write(f"Risk Zone: {risk_zone_count}\n")
        report_file.write("=====================\n")

    # Print confirmation
    print("Daily report saved to logs/daily_report.txt")

# Run the report
generate_daily_report()
```

Run:

```bash
python daily_report.py
```

---

# DAY 17 CHECKLIST

* [ ] Created `report.py`
* [ ] Ran `python report.py`
* [ ] Created `daily_report.py`
* [ ] Ran `python daily_report.py`
* [ ] Checked `logs/daily_report.txt`
* [ ] Understood file reading
* [ ] Understood counting decisions
* [ ] Understood summary reporting

---

# What You Learned Today

Today you learned how to turn raw logs into useful reports.

This is important for:

* AI trading agents
* dashboards
* business reports
* monitoring systems
* portfolio projects

---

# Bonus Task

Update `README.md` and add:

````markdown
## Reports

This project includes reporting tools:

- `report.py` prints a summary report in the terminal.
- `daily_report.py` saves a report inside `logs/daily_report.txt`.

Run:

```bash
python report.py
python daily_report.py
````

```
```
