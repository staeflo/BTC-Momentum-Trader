import time 
from data_fetcher import fetch_data
from momentum_strategy import calculate_momentum
from config import APCA_API_KEY_ID, APCA_API_SECRET_KEY, APCA_API_BASE_URL, BTC_SYMBOL
import alpaca_trade_api as tradeapi

api = tradeapi.REST(APCA_API_KEY_ID, APCA_API_SECRET_KEY, APCA_API_BASE_URL, api_version='v2')




def get_current_btc_position():
    # Fetch account information
    account = api.get_account()
    
    # Fetch all positions
    positions = api.list_positions()
    
    # Find BTC position
    btc_position = next((p for p in positions if p.symbol == 'BTCUSD'), None)
    
    if btc_position:
        return float(btc_position.qty)
    return 0.0

def trade():
    df = fetch_data()
    signals = calculate_momentum(df)

    latest_signal = signals['positions'].iloc[-1]
    print(f"{latest_signal} is the latest signal.")

    current_btc_position = get_current_btc_position()

    if latest_signal == 1.0:
        print("Buying BTC")
        api.submit_order(
            symbol=BTC_SYMBOL,
            qty=0.01,  # Adjust quantity as needed
            side='buy',
            type='market',
            time_in_force='gtc'
        )
    elif latest_signal == -1.0:
        if current_btc_position >= 0.01:  # Check if we have enough BTC to sell
            print("Selling BTC")
            api.submit_order(
                symbol=BTC_SYMBOL,
                qty=0.01,  # Adjust quantity as needed
                side='sell',
                type='market',
                time_in_force='gtc'
            )
        else:
            print("Selling BTC")
            api.submit_order(
                symbol=BTC_SYMBOL,
                qty=current_btc_position,  # Adjust quantity as needed
                side='sell',
                type='market',
                time_in_force='gtc'
            )













if __name__ == "__main__":
    while True:
        trade()
        time.sleep(60)  # run every minute
