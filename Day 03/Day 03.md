# Day 3 — Functions, APIs, and Your First AI Developer Workflow

## Goal for Today

Learn how developers organize code and connect Python to real-world data.

Estimated time:

* 2.5–3 hours

---

# PART 1 — Review Day 2 (15 mins)

Run these files again:

* `favorite_crypto.py`
* `ai_loop.py`
* `market_checker.py`
* `agent_memory.py`

Goal:

* Build coding confidence through repetition

---

# PART 2 — Learn Python Functions (60 mins)

## Study Topics

From:
[CS50 Python](https://cs50.harvard.edu/python/?utm_source=chatgpt.com)

Focus on:

* Functions
* Parameters
* Return values
* Reusable code

---

# PART 3 — Create Your First Functions (45 mins)

## Exercise 1 — AI Greeting Function

Create:

```text id="wq3f8k"
ai_greeting.py
```

Code:

```python id="m4z2kp"
def greet_user(name):
    print("Welcome to AI development,", name)

greet_user("Simeon")
```

Run:

```bash id="z4r1pd"
python ai_greeting.py
```

---

## Exercise 2 — BTC Signal Function

Create:

```text id="j8x2vn"
btc_signal.py
```

Code:

```python id="f0n7dt"
def btc_signal(price):

    if price >= 100000:
        return "Bullish"

    else:
        return "Bearish"

signal = btc_signal(105000)

print("BTC Market Signal:", signal)
```

Goal:

* Understand AI decision-making logic

---

# PART 4 — Learn APIs (IMPORTANT) (45 mins)

## What is an API?

APIs allow your AI agent to:

* Get BTC prices
* Read news
* Send messages
* Execute trades
* Connect to Azure/OpenAI

This is one of the MOST important skills.

---

## Install Requests Library

Open terminal:

```bash id="i8g0xq"
pip install requests
```

---

# PART 5 — Your First API Call (45 mins)

## Create:

```text id="1u6rzd"
btc_api.py
```

Code:

```python id="2v6mwd"
import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

response = requests.get(url)

print(response.status_code)
print(response.text)
```

Run:

```bash id="jk4m8w"
python btc_api.py
```

Goal:

* See live data from the internet

This is EXACTLY how AI agents connect to tools and services.

---

# PART 6 — Install GitHub Copilot Extension (Optional)

Inside VS Code:

* Extensions
* Search:

  * GitHub Copilot

Install it.

This will help speed up coding later.

---

# DAY 3 CHECKLIST

## Python

* [ ] Learned functions
* [ ] Learned parameters
* [ ] Learned return values

## Coding

* [ ] ai_greeting.py
* [ ] btc_signal.py
* [ ] btc_api.py

## Tools

* [ ] Installed requests
* [ ] Tested first API call

---

# WHAT YOU LEARNED TODAY

Today you learned:

* Reusable code with functions
* How AI systems make decisions
* How APIs work
* How AI agents connect to the outside world

These are CORE AI developer skills.

---

# REAL-WORLD CONNECTION

Your future AI trading system will use:

* APIs for market data
* Functions for strategy logic
* Conditions for trade decisions
* AI models for predictions

You are now starting the REAL developer workflow.

---

# BONUS (If Finished Early)

Install:

* [Postman](https://www.postman.com/downloads/?utm_source=chatgpt.com)

Learn basic API testing.

This becomes VERY useful later for:

* Azure AI
* OpenAI APIs
* Trading APIs
* Agent tools
