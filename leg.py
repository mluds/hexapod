from servo import Servo
from threading import Thread


class Leg:
    def __init__(self, serial, hip_id, knee_id, ankle_id,
        hip_os=0, knee_os=0, ankle_os=0):
        self.hip = Servo(serial, hip_id, hip_os)
        self.knee = Servo(serial, knee_id, knee_os)
        self.ankle = Servo(serial, ankle_id, ankle_os)
        self.joints = [
            self.hip, self.knee, self.ankle
        ]

    def lay(self):
        threads = []
        for j in self.joints:
            threads.append(Thread(j.move(0)))
        for t in threads:
            t.start()
        for t in threads:
            t.join()