from kafka import KafkaConsumer
import json

# Create a Kafka consumer
consumer = KafkaConsumer('delhaize-shop',
                         bootstrap_servers='localhost:9092',
                         value_deserializer=lambda v: json.loads(v.decode('utf-8')),
                         auto_offset_reset='earliest',
                         group_id='my-group')

data = []

for message in consumer:
    # Stop consuming when the "end" message is received
    if message.value == {"end": True}:
        break
    
    print(f"Received message: {json.loads(message.value)}")
    # Append the message to the data list
    data.append(message.value)

# Write the data to a local JSON file
with open('data/output.json', 'w') as f:
    json.dump(data, f)

print("Finished writing to output.json")