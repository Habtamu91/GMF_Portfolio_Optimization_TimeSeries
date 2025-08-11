# src/optimization.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import minimize

def calculate_returns(prices):
    """Calculate daily returns from price data"""
    return prices.pct_change().dropna()

def portfolio_performance(weights, expected_returns, cov_matrix):
    """
    Calculate portfolio return and volatility
    """
    returns = np.dot(weights, expected_returns)
    volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    return returns, volatility

def minimize_volatility(expected_returns, cov_matrix, target_return=None):
    """
    Optimize portfolio for minimum volatility
    """
    num_assets = len(expected_returns)
    args = (expected_returns, cov_matrix)
    
    # Constraints
    constraints = [{'type': 'eq', 'fun': lambda x: np.sum(x) - 1}]  # weights sum to 1
    if target_return:
        constraints.append({'type': 'eq', 'fun': lambda x: portfolio_performance(x, *args)[0] - target_return})
    
    bounds = tuple((0, 1) for _ in range(num_assets))  # long-only portfolio
    
    # Optimization
    result = minimize(
        fun=lambda weights: portfolio_performance(weights, *args)[1],  # minimize volatility
        x0=np.array(num_assets * [1. / num_assets]),  # initial guess
        method='SLSQP',
        bounds=bounds,
        constraints=constraints
    )
    return result.x

def maximize_sharpe(expected_returns, cov_matrix, risk_free_rate=0.0):
    """
    Optimize portfolio for maximum Sharpe ratio
    """
    num_assets = len(expected_returns)
    args = (expected_returns, cov_matrix)
    
    def negative_sharpe(weights):
        ret, vol = portfolio_performance(weights, *args)
        return -(ret - risk_free_rate) / vol
    
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    bounds = tuple((0, 1) for _ in range(num_assets))
    
    result = minimize(
        fun=negative_sharpe,
        x0=np.array(num_assets * [1. / num_assets]),
        method='SLSQP',
        bounds=bounds,
        constraints=constraints
    )
    return result.x

def calculate_efficient_frontier(expected_returns, cov_matrix, points=50):
    """
    Calculate the efficient frontier
    """
    target_returns = np.linspace(expected_returns.min(), expected_returns.max(), points)
    portfolios = []
    
    for target in target_returns:
        weights = minimize_volatility(expected_returns, cov_matrix, target_return=target)
        ret, vol = portfolio_performance(weights, expected_returns, cov_matrix)
        portfolios.append({
            'Weights': weights,
            'Return': ret,
            'Volatility': vol,
            'Sharpe': (ret - 0.02) / vol  # Assuming 2% risk-free rate
        })
    
    return pd.DataFrame(portfolios)

def plot_efficient_frontier(frontier_df, show_max_sharpe=True):
    """
    Plot the efficient frontier with optional max Sharpe ratio portfolio
    """
    plt.figure(figsize=(10, 6))
    plt.plot(frontier_df['Volatility'], frontier_df['Return'], 'b-')
    
    if show_max_sharpe:
        max_sharpe = frontier_df.loc[frontier_df['Sharpe'].idxmax()]
        plt.scatter(max_sharpe['Volatility'], max_sharpe['Return'], color='r', s=100)
        plt.annotate(
            'Max Sharpe',
            (max_sharpe['Volatility'], max_sharpe['Return']),
            xytext=(10, 10),
            textcoords='offset points'
        )
    
    plt.title('Efficient Frontier')
    plt.xlabel('Volatility (Std. Deviation)')
    plt.ylabel('Expected Return')
    plt.grid(True)
    return plt