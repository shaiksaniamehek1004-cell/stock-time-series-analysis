# Stock Time Series Analysis

This project downloads historical stock price data for Apple (AAPL) and Google (GOOG) using the `yfinance` library and performs time series analysis using Pandas and Matplotlib.

## Features

* Download historical stock data using `yfinance`
* Analyze stock closing prices
* Visualize trading volumes
* Calculate rolling averages
* Perform weekly resampling of stock data
* Compare Apple and Google stock trends

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* yfinance

## Project Structure

```text
stock-time-series-analysis/
│
├── analysis.py
├── README.md
└── stocks_analysis.png
```

## Installation

Install the required libraries:

```bash
pip install numpy pandas matplotlib yfinance
```

## How to Run

1. Open PowerShell or Command Prompt.
2. Navigate to the project folder:

```bash
cd "C:\Users\princ\OneDrive\Desktop\PROJECTS\TIME SERIES ANALYSIS WITH PYTHON"
```

3. Run the Python script:

```bash
python analysis.py
```

## Analysis Performed

### Closing Price Analysis

* Apple (AAPL) closing prices
* Google (GOOG) closing prices

### Volume Analysis

* Daily trading volume
* 7-day average volume using resampling
* 7-day rolling average volume

### Visualizations

The script generates charts for:

* Stock closing prices
* Trading volumes
* Weekly average volumes
* Rolling average volumes

## Sample Output

The script saves generated charts as:

```text
stocks_analysis.png
```

## Repository URL

Repository URL: https://github.com/shaiksaniamehek1004-cell/stock-time-series-analysis

## Project URL

Project URL: https://github.com/shaiksaniamehek1004-cell/stock-time-series-analysis

## Author

Sania Mehek

---

This project demonstrates practical time series analysis techniques using real-world stock market data and Python data analysis libraries.
