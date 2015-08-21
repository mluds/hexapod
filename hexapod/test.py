from .hexapod import Hexapod
from .connection import ConnectionException
import sys
import time


def run():
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
