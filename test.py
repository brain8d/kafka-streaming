# Tests for application
from requests import Session

with Session as sess:
    for i in range(1000):
        data = {
            # TODO: Fill with test data
        }
        sess.post("http://localhost:8000/data", json=data)


# Testing methods?
from CloudManager import CloudManager  # your own module

cloud_manager = CloudManager()  # connects to database internally

data = cloud_manager.retrieve_data()

print(f"Items in the cloud database: {len(data)}")  # 1000?