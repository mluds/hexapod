from serial import SerialTimeoutException
import logging as log
import time
from math import copysign


INTERVAL = 10
ZERO_POSITION = 1500


class Servo:
    def __init__(self, connection, id, offset=0, flip=False):
        self.connection = connection
        self.id = id
        self.position = self.bound(ZERO_POSITION + offset)
        self.flip = flip

    def convert(self, angle):
        if self.flip:
            angle *= -1
        return int(1500.0 + float(angle)*11.1111111)

    def bound(self, position):
        if position < 500:
            return 500
        elif position > 2500:
             return 2500
        return position

    def set(self, angle):
        pos = self.convert(angle)
        self.connection.set(self.id, pos)
        self.position = pos

    def move(self, angle):
        start = self.position
        finish = self.convert(angle)
        step = int(copysign(INTERVAL, finish-start))
        steps = range(start + step, finish, step)
        steps.append(finish)
        print("ID: " + str(self.id))
        print("Start: " + str(start))
        print("Finish: " + str(finish))
        print("Steps: " + str(steps))
        for i in steps:
            self.connection.set(self.id, i)
        self.position = i

    def deactivate(self):
        self.connection.deactivate(self.id)
