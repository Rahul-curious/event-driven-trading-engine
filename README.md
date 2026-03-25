
# Event-Driven Trading Engine

A Python-based event-driven trading system for simulating strategy execution on financial time-series data.

The system is designed with a modular architecture that mirrors real-world trading pipelines, including components for data ingestion, signal generation, execution simulation, and portfolio management. It processes sequential data streams to emulate real-time system behavior and focuses on correctness, efficiency, and structured design.

---

## Features

- Event-driven processing of financial time-series data  
- Modular architecture (data, strategy, execution, portfolio, metrics)  
- Strategy implementations: SMA crossover, RSI  
- Performance evaluation:
  - Profit & Loss (PnL)
  - Returns
  - Drawdown
  - Sharpe Ratio  
- Parameter optimization for strategy tuning  
- Visualization of strategy and benchmark performance  
---

## 🧠 System Architecture

The engine follows a simplified version of real-world trading systems:
The system processes time-series data sequentially to mimic real-world trading environments where decisions are made on streaming data.

Data → Strategy → Signal → Execution → Portfolio → Metrics

### Components:

- **Data Handler**  
  Loads historical price data and processes it sequentially  

- **Strategy Module**  
  Generates trading signals (Buy/Sell) based on indicators  

- **Execution Engine**  
  Simulates order execution  

- **Portfolio Manager**  
  Tracks positions, capital, and PnL  

- **Performance Metrics**  
  Computes returns, drawdown, and Sharpe ratio  

---

## 📊 Data Requirements

CSV file (`stock.csv`) must contain:

- `timestamp` (yyyy-mm-dd)
- `close` (price)

Example:

timestamp,close  
2020-01-01,100  
2020-01-02,102  

---

## ⚙️ Installation

Clone the repository:

git clone https://github.com/Rahul-curious/event-driven-trading-engine.git  
cd event-driven-trading-engine  

---

## ▶️ Usage

```python
from SMA_Backtesting import SMABacktester

backtester = SMABacktester(
    symbol='SBI',
    SMA_S=50,
    SMA_L=200,
    start='2020-01-01',
    end='2023-01-01'
)

backtester.test_strategy()
backtester.plot_results()
