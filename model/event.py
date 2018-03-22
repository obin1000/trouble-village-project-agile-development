# Abstracte weergaven van een dorp
class VillageEvent:
    # Constructor voor Village

    def __init__(self, Status, effect):
        self.Stats = Status
        self.effect = effect

    def getEffect(self):
        return self.effect

    def setEffect(self, effect):
        self.effect = effect

    def getStatus(self):
        return self.Status

import random
VillageEvent.Status=random.randint(1,100)
if VillageEvent.Status > 33 and VillageEvent.Status < 66 :
        print("Status van het dorp: In brand")
elif VillageEvent.Status > 66:
        print("Status van het dorp: Onder water")
elif VillageEvent.Status < 33:
        print("Status van het dorp: Overstroomd")