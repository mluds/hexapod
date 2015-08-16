from hexapod import Hexapod, ConnectionException
import sys
import time


if __name__ == '__main__':
    try:
        hexapod = Hexapod()
    except ConnectionException:
        print("Could not establish a connection")
        sys.exit(1)

    hexapod.stand()
    time.sleep(8)
    hexapod.walk()
    
    hexapod.deactivate()

    sys.exit(0)
