from .servo import Servo
from threading import Thread


class Leg:
    def __init__(self, serial, hip_id, knee_id, ankle_id,
        hip_os=0, knee_os=0, ankle_os=0, is_left=False):
        self.hip = Servo(serial, hip_id, hip_os, is_left)
        self.knee = Servo(serial, knee_id, knee_os)
        self.ankle = Servo(serial, ankle_id, ankle_os)
        self.joints = [
            self.hip, self.knee, self.ankle
        ]

    def center(self):
        for j in self.joints:
            j.set(0)

    def lay(self):
        threads = []
        for j in self.joints:
            threads.append(Thread(j.set(0)))
        for t in threads:
            t.start()
        for t in threads:
            t.join()

    def stand(self):
        threads = []
        threads.append(Thread(self.hip.set(0)))
        threads.append(Thread(self.knee.set(45)))
        threads.append(Thread(self.ankle.set(-45)))
        for t in threads:
            t.start()
        for t in threads:
            t.join()

    def lift(self, n):
        #self.hip.set(self.hip.pos)
        self.knee.move(n)
        #self.ankle.set(self.ankle.pos)

    def shift(self, n):
        self.hip.move(n)
        #self.knee.set(self.ankle.pos)
        #self.ankle.set(self.ankle.pos)
