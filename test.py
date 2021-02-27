import tushare as ts
import pandas as pd
import numpy as np
from project import strategy
from project.utils import utils
from project.strategy import week_day_vol_strategy

'''
该程序是为了实现量化交易而做的一个demo
'''

#=================接口初始化===============
#API token
ts.set_token('edcc3ab3b95655ad478dd6ccb07266848a91a34186f36321baa85a81')
#调用API
pro = ts.pro_api()
#-----------------获取所有股票的信息-----
data = pro.query('stock_basic', exchange='', list_status='L', fields='ts_code')
data.to_csv('A股所有股票代码.csv',columns = None, index = None)
#-----------------获取所有股票代码的字符串格式以供下面遍历
Stock_code_list = pd.read_csv('A股所有股票代码.csv',dtype=str).values.tolist()
#-----------------获得交易所的交易日历
#data = pro.daily(ts_code = '000100.sz',start_date='20180701', end_date='')
#-----------------获得今天之前的有效交易日期
# time = utils.get_trade_date() #获取今天日期的字符串格式
# TT = pro.query('trade_cal', start_date='20210220', end_date=time)
# print(TT)
#================接口初始化 END=============


#=================主要参数修改==============
strategy_start_date = '20210101'  #引号里使用xxxxmmdd格式来表示日期
select_stock_store = []
#=================参数设定 END==============

#=================主程序===================
if __name__ == '__main__':
    # print(Stock_code_list)
    for i in Stock_code_list:
        code_number = i[0]
        #获得主要的数据
        df = pro.query('daily',ts_code = code_number, start_date = strategy_start_date, end_data = '',head=30)
        new_df = df.set_index('trade_date')
        new_df.index = pd.DatetimeIndex(new_df.index)
        new_df.sort_index(inplace=True) #由于pandas的rolling函数窗口上面超出边界，所以需要倒序一下

        #--------------------均线策略结果----------------------------
        ma_strategy_result = week_day_vol_strategy.ma_strategy(df,new_df)

        #-------------------获得日线涨幅策略结果--------------------
        day_pecentage_strategy_result = week_day_vol_strategy.day_pecentage_strategy(df,new_df)

        #-------------------日线倍量策略结果------------------------
        day_vol_strategy_result = week_day_vol_strategy.day_vol_strategy(df,new_df)

        #------------------周线倍量策略结果-----------------------
        #======
        #空缺
        #======

        #------------------四个策略都满足，返回股票代码-----------------
        if ma_strategy_result and day_vol_strategy_result and day_pecentage_strategy_result:
            print(code_number,'满足策略,已记录到股票待选库')
            select_stock_store.append(code_number)
        else:
            print(code_number,'未满足策略')

print('今天满足策略的股票如下：',Stock_code_list)
#=================主程序 END===================
