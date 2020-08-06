import  pandas as pd
import datetime
from time import *

df_trades = pd.read_csv("trades.csv", skip_blank_lines=True, encoding='ISO-8859-1')
df_trades = df_trades.dropna()
df_trades['dt'] = pd.to_datetime(df_trades['datetime'])

df_trade_daily = pd.read_csv("df_daily_trade.csv")

list_lost=list()
for dt, group in df_trade_daily.sort_values(by="dt").groupby("dt"):
    print(dt)
    for i, row in group.iterrows():
        kdcode = row['kdcode']
        dt = row['dt']
        stock_code = kdcode[0:6]
        datetime = dt + " 15:00:00"
        df_select_1 = df_trades[(df_trades['dt'] == datetime) & (df_trades['order_book_id'] == (stock_code + ".XSHE"))]
        if df_select_1.shape[0] == 0:
            df_select_2 = df_trades[(df_trades['dt'] == datetime) & (df_trades['order_book_id'] == (stock_code + ".XSHG"))]
            if df_select_2.shape[0] == 0:
                list_lost.append(row)

df_lost=pd.DataFrame(list_lost)
df_lost.to_csv("./list_lost.csv", mode='a',encoding='utf-8-sig')
print("end")


