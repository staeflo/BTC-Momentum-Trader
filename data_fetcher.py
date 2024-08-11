# data_fetcher.py

import alpaca_trade_api as tradeapi
import pandas as pd
from config import APCA_API_KEY_ID, APCA_API_SECRET_KEY,BTC_SYMBOL

api = tradeapi.REST(APCA_API_KEY_ID, APCA_API_SECRET_KEY, base_url='https://paper-api.alpaca.markets', api_version='v2')

def fetch_data():
    # Fetch historical data for BTC/USD
    bars = api.get_crypto_bars(BTC_SYMBOL, timeframe='1Min').df

    # Print DataFrame columns to inspect its structure
    #print("Columns available in DataFrame:", bars.columns)
    
    
    # Select relevant columns and reset index
    df = bars[['open', 'high', 'low', 'close', 'volume']].copy()
    df.index = pd.to_datetime(df.index)
    last_row = df.iloc[-1]
    print(last_row)
    return df

