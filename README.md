Project Structure

The project is organized into a modular structure to facilitate data management, model development, and analysis. Below is an overview of the key directories and their contents:



GMF-Portfolio_Optimization-TimeSeries/
│
├── data/
│   ├── raw/               # Raw data fetched from Twelve Data API
│   └── processed/         # Cleaned and processed datasets used for modeling
│
├── notebooks/
│   ├── 01_Data_Preprocessing_EDA.ipynb   # Data preprocessing and Exploratory Data Analysis
│   ├── 02_Time_Series_Forecasting.ipynb  # Development and evaluation of time series forecasting models
│   ├── 03_Forecast_Analysis.ipynb        # Analysis and interpretation of forecast results
│   ├── 04_Portfolio_Optimization.ipynb   # Portfolio optimization using MPT
│   └── 05_Backtesting.ipynb              # Backtesting of the optimized portfolio strategy
│
├── src/
│   ├── data_processing.py  # Scripts for data fetching, cleaning, and feature engineering
│   ├── models.py           # Implementations of forecasting models (ARIMA, LSTM)
│   ├── optimization.py     # Scripts for portfolio optimization calculations
│   └── backtesting.py      # Scripts for simulating and evaluating portfolio performance
│
├── outputs/
│   ├── forecasts/         # Saved model predictions and performance metrics
│   ├── portfolios/        # Optimal portfolio weights and related metrics
│   └── visualizations/    # Generated plots and charts from analysis
│
├── config/
│   └── settings.yaml      # Configuration settings for the project
│
├── README.md              # Project README file
├── requirements.txt       # Python dependencies
└── LICENSE                # Project license information


Methodology

This project follows a structured methodology encompassing data collection, preprocessing, exploratory data analysis, time series forecasting, portfolio optimization, and strategy backtesting. Each phase is designed to build upon the previous one, leading to a robust and data-driven portfolio management solution.

1. Data Collection & Preprocessing

Historical financial data for Tesla (TSLA), Vanguard Total Bond Market ETF (BND), and S&P 500 ETF (SPY) was collected from the Twelve Data API, covering the period from July 1, 2015, to July 31, 2025. The src/data_processing.py script handles the fetching and initial cleaning of this data. Key preprocessing steps included:

- Handling Missing Values: Forward-fill and backward-fill methods were applied to address any missing data points, ensuring a complete time series.


- Data Type Conversion: Ensuring all columns, especially price and volume data, were converted to appropriate numeric formats.

- Feature Engineering: Calculation of daily returns and rolling volatility for each asset, which are crucial for subsequent analysis and model training.

2. Exploratory Data Analysis (EDA)

EDA was performed to gain insights into the characteristics of the financial data. This involved:

- Visualization of Trends: Plotting historical closing prices to identify long-term trends and patterns for each asset.

- Volatility Analysis: Calculating and visualizing daily percentage changes, rolling means, and standard deviations to understand short-term fluctuations and overall volatility.

- Stationarity Testing: Performing statistical tests, such as the Augmented Dickey-Fuller (ADF) test, on closing prices and daily returns to assess stationarity, a prerequisite for ARIMA models. Discussions on the implications of stationarity for time series modeling were conducted.

- Risk Metrics: Calculating foundational risk metrics like Value at Risk (VaR) and the Sharpe Ratio to assess potential losses and historical risk-adjusted returns.

3. Time Series Forecasting Models

To predict Tesla's future stock prices, at least two different types of forecasting models were implemented and compared:

- Classical Statistical Model (ARIMA/SARIMA): AutoRegressive Integrated Moving Average (ARIMA) or Seasonal ARIMA (SARIMA) models were built using libraries like statsmodels and pmdarima. Techniques like grid search or auto_arima were used to optimize model parameters (p, d, q).

- Deep Learning Model (LSTM): A Long Short-Term Memory (LSTM) neural network was constructed, trained, and evaluated for time series forecasting. Experimentation with architecture (layers, neurons) and hyperparameters (epochs, batch size) was performed.

- The dataset was chronologically split into training (2015-2023) and testing (2024-2025) sets to preserve temporal order, which is crucial for time series data. Model performance was compared using metrics such as Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and Mean Absolute Percentage Error (MAPE).

4. Forecast Analysis

Using the best-performing model from Task 2, future stock prices for Tesla were forecasted for a period of 6-12 months. The forecast included confidence intervals to indicate the range within which future prices are expected to lie. Analysis focused on:

- Trend Analysis: Identifying long-term trends (upward, downward, stable) and any significant patterns or anomalies.

- Volatility and Risk: Discussing the uncertainty captured by confidence intervals and their implications for long-term forecast reliability.

- Market Opportunities and Risks: Outlining potential market opportunities (e.g., expected price increases) and risks (e.g., high volatility or expected declines) based on the forecast.

5. Portfolio Optimization

Insights from the TSLA forecast were integrated with historical data for BND and SPY to construct an optimized portfolio based on Modern Portfolio Theory (MPT). Key steps included:

- Expected Returns: Using the forecasted return for TSLA and historical average daily returns (annualized) for BND and SPY as proxies for their expected returns.

- Covariance Matrix: Computing the covariance matrix based on the historical daily returns of all three assets to understand their co-movement and calculate portfolio risk.

- Efficient Frontier: Running an optimization simulation to generate the Efficient Frontier, representing optimal portfolios that offer the highest expected return for a defined level of risk. The Efficient Frontier was plotted with portfolio volatility on the x-axis and return on the y-axis.

- Key Portfolios: Identifying and marking the Maximum Sharpe Ratio Portfolio (Tangency Portfolio) and the Minimum Volatility Portfolio on the Efficient Frontier.

- Optimal Portfolio Recommendation: Selecting and justifying an optimal portfolio based on the analysis of the Efficient Frontier, considering priorities such as maximizing risk-adjusted return or minimizing risk. The final recommendation included optimal weights for TSLA, BND, and SPY, along with the portfolio's expected annual return, volatility, and Sharpe Ratio.

6. Strategy Backtesting

To validate the proposed strategy, a backtesting period was defined (e.g., August 1, 2024 - July 31, 2025). The strategy's performance was simulated and compared against a simple benchmark portfolio (e.g., a static 60% SPY / 40% BND portfolio). Performance analysis involved:

- Cumulative Returns Plot: Visualizing the cumulative returns of the strategy portfolio against the benchmark over the backtesting period.

- Performance Metrics: Calculating the final Sharpe Ratio and total return for both the strategy and the benchmark.

- Outperformance Assessment: Concluding whether the strategy outperformed the benchmark and discussing the implications of the initial backtest for the viability of the model-driven approach.

How to Run the Project

To set up and run this project locally, follow these steps:

1.Clone the repository:

2.Install dependencies:

3.Run Notebooks:

4.View Outputs:

Technologies Used

This project utilizes a range of powerful libraries and tools for data science, machine learning, and financial analysis:

- Python: The primary programming language.

- pandas: For data manipulation and analysis.

- numpy: For numerical operations.

- yfinance: For fetching historical financial data.

- matplotlib & seaborn: For data visualization.

- scikit-learn: For various machine learning utilities.

- statsmodels: For statistical modeling, including ARIMA/SARIMA.

- pmdarima: (Optional) For auto_arima functionality to automatically determine ARIMA parameters.

- tensorflow (or keras): For building and training LSTM models.

- PyPortfolioOpt: For Modern Portfolio Theory (MPT) and portfolio optimization.

- joblib: For efficient saving and loading of Python objects.

- tqdm: For displaying progress bars.

- pyyaml: For reading configuration files.

License

This project is licensed under the MIT License - see the LICENSE file for details.

Author

Habtamu Belay
3rd-Year Data Science Student, Bahir Dar University

