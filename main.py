import yfinance as yf
from time import sleep
import os
value_preview = 133.0
while True:
    data = yf.download(tickers = 'USDJPY=X' ,period ='1d', interval = '1m')
    os.system('cls')
    open=data['Open']
    value = open[-1]
    value = float(value)
    value = round(value,3)

    if value_preview < value:
        os.system('clear')
        os.system('color 0A')
        os.system('cls')
        print(" ↑",value)
    else:
        os.system('color 0C')
        os.system('cls')
        print(" ↓",value)

    sleep(1)
    value_preview = value