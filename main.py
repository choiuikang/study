# 경로 확인
import os

#필요한 라이브러리 호출
import pandas as pd
import numpy as np

import datetime
import sys

end_dt = datetime.datetime.now()

start_dt = end_dt - datetime.timedelta(days=1)


end_dt = str(end_dt.year) + str(end_dt.month) + str(end_dt.day)
start_dt = str(start_dt.year) + str(start_dt.month) + str(start_dt.day)


stock_total = pd.read_csv("stock_list.csv")

# for i in range(len(stock_total)):
for i in range(5):    
    stock_code = stock_total['종목코드'][i]
    stock_name = stock_total['종목명'][i]
    market = stock_total['시장구분'][i]
        
    os.system("python3 stock_crawler.py" + " " + start_dt + " " + end_dt + " " + stock_code + " " + stock_name + " " + market)