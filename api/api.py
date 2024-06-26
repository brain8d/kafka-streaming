from fastapi import FastAPI
from pydantic import BaseModel
from kafka import KafkaProducer
import json


# just testing something here
class Item(BaseModel):
    id: str
    store: str | None = None
    date: float
    products: dict | None = None

app = FastAPI()

# A Kafka producer is created that connects to a Kafka broker running on localhost:9092
# The value_serializer argument is set to a function that converts the message value to a JSON string and then encodes it to bytes. Kafka messages must be bytes.
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))


#In the /data endpoint, the received data is sent to the delhaize-shop Kafka topic using the producer.send() method.
@app.post("/data")
async def data(user_data: dict):
    if producer.bootstrap_connected():
        producer.send('delhaize-shop', user_data)
        return {"status": "ok"}
    else:
        print("Bootstrap not connected")


'''@app.get("/data")
def read_data():
    return {"key": "value"}'''

# then run uvicorn api.api:app --host 0.0.0.0 --port 8000
# Uvicorn is a lightning-fast ASGI (Asynchronous Server Gateway Interface) server implementation, using uvloop and httptools.
