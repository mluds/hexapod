from serial import SerialTimeoutException
import logging as log


class Servo:
    def __init__(self, conn, id, offset):
        self.conn = conn
        self.id = id
        self.offset = offset
        self.pos = 1500

    def set(self, angle):
        pos = int(1500.0 + float(angle)*11.1111111) + self.offset

        if pos < 500:
            pos = 500
        elif pos > 2500:
            pos = 2500

        self.conn.send("#%dP%.4dT0\r" % (self.id, pos))

    def move(self, angle):
        pass

    def deactivate(self):
        try:
            self.conn.send("#%dL\r" % self.id)
        except SerialTimeoutException:
            log.error("Servo %d: Write timeout" % self.id)
