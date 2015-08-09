import serial.tools.list_ports
import serial
from threading import Lock
import logging as log


BAUD_RATE = 9600


class ConnectionException(Exception):
    pass


class Connection:
    def __init__(self):

        self.ser = None

        comList = []
        comports = serial.tools.list_ports.comports()
        for comport in comports:
                for thing in comport:
                        #print thing
                        comList.append(thing)
        
        comList = list(set(comList))
        print "Attempting to connect to Servotor"
        for port in comList:
                try:
                        ser = serial.Serial(port, baudrate= BAUD_RATE, timeout=2)
                        ser.write('V\n')
                        result = ser.readline()
                        if "SERVOTOR" in result:
                                print "Connect Successful! Connected on port:",port
                                self.ser = ser
                                self.ser.flush()
                                self.serOpen = True
                                self.serNum = 1
                                break
                except:
                        pass
        if self.serOpen == False:
            print "Trying Windows Method"
            for i in range(1,100):
                try:
                    try:
                        ser = serial.Serial(i, baudrate=BAUD_RATE, timeout=1)
                        #print "ser",i
                    except:
                        #print "ser",i,"failed"
                        raise Exception
                    ser.flush()
                    time.sleep(0.1)
                    ser.write("V\n")
                    time.sleep(1)
                    readReply = ser.readline()
                    #print "read:",readReply
                    if "SERVOTOR" in readReply:
                        print "Connect Successful! Connected on port COM"+str(i+1)
                        ser.flush()
                        self.ser = ser
                        self.serNum = i
                        self.serOpen = True
                        break
                    else:
                        ser.close()
                        pass
                except:
                    pass

        if not self.ser:
            raise ConnectionException

        self.lock = Lock()

    def send(self, data):
        self.lock.acquire()
        self.ser.write(data)
        self.lock.release()
