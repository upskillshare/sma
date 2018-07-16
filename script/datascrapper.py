#import all required modules
from datetime import date , datetime
import nsepy as nse
import nsetools as nst
import pandas as pd
import os

from nsepy.history import get_price_list
prices = get_price_list(dt=date(2015,1,1))

#set start date and end date. end date should be  today's date
csv_out = 'C:\Swapnil\Git\StockAnalysis\sma\data\\raw'

prices.to_csv(csv_out+'\\da.csv')
