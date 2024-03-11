import json
import os

class SensorDataHandler:
    def __init__(self, sensor):
        self.sensor = sensor

    def to_dict(self):
        return {"nombre": self.sensor.nombre, "unidades": self.sensor.unidades, "valor": self.sensor.valor}

    def save_to_json(self):
        data = self.to_dict()
        if os.path.exists('data.json'):
            with open('data.json', 'r+') as file:
                file_data = json.load(file)
                file_data.append(data)
                file.seek(0)
                json.dump(file_data, file)
        else:
            with open('data.json', 'w') as file:
                json.dump([data], file)