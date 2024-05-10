# main.py
from src.api.stock_api import get_latest_stock_price
def main():
    # Replace 'YOUR_ALPHA_VANTAGE_API_KEY' with your actual API key
    api_key = 'LDWRX708P68IS36Y'
    symbol = 'INFY.BSE'  # Infosys stock symbol

    # Fetch the latest stock price
    latest_price = get_latest_stock_price(api_key, symbol)

    if latest_price is not None:
        print(f"Latest price for Infosys (BSE:INFY) is {latest_price}")
    else:
        print("Failed to retrieve the latest price.")

if __name__ == "__main__":
    main()
