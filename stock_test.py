import sys
import os
import pandas as pd
import datetime
from pykrx import stock

# 외부변수
stock_code = sys.argv[1]
stock_name = sys.argv[2]
market = sys.argv[3]


# 날짜선택
end_dt = datetime.datetime.now()
start_dt = end_dt - datetime.timedelta(days=1)

end_dt = str(end_dt.year) + str(end_dt.month) + str(end_dt.day)
start_dt = str(start_dt.year) + str(start_dt.month) + str(start_dt.day)

now = datetime.datetime.now()


stock_df = stock.get_market_ohlcv_by_date(fromdate=start_dt, todate=end_dt, ticker=stock_code) 
    # 위 데이터를 가져오면 날짜,시가,고가,저가,..등만 나오므로 칼럼을 추가해주도록 하자.
    
stock_df["종목명"] = stock_name 
stock_df["종목코드"] = stock_code
stock_df["시장구분"] = market
stock_df["time"] = now
        
stock_df = stock_df.reset_index()

    
if not os.path.exists('stock_df_total_test.csv'):
        stock_df.to_csv('stock_df_total_test.csv', index=False, mode='w')
else:
        stock_df.to_csv('stock_df_total_test.csv', index=False, mode='a', header=False)


