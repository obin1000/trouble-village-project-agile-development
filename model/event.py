# Abstracte weergaven van een dorp
class VillageEvent:
    # Constructor voor Village

    def __init__(self, Status, effect, state):
        self.Stats = Status
        self.effect = effect
        self.state = state

    def getEffect(self):
        return self.effect

    def setEffect(self, effect):
        self.effect = effect

    def getStatus(self):
        return self.Status

    def setState(self, state):
        return self.state

    def getState(self):
        return self.state

bosbrand = "Bosbrand"
overstroming = "Overstroming"

import random
VillageEvent.Status=random.randint(1,100)

if VillageEvent.Status <50:
        print("Status van het dorp: In brand")
        print(bosbrand)
        VillageEvent.state = bosbrand

elif VillageEvent.Status > 50:
        print("Status van het dorp: Overstroomd")
        print(overstroming)
        VillageEvent.state = overstroming
