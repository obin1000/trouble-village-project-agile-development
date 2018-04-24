#!/usr/bin/python3

from driver.nfchelp.rfid import RFID
import threading
from model.event import *
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
        if card == "25213744934":  # waterkaart
            self.dorp.addWater(200)
            self.troublevillage.nextTurn()
        elif card == "2529811922152":  # houtkaart
            self.dorp.addWood(200)
            self.troublevillage.nextTurn()
        elif card == "68169399106":  # bosbrandkaart
            Burn(self.dorp,self.troublevillage)
            self.troublevillage.nextTurn()
        elif card == "180439599163":  # overstromingkaart
            Flood(self.dorp,self.troublevillage)
            self.troublevillage.nextTurn()
        elif card == "164989799196":  # populatie kaart
            self.dorp.addPopulation(50)
            self.troublevillage.update()
        elif card == "124173115221127":     # dode kaart
            self.dorp.lowerPopulation(30)
            self.troublevillage.update()
        elif card == "25061219217197":  # wellbuilding
            self.dorp.buildWell()
            self.troublevillage.update()
        elif card == "18824821821771":  # stockpilebuilding
            self.dorp.buildStockpile()
            self.troublevillage.update()

    def testCard(self):
            Burn(self.dorp,self.troublevillage)
            self.troublevillage.nextTurn()
        

