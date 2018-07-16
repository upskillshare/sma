#import all required modules
from datetime import date , datetime
import nsepy as nse
import nsetools as nst
import pandas as pd
import os

#set start date and end date. end date should be  today's date
today = datetime.now()
start_date = date(2000,1,1)
end_date   = date(today.year,today.month,today.day)
csv_out = 'C:\Swapnil\Git\StockAnalysis\sma\data\\raw'

stock_series  = pd.read_csv("C:\Swapnil\Git\StockAnalysis\sma\data\interim\ind_niftynext50list.csv",usecols=['Symbol'])
stock_list = stock_series['Symbol'].tolist()

def scrap_data(symbol_list,output_path=''):
    for symbol in symbol_list:
        print ("Getting Data for : {}".format(symbol))
        df = nse.get_history(symbol,start_date,end_date)
        out  = csv_out + '\\'+ symbol + '.csv'
        df.to_csv(out)
        out = ''
        df = pd.DataFrame()

scrap_data (stock_list)
