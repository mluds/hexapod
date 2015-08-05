from servo import Servo

class Leg:
    def __init__(self, serial, hip_id, knee_id, ankle_id, is_active=True):
        self.hip = Servo(hip_id)
        self.knee = Servo(knee_id)
        self.ankle = Servo(ankle_id)