from math import copysign


INTERVAL = 100
ZERO_POSITION = 1500
MAX_POSITION = 2500
MIN_POSITION = 500


class Servo:
    def __init__(self, connection, identifier, offset=0, flip=False):
        self.connection = connection
        self.id = identifier
        self.offset = offset
        self.flip = flip
        self.position = self.bound(ZERO_POSITION + offset)
    
    def bound(self, position):
        if position < MIN_POSITION:
            return MIN_POSITION
        elif position > MAX_POSITION:
             return MAX_POSITION
        return position

    def convert(self, angle):
        if self.flip:
            angle *= -1
        raw_position = int(1500.0 + float(angle)*11.1111111)
        return self.bound(raw_position + self.offset)
        
    def set(self, position):
        self.connection.set(self.id, position)
        self.position = position

    def steps(self, angle):
        start = self.position
        finish = self.convert(angle)
        step = int(copysign(INTERVAL, finish-start))
        steps = range(start + step, finish, step)
        steps.append(finish)
        return steps

    def deactivate(self):
        self.connection.deactivate(self.id)
