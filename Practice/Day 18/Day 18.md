# Day 18 — Telegram Alerts and Real-Time AI Notifications

## Goal for Today

Upgrade your AI agent so it can send real-time Telegram alerts.

Today you will learn:

* Telegram bots
* sending API requests
* real-time notifications
* alert systems
* external integrations

Estimated time: **2.5–3 hours**

---

# PART 1 — Concept Explanation

Right now your AI agent:

* monitors assets,
* saves logs,
* creates reports.

But professional AI systems also:

```text
Send alerts automatically.
```

Examples:

* trading alerts
* AI warnings
* server notifications
* monitoring alerts
* business automation messages

Today you will build your first:

## Real-time notification system.

---

# PART 2 — Create a Telegram Bot

## Step 1 — Open Telegram

Search for:

Telegram

---

## Step 2 — Search for BotFather

Search:

```text
@BotFather
```

BotFather is the official Telegram bot creator.

---

## Step 3 — Create a New Bot

Send:

```text
/newbot
```

BotFather will ask:

* bot name
* bot username

Example:

```text
AI BTC Agent
ai_btc_agent_bot
```

---

## Step 4 — Save Your Bot Token

BotFather gives you something like:

```text
123456789:ABCxxxxxxxxxxxxxxxxxxxx
```

This is your:

## Telegram Bot API Token

Keep it private.

---

# PART 3 — Get Your Chat ID

## Step 1

Search for:

```text
@userinfobot
```

---

## Step 2

Start the bot.

It will show your:

```text
Chat ID
```

Example:

```text
123456789
```

Save it.

---

# Concept Explanation — Why Tokens Matter

Your Telegram token acts like:

## A password for your bot.

Anyone with your token can control your bot.

Never upload tokens to GitHub.

Always store them inside:

```text
.env
```

---

# PART 4 — Update `.env`

Add:

```text
TELEGRAM_BOT_TOKEN=YOUR_BOT_TOKEN
TELEGRAM_CHAT_ID=YOUR_CHAT_ID
```

Example:

```text
TELEGRAM_BOT_TOKEN=123456:ABCxyz
TELEGRAM_CHAT_ID=123456789
```

---

# PART 5 — Update `config.py`

Add:

```python
# Telegram settings from .env
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
```

---

# PART 6 — Create `telegram_alert.py`

Create:

```text
telegram_alert.py
```

Add this code:

```python
# Import requests for API calls
import requests

# Import Telegram settings from config
from config import (
    TELEGRAM_BOT_TOKEN,
    TELEGRAM_CHAT_ID
)

# Function to send Telegram alert
def send_telegram_message(message):

    # Telegram API URL
    url = (
        f"https://api.telegram.org/bot"
        f"{TELEGRAM_BOT_TOKEN}/sendMessage"
    )

    # Telegram message payload
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }

    # Send POST request to Telegram API
    response = requests.post(url, data=payload)

    # Raise error if request fails
    response.raise_for_status()

    # Print success message
    print("Telegram alert sent successfully.")

# Test the function
send_telegram_message("AI BTC Agent test alert.")
```

Run:

```bash
python telegram_alert.py
```

You should receive a Telegram message.

---

# Concept Explanation — POST Requests

Before, your AI used:

```python
requests.get()
```

to retrieve data.

Now you are using:

```python
requests.post()
```

to SEND data.

This is important.

AI systems both:

* receive information,
* and send actions/notifications.

---

# PART 7 — Integrate Telegram Alerts Into `main.py`

Add import:

```python
# Import Telegram alert function
from telegram_alert import send_telegram_message
```

---

# PART 8 — Add Alert Logic

Inside your monitoring loop, after the AI decision:

```python
# Send Telegram alert for Strong Buy
if decision == "Strong Buy":

    # Create alert message
    alert_message = (
        f"🚀 Strong Buy Alert\n"
        f"Asset: {asset['name']}\n"
        f"Price: {price}\n"
        f"Decision: {decision}"
    )

    # Send Telegram alert
    send_telegram_message(alert_message)
```

---

# Example Full Integration

Add this inside the `try:` block after printing results:

```python
# Send Telegram alert for Strong Buy
if decision == "Strong Buy":

    # Create Telegram alert message
    alert_message = (
        f"🚀 Strong Buy Alert\n"
        f"Asset: {asset['name']}\n"
        f"Price: {price}\n"
        f"Decision: {decision}"
    )

    # Send Telegram alert
    send_telegram_message(alert_message)
```

---

# Concept Explanation — Event-Driven Alerts

Your AI agent now reacts to conditions:

```text
IF Strong Buy
THEN Send Telegram Alert
```

This is called:

## Event-driven automation.

Professional systems use this everywhere:

* monitoring systems
* trading bots
* AI copilots
* cloud alerts
* business automation

---

# PART 9 — Add Error Protection to Telegram Alerts

Update `telegram_alert.py`

```python
# Import requests for API calls
import requests

# Import Telegram settings from config
from config import (
    TELEGRAM_BOT_TOKEN,
    TELEGRAM_CHAT_ID
)

# Function to send Telegram alert
def send_telegram_message(message):

    try:
        # Telegram API URL
        url = (
            f"https://api.telegram.org/bot"
            f"{TELEGRAM_BOT_TOKEN}/sendMessage"
        )

        # Telegram message payload
        payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": message
        }

        # Send POST request
        response = requests.post(url, data=payload, timeout=10)

        # Raise error if request fails
        response.raise_for_status()

        # Print success message
        print("Telegram alert sent successfully.")

    except Exception as error:

        # Print safe error message
        print("Telegram alert failed.")
        print(error)
```

---

# Concept Explanation — External Integrations

Your AI system now connects to:

## External services.

This is a major step.

Most professional AI systems integrate with:

* Slack
* Telegram
* Discord
* email
* APIs
* databases
* cloud platforms

---

# DAY 18 CHECKLIST

## Concepts Understood

* [ ] Telegram bots
* [ ] API tokens
* [ ] POST requests
* [ ] Real-time notifications
* [ ] Event-driven automation
* [ ] External integrations

## Coding

* [ ] Updated `.env`
* [ ] Updated `config.py`
* [ ] Created `telegram_alert.py`
* [ ] Updated `main.py`
* [ ] Sent Telegram test message
* [ ] Sent real Strong Buy alert

---

# What You Learned Today

Today your AI agent became interactive.

Instead of only:

* logging data,
* or printing results,

it can now:

## Notify you in real time.

This is a huge step toward:

* AI trading bots
* automation systems
* alert platforms
* enterprise AI workflows

---

# Bonus Task

Add alerts for:

* `Buy`
* `Risk Zone`

Use different emojis:

```text
🚀 Strong Buy
📈 Buy
⚠️ Risk Zone
```

Only send alerts once per scan per asset.
