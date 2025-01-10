from pandas_datareader import data, wb
import pandas as pd
import numpy as np
import datetime
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_pickle("all_banks.pkl")

print(df.head())
start = datetime.datetime(2006, 1, 1)
end = datetime.datetime(2016, 1, 1)

BAC = df["BAC"]
filtered_bac_data = BAC.loc[start:end]

C = df["C"].loc[start:end]
GS = df["GS"].loc[start:end]
JPM = df["JPM"].loc[start:end]
MS = df["MS"].loc[start:end]
WFC = df["WFC"].loc[start:end]

tickers = ["BAC", "C", "GS", "JPM", "MS", "WFC"]

bank_stocks = pd.concat([BAC, C, GS, JPM, MS, WFC], axis=1, keys=tickers)

bank_stocks.columns.names = ["Bank Ticker", "Stock Info"]
print(bank_stocks.head())

print(bank_stocks.xs(key="Close", axis=1, level="Stock Info").max())

returns = pd.DataFrame()

for tick in tickers:
    returns[tick + " Return"] = bank_stocks[tick]["Close"].pct_change()
print(returns.head())

sns.pairplot(returns[1:])
plt.show()

print(returns.idxmin())

print(returns.idxmax())

print(returns.std())

print(returns.head())

returns.loc["2015-01-01":"2015-12-31"].std()

sns.displot(returns.loc["2015-01-01":"2015-12-31"]["MS Return"], color="green", bins=50)
plt.show()

sns.displot(returns.loc["2008-01-01":"2008-12-31"]["C Return"], color="red", bins=50)

for tick in tickers:
    bank_stocks[tick]["Close"].plot(label=tick, figsize=(12, 4))
plt.legend()
plt.show()

bank_stocks.xs(key="Close", axis=1, level="Stock Info").plot()
plt.show()


BAC["Close"].loc["2008-01-01":"2009-01-01"].rolling(window=30).mean().plot(
    label="30 day average"
)
BAC["Close"].loc["2008-01-01":"2009-01-01"].plot(label="BAC close")
plt.legend()
plt.show()

sns.heatmap(bank_stocks.xs(key="Close", axis=1, level="Stock Info").corr(), annot=True)

sns.clustermap(
    bank_stocks.xs(key="Close", axis=1, level="Stock Info").corr(), annot=True
)

close_corr = bank_stocks.xs(key="Close", axis=1, level="Stock Info").corr()

close_corr.plot(kind="heatmap", colorscale="rdylbu")

bac15 = BAC[["Open", "High", "Low", "Close"]].loc["2015-01-01":"2016-01-01"]
bac15.plot(kind="candle")

MS["Close"].loc["2015-01-01":"2016-01-01"].ta_plot(study="sma", periods=[13, 21, 55])

BAC["Close"].loc["2015-01-01":"2016-01-01"].ta_plot(study="boll")

