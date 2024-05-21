from kafka import KafkaConsumer
import json
from CloudManager import CloudManager

# Create a Kafka consumer
consumer = KafkaConsumer('delhaize_shop',
                         bootstrap_servers='localhost:9092',
                         value_deserializer=lambda v: json.loads(v.decode('utf-8')))

from CloudManager import CloudManager

# Create an instance of CloudManager
cloud_manager = CloudManager("database-1.czkwus82o4b9.us-east-1.rds.amazonaws.com", 5432, "postgres", "Thisisnotsecure1!", "mydatabase")

# Create the connection outside the loop
connection = cloud_manager.create_connection()

for message in consumer:
    # Stop consuming when the "end" message is received
    if message.value == {"end": True}:
        break

    # Insert the message into the database
    query = """
        INSERT INTO transactions (id, store, date, products)
        VALUES (%s, %s, %s, %s)
    """
    params = (message.value['id'], message.value['store'], message.value['date'], json.dumps(message.value['products']))
    print(f"Executing query: {query}")
    print(f"With parameters: {params}")
    cloud_manager.execute_query(connection, query, params)

# Close the connection
connection.close()