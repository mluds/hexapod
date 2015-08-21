from .connection import Connection
from .servo import Servo
from .leg import Leg
from .mover import Mover
from .movement import Movement
from .config import config
import time


class Hexapod:
    def __init__(self):
        print(config.legs.left.middle)
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
        movements = []
        for leg in self.legs:
            movements.extend(leg.stand())
        stand = Mover(movements)
        stand.prepare()
        stand.run()

    def lift(self, legs, n):
        movements = []
        for leg in legs:
            movements.extend([
                Movement(leg.knee, n),
                Movement(leg.ankle, -90 - n)
            ])
        lift = Mover(movements)
        lift.prepare()
        lift.run()

    def shift(self, legs, n):
        movements = []
        for leg in legs:
            movements.append(Movement(leg.hip, n))
        shift = Mover(movements)
        shift.prepare()
        shift.run()

    def walk(self):
        upangle = -10
        downangle = -45
        rotation = 25

        self.lift(self.tripod1, upangle)
        self.shift(self.tripod2, -rotation)

        for i in range(20):
            for i in [0, 1]:
                self.lift(self.tripods[i], downangle)
                self.lift(self.tripods[1 - i], upangle)

                self.shift(self.tripods[1 - i], rotation)
                self.shift(self.tripods[i], -rotation)
