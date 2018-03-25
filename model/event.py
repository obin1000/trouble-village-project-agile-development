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

