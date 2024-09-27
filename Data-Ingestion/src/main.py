import subprocess
import time

def run_producer():
    print("Starting the producer...")
    subprocess.run(["python", "src/producer/open_close_producer.py"])

def run_consumer():
    print("Starting the consumer...")
    subprocess.run(["python", "src/consumer/open_close_consumer.py"])

def main():
    run_producer()
    time.sleep(1)  
    run_consumer()

if __name__ == "__main__":
    main()