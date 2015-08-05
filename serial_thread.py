from threading import Thread, Lock
from serial.tools.list_ports import comports
from serial import Serial

BAUD_RATE = 9600

class SerialThread(Thread):

    def __init__(self):
        self.send = []
        self.receive = []
        self.send_lock = Lock()
        self.receive_lock = Lock()
        self.is_open = False
        self.n = 0

    def run(self):
        self.connect()
        while (True):
            send = False
            if self.send:
                self.send_lock.acquire()
                to_send = self.send.pop(0)
                self.send_lock.release()
                send = True

    def connect(self):
        for port in comports():
            try:
                serial = Serial(port[1], BAUD_RATE, timeout=2)
                serial.write('V\n')
                result = serial.readline()
                if "SERVOTOR" in serial.readline():
                    print("Connected on port {}", port)
                    self.serial = serial
                    self.serial.flush()
                    self.is_open = True
                    self.n = 1
                    break
            except ValueError:
                print("A serial parameter is out of range")
            except SerialException:
                print("Serial device either cannot be found or be configured")
            except SerialTimeoutException:
                print("Serial connection timed out while writing data")
