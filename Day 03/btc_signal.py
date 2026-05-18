def btc_signal(price):

    if price >= 100000:
        return "Bullish"

    else:
        return "Bearish"

signal = btc_signal(105000)

print("BTC Market Signal:", signal)