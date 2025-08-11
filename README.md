
# GMF Portfolio Optimization Time Series

## Project Overview
Time Series Forecasting & Portfolio Optimization using ARIMA, SARIMA, and LSTM models to predict Tesla (TSLA) prices, combined with BND and SPY for constructing efficient portfolios using Modern Portfolio Theory and backtesting strategy performance.

## Project Structure
<pre>
GMF-Portfolio_Optimization-TimeSeries/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_Data_Preprocessing_EDA.ipynb
│   ├── 02_Time_Series_Forecasting.ipynb
│   ├── 03_Forecast_Analysis.ipynb
│   ├── 04_Portfolio_Optimization.ipynb
│   └── 05_Backtesting.ipynb
│
├── src/
│   ├── data_processing.py
│   ├── models.py
│   ├── optimization.py
│   └── backtesting.py
│
├── outputs/
│   ├── forecasts/
│   ├── portfolios/
│   └── visualizations/
│
├── config/
│   └── settings.yaml
│
├── README.md
├── requirements.txt
└── LICENSE
</pre>

## Methodology
[... rest of your content remains exactly the same ...]
## Methodology

### Data Collection & Preprocessing
- Collected historical data for TSLA, BND, SPY (2015-2025) from Twelve Data API
- Preprocessing steps:
  - Missing value handling (forward/backward fill)
  - Data type conversion
  - Feature engineering (daily returns, rolling volatility)

### Exploratory Data Analysis
- Visualized historical trends and volatility
- Conducted stationarity testing (ADF tests)
- Calculated risk metrics (VaR, Sharpe Ratio)

### Time Series Forecasting
- Developed and compared:
  - ARIMA/SARIMA models
  - LSTM neural networks
- Evaluation metrics: MAE, RMSE, MAPE
- Training period: 2015-2023
- Testing period: 2024-2025

### Portfolio Optimization
- Modern Portfolio Theory implementation:
  - Calculated expected returns and covariance matrix
  - Generated efficient frontier
  - Identified optimal portfolios:
    - Maximum Sharpe Ratio
    - Minimum Volatility

### Backtesting
- Test period: August 2024 - July 2025
- Compared against 60% SPY / 40% BND benchmark
- Evaluated performance metrics:
  - Cumulative returns
  - Sharpe Ratio
  - Total returns

## How to Run the Project

### Prerequisites
- Python 3.8+
- pip package manager

### Installation
```bash
git clone https://github.com/Habtamu91/GMF_Portfolio_Optimization_TimeSeries.git
cd GMF_Portfolio_Optimization_TimeSeries
pip install -r requirements.txt
```

### Usage
1. Run notebooks in sequential order:
   - `01_Data_Preprocessing_EDA.ipynb`
   - `02_Time_Series_Forecasting.ipynb`
   - `03_Forecast_Analysis.ipynb`
   - `04_Portfolio_Optimization.ipynb`
   - `05_Backtesting.ipynb`

## Technologies Used
- **Python Libraries**:
  - pandas, numpy
  - matplotlib, seaborn
  - statsmodels, pmdarima
  - tensorflow/keras
  - PyPortfolioOpt

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
Habtamu Belay  
3rd-Year Data Science Student  
Bahir Dar University
```

