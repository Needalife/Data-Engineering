import requests
from confluent_kafka import Producer
from config.kafka_config import read_config

POLYGON_API_KEY = 'Hzp2QBWvkQ3lhgMA06uuQHXiBHuLLMBb' 
POLYGON_URL = 'https://api.polygon.io/v1/open-close/{ticker}/{date}'

def produce(topic, config):
    producer = Producer(config)

    # Example ticker and date
    ticker = "AAPL"
    date = "2024-09-24"
    
    response = requests.get(POLYGON_URL.format(ticker=ticker, date=date), params={'adjusted': 'true', 'apiKey': POLYGON_API_KEY})
    
    if response.status_code == 200:
        stock_data = response.json()
        key = ticker  # Using ticker as key for simplicity
        value = str(stock_data)  # Convert stock data to string
        
        producer.produce(topic, key=key, value=value)
        print(f"Produced message to topic {topic}: key = {key:12} value = {value:12}")
        
        producer.flush()
    else:
        print(f"Error fetching data for {ticker} on {date}: {response.status_code}")

def main():
    config = read_config()
    topic = "open_close_data"
    
    produce(topic, config)

if __name__ == "__main__":
    main()