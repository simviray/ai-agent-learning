def btc_signal(price):

    if price >= 100000:
        return "Bullish"

    else:
        return "Bearish"