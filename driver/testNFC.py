#!/usr/bin/python3

import sys
from pirc522 import RFID
import signal
import time

sys.path.insert(0, "/home/pi/pi-rc522/ChipReader")


class NFC:

    def __init__(self):
        rdr = RFID()
        util = rdr.util()
        util.debug = False
        while True:
            # Request tag
            (error, data) = rdr.request()
            if not error:
                print("\nDetected")
                (error, uid) = rdr.anticoll()
                if not error:
                    # Print UID
                    print("Card read UID: " + str(uid[0]) + "," + str(uid[1]) + "," + str(uid[2]) + "," + str(uid[3]))


nnie = NFC()

