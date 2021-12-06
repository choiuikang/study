#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
import pandas as pd
import time
from pykrx import stock


# In[5]:


stock_total = pd.read_csv("stock_list.csv")


# In[7]:


start_day = "20111201"
end_day = "20211201"


# In[6]:


# stock_df_total = pd.DataFrame()
# for i in range(len(stock_total)):
for i in range(5):    
    stock_code = stock_total['종목코드'][i]
    stock_name = stock_total['종목명'][i]
    market = stock_total['시장구분'][i]
    
 #stock.get_market_ohlcv_by_date 주식데이터 시작일,종료일,티커 파라미터를 넣어주면 일자별로 정렬하여 DataFrame으로 반환한다.
    stock_df = stock.get_market_ohlcv_by_date(fromdate=start_day, todate=end_day, ticker=stock_code) 
    # 위 데이터를 가져오면 날짜,시가,고가,저가,..등만 나오므로 칼럼을 추가해주도록 하자.
    stock_df["종목명"] = stock_name 
    stock_df["종목코드"] = stock_code
    stock_df["시장구분"] = market
        
    stock_df = stock_df.reset_index()
    time.sleep(0.5)
    print(stock_name)
    
    if not os.path.exists('stock_df_total_3.csv'):
        stock_df.to_csv('stock_df_total_3.csv', index=False, mode='w')
    else:
        stock_df.to_csv('stock_df_total_3.csv', index=False, mode='a', header=False)
    #time.sleep(0.5) # time.sleep(1) 1초마다 데이터 실행 (데이터가 많으면 한꺼번에 처리하려해 서버 팅길수 있으므로 설정 )
#     print(str(i) + " 번째 "+ stock_name) # 잘 실행되는지 확인하기위해 설정 해주었다.
    
    # pd.concat 데이터 프레임 이어 붙히기
#     stock_df_total = pd.concat([stock_df_total,stock_df])

