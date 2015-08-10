from .servo import Servo
from threading import Thread


class Leg:
    def __init__(self, serial, hip_id, knee_id, ankle_id,
        hip_os=0, knee_os=0, ankle_os=0, is_left=False):
        self.hip = Servo(serial, hip_id, hip_os, is_left)
        self.knee = Servo(serial, knee_id, knee_os, True)
        self.ankle = Servo(serial, ankle_id, ankle_os)
        self.joints = [
            self.hip, self.knee, self.ankle
        ]

    def deactivate(self):
        for j in self.joints:
            j.deactivate()

    def zero(self):
        for j in self.joints:
            j.move(0)

    def stand(self):
        self.hip.move(0)
        self.knee.move(-45)
        self.ankle.move(-45)

    def lift(self, n):
        self.knee.move(n)

    def shift(self, n):
        self.hip.move(n)
