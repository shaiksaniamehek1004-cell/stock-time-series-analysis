import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Download stock data
apple = yf.download("AAPL", start="2019-01-01", end="2020-12-01")
google = yf.download("GOOG", start="2019-01-01", end="2020-12-01")

# Closing prices
fig, ax = plt.subplots(nrows=2, sharex=True, figsize=(12, 6))
apple['Close'].plot(ax=ax[0], title="Apple Stock", legend=False)
google['Close'].plot(ax=ax[1], title="Google Stock", legend=False)
fig.tight_layout()

# Volume
fig, ax = plt.subplots(nrows=2, sharex=True, figsize=(12, 6))
apple['Volume'].plot(ax=ax[0], title="Apple Stock - Volume", legend=False)
google['Volume'].plot(ax=ax[1], title="Google Stock - Volume", legend=False)
fig.tight_layout()

# 7-day resample mean
fig, ax = plt.subplots(nrows=2, sharex=True, figsize=(12, 6))
apple['Volume'].resample('7D').mean().plot(
    ax=ax[0], title="Apple Stock - Volume (7D Mean)", legend=False)
google['Volume'].resample('7D').mean().plot(
    ax=ax[1], title="Google Stock - Volume (7D Mean)", legend=False)
fig.tight_layout()

# 7-day rolling mean
fig, ax = plt.subplots(nrows=2, sharex=True, figsize=(12, 6))
apple['Volume'].rolling(7).mean().plot(
    ax=ax[0], title="Apple Stock - Volume (Rolling)", legend=False)
google['Volume'].rolling(7).mean().plot(
    ax=ax[1], title="Google Stock - Volume (Rolling)", legend=False)
fig.tight_layout()

plt.show()
