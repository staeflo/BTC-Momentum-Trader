# Crypto Momentum Trading Bot

## Project Overview

This project is a Python-based automated trading bot that trades Bitcoin (BTC) using a simple momentum strategy. The bot leverages the Alpaca API to execute trades on the market based on historical price data. The strategy involves generating buy or sell signals depending on the crossover of two moving averages: a 40-minute moving average and a 100-minute moving average.

## Project Structure

The project consists of the following components:

- **Main Script:** Contains the trading logic, which includes fetching data, calculating trade signals, and executing trades.
- **Data Fetcher:** A module to download historical BTC price data for the last 1000 minutes.
- **Momentum Strategy:** A module that generates trading signals based on the crossover of the 40-minute and 100-minute moving averages.
- **Configuration:** A configuration file (`config.py`) that stores the Alpaca API credentials and other constants used in the project.

## Dependencies

- `alpaca-trade-api`: This package is used to interact with the Alpaca API for fetching account information, retrieving current positions, and executing trades.

## Installation

To get started with this project, you'll need to install the necessary Python packages. You can do this by running:

```bash```
pip install alpaca-trade-api

## How It Works

- **Fetch Data:** The bot uses the `fetch_data` function to download the last 1000 minutes of BTC price data.

- **Calculate Momentum:** The bot calculates the 40-minute and 100-minute moving averages. If the 40-minute moving average crosses above the 100-minute moving average, the bot generates a buy signal. If it crosses below, a sell signal is generated.

- **Trade Execution:** The bot checks the current BTC position in the account. If a buy signal is generated, it buys BTC. If a sell signal is generated, it sells BTC (if there’s enough BTC in the account).

- **Continuous Trading:** The bot runs indefinitely, executing trades every 60 seconds based on the latest data and momentum calculations.

## Outlook and Future Improvements

This project provides a basic framework for automated trading using a simple momentum strategy. However, there are several areas where you could expand and improve the bot:

- **Backtesting:** Implement a backtesting framework to evaluate the performance of the momentum strategy on historical data before deploying it in live trading.

- **Risk Management:** Introduce risk management techniques such as stop-loss and take-profit levels to minimize potential losses.

- **Enhanced Strategies:** Explore more sophisticated trading strategies, such as incorporating additional indicators (e.g., RSI, MACD) or machine learning models to generate signals.

- **Logging and Monitoring:** Add logging and alerting mechanisms to monitor the bot’s performance and ensure it is functioning correctly.

- **Portfolio Diversification:** Extend the bot to trade multiple cryptocurrencies or other assets to diversify the trading portfolio.

- **Parameter Optimization:** Implement a method for optimizing the parameters (e.g., moving average lengths) to improve the strategy's effectiveness.

