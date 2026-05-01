import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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

#print(f"Shape: {prices.shape}")
#print(f"Date range: {prices.index[0].date()} to {prices.index[-1].date()}")
#print(f"Missing values: {prices.isnull().sum()}")

daily_returns = prices.pct_change().dropna()
annualized_returns = (1+daily_returns.mean()) ** 252 - 1
annualized_volatility = daily_returns.std() * np.sqrt(252)

RISK_FREE_RATE = 0.036

sharpe_ratio = (annualized_returns - RISK_FREE_RATE)/annualized_volatility

def max_drawdown(price_series):
    peak = price_series.cummax()
    drawdown = (price_series - peak) / peak
    return drawdown.min()

max_drawdowns = prices.apply(max_drawdown)

correlation_matrix = daily_returns.corr()

summary = pd.DataFrame({
    "Annualized Return" : annualized_returns,
    "Annualized Volatility" : annualized_volatility,
    "Sharpe Ratio" : sharpe_ratio,
    "Max Drawdown" : max_drawdowns
}).round(4)

print("\n Summary Metrics")
print(summary)
print("\nCorrelation Matrix")
print(correlation_matrix.round(3))

fig, ax = plt.subplots(figsize=(12,8))

sns.heatmap(
    correlation_matrix,
    annot = True,
    fmt = ".2f",
    cmap = "coolwarm",
    center = 0,
    vmin = -1,
    vmax = 1,
    square = True,
    linewidths = 0.5,
    ax=ax
)

ax.set_title("Stock Return Correlation Matrix (2019–2024)", 
             fontsize=16, fontweight="bold", pad=20)

plt.tight_layout()
plt.savefig("correlation_heatmap.png", dpi=150, bbox_inches="tight")
plt.show()

fig, ax = plt.subplots(figsize = (12,4))
ax.axis("off")

formatted = summary.copy()
formatted["Annualized Return"]     = summary["Annualized Return"].map("{:.2%}".format)
formatted["Annualized Volatility"] = summary["Annualized Volatility"].map("{:.2%}".format)
formatted["Sharpe Ratio"]          = summary["Sharpe Ratio"].map("{:.2f}".format)
formatted["Max Drawdown"]          = summary["Max Drawdown"].map("{:.2%}".format)

table = ax.table(
    cellText=formatted.values,
    rowLabels=formatted.index,
    colLabels=formatted.columns,
    cellLoc="center",
    loc="center"
)

table.auto_set_font_size(False)
table.set_fontsize(11)
table.scale(1.2, 1.8)

ax.set_title("Summary Metrics by Stock (2019–2024)", 
             fontsize=14, fontweight="bold", pad=20)

plt.tight_layout()
plt.savefig("summary_table.png", dpi=150, bbox_inches="tight")
plt.show()