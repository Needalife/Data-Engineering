import requests
import time
from datetime import datetime
from confluent_kafka import Producer
from kafka_config import read_config

POLYGON_API_KEY = 'Hzp2QBWvkQ3lhgMA06uuQHXiBHuLLMBb'
POLYGON_URL = 'https://api.polygon.io/v1/open-close/{ticker}/{date}'

def fetch_stock_data(ticker, date):
    response = requests.get(POLYGON_URL.format(ticker=ticker, date=date), params={'adjusted': 'true', 'apiKey': POLYGON_API_KEY})
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data for {ticker} on {date}: {response.status_code}")
        return None

def produce_stock_data(producer, topic, ticker, date):
    stock_data = fetch_stock_data(ticker, date)
    
    if stock_data:
        key = ticker  
        value = str(stock_data) 
        
        producer.produce(topic, key=key, value=value)
        print(f"[{datetime.now().strftime('%d/%m %H:%M')}] Produced message to topic {topic}: key = {key:12} value = {value:12} at")
        
        producer.flush()  
    else:
        print(f"Skipping producing data for {ticker} on {date} due to fetch error")

def produce(topic, config):
    producer = Producer(config)

    ticker = "AAPL"  
    date = "2024-09-24"  

    while True:
        produce_stock_data(producer, topic, ticker, date)
        time.sleep(60)  

def main():
    config = read_config()
    topic = "open_close_data"
    
    produce(topic, config)

if __name__ == "__main__":
    main()
