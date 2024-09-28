import subprocess
import time
import os, sys
# Ensure the src directory is added to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

def runProducer():
    print("Starting the producer...")
    subprocess.run(
    [sys.executable, "-m", "producer.open_close_producer"],
    cwd="src",
    )

def runConsumer():
    print("Starting the consumer...")
    subprocess.run(
    [sys.executable, "-m", "consumer.open_close_consumer"],
    cwd="src",
    )

def main():
    runProducer()
    time.sleep(5)  
    runConsumer()

if __name__ == "__main__":
    main()