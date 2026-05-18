# Day 6 — Files, Persistent Memory, and Building a Simple AI Agent

## Goal for Today

Learn how AI systems:

* save information,
* remember past actions,
* store logs,
* and maintain persistent memory.

Today you will build your first simple AI-style memory system.

Estimated time:

* 2.5–3 hours

---

# PART 1 — Review Day 5 (15 mins)

Run:

* `btc_price_checker.py`
* `market_ai_agent.py`

---

# Concept Explanation — Why Review Matters

AI engineering is not just about writing code once.

Professional developers:

* improve systems,
* test repeatedly,
* refine logic,
* and verify outputs.

Repetition builds:

* speed,
* confidence,
* and debugging ability.

---

# PART 2 — Understanding AI Memory (30 mins)

# What Is Memory in AI?

Memory allows AI systems to:

* remember conversations,
* track previous actions,
* store decisions,
* and maintain context.

Without memory:
AI agents forget everything after each action.

---

# Example Without Memory

```text id="d2q5nv"
User: What is BTC price?
AI: 105000

User: What did I ask earlier?
AI: I don't know.
```

---

# Example With Memory

```text id="b7p4rz"
User: What is BTC price?
AI: 105000

User: What did I ask earlier?
AI: You asked about BTC price.
```

---

# Types of AI Memory

| Type              | Purpose              |
| ----------------- | -------------------- |
| Short-term memory | Current conversation |
| Long-term memory  | Stored knowledge     |
| Vector memory     | Semantic retrieval   |
| File memory       | Saved logs/data      |

Today you start with:

## File-based memory.

---

# PART 3 — Learn File Handling (45 mins)

# What Is File Handling?

File handling means:

> Reading and writing information to files.

AI systems use files to:

* save logs,
* store history,
* keep records,
* and maintain memory.

---

# Create:

```text id="j4n8yx"
write_memory.py
```

Code:

```python id="y6k2rt"
memory = open("agent_memory.txt", "w")

memory.write("BTC price checked.\n")
memory.write("AI decision: Buy\n")

memory.close()

print("Memory saved.")
```

Run:

```bash id="p8v2cz"
python write_memory.py
```

---

# Concept Explanation — Breaking Down the Code

---

## `open()`

Opens or creates a file.

Example:

```python id="z6v9od"
open("agent_memory.txt", "w")
```

---

## `"w"`

Means:

## Write mode

It creates or overwrites the file.

---

## `.write()`

Adds text into the file.

---

## `\n`

Means:

## New line

Without it:
everything appears on one line.

---

## `.close()`

Closes the file safely.

Professional systems close resources properly.

---

# PART 4 — Read Stored Memory (30 mins)

# Create:

```text id="g3r7xt"
read_memory.py
```

Code:

```python id="s4w9ph"
memory = open("agent_memory.txt", "r")

content = memory.read()

print(content)

memory.close()
```

Run:

```bash id="v2x6jm"
python read_memory.py
```

---

# Concept Explanation — `"r"`

Means:

## Read mode

The program reads stored data.

---

# Why Reading Matters in AI

AI systems constantly:

* retrieve memory,
* analyze stored history,
* and reuse information.

Examples:

* Chat history
* Trade logs
* User preferences
* AI reasoning history

---

# PART 5 — Build a Simple AI Memory Agent (60 mins)

# Create:

```text id="f5m8qw"
memory_agent.py
```

Code:

```python id="q2n7vd"
import requests

url = "https://api.coinbase.com/v2/prices/spot?currency=USD"

response = requests.get(url)

data = response.json()

btc_price = float(data["data"]["amount"])

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

memory = open("trade_memory.txt", "a")

memory.write(f"BTC Price: {btc_price}\n")
memory.write(f"Decision: {decision}\n")
memory.write("----------------------\n")

memory.close()

print("AI Agent Decision:", decision)
print("Memory stored successfully.")
```

Run multiple times.

Then open:

```text id="c6y3mp"
trade_memory.txt
```

---

# Concept Explanation — `"a"`

Means:

## Append mode

Instead of overwriting:
the program ADDS new information.

This is critical for:

* AI logs
* Chat history
* Audit trails
* Trading history

---

# Real AI Example

ChatGPT-style systems often:

* append conversations,
* store prompts,
* save responses,
* track actions.

Exactly like this idea.

---

# PART 6 — Understanding Logs (20 mins)

# What Are Logs?

Logs are records of system activity.

AI systems log:

* actions,
* errors,
* prompts,
* outputs,
* decisions.

---

# Example AI Trading Log

```text id="x8q4kv"
BTC Price: 105000
Decision: Buy
Time: 8:00 PM
```

Logs help developers:

* debug,
* analyze,
* and improve systems.

---

# PART 7 — Learn About Automation Thinking (20 mins)

# Important Concept

AI systems are:

## Automated workflows with intelligence.

Most systems follow:

```text id="z2v5rw"
Input
↓
Processing
↓
Decision
↓
Memory
↓
Action
```

Your project today already includes:

* Input → BTC API
* Processing → Python logic
* Decision → Buy/Hold
* Memory → File logging

This is EARLY AI agent architecture.

---

# DAY 6 CHECKLIST

## Concepts Understood

* [ ] AI memory
* [ ] File handling
* [ ] Logging
* [ ] Read/write modes
* [ ] Append mode

## Coding

* [ ] write_memory.py
* [ ] read_memory.py
* [ ] memory_agent.py

## Skills

* [ ] Comfortable saving files
* [ ] Comfortable reading files
* [ ] Comfortable storing AI decisions

---

# WHAT YOU LEARNED TODAY

Today you learned:

* Persistent memory
* File storage
* AI logging
* Data history tracking

These concepts are foundational for:

* AI agents
* Chatbots
* Trading bots
* Autonomous systems
* Enterprise AI auditing

---

# REAL-WORLD CONNECTION

Enterprise AI systems often store:

* prompts,
* user history,
* AI outputs,
* actions,
* tool usage,
* compliance logs.

You are now learning the SAME architecture principles.

---

# BONUS (If Finished Early)

## Create Timestamped Logs

Research:

```python id="m4v8xo"
from datetime import datetime
```

Try adding timestamps into:

```text id="s7y2dz"
trade_memory.txt
```

---

# ADVANCED THINKING QUESTION

Think about this:

> If an AI system can remember past actions,
> how could memory improve future decisions?

This idea becomes VERY important later in:

* RAG systems
* Vector databases
* Autonomous agents
* Multi-agent collaboration
* Long-term AI reasoning
