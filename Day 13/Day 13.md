# Day 13 — Requirements File, Virtual Environment, and Clean Dependency Management

## Goal for Today

Learn how professional Python projects manage dependencies using:

* virtual environments
* `requirements.txt`
* clean installs
* reproducible project setup

Estimated time: **2.5–3 hours**

---

# PART 1 — Review Day 12

Your project should now look like this:

```text
ai_btc_agent/
│
├── .env
├── .gitignore
├── README.md
├── main.py
├── config.py
├── market_data.py
├── agent_logic.py
├── logger.py
│
└── logs/
    ├── trade_memory.txt
    └── error_log.txt
```

Run:

```bash
python main.py
```

---

# Concept Explanation — What Are Dependencies?

Dependencies are external packages your project needs to work.

Your project uses:

```text
requests
python-dotenv
```

These are not part of your own code.

They are tools your code depends on.

---

# PART 2 — Create a Virtual Environment

Inside your project folder, run:

```bash
python -m venv .venv
```

---

# Concept Explanation — What Is a Virtual Environment?

A virtual environment is an isolated Python workspace.

It keeps project packages separate from your whole computer.

This prevents problems like:

```text
Project A needs old package version.
Project B needs new package version.
```

With virtual environments, each project can have its own setup.

---

# PART 3 — Activate the Virtual Environment

## Windows PowerShell

```powershell
.venv\Scripts\Activate
```

## Command Prompt

```cmd
.venv\Scripts\activate.bat
```

## Mac/Linux

```bash
source .venv/bin/activate
```

When activated, you should see:

```text
(.venv)
```

before your terminal line.

---

# PART 4 — Install Dependencies

Run:

```bash
pip install requests python-dotenv
```

---

# Concept Explanation — What Is `pip`?

`pip` is Python’s package installer.

It installs tools and libraries your project needs.

Example:

```bash
pip install requests
```

means:

```text
Install the requests package so Python can call APIs.
```

---

# PART 5 — Create `requirements.txt`

Run:

```bash
pip freeze > requirements.txt
```

This creates:

```text
requirements.txt
```

---

# Concept Explanation — What Is `requirements.txt`?

`requirements.txt` is a list of packages your project needs.

Example:

```text
requests==2.32.3
python-dotenv==1.0.1
```

This helps another computer install the same dependencies.

---

# PART 6 — Update `.gitignore`

Open:

```text
.gitignore
```

Add:

```text
.env
logs/
__pycache__/
.venv/
```

---

# Concept Explanation — Why Ignore `.venv`?

You should NOT upload `.venv` to GitHub because it can be large and computer-specific.

Instead, upload:

```text
requirements.txt
```

Then others can recreate the environment.

---

# PART 7 — Test Reinstall Workflow

Deactivate your environment:

```bash
deactivate
```

Activate it again:

```powershell
.venv\Scripts\Activate
```

Then run:

```bash
pip install -r requirements.txt
python main.py
```

---

# Concept Explanation — `pip install -r requirements.txt`

This command means:

```text
Install everything listed in requirements.txt.
```

This is a professional setup workflow.

---

# PART 8 — Add a Small Environment Check Script

Create:

```text
check_environment.py
```

Code:

```python
# Import sys to check Python information
import sys

# Import requests to confirm it is installed
import requests

# Import dotenv to confirm python-dotenv is installed
import dotenv

# Print Python version
print("Python Version:", sys.version)

# Print requests package version
print("Requests Version:", requests.__version__)

# Print confirmation that dotenv loaded successfully
print("python-dotenv is installed and working.")
```

Run:

```bash
python check_environment.py
```

---

# Concept Explanation — Why Check Your Environment?

Environment checks help confirm:

```text
Python is working.
Packages are installed.
Project setup is correct.
```

This is useful before building larger AI systems.

---

# DAY 13 CHECKLIST

## Concepts Understood

* [ ] Dependencies
* [ ] Virtual environment
* [ ] `pip`
* [ ] `requirements.txt`
* [ ] `.gitignore`
* [ ] Reproducible setup

## Coding / Setup

* [ ] Created `.venv`
* [ ] Activated `.venv`
* [ ] Installed dependencies
* [ ] Created `requirements.txt`
* [ ] Updated `.gitignore`
* [ ] Created `check_environment.py`
* [ ] Ran `python main.py`

---

# What You Learned Today

Today you learned how to make your Python project easier to install, share, and maintain.

This is important for:

```text
AI agents
cloud deployment
GitHub projects
FastAPI apps
Docker containers
Azure AI apps
```

---

# Bonus Task

Update your `README.md` and add this section:

````markdown
# Setup Instructions

1. Create virtual environment:

```bash
python -m venv .venv
````

2. Activate virtual environment:

```powershell
.venv\Scripts\Activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run project:

```bash
python main.py
```

```

This makes your project easier for others to use.
```
