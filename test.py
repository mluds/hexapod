from hexapod import Hexapod, HexapodException
import sys


if __name__ == '__main__':
    try:
        hexapod = Hexapod()
    except HexapodException:
        print("Could not establish a connection")
        sys.exit(1)

    hexapod.lay()

    sys.exit(0)
