import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import urllib
import datetime as dt
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web
import datetime as dt
import csv


plt.style.use('ggplot')

def get_stock(stocks, start, end):
    for item in stocks:
        df = web.DataReader(item, "google", start, end)
        df.to_csv('stock_/{}.csv'.format(item))

    Dates =[]
    Closes=[]
    for item in stocks:
        dataFrames= pd.read_csv('stock_/{}.csv'.format(item))
        Dates.append(dataFrames['Date'].tolist())
        Closes.append(dataFrames['Close'].tolist())
    dates =[]
    all_dates=[]
    for Date in Dates:
        Date = (dt.datetime.strptime(i, "%Y-%m-%d") for i in Date)  # strptime 用来把string转化成dateTime object
        Date = [dt.datetime.strftime(i, "%Y,%m,%d") for i in Date]  # 把strftime变成string
        for d in Date:
            dates.append(dt.datetime.strptime(d, "%Y,%m,%d")) 
        dates = matplotlib.dates.date2num(dates)  # date2num必须要用datetime object
        all_dates.append(dates)
        dates=[]

    count=0
    title=''
    for stock in stocks:
        plt.plot_date(all_dates[count], Closes[count], '-', label='{}_Price'.format(stock))
        plt.xlabel('Date')
        plt.ylabel('Price')
        title+=stock+' '
        plt.legend()
        count=count+1
    plt.title('{} Stock Graph'.format(title))
    plt.show()



American_company=["AAPL", "MSFT", "GOOGL", "FB", "AMZN", "BABA"]
start = dt.datetime(2016,5,1)
end = dt.datetime(2017, 6, 16)
get_stock(American_company, start, end)