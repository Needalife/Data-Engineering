import os
import subprocess

def run_kafka_producer():
    print("--------------------------------------------------")
    print("> Producing data to Kafka and storing in MongoDB...")
    subprocess.run(["python3", "kafka_producer.py"])

def run_kafka_consumer():
    print("--------------------------------------------------")
    print("> Starting Kafka consumer...")
    subprocess.run(["python3", "kafka_consumer.py"])

def main():
    run_kafka_producer()
    run_kafka_consumer()

if __name__ == "__main__":
    main()