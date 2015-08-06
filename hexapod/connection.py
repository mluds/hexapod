from serial.tools.list_ports import comports
from serial import Serial, SerialException, SerialTimeoutException
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
                serial = Serial(port[1], BAUD_RATE, timeout=2, writeTimeout=2)
                serial.write('V\n')
                if "SERVOTOR" in serial.readline():
                    log.info("%s: Connected" % port)
                    self.serial = serial
                    break
            except ValueError:
                log.warning("A serial parameter is out of range")
            except SerialException:
                log.warning("%s: Could not connect" % port[1])
            except SerialTimeoutException:
                log.warning("%s: Write timeout" % port[1])

        if not self.serial:
            raise ConnectionException

        self.lock = Lock()

    def send(self, data):
        self.lock.acquire()
        self.serial.write(data)
        self.lock.release()
