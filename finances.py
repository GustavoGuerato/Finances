from pandas_datareader import data, wb
import pandas as pd
import numpy as np
import datetime
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_pickle("all_banks")

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
