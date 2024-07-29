# Kafka Streaming project

# Overview
This project involves creating a data streaming pipeline for Delhaize, enabling real-time processing and storage of sales data. The pipeline includes an API to send data to a Kafka queue, processing the data to categorize products and calculate prices, and storing the processed data in a cloud database. The project focuses on applying DevOps best practices.

The project was hosted on Google Cloud using free trial, now stopped.

## Deliverables
- Create an API to send data to a Kafka queue (producer) &rarr; ```producer.py```.
- Develop a worker to preprocess the data (consumer) &rarr; ```consumer.py```.
- Store the preprocessed data in a cloud database &rarr; Hosten on GCP as Postgres Database.
- Apply DevOps best practices (OOP, Docker, CI/CD, clean coding, unit tests, etc.) &rarr; ```CloudManager.py```.

Work in Progress:
- CI/CD
- unit tests

### Context
Delhaize generates sales data with each customer purchase. Your manager needs analytics on this data, such as product category proportions and average prices. A proper data pipeline is required to achieve this.


### Sample Data
#### Input Data
```json
{
    "id": "123456789",
    "store": "Brussels",
    "date": "2020-01-01",
    "products": [
        {"id": "123456789", "name": "Banana", "price": 1.5},
        {"id": "123456789", "name": "Bread", "price": 1.5},
        {"id": "123456789", "name": "Water", "price": 1.5}
    ]
}
```

#### Processed Data
```json
{
    "id": "123456789",
    "store": "Brussels",
    "date": "2020-01-01",
    "total_price": 4.5,
    "products": [
        {"id": "123456789", "name": "Banana", "price": 1.5, "category": "Fruit"},
        {"id": "123456789", "name": "Bread", "price": 1.5, "category": "Bakery"},
        {"id": "123456789", "name": "Water", "price": 1.5, "category": "Drink"}
    ]
}
```


