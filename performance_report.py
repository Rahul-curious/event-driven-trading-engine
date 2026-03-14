import numpy as np
import pandas as pd

"""
Performance Report Generator
Rahul Prakash — Quant Finance Module
Calculates key trading metrics:
Sharpe Ratio, Max Drawdown, Win Rate
"""

def sharpe_ratio(returns, risk_free=0.02):
    """
    Sharpe Ratio = (Return - RiskFree) / Std
    Higher = Better risk-adjusted return
    """
    excess = returns - risk_free / 252
    return np.sqrt(252) * (
        excess.mean() / excess.std()
    )

def max_drawdown(cumulative_returns):
    """
    Max Drawdown = Biggest peak to trough loss
    Lower = Better (less risk)
    """
    rolling_max = cumulative_returns.cummax()
    drawdown = (
        cumulative_returns - rolling_max
    ) / rolling_max
    return drawdown.min()

def win_rate(returns):
    """
    Win Rate = % of profitable trades
    Higher = Better
    """
    wins = (returns > 0).sum()
    total = (returns != 0).sum()
    return wins / total if total > 0 else 0

def generate_report(strategy_returns, 
                    market_returns, symbol):
    """
    Full performance report for a strategy
    """
    print("=" * 45)
    print(f"PERFORMANCE REPORT — {symbol}")
    print("=" * 45)

    # Sharpe Ratio
    sr = sharpe_ratio(strategy_returns)
    print(f"Sharpe Ratio      : {round(sr, 4)}")

    # Max Drawdown
    cum_returns = (
        strategy_returns.cumsum().apply(np.exp)
    )
    md = max_drawdown(cum_returns)
    print(f"Max Drawdown      : {round(md*100, 2)}%")

    # Win Rate
    wr = win_rate(strategy_returns)
    print(f"Win Rate          : {round(wr*100, 2)}%")

    # Total Return
    total = cum_returns.iloc[-1]
    print(f"Total Return      : {round(total, 4)}x")

    # Market Return
    mkt = (
        market_returns.cumsum().apply(np.exp).iloc[-1]
    )
    print(f"Market Return     : {round(mkt, 4)}x")

    # Alpha
    alpha = total - mkt
    print(f"Alpha             : {round(alpha, 4)}")
    print("=" * 45)

    return {
        "sharpe_ratio": round(sr, 4),
        "max_drawdown": round(md * 100, 2),
        "win_rate": round(wr * 100, 2),
        "total_return": round(total, 4),
        "alpha": round(alpha, 4)
    }


if __name__ == "__main__":
    print("Performance Report Module Ready")
    print("Metrics: Sharpe, Drawdown, WinRate, Alpha")