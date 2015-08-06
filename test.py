from hexapod import Hexapod
from connection import ConnectionException
import sys


if __name__ == '__main__':
    try:
        hexapod = Hexapod()
    except ConnectionException:
        print("Could not establish a connection")
        sys.exit(1)

    hexapod.lay()

    sys.exit(0)
