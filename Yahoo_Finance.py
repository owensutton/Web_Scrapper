import pandas as pd
from pandas_datareader import data as pdr
from datetime import date
import yfinance as yf
yf.pdr_override()


def main():
    symbol = input("Enter Stock Symbol: ")
    get_stock_price(symbol)


def get_stock_price(stock):
    start_date = "2023-01-01"
    today = date.today()
    data = pdr.get_data_yahoo(str(stock), start=start_date, end=today)
    print(data)


main()
