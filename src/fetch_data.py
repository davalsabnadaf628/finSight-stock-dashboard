import yfinance as yf

def get_stock_data(ticker):
    data = yf.download(ticker, start="2023-01-01", end="2023-12-31")
    return data
