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

    def getImage(self):
        villageImg = "404"
        if self.state == 0:
            villageImg = "img/Base.gif"
        elif self.state == 1:
            villageImg = "img/Fire.gif"
        elif self.state == 2:
            villageImg = "img/giphy.gif"
        elif self.state == 3:
            villageImg = "img/giphy.gif"
        return villageImg

    def setPopulation(self, population):
        self.population = population
        if(self.population < 0):
            print("Game over!")
            self.population = 0

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

    #for next turn use the one in scene
    def nextTurn(self):
        if(self.population > 0):
            self.turn += 1
            return self.turn

    def getTurn(self):
        return self.turn
