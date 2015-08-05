from serial.tools.list_ports import comports
from serial import Serial, SerialException, SerialTimeoutException
from leg import Leg


BAUD_RATE = 9600


# Thrown when a connection cannot be established
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
                if "SERVOTOR" in serial.readline():
                    print("Connected on port {}", port)
                    self.serial = serial
                    self.serial.flush()
                    break
            except ValueError:
                print("A serial parameter is out of range")
            except SerialException:
                print("%s: Could not connect to serial device" % port[1])
            except SerialTimeoutException:
                print("%s: Serial device timed out while writing data" % port[1])

        if not self.serial:
            raise HexapodException

        # Initialize legs and neck
        self.LF = Leg(self.serial, 7, 6, 5)
        self.LM = Leg(self.serial, 11, 10, 9)
        self.LB = Leg(self.serial, 15, 14, 13)
        self.RF = Leg(self.serial, 24, 25, 26)
        self.RM = Leg(self.serial, 20, 21, 22)
        self.RB = Leg(self.serial, 16, 17, 18)
