import pandas as pd
from data_fetcher import fetch_data  # Import the fetch_data function
import numpy as np

def calculate_momentum(df, short_window = 40,long_window=100):
    signals = pd.DataFrame(index=df.index)
    signals['signal'] = 0.0

    # Create short simple moving average
    signals['short_mavg'] = df['close'].rolling(window = short_window, min_periods = 1,center = False).mean()
    # Create long simple moving average
    signals['long_mavg'] = df['close'].rolling(window = long_window, min_periods = 1,center = False).mean()
    #Generate Buy & Sell signals

    signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] > signals['long_mavg'][short_window:], 1.0, 0.0)
    signals['positions'] = signals['signal'].diff()
    return signals

