def ema(closes, in_position):
    import talib
    import numpy as np

    timeperiod = 100
    if len(closes) > timeperiod:
        closes = np.array(closes)

        ema = talib.EMA(closes, timeperiod=timeperiod)
        close_1 = closes[-1]
        close_2 = closes[-2]
        close_3 = closes[-3]
        close_4 = closes[-4]
        close_5 = closes[-5]

        ema_1 = ema[-1]
        ema_2 = ema[-2]
        ema_3 = ema[-3]
        ema_4 = ema[-4]
        ema_5 = ema[-5]

        if close_1 > ema_1 and close_2 > ema_2 and close_3 > ema_3 and close_4 > ema_4 and close_5 > ema_5 and not(in_position):
            return('Uptrend')
        elif close_1 < ema_1 and close_2 < ema_2 and close_3 < ema_3 and close_4 < ema_4 and close_5 < ema_5 and in_position:
            return('Downtrend') 
        else: 
            return('Notrend')

