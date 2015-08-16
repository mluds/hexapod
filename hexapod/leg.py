from .servo import Servo
from .movement import Movement


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
            j.set(0)

    def stand(self):
        return [
            Movement(self.hip, 0),
            Movement(self.knee, -45),
            Movement(self.ankle, -45)
        ]
