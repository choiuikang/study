import pandas as pd
import time
from pykrx import stock
import plotly.express as px
import streamlit as st


st.title('주식 대시보드')

# 삼성 전자 ticker 사용해서 데이터 수집
# 날짜는 2021년 1월 1일 부터 12월 1일까지
# interval 옵션에서 1m은 분봉이나, 이는 나중에 사용할 예정


# 4개의 회사 코드 생성
stock_info= pd.DataFrame({
    'stock_name': ['삼성전자', "SK하이닉스", "LG전자","현대중공업"],
    'stock_code': ["005930", "000660", "066570","329180"]})

# 날짜 선택
start_day = "20210101"
end_day = "20211201"

# 4개의 회사 포문 이용 데이터 수집
stock_df_total = pd.DataFrame()
for i in range(len(stock_info)):
    stock_code = stock_info['stock_code'][i]
    stock_name = stock_info['stock_name'][i]
    
 #stock.get_market_ohlcv_by_date 주식데이터 시작일,종료일,티커 파라미터를 넣어주면 일자별로 정렬하여 DataFrame으로 반환한다.
    #stock_df = stock.get_market_ohlcv_by_date(fromdate=start_day, todate=end_day, ticker=stock_code) 
    stock_df = stock.get_market_ohlcv_by_date(fromdate=start_day, todate=end_day, ticker=stock_code) 

    # 위 데이터를 가져오면 날짜,시가,고가,저가,..등만 나오므로 칼럼을 추가해주도록 하자.
    stock_df["종목명"] = stock_name 
    stock_df["종목코드"] = stock_code
    
    
#     time.sleep(1) # time.sleep(1) 1초마다 데이터 실행 (데이터가 많으면 한꺼번에 처리하려해 서버 팅길수 있으므로 설정 )
    print(str(i) + " 번째 "+ stock_name) # 잘 실행되는지 확인하기위해 설정 해주었다.
    
    # pd.concat 데이터 프레임 이어 붙히기
    stock_df_total = pd.concat([stock_df_total,stock_df])
    
    
#인덱스 제거
stock_df_total = stock_df_total.reset_index()

# 시각화 1
# 4개의 회사에 대한 line chart
fig = px.line(stock_df_total, x="날짜", y="종가", color='종목명')
st.plotly_chart(fig, use_container_width=True)

# 시각화 2
total_df = stock_df_total.pivot(index='날짜', columns='종목명', values='종가')

fig2 = px.area(total_df, facet_col="종목명", facet_col_wrap=2)
st.plotly_chart(fig2, use_container_width=True)

