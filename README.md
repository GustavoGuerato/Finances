Bank Stock Analysis Project

This project involves analyzing stock data for six major banks: Bank of America (BAC), Citigroup (C), Goldman Sachs (GS), JPMorgan Chase (JPM), Morgan Stanley (MS), and Wells Fargo (WFC). The analysis focuses on stock performance from 2006 to 2016, including returns, volatility, and correlations between the banks' stocks.

Files

all_banks.pkl: A pickle file containing the stock data for the banks.

Requirements

Python 3.x

pandas

numpy

datetime

seaborn

matplotlib

pandas_datareader

Installation

Ensure you have Python installed. You can install the required packages using:

pip install pandas numpy seaborn matplotlib pandas_datareader

Usage

Load the Data:
The stock data is loaded from a pickle file:

df = pd.read_pickle("all_banks.pkl")
print(df.head())

Filter Data by Date:
Data for each bank is filtered between 2006 and 2016:

start = datetime.datetime(2006, 1, 1)
end = datetime.datetime(2016, 1, 1)

BAC = df["BAC"].loc[start:end]
C = df["C"].loc[start:end]
GS = df["GS"].loc[start:end]
JPM = df["JPM"].loc[start:end]
MS = df["MS"].loc[start:end]
WFC = df["WFC"].loc[start:end]

Concatenate Bank Data:
Combine all bank data into a single DataFrame:

tickers = ["BAC", "C", "GS", "JPM", "MS", "WFC"]
bank_stocks = pd.concat([BAC, C, GS, JPM, MS, WFC], axis=1, keys=tickers)
bank_stocks.columns.names = ["Bank Ticker", "Stock Info"]
print(bank_stocks.head())

Calculate Returns:
Calculate daily returns for each bank:

returns = pd.DataFrame()
for tick in tickers:
    returns[tick + " Return"] = bank_stocks[tick]["Close"].pct_change()
print(returns.head())

Visualize Data:
Use seaborn and matplotlib for various visualizations:

Pairplot of returns:

sns.pairplot(returns[1:])
plt.show()

Distribution of returns:

sns.displot(returns.loc["2015-01-01":"2015-12-31"]["MS Return"], color="green", bins=50)
plt.show()

Plot Closing Prices:
Plot the closing prices for all banks:

for tick in tickers:
    bank_stocks[tick]["Close"].plot(label=tick, figsize=(12, 4))
plt.legend()
plt.show()

Rolling Mean and Bollinger Bands:
Calculate rolling mean and Bollinger Bands:

BAC["Close"].loc["2008-01-01":"2009-01-01"].rolling(window=30).mean().plot(label="30 day average")
BAC["Close"].loc["2008-01-01":"2009-01-01"].plot(label="BAC close")
plt.legend()
plt.show()

Correlation Heatmap and Clustermap:
Visualize the correlation between the banks:

sns.heatmap(bank_stocks.xs(key="Close", axis=1, level="Stock Info").corr(), annot=True)
sns.clustermap(bank_stocks.xs(key="Close", axis=1, level="Stock Info").corr(), annot=True)

Conclusion

This project demonstrates how to analyze and visualize stock data using Python. It covers loading data, filtering by date, calculating returns, visualizing data, and exploring correlations.

