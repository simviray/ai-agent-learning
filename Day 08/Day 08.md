# Day 8 — Error Handling, Reliability, and Building Safer AI Agents

## Goal for Today

Learn how AI systems:

* handle failures,
* survive API problems,
* avoid crashes,
* and become more reliable.

Today you will build a safer AI monitoring system using error handling.

Estimated time:

* 2.5–3 hours

---

# PART 1 — Review Day 7 (15 mins)

Run:

* `for_loop_practice.py`
* `while_loop_practice.py`
* `btc_monitor_agent.py`

Observe:

* loops,
* automation,
* repeated monitoring.

---

# Concept Explanation — Why Reliability Matters

Real AI systems operate in unpredictable environments.

Problems happen constantly:

* internet failures,
* API outages,
* bad data,
* invalid inputs,
* server overloads.

Without protection:
AI systems crash.

Professional AI engineers design systems to:

* survive failures,
* recover gracefully,
* and continue operating safely.

---

# PART 2 — Understanding Errors in Python (30 mins)

# What Is an Error?

An error is:

> A problem that stops your program from running correctly.

Example:

```python id="u7m3xq"
print(price)
```

If `price` does not exist:
Python crashes.

---

# Common Types of Errors

| Error Type      | Meaning                 |
| --------------- | ----------------------- |
| SyntaxError     | Invalid Python code     |
| NameError       | Variable does not exist |
| TypeError       | Wrong data type         |
| ValueError      | Invalid value           |
| ConnectionError | API/network problem     |

---

# Why Errors Matter in AI Systems

AI systems rely heavily on:

* APIs,
* databases,
* cloud services,
* user input,
* external tools.

All of these can fail.

Error handling makes AI systems:

* safer,
* smarter,
* and production-ready.

---

# PART 3 — Learn TRY and EXCEPT (45 mins)

# What Is TRY/EXCEPT?

TRY/EXCEPT means:

> “Try running this code. If it fails, handle the error safely.”

---

# Create:

```text id="v5q8np"
error_handling.py
```

Code:

```python id="r3x7vt"
# TRY means attempt to run the code
try:

    # Ask user for a number
    number = int(input("Enter a number: "))

    # Print the number
    print("You entered:", number)

# EXCEPT runs if an error happens
except:

    # Print friendly error message
    print("Invalid input. Please enter a valid number.")
```

Run:

```bash id="w9m4xy"
python error_handling.py
```

Test:

* valid number
* invalid text

---

# Concept Explanation — TRY Block

```python id="n6v2ps"
try:
```

Means:

> Attempt this operation.

---

# Concept Explanation — EXCEPT Block

```python id="j4x8tr"
except:
```

Means:

> If something fails, run this code instead.

---

# Why AI Systems Need This

Without TRY/EXCEPT:

* one failure crashes the entire AI system.

With TRY/EXCEPT:

* systems recover safely.

---

# PART 4 — Handling API Failures (45 mins)

# Create:

```text id="f2v7qm"
safe_btc_checker.py
```

Code:

```python id="x8m3zp"
# Import required libraries
import requests

# TRY running the API workflow
try:

    # API endpoint
    url = "https://api.coinbase.com/v2/prices/spot?currency=USD"

    # Request BTC data
    response = requests.get(url)

    # Convert response into JSON
    data = response.json()

    # Extract BTC price
    btc_price = float(data["data"]["amount"])

    # Print BTC price
    print("BTC Price:", btc_price)

# Handle errors safely
except:

    # Print error message
    print("Failed to retrieve BTC data.")
```

Run:

```bash id="s5q9yn"
python safe_btc_checker.py
```

---

# Concept Explanation — Safe AI Systems

Professional AI systems NEVER assume:

* APIs always work,
* internet is always available,
* data is always valid.

Safe systems:

* validate inputs,
* handle failures,
* and continue running.

---

# PART 5 — Understanding Specific Errors (30 mins)

# Better Error Handling

Instead of:

```python id="k2x6tp"
except:
```

You can target specific errors.

---

# Create:

```text id="z7m4rv"
specific_errors.py
```

Code:

```python id="p8v3xy"
# TRY running the code
try:

    # Ask user for a number
    number = int(input("Enter a number: "))

    # Divide 100 by the number
    result = 100 / number

    # Print result
    print("Result:", result)

# Handle invalid number input
except ValueError:

    print("Please enter a valid number.")

# Handle division by zero
except ZeroDivisionError:

    print("Cannot divide by zero.")
```

Run:

```bash id="v4q7zn"
python specific_errors.py
```

Test:

* letters
* zero
* normal numbers

---

# Concept Explanation — Why Specific Errors Matter

Specific error handling gives:

* better debugging,
* safer systems,
* clearer logs,
* and more intelligent recovery.

Enterprise AI systems often log:

* exact failure types,
* timestamps,
* API problems,
* model failures.

---

# PART 6 — Build a Safer AI Monitoring Agent (60 mins)

# Create:

```text id="g6x2pm"
safe_monitor_agent.py
```

Code:

```python id="m9v5rt"
# Import required libraries
import requests
import time

# Repeat monitoring 5 times
for i in range(5):

    # TRY the monitoring workflow
    try:

        # API endpoint
        url = "https://api.coinbase.com/v2/prices/spot?currency=USD"

        # Request BTC data
        response = requests.get(url)

        # Convert API response into JSON
        data = response.json()

        # Extract BTC price
        btc_price = float(data["data"]["amount"])

        # Print BTC price
        print("BTC Price:", btc_price)

        # AI decision logic
        if btc_price >= 110000:

            print("AI Decision: Strong Buy")

        elif btc_price >= 100000:

            print("AI Decision: Buy")

        elif btc_price >= 90000:

            print("AI Decision: Hold")

        else:

            print("AI Decision: Risk Zone")

    # Handle possible failures
    except:

        # Print failure message
        print("Error retrieving market data.")

    # Print separator
    print("----------------------")

    # Wait 5 seconds
    time.sleep(5)

print("Monitoring completed.")
```

Run:

```bash id="y8q4nv"
python safe_monitor_agent.py
```

---

# Concept Explanation — Reliability Engineering

Today you moved closer to:

## Production-grade AI systems.

Professional AI engineers focus heavily on:

* uptime,
* recovery,
* stability,
* monitoring,
* and reliability.

A working AI system that crashes often is NOT useful.

---

# PART 7 — Understanding Defensive Programming (20 mins)

# What Is Defensive Programming?

Defensive programming means:

> Assume things can go wrong and prepare for it.

Examples:

* user enters wrong input,
* API returns bad data,
* server disconnects,
* model fails.

Professional AI systems always defend against failures.

---

# Example Real AI Failures

| Problem        | Example                    |
| -------------- | -------------------------- |
| API outage     | BTC API unavailable        |
| Bad JSON       | Missing fields             |
| Model timeout  | LLM stops responding       |
| Invalid prompt | User input breaks workflow |

Defensive programming reduces risk.

---

# DAY 8 CHECKLIST

## Concepts Understood

* [ ] Errors
* [ ] TRY/EXCEPT
* [ ] API safety
* [ ] Specific exceptions
* [ ] Defensive programming

## Coding

* [ ] error_handling.py
* [ ] safe_btc_checker.py
* [ ] specific_errors.py
* [ ] safe_monitor_agent.py

## Skills

* [ ] Comfortable handling failures
* [ ] Comfortable debugging errors
* [ ] Comfortable building safer systems

---

# WHAT YOU LEARNED TODAY

Today you learned:

* error handling,
* system reliability,
* safe API usage,
* defensive programming,
* and fault tolerance.

These concepts are foundational for:

* enterprise AI,
* cloud AI systems,
* autonomous agents,
* AI trading bots,
* and production AI platforms.

---

# REAL-WORLD CONNECTION

Professional AI systems must survive:

* internet failures,
* cloud outages,
* API rate limits,
* invalid inputs,
* and unexpected data.

Today you learned the FIRST layer of production reliability engineering.

---

# BONUS (If Finished Early)

## Add Error Logging

Modify:

```text id="x4q7vp"
safe_monitor_agent.py
```

So errors save into:

```text id="v9m2zy"
error_log.txt
```

Include:

* timestamp,
* error type,
* and failure message.

---

# ADVANCED THINKING QUESTION

Think about this:

> If an AI agent can recover from failures,
> what additional features would make it trustworthy for real businesses?

Hint:

* monitoring,
* audit logs,
* security,
* validation,
* fallback systems,
* human approval workflows.
