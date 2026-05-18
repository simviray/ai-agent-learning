# Import price threshold settings from config
from config import (
    BTC_BUY_LEVEL,
    BTC_STRONG_BUY_LEVEL,
    BTC_HOLD_LEVEL
)

# Function for AI market decision
def market_agent(price):

    # Strong Buy condition
    if price >= BTC_STRONG_BUY_LEVEL:
        return "Strong Buy"

    # Buy condition
    elif price >= BTC_BUY_LEVEL:
        return "Buy"

    # Hold condition
    elif price >= BTC_HOLD_LEVEL:
        return "Hold"

    # Risk Zone condition
    else:
        return "Risk Zone"