from hexapod import Hexapod, HexapodException


if __name__ == '__main__':
    try:
        hexapod = Hexapod()
    except HexapodException:
        print("Could not establish a connection")
