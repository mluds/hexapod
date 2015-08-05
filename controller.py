from serial_handler import SerialHandler
from servo import Servo
from time import time

class Controller:

    def __init__(self, servo_count=32):
        self.serial = SerialThread()
        self.serial.start()
        self.servos = []
        for i in range(servo_count):
            self.servos[i] = Servo(i, self.serial_handler)
            self.servos[i].kill()

    def kill_all(self):
        if self.serial.is_open:
            for servo in self.servos:
                servo.kill()