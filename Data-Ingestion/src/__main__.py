import subprocess
import time
import sys

def runProducer():
    print("Starting the producer...")
    # Start producer without blocking
    producer_process = subprocess.Popen(
        [sys.executable, "-m", "producer.open_close_producer"],
        cwd="src"
    )
    return producer_process

def runConsumer():
    print("Starting the consumer...")
    # Start consumer without blocking
    consumer_process = subprocess.Popen(
        [sys.executable, "-m", "consumer.open_close_consumer"],
        cwd="src"
    )
    return consumer_process

def main():
    consumer_process = runConsumer()
    
    time.sleep(2) 
    
    producer_process = runProducer()

    try:
        producer_process.wait()  # Keeps the producer running continuously
        consumer_process.wait()  # Keeps the consumer running continuously
    except KeyboardInterrupt:
        print("Terminating processes...")
        producer_process.terminate()
        consumer_process.terminate()
        print("Processes terminated.")

if __name__ == "__main__":
    main()
