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

    def getPopulation(self):
        return self.population

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

    def getWater(self):
        return self.water

    def nextTurn(self):
        self.turn += 1
        return self.turn

    def getTurn(self):
        return self.turn
