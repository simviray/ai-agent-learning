# Day 4 — Python Modules, JSON, and AI Data Handling

## Goal for Today

Learn how AI applications organize files and process structured data.

Estimated time:

* 2.5–3 hours

---

# PART 1 — Review Day 3 (15 mins)

Run again:

* `ai_greeting.py`
* `btc_signal.py`
* `btc_api.py`

Goal:

* Become comfortable reading and understanding your own code

---

# PART 2 — Learn Python Modules (45 mins)

## Study Topics

Learn:

* Importing modules
* Using libraries
* Reusing code
* Organizing projects

Why important?
AI agents depend heavily on:

* External libraries
* AI SDKs
* APIs
* Tool integrations

---

# PART 3 — Create Your First Python Module (45 mins)

## Create:

```text id="hh8c4f"
crypto_tools.py
```

Code:

```python id="tf3r2m"
def btc_signal(price):

    if price >= 100000:
        return "Bullish"

    else:
        return "Bearish"
```

---

## Create:

```text id="p1m7qy"
main.py
```

Code:

```python id="q9f2xs"
from crypto_tools import btc_signal

signal = btc_signal(95000)

print("BTC Signal:", signal)
```

Run:

```bash id="yt4w5s"
python main.py
```

Goal:

* Understand how large AI projects are structured

---

# PART 4 — Learn JSON (VERY IMPORTANT) (60 mins)

## What is JSON?

JSON is used everywhere in AI:

* OpenAI responses
* Azure AI
* Trading APIs
* Agent memory
* Web applications

You MUST understand JSON.

---

## Create:

```text id="q2s5la"
json_practice.py
```

Code:

```python id="f7t4kp"
import json

agent_data = {
    "agent_name": "BTC AI Agent",
    "model": "Qwen",
    "status": "Active",
    "confidence": 92
}

json_data = json.dumps(agent_data, indent=4)

print(json_data)
```

Run:

```bash id="c7v3yb"
python json_practice.py
```

---

# PART 5 — Read API JSON Data (45 mins)

## Create:

```text id="j0p4nt"
btc_json_reader.py
```

Code:

```python id="v5x8dc"
import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

response = requests.get(url)

data = response.json()

print(data)
```

Goal:

* Learn how AI systems process external data

---

# PART 6 — Beginner VS Code Skills (15 mins)

Practice:

* Open terminal
* Create files
* Save projects
* Run Python scripts

You are building real developer habits now.

---

# DAY 4 CHECKLIST

## Python Concepts

* [ ] Modules
* [ ] Imports
* [ ] JSON basics
* [ ] API JSON reading

## Coding

* [ ] crypto_tools.py
* [ ] main.py
* [ ] json_practice.py
* [ ] btc_json_reader.py

## Skills

* [ ] Comfortable running Python files
* [ ] Comfortable editing code in VS Code

---

# WHAT YOU LEARNED TODAY

Today you learned:

* How AI systems organize code
* How APIs send structured data
* How JSON works
* How AI agents process information

This is foundational for:

* Azure AI
* LangChain
* OpenAI APIs
* AI trading bots
* RAG systems

---

# REAL-WORLD CONNECTION

Your future AI agents will:

* Receive JSON from APIs
* Process structured data
* Store AI memory
* Pass information between tools

JSON is one of the MOST IMPORTANT AI developer skills.

---

# BONUS (If Finished Early)

## Install Ollama

[Ollama](https://ollama.com?utm_source=chatgpt.com)

Then test:

```bash id="k4u9ps"
ollama --version
```

---

## Optional Reading

Learn:

* What is REST API?
* What is JSON?
* What is an endpoint?

These concepts will become VERY important soon.
