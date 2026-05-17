# Day 7 — Loops, Automation, and Building a Repeating AI Agent

## Goal for Today

Learn how AI systems:

* repeat tasks automatically,
* monitor data continuously,
* run scheduled workflows,
* and behave more like autonomous agents.

Today you will build your first repeating AI monitoring system.

Estimated time:

* 2.5–3 hours

---

# PART 1 — Review Day 6 (15 mins)

Run:

* `write_memory.py`
* `read_memory.py`
* `memory_agent.py`

Open:

```text id="j6v2qr"
trade_memory.txt
```

Observe:

* stored BTC prices,
* decisions,
* and logs.

---

# Concept Explanation — Why Memory + Automation Matter

A true AI agent does NOT just:

* answer once,
* then stop.

Real AI agents:

* monitor continuously,
* remember previous activity,
* repeat workflows,
* and react automatically.

Examples:

* Trading bots
* AI monitoring systems
* Chat assistants
* Security AI
* Enterprise copilots

---

# PART 2 — Understanding Loops (30 mins)

# What Is a Loop?

A loop allows code to:

> Repeat actions automatically.

Instead of:

```python id="m8q5vy"
print("Checking BTC")
print("Checking BTC")
print("Checking BTC")
```

You use:

```python id="n2w8xt"
for i in range(3):
    print("Checking BTC")
```

---

# Why Loops Matter in AI

AI systems constantly repeat actions:

* checking APIs,
* monitoring markets,
* scanning documents,
* analyzing conversations,
* watching sensors.

Without loops:
AI automation would not exist.

---

# Types of Loops

| Loop Type    | Purpose                        |
| ------------ | ------------------------------ |
| `for` loop   | Repeat a fixed number of times |
| `while` loop | Repeat until condition changes |

Today you will learn BOTH.

---

# PART 3 — Learn FOR Loops (45 mins)

# Create:

```text id="g4v9ks"
for_loop_practice.py
```

Code:

```python id="h3x7qp"
# This loop repeats 5 times
for i in range(5):

    # Print the current loop number
    print("AI Agent Scan Number:", i)
```

Run:

```bash id="z9m4tw"
python for_loop_practice.py
```

---

# Concept Explanation — Breaking Down the Code

---

## `for`

Starts a repeating loop.

---

## `i`

Temporary variable used during each repetition.

---

## `range(5)`

Means:

> Repeat 5 times.

Python counts:

```text id="c7q2zd"
0
1
2
3
4
```

---

# Real AI Example

An AI monitoring system may:

```python id="f6t8pr"
for stock in stock_list:
```

Meaning:

> Check every stock automatically.

---

# PART 4 — Learn WHILE Loops (45 mins)

# Create:

```text id="t2w6yn"
while_loop_practice.py
```

Code:

```python id="s5v9kx"
# Start counter at 0
counter = 0

# Repeat while counter is less than 5
while counter < 5:

    # Print current counter
    print("Monitoring BTC...", counter)

    # Increase counter by 1
    counter += 1
```

Run:

```bash id="u4n7qs"
python while_loop_practice.py
```

---

# Concept Explanation — What Is a While Loop?

A `while` loop repeats:

> As long as a condition remains TRUE.

Example:

```python id="b7x2vo"
while counter < 5
```

Means:

> Keep repeating until counter reaches 5.

---

# Why While Loops Matter in AI

Many AI agents run FOREVER:

* trading bots,
* AI assistants,
* monitoring systems,
* autonomous workflows.

Example:

```python id="r8m5zt"
while True:
```

Means:

> Run continuously.

VERY important in automation.

---

# PART 5 — Add Delays with Time Module (30 mins)

# What Is a Delay?

AI systems often pause between actions:

* checking APIs every minute,
* scanning markets every 15 seconds,
* monitoring systems hourly.

Without delays:
systems can overload APIs.

---

# Create:

```text id="w3q8rv"
time_delay.py
```

Code:

```python id="x9k4mp"
# Import Python time library
import time

# Repeat 3 times
for i in range(3):

    # Print monitoring message
    print("Checking market...")

    # Wait 2 seconds before continuing
    time.sleep(2)

print("Monitoring complete.")
```

Run:

```bash id="v2p6xs"
python time_delay.py
```

---

# Concept Explanation — `time.sleep(2)`

Means:

> Pause the program for 2 seconds.

Used heavily in:

* AI monitoring
* Trading bots
* Automation systems
* API scheduling

---

# PART 6 — Build a Repeating AI BTC Monitor (60 mins)

# Create:

```text id="p8x4zn"
btc_monitor_agent.py
```

Code:

```python id="m5q7tx"
# Import required libraries
import requests
import time

# Repeat monitoring 5 times
for i in range(5):

    # API endpoint for BTC price
    url = "https://api.coinbase.com/v2/prices/spot?currency=USD"

    # Request BTC data
    response = requests.get(url)

    # Convert response into JSON
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

    # Print separator line
    print("----------------------")

    # Wait 5 seconds before checking again
    time.sleep(5)

print("Monitoring session completed.")
```

Run:

```bash id="n4v8yc"
python btc_monitor_agent.py
```

---

# Concept Explanation — Workflow Thinking

Your AI agent now:

1. Retrieves live BTC data
2. Processes JSON
3. Makes decisions
4. Repeats automatically
5. Waits between actions

This is REAL automation architecture.

---

# PART 7 — Learn About Infinite Loops (20 mins)

# What Is an Infinite Loop?

Example:

```python id="t7m3zx"
while True:
```

Means:

> Repeat forever.

---

# WARNING

Infinite loops can:

* overload systems,
* spam APIs,
* freeze programs.

Professional developers use safeguards.

---

# Example Safe Infinite Loop

```python id="z4q8np"
import time

while True:

    print("AI agent running...")

    time.sleep(10)
```

This pauses safely.

---

# DAY 7 CHECKLIST

## Concepts Understood

* [ ] For loops
* [ ] While loops
* [ ] Infinite loops
* [ ] Time delays
* [ ] Automation workflows

## Coding

* [ ] for_loop_practice.py
* [ ] while_loop_practice.py
* [ ] time_delay.py
* [ ] btc_monitor_agent.py

## Skills

* [ ] Comfortable repeating tasks
* [ ] Comfortable adding delays
* [ ] Comfortable automating workflows

---

# WHAT YOU LEARNED TODAY

Today you learned:

* automation loops,
* repeating workflows,
* AI monitoring systems,
* scheduled behavior,
* and continuous execution.

These concepts are foundational for:

* AI agents
* Trading bots
* Monitoring systems
* Autonomous AI
* Enterprise automation

---

# REAL-WORLD CONNECTION

Your future AI systems may:

* monitor BTC 24/7,
* scan news continuously,
* watch server activity,
* automate business workflows,
* or coordinate multiple AI agents.

Loops are one of the MOST important automation concepts.

---

# BONUS (If Finished Early)

## Add Memory Logging

Modify:

```text id="g5r9xt"
btc_monitor_agent.py
```

So each BTC price:

* saves into a file,
* stores timestamp,
* and logs AI decisions.

---

# ADVANCED THINKING QUESTION

Think about this:

> If an AI agent can monitor continuously,
> how could it decide WHEN to take action automatically?

Hint:

* thresholds,
* probability,
* confidence,
* event triggers,
* and AI reasoning models.
