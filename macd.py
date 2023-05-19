def macd(closes, in_position, macds, macdsignals):
    import talib
    import numpy as np

    if len(closes) > 33:
        closes = np.array(closes)

        macd, macdsignal, macdhist = talib.MACD(closes, fastperiod=12, slowperiod=26, signalperiod=9)

        macds.append(macd)
        macdsignals.append(macdsignal)

        macd = macds[-1][-1]
        macdsignal = macdsignals[-1][-1]
        
        prev_macd = macds[-2][-1]
        prev_macdsignal = macdsignals[-2][-1]

        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print(f'macd: {macd}')
        print(f'macdsignal: {macdsignal}')
        print(f'prev_macd: {prev_macd}')
        print(f'prev_macdsignal: {prev_macdsignal}')
    
        if prev_macd < prev_macdsignal and macd > macdsignal and not(in_position):
            return True, macds, macdsignals
        
        else: 
            return False, macds, macdsignals



