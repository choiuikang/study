# 경로 확인
import os

#필요한 라이브러리 호출
import pandas as pd
import numpy as np
import time
import datetime
import sys

stock_total = pd.read_csv("stock_list.csv")

# for i in range(len(stock_total)):
for i in range(5):    
    time.sleep(0.5)
    
    stock_code = stock_total['종목코드'][i]
    stock_name = stock_total['종목명'][i]
    market = stock_total['시장구분'][i]
    
#     stock_code = str(stock_code)
#     stock_name = str(stock_name)
#     market = str(market)
    
    # 현재 날짜
    now = datetime.datetime.now()
    
    # 로그
    log_df = pd.DataFrame({
        'stock_code':[stock_code],
        'stock_name':[stock_name],
        'market':[market],
        'time' : [now]
    })
    
    # 로그 csv
    log_df.to_csv("log.csv", mode = 'a', header=False)
    
    # 시스템 실행
    os.system("python3 stock_test.py" + " " +  stock_code + " " + stock_name + " " + market)
    
    