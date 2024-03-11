import serial

class ArduinoConnection:
    def __init__(self, port, baud_rate=9600):
        self.connection = serial.Serial(port, baud_rate)

    def read_from_arduino(self):
        if self.connection.in_waiting > 0:
            return self.connection.readline().decode()

    def write_to_arduino(self, message):
        self.connection.write(message.encode())