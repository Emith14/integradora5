import requests
from sensorManejo import SensorDataHandler
from conexionMongo import MongoDBHandler
from conexionArduino import ArduinoConnection

class Sensores:
    def __init__(self, nombre=None, unidades=None, valor=None, port=None):
        self.nombre = nombre
        self.unidades = unidades
        self.valor = valor
        self.data_handler = SensorDataHandler(self)
        self.arduino_connection = ArduinoConnection(port) if port else None

    def __str__(self):
        return f"Nombre: {self.nombre}, Unidades: {self.unidades}, Valor: {self.valor}"

    def save_to_json(self):
        self.data_handler.save_to_json()

    def send_to_mongodb(self, uri, db_name, collection_name):
        mongo_handler = MongoDBHandler(uri, db_name, collection_name)
        mongo_handler.send_to_mongodb(self)

    def check_connection_and_send(self, uri, db_name, collection_name):
        try:
            requests.get('http://google.com', timeout=3)
            self.send_to_mongodb(uri, db_name, collection_name)
        except (requests.ConnectionError, requests.Timeout):
            self.save_to_json()

    def read_from_arduino(self):
        if self.arduino_connection:
            self.valor = self.arduino_connection.read_from_arduino()