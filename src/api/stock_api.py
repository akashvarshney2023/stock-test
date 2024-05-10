# src/api/stock_api.py
import requests

def get_latest_stock_price(api_key, symbol):
    """
    Fetches the latest stock price for the given stock symbol using the Alpha Vantage API.

    Args:
        api_key (str): Your Alpha Vantage API key.
        symbol (str): Stock symbol, e.g., 'NSE:INFY' for Infosys.

    Returns:
        float: Latest stock price, or None if an error occurs.
    """
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'

    try:
        response = requests.get(url)
        data = response.json()

        # Check if the response contains the desired data
        if 'Global Quote' in data:
            latest_price = float(data['Global Quote']['05. price'])
            return latest_price
        else:
            print("Error: Unable to retrieve data from Alpha Vantage.")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None
