# Abstracte weergaven van een dorp
class Village:
    # Constructor voor Village
    def __init__(self, name, population, wood, water, players):
        self.name = name
        self.population = population
        self.wood = wood
        self.water = water
        self.players = players
        self.turn = 0
        self.state = 0

    def getPopulation(self):
        return self.population

    # 0 = default; 1 = burning; 2 = flood;
    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state
        return self.state

    def setPopulation(self, population):
        self.population = population

    def getName(self):
        return self.name

    def setWood(self, wood):
        self.wood = wood

    def getWood(self):
        return self.wood

    def setWater(self, water):
        self.water = water
        if(self.water < 0):
            self.water = 0

    def getWater(self):
        return self.water

    def nextTurn(self):
        self.turn += 1
        return self.turn

    def getTurn(self):
        return self.turn
