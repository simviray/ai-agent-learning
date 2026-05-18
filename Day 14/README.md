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
- Virtual environment support
- Dependency management using `requirements.txt`
- Git and GitHub integration

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
├── check_environment.py
├── git_notes.py
│
├── logs/
│   ├── trade_memory.txt
│   └── error_log.txt
│
└── .venv/