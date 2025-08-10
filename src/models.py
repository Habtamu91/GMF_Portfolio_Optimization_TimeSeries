"""
src/models.py
Final corrected version with matching function names
"""

import numpy as np
import pandas as pd
from pmdarima import ARIMA
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.metrics import mean_absolute_error, mean_squared_error

def train_arima(train_series, order=(3,1,2)):
    """Train ARIMA model with proper configuration"""
    model = ARIMA(order=order)
    model.fit(train_series.values)  # Use .values to avoid date index issues
    return model

def forecast_arima(model, test_series):
    """Generate forecasts with confidence intervals"""
    forecast, conf_int = model.predict(
        n_periods=len(test_series),
        return_conf_int=True
    )
    return pd.Series(forecast, index=test_series.index), conf_int

def prepare_lstm_data(series, n_steps=60, additional_features=None):
    """Prepare time series data for LSTM"""
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(series.values.reshape(-1,1))
    
    # Prepare additional features if provided
    feature_data = []
    if additional_features:
        for feature in additional_features:
            feat_scaler = MinMaxScaler()
            scaled_feat = feat_scaler.fit_transform(feature.values.reshape(-1,1))
            feature_data.append(scaled_feat)
    
    # Create sequences
    X, y = [], []
    for i in range(n_steps, len(scaled)):
        main_window = scaled[i-n_steps:i, 0]
        if additional_features:
            feat_window = [feat[i-n_steps:i, 0] for feat in feature_data]
            full_window = np.column_stack([main_window, *feat_window])
        else:
            full_window = main_window.reshape(-1,1)
        X.append(full_window)
        y.append(scaled[i, 0])
    
    return np.array(X), np.array(y), scaler

def build_lstm_model(input_shape, lstm_units=100, dense_units=30, dropout_rate=0.2):
    """Build optimized LSTM architecture"""
    model = Sequential([
        LSTM(lstm_units, input_shape=input_shape),
        Dropout(dropout_rate),
        Dense(dense_units, activation='relu'),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')
    return model

def create_hybrid_model(arima_model, lstm_model, arima_weight=0.4):
    """Create hybrid model that combines ARIMA and LSTM predictions"""
    def hybrid_predict(X):
        # Get time steps from input shape
        time_steps = X.shape[1]
        
        # Get ARIMA forecast
        arima_pred, _ = forecast_arima(
            arima_model, 
            pd.Series(np.zeros(time_steps))
        )
        
        # Get LSTM forecast
        lstm_pred = lstm_model.predict(X).flatten()
        
        # Combine predictions
        return (arima_weight * arima_pred.values + 
                (1-arima_weight) * lstm_pred)
    
    return hybrid_predict

def evaluate_forecasts(actual, forecasts):
    """Evaluate multiple forecasting methods"""
    results = {}
    for name, pred in forecasts.items():
        aligned = actual[pred.index]
        results[name] = {
            'MAE': mean_absolute_error(aligned, pred),
            'RMSE': np.sqrt(mean_squared_error(aligned, pred)),
            'MAPE': np.mean(np.abs((aligned - pred)/aligned))*100
        }
    return pd.DataFrame(results)