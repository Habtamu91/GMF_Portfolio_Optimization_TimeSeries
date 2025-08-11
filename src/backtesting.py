# src/backtesting.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import Union, Dict, Optional, Tuple

def backtest_strategy(
    returns: pd.DataFrame,
    weights: Union[Dict[str, float], pd.DataFrame],
    rebalance_freq: str = 'QE',
    initial_capital: float = 10000,
    risk_free_rate: float = 0.02
) -> Dict[str, Union[Dict[str, float], pd.DataFrame]]:
    """
    Robust portfolio backtesting implementation
    
    Args:
        returns: Daily returns of assets (columns: asset names)
        weights: Either dict of {asset: weight} or DataFrame of dynamic weights
        rebalance_freq: Pandas frequency string ('D', 'W', 'ME', 'QE', 'YE')
        initial_capital: Starting portfolio value
        risk_free_rate: Risk-free rate for Sharpe ratio
    
    Returns:
        Dictionary containing:
        - metrics: Performance metrics
        - performance: DataFrame with daily values
    """
    # Validate inputs
    if not isinstance(returns, pd.DataFrame):
        raise TypeError("returns must be a pandas DataFrame")
    
    # Convert weights to DataFrame if dictionary provided
    if isinstance(weights, dict):
        if not all(asset in returns.columns for asset in weights.keys()):
            raise ValueError("Weight keys must match returns columns")
        weights_df = pd.DataFrame(
            [weights[col] for col in returns.columns],
            index=returns.index,
            columns=returns.columns
        )
    else:
        weights_df = weights.reindex(returns.index, method='ffill')
    
    # Calculate daily portfolio returns
    daily_returns = (weights_df.shift(1) * returns).sum(axis=1)
    
    # Calculate portfolio value
    portfolio_value = initial_capital * (1 + daily_returns).cumprod()
    daily_returns = portfolio_value.pct_change().fillna(0)
    
    # Calculate metrics
    total_days = len(portfolio_value)
    metrics = {
        'CAGR': (portfolio_value.iloc[-1]/initial_capital)**(252/total_days) - 1,
        'Volatility': daily_returns.std() * np.sqrt(252),
        'Sharpe Ratio': (daily_returns.mean() - risk_free_rate/252) / daily_returns.std() * np.sqrt(252),
        'Max Drawdown': (portfolio_value/portfolio_value.cummax() - 1).min(),
        'Sortino Ratio': None,
        'Rebalance Dates': weights_df.resample(rebalance_freq).first().dropna().index
    }
    
    # Calculate Sortino ratio
    downside_returns = daily_returns[daily_returns < 0]
    if len(downside_returns) > 0:
        downside_dev = downside_returns.std() * np.sqrt(252)
        metrics['Sortino Ratio'] = (metrics['CAGR'] - risk_free_rate) / downside_dev
    
    return {
        'metrics': metrics,
        'performance': pd.DataFrame({
            'Portfolio Value': portfolio_value,
            'Daily Return': daily_returns,
            'Drawdown': portfolio_value/portfolio_value.cummax() - 1
        })
    }

def plot_backtest_results(
    results: Dict[str, Union[Dict[str, float], pd.DataFrame]],
    benchmark: Optional[Dict[str, Union[Dict[str, float], pd.DataFrame]]] = None,
    save_path: Optional[str] = None,
    figsize: Tuple[int, int] = (12, 8)
) -> plt.Figure:
    """
    Visualize backtest results
    
    Args:
        results: Output from backtest_strategy()
        benchmark: Optional benchmark results
        save_path: Path to save the figure
        figsize: Figure dimensions
    
    Returns:
        matplotlib Figure object
    """
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=figsize, gridspec_kw={'height_ratios': [2, 1]})
    
    # Portfolio growth
    ax1.plot(results['performance']['Portfolio Value'], label='Strategy')
    if benchmark:
        ax1.plot(benchmark['performance']['Portfolio Value'], label='Benchmark')
    ax1.set_title('Portfolio Growth', pad=20)
    ax1.set_ylabel('Value ($)')
    ax1.legend()
    ax1.grid(True)
    
    # Drawdown
    ax2.fill_between(
        results['performance'].index,
        results['performance']['Drawdown'] * 100,
        0,
        color='red',
        alpha=0.3
    )
    ax2.set_title('Drawdown', pad=20)
    ax2.set_ylabel('Drawdown (%)')
    ax2.grid(True)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig

def generate_report(
    results: Dict[str, Union[Dict[str, float], pd.DataFrame]],
    filepath: Optional[str] = None
) -> str:
    """
    Generate printable performance report
    
    Args:
        results: Backtest results dictionary
        filepath: Path to save the report
    
    Returns:
        Formatted report string
    """
    metrics = results['metrics']
    report = f"""
    PORTFOLIO PERFORMANCE REPORT
    ----------------------------
    CAGR: {metrics['CAGR']:.2%}
    Volatility: {metrics['Volatility']:.2%}
    Sharpe Ratio: {metrics['Sharpe Ratio']:.2f}
    Max Drawdown: {metrics['Max Drawdown']:.2%}
    """
    
    if metrics['Sortino Ratio'] is not None:
        report += f"Sortino Ratio: {metrics['Sortino Ratio']:.2f}\n"
    
    report += f"\nRebalancing Frequency: {len(metrics['Rebalance Dates'])} events"
    
    if filepath:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(report)
    
    return report