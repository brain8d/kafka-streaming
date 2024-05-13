# Code for API here
from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/data")
async def data(user_data: dict):
   
    print(user_data)
    # TODO: Implement code to send data to the queue

    return {"status": "ok"}