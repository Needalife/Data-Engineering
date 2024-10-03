import os
import subprocess

def run_bigquery_to_data():
    print("Fetching data from BigQuery...")
    subprocess.run(["python3", "bigquery_to_data.py"])

def run_kafka_producer():
    print("Producing data to Kafka and storing in MongoDB...")
    subprocess.run(["python3", "kafka_producer.py"])

def run_kafka_consumer():
    print("Starting Kafka consumer...")
    subprocess.run(["python3", "kafka_consumer.py"])

def main():
    run_bigquery_to_data()
    run_kafka_producer()
    run_kafka_consumer()

if __name__ == "__main__":
    main()