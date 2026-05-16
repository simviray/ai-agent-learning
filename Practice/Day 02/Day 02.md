# Day 2 — Python Fundamentals for AI Development

## Goal for Today

Learn the core Python skills every AI developer uses daily.

Estimated time:

* 2.5–3 hours

---

# PART 1 — Review Day 1 (15 mins)

Open VS Code and run again:

* `hello_ai.py`
* `btc_app.py`

Goal:

* Become comfortable running Python files

---

# PART 2 — Learn Core Python Concepts (75 mins)

## Study These Topics

From:
[CS50 Python](https://cs50.harvard.edu/python/?utm_source=chatgpt.com)

Focus on:

* Variables
* Data types
* Lists
* Dictionaries
* If statements
* Loops

---

# PART 3 — Practice Python Basics (60 mins)

## Exercise 1 — Favorite Crypto

Create:

```text id="gn9k5x"
favorite_crypto.py
```

Code:

```python id="n29h7n"
crypto = input("What is your favorite crypto? ")

print("Your favorite crypto is", crypto)
```

---

## Exercise 2 — AI Agent Loop

Create:

```text id="9p0xq4"
ai_loop.py
```

Code:

```python id="gx9i5u"
tasks = ["Analyze BTC", "Check news", "Send alert"]

for task in tasks:
    print("AI Agent Task:", task)
```

---

## Exercise 3 — Market Condition Checker

Create:

```text id="n7v2mc"
market_checker.py
```

Code:

```python id="u4pm4x"
btc_price = 98000

if btc_price >= 100000:
    print("Bull Market")
else:
    print("Waiting for breakout")
```

---

# PART 4 — Learn Lists & Dictionaries (30 mins)

## Create:

```text id="j4oe1w"
agent_memory.py
```

Code:

```python id="1c7hku"
agent = {
    "name": "BTC Agent",
    "model": "Qwen",
    "status": "Active"
}

print(agent["name"])
print(agent["model"])
print(agent["status"])
```

Goal:

* Understand how AI agents store memory/data

---

# PART 5 — Install Git (If Not Yet Installed)

Download:

[Git Download](https://git-scm.com/downloads?utm_source=chatgpt.com)

After installation:
Open terminal and run:

```bash id="7d5i2v"
git --version
```

---

# PART 6 — GitHub Practice (Optional)

Create repository:

```text id="pz6v5e"
ai-agent-learning
```

Upload your Python files.

---

# DAY 2 CHECKLIST

## Python Skills

* [ ] Variables
* [ ] Lists
* [ ] Dictionaries
* [ ] Loops
* [ ] If statements

## Coding

* [ ] favorite_crypto.py
* [ ] ai_loop.py
* [ ] market_checker.py
* [ ] agent_memory.py

## Tools

* [ ] Git installed
* [ ] GitHub account ready

---

# WHAT YOU LEARNED TODAY

Today you learned the SAME concepts used in:

* AI agents
* Trading bots
* Chatbots
* Automation systems

Especially:

* Lists → task queues
* Dictionaries → AI memory
* Loops → autonomous actions
* Conditions → AI decisions

---

# BONUS (If Finished Early)

Install:

* [Ollama](https://ollama.com?utm_source=chatgpt.com)

Then test in terminal:

```bash id="z5f5xj"
ollama --version
```

No need to download models yet.
