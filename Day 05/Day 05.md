# Day 5 — APIs, AI Workflows, and Your First Real AI Data Project

## Goal for Today

Learn how AI systems:

* retrieve live data,
* process information,
* make decisions,
* and automate workflows.

Today you will build your first mini AI-style workflow using live crypto data.

Estimated time:

* 2.5–3 hours

---

# PART 1 — Review Day 4 (15 mins)

Run:

* `main.py`
* `json_practice.py`
* `btc_json_reader.py`

---

# Concept Explanation — Why Repetition Matters

Professional developers repeat workflows until they become automatic.

AI engineers constantly:

* read APIs,
* process JSON,
* debug data,
* and automate logic.

The goal is:

> Train your brain to think like a system builder.

---

# PART 2 — Understanding AI Workflows (30 mins)

# What Is an AI Workflow?

An AI workflow is:

> A sequence of automated steps that an AI system follows.

Example AI Trading Workflow:

```text id="7j5m2w"
1. Get BTC price
2. Analyze market
3. Generate signal
4. Save result
5. Send alert
```

AI systems are NOT magic.
They are structured workflows.

---

# Real AI Agent Architecture

Most AI agents follow this pattern:

```text id="v3q8tx"
Input → Processing → Decision → Action
```

Example:

```text id="k2p6dn"
Market Data → AI Analysis → Buy Signal → Execute Trade
```

This is the foundation of:

* AI trading bots
* ChatGPT agents
* Enterprise copilots
* Automation systems

---

# PART 3 — Install a Better API Tool (15 mins)

## Install Requests (if not yet installed)

Open terminal:

```bash id="b5x7tc"
pip install requests
```

---

# Concept Explanation — What Is a Library?

A library is:

> Prebuilt code created by other developers.

Instead of building everything from scratch:
you IMPORT tools.

Example:

```python
import requests
```

Means:

> “Use the requests library to access web APIs.”

AI developers constantly use libraries.

---

# PART 4 — Your First Real Data Project (60 mins)

# Create:

```text id="q9w4zn"
btc_price_checker.py
```

Code:

```python id="f4x7ru"
import requests

url = "https://api.coinbase.com/v2/prices/spot?currency=USD"

response = requests.get(url)

data = response.json()

btc_price = float(data["data"]["amount"])

print("Current BTC Price:", btc_price)

if btc_price >= 100000:
    print("Market Status: Bullish")

else:
    print("Market Status: Neutral")
```

Run:

```bash id="m2v8cs"
python btc_price_checker.py
```

---

# Concept Explanation — Breaking Down the Code

---

## `requests.get(url)`

Sends a request to the API.

Your program asks:

> “Please send BTC price data.”

---

## `response.json()`

Converts the API response into Python-readable data.

Most AI systems use JSON.

---

## `data["data"]["amount"]`

This extracts nested information.

JSON often contains layers like:

```json id="n4r7pk"
{
  "data": {
    "amount": "105000"
  }
}
```

Think of it like folders inside folders.

---

## `float()`

Converts text into a number.

Example:

```python
"105000"
```

becomes:

```python
105000.0
```

Why important?
AI systems must convert data into usable formats.

---

# PART 5 — Understanding Variables in AI Systems (20 mins)

## Example

```python
btc_price = 105000
```

A variable stores information.

AI agents store:

* prices,
* prompts,
* responses,
* memory,
* confidence scores,
* user inputs.

Variables are temporary memory containers.

---

# PART 6 — Create an AI Decision System (45 mins)

# Create:

```text id="r4y8jm"
market_ai_agent.py
```

Code:

```python id="h6v2qp"
import requests

url = "https://api.coinbase.com/v2/prices/spot?currency=USD"

response = requests.get(url)

data = response.json()

btc_price = float(data["data"]["amount"])

print("BTC Price:", btc_price)

def market_agent(price):

    if price >= 110000:
        return "Strong Buy"

    elif price >= 100000:
        return "Buy"

    elif price >= 90000:
        return "Hold"

    else:
        return "Risk Zone"

decision = market_agent(btc_price)

print("AI Agent Decision:", decision)
```

---

# Concept Explanation — Decision Trees

This:

```python
if
elif
else
```

is called conditional logic.

AI systems use conditional logic constantly.

Example:

* If confidence high → trade
* If confidence low → wait
* If risk high → stop

This is foundational AI reasoning.

---

# PART 7 — Learn About Debugging (15 mins)

# What Is Debugging?

Debugging means:

> Finding and fixing problems in code.

ALL developers debug constantly.

---

# Common Beginner Errors

## Missing Colon

Wrong:

```python
if price > 100000
```

Correct:

```python
if price > 100000:
```

---

## Indentation Errors

Python uses spacing structure.

Wrong:

```python
if True:
print("Hello")
```

Correct:

```python
if True:
    print("Hello")
```

---

# Concept Explanation — Why Python Uses Indentation

Indentation defines:

* hierarchy,
* structure,
* and execution flow.

Python forces clean readable code.

---

# DAY 5 CHECKLIST

## Concepts Understood

* [ ] AI workflows
* [ ] Variables
* [ ] Conditional logic
* [ ] API data extraction
* [ ] Debugging basics

## Coding

* [ ] btc_price_checker.py
* [ ] market_ai_agent.py

## Skills

* [ ] Comfortable reading API data
* [ ] Comfortable extracting JSON values
* [ ] Comfortable using conditions

---

# WHAT YOU LEARNED TODAY

Today you learned:

* How AI systems retrieve live data
* How AI workflows operate
* How AI makes decisions
* How APIs power automation

These concepts are used in:

* AI trading systems
* Chatbots
* Autonomous agents
* Enterprise AI
* Azure AI orchestration

---

# REAL-WORLD CONNECTION

Your future AI trading system will:

1. Retrieve market data
2. Analyze conditions
3. Make AI decisions
4. Trigger alerts or trades

You just built the EARLY version of that architecture.

---

# BONUS (If Finished Early)

## Install Postman

[Postman](https://www.postman.com/downloads/?utm_source=chatgpt.com)

---

# Why Postman Matters

Postman helps developers:

* test APIs,
* inspect JSON,
* debug requests,
* simulate AI integrations.

Professional AI engineers use tools like this daily.

---

# ADVANCED THINKING QUESTION

Think about this:

> If an AI agent can retrieve data and make decisions,
> what additional capabilities would it need to become autonomous?

Hint:

* memory,
* planning,
* tools,
* reasoning,
* action execution.
