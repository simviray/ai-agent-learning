# Day 10 — Functions, Reusability, and Building Modular AI Systems

## Goal for Today

Learn how professional AI systems:

* organize reusable logic,
* separate responsibilities,
* build modular workflows,
* and reduce duplicated code.

Today you will refactor your AI monitor into cleaner reusable functions.

Estimated time: **2.5–3 hours**

---

# PART 1 — Review Day 9

Run:

```bash
python professional_monitor_agent.py
```

Open:

* `trade_memory.txt`
* `error_log.txt`

Observe:

* timestamps,
* decisions,
* logs,
* monitoring cycles.

---

# Concept Explanation — Why Refactoring Matters

Beginner code often becomes:

* repetitive,
* messy,
* difficult to maintain.

Professional developers improve code by:

* separating responsibilities,
* creating reusable functions,
* simplifying workflows,
* and improving readability.

This process is called:

# Refactoring

---

# Example of Bad Repetition

```python
print("Checking BTC")
print("Checking BTC")
print("Checking BTC")
```

Better:

```python
def check_market():
    print("Checking BTC")
```

Now you can reuse the function anytime.

---

# PART 2 — Understanding Functions Deeply

# What Is a Function?

A function is:

> A reusable block of code designed to perform one responsibility.

Functions help AI systems:

* stay organized,
* reduce repetition,
* scale larger projects,
* and improve debugging.

---

# Real AI System Example

A professional AI trading system may separate:

```text
get_market_data()
analyze_market()
store_memory()
send_alert()
execute_trade()
```

Each function has ONE responsibility.

---

# PART 3 — Create Reusable Functions

## Create:

```text
function_practice.py
```

Code:

```python
# Function to greet a user
def greet_user(name):

    # Print greeting message
    print(f"Welcome, {name}")

# Function to calculate BTC tax estimate
def calculate_tax(amount):

    # Calculate 10% sample tax
    tax = amount * 0.10

    # Return the calculated value
    return tax

# Call greeting function
greet_user("Simeon")

# Call tax function
result = calculate_tax(5000)

# Print returned value
print("Estimated Tax:", result)
```

Run:

```bash
python function_practice.py
```

---

# Concept Explanation — `return`

`return` sends information BACK from a function.

Example:

```python
return tax
```

This allows another part of the program to USE the result.

Without `return`,
the data disappears after the function finishes.

---

# PART 4 — Create a Modular BTC Agent

## Create:

```text
modular_btc_agent.py
```

Code:

```python
# Import required libraries
import requests
from datetime import datetime
import time

# Function to create timestamp
def get_timestamp():

    # Return formatted timestamp
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Function to retrieve BTC price
def get_btc_price():

    # Coinbase API endpoint
    url = "https://api.coinbase.com/v2/prices/spot?currency=USD"

    # Request BTC data
    response = requests.get(url, timeout=10)

    # Raise error if request failed
    response.raise_for_status()

    # Convert response to JSON
    data = response.json()

    # Extract BTC price
    btc_price = float(data["data"]["amount"])

    # Return BTC price
    return btc_price

# Function for AI market decision
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

# Function to save trade memory
def save_trade_memory(scan_number, timestamp, btc_price, decision):

    # Open trade memory file safely
    with open("trade_memory.txt", "a") as memory_file:

        # Save scan details
        memory_file.write(f"Scan Number: {scan_number}\n")
        memory_file.write(f"Timestamp: {timestamp}\n")
        memory_file.write(f"BTC Price: {btc_price}\n")
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
    with open("error_log.txt", "a") as error_file:

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

        # Save memory
        save_trade_memory(scan, timestamp, btc_price, decision)

        # Print results
        print(f"Scan Number: {scan}")
        print("Timestamp:", timestamp)
        print("BTC Price:", btc_price)
        print("AI Decision:", decision)

    except Exception as error:

        # Save error log
        save_error_log(error)

        # Print safe error message
        print("Error logged safely.")

    # Print separator
    print("----------------------")

    # Wait 5 seconds
    time.sleep(5)

# Print completion message
print("Modular AI monitoring completed.")
```

Run:

```bash
python modular_btc_agent.py
```

---

# Concept Explanation — Modular Programming

Modular programming means:

> Breaking a large system into smaller reusable components.

Instead of ONE giant file:
you organize responsibilities cleanly.

This improves:

* readability,
* debugging,
* scalability,
* and teamwork.

---

# Real Enterprise Example

Large AI systems may have:

```text
api_tools.py
memory_system.py
agent_logic.py
security.py
database.py
alerts.py
```

This is professional architecture.

---

# PART 5 — Understanding Abstraction

# What Is Abstraction?

Abstraction means:

> Hiding complexity behind simple reusable functions.

Example:

```python
btc_price = get_btc_price()
```

You do NOT need to think about:

* requests,
* JSON,
* API parsing,
* response handling.

The function hides the complexity.

---

# Why Abstraction Matters in AI

Modern AI frameworks heavily use abstraction:

* LangChain
* Semantic Kernel
* CrewAI
* AutoGen

These frameworks simplify complex workflows.

---

# PART 6 — Learn About Single Responsibility Principle

# Important Software Concept

A function should ideally:

## Do ONE thing well.

Examples:

| Function              | Responsibility    |
| --------------------- | ----------------- |
| `get_btc_price()`     | Retrieve BTC data |
| `market_agent()`      | Make AI decision  |
| `save_trade_memory()` | Save logs         |
| `save_error_log()`    | Save errors       |

This improves maintainability.

---

# PART 7 — Understanding Scalability

# What Is Scalability?

Scalability means:

> A system can grow larger without becoming unmanageable.

Your current system could later expand to:

* multiple cryptocurrencies,
* multiple AI agents,
* databases,
* dashboards,
* cloud deployment.

Modular systems scale MUCH better.

---

# DAY 10 CHECKLIST

## Concepts Understood

* [ ] Refactoring
* [ ] Modular programming
* [ ] Abstraction
* [ ] Reusability
* [ ] Single responsibility principle
* [ ] Scalability

## Coding

* [ ] function_practice.py
* [ ] modular_btc_agent.py

## Skills

* [ ] Comfortable creating reusable functions
* [ ] Comfortable separating responsibilities
* [ ] Comfortable organizing larger systems

---

# WHAT YOU LEARNED TODAY

Today you learned:

* professional code organization,
* modular architecture,
* reusable workflows,
* and scalable system design.

These concepts are foundational for:

* AI agents,
* cloud systems,
* enterprise AI,
* trading bots,
* and large-scale automation.

---

# REAL-WORLD CONNECTION

Professional AI engineering is NOT only about:

* “making code work.”

It is about:

* maintainability,
* scalability,
* reliability,
* and architecture quality.

Today you started thinking like:

## A systems engineer.

---

# BONUS TASK

Modify:

```text
modular_btc_agent.py
```

Add:

* ETH price monitoring
* Separate ETH decision logic
* ETH logging

This introduces:

## Multi-asset AI monitoring.

---

# ADVANCED THINKING QUESTION

Think about this:

> If your AI system grows to 100 different functions,
> how would you organize the project professionally?

Hint:

* folders,
* modules,
* packages,
* APIs,
* databases,
* and service layers.
