from serial.tools.list_ports import comports
from serial import Serial, SerialException
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
                if "SERVOTOR" in result:
                    log.info("Connected on port: %s" % port[0])
                    serial.flush()
                    self.serial = serial
                    break
            except SerialException:
                log.warning("Could not connect on port: %s" % port[0])

        if not self.serial:
            raise ConnectionException

    def deactivate(self, servo_id):
        self.serial.write("#%dL\r" % servo_id)

    def set(self, servo_id, position):
        self.serial.write("#%dP%.4dT0\r" % (servo_id, position))
