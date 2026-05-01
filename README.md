# S&P 500 Stack Return Analyzer

An end to end stock return analysis using Python, yfinance, and pandas. Pulls 5 years of real market data and computes financial metrics.

Built as the first project of a larger finance reserach project.

## What it's doing:

- Pulls 5 years of adjusted daily closing prices from 2019 to 2024 for 10 different tickers, and computes annualized return, annualized volatility, Sharpe ratio, and max drawdown for each.
- Generates a correlation heatmap across all 10 stocks
- Summarizes computations over 5 years

## Stocks Analyzed:

AAPL | Apple

MSFT | Microsoft

JPM | JPMorgan Chase

GS | Goldman Sachs

XOM | ExxonMobil

JNJ | Johnson & Johnson

PG | Procter & Gamble

AMZN | Amazon

LMT | Lockheed Martin

GLD | Gold ETF

## Key findings:

Best risk-adjusted return: APPL > Sharpe ratio of 1.31

Worst drawdown: XOM > peak to trough decline of -60.35%

Best diversifier: GLD > lowest average correlation

## Setup

```bash
git clone https://github.com/YOUR_USERNAME/sp500-return-analyzer.git
cd sp500-return-analyzer
python -m venv venv
.venv\Scripts\activate
pip install -r requirements.txt
python analyzer.py
```

