from serial import SerialTimeoutException
import logging as log
import time
from math import copysign


INTERVAL = 100


class Servo:
    def __init__(self, conn, id, offset=0, flip=False):
        self.conn = conn
        self.id = id
        self.offset = offset
        self.pos = 1500
        self.flip = flip

    def round(self, x, base=5):
        return int(base * round(float(x)/base))

    def get_pos(self):
        return self.round(self.pos + self.offset, INTERVAL)

    def ang_to_pos(self, ang):
        pos = int(1500.0 + float(ang)*11.1111111 + self.offset)

        if pos < 500:
            pos = 500
        elif pos > 2500:
            pos = 2500

        return pos

    def set(self, angle):
        if self.flip:
            angle *= -1
        pos = self.ang_to_pos(angle)
        self.conn.send("#%dP%.4dT0\r" % (self.id, pos))
        self.pos = pos

    def move(self, angle):
        start = self.get_pos()
        if self.flip:
            angle *= -1
        finish = self.ang_to_pos(angle)
        step = int(copysign(INTERVAL, finish-start))
        steps = range(start, finish, step)
        steps.append(finish)
        self.conn.lock.acquire()
        print("ID: " + str(self.id))
        print("Start: " + str(start))
        print("Finish: " + str(finish))
        print("Steps: " + str(steps))
        self.conn.lock.release()
        for i in steps:
            self.conn.send("#%dP%.4dT0\r" % (self.id, i))
            #time.sleep(0.01)

    def deactivate(self):
        try:
            self.conn.send("#%dL\r" % self.id)
        except SerialTimeoutException:
            log.error("Servo %d: Write timeout" % self.id)
