#!/usr/bin/python3

from driver.nfchelp.rfid import RFID
import threading
from time import sleep


class NFC(threading.Thread):

    #Make the thread and give it a name
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.rdr = RFID()
        self.util = self.rdr.util()
        self.util.debug = False


    def run(self):
        while True:
            #Keeps cpu usage low
            sleep(1)
            # Request tag
            (error, data) = self.rdr.request()
            if not error:
                (error, uid) = self.rdr.anticoll()
                if not error:
                    # Print card value
                    print("Card read UID: " + str(uid[0]) + "," + str(uid[1]) + "," + str(uid[2]) + "," + str(uid[3]))

