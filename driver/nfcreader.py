#!/usr/bin/python3

from driver.nfchelp.rfid import RFID
import threading
from model.scene import *
from time import sleep


class NFC(threading.Thread):

    # Make the thread and give it a name
    def __init__(self, name, dorp, troublevillage):
        threading.Thread.__init__(self)
        self.dorp = dorp
        self.troublevillage = troublevillage
        self.name = name
        self.rdr = RFID()
        self.util = self.rdr.util()
        self.util.debug = False

    def run(self):
        while True:
            # Keeps cpu usage low
            sleep(0.2)
            # Request tag
            (error, data) = self.rdr.request()
            if not error:
                (error, uid) = self.rdr.anticoll()
                if not error:
                    self.checkCard(uid)
                    sleep(4)

    def arrayToString(self, array):
        return ''.join(str(e) for e in array)

    def checkCard(self, uid):
        card = self.arrayToString(uid)
        if card == "25213744934": # waterkaart
            self.dorp.addWater(100)
            self.troublevillage.nextTurn()
        elif card == "2529811922152": # houtkaart
            self.dorp.addWood(100)
            self.troublevillage.nextTurn()
        elif card == "68169399106": # bosbrandkaart
            self.dorp.setState(1)
            self.troublevillage.nextTurn()
        elif card == "180439599163": # overstromingkaart
            self.dorp.setState(2)
            self.troublevillage.nextTurn()
        elif card == "25061219217197": # well
            print("building well")
        elif card == "18824821821771": # stockpile
            print("buidling stockpile")

