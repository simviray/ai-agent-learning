# AI BTC Agent

## Project Purpose

This project is a beginner AI-style Bitcoin monitoring agent built with Python.

The system:
- retrieves live BTC price data from an API,
- analyzes market conditions,
- makes AI-style decisions,
- stores monitoring history,
- logs errors,
- and uses modular project architecture.

This project is part of AI Agent Developer Training.

---

# Features

- Live BTC price monitoring
- AI-style market decision logic
- Timestamped logging
- Error handling
- Configurable settings using `.env`
- Automatic logs folder creation
- Modular multi-file architecture

---

# Project Structure

```text
ai_btc_agent/
│
├── .env
├── main.py
├── config.py
├── market_data.py
├── agent_logic.py
├── logger.py
├── README.md
│
└── logs/
    ├── trade_memory.txt
    └── error_log.txt
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
- stores API URL,
- stores scan settings,
- stores BTC decision levels.

---

## market_data.py

Handles market API requests.

Responsibilities:
- retrieves BTC price data,
- processes API responses,
- converts JSON into usable Python data.

---

## agent_logic.py

Contains AI-style decision logic.

Responsibilities:
- analyzes BTC price,
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
- saves trade monitoring history,
- saves error logs.

---

## .env

Stores environment variables and project configuration.

Examples:
- API URLs
- scan delay
- price thresholds

---

# How to Install Dependencies

## Install Python Packages

Open terminal and run:

```bash
pip install requests python-dotenv
```

---

# How to Run the Project

Open terminal inside the project folder.

Run:

```bash
python main.py
```

---

# Example Output

```text
Scan Number: 1
Timestamp: 2026-05-17 10:30:00
BTC Price: 105000.50
AI Decision: Buy
```

---

# Logs

Monitoring logs are saved inside:

```text
logs/trade_memory.txt
```

Error logs are saved inside:

```text
logs/error_log.txt
```

---

# Future Improvements

Possible upgrades:
- ETH monitoring
- Multi-asset monitoring
- Technical indicators
- AI prediction models
- Database integration
- FastAPI backend
- Telegram alerts
- Azure AI integration
- OpenAI integration
- Local LLM integration with Ollama

---

# Technologies Used

- Python
- Requests
- python-dotenv
- pathlib
- REST APIs
- JSON
- File logging

---

# Learning Goals

This project teaches:
- modular programming,
- API integration,
- logging,
- environment variables,
- project architecture,
- and beginner AI agent workflows.
