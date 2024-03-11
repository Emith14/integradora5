import pymongo
import requests
from sensorManejo import SensorDataHandler

class MongoDBHandler:
    def __init__(self, uri, db_name, collection_name):
        self.uri = uri
        self.db_name = db_name
        self.collection_name = collection_name

    def send_to_mongodb(self, sensor):
        client = pymongo.MongoClient(self.uri)
        db = client[self.db_name]
        collection = db[self.collection_name]
        data_handler = SensorDataHandler(sensor)
        collection.insert_one(data_handler.to_dict())

    def check_connection_and_send(self, sensor):
        try:
            requests.get('http://google.com', timeout=3)
            self.send_to_mongodb(sensor)
        except (requests.ConnectionError, requests.Timeout):
            data_handler = SensorDataHandler(sensor)
            data_handler.save_to_json()