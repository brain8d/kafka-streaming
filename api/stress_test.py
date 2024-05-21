import random
import datetime

def generate_data():
    stores = ["Brussels", "Antwerp", "Ghent"]
    products = ["Banana", "Bread", "Water"]
    start_date = datetime.date(2020, 1, 1)
    end_date = datetime.date(2022, 12, 31)

    data = {
        "id": str(random.randint(100000000, 999999999)),
        "store": random.choice(stores),
        "date": str(start_date + (end_date - start_date) * random.random()),
        "products": [
            {
                "id": str(random.randint(100000000, 999999999)),
                "name": random.choice(products),
                "price": round(random.uniform(1, 10), 2)
            } for _ in range(random.randint(1, 5))
        ]
    }

    return data
   

if __name__ == "__main__":
    from requests import Session

    with Session() as sess:
        for i in range(100):
            data = generate_data()
            sess.post("http://localhost:8000/data", json=data)
            