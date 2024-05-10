# main.py
from src.api.stock_api import get_latest_stock_price
from src.api.historical_api import save_or_update_market_data
from src.modules.stocks import nifty_500_stocks
import os


def main():
  
    for symbol in nifty_500_stocks[:10]: # [:10] to test the script on a small sample of stocks
        
        print(f"Fetching data for {symbol}...")
        save_or_update_market_data(symbol)
      

if __name__ == "__main__":
    main()
