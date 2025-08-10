"""
src/data_processing.py
Data fetching, cleaning, feature engineering for portfolio optimization.
Source: Twelve Data API
"""

import os
from pathlib import Path
from datetime import datetime
import pandas as pd
import requests

# ====== CONFIG ======
TWELVEDATA_API_KEY = "2ae678fa30a14ce7984717f9edcb17a2"
TICKERS = ["TSLA", "BND", "SPY"]
START_DATE = "2015-07-01"
END_DATE = datetime.now().strftime("%Y-%m-%d")

# ====== PATHS ======
PROJECT_ROOT = Path(__file__).parent.parent
RAW_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
FEATURES_DIR = PROCESSED_DIR / "features"

# Create directories
RAW_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
FEATURES_DIR.mkdir(parents=True, exist_ok=True)

# -----------------------------
# Fetch from Twelve Data API
# -----------------------------
def fetch_twelvedata(ticker):
    """Fetch historical OHLCV data from Twelve Data API."""
    try:
        url = "https://api.twelvedata.com/time_series"
        params = {
            "symbol": ticker,
            "interval": "1day",
            "start_date": START_DATE,
            "end_date": END_DATE,
            "apikey": TWELVEDATA_API_KEY,
            "outputsize": "5000"
        }

        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()

        if "values" not in data:
            print(f"No data returned for {ticker}")
            return None

        df = pd.DataFrame(data["values"])
        df["datetime"] = pd.to_datetime(df["datetime"])
        df.set_index("datetime", inplace=True)

        # Convert to numeric
        numeric_cols = ["open", "high", "low", "close", "volume"]
        df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")

        # Standardize column names
        df = df.rename(columns={
            "open": "Open",
            "high": "High",
            "low": "Low",
            "close": "Close",
            "volume": "Volume"
        })

        # Ensure Adj Close column
        if "Adj Close" not in df.columns:
            df["Adj Close"] = df["Close"]

        return df

    except Exception as e:
        print(f"Error fetching {ticker}: {str(e)}")
        return None

# -----------------------------
# Data preprocessing
# -----------------------------
def preprocess_data(ticker):
    """Load raw CSV, handle missing values, save cleaned CSV."""
    try:
        df = pd.read_csv(RAW_DIR / f"{ticker}.csv", index_col="datetime", parse_dates=True)
        df = df.ffill().bfill()  # fill missing values
        df.to_csv(PROCESSED_DIR / f"{ticker}_cleaned.csv")
        return df["Adj Close"]
    except Exception as e:
        print(f"Error processing {ticker}: {str(e)}")
        return None

# -----------------------------
# Helper functions for notebooks
# -----------------------------
def calculate_daily_returns(prices_df):
    """Calculate daily percentage returns from prices."""
    return prices_df.pct_change().dropna()

def calculate_rolling_volatility(returns_df, window=21):
    """Calculate rolling annualized volatility from daily returns."""
    return returns_df.rolling(window).std() * (252 ** 0.5)

def load_merged_data():
    """Load preprocessed merged data from Task 1"""
    merged_path = PROCESSED_DIR / "merged_data.csv"
    if not merged_path.exists():
        raise FileNotFoundError(
            f"Processed data not found at {merged_path}. "
            "Please run Task 1 data processing first."
        )
    return pd.read_csv(merged_path, parse_dates=['datetime'], index_col='datetime')

def load_asset_data(ticker):
    """Load individual asset data with all features"""
    asset_path = PROCESSED_DIR / f"{ticker}_cleaned.csv"
    if not asset_path.exists():
        raise FileNotFoundError(f"Processed data for {ticker} not found at {asset_path}")
    return pd.read_csv(asset_path, parse_dates=['datetime'], index_col='datetime')

def get_feature(feature_name):
    """Load pre-calculated features like returns/volatility"""
    feature_path = FEATURES_DIR / f"{feature_name}.csv"
    if not feature_path.exists():
        available_features = [f.stem for f in FEATURES_DIR.glob("*.csv")]
        raise FileNotFoundError(
            f"Feature {feature_name} not found. Available features: {available_features}"
        )
    return pd.read_csv(feature_path, parse_dates=['datetime'], index_col='datetime')

# -----------------------------
# Main script
# -----------------------------
def main():
    print("Fetching data using Twelve Data API...")

    # Step 1: Fetch and save raw data
    for ticker in TICKERS:
        print(f"\nFetching {ticker} data...")
        df = fetch_twelvedata(ticker)
        if df is not None:
            df.to_csv(RAW_DIR / f"{ticker}.csv")
            print(f"✅ Saved {ticker} data to {RAW_DIR}")
        else:
            print(f"❌ Failed to fetch {ticker} data")

    # Step 2: Preprocess & merge prices
    merged_data = pd.DataFrame()
    for ticker in TICKERS:
        prices = preprocess_data(ticker)
        if prices is not None:
            merged_data[ticker] = prices

    if not merged_data.empty:
        merged_data.to_csv(PROCESSED_DIR / "merged_data.csv")

        # Step 3: Features
        daily_returns = calculate_daily_returns(merged_data)
        daily_returns.to_csv(FEATURES_DIR / "daily_returns.csv")

        rolling_vol = calculate_rolling_volatility(daily_returns)
        rolling_vol.to_csv(FEATURES_DIR / "rolling_volatility.csv")

        print("\n✅ Data processing complete!")
        print(f"- Merged prices: {PROCESSED_DIR / 'merged_data.csv'}")
        print(f"- Daily returns: {FEATURES_DIR / 'daily_returns.csv'}")
        print(f"- Rolling volatility: {FEATURES_DIR / 'rolling_volatility.csv'}")
    else:
        print("\n❌ No merged data available.")

if __name__ == "__main__":
    main()