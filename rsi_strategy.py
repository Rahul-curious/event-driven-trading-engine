import pandas as pd
import numpy as np

class RSIStrategy():
    """
    RSI (Relative Strength Index) Strategy
    Added by Rahul Prakash
    
    Buy when RSI < 30 (oversold)
    Sell when RSI > 70 (overbought)
    """

    def __init__(self, symbol, period=14, 
                 start="2020-01-01", end="2023-01-01"):
        self.symbol = symbol
        self.period = period  # RSI lookback period
        self.start = start
        self.end = end
        self.data = None
        self.results = None

    def get_data(self, filepath="data/stock.csv"):
        """Load stock data from CSV"""
        df = pd.read_csv(filepath, 
                         index_col="Date", 
                         parse_dates=True)
        df = df.loc[self.start:self.end]
        df["returns"] = np.log(df["Close"] / 
                               df["Close"].shift(1))
        self.data = df
        return self

    def calculate_rsi(self):
        """
        Calculate RSI indicator
        RSI = 100 - (100 / (1 + RS))
        RS = Average Gain / Average Loss
        """
        delta = self.data["Close"].diff()

        # Separate gains and losses
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)

        # Calculate average gain/loss
        avg_gain = gain.rolling(
            window=self.period).mean()
        avg_loss = loss.rolling(
            window=self.period).mean()

        # Calculate RS and RSI
        rs = avg_gain / avg_loss
        self.data["RSI"] = 100 - (100 / (1 + rs))
        return self

    def generate_signals(self):
        """
        Generate buy/sell signals
        Buy  = RSI < 30 (oversold)
        Sell = RSI > 70 (overbought)
        """
        self.data["signal"] = 0
        self.data.loc[
            self.data["RSI"] < 30, "signal"] = 1   # BUY
        self.data.loc[
            self.data["RSI"] > 70, "signal"] = -1  # SELL
        return self

    def test_strategy(self):
        """Backtest RSI strategy and calculate P&L"""
        self.calculate_rsi()
        self.generate_signals()

        # Calculate strategy returns
        self.data["strategy"] = (
            self.data["signal"].shift(1) * 
            self.data["returns"]
        )

        # Cumulative performance
        self.data["creturns"] = (
            self.data["returns"].cumsum().apply(np.exp))
        self.data["cstrategy"] = (
            self.data["strategy"].cumsum().apply(np.exp))

        self.results = self.data

        # Performance metrics
        perf = self.data["cstrategy"].iloc[-1]
        outperf = perf - self.data["creturns"].iloc[-1]

        print(f"RSI Strategy | {self.symbol}")
        print(f"Period: {self.period} days")
        print(f"Return: {round(perf, 4)}")
        print(f"vs Buy&Hold: {round(outperf, 4)}")
        return round(perf, 4), round(outperf, 4)


if __name__ == "__main__":
    rsi = RSIStrategy("AAPL", period=14,
                      start="2020-01-01",
                      end="2023-01-01")
    rsi.get_data()
    rsi.test_strategy()