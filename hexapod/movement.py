class Movement:
    def __init__(self, servo, angle):
        self.servo = servo
        self.angle = angle
        self.steps = []
    
    def prepare(self):
        self.steps = self.servo.steps(self.angle)
