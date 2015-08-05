from servo import Servo

class Leg:
    def __init__(self, serial, hip_id, knee_id, ankle_id):
        self.hip = Servo(serial, hip_id)
        self.knee = Servo(serial, knee_id)
        self.ankle = Servo(serial, ankle_id)

    def stand(self):
        self.hip.set_angle(0)
        self.knee.set_angle(45)
        self.ankle.set_angle(45)