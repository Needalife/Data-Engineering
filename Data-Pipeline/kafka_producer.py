import requests
import time
import os

from datetime import datetime
from confluent_kafka import Producer
from google.cloud import bigquery
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from kafka_config import read_config 

def fetch_from_bigquery(table_name):
    client = bigquery.Client()
    query = f"""
    SELECT * 
    FROM `{table_name}`
    LIMIT 10
    """
    query_job = client.query(query) # request API

    results = query_job.result()
    rows = [dict(row) for row in results] 
    return rows

def produce_to_kafka(producer, topic, data):
    for record in data:
        key = str(record.get('id')) 
        value = str(record)
        
        producer.produce(topic, key=key, value=value)
        print(f"[{datetime.now().strftime('%d/%m %H:%M')}] Produced message to topic {topic}: key = {key} value = {value}\n")
    
    producer.flush() 

def store_in_mongodb(data):
    # Mongo credentials
    db_username = os.getenv("MONGO_DB_USERNAME")
    db_password = os.getenv("MONGO_DB_PASSWORD")

    uri = f"mongodb+srv://{db_username}:{db_password}@clusterkafkaconsumer.2esen.mongodb.net/?retryWrites=true&w=majority&appName=ClusterKafkaConsumer"

    client = MongoClient(uri, server_api=ServerApi('1'))

    # Ping to confirm
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        
        # Access the database and collection
        db = client['ClusterKafkaConsumer']
        collection_name = 'cuong_testing'         
        
        # Insert data into MongoDB
        if data:
            collection = db[collection_name]
            collection.insert_many(data)
            print(f"[{datetime.now().strftime('%d/%m %H:%M')}] Stored {len(data)} records in MongoDB.\n")
    
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")

def main():
    table_name = 'project-finance-400806.mental_health_finaldata_1.mental_health'
    
    # Fetch data from BigQuery
    data = fetch_from_bigquery(table_name)
    
    config = read_config()  # Load Kafka config 
    topic = "open_close_data"  # Kafka topic

    producer = Producer(config)
    produce_to_kafka(producer, topic, data)

    store_in_mongodb(data)

if __name__ == "__main__":
    main()