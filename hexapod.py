from serial.tools.list_ports import comports
from serial import Serial, SerialException, SerialTimeoutException
from leg import Leg
import logging as log


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
                serial = Serial(port[1], BAUD_RATE, timeout=2, writeTimeout=2)
                serial.write('V\n')
                if "SERVOTOR" in serial.readline():
                    log.info("%s: Connected" % port)
                    self.serial = serial
                    self.serial.flush()
                    break
            except ValueError:
                log.warning("A serial parameter is out of range")
            except SerialException:
                log.warning("%s: Could not connect" % port[1])
            except SerialTimeoutException:
                log.warning("%s: Write timeout" % port[1])

        if not self.serial:
            raise HexapodException

        # Initialize legs and neck
        self.LF = Leg(self.serial, 7, 6, 5)
        self.LM = Leg(self.serial, 11, 10, 9)
        self.LB = Leg(self.serial, 15, 14, 13)
        self.RF = Leg(self.serial, 24, 25, 26)
        self.RM = Leg(self.serial, 20, 21, 22)
        self.RB = Leg(self.serial, 16, 17, 18)
        self.neck = Servo(self.serial, 31)

        self.legs = [
            self.LF, self.LM, self.LB,
            self.RF, self.RM, self.RB
        ]

    def lay(self):
        for leg in self.legs:
            leg.stand()
