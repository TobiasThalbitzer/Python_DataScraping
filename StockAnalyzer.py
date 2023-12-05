import yfinance as yf
import pandas as pd
from datetime import date, timedelta


def getClosestEndDate(stock_data, end_date):
    date = pd.Timestamp(end_date)
    for i in range(len(stock_data)):
        if stock_data.iloc[i].name >= date:
            return stock_data.iloc[i].name
    print("no close dates could be found")
    return None


def compareToPeriodInPercent(stock_data, start_date, end_date):
    # Ensure the start and end dates are in the index
    start_date = stock_data.index.min() if start_date not in stock_data.index else start_date
    end_date1 = getClosestEndDate(stock_data, end_date)
    if end_date1 is not None:
        x = stock_data.loc[start_date].Close
        x1 = stock_data.loc[end_date1].Close
        one_percent = x / 100
        return print((x1 / one_percent - 100))
    print("Period is out of total period with end_date: ", end_date, "and compared with last index date: ", stock_data.index.max())


def getStockData(stockSymbol, start_date, end_date):
    # Generate a business day date range
    date_range = pd.bdate_range(start=start_date, end=end_date)
    # Download stock data for the adjusted date range
    stock_data1 = yf.download(stockSymbol, start=date_range[0], end=date_range[-1])
    return stock_data1


def getPercentageIncreaseForTimeIncrements(StockSymbol, firstDate, endDate):
    listOfTimeIncrements = [timedelta(days=10), timedelta(days=30), timedelta(days=60), timedelta(days=365)]
    firstDate = date(2012, 1, 1)
    endDate = date(2022, 1, 1)

    stock_data = getStockData(StockSymbol, firstDate, endDate)

    for timeDelta_ in listOfTimeIncrements:
        comparePeriod = firstDate + timeDelta_
        print("Comparing period with endperiod:", comparePeriod)
        compareToPeriodInPercent(stock_data, firstDate, comparePeriod)



