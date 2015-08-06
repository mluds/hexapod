from .connection import Connection
from .leg import Leg
import logging as log


class Hexapod:
    def __init__(self):
        conn = Connection()

        self.LF = Leg(conn, 7, 6, 5)
        self.LM = Leg(conn, 11, 10, 9)
        self.LB = Leg(conn, 15, 14, 13)
        self.RF = Leg(conn, 24, 25, 26)
        self.RM = Leg(conn, 20, 21, 22)
        self.RB = Leg(conn, 16, 17, 18)
        self.neck = Servo(conn, 31)

        self.legs = [
            self.LF, self.LM, self.LB,
            self.RF, self.RM, self.RB
        ]

    def lay(self):
        threads = []
        for leg in self.legs:
            threads.append(leg.lay())
        for t in threads:
            t.start()
        for t in threads:
            t.join()
