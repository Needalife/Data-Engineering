from confluent_kafka import Consumer, KafkaError
from config.kafka_config import read_config

def consume(topic, config):
    config["group.id"] = "python-group-1"
    config["auto.offset.reset"] = "earliest"

    consumer = Consumer(config)
    consumer.subscribe([topic])

    try:
        while True:
            msg = consumer.poll(1.0)  
            
            if msg is None:
                continue  
            
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue 
                else:
                    print(f"Consumer error: {msg.error()}")
                    break
            
            key = msg.key().decode("utf-8")
            value = msg.value().decode("utf-8")
            print(f"Consumed message from topic {topic}: key = {key:12} value = {value:12}")
    
    finally:
        consumer.close()

def main():
    config = read_config()
    topic = "open_close_data"
    
    consume(topic, config)

if __name__ == "__main__":
    main()