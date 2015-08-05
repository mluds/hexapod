from serial.tools.list_ports import comports
from serial import Serial
from leg import Leg


BAUD_RATE = 9600


class HexapodException(Exception):
    pass


class Hexapod:

    def __init__(self):

        # Try to establish a serial connection
        self.serial = None

        for port in comports():
            try:
                serial = Serial(port[1], BAUD_RATE, timeout=2)
                serial.write('V\n')
            except ValueError:
                print("A serial parameter is out of range")
            except SerialException:
                print("{}: Serial device either cannot be found or be configured", port[1])
            except SerialTimeoutException:
                print("{}: Serial connection timed out while writing data", port[1])

            if "SERVOTOR" in serial.readline():
                print("Connected on port {}", port)
                self.serial = serial
                self.serial.flush()
                break

        if not self.serial:
            raise HexapodException

        # Initialize legs and neck
        self.LF = Leg(self.serial, 7, 6, 5)
        self.LM = Leg(self.serial, 11, 10, 9)
        self.LB = Leg(self.serial, 15, 14, 13)
        self.RF = Leg(self.serial, 24, 25, 26)
        self.RM = Leg(self.serial, 20, 21, 22)
        self.RB = Leg(self.serial, 16, 17, 18)
