import pandas as pd

#==================均线策略==========================
#日线中10，20，30均线粘合。最大/最小值 <= 1.02
def ma_strategy(df,new_df):
    #获得10日均线
    ten_day_close_ma_line = new_df['close'].rolling(10).mean()
    last_ten_day_close_ma = ten_day_close_ma_line.iloc[-1]
    #获得20日均线
    twenty_day_close_ma_line = new_df['close'].rolling(20).mean()
    last_twenty_day_close_ma = twenty_day_close_ma_line.iloc[-1]
    #获得30日均线
    thirty_day_close_ma_line = new_df['close'].rolling(30).mean()
    last_thirty_day_close_ma = thirty_day_close_ma_line.iloc[-1]
    #获得均线最大值和最小值的比值
    max_ma_value = max(last_ten_day_close_ma,last_twenty_day_close_ma,last_thirty_day_close_ma)
    min_ma_value = min(last_ten_day_close_ma,last_twenty_day_close_ma,last_thirty_day_close_ma)
    # print(max_ma_value/min_ma_value)
    if max_ma_value/min_ma_value <= 1.02:
        return True
    else:
        return False
#==================均线策略 END=====================


#==================日线涨幅策略=====================
#日线的涨幅越小越小，不超过5%
def day_pecentage_strategy(df,new_df):
    change_pecentage = df['pct_chg'][0] #最近一个交易日的涨跌幅
    if change_pecentage<=0.05:
        return True
    else:
        return False
#==================日线涨幅策略 END=================


#=================日线倍量策略======================
#最近一个交易日的成交量是昨日的倍量
def day_vol_strategy(df,new_df):
    last_day_trade_vol = df['vol'][0]
    last_two_day_trade_vol = df['vol'][1]
    if last_day_trade_vol/last_two_day_trade_vol >= 2:
        return True
    else:
        return False
#=================日线倍量策略 END=================


#=================周线倍量策略=====================
#本周的成交量是上周的倍量
#=================周线倍量策略 END=================
