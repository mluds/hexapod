from serial import SerialTimeoutException


class Servo:
    def __init__(self, serial, id, offset):
        self.serial = serial
        self.id = id
        self.offset = offset

    def move(self, angle):
        pass

    def deactivate(self):
        try:
            self.serial.write("#%dL\r" % self.id)
        except SerialTimeoutException:
            print("Servo %d: Write timeout" % self.id)
