import tradingview_ta 
import data_storage
from tradingview_ta import TA_Handler, Interval, Exchange

def get_summary(stock, exchange="IDX", screener="indonesia", interval="1M"):
    handler = TA_Handler(
        symbol=stock,
        exchange=exchange,
        screener=screener,
        interval=interval
    )
    return(handler.get_analysis().summary)

idx_list = data_storage.idx_list

buy_list = []
strong_buy_list = []

for i in idx_list:
    try: 
        summary = get_summary(i)
        if summary['RECOMMENDATION'] == 'BUY' :
            buy_list.append(i)
        elif summary['RECOMMENDATION'] == 'STRONG_BUY':
            strong_buy_list.append(i)
        print(f"stock:{i} done")
    except:
        print(f"stock:{i} fails")
        pass
    
f = open("buy_list.txt", "w")
f.write(str(buy_list))
f.close()

f = open("strong_buy_list.txt", "w")
f.write(str(strong_buy_list))
f.close()
