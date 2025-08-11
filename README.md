Absolutely! Let’s do this right.

I’ll provide you a **full README.md** with a **clear, neat ASCII folder structure** that renders perfectly on GitHub, plus all your content well formatted.

---

### Here is the full README.md — just copy-paste exactly as it is:

```markdown
# GMF Portfolio Optimization Time Series

## Project Structure

The project is organized into a modular structure to facilitate data management, model development, and analysis. Below is an overview of the key directories and their contents:

```

GMF-Portfolio\_Optimization-TimeSeries/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 01\_Data\_Preprocessing\_EDA.ipynb
│   ├── 02\_Time\_Series\_Forecasting.ipynb
│   ├── 03\_Forecast\_Analysis.ipynb
│   ├── 04\_Portfolio\_Optimization.ipynb
│   └── 05\_Backtesting.ipynb
├── src/
│   ├── data\_processing.py
│   ├── models.py
│   ├── optimization.py
│   └── backtesting.py
├── outputs/
│   ├── forecasts/
│   ├── portfolios/
│   └── visualizations/
├── config/
│   └── settings.yaml
├── README.md
├── requirements.txt
└── LICENSE

````

---

## Methodology

This project follows a structured methodology encompassing data collection, preprocessing, exploratory data analysis, time series forecasting, portfolio optimization, and strategy backtesting. Each phase builds upon the previous to create a robust, data-driven portfolio management solution.

### Data Collection & Preprocessing

Historical financial data for Tesla (TSLA), Vanguard Total Bond Market ETF (BND), and S&P 500 ETF (SPY) was collected from the Twelve Data API, covering July 1, 2015, to July 31, 2025. The `src/data_processing.py` script handles data fetching and initial cleaning.

Key preprocessing steps included:

- **Handling Missing Values:** Forward-fill and backward-fill to ensure a complete time series.  
- **Data Type Conversion:** Converting price and volume data to appropriate numeric formats.  
- **Feature Engineering:** Calculating daily returns and rolling volatility for each asset.  

### Exploratory Data Analysis (EDA)

Performed to gain insights into the financial data:

- **Visualization of Trends:** Historical closing prices plotted for each asset.  
- **Volatility Analysis:** Daily percentage changes, rolling means, and standard deviations analyzed.  
- **Stationarity Testing:** Augmented Dickey-Fuller (ADF) tests on prices and returns.  
- **Risk Metrics:** Value at Risk (VaR) and Sharpe Ratio calculated.  

### Time Series Forecasting Models

Two types of forecasting models were developed and compared:

- **Classical Statistical Model:** ARIMA/SARIMA using `statsmodels` and `pmdarima` with parameter tuning.  
- **Deep Learning Model:** LSTM neural network with tuning of architecture and hyperparameters.  

The dataset was split chronologically into training (2015-2023) and testing (2024-2025) sets. Models were evaluated with MAE, RMSE, and MAPE metrics.

### Forecast Analysis

Using the best model, Tesla’s stock prices were forecasted 6-12 months ahead with confidence intervals.

Focus areas included:

- Trend identification (upward, downward, stable).  
- Volatility and risk from confidence intervals.  
- Market opportunities and risks based on forecasts.  

### Portfolio Optimization

Using the forecast and historical data for BND and SPY, an optimized portfolio was constructed based on Modern Portfolio Theory (MPT):

- **Expected Returns:** Forecasted returns for TSLA, historical for BND and SPY.  
- **Covariance Matrix:** Calculated from historical returns.  
- **Efficient Frontier:** Generated and plotted.  
- **Key Portfolios:** Maximum Sharpe Ratio and Minimum Volatility portfolios identified.  
- **Recommendation:** Optimal portfolio weights and expected metrics provided.  

### Strategy Backtesting

Backtesting was performed from August 1, 2024, to July 31, 2025, comparing the strategy against a benchmark (60% SPY / 40% BND):

- Cumulative returns plotted.  
- Performance metrics including Sharpe Ratio and total returns calculated.  
- Assessment of strategy’s outperformance.  

---

## How to Run the Project

### Prerequisites

- Python 3.8 or higher  
- pip package manager  

### Installation

1. Clone the repository:

```bash
git clone https://github.com/Habtamu91/GMF_Portfolio_Optimization_TimeSeries.git
cd GMF_Portfolio_Optimization_TimeSeries
````

2. Install dependencies:

```bash
pip install -r requirements.txt
```

### Usage

* Run the Jupyter notebooks in the `notebooks/` directory sequentially.
* Alternatively, execute the individual scripts in `src/` for specific tasks.

---

## Technologies Used

* Python
* pandas, numpy
* yfinance
* matplotlib, seaborn
* scikit-learn
* statsmodels, pmdarima
* tensorflow / keras
* PyPortfolioOpt
* joblib
* tqdm
* pyyaml

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Author

**Habtamu Belay**
3rd-Year Data Science Student
Bahir Dar University

```

---

### Why this will work perfectly on GitHub?

- The folder structure is inside a fenced code block (triple backticks) which **preserves whitespace and line breaks exactly**.
- Uses classic ASCII folder-tree characters (`├──`, `│`, `└──`) which render well on GitHub.
- No comments inside the folder tree to mess formatting.
- Indentation is consistent with spaces.
- All sections are markdown formatted cleanly with proper headings, lists, and code blocks.

---


```
