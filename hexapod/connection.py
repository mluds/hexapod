from serial.tools.list_ports import comports
from serial import Serial
from threading import Lock
import logging as log


BAUD_RATE = 9600


class ConnectionException(Exception):
    pass


class Connection:
    def __init__(self):
        self.serial = None

        for port in comports():
            try:
                serial = Serial(port[0], baudrate=BAUD_RATE, timeout=2)
                serial.write('V\n')
                result = serial.readline()
                print result
                if "SERVOTOR" in result:
                    print "Connect Successful! Connected on port:", port
                    self.serial = serial
                    self.serial.flush()
                    break
            except Exception as e:
                    print type(e)
                    print e.args

        if not self.serial:
            raise ConnectionException

    def deactivate(self, servo_id):
        self.serial.write("#%dL\r" % servo_id)

    def set(self, servo_id, position):
        self.serial.write("#%dP%.4dT0\r" % (servo_id, position))
