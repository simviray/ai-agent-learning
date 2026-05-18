# Function for market decision using flexible levels
def market_agent(price, strong_buy_level, buy_level, hold_level):

    # Strong Buy condition
    if price >= strong_buy_level:
        return "Strong Buy"

    # Buy condition
    elif price >= buy_level:
        return "Buy"

    # Hold condition
    elif price >= hold_level:
        return "Hold"

    # Risk Zone condition
    else:
        return "Risk Zone"