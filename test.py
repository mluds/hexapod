from hexapod import Hexapod, ConnectionException
import sys


if __name__ == '__main__':
    try:
        hexapod = Hexapod()
    except ConnectionException:
        print("Could not establish a connection")
        sys.exit(1)

    hexapod.walk()
    hexapod.stand()
    hexapod.deactivate()

    sys.exit(0)
