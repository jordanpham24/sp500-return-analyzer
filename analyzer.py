import yfinance as yf
import pandas as pd
import numpy as np

TICKERS = [
    "AAPL",  # Apple         
    "MSFT",  # Microsoft      
    "JPM",   # JPMorgan   
    "GS",    # Goldman Sachs 
    "XOM",   # ExxonMobil 
    "JNJ",   # Johnson & Johnson 
    "PG",    # Procter & Gamble
    "AMZN",  # Amazon  
    "LMT",   # Lockheed Martin 
    "GLD",   # Gold ETF
]

START_DATE = "2019-01-01"
END_DATE   = "2024-01-01"

raw = yf.download(TICKERS, start=START_DATE, end=END_DATE, auto_adjust=True)

prices = raw["Close"]

print(f"Shape: {prices.shape}")
print(f"Date range: {prices.index[0].date()} to {prices.index[-1].date()}")
print(f"Missing values: {prices.isnull().sum()}")