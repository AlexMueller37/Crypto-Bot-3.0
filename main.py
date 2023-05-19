from make_order import order 
from macd import macd 
from ema import ema

import requests
from time import sleep

TRADE_SYMBOL = 'BTCUSD'

url = f'https://api.binance.us/api/v3/ticker?symbol={TRADE_SYMBOL}'

closes = []
in_position = False

TRADE_QUANTITY = 1

API_KEY = 'PKEACEMDMC69HGLPAKU0'
SECRET_KEY = 'SdWuBij5goM1FacHxGBVZPgfObz3X4lg2n0F5Evl'

macds = [0]
macdsignals = [0]

counter = 0

macd_total=False
ema_total=False

while True: 
    counter += 1 

    response = requests.get(url)
    response = response.json()

    close = response['lastPrice']
    closes.append(float(close))

    last_price = closes[-1]

    print(f'candle closed at {close}')

    #
    try:
        macds = macd(closes, in_position, macds, macdsignals)[1]
    except TypeError:
        pass
    try:
        macdsignals = macd(closes, in_position, macds, macdsignals)[2]
    except TypeError:
        pass
    try:
        macd_total = macd(closes, in_position, macds, macdsignals)[0]
    except TypeError:
        pass

    try:
        ema_total = ema(closes, in_position)
    except TypeError:
        pass
    #

    if macd_total and  ema_total == 'Uptrend': 
        print('Buying...')
        order(TRADE_SYMBOL, TRADE_QUANTITY, 'buy', 'market', 'gtc', API_KEY, SECRET_KEY)
        print('Success!')
        in_position = True

    print(f'Currently Holding : {in_position}')
    print(f'Counter # : {counter}')
    print('-------------------------------------------------------------------------------------------')    
    print(f'Macd: {macd_total}')
    print(f'EMA: {ema_total}')
    print('===========================================================================================')
        
    sleep(5)
