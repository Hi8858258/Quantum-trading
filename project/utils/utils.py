import datetime


#时间转换模块

# dateTime_p = datetime.datetime.now()
# dateTime_t = dateTime_p+datetime.timedelta(days=1)
#     # print(dateTime_p)
# str_p = datetime.datetime.strftime(dateTime_p,'%Y%m%d')
# str_weekday = datetime.datetime.strftime(dateTime_t,'%w')
# print (str_weekday)

def get_trade_date(trade_longth=7):
    dateTime_p = datetime.datetime.now() #获得今天的日期
    str_p = datetime.datetime.strftime(dateTime_p,'%Y%m%d')
    return str_p

