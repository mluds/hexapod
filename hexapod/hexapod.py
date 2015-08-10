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

    def lay(self):
        threads = []
        for leg in self.legs:
            threads.append(Thread(leg.lay()))
        for t in threads:
            t.start()
        for t in threads:
            t.join()

    def stand(self, legs):
        threads = []
        for leg in legs:
            threads.append(Thread(leg.stand()))
        for t in threads:
            t.start()
        for t in threads:
            t.join()

    def lift(self, legs, n):
        for leg in legs:
            leg.knee.set(n)
            leg.ankle.set(n - 90)

    def shift(self, legs, n):
        for leg in legs:
            leg.shift(n)

    def walk(self):
        sl = 0.2
        angle = 20
        upangle = 20
        downangle = 45
        self.stand(self.legs)
        time.sleep(3)

        self.lift(self.tripod1, upangle)
        time.sleep(sl)
        self.shift(self.tripod2, -angle)
        time.sleep(sl)

        for i in range(0, 100):
            self.lift(self.tripod1, downangle)
            time.sleep(sl)
            self.lift(self.tripod2, upangle)
            time.sleep(sl)

            self.shift(self.tripod2, angle)
            time.sleep(sl)
            self.shift(self.tripod1, -angle)
            time.sleep(sl)

            self.lift(self.tripod2, downangle)
            time.sleep(sl)
            self.lift(self.tripod1, upangle)
            time.sleep(sl)

            self.shift(self.tripod1, angle)
            time.sleep(sl)
            self.shift(self.tripod2, -angle)
            time.sleep(sl)
