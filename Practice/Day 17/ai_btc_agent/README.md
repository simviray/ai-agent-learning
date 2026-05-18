# AI BTC Agent

## Project Purpose

This project is a beginner AI-style multi-asset monitoring agent built with Python.

The system:
- retrieves live crypto price data from APIs,
- analyzes market conditions,
- makes AI-style decisions,
- stores monitoring history,
- logs errors,
- generates reports,
- and uses modular project architecture.

This project is part of AI Agent Developer Training.

---

# Features

- Live BTC monitoring
- Live ETH monitoring
- Live SOL monitoring
- Live XRP monitoring
- AI-style market decision logic
- Timestamped logging
- Error handling
- Configurable settings using `.env`
- Automatic logs folder creation
- Modular multi-file architecture
- Virtual environment support
- Dependency management using `requirements.txt`
- Git and GitHub integration
- Reporting system
- Scalable multi-asset design

---

# Project Structure

```text
ai_btc_agent/
│
├── .env
├── .gitignore
├── README.md
├── requirements.txt
├── main.py
├── config.py
├── market_data.py
├── agent_logic.py
├── logger.py
├── report.py
├── daily_report.py
├── check_environment.py
├── git_notes.py
│
├── logs/
│   ├── trade_memory.txt
│   ├── error_log.txt
│   └── daily_report.txt
│
└── .venv/
```

---

# What Each File Does

## main.py

The main entry point of the application.

Responsibilities:
- runs the monitoring loop,
- connects all modules together,
- controls scan execution.

---

## config.py

Stores project configuration and settings.

Responsibilities:
- loads `.env` settings,
- creates log folder paths,
- stores API URLs,
- stores scan settings,
- stores asset decision levels,
- stores centralized asset configuration.

---

## market_data.py

Handles market API requests.

Responsibilities:
- retrieves crypto price data,
- processes API responses,
- converts JSON into usable Python data.

---

## agent_logic.py

Contains AI-style decision logic.

Responsibilities:
- analyzes asset prices,
- returns market decisions:
  - Strong Buy
  - Buy
  - Hold
  - Risk Zone

---

## logger.py

Handles logging and memory storage.

Responsibilities:
- creates timestamps,
- saves monitoring history,
- saves error logs.

---

## report.py

Prints a summary report in the terminal.

Responsibilities:
- reads monitoring logs,
- counts decisions,
- displays summary statistics.

---

## daily_report.py

Generates and saves daily reports.

Responsibilities:
- creates report summaries,
- saves reports into:
  - `logs/daily_report.txt`

---

## check_environment.py

Checks whether:
- Python is installed correctly,
- required packages are installed,
- and the project environment is working properly.

---

## git_notes.py

Stores common Git command references for beginner developers.

---

## .env

Stores environment variables and project configuration.

Examples:
- API URLs
- scan delay
- price thresholds

---

## requirements.txt

Stores all required Python packages for the project.

Used to recreate the environment quickly.

---

# Setup Instructions

## 1. Create Virtual Environment

Open terminal inside the project folder and run:

```bash
python -m venv .venv
```

---

## 2. Activate Virtual Environment

### Windows PowerShell

```powershell
.venv\Scripts\Activate
```

### Windows Command Prompt

```cmd
.venv\Scripts\activate.bat
```

### Mac/Linux

```bash
source .venv/bin/activate
```

After activation, you should see:

```text
(.venv)
```

before your terminal line.

---

## 3. Install Dependencies

Run:

```bash
pip install -r requirements.txt
```

This installs all required project packages automatically.

---

# Required Packages

This project uses:

- requests
- python-dotenv

---

# How to Run the Project

Start the AI multi-asset monitoring agent:

```bash
python main.py
```

---

# Monitored Assets

This project currently monitors:

- BTC
- ETH
- SOL
- XRP

---

# How to Run Environment Check

Run:

```bash
python check_environment.py
```

This confirms:
- Python works,
- packages are installed,
- and the environment is configured correctly.

---

# Example Output

```text
Scan Number: 1
Timestamp: 2026-05-17 10:30:00
Asset: BTC
Price: 105000.50
AI Decision: Buy
```

---

# Logs

Monitoring logs:

```text
logs/trade_memory.txt
```

Error logs:

```text
logs/error_log.txt
```

Daily reports:

```text
logs/daily_report.txt
```

---

## Reports

This project includes reporting tools for analyzing AI agent activity.

### report.py

Prints a summary report directly in the terminal.

The report includes:
- total decisions,
- Strong Buy count,
- Buy count,
- Hold count,
- Risk Zone count.

Run:

```bash
python report.py
```

---

### daily_report.py

Generates and saves a report inside:

```text
logs/daily_report.txt
```

The report includes:
- timestamp,
- total decisions,
- decision summaries,
- and monitoring statistics.

Run:

```bash
python daily_report.py
```

---

### Example Report Output

```text
AI Agent Performance Report
---------------------------
Total Decisions: 20
Strong Buy: 3
Buy: 8
Hold: 6
Risk Zone: 3
```

---

# Deactivate Virtual Environment

When finished working:

```bash
deactivate
```

---

# .gitignore

Recommended `.gitignore`:

```text
.env
logs/
__pycache__/
.venv/
```

---

# Git Workflow

## Check Project Status

View current project changes:

```bash
git status
```

---

## Stage Changes

Prepare files for the next commit:

```bash
git add .
```

---

## Commit Changes

Save a snapshot of your project:

```bash
git commit -m "Describe your update"
```

Example:

```bash
git commit -m "Added XRP monitoring support"
```

---

## Push to GitHub

Upload your commits to GitHub:

```bash
git push
```

---

## Recommended Daily Workflow

```bash
git status
git add .
git commit -m "Describe your update"
git push
```

---

## Why Git Workflow Matters

Git helps developers:
- track project history,
- restore old versions,
- collaborate safely,
- and manage professional software projects.

This workflow is commonly used in:
- AI engineering
- cloud development
- enterprise software
- DevOps
- open-source projects

---

# Future Improvements

Possible upgrades:
- ADA monitoring
- DOGE monitoring
- Technical indicators
- AI prediction models
- Database integration
- FastAPI backend
- Telegram alerts
- Azure AI integration
- OpenAI integration
- Local LLM integration with Ollama
- Multi-agent AI systems
- Real-time dashboards

---

# Technologies Used

- Python
- Requests
- python-dotenv
- pathlib
- REST APIs
- JSON
- File logging
- Git
- GitHub

---

# Learning Goals

This project teaches:
- modular programming,
- API integration,
- logging,
- environment variables,
- project architecture,
- dependency management,
- Git workflow,
- reporting systems,
- and beginner AI agent workflows.

---

# Author

AI Agent Developer Training Project
by Simeon Viray