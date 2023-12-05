import yfinance as yf
import StockAnalyzer
import pandas as pd
from datetime import date, timedelta

msft = yf.Ticker("MSFT")

symbol = 'AAPL'
start_date = '2022-01-01'
end_date = '2022-12-31'

StockAnalyzer.getPercentageIncreaseForTimeIncrements('TSLA', date(2020, 1, 1), date(2021, 1, 1))