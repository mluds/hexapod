from .connection import Connection
from .servo import Servo
from .leg import Leg
import logging as log
from threading import Thread
import time


class Hexapod:
    def __init__(self):
        conn = Connection()

        self.LF = Leg(conn, 7, 6, 5, -50, -50, -50, True)
        self.LM = Leg(conn, 11, 10, 9, 50, 0, 15, True)
        self.LB = Leg(conn, 15, 14, 13, -50, 0, -10, True)
        self.RF = Leg(conn, 24, 25, 26, -50, -25, 50)
        self.RM = Leg(conn, 20, 21, 22, -50, -50, 60)
        self.RB = Leg(conn, 16, 17, 18, -50, 100, -20)
        self.neck = Servo(conn, 31)

        self.legs = [
            self.LF, self.LM, self.LB,
            self.RF, self.RM, self.RB
        ]

        self.tripod1 = [
            self.LM, self.RF, self.RB
        ]

        self.tripod2 = [
            self.RM, self.LF, self.LB
        ]

        self.tripods = [
            self.tripod1,
            self.tripod2
        ]

    def deactivate(self):
        for leg in self.legs:
            leg.deactivate()

    def zero(self):
        for leg in self.legs:
            leg.zero()

    def stand(self):
        for leg in self.legs:
            leg.stand()

    def lift(self, legs, n):
        for leg in legs:
            leg.knee.set(n)
            leg.ankle.set(n - 90)

    def shift(self, legs, n):
        for leg in legs:
            leg.shift(n)

    def walk(self):
        sl = 0.5
        angle = 25
        upangle = -10
        downangle = -45

        self.stand()
        time.sleep(3)

        self.lift(self.tripod1, upangle)
        time.sleep(sl)
        self.shift(self.tripod2, -angle)
        time.sleep(sl)

        for i in range(4):
            for i in [0, 1]:
                self.lift(self.tripods[i], downangle)
                time.sleep(sl)
                self.lift(self.tripods[1 - i], upangle)
                time.sleep(sl)

                self.shift(self.tripods[1 - i], angle)
                time.sleep(sl)
                self.shift(self.tripods[i], -angle)
                time.sleep(sl)

            # self.lift(self.tripod2, downangle)
            # time.sleep(sl)
            # self.lift(self.tripod1, upangle)
            # time.sleep(sl)

            # self.shift(self.tripod1, angle)
            # time.sleep(sl)
            # self.shift(self.tripod2, -angle)
            # time.sleep(sl)
