from collections import deque


class Movement:
    def __init__(self, servo, angle):
        self.servo = servo
        self.angle = angle
        self.steps = deque()
    
    def prepare(self):
        self.steps = deque(self.servo.steps(self.angle))
