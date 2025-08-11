```markdown
# Time Series Forecasting & Portfolio Optimization

## 📌 Project Overview
This project was developed during **10 Academy – Week 11 Intensive Training** for **Guide Me in Finance (GMF) Investments**, a financial advisory firm specializing in personalized portfolio management.

The objective was to apply **time series forecasting** and **Modern Portfolio Theory (MPT)** to historical market data in order to:
- Predict **Tesla (TSLA)** stock prices.
- Combine forecasts with **Vanguard Total Bond Market ETF (BND)** and **S&P 500 ETF (SPY)** historical data.
- Construct an **optimized portfolio** balancing risk and return.
- Backtest the strategy against a benchmark.

---

## 🎯 Business Objective
The goal is to use **data-driven insights** to enhance portfolio performance, minimize risks, and capitalize on market opportunities by:
1. Forecasting future price trends for TSLA.
2. Optimizing portfolio weights using historical and forecasted returns.
3. Simulating performance through backtesting.

---

## 📂 Project Structure
```

GMF-Portfolio_Optimization-TimeSeries/
│
├── data/
│   ├── raw/               # Raw data from Twelve Data API
│   └── processed/         # Cleaned & processed datasets
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
│   ├── forecasts/         # Model predictions
│   ├── portfolios/        # Optimal weights & metrics
│   └── visualizations/    # Plots & charts
├── config/settings.yaml
├── README.md
├── requirements.txt
└── LICENSE

````

---

## 📊 Methodology

### **1. Data Collection & Preprocessing**
- Collected OHLCV data for TSLA, BND, SPY from **Twelve Data API** (2015-07-01 to 2025-07-31).
- Handled missing values, ensured time-based indexing, calculated **daily returns** and **rolling volatility**.

### **2. Exploratory Data Analysis (EDA)**
- Visualized historical trends, volatility patterns, and correlations.
- Performed stationarity tests (ADF).
- Calculated **Value at Risk (VaR)** and **Sharpe Ratio**.

### **3. Time Series Forecasting**
- Implemented:
  - **ARIMA/SARIMA** models (statistical approach).
  - **LSTM** deep learning model (sequence modeling).
- Evaluated with **MAE**, **RMSE**, and **MAPE**.

### **4. Forecast Analysis**
- Generated **6–12 month forecasts** for TSLA.
- Included confidence intervals to assess forecast uncertainty.

### **5. Portfolio Optimization**
- Combined forecasted TSLA returns with historical returns of BND and SPY.
- Computed **Efficient Frontier** using MPT.
- Identified:
  - **Maximum Sharpe Ratio Portfolio**.
  - **Minimum Volatility Portfolio**.
- Recommended optimal weights.

### **6. Backtesting**
- Simulated strategy performance for the last year (2024-08-01 to 2025-07-31).
- Compared against a **60% SPY / 40% BND benchmark**.

---

## 📈 Key Results
- **Best Model:** Selected based on lowest RMSE between ARIMA and LSTM.
- **Optimal Portfolio Weights:** Derived from Efficient Frontier analysis.
- **Backtest Performance:** Compared cumulative returns, total return, and Sharpe Ratio vs. benchmark.

---

## 🛠️ Technologies Used
- **Python** (pandas, numpy, matplotlib, seaborn)
- **pmdarima**, **statsmodels** – ARIMA/SARIMA modeling
- **TensorFlow/Keras** – LSTM modeling
- **PyPortfolioOpt** – Portfolio optimization
- **Streamlit** (optional extension for interactive dashboards)
- **Git & GitHub** – Version control

---

## 🚀 How to Run the Project
1. **Clone the repository**  
   ```bash
   git clone https://github.com/Habtamu91/GMF-Portfolio_Optimization-TimeSeries.git
   cd GMF-Portfolio_Optimization-TimeSeries
````

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```
3. **Run Notebooks** in `notebooks/` in order (1 → 5).
4. **View Outputs** in the `outputs/` folder.

---

## 📜 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Habtamu Belay**
3rd-Year Data Science Student, Bahir Dar University
 [GitHub] : (https://github.com/Habtamu91)

---

