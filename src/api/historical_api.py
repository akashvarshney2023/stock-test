import os
import requests
import json
from time import sleep

# Alpha Vantage API endpoint

def fetch_stock_data(symbol):
    API_ENDPOINT = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}.BSE&outputsize=full&apikey=LDWRX708P68IS36Y'
    response = requests.get(API_ENDPOINT)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for {symbol}. Status code: {response.status_code}")
        return None


def save_to_json(data, symbol):
    file_path = os.path.join(os.getcwd(),'src/data/history_data',f"{symbol}.json")   
    with open(file_path, 'w') as f:
        json.dump(data, f)
    print(f"Data saved to {file_path}")

def save_or_update_market_data(symbol):
    data = fetch_stock_data(symbol)
    if data:
        save_to_json(data, symbol)
        # Sleep for a while to avoid hitting API rate limits
        sleep(15)   

