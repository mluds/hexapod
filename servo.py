from serial import SerialTimeoutException
import logging as log


MIN_POS = 0
MAX_POS = 3000
ZERO_POS = 1500


class Servo:
    def __init__(self, conn, id, offset):
        self.conn = conn
        self.id = id
        self.offset = offset

    def move(self, angle):
        pass

    def deactivate(self):
        try:
            self.conn.send("#%dL\r" % self.id)
        except SerialTimeoutException:
            log.error("Servo %d: Write timeout" % self.id)
